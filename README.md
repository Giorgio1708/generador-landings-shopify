# Generador Automatico de Landings para Shopify

Automatiza la creacion de landing pages de productos para Shopify.
Con solo una imagen del producto y un angulo de venta, genera 8 imagenes
de alta conversion usando Gemini AI y crea el producto con su template
en tu tienda Shopify.

## Que hace

1. Genera 8 imagenes de landing (portada antes/despues, infografia, testimonios, FAQ, comparativa, resultados, garantias)
2. Crea el producto en Shopify como draft
3. Sube las imagenes al producto
4. Crea un template de producto personalizado con las imagenes
5. Asigna el template al producto automaticamente

## Requisitos

- Python 3.11+
- Cuenta de Google AI Studio con billing activo (Gemini API)
- Tienda Shopify con una Custom App configurada

## Instalacion

```bash
git clone https://github.com/tu-usuario/generador-landings-shopify
cd generador-landings-shopify
pip install -r requirements.txt
cp .env.example .env
```

Edita `.env` con tus credenciales:

```
GEMINI_API_KEY=tu_api_key_de_gemini
SHOPIFY_STORE=tu-tienda.myshopify.com
SHOPIFY_CLIENT_ID=tu_client_id
SHOPIFY_CLIENT_SECRET=tu_client_secret
```

## Configurar Shopify

1. Ve a tu admin: `Settings > Apps > Develop apps > Create an app`
2. En `Configure Admin API scopes` activa:
   - `write_products` / `read_products`
   - `write_themes` / `read_themes`
3. Instala la app y copia el `Client ID` y `Client Secret`

## Uso

```bash
python main.py \
  --imagen "producto.jpg" \
  --nombre "Nombre del Producto" \
  --beneficios "beneficio 1, beneficio 2, beneficio 3" \
  --uso "Tomar 1 capsula al dia con agua" \
  --color "#1565C0" \
  --precio-normal "89.900" \
  --precio-oferta "59.900" \
  --angulo "Descripcion del cliente objetivo y su problema principal"
```

### Opciones

| Flag | Descripcion | Default |
|------|-------------|---------|
| `--imagen` | Ruta a la imagen del producto | requerido |
| `--nombre` | Nombre del producto | requerido |
| `--beneficios` | Beneficios del producto | requerido |
| `--uso` | Modo de uso | requerido |
| `--color` | Color hex de la marca | requerido |
| `--precio-normal` | Precio tachado | requerido |
| `--precio-oferta` | Precio de oferta | requerido |
| `--angulo` | Angulo de venta | requerido |
| `--fuente` | Tipografia | `Poppins` |
| `--fases` | Fases a generar | `1,2,3,4,5,6,7,8` |
| `--skip-shopify` | Solo generar imagenes | `false` |

### Solo generar imagenes (sin Shopify)

```bash
python main.py --imagen "producto.jpg" ... --skip-shopify
```

### Generar solo algunas fases

```bash
python main.py --imagen "producto.jpg" ... --fases "1,2,3"
```

## Costos aproximados

- Gemini 3 Pro: ~$0.30 USD por landing completa (8 imagenes)
- Tier gratuito: hasta ~62 landings/dia sin costo

## Estructura del proyecto

```
generador-landings-shopify/
├── main.py                    # CLI principal
├── config/settings.py         # Configuracion
├── models/product_input.py    # Modelo de datos
├── generators/
│   ├── templates.py           # 8 plantillas de imagen
│   ├── prompt_builder.py      # Constructor de prompts
│   └── image_generator.py     # Llamadas a Gemini API
└── shopify/
    ├── client.py              # Cliente HTTP Shopify
    ├── product.py             # Crear producto + imagenes
    ├── metafields.py          # Metafields de landing
    └── template.py            # Templates de tema
```
