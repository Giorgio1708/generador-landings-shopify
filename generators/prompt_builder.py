from generators.prompt_generator import generate_specialized_prompt
from models.product_input import ProductInput


def build_prompt(
    fase: int,
    product: ProductInput,
    feedback: str = "",
) -> str:
    """
    Genera un prompt de imagen ultra-específico para la fase indicada.

    Flujo de dos pasos:
      1. gemini-2.5-flash analiza el producto real (imagen + info) y construye
         un prompt cinematográfico detallado siguiendo la plantilla de la fase.
      2. Ese prompt es el que se pasa al modelo de generación de imágenes.
    """
    return generate_specialized_prompt(
        fase=fase,
        product=product,
        product_image_path=product.imagen_path,
        feedback=feedback,
    )
