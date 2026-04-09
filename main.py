import os
import sys
import subprocess
from pathlib import Path

import click

from config.settings import OUTPUT_DIR
from models.product_input import ProductInput
from generators.image_generator import ImageGenerator
from generators.prompt_builder import build_prompt
from shopify.product import create_shopify_product


@click.command()
@click.option("--imagen", required=True, type=click.Path(exists=True), help="Ruta a la imagen del producto")
@click.option("--nombre", required=True, help="Nombre del producto")
@click.option("--beneficios", required=True, help="Beneficios del producto (texto libre)")
@click.option("--uso", required=True, help="Modo de uso del producto")
@click.option("--color", required=True, help="Color hex de la marca (ej: #7B2D8B)")
@click.option("--precio-normal", required=True, help="Precio normal/tachado (ej: 89.900)")
@click.option("--precio-oferta", required=True, help="Precio de oferta (ej: 59.900)")
@click.option("--angulo", required=True, help="Ángulo de venta (texto libre, describe al cliente objetivo)")
@click.option("--fuente", default="Poppins", show_default=True, help="Tipografía para las imágenes")
@click.option(
    "--fases",
    default="1,2,3,4,5,6,7,8",
    show_default=True,
    help="Fases a generar separadas por coma (ej: 1,2,3)",
)
@click.option("--skip-shopify", is_flag=True, help="Solo generar imágenes, sin subir a Shopify")
def main(imagen, nombre, beneficios, uso, color, precio_normal, precio_oferta,
         angulo, fuente, fases, skip_shopify):
    """Generador automático de landings para Shopify con imágenes por Gemini."""

    fases_list = [int(f.strip()) for f in fases.split(",") if f.strip().isdigit()]
    if not fases_list:
        click.echo("Error: el parámetro --fases no contiene números válidos.", err=True)
        sys.exit(1)

    product = ProductInput(
        imagen_path=imagen,
        nombre=nombre,
        beneficios=beneficios,
        uso=uso,
        color_hex=color,
        precio_normal=precio_normal,
        precio_oferta=precio_oferta,
        angulo_venta=angulo,
        fuente=fuente,
        fases=fases_list,
    )

    output_dir = Path(OUTPUT_DIR) / product.slug
    output_dir.mkdir(parents=True, exist_ok=True)

    click.echo(f"\n{'='*50}")
    click.echo(f"  Producto: {nombre}")
    click.echo(f"  Fases:    {fases_list}")
    click.echo(f"  Output:   {output_dir}")
    click.echo(f"{'='*50}\n")

    try:
        generator = ImageGenerator()
    except ValueError as e:
        click.echo(f"Error de configuración: {e}", err=True)
        sys.exit(1)

    generated_images = {}

    for fase_num in fases_list:
        output_path = output_dir / f"fase_{fase_num}.png"

        if fase_num == 1:
            generated_images[1] = _generar_portada_iterativa(
                generator, product, output_path
            )
        else:
            click.echo(f"  [{fase_num}/8] Generando fase {fase_num}...")
            prompt = build_prompt(fase_num, product)
            generator.generate(prompt, str(output_path), product.imagen_path)
            generated_images[fase_num] = str(output_path)
            click.echo(f"         OK {output_path.name}")

    click.echo(f"\n  {len(generated_images)} imágenes generadas en: {output_dir}\n")

    if not skip_shopify:
        click.echo("  Subiendo producto a Shopify...")
        try:
            product_url = create_shopify_product(product, generated_images)
            click.echo(f"\n  OK Producto creado (draft): {product_url}\n")
        except Exception as e:
            click.echo(f"\n  ERROR Error en Shopify: {e}", err=True)
            click.echo(f"    Las imágenes están guardadas en: {output_dir}")
    else:
        click.echo("  Shopify omitido (--skip-shopify activo).")

    click.echo("¡Listo!\n")


def _generar_portada_iterativa(
    generator: ImageGenerator,
    product: ProductInput,
    output_path: Path,
) -> str:
    feedback = ""
    iteracion = 1

    while True:
        click.echo(f"  [1/8] Generando Portada{' (iteración ' + str(iteracion) + ')' if iteracion > 1 else ''}...")
        prompt = build_prompt(1, product, feedback=feedback)
        generator.generate(prompt, str(output_path), product.imagen_path)
        click.echo(f"         OK Guardada: {output_path}")

        _abrir_imagen(output_path)

        respuesta = click.prompt(
            "\n  Aprobar portada? [s = si  |  escribe feedback para regenerar]",
            default="s",
        ).strip()

        if respuesta.lower() in ("s", "si", "sí", "yes", "y", ""):
            click.echo()
            return str(output_path)

        feedback = respuesta
        iteracion += 1
        click.echo()


def _abrir_imagen(path: Path) -> None:
    try:
        if sys.platform == "win32":
            os.startfile(str(path))
        elif sys.platform == "darwin":
            subprocess.run(["open", str(path)], check=False)
        else:
            subprocess.run(["xdg-open", str(path)], check=False)
    except Exception:
        pass


if __name__ == "__main__":
    main()
