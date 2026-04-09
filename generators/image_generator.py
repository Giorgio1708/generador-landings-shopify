import mimetypes
from io import BytesIO
from pathlib import Path

from google import genai
from google.genai import types
from PIL import Image

from config.settings import GEMINI_API_KEY, GEMINI_MODEL


class ImageGenerator:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY no está configurado en el archivo .env")
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt: str, output_path: str, product_image_path: str) -> None:
        """Genera una imagen usando Gemini con la imagen del producto como referencia."""
        with open(product_image_path, "rb") as f:
            image_data = f.read()

        mime_type, _ = mimetypes.guess_type(product_image_path)
        if not mime_type:
            mime_type = "image/jpeg"

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=[
                types.Part.from_bytes(data=image_data, mime_type=mime_type),
                types.Part.from_text(text=prompt),
            ],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )

        for part in response.candidates[0].content.parts:
            if getattr(part, "inline_data", None) is not None:
                img = Image.open(BytesIO(part.inline_data.data))
                Path(output_path).parent.mkdir(parents=True, exist_ok=True)
                img.save(output_path, "PNG")
                return

        raise RuntimeError(
            "Gemini no devolvió una imagen. "
            "Verifica que el modelo soporta generación de imágenes y que el prompt es válido."
        )
