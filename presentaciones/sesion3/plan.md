# Plan · Pantallas con componentes

**Curso:** Seminario de Ingeniería de Software · Universidad Icesi
**Sesión:** 3 del bloque de Domiciano (sesión 19 del planeador), semana 10 · *Pantallas con componentes*
**Duración:** 2 horas en clase
**Público:** estudiantes de Ingeniería de Sistemas, con los siete componentes de la sesión 2 en `lib/components/`.
**Fuente:** las siete lecciones de la sección *Sesión 3 · Pantallas con componentes* del visor
(`S0020` a `S0026`). El plan sigue su orden y su contenido; no agrega temas nuevos.

**Estado:** pendiente de aprobación del profesor. No se construye hasta tener su visto bueno.

## Qué tiene que lograr

1. Que sepan qué pone un `Scaffold` y que toda pantalla empieza por él.
2. Que entiendan por qué el `body` empieza con un `SafeArea`, aunque en Chrome no se note.
3. Que den aire con `Padding` y dibujen cajas con `Container`, sin confundir `padding` y `margin`.
4. Que resuelvan las dos franjas amarillas: `Expanded` para la de la derecha y `SingleChildScrollView` para la de abajo.
5. Que armen una pantalla de afuera hacia adentro y salgan con el taller empezado: la pantalla de perfil.

## Cómo se reutilizan las ilustraciones

Mismo criterio de las sesiones 1 y 2: poco texto, la figura de la lección ocupa la slide y lo
que dice la lección va en las notas de orador.

- **Se recorta el título propio de cada figura**: lo pone la slide.
- **Figuras de código anotado** (`sfPartes`, `saCodigo`, `cpPadding`, `cpContainer`, `exCodigo`,
  `scCodigo`, `apPerfil`): van enteras. Esta vez no tienen tarjetas debajo, así que no hay nada
  que recortar.
- **`exCodigo` y `apPerfil` tienen 20 líneas de código**: si en la revisión visual quedan
  ilegibles, se parten en dos slides.
- **`scVentana` y `tpPantallas` son altas** (664 y 882 px): se escalan a la altura del lienzo.
  De `tpPantallas` se usa el celular, con el contenido de la pantalla listado al lado.

## Slides

