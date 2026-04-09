from shopify.client import ShopifyClient


def set_landing_metafields(
    client: ShopifyClient,
    product_id: int,
    image_urls: dict,
    color_hex: str,
    angulo_venta: str,
) -> None:
    """Crea metafields en el producto para que el tema de Shopify pueda renderizar la landing."""

    metafields = []

    for fase_num, url in image_urls.items():
        metafields.append({
            "namespace": "landing",
            "key": f"fase_{fase_num}",
            "value": url,
            "type": "url",
        })

    metafields.append({
        "namespace": "landing",
        "key": "color_marca",
        "value": color_hex,
        "type": "single_line_text_field",
    })

    metafields.append({
        "namespace": "landing",
        "key": "angulo_venta",
        "value": angulo_venta,
        "type": "multi_line_text_field",
    })

    for mf in metafields:
        client.post(
            f"/products/{product_id}/metafields.json",
            {"metafield": mf},
        )
