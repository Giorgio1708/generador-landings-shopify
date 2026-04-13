# Plantillas de estructura — instrucciones para que gemini-2.5-flash genere
# el prompt especializado de imagen por producto.
# Variables: {COLOR_HEX}, {PRECIO_NORMAL}, {PRECIO_OFERTA}, {FUENTE}, {INFO_PRODUCTO}, {ANGULO_VENTA}

FASE_NOMBRES = {
    1: "Portada",
    2: "Infografía de Beneficios",
    3: "Características Técnicas",
    4: "Garantías",
    5: "Preguntas Frecuentes",
    6: "Testimonios",
}

TEMPLATES = {

# ─────────────────────────────────────────────────────────────────────────────
1: """Genera una imagen publicitaria de altísima calidad, formato vertical 9:16,
que simule un anuncio de e-commerce de conversión máxima.

CONCEPTO: La imagen es 100% visual y fluida. NO hay bloques separados ni
divisiones horizontales visibles. Todo se integra en una sola composición
cinematográfica que fluye de arriba hacia abajo naturalmente.

COMPOSICIÓN GENERAL:
La imagen entera es una escena fotográfica de alta producción con elementos
de UI sobrepuestos de forma orgánica, como si fuera un story de Instagram
con diseño premium. Nada parece pegado. Todo respira.

ZONA SUPERIOR — VISUAL DE TRANSFORMACIÓN:
Una composición de pantalla dividida verticalmente de forma dramática por
una línea de luz (no una línea gráfica simple, sino un destello de luz que
separa ambos lados de forma cinematográfica).

LADO IZQUIERDO — ANTES:
Etiqueta "ANTES" flotante en rojo con tipografía {FUENTE}.
Persona real sufriendo intensamente el problema principal de {ANGULO_VENTA}.
Expresión genuina de dolor/agotamiento/frustración. Postura corporal que
lo refleja. Paleta fría y desaturada. Iluminación tenue y dramática.

LADO DERECHO — DESPUÉS:
Etiqueta "DESPUÉS" flotante en {COLOR_HEX} con tipografía {FUENTE}.
La misma persona completamente transformada — vitalidad, alivio, felicidad
real. Sostiene el producto (imagen adjunta) con naturalidad y orgullo.
Bokeh profundo, iluminación cálida y dorada, colores vibrantes y saturados.

ELEMENTOS UI FLOTANTES (integrados sobre la foto, no debajo):
— Esquina superior derecha: píldora redondeada {COLOR_HEX} "PAGA SOLO CUANDO RECIBES"
— Centro inferior de la foto (sobre la imagen, no debajo): barra de prueba
  social con fondo negro semitransparente, bordes redondeados:
  ★★★★★ · ✓ Verificado · "MÁS DE 3.500 CLIENTES FELICES"

ZONA INFERIOR — DEGRADADO OSCURO CON TEXTO (fluye desde la foto):
La imagen base continúa hacia abajo pero se oscurece progresivamente
con un degradado negro suave desde el centro hacia abajo.
Sobre ese degradado oscuro, de arriba a abajo:

TITULAR: fuente {FUENTE} bold, mayúsculas, blanco, máximo 2 líneas.
Construido desde {INFO_PRODUCTO} y {ANGULO_VENTA}. Una palabra clave
resaltada con subrayado o color {COLOR_HEX}.

PRECIO en la misma zona, alineado a la izquierda:
{PRECIO_OFERTA} grande y blanco en negrita.
{PRECIO_NORMAL} tachado en gris junto al lado.
Píldora de ahorro en {COLOR_HEX} con el ahorro calculado.

PIE INTEGRADO al fondo, pequeño, centrado:
🚚 Envío Gratis  |  🕐 Entrega 3 a 6 días

REGLA ABSOLUTA: No debe verse como "sección arriba + sección abajo".
Debe verse como UNA sola imagen fotográfica de moda/lifestyle con
elementos informativos integrados de forma orgánica y premium.""",

# ─────────────────────────────────────────────────────────────────────────────
2: """Genera una imagen publicitaria vertical 9:16, estilo infografía de producto premium.
Fondo blanco limpio o blanco hueso. Paleta {COLOR_HEX}. Fuente {FUENTE}.

PRODUCTO: {INFO_PRODUCTO}

CONCEPTO: El producto es el protagonista absoluto al centro. 4 beneficios
clave lo rodean como satélites. Mínimo texto. Máximo impacto visual.

ESTRUCTURA:

ENCABEZADO (parte superior, ~15% del canvas):
Título corto y poderoso extraído del beneficio principal de {INFO_PRODUCTO}.
Fuente {FUENTE} bold. Color oscuro que contraste con el fondo blanco.
Subtítulo en una línea, fuente delgada, color gris.

ZONA CENTRAL — PRODUCTO 3D HERO (~50% del canvas):
El producto (imagen adjunta) renderizado en 3D o con fotografía de estudio
de altísima calidad, flotando en el centro ligeramente elevado, con sombra
suave debajo y un halo de luz tenue en {COLOR_HEX} alrededor.
El producto debe verse tridimensional, con profundidad y detalles del empaque
perfectamente visibles: etiqueta, colores, textura, forma exacta.
Escala grande — ocupa el 40-50% del ancho del canvas.

LOS 4 BENEFICIOS RODEANDO EL PRODUCTO:
Posicionados en las 4 esquinas alrededor del producto (arriba izquierda,
arriba derecha, abajo izquierda, abajo derecha).
Cada beneficio conectado al producto con una línea fina y elegante de {COLOR_HEX}.
Cada beneficio: SOLO UNA PALABRA CLAVE en mayúsculas bold {COLOR_HEX}
+ una línea descriptiva breve en gris (máximo 5 palabras).
Los 4 beneficios se extraen directamente de {INFO_PRODUCTO}.
NO usar cajas ni cuadros — las palabras flotan sobre el fondo blanco.

PIE (~15% del canvas):
Sello circular con "Fórmula Premium · Alta Biodisponibilidad" a un lado.
Barra de separación fina en {COLOR_HEX}.
Texto pequeño: nombre del producto de {INFO_PRODUCTO}.

REGLA ABSOLUTA: Sin grillas de iconos. Sin bloques de texto. Solo el
producto 3D al centro y 4 palabras clave orbitando a su alrededor.""",

# ─────────────────────────────────────────────────────────────────────────────
3: """Genera una imagen publicitaria vertical 9:16 estilo "Producto Héroe Técnico".
Fondo de estudio premium derivado de {COLOR_HEX} o neutro/crema. Fuente {FUENTE}.

PRODUCTO: {INFO_PRODUCTO}

1. FONDO Y LUZ:
Fondo sólido premium (oscuro derivado de {COLOR_HEX} o crema/neutro si la marca es clara).
Iluminación tipo softbox: suave, difusa, envuelve el producto con elegancia.

2. PRODUCTO CENTRAL:
Producto (imagen adjunta) centrado en la mitad inferior, grande y nítido.
Sobre la tapa del producto, flotando en gravedad cero: 2 unidades del producto
(cápsulas/gomitas/gotas/tabletas según {INFO_PRODUCTO}), tridimensionales,
con iluminación brillante. Se ven reales y perfectos.

3. ENCABEZADO SUPERIOR:
Titular centrado, fuente {FUENTE} GRUESA bold, alto contraste con el fondo:
"Tu fórmula diaria de [Beneficio Principal de {INFO_PRODUCTO}]"
Subtítulo debajo, fuente delgada: ingredientes clave o potencia de {INFO_PRODUCTO}.

4. ESPECIFICACIONES TÉCNICAS (lado derecho del producto):
Línea fina y elegante saliendo del costado del producto hacia la derecha.
Al final de la línea, bloque sobre tarjeta traslúcida minimalista:
— Dosis recomendada de {INFO_PRODUCTO}
— Duración del frasco / total de porciones

5. PIE: "Basado en ciencia · Calidad Premium" — pequeño, centrado, discreto.

REGLA: Si fondo oscuro → textos blancos. Si fondo claro → textos oscuros.
Acento y líneas en {COLOR_HEX}.""",

# ─────────────────────────────────────────────────────────────────────────────
4: """Genera una imagen vertical 9:16 para sección de garantías y confianza.
Estética dark mode premium. Paleta {COLOR_HEX}. Fuente {FUENTE}.

PRODUCTO: {INFO_PRODUCTO}

1. TÍTULO PRINCIPAL:
"COMPRA CON TOTAL CONFIANZA"
Fuente {FUENTE} GRUESA, blanco, centrado arriba.

2. FILA DE 3 GARANTÍAS (iconos lineales):
Iconos limpios y modernos en {COLOR_HEX}, texto blanco debajo.
— Escudo con check: "SIN EFECTOS SECUNDARIOS"
— Cronómetro: "RESULTADOS EN POCAS SEMANAS"
— Hoja/planta: "INGREDIENTES 100% NATURALES"

3. SECCIÓN LOGÍSTICA — "NUESTROS ALIADOS":
3 tarjetas verticales con bordes redondeados, fondo oscuro, borde {COLOR_HEX}.
— Tarjeta 1: icono paquete/mano → "PAGO CONTRA ENTREGA"
— Tarjeta 2: icono camión/avión → "ENVÍO GRATIS" / "A todo el país"
— Tarjeta 3: icono matraz+check → "PRODUCTO 100% PROBADO" / "Calidad garantizada"

4. PIE DISCRETO: "Tu satisfacción es nuestra prioridad."

Diseño limpio, amplio espacio entre elementos, profesional. Sin dorados.""",

# ─────────────────────────────────────────────────────────────────────────────
5: """Genera una imagen vertical 9:16 para sección de Preguntas Frecuentes.
Dark Mode Premium. Paleta {COLOR_HEX}. Fuente {FUENTE}.

PRODUCTO: {INFO_PRODUCTO}

1. FONDO Y TÍTULO:
Fondo negro/gris carbón sólido.
Título: "Preguntas frecuentes" — {FUENTE} bold, blanco/crema, grande, centrado.

2. CUERPO — 4 tarjetas apiladas verticalmente:
Cada tarjeta: fondo ligeramente más claro que el fondo (gris oscuro),
bordes redondeados, trazo fino {COLOR_HEX} en borde.
Formato interno de cada tarjeta:
Q en color {COLOR_HEX} → pregunta en texto blanco brillante.
A justo debajo → respuesta breve y tranquilizadora en gris claro.

Genera las 4 preguntas y respuestas adaptadas específicamente a {INFO_PRODUCTO}:
1. ¿Cuándo veré resultados?
2. ¿Es seguro? ¿Tiene contraindicaciones?
3. ¿Cuál es su beneficio principal?
4. ¿Por qué es mejor que otras marcas?

3. Tipografía sans-serif geométrica {FUENTE}. Diseño limpio y corporativo.""",

# ─────────────────────────────────────────────────────────────────────────────
6: """Genera una imagen vertical 9:16 para sección de testimonios de clientes reales.
Dark mode. Paleta {COLOR_HEX}. Fuente {FUENTE}.

PRODUCTO: {INFO_PRODUCTO}

CONCEPTO CLAVE: Esta sección debe verse COMPLETAMENTE AUTÉNTICA y sin filtros.
Las fotos del producto NO son de estudio. Son fotos de clientes reales.

1. FONDO Y TÍTULO:
Fondo gris carbón muy oscuro o negro.
Título: "Lo que dicen nuestros clientes" — {FUENTE} GRUESA, blanco, grande, centrado.
Subtítulo pequeño: ★★★★★ "Más de 3.500 personas lo comprueban"

2. CUADRÍCULA DE 6 TARJETAS (3 filas × 2 columnas):
Cada tarjeta: bordes redondeados, fondo gris oscuro translúcido, borde muy fino {COLOR_HEX}.

FOTO UGC (parte superior de cada tarjeta — ocupa ~45% de la tarjeta):
Foto del producto (imagen adjunta) en 6 situaciones cotidianas DISTINTAS y ALEATORIAS:
- Tarjeta 1: producto tirado sobre una cama deshecha, sábanas arrugadas, luz de tarde.
- Tarjeta 2: mano en primera persona sosteniendo el producto frente a una ventana.
- Tarjeta 3: producto apoyado en el borde de un sofá con cojines desordenados.
- Tarjeta 4: producto sobre una mesa de madera con taza de café al lado.
- Tarjeta 5: mano latinoamericana sosteniendo el producto, fondo de cocina borroso.
- Tarjeta 6: producto sobre una mesa de noche con celular y vaso de agua cerca.

ESTILO FOTOGRÁFICO OBLIGATORIO para cada foto:
— Tomada con Android de gama baja. Ruido digital visible. Leve sobreexposición.
— Colores ligeramente saturados y cálidos. Foco imperfecto.
— Ángulo casual, no planificado. Composición descuidada a propósito.
— NADA de fotografía profesional. NADA de fondo blanco. NADA de producto centrado.
— Se ve como una foto de WhatsApp enviada por un cliente real.

PARTE INFERIOR DE CADA TARJETA:
Nombre latinoamericano bold blanco (Claudia R., Andrés M., Verónica L., Carlos T., Diana P., Sebastián G.)
★★★★★ en {COLOR_HEX}
Testimonio corto, directo y natural de máximo 2 líneas relacionado con {INFO_PRODUCTO}.
El testimonio debe sonar como lo diría una persona real, no un copywriter.

3. PIE: "Experiencias reales. Resultados individuales pueden variar." """,

}
