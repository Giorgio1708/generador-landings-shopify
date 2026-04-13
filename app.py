import streamlit as st
import tempfile
import os
import sys
from pathlib import Path
from PIL import Image

# ── Configuración de página ───────────────────────────────────────────────────
st.set_page_config(
    page_title="Generador de Landings",
    page_icon="🚀",
    layout="centered",
)

st.markdown("""
<style>
  .block-container { max-width: 680px; padding-top: 2rem; }
  .stButton > button { width: 100%; font-size: 1.1rem; padding: 0.6rem; }
  .fase-img { border-radius: 8px; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

# ── Inicializar estado ────────────────────────────────────────────────────────
defaults = {
    "step": "input",          # input | phase1 | generating | done
    "img_path": None,
    "product_info": {},
    "phase1_path": None,
    "all_images": {},
    "shopify_url": None,
    "feedback": "",
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


def reset():
    for k, v in defaults.items():
        st.session_state[k] = v
    st.rerun()


# ── Importar módulos del proyecto ─────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
from generators.product_analyzer import analyze_product_image
from generators.image_generator import ImageGenerator
from generators.prompt_builder import build_prompt
from models.product_input import ProductInput
from shopify.product import create_shopify_product
from config.settings import OUTPUT_DIR


def _build_product(info: dict, img_path: str) -> ProductInput:
    return ProductInput(
        imagen_path=img_path,
        nombre=info["nombre"],
        beneficios=info["beneficios"],
        uso=info["uso"],
        color_hex=info.get("color_hex", "#1565C0"),
        precio_normal=info["precio_normal"],
        precio_oferta=info["precio_oferta"],
        angulo_venta=info["angulo_venta"],
        fuente=info.get("fuente", "Poppins"),
    )


# ══════════════════════════════════════════════════════════════════════════════
# PASO 1 — Formulario de entrada
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.step == "input":

    st.title("🚀 Generador de Landings")
    st.caption("Sube el producto, escribe el ángulo de venta y nosotros hacemos el resto.")

    uploaded = st.file_uploader(
        "Imagen del producto",
        type=["jpg", "jpeg", "png", "webp"],
        help="Foto del frasco, caja o empaque del producto",
    )

    if uploaded:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(uploaded, use_container_width=True)
        with col2:
            st.success(f"✓ {uploaded.name}")

    angulo = st.text_area(
        "Ángulo de venta",
        placeholder="¿A quién va dirigido? ¿Cuál es su dolor principal?\n\nEj: Mujeres mayores de 35 que sufren insomnio y calambres nocturnos y buscan un suplemento natural que les devuelva la energía.",
        height=120,
    )

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        precio_normal = st.text_input("Precio normal", placeholder="89.900")
    with col_p2:
        precio_oferta = st.text_input("Precio oferta", placeholder="59.900")

    skip_shopify = st.checkbox("Solo generar imágenes (no subir a Shopify)")

    st.divider()

    if st.button("🚀 GENERAR LANDING", type="primary", disabled=not uploaded):
        if not angulo.strip():
            st.error("Escribe el ángulo de venta antes de continuar.")
            st.stop()
        if not precio_normal.strip() or not precio_oferta.strip():
            st.error("Completa los precios.")
            st.stop()

        # Guardar imagen temporalmente
        suffix = Path(uploaded.name).suffix
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        tmp.write(uploaded.getbuffer())
        tmp.close()
        st.session_state.img_path = tmp.name

        # Analizar producto con Gemini
        with st.spinner("Analizando producto con Gemini..."):
            try:
                info = analyze_product_image(st.session_state.img_path)
            except Exception as e:
                st.error(f"Error al analizar imagen: {e}")
                st.stop()

        st.session_state.product_info = {
            "nombre": info.get("nombre", "Producto"),
            "beneficios": info.get("beneficios", ""),
            "uso": info.get("uso", ""),
            "color_hex": info.get("color_hex", "#1565C0"),
            "fuente": "Poppins",
            "angulo_venta": angulo,
            "precio_normal": precio_normal,
            "precio_oferta": precio_oferta,
            "skip_shopify": skip_shopify,
        }

        # Generar Fase 1
        with st.spinner("Generando portada (Fase 1)..."):
            product = _build_product(st.session_state.product_info, st.session_state.img_path)
            output_dir = Path(OUTPUT_DIR) / product.slug
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = str(output_dir / "fase_1.png")

            try:
                gen = ImageGenerator()
                prompt = build_prompt(1, product)
                gen.generate(prompt, output_path, st.session_state.img_path)
                st.session_state.phase1_path = output_path
                st.session_state.all_images[1] = output_path
                st.session_state.step = "phase1"
                st.rerun()
            except Exception as e:
                st.error(f"Error generando imagen: {e}")


# ══════════════════════════════════════════════════════════════════════════════
# PASO 2 — Revisión Fase 1 (Portada)
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == "phase1":

    info = st.session_state.product_info
    st.title("🖼️ Revisa la Portada")
    st.caption(f"Producto detectado: **{info['nombre']}** · Color: `{info['color_hex']}`")

    if st.session_state.phase1_path:
        st.image(st.session_state.phase1_path, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Aprobar — generar las 6 secciones", type="primary"):
            st.session_state.step = "generating"
            st.rerun()

    with col2:
        if st.button("🔄 Regenerar portada"):
            st.session_state.step = "regenerating"
            st.rerun()

    feedback = st.text_input(
        "Feedback para regenerar (opcional)",
        placeholder="ej: más dramático en el ANTES, cambiar fondo a negro...",
    )
    if feedback:
        st.session_state.feedback = feedback

    if st.button("↩️ Volver a empezar"):
        reset()


# ══════════════════════════════════════════════════════════════════════════════
# PASO 2b — Regenerar Fase 1 con feedback
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == "regenerating":
    with st.spinner("Regenerando portada..."):
        product = _build_product(st.session_state.product_info, st.session_state.img_path)
        output_path = st.session_state.phase1_path
        try:
            gen = ImageGenerator()
            prompt = build_prompt(1, product, feedback=st.session_state.feedback)
            gen.generate(prompt, output_path, st.session_state.img_path)
            st.session_state.all_images[1] = output_path
            st.session_state.feedback = ""
            st.session_state.step = "phase1"
            st.rerun()
        except Exception as e:
            st.error(f"Error regenerando: {e}")
            st.session_state.step = "phase1"
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# PASO 3 — Generar fases 2-8 y subir a Shopify
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == "generating":

    info = st.session_state.product_info
    product = _build_product(info, st.session_state.img_path)
    output_dir = Path(OUTPUT_DIR) / product.slug

    st.title("⚙️ Generando landing...")

    progress = st.progress(1 / 6, text="Fase 1 lista")
    gen = ImageGenerator()

    for fase_num in range(2, 7):
        progress.progress(fase_num / 6, text=f"Generando sección {fase_num} de 6...")
        output_path = str(output_dir / f"fase_{fase_num}.png")
        try:
            prompt = build_prompt(fase_num, product)
            gen.generate(prompt, output_path, st.session_state.img_path)
            st.session_state.all_images[fase_num] = output_path
        except Exception as e:
            st.warning(f"Fase {fase_num} falló: {e}")

    progress.progress(1.0, text="Imagenes listas")

    # Subir a Shopify
    if not info.get("skip_shopify"):
        with st.spinner("Subiendo a Shopify..."):
            try:
                url = create_shopify_product(product, st.session_state.all_images)
                st.session_state.shopify_url = url
            except Exception as e:
                st.warning(f"Error en Shopify: {e}")

    st.session_state.step = "done"
    st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# PASO 4 — Resultado final
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.step == "done":

    info = st.session_state.product_info
    st.title("✅ Landing generada")
    st.caption(f"**{info['nombre']}**")

    if st.session_state.shopify_url:
        st.success(f"Producto en Shopify (draft): {st.session_state.shopify_url}")
        st.link_button("Ver en Shopify Admin", st.session_state.shopify_url)

    st.divider()

    # Mostrar todas las imágenes
    fase_nombres = {
        1: "Portada",
        2: "Infografía de Beneficios",
        3: "Características Técnicas",
        4: "Garantías",
        5: "Preguntas Frecuentes",
        6: "Testimonios",
    }

    for fase_num, path in sorted(st.session_state.all_images.items()):
        if Path(path).exists():
            st.subheader(f"Fase {fase_num} — {fase_nombres.get(fase_num, '')}")
            st.image(path, use_container_width=True)

    st.divider()
    if st.button("🆕 Generar otro producto", type="primary"):
        reset()


