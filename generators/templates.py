# Plantillas de generación de imágenes — basadas en el prompt maestro original.
# La imagen del producto se envía como referencia multimodal a Gemini (imagen adjunta).
# Variables disponibles: {COLOR_HEX}, {PRECIO_NORMAL}, {PRECIO_OFERTA}, {FUENTE}, {INFO_PRODUCTO}, {ANGULO_VENTA}

FASE_NOMBRES = {
    1: "Portada",
    2: "Beneficios",
    3: "Producto Héroe",
    4: "Testimonios",
    5: "FAQ",
    6: "Comparativa",
    7: "Resultados",
    8: "Garantías",
}

TEMPLATES = {

1: """Genera una imagen realista de alta resolución en formato vertical (ratio 9:16) que simule un anuncio publicitario de e-commerce perfecto. La imagen debe tener exactamente esta estructura de pantalla dividida:

SECCIÓN SUPERIOR (Comparativo ANTES / DESPUÉS - 50% del canvas):
Divide esta sección en dos mitades iguales con una línea fina blanca vertical en el centro y una flecha → en el centro que indique la transformación.

MITAD IZQUIERDA — "ANTES":
Etiqueta "ANTES" en rojo en la esquina superior izquierda.
Fotografía realista y cinematográfica de una persona sufriendo intensamente el problema principal relacionado con {ANGULO_VENTA}. Expresión de dolor genuino, frustración o agotamiento visible. Postura corporal que refleja el malestar. Tonos fríos, desaturados, iluminación baja y sombría. Sin producto visible.

MITAD DERECHA — "DESPUÉS":
Etiqueta "DESPUÉS" en el color {COLOR_HEX} en la esquina superior derecha.
La misma persona completamente transformada — expresión de alivio genuino, felicidad real, energía visible. Sostiene el producto (imagen adjunta) con orgullo o lo señala sonriendo. Iluminación cálida, colores vibrantes y saturados, bokeh profundo. Contraste visual dramático respecto al lado izquierdo.

Elemento UI superpuesto:
Esquina superior derecha: Etiqueta redondeada del color {COLOR_HEX} con texto blanco: "PAGA SOLO CUANDO RECIBES".

SECCIÓN INFERIOR (Ventas y Texto - 50% del canvas):
Fondo: Color carbón oscuro sólido (casi negro), transición suave desde la foto superior, difuminado integrándose con la foto.
Barra de Prueba Social: Justo debajo de la foto, inserta: 5 estrellas blancas, icono de check, texto "Verificado", texto debajo "MÁS DE 3.500 CLIENTES FELICES".
Titular Principal (Headline): Un titular impactante basado en {INFO_PRODUCTO} y el ángulo de venta: {ANGULO_VENTA}. Debe ser en fuente {FUENTE} gruesa, mayúsculas, color BLANCO. Una palabra clave del titular debe estar resaltada en el color {COLOR_HEX}.
Cuerpo de Texto: Debajo del titular, un párrafo corto en texto blanco y legible explicando los beneficios principales basados en {INFO_PRODUCTO}.
Estructura de Precios:
Precio de Oferta: {PRECIO_OFERTA} (Grande, blanco, negrita).
Precio Original: {PRECIO_NORMAL} (Tachado, color gris).
Píldora de Ahorro: Etiqueta del color {COLOR_HEX} redondeada con texto blanco indicando el ahorro calculado entre ambos precios.
Pie de página: Iconos pequeños blancos y texto en la parte inferior: Icono camión "Envío Gratis" | Icono reloj "Entrega entre: 3 a 6 días".""",

2: """Crea una imagen tipo infografía (ratio 9:16) con diseño limpio y equilibrado, usando FONDO BLANCO y la paleta de colores basada en {COLOR_HEX} y la fuente {FUENTE}. Asegura que todas las áreas de texto sean fáciles de leer.

Todos los iconos serán lineales e irán dentro de un cuadro con bordes redondeados de un color mucho más claro (pastel/crema) que {COLOR_HEX} para contraste, o usando {COLOR_HEX} si contrasta bien.

PRODUCTO DE REFERENCIA: {INFO_PRODUCTO}

Encabezado Superior:
Área de título principal y subtítulo, alineados a la izquierda.
Título Principal: extraer beneficio clave corto de {INFO_PRODUCTO}
Subtítulo: complementar título usando información de {INFO_PRODUCTO}
A la derecha, un sello circular dorado que en su interior incluya un beneficio clave en porcentaje (ej. "80%+ Ingrediente/Efecto relevante").
Junto al sello, la ilustración realista del frasco y etiqueta basada en la imagen adjunta del producto.
Atrás del frasco, una forma orgánica suave (tipo mancha) del mismo color pastel/crema de los cuadros de iconos, resaltando el producto con estética natural/wellness.

Sección "Beneficios Clave":
Título de la sección: Beneficios Clave.
Seis bloques de iconos lineales simples relacionados con el producto o su efecto según {INFO_PRODUCTO}, organizados en dos filas de tres.
Debajo de cada icono, un área de texto breve con cada beneficio.
Al finalizar esta sección, una línea fina separadora del mismo color pastel.

Sección "¿Por Qué Elegir?":
Título de la sección: ¿Por qué elegir nuestro producto?
Tres bloques de iconos lineales simples.
Debajo de cada icono, un texto relacionado con una razón de compra relevante para {INFO_PRODUCTO}.
Al finalizar esta sección, una línea fina separadora del mismo color pastel.

Sección "Modo de Uso":
Título de la sección: Modo de uso.
Un icono lineal relacionado con el modo de utilización basado en las instrucciones de {INFO_PRODUCTO}.
A la derecha, dos áreas de texto con instrucciones breves (Paso 1 y Paso 2) extraídas de {INFO_PRODUCTO}.""",

3: """Genera una imagen publicitaria vertical (ratio 9:16) manteniendo estrictamente la estética y paleta de colores {COLOR_HEX}, replicando la siguiente estructura geométrica de "Producto Héroe":

PRODUCTO DE REFERENCIA: {INFO_PRODUCTO}

1. FONDO Y AMBIENTE:
Usa un fondo de estudio limpio y premium. El color del fondo debe ser coherente con la marca: puede ser un sólido mate de un tono derivado de {COLOR_HEX} (si es oscuro) o un color neutro/crema (si la marca es clara) que permita leer los textos perfectamente. La iluminación es suave y difusa (Softbox lighting).

2. ESTRUCTURA CENTRAL (HÉROE):
Coloca el frasco de la imagen adjunta en el centro exacto de la mitad inferior.
Efecto de Suspensión (Gravedad Cero): Justo encima de la tapa del frasco, flotando en el aire, coloca 2 unidades del producto (cápsulas/gomitas/gotas/tabletas según {INFO_PRODUCTO}) con iluminación brillante y nítida. Deben verse tridimensionales y realistas.

3. TEXTOS SUPERIORES (ENCABEZADO):
En la parte superior, centrado:
Titular: "Tu fórmula diaria de [Beneficio Principal extraído de {INFO_PRODUCTO}]". Fuente {FUENTE} GRUESA (Bold), tamaño grande. Color que contraste fuertemente con el fondo.
Subtítulo: Justo debajo, centrado: los ingredientes clave o potencia extraídos de {INFO_PRODUCTO}. Fuente más delgada, tamaño mediano.

4. ESPECIFICACIONES TÉCNICAS (ESTILO CLÍNICO):
A la derecha del frasco, crea un elemento gráfico de UI:
Dibuja una línea fina y elegante que salga desde el costado del frasco hacia la derecha.
Al final de la línea, coloca un bloque de texto flotante alineado a la izquierda con:
"Dosis recomendada extraída de {INFO_PRODUCTO}"
"Duración del frasco/Total de porciones"
Pon el texto sobre una sutil tarjeta traslúcida, manteniendo el estilo minimalista.

5. PIE DE PÁGINA:
En el borde inferior, texto pequeño y discreto centrado: "Basado en ciencia · Calidad Premium".

IMPORTANTE: Si el fondo es oscuro, usa textos blancos. Si el fondo es claro, usa textos oscuros. El color de acento para líneas o detalles debe ser {COLOR_HEX}.""",

4: """Genera una imagen vertical (ratio 9:16) para una sección de testimonios, manteniendo estrictamente la estética oscura y la paleta de colores {COLOR_HEX}.

PRODUCTO DE REFERENCIA: {INFO_PRODUCTO}

1. FONDO Y TÍTULO:
Fondo: Un fondo oscuro, gris carbón muy oscuro o negro con iluminación sutil y difusa.
Título Principal: En la parte superior, centrado, en fuente {FUENTE} GRUESA (Bold), color blanco, tamaño grande: "Lo que dicen quienes ya lo usan".

2. CUADRÍCULA DE TESTIMONIOS (4 TARJETAS):
Crea una cuadrícula de 2 filas por 2 columnas con cuatro tarjetas de testimonios.
Cada tarjeta debe tener bordes redondeados y un color de fondo ligeramente más claro que el fondo principal (gris oscuro translúcido), con un borde muy fino del color de acento {COLOR_HEX}.

Contenido de cada tarjeta:
Foto UGC del Producto: En lugar de foto de perfil, ocupa la parte superior de cada tarjeta con una fotografía estilo UGC (User Generated Content) del producto (imagen adjunta) en una ubicación cotidiana diferente en cada tarjeta: encima de una cama con sábanas arrugadas, sobre un mostrador de baño con objetos personales al fondo, encima de una mesa de cocina con luz natural lateral, sobre una mesa de noche con celular o vaso de agua cerca. Cada foto debe verse tomada con un Android de gama baja: leve sobreexposición, colores ligeramente saturados, ángulo imperfecto, sin composición planeada, totalmente espontánea y auténtica.
Nombre del Cliente: Debajo de la foto, nombre latinoamericano en blanco bold (ej. "Claudia R.", "Andrés M.", "Verónica L.", "Carlos T.").
Calificación: Debajo del nombre, cinco estrellas del color de acento {COLOR_HEX}.
Texto del Testimonio: Un párrafo breve con el texto del testimonio en fuente {FUENTE}, color blanco o gris claro, legible. Genera 4 testimonios distintos relacionados con los beneficios de {INFO_PRODUCTO}.

3. PIE DE PÁGINA:
En el borde inferior, centrado, en texto pequeño y discreto: "Experiencias reales. Resultados individuales pueden variar.\"""",

5: """Genera una imagen vertical (ratio 9:16) para la sección de Preguntas Frecuentes, manteniendo estrictamente la estética oscura ("Dark Mode Premium") y la paleta de colores de las fases anteriores.

PRODUCTO DE REFERENCIA: {INFO_PRODUCTO}

1. FONDO Y TÍTULO:
Fondo: Color oscuro sólido o degradado muy sutil (negro/gris carbón).
Título Principal: En la parte superior, centrado, grande y legible en fuente {FUENTE} (Bold). Color: Blanco o Crema muy claro. Texto: "Preguntas frecuentes".

2. ESTRUCTURA DE TARJETAS (CUERPO CENTRAL):
Crea una columna vertical con 4 tarjetas rectangulares apiladas una debajo de la otra.
Estilo de la Tarjeta: Fondo oscuro (ligeramente más claro que el fondo principal para crear profundidad), bordes redondeados y un trazo/borde muy fino del color de acento {COLOR_HEX}.

3. CONTENIDO DE LAS TARJETAS:
Dentro de cada tarjeta, coloca una pregunta y respuesta lógica para este tipo de producto según {INFO_PRODUCTO}, siguiendo este formato visual exacto:
Icono Q (Pregunta): La letra "Q" en color {COLOR_HEX}, seguido de la pregunta en texto blanco brillante.
Icono A (Respuesta): La letra "A" debajo, seguido de la respuesta breve y tranquilizadora en texto gris claro o blanco suave.
Las 4 preguntas deben cubrir: Tiempo de resultados, Seguridad/Contraindicaciones, Beneficio principal, Diferenciador vs. otras marcas.
Genera las preguntas y respuestas basándote en {INFO_PRODUCTO}.

4. ESTÉTICA GENERAL:
El diseño debe verse limpio, moderno y corporativo. Tipografía Sans-Serif geométrica {FUENTE}.""",

6: """Genera una imagen vertical (ratio 9:16) con una tabla comparativa de alto contraste, manteniendo la estética oscura y la paleta de colores {COLOR_HEX}.

PRODUCTO DE REFERENCIA: {INFO_PRODUCTO}

1. ENCABEZADO IMPACTANTE:
En la parte superior, centrado, en fuente {FUENTE} GRUESA (Bold) y mayúsculas.
Texto: "LA DIFERENCIA ES CLARA".
Color: Blanco o el color de acento {COLOR_HEX} (si es claro/luminoso) para que destaque sobre el fondo oscuro.

2. ESTRUCTURA DE COLUMNAS (IZQUIERDA VS DERECHA):
Columna Izquierda (NUESTRO PRODUCTO — HÉROE):
Cabecera: Imagen pequeña del frasco (imagen adjunta) + nombre del producto de {INFO_PRODUCTO}.
Estilo de Texto: Blanco brillante, Negrita.
Iconos: CHECK (✓) dentro de círculos del color de acento {COLOR_HEX} para cada punto.

Columna Derecha (COMPETENCIA):
Cabecera: Texto gris: "OTROS SUPLEMENTOS" o "GENÉRICOS".
Estilo de Texto: Gris apagado, fuente delgada o regular.
Iconos: "X" en gris muy oscuro sutil. La columna debe verse visualmente inferior comparada con la izquierda.

3. CONTENIDO DE LAS FILAS (5 filas comparativas, separadas por líneas finas grises):
Fila 1 — Formato/Absorción: Izquierda: "Absorción Superior/Rápida" vs Derecha: "Absorción lenta".
Fila 2 — Ingredientes: Izquierda: "Ingredientes Premium/Naturales" vs Derecha: "Rellenos sintéticos".
Fila 3 — Seguridad: Izquierda: "Testeado en Lab" vs Derecha: "Sin verificar".
Fila 4 — Beneficio Clave: Izquierda: beneficio principal extraído de {INFO_PRODUCTO} vs Derecha: "Efecto mínimo".
Fila 5 — Resultado: Izquierda: "Resultados Visibles" vs Derecha: "Resultados inconsistentes".

4. ESTÉTICA:
Fondo negro o gris carbón muy oscuro. La columna de nuestro producto debe parecer iluminada, mientras que la de la competencia debe verse en la sombra.""",

7: """Genera una imagen vertical (ratio 9:16) dividida en dos secciones principales (Visual Superior y Datos Inferior), manteniendo la estética oscura y la paleta de colores {COLOR_HEX}.

PRODUCTO DE REFERENCIA: {INFO_PRODUCTO}

1. ENCABEZADO:
En el tope superior, centrado, en fuente {FUENTE} GRUESA (Bold) y mayúsculas.
Texto: "RESULTADOS QUE SE VEN".
Color: Verde lima brillante o el color de acento {COLOR_HEX}.

2. SECCIÓN VISUAL (MITAD SUPERIOR):
Crea una composición de pantalla dividida verticalmente por una línea fina blanca.
Lado Izquierdo: Etiqueta "ANTES" en la parte superior. Muestra una representación visual realista del problema que resuelve {INFO_PRODUCTO}, en tonos desaturados o sepia. Sin producto visible.
Lado Derecho: Etiqueta "DESPUÉS" en la parte superior. Muestra el resultado ideal con iluminación brillante, colores vivos y saturados. Persona con el beneficio ya logrado.
Adapta la composición al tipo específico de producto y beneficio descrito en {INFO_PRODUCTO}.
Overlay: Un círculo sutil flotando en la intersección que diga la característica/ingrediente clave extraído de {INFO_PRODUCTO}.

3. SECCIÓN DE DATOS (MITAD INFERIOR):
Fondo oscuro sólido.
Crea una tabla de 4 filas con líneas de separación horizontales muy finas.
Columna Izquierda (Categoría): Texto en mayúsculas, color de acento {COLOR_HEX}. Categorías derivadas de los beneficios de {INFO_PRODUCTO}.
Columna Derecha (Beneficio): Texto blanco descriptivo del resultado esperado.

4. ESTILO GENERAL:
Dark Mode Premium. El contraste entre el Antes (apagado) y el Después (brillante) debe ser la clave visual.""",

8: """Genera una imagen vertical (ratio 9:16) para la sección de garantías y logística, manteniendo estrictamente la estética oscura y la paleta de colores {COLOR_HEX}.

PRODUCTO DE REFERENCIA: {INFO_PRODUCTO}

1. FONDO Y TÍTULO PRINCIPAL:
Fondo: Color oscuro sólido o degradado sutil, consistente con el resto de la página.
Título: En la parte superior, centrado, en fuente {FUENTE} GRUESA (Bold). Color blanco. Texto: "COMPRA CON TOTAL CONFIANZA".

2. SECCIÓN SUPERIOR — GARANTÍAS DEL PRODUCTO (Fila de 3 Iconos):
Crea una fila horizontal con tres módulos de iconos.
Estilo de Icono: Iconos lineales limpios y modernos en el color de acento {COLOR_HEX}.
Estilo de Texto: Texto blanco legible debajo de cada icono.
Módulo 1: Icono de escudo con check. Texto: "SIN EFECTOS SECUNDARIOS".
Módulo 2: Icono de cronómetro/velocidad. Texto: "RESULTADOS EN POCAS SEMANAS".
Módulo 3: Icono de hoja/planta. Texto: "INGREDIENTES 100% NATURALES".

3. SECCIÓN INFERIOR — LOGÍSTICA Y SEGURIDAD:
Subtítulo: Debajo de la fila de iconos, en texto blanco, fuente {FUENTE} GRUESA: "NUESTROS ALIADOS LOGÍSTICOS".
Estructura: Una fila con tres tarjetas rectangulares verticales con bordes redondeados.
Estilo de Tarjeta: Fondo oscuro (ligeramente más claro que el fondo principal), con un borde fino del color de acento {COLOR_HEX}.

Tarjeta 1 — Pago: Icono de mano recibiendo paquete/dinero. Título: "PAGO CONTRA ENTREGA".
Tarjeta 2 — Envío: Icono de avión o camión. Título: "ENVÍO GRATIS". Subtítulo: "A todo el país".
Tarjeta 3 — Calidad: Icono de matraz de laboratorio con check. Título: "PRODUCTO 100% PROBADO". Subtítulo: "Calidad garantizada".

4. ESTÉTICA GENERAL:
El diseño debe ser limpio, con amplio espacio entre elementos, transmitiendo seguridad y profesionalismo. Sin dorados ni estilos recargados.""",

}
