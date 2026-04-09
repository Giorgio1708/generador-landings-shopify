import json
import re
import mimetypes
from google import genai
from google.genai import types
from config.settings import GEMINI_API_KEY


def analyze_product_image(image_path: str) -> dict:
    """
    Analiza la imagen del producto con Gemini y extrae:
    nombre, beneficios, uso, color_hex, fuente
    """
    client = genai.Client(api_key=GEMINI_API_KEY)

    with open(image_path, "rb") as f:
        image_data = f.read()

    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        mime_type = "image/jpeg"

    prompt = """Analiza esta imagen de producto de e-commerce.
Responde UNICAMENTE con un JSON valido, sin markdown, sin texto adicional.

{
  "nombre": "nombre completo del producto como aparece en el empaque",
  "beneficios": "beneficio 1, beneficio 2, beneficio 3, beneficio 4, beneficio 5",
  "uso": "modo de uso breve inferido del tipo de producto",
  "color_hex": "#RRGGBB del color dominante de la marca o empaque"
}"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(data=image_data, mime_type=mime_type),
            types.Part.from_text(text=prompt),
        ],
    )

    text = response.text.strip()
    text = re.sub(r"^```(?:json)?\n?", "", text)
    text = re.sub(r"\n?```$", "", text)

    return json.loads(text)
