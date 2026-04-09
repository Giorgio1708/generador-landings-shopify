from generators.templates import TEMPLATES
from models.product_input import ProductInput


def build_prompt(fase: int, product: ProductInput, feedback: str = "") -> str:
    template = TEMPLATES[fase]

    prompt = template.replace("{COLOR_HEX}", product.color_hex)
    prompt = prompt.replace("{PRECIO_NORMAL}", product.precio_normal)
    prompt = prompt.replace("{PRECIO_OFERTA}", product.precio_oferta)
    prompt = prompt.replace("{FUENTE}", product.fuente)
    prompt = prompt.replace("{INFO_PRODUCTO}", product.info_producto)
    prompt = prompt.replace("{ANGULO_VENTA}", product.angulo_venta)

    if feedback:
        prompt = (
            f"FEEDBACK DE REVISIÓN (aplicar en esta regeneración): {feedback}\n\n"
            f"{prompt}"
        )

    return prompt
