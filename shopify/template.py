import json
import re
from shopify.client import ShopifyClient
from shopify.review_generator import generate_reviews

LANDING_SECTION_KEY = "sections/landing-imagenes.liquid"

LANDING_SECTION_LIQUID = """{%- if section.settings.image_url != blank -%}
<div style="margin:0;padding:0;line-height:0;font-size:0;">
  <img
    src="{{ section.settings.image_url }}"
    alt="{{ section.settings.image_alt | default: '' }}"
    style="width:100%;display:block;"
    loading="lazy"
  >
</div>
{%- endif -%}

{% schema %}
{
  "name": "Landing Imagen",
  "settings": [
    {
      "type": "text",
      "id": "image_url",
      "label": "URL de la imagen"
    },
    {
      "type": "text",
      "id": "image_alt",
      "label": "Texto alternativo"
    }
  ],
  "presets": [{"name": "Landing Imagen"}]
}
{% endschema %}"""

# ID del bloque EasySell extraído de plantilla-ia
EASYSELL_BLOCK_ID = "easysell_cod_form_app_block_F6x3md"
EASYSELL_BLOCK_TYPE = "shopify://apps/easysell-cod-form/blocks/app-block/7bfd0a95-6839-4f02-b2ee-896832dbe67e"


def get_active_theme_id(client: ShopifyClient) -> int:
    themes = client.get("/themes.json")
    for theme in themes["themes"]:
        if theme["role"] == "main":
            return theme["id"]
    raise RuntimeError("No se encontro un tema activo en Shopify")


def ensure_landing_section(client: ShopifyClient, theme_id: int) -> None:
    """Sube la seccion landing-imagenes.liquid al tema si no existe o la actualiza."""
    client.put_asset(theme_id, LANDING_SECTION_KEY, LANDING_SECTION_LIQUID)


def create_product_template(
    client: ShopifyClient,
    theme_id: int,
    product_slug: str,
    image_urls: dict,
    info_producto: str = "",
    color_hex: str = "#F5A623",
) -> str:
    """
    Crea un template JSON de producto con las imagenes generadas y 20 reseñas IA.
    Estructura: fase_1 → formulario COD → fases 2-6 → reseñas
    Retorna el template_suffix asignado al producto.
    """
    suffix = "landing-" + re.sub(r"[^a-z0-9\-]", "-", product_slug.lower())[:40]
    template_key = f"templates/product.{suffix}.json"

    sections = {}
    order = []

    # Fase 1 — portada (antes del formulario)
    if 1 in image_urls:
        sections["landing_fase_1"] = {
            "type": "landing-imagenes",
            "settings": {"image_url": image_urls[1], "image_alt": "Portada"},
        }
        order.append("landing_fase_1")

    # Formulario EasySell COD
    sections["cod_form"] = {
        "type": "apps",
        "blocks": {
            EASYSELL_BLOCK_ID: {
                "type": EASYSELL_BLOCK_TYPE,
                "settings": {"product": ""},
            }
        },
        "block_order": [EASYSELL_BLOCK_ID],
        "settings": {"include_margins": True},
    }
    order.append("cod_form")

    # Fases 2-6 debajo del formulario
    for fase_num in range(2, 7):
        if fase_num in image_urls:
            sec_id = f"landing_fase_{fase_num}"
            sections[sec_id] = {
                "type": "landing-imagenes",
                "settings": {
                    "image_url": image_urls[fase_num],
                    "image_alt": f"Sección {fase_num}",
                },
            }
            order.append(sec_id)

    # Sección de reseñas generadas por IA
    if info_producto:
        reviews = generate_reviews(info_producto)
        _add_reviews_section(sections, order, reviews, color_hex)

    template_content = json.dumps(
        {"sections": sections, "order": order},
        indent=2,
        ensure_ascii=False,
    )

    client.put_asset(theme_id, template_key, template_content)
    return suffix


def _add_reviews_section(
    sections: dict,
    order: list,
    reviews: list,
    color_hex: str,
) -> None:
    """Agrega la sección de reviews-buider con 20 bloques generados por IA."""

    # Contar distribución de estrellas para el resumen
    dist = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
    for r in reviews:
        stars = int(r.get("rating", 5))
        dist[stars] = dist.get(stars, 0) + 1

    # Construir bloques
    blocks = {}
    block_order = []
    for i, review in enumerate(reviews):
        block_id = f"review_{i + 1}"
        blocks[block_id] = {
            "type": "review",
            "settings": {
                "initials": review.get("initials", "CL"),
                "name": review.get("name", "Cliente"),
                "verified": True,
                "verified_text": "Compra Verificada",
                "time_ago": review.get("time_ago", "hace 1 mes"),
                "rating": int(review.get("rating", 5)),
                "text": review.get("text", ""),
            },
        }
        block_order.append(block_id)

    sections["customer_reviews"] = {
        "type": "reviews-buider",
        "settings": {
            "title": "Lo que dicen nuestros clientes",
            "title_size": 22,
            "dist_5": dist[5],
            "dist_4": dist[4],
            "dist_3": dist[3],
            "dist_2": dist[2],
            "dist_1": dist[1],
            "show_photo_grid": False,
            "photo_grid_limit": 6,
            "accent": color_hex,
            "bg": "#FFFFFF",
            "text": "#111111",
            "verified_icon": "#16a34a",
            "max_width": 520,
            "padding_y": 24,
            "padding_x": 16,
        },
        "blocks": blocks,
        "block_order": block_order,
    }
    order.append("customer_reviews")


def assign_template_to_product(
    client: ShopifyClient, product_id: int, template_suffix: str
) -> None:
    """Asigna el template al producto via template_suffix."""
    client.put(
        f"/products/{product_id}.json",
        {"product": {"id": product_id, "template_suffix": template_suffix}},
    )
