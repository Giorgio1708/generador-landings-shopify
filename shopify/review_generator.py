"""
Genera 20 reseñas únicas con Gemini basadas en el producto real.
Cada reseña: nombre latino, iniciales, historia de 1-1.5 párrafos, rating, tiempo.
"""

import json
import re
from google import genai
from google.genai import types
from config.settings import GEMINI_API_KEY


_PROMPT = """Eres un experto en copywriting de e-commerce latinoamericano.

Genera exactamente 20 reseñas de clientes para el siguiente producto:
{INFO_PRODUCTO}

REGLAS ABSOLUTAS:
- Cada reseña debe tener un nombre latinoamericano diferente (mezcla de Colombia, México, Venezuela, Perú, Ecuador, Argentina)
- Cada historia debe ser ÚNICA — diferente problema inicial, diferente momento de uso, diferente resultado
- El texto de cada reseña debe ser de 1 párrafo a 1.5 párrafos (entre 60 y 120 palabras)
- El tono debe sonar como una persona real escribiendo desde su celular, NO como copywriter
- Usa expresiones coloquiales latinas naturales
- Las historias deben girar alrededor del producto y sus beneficios reales: {INFO_PRODUCTO}
- Los tiempos deben variar: "hace 2 días", "hace 1 semana", "hace 3 semanas", "hace 1 mes", "hace 2 meses", etc.
- 17 reseñas de 5 estrellas, 2 de 4 estrellas, 1 de 5 estrellas (todas positivas)
- NO uses frases genéricas como "excelente producto" o "muy bueno" como única reseña

Responde ÚNICAMENTE con un array JSON válido, sin markdown, sin texto adicional.
Formato exacto:
[
  {{
    "name": "Claudia M.",
    "initials": "CM",
    "rating": 5,
    "time_ago": "hace 3 semanas",
    "text": "texto de la reseña aquí..."
  }},
  ...
]"""


def generate_reviews(info_producto: str) -> list[dict]:
    """
    Genera 20 reseñas únicas usando Gemini basadas en el producto.
    Retorna lista de dicts con name, initials, rating, time_ago, text.
    """
    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = _PROMPT.format(INFO_PRODUCTO=info_producto)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[types.Part.from_text(text=prompt)],
    )

    text = response.text.strip()
    text = re.sub(r"^```(?:json)?\n?", "", text)
    text = re.sub(r"\n?```$", "", text)

    reviews = json.loads(text)
    return reviews[:20]  # máximo 20
