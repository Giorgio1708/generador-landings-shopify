"""
Generador de prompts especializados por fase.

Flujo:
  1. Toma el template base (estructura/instrucciones) + info del producto
  2. Llama a gemini-2.5-flash con la imagen del producto para generar
     un prompt de imagen ultra-específico y adaptado al producto real
  3. Devuelve ese prompt generado para que image_generator lo ejecute

Esto replica el flujo original: "el Gem generaba el prompt → se pegaba en otra
conversación con Gemini imagen" — pero de forma completamente automatizada.
"""

import mimetypes
import re

from google import genai
from google.genai import types

from config.settings import GEMINI_API_KEY
from generators.templates import TEMPLATES, FASE_NOMBRES
from models.product_input import ProductInput


_META_INSTRUCCION = """Eres un experto en diseño de e-commerce y redactor de prompts para generadores de imágenes IA.

Tu tarea es generar UN SOLO prompt de imagen fotorrealista, extremadamente específico y detallado, basado en:
1. La plantilla de estructura que recibes (define el layout, secciones y elementos requeridos)
2. La imagen real del producto (imagen adjunta)
3. La información del producto proporcionada

REGLAS ABSOLUTAS:
- El prompt resultante debe describir EXACTAMENTE este producto específico, no un producto genérico
- Menciona características visuales reales del empaque: colores, forma del frasco, etiqueta, tipografía, tamaño
- Adapta CADA elemento de texto de la plantilla al producto real (beneficios reales, modo de uso real, nombre real)
- El prompt debe estar en español
- NO escribas explicaciones ni comentarios — devuelve ÚNICAMENTE el prompt final
- El prompt debe ser ejecutable directamente en un modelo de generación de imágenes
- Formato vertical 9:16 siempre
- Máximo 600 palabras en el prompt

PLANTILLA DE ESTRUCTURA (lo que debes construir):
{TEMPLATE}

INFORMACIÓN DEL PRODUCTO:
Nombre: {NOMBRE}
Ángulo de venta: {ANGULO_VENTA}
Beneficios: {BENEFICIOS}
Modo de uso: {USO}
Color de marca: {COLOR_HEX}
Precio normal: {PRECIO_NORMAL}
Precio oferta: {PRECIO_OFERTA}
Fuente tipográfica: {FUENTE}

Genera el prompt ahora:"""


def generate_specialized_prompt(
    fase: int,
    product: ProductInput,
    product_image_path: str,
    feedback: str = "",
) -> str:
    """
    Usa gemini-2.5-flash (multimodal) para generar un prompt de imagen
    ultra-específico para la fase indicada, basado en el producto real.
    """
    client = genai.Client(api_key=GEMINI_API_KEY)

    with open(product_image_path, "rb") as f:
        image_data = f.read()

    mime_type, _ = mimetypes.guess_type(product_image_path)
    if not mime_type:
        mime_type = "image/jpeg"

    template = TEMPLATES[fase]

    meta_prompt = _META_INSTRUCCION.format(
        TEMPLATE=template,
        NOMBRE=product.nombre,
        ANGULO_VENTA=product.angulo_venta,
        BENEFICIOS=product.beneficios,
        USO=product.uso,
        COLOR_HEX=product.color_hex,
        PRECIO_NORMAL=product.precio_normal,
        PRECIO_OFERTA=product.precio_oferta,
        FUENTE=product.fuente,
    )

    if feedback:
        meta_prompt = (
            f"IMPORTANT — User feedback to apply in this iteration: {feedback}\n\n"
            + meta_prompt
        )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(data=image_data, mime_type=mime_type),
            types.Part.from_text(text=meta_prompt),
        ],
    )

    prompt = response.text.strip()
    # Elimina bloques markdown si el modelo los devuelve
    prompt = re.sub(r"^```[a-z]*\n?", "", prompt)
    prompt = re.sub(r"\n?```$", "", prompt)
    return prompt
