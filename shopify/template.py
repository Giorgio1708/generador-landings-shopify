import json
import re
from shopify.client import ShopifyClient

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
) -> str:
    """
    Crea un template JSON de producto con las imagenes generadas.
    Estructura: fase_1 → formulario COD → fases 2-8
    Retorna el template_suffix asignado al producto.
    """
    # Sanitizar slug para usar como sufijo de template
    suffix = "landing-" + re.sub(r"[^a-z0-9\-]", "-", product_slug.lower())[:40]
    template_key = f"templates/product.{suffix}.json"

    sections = {}
    order = []

    # Fase 1 antes del formulario de compra
    if 1 in image_urls:
        sections["landing_fase_1"] = {
            "type": "landing-imagenes",
            "settings": {
                "image_url": image_urls[1],
                "image_alt": "Portada",
            },
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

    # Fases 2-8 debajo del formulario
    for fase_num in range(2, 9):
        if fase_num in image_urls:
            sec_id = f"landing_fase_{fase_num}"
            sections[sec_id] = {
                "type": "landing-imagenes",
                "settings": {
                    "image_url": image_urls[fase_num],
                    "image_alt": f"Fase {fase_num}",
                },
            }
            order.append(sec_id)

    template_content = json.dumps(
        {"sections": sections, "order": order},
        indent=2,
        ensure_ascii=False,
    )

    client.put_asset(theme_id, template_key, template_content)
    return suffix


def assign_template_to_product(
    client: ShopifyClient, product_id: int, template_suffix: str
) -> None:
    """Asigna el template al producto via template_suffix."""
    client.put(
        f"/products/{product_id}.json",
        {"product": {"id": product_id, "template_suffix": template_suffix}},
    )