| # | Título | Layout | Contenido | Gráfico |
|---|---|---|---|---|
| 1 | Pantallas con componentes | `titleSlideA` | Subtítulo: *Scaffold, SafeArea y layout*. Etiqueta: *Seminario de Ingeniería de Software · Universidad Icesi* | · |
| 2 | El recorrido de hoy | `slideStandard` | Seis pasos: Scaffold → SafeArea → Container y Padding → Expanded → scroll → armar la pantalla | `H.bigPipeline` con íconos |
| 3 | Lo que ya tienes | `slideStandard` | Los siete componentes de la sesión 2, con su nombre. Hoy se encajan | Siete tarjetas con el nombre de cada componente |
| 4 | Scaffold | `sectionSlideEBlue` | Divisor de bloque | · |
| 5 | Lo que le falta a un widget suelto | `slideStandard` | El mismo `Text`, sin y con `Scaffold` | SVG `sfSinScaffold` |
| 6 | Los lugares de un Scaffold | `slideStandard` | `backgroundColor`, `appBar`, `body`, `floatingActionButton` | SVG `sfPartes` |
| 7 | Una pantalla es una Screen | `slideStandard` | Tiene `Scaffold`, vive en `lib/screens/`, se abre por su ruta. La Page llega en la sesión 9 | SVG `sfScreen` |
| 8 | SafeArea | `sectionSlideEBlue` | Divisor de bloque | · |
| 9 | La pantalla no es toda tuya | `slideStandard` | Barra de estado y cámara · zona segura · barra de gestos | SVG `saZonas` |
| 10 | Cuándo hace falta | `slideStandard` | Sin nada · con `AppBar` · con `SafeArea` | SVG `saCasos` |
| 11 | SafeArea envuelve el contenido | `slideStandard` | Va en el `body`, dentro del `Scaffold` | SVG `saCodigo` |
| 12 | La regla del curso | `sectionSlideEGreen` | *El body de toda Screen empieza con un SafeArea* | · |
| 13 | Container y Padding | `sectionSlideEBlue` | Divisor de bloque | · |
| 14 | Padding: aire alrededor | `slideStandard` | `padding` y `child` | SVG `cpPadding` |
| 15 | Tres formas de decir cuánto aire | `slideStandard` | `all`, `symmetric`, `only` | SVG `cpInsets` |
| 16 | Container: una caja que se ve | `slideStandard` | `padding`, `color`, `border`, `borderRadius` | SVG `cpContainer` |
| 17 | Las capas de un Container | `slideStandard` | `margin` por fuera, `padding` por dentro | SVG `cpCaja` |
| 18 | Expanded y scroll | `sectionSlideEBlue` | Divisor de bloque | · |
| 19 | Una fila con un texto largo | `slideStandard` | Sin `Expanded` se sale; con `Expanded` recibe lo que sobra | SVG `exSobra` |
| 20 | Expanded dentro de una Row | `slideStandard` | Se envuelve al hijo que debe adaptarse | SVG `exCodigo` |
| 21 | Repartir el espacio con flex | `slideStandard` | Mitades, dos partes y una, uno fijo y uno flexible | SVG `exFlex` |
| 22 | La pantalla es una ventana | `slideStandard` | Sin scroll, lo que no cabe queda fuera; con scroll, la pantalla se desliza | SVG `scVentana` |
| 23 | SingleChildScrollView envuelve la Column | `slideStandard` | El scroll mide la pantalla; la `Column`, lo que necesiten sus hijos | SVG `scCodigo` |
| 24 | El mismo scroll, de lado | `slideStandard` | `scrollDirection: Axis.horizontal` y una `Row` | SVG `scHorizontal` |
| 25 | Lo que no va dentro de un scroll | `slideSidebarLeftOrange` | `Expanded` y `Spacer` reparten lo que sobra · dentro de un scroll no sobra nada · se separa con `SizedBox` | Panel lateral: ícono de alerta |
| 26 | Armar una pantalla | `sectionSlideEBlue` | Divisor de bloque | · |
| 27 | De afuera hacia adentro | `slideStandard` | `Scaffold` → `SafeArea` → `SingleChildScrollView` → `Column` → componentes | SVG `apCapas` |
| 28 | Tus componentes, dentro de la pantalla | `slideStandard` | La pantalla ordena y entrega datos; no dibuja | SVG `apPerfil` |
| 29 | ¿De quién es el problema? | `slideStandard` | Dos tarjetas: lo que se corrige en el componente (tamaño, color, contenido) · lo que se corrige en la pantalla (orden, separación, scroll) | Dos tarjetas con ícono |
| 30 | Manos a la obra | `titleSlideF` | Separador de la parte práctica: *Taller · Pantallas* | · |
| 31 | Pantalla de perfil | `slideGraphicRight` | `ProfileScreen` · `'/profile'` · con barra y scroll · botones, contactos que se deslizan, conversaciones | Celular de perfil de `tpPantallas` |
| 32 | Un componente que te entregamos | `slideStandard` | `SectionHeader`: recibe `title` y `actionLabel`. Se lee antes de usarlo | Código de `SectionHeader` en un frame de editor |
| 33 | Tu proyecto al terminar | `slideStandard` | Un componente y una pantalla nuevos | SVG `tpCarpetas` |
| 34 | Para la próxima sesión | `slideSidebarLeftOrange` | La pantalla de perfil terminada y probada en una ventana angosta · la lectura sobre archivos de contexto para agentes | Panel lateral: íconos |

**34 slides**, dos menos que la sesión 2. Cada slide de contenido lleva **notas de orador**
(tecla `S`) con lo que dice la lección.

## Decisiones

- **Título de la portada**: "Pantallas con componentes", el tema del planeador.
- **Expanded y scroll en un solo bloque**: son las dos soluciones a la misma franja amarilla, una
  a lo ancho y otra a lo alto.
- **Sin slides de "Ejemplo completo"**: es código para ejecutar en el visor. Se menciona en las notas.
- **Sin slide de imports con `package:`**: se dice en las notas de la slide 28.
- **Slide 32**: el código de `SectionHeader` se dibuja con `tools/code_frame.py`, sin flechas,
  con el `Expanded` resaltado. Es la única figura que no viene de una lección.
- **Slide 34** toma la actividad *fuera de clase* del planeador. **Falta que el profesor diga cuál
  es la lectura**; si no la hay todavía, la slide deja solo el primer punto.

## Dónde queda

`SeminarioSoftware/presentaciones/sesion3/` → `presentacion.html`, publicado en
https://domicianorincon.github.io/SeminarioSoftware/presentaciones/3/ y enlazado al inicio de
la lección `S0020`, la primera de la sesión.

Las figuras se copian al deck con `figuras.py` (en esta carpeta, adaptado del de la sesión 2),
que las lee de `SeminarioSoftware/content/` y escribe `slides/00-figuras.js`.
