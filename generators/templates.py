# Plantillas de generación de imágenes para cada fase de la landing.
# Las variables {COLOR_HEX}, {PRECIO_NORMAL}, {PRECIO_OFERTA}, {FUENTE},
# {INFO_PRODUCTO} y {ANGULO_VENTA} se reemplazan en tiempo de ejecución.
# La imagen del producto se envía como parte multimodal a Gemini (no como texto).

FASE_NOMBRES = {
    1: "Portada",
    2: "Infografía de Beneficios",
    3: "Características Técnicas",
    4: "Testimonios",
    5: "Preguntas Frecuentes",
    6: "Tabla Comparativa",
    7: "Resultados Visuales",
    8: "Garantías y Logística",
}

TEMPLATES = {

1: """ÁNGULO DE VENTA DEL PRODUCTO: {ANGULO_VENTA}

Genera una imagen realista de alta resolución en formato vertical (ratio 9:16) que simule un anuncio publicitario de e-commerce de alta conversión. La imagen tiene DOS secciones claramente diferenciadas:

SECCIÓN SUPERIOR - ANTES Y DESPUÉS (50% del canvas):
Esta sección es una composición dividida en DOS mitades lado a lado, separadas por una línea fina vertical blanca con una flecha apuntando de izquierda a derecha en el centro.

LADO IZQUIERDO - "ANTES":
Etiqueta "ANTES" en la esquina superior izquierda, texto rojo o gris oscuro, fuente {FUENTE} bold.
Muestra a una persona real sufriendo activamente el problema principal derivado de {ANGULO_VENTA} e {INFO_PRODUCTO}. La expresión facial debe ser de malestar, frustración o dolor genuino. La escena, la postura corporal y el entorno deben reflejar exactamente ese sufrimiento de forma visceral y reconocible. Tonos desaturados, fríos, iluminación tenue. Sin producto visible.

LADO DERECHO - "DESPUÉS":
Etiqueta "DESPUÉS" en la esquina superior derecha, texto del color {COLOR_HEX}, fuente {FUENTE} bold.
La misma persona (misma edad, mismo contexto) completamente transformada: expresión de alivio, energía y satisfacción genuina. Sosteniendo el producto de referencia (imagen adjunta) en la mano de forma prominente. Iluminación cálida, brillante, saturada. Fondo ligeramente desenfocado (bokeh).

Elemento UI superpuesto: esquina superior derecha de toda la sección, etiqueta redondeada del color {COLOR_HEX} con texto blanco: "PAGA SOLO CUANDO RECIBES".

SECCIÓN INFERIOR - VENTAS Y TEXTO (50% del canvas):
Fondo: color carbón oscuro sólido (casi negro), transición suave difuminada desde la sección superior.
Barra de Prueba Social: 5 estrellas blancas + icono check + "Verificado" + "MÁS DE [3.500] CLIENTES FELICES".
Titular Principal: texto en fuente {FUENTE} gruesa, mayúsculas, color BLANCO, basado en la transformación del ANTES al DESPUÉS de {ANGULO_VENTA}. Una palabra o frase clave resaltada en el color {COLOR_HEX}.
Cuerpo de Texto: párrafo corto en texto blanco explicando los beneficios de {INFO_PRODUCTO} en relación directa con el dolor mostrado en el ANTES.
Estructura de Precios: Precio oferta {PRECIO_OFERTA} grande y blanco | Precio normal {PRECIO_NORMAL} tachado en gris | Píldora de ahorro en color {COLOR_HEX}.
Pie de página: icono camión "Envío Gratis" | icono reloj "Entrega entre: 3 a 6 días".""",

2: """ÁNGULO DE VENTA DEL PRODUCTO: {ANGULO_VENTA}

Crea una imagen tipo infografía (ratio 9:16) con diseño limpio y equilibrado, usando FONDO BLANCO y la paleta de colores basada en {COLOR_HEX} y la fuente {FUENTE}. Asegura que todas las áreas de texto sean fáciles de leer.

Todos los iconos serán lineales e irán dentro de un cuadro con bordes redondeados de un color mucho más claro (pastel/crema) que {COLOR_HEX} para contraste, o usando {COLOR_HEX} si contrasta bien.

Encabezado Superior:
Área de título principal y subtítulo, alineados a la izquierda.
Título Principal: [EXTRAER BENEFICIO CLAVE CORTO DE {INFO_PRODUCTO}]
Subtítulo: [COMPLEMENTAR TÍTULO USANDO INFORMACIÓN DE {INFO_PRODUCTO}]
A la derecha, un sello circular dorado que en su interior incluya un beneficio clave en % (ej. "80%+ [Ingrediente/Efecto]").
Junto al sello, la ilustración realista del producto de referencia en la imagen adjunta.
Atrás del producto, una forma orgánica suave (tipo mancha) del mismo color pastel/crema de los cuadros de iconos, resaltando el producto con estética natural/"wellness".

Sección "Beneficios Clave":
Título de la sección: Beneficios Clave.
Seis bloques de iconos lineales simples relacionados con el producto o su efecto ({INFO_PRODUCTO}), organizados en dos filas de tres.
Debajo de cada icono, un área de texto breve (ej. "[Beneficio 1]", "[Beneficio 2]", etc.).
Al finalizar esta sección, una línea fina separadora del mismo color pastel.

Sección "¿Por Qué Elegir?":
Título de la sección: ¿Por qué elegir nuestro producto?
Tres bloques de iconos lineales simples.
Debajo de cada icono, un texto relacionado con una razón de compra (ej. "[Razón 1]", "[Razón 2]", etc.).
Al finalizar esta sección, una línea fina separadora del mismo color pastel.

Sección "Modo de Uso":
Título de la sección: Modo de uso.
Un icono lineal relacionado con el modo de utilización basado en las instrucciones de {INFO_PRODUCTO}.
A la derecha, dos áreas de texto con instrucciones breves y detalladas (Paso 1 y Paso 2) extraídas de {INFO_PRODUCTO}.""",

3: """ÁNGULO DE VENTA DEL PRODUCTO: {ANGULO_VENTA}

Genera una imagen publicitaria vertical (ratio 9:16) manteniendo estrictamente la estética y paleta de colores usada anteriormente ({COLOR_HEX}), replicando la siguiente estructura geométrica de "Producto Héroe":

1. FONDO Y AMBIENTE:
Usa un fondo de estudio limpio y premium. El color del fondo debe ser coherente con la marca: puede ser un sólido mate de un tono derivado de {COLOR_HEX} (si es oscuro) o un color neutro/crema (si la marca es clara) que permita leer los textos perfectamente. La iluminación es suave y difusa ("Softbox lighting").

2. ESTRUCTURA CENTRAL (HÉROE):
Coloca el producto de referencia (imagen adjunta) en el centro exacto de la mitad inferior.
Efecto de Suspensión (Gravedad Cero): Justo encima del producto, flotando en el aire, coloca 2 unidades del producto (cápsulas/gomitas/gotas según {INFO_PRODUCTO}) con una iluminación brillante y nítida. Deben verse tridimensionales y realistas.

3. TEXTOS SUPERIORES (ENCABEZADO):
En la parte superior, centrado:
Titular: "Tu fórmula diaria de [Beneficio Principal Corto extraído de {INFO_PRODUCTO}]". Fuente {FUENTE} GRUESA (Bold), tamaño grande. Color que contraste fuertemente con el fondo.
Subtítulo: Justo debajo, centrado: "[Ingredientes Clave o Potencia extraídos de {INFO_PRODUCTO}]". Fuente más delgada, tamaño mediano.

4. ESPECIFICACIONES TÉCNICAS (ESTILO CLÍNICO):
A la derecha del producto, crea un elemento gráfico de UI:
Dibuja una línea fina y elegante que salga desde el costado del producto hacia la derecha.
Al final de la línea (lado derecho), coloca un bloque de texto flotante alineado a la izquierda que diga claramente:
"[Dosis recomendada extraída de {INFO_PRODUCTO}]"
"[Duración del frasco/Total porciones extraídas de {INFO_PRODUCTO}]"

5. PIE DE PÁGINA:
En el borde inferior, texto pequeño y discreto centrado: "Basado en ciencia • Calidad Premium".

IMPORTANTE: Si el fondo es oscuro, usa textos blancos. Si el fondo es claro, usa textos oscuros. El color de acento para líneas o detalles debe ser {COLOR_HEX}.""",

4: """ÁNGULO DE VENTA DEL PRODUCTO: {ANGULO_VENTA}

Genera una imagen vertical (ratio 9:16) para una sección de testimonios, manteniendo estrictamente la estética oscura y la paleta de colores {COLOR_HEX}. La imagen debe replicar la estructura de cuadrícula siguiente.

1. FONDO Y TÍTULO:
Fondo: Un fondo oscuro, consistente con el estilo de la marca. Puede ser un gris carbón muy oscuro o negro con una iluminación sutil y difusa.
Título Principal: En la parte superior, centrado, en fuente {FUENTE} GRUESA (Bold), color blanco, tamaño grande: "Lo que dicen quienes ya lo usan".

2. CUADRÍCULA DE TESTIMONIOS (4 TARJETAS):
Crea una cuadrícula de 2 filas por 2 columnas con cuatro tarjetas de testimonios.
Cada tarjeta debe tener bordes redondeados y un color de fondo ligeramente más claro que el fondo principal (ej. un gris oscuro translúcido) para destacarse sutilmente, con un borde muy fino del color de acento {COLOR_HEX}.
Contenido de cada Tarjeta:
Foto de Perfil y Nombre: En la esquina superior izquierda de cada tarjeta, una pequeña foto de perfil circular y al lado el nombre del cliente (ej. "Claudia R.", "Andrés M.", "Verónica L.", "Carlos T.").
Calificación: Debajo del nombre, cinco estrellas del color de acento {COLOR_HEX}.
Texto del Testimonio: Debajo de la calificación, un párrafo breve con el texto del testimonio en fuente {FUENTE}, color blanco o gris claro, legible. Genera testimonios realistas y positivos relacionados con {INFO_PRODUCTO}, cumpliendo con políticas de publicidad (sin promesas exageradas).

3. PIE DE PÁGINA:
En el borde inferior, centrado, en texto pequeño y discreto: "Experiencias reales. Resultados individuales pueden variar." """,

5: """ÁNGULO DE VENTA DEL PRODUCTO: {ANGULO_VENTA}

Genera una imagen vertical (ratio 9:16) para la sección de Preguntas Frecuentes, manteniendo estrictamente la estética oscura ("Dark Mode Premium") y la paleta de colores de la marca.

1. FONDO Y TÍTULO:
Fondo: Color oscuro sólido o degradado muy sutil (negro/gris carbón).
Título Principal: En la parte superior, centrado, grande y legible en fuente {FUENTE}. Color: Blanco o Crema muy claro. Texto: "Preguntas frecuentes".

2. ESTRUCTURA DE TARJETAS (CUERPO CENTRAL):
Crea una columna vertical con 4 tarjetas rectangulares apiladas una debajo de la otra.
Estilo de la Tarjeta: Fondo oscuro (ligeramente más claro que el fondo principal para crear profundidad), bordes redondeados y un trazo/borde muy fino del color de acento {COLOR_HEX}.

3. CONTENIDO DE LAS TARJETAS (Generar texto basado en {INFO_PRODUCTO}):
Dentro de cada tarjeta, coloca una pregunta y respuesta lógica para este tipo de producto:
Icono Q (Pregunta): La letra "Q" o un punto en color {COLOR_HEX}, seguido de la pregunta en texto blanco brillante (ej. "¿Cuándo veré resultados?", "¿Es seguro?", "¿Cómo se toma?", "¿Por qué es diferente?").
Icono A (Respuesta): La letra "A" o un guion debajo, seguido de la respuesta breve y tranquilizadora en texto gris claro o blanco suave.
Genera las preguntas más comunes para el tipo de producto descrito en {INFO_PRODUCTO}: tiempo de resultados, seguridad/contraindicaciones, beneficio principal, diferenciador.

4. ESTÉTICA GENERAL:
El diseño debe verse limpio, moderno y corporativo. La tipografía debe ser Sans-Serif geométrica.""",

6: """ÁNGULO DE VENTA DEL PRODUCTO: {ANGULO_VENTA}

Genera una imagen vertical (ratio 9:16) con una tabla comparativa de alto contraste, manteniendo la estética oscura y la paleta de colores de la marca.

1. ENCABEZADO IMPACTANTE:
En la parte superior, centrado, en fuente {FUENTE} GRUESA (Bold) y mayúsculas.
Texto: "LA DIFERENCIA ES CLARA".
Color: Usa un tono brillante (Blanco o el color de acento {COLOR_HEX} si es claro/luminoso) para que destaque sobre el fondo oscuro.

2. ESTRUCTURA DE COLUMNAS (IZQUIERDA VS DERECHA):
Columna Izquierda (HÉROE):
Cabecera: Imagen pequeña del producto de referencia (imagen adjunta) + nombre del producto extraído de {INFO_PRODUCTO}.
Estilo de Texto: Blanco brillante, Negrita.
Iconos: Usa iconos de CHECK (✓) dentro de círculos del color de acento {COLOR_HEX} para cada punto.

Columna Derecha (COMPETENCIA):
Cabecera: Texto gris: "OTROS SUPLEMENTOS" o "GENÉRICOS".
Estilo de Texto: Gris apagado, fuente delgada o regular.
Iconos: Iconos de "X" en gris muy oscuro sutil. La columna debe verse visualmente "inferior" comparada con la izquierda.

3. CONTENIDO DE LAS FILAS:
Crea 5 filas comparativas horizontales separadas por líneas finas grises. Deduce los puntos de comparación basándote en {INFO_PRODUCTO}:
Fila 1 (Formato/Absorción): Izquierda: "Absorción Superior/Rápida" vs Derecha: "Absorción lenta/Pobre".
Fila 2 (Ingredientes): Izquierda: "Ingredientes Premium/Naturales" vs Derecha: "Rellenos sintéticos".
Fila 3 (Seguridad): Izquierda: "Testeado en Lab" vs Derecha: "Sin verificar".
Fila 4 (Beneficio Clave): Izquierda: "[Beneficio Principal extraído de {INFO_PRODUCTO}]" vs Derecha: "Efecto mínimo".
Fila 5 (Resultado): Izquierda: "Resultados Visibles" vs Derecha: "Resultados inconsistentes".

4. ESTÉTICA:
Fondo negro o gris carbón muy oscuro. La columna del producto debe parecer iluminada, mientras que la de la competencia debe verse en la sombra.""",

7: """ÁNGULO DE VENTA DEL PRODUCTO: {ANGULO_VENTA}

Genera una imagen vertical (ratio 9:16) dividida en dos secciones principales (Visual Superior y Datos Inferior), manteniendo la estética oscura y la paleta de colores de la marca ({COLOR_HEX}).

1. ENCABEZADO:
En el tope superior, centrado, en fuente {FUENTE} GRUESA (Bold) y mayúsculas.
Texto: "RESULTADOS QUE SE VEN".
Color: Usa un tono verde lima brillante o el color de acento {COLOR_HEX}.

2. SECCIÓN VISUAL (MITAD SUPERIOR):
Crea una composición de pantalla dividida verticalmente por una línea fina blanca.
Lado Izquierdo: Etiqueta "ANTES" en la parte superior. Muestra una representación visual del "problema" relacionado con {INFO_PRODUCTO} en tonos desaturados o sepia.
Lado Derecho: Etiqueta "DESPUÉS" en la parte superior. Muestra el "resultado ideal" con iluminación brillante, colores vivos y saturados.
Adapta la imagen al tipo de producto en {INFO_PRODUCTO}. Si es abstracto, usa metáforas visuales claras.
Overlay: Un círculo sutil flotando en la intersección que diga una característica clave extraída de {INFO_PRODUCTO}.

3. SECCIÓN DE DATOS (MITAD INFERIOR):
Fondo oscuro sólido.
Crea una tabla de 3 o 4 filas con líneas de separación horizontales muy finas.
Columna Izquierda (Categoría): Texto en mayúsculas, color de acento {COLOR_HEX} (según el tipo de beneficios en {INFO_PRODUCTO}).
Columna Derecha (Beneficio): Texto blanco descriptivo del resultado.

4. ESTILO GENERAL:
Mantén la coherencia con el "Dark Mode Premium". El contraste entre el Antes (apagado) y el Después (brillante) debe ser la clave visual.""",

8: """ÁNGULO DE VENTA DEL PRODUCTO: {ANGULO_VENTA}

Genera una imagen vertical (ratio 9:16) para la sección de garantías y logística, manteniendo estrictamente la estética oscura y la paleta de colores de la marca ({COLOR_HEX}).

1. FONDO Y TÍTULO PRINCIPAL:
Fondo: Color oscuro sólido o degradado sutil, consistente con el resto de la página.
Título: En la parte superior, centrado, en fuente {FUENTE} GRUESA (Bold). Color blanco. Texto: "COMPRA CON TOTAL CONFIANZA".

2. SECCIÓN SUPERIOR: GARANTÍAS DEL PRODUCTO (Fila de 3 Iconos):
Crea una fila horizontal con tres módulos de iconos.
Estilo de Icono: Iconos lineales limpios y modernos en el color de acento {COLOR_HEX}.
Estilo de Texto: Texto blanco legible debajo de cada icono.
Contenido (Izquierda a Derecha):
Módulo 1: Icono de escudo con check. Texto: "SIN EFECTOS SECUNDARIOS".
Módulo 2: Icono de cronómetro/velocidad. Texto: "RESULTADOS EN POCAS SEMANAS".
Módulo 3: Icono de hoja/planta. Texto: "INGREDIENTES 100% NATURALES".

3. SECCIÓN INFERIOR: LOGÍSTICA Y SEGURIDAD (Título + Tarjetas):
Título de Sección: Debajo de la fila de iconos, un subtítulo en texto blanco, fuente {FUENTE} GRUESA: "NUESTROS ALIADOS LOGÍSTICOS".
Estructura de Tarjetas: Crea una fila con tres tarjetas rectangulares verticales con bordes redondeados.
Estilo de Tarjeta: Fondo oscuro (ligeramente más claro que el fondo principal), con un borde fino del color de acento {COLOR_HEX}.
Contenido de cada Tarjeta:
Tarjeta 1 (Pago): Icono de mano recibiendo paquete/dinero. Título: "PAGO CONTRA ENTREGA".
Tarjeta 2 (Envío): Icono de avión o camión. Título: "ENVÍO GRATIS". Subtítulo: "A todo el país".
Tarjeta 3 (Calidad): Icono de matraz de laboratorio con check. Título: "PRODUCTO 100% PROBADO". Subtítulo: "Calidad garantizada".

4. ESTÉTICA GENERAL:
El diseño debe ser limpio, con amplio espacio entre elementos, transmitiendo seguridad y profesionalismo.""",

}
