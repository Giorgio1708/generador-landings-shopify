from dataclasses import dataclass, field
from typing import List


@dataclass
class ProductInput:
    imagen_path: str        # Ruta a la imagen del producto
    nombre: str             # Nombre del producto
    beneficios: str         # Lista de beneficios
    uso: str                # Modo de uso
    color_hex: str          # Color principal de marca (#RRGGBB)
    precio_normal: str      # Precio tachado
    precio_oferta: str      # Precio de oferta
    angulo_venta: str       # Ángulo de venta (texto libre)
    fuente: str = "Poppins"
    fases: List[int] = field(default_factory=lambda: list(range(1, 9)))

    @property
    def info_producto(self) -> str:
        return (
            f"Nombre del producto: {self.nombre}. "
            f"Beneficios principales: {self.beneficios}. "
            f"Modo de uso: {self.uso}."
        )

    @property
    def slug(self) -> str:
        import re
        s = self.nombre.lower()
        s = re.sub(r"[^a-z0-9\s]", "", s)
        s = re.sub(r"\s+", "_", s.strip())
        return s or "producto"
