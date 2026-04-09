"""
Modo interactivo para generar una nueva landing.
Uso: python nuevo_producto.py
"""
import os
import sys
import subprocess
from pathlib import Path


def preguntar(texto, ejemplo=""):
    if ejemplo:
        return input(f"\n{texto}\n  (ej: {ejemplo})\n  > ").strip()
    return input(f"\n{texto}\n  > ").strip()


def main():
    print("\n" + "="*50)
    print("  GENERADOR DE LANDINGS — NUEVO PRODUCTO")
    print("="*50)

    imagen = preguntar(
        "Ruta o nombre de la imagen del producto",
        "producto.jpg"
    )
    if not Path(imagen).exists():
        print(f"\nERROR: No se encontro el archivo '{imagen}'")
        print("Asegurate de que la imagen este en esta carpeta o escribe la ruta completa.")
        sys.exit(1)

    nombre = preguntar(
        "Nombre del producto",
        "Magnesium Complex 1000mg"
    )

    beneficios = preguntar(
        "Beneficios principales (separados por coma)",
        "mejora el sueno, fortalece huesos, reduce calambres"
    )

    uso = preguntar(
        "Modo de uso",
        "Tomar 2 capsulas al dia con agua"
    )

    color = preguntar(
        "Color hex de la marca",
        "#1565C0"
    )
    if not color.startswith("#"):
        color = "#" + color

    precio_normal = preguntar(
        "Precio normal (tachado)",
        "89.900"
    )

    precio_oferta = preguntar(
        "Precio de oferta",
        "59.900"
    )

    angulo = preguntar(
        "Angulo de venta: describe a tu cliente y su dolor principal",
        "Mujeres mayores de 35 que sufren insomnio y calambres nocturnos"
    )

    fuente = input("\nTipografia (Enter para usar Poppins): ").strip() or "Poppins"

    print("\n" + "-"*50)
    print(f"  Producto : {nombre}")
    print(f"  Color    : {color}")
    print(f"  Precio   : {precio_normal} -> {precio_oferta}")
    print(f"  Imagen   : {imagen}")
    print("-"*50)

    confirmar = input("\nGenerar landing y subir a Shopify? [s/n]: ").strip().lower()
    if confirmar not in ("s", "si", "yes", "y"):
        print("Cancelado.")
        sys.exit(0)

    cmd = [
        sys.executable, "main.py",
        "--imagen", imagen,
        "--nombre", nombre,
        "--beneficios", beneficios,
        "--uso", uso,
        "--color", color,
        "--precio-normal", precio_normal,
        "--precio-oferta", precio_oferta,
        "--angulo", angulo,
        "--fuente", fuente,
    ]

    subprocess.run(cmd)


if __name__ == "__main__":
    main()
