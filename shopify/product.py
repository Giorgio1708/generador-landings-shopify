import base64
import time
from pathlib import Path

from models.product_input import ProductInput
from shopify.client import ShopifyClient
from shopify.metafields import set_landing_metafields
from shopify.template import (
    get_active_theme_id,
    ensure_landing_section,
    create_product_template,
    assign_template_to_product,
)


def create_shopify_product(product: ProductInput, generated_images: dict) -> str:
    """
    Crea un producto en Shopify (como draft), sube las imagenes, configura
    metafields, crea el template de landing y lo asigna al producto.
    Devuelve la URL del producto en el admin de Shopify.
    """
    client = ShopifyClient()

    # 1. Crear el producto
    body_html = _build_description(product)
    response = client.post(
        "/products.json",
        {
            "product": {
                "title": product.nombre,
                "body_html": body_html,
                "status": "draft",
                "tags": "landing-auto",
            }
        },
    )
    product_id = response["product"]["id"]

    # 2. Subir imagenes como adjuntos base64
    image_urls = {}
    for fase_num in sorted(generated_images.keys()):
        image_path = generated_images[fase_num]
        url = _upload_image(client, product_id, fase_num, image_path)
        if url:
            image_urls[fase_num] = url
        time.sleep(0.5)

    # 3. Metafields
    set_landing_metafields(
        client,
        product_id,
        image_urls,
        product.color_hex,
        product.angulo_venta,
    )

    # 4. Crear template de landing en el tema activo y asignarlo al producto
    theme_id = get_active_theme_id(client)
    ensure_landing_section(client, theme_id)
    template_suffix = create_product_template(
        client,
        theme_id,
        product.slug,
        image_urls,
        info_producto=product.info_producto,
        color_hex=product.color_hex,
    )
    assign_template_to_product(client, product_id, template_suffix)

    store = client.base_url.split("/admin")[0].replace("https://", "")
    return f"https://{store}/admin/products/{product_id}"


def _upload_image(
    client: ShopifyClient, product_id: int, fase_num: int, image_path: str
) -> str | None:
    with open(image_path, "rb") as f:
        attachment = base64.b64encode(f.read()).decode("utf-8")

    filename = Path(image_path).name
    response = client.post(
        f"/products/{product_id}/images.json",
        {
            "image": {
                "attachment": attachment,
                "filename": filename,
                "position": fase_num,
                "alt": f"Landing - Fase {fase_num}",
            }
        },
    )
    return response.get("image", {}).get("src")


def _build_description(product: ProductInput) -> str:
    return (
        f"<h2>{product.nombre}</h2>"
        f"<p>{product.angulo_venta}</p>"
        f"<h3>Beneficios</h3>"
        f"<p>{product.beneficios}</p>"
        f"<h3>Modo de uso</h3>"
        f"<p>{product.uso}</p>"
    )
