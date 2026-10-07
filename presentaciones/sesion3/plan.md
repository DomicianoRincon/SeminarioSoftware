# Plan · Pantallas con componentes

**Curso:** Seminario de Ingeniería de Software · Universidad Icesi
**Sesión:** 3 del bloque de Domiciano (sesión 19 del planeador), semana 10 · *Pantallas con componentes*
**Duración:** 2 horas en clase
**Público:** estudiantes de Ingeniería de Sistemas, con los siete componentes de la sesión 2 en `lib/components/`.
**Fuente:** las nueve lecciones de la sección *Sesión 3 · Pantallas con componentes* del visor
(`S0020`, `S0021`, `S0028`, `S0027`, `S0022`, `S0023`, `S0024`, `S0025`, `S0026`). El plan sigue su
orden y su contenido; no agrega temas nuevos.

**Estado:** deck construido el 2026-10-07 por pedido directo del profesor ("de la misma forma y
estilo que las dos anteriores"), sin ronda previa de aprobación de este plan. Enlazado en `S0026`.
Pendiente su revisión del `presentacion.html`.

## Qué tiene que lograr

1. Que sepan qué pone un `Scaffold` y que toda pantalla empieza por él.
2. Que entiendan por qué el `body` empieza con un `SafeArea`, aunque en Chrome no se note.
3. Que reconozcan los lugares de un `AppBar` y cómo se ve una `BottomNavigationBar`.
4. Que den aire con `Padding` y dibujen cajas con `Container`, sin confundir `padding` y `margin`.
5. Que resuelvan las dos franjas amarillas: `Expanded` para la de la derecha y `SingleChildScrollView` para la de abajo.
6. Que sepan los dos pasos de una pantalla nueva: escribirla y anotarla en `main.dart`.
7. Que salgan con el taller empezado: la pantalla de perfil en cuatro bloques, y después en cuatro secciones.

## Cómo se reutilizan las ilustraciones

Mismo criterio de las sesiones 1 y 2: poco texto, la figura de la lección ocupa la slide y lo
que dice la lección va en las notas de orador.

- **Se recorta el título propio de cada figura**: lo pone la slide.
- **Figuras de código anotado**: se recortan al editor y al panel de resultado.
- **`bnCodigo` se vuelve a generar** en 14 líneas (solo la barra, con `icon` y `label` en un
  renglón): con las 21 de la lección el código quedaba ilegible.
- **De `tpPantallas` se usa solo el celular**; los cuatro bloques los lista la slide.
- **El fondo `#FBFBFD` de las lecciones pasa a blanco**, también en degradados y parches.

## Slides

| # | Título | Layout | Contenido | Gráfico |
|---|---|---|---|---|
| 1 | Pantallas con componentes | `titleSlideA` | Subtítulo: *Scaffold, SafeArea y layout* | · |
| 2 | El recorrido de hoy | `slideStandard` | Scaffold y SafeArea → las dos barras → Container y Padding → Expanded y scroll → taller | `H.bigPipeline` |
| 3 | Lo que ya tienes | `slideStandard` | Los siete componentes de la sesión 2 | Siete tarjetas con su nombre |
| 4 | Scaffold | `sectionSlideEBlue` | Divisor de bloque | · |
| 5 | Lo que le falta a un widget suelto | `slideStandard` | El mismo `Text`, sin y con `Scaffold` | SVG `sfSinScaffold` |
| 6 | Los lugares de un Scaffold | `slideStandard` | `backgroundColor`, `appBar`, `body`, `floatingActionButton` | SVG `sfPartes` |
| 7 | Una pantalla es una Screen | `slideStandard` | Screen frente a Page | SVG `sfScreen` |
| 8 | SafeArea | `sectionSlideEBlue` | Divisor de bloque | · |
| 9 | La pantalla no es toda tuya | `slideStandard` | Barra de estado · zona segura · barra de gestos | SVG `saZonas` |
| 10 | Tres pantallas con el mismo contenido | `slideStandard` | Sin nada · con `AppBar` · con `SafeArea` | SVG `saCasos` |
| 11 | SafeArea envuelve el contenido | `slideStandard` | Va en el `body`, dentro del `Scaffold` | SVG `saCodigo` |
| 12 | La regla del curso | `sectionSlideEGreen` | *El body de toda Screen empieza con un SafeArea* | · |
| 13 | Las dos barras | `sectionSlideEBlue` | Divisor de bloque | · |
| 14 | Las partes de un AppBar | `slideStandard` | `leading`, `title`, `actions` | SVG `abPartes` |
| 15 | La misma barra, con tres ajustes | `slideStandard` | `centerTitle`, `backgroundColor`, `foregroundColor` | SVG `abVariantes` |
| 16 | Tres botones en bottomNavigationBar | `slideStandard` | `items`, `icon`, `label`, `currentIndex` | `bnCodigo`, versión corta |
| 17 | Container y Padding | `sectionSlideEBlue` | Divisor de bloque | · |
| 18 | Padding: aire alrededor de un widget | `slideStandard` | `padding` y `child` | SVG `cpPadding` |
| 19 | Tres formas de decir cuánto aire | `slideStandard` | `all`, `symmetric`, `only` | SVG `cpInsets` |
| 20 | Container: una caja que se ve | `slideStandard` | `padding`, `color`, `border`, `borderRadius` | SVG `cpContainer` |
| 21 | Las capas de un Container | `slideStandard` | `margin` por fuera, `padding` por dentro | SVG `cpCaja` |
| 22 | Expanded y scroll | `sectionSlideEBlue` | Divisor de bloque | · |
| 23 | Una fila con un texto largo | `slideStandard` | Sin `Expanded` se sale; con `Expanded` recibe lo que sobra | SVG `exSobra` |
| 24 | Expanded dentro de una Row | `slideStandard` | Se envuelve al hijo que debe adaptarse | SVG `exCodigo` |
| 25 | Repartir el espacio con flex | `slideStandard` | Mitades · dos partes y una · uno fijo y uno flexible | SVG `exFlex` |
| 26 | La pantalla es una ventana | `slideStandard` | Sin scroll y con scroll | SVG `scVentana` |
| 27 | SingleChildScrollView envuelve la Column | `slideStandard` | El scroll y su `padding` | SVG `scCodigo` |
| 28 | El mismo scroll, de lado | `slideStandard` | `scrollDirection: Axis.horizontal` y una `Row` | SVG `scHorizontal` |
| 29 | Lo que no va dentro de un scroll | `slideSidebarLeftOrange` | `Expanded` y `Spacer` · se separa con `SizedBox` | Panel lateral con íconos |
| 30 | Armar una pantalla | `sectionSlideEBlue` | Divisor de bloque | · |
| 31 | La estructura de una pantalla | `slideStandard` | Archivo, clase `XxxScreen` y `Scaffold` como raíz | SVG `apEstructura` |
| 32 | Anotar la pantalla en main.dart | `slideStandard` | `import`, entrada de `routes`, `initialRoute` | SVG `apRutas` |
| 33 | Manos a la obra | `titleSlideF` | Separador: *Taller · Pantallas* | · |
| 34 | Cuatro bloques | `slideGraphicRight` | Los cuatro bloques y sus componentes | Celular de `tpPantallas` |
| 35 | Primero, el esqueleto del body | `slideStandard` | `SafeArea` → `SingleChildScrollView` → `Column` | SVG `apCapas` |
| 36 | Bloque 1 · La información del perfil | `slideStandard` | `ProfileInfo` y `StatsRow` | SVG `tpBloque1` |
| 37 | Bloque 2 · Los botones | `slideStandard` | `PrimaryButton` y `SecondaryButton` | SVG `tpBloque2` |
| 38 | Bloque 3 · Contactos sugeridos | `slideStandard` | `SectionHeader` y fila de `ContactCard` | SVG `tpBloque3` |
| 39 | Bloque 4 · Últimas conversaciones | `slideStandard` | `SectionHeader` y `ChatItem` | SVG `tpBloque4` |
| 40 | Después, cada bloque a su archivo | `slideStandard` | Las cuatro secciones y la `Column` final de la pantalla | Tarjetas y bloque de código |
| 41 | Tu proyecto al terminar | `slideStandard` | Cinco archivos nuevos en `components/` y la pantalla | SVG `tpCarpetas` |
| 42 | Para la próxima sesión | `slideSidebarLeftOrange` | Terminar la pantalla y sus secciones · probarla angosta · la sesión 4 | Panel lateral con íconos |

**42 slides.** Cada slide de contenido lleva **notas de orador** (tecla `S`) con lo que dice la lección.

## Decisiones

- **Título de la portada**: "Pantallas con componentes", el tema del planeador.
- **AppBar y BottomNavigationBar en un solo bloque**, *Las dos barras*, en el orden del `toc.md`.
- **Expanded y scroll en un solo bloque**: son las dos soluciones a la misma franja amarilla.
- **Sin slides de "Ejemplo completo"**: es código para ejecutar en el visor.
- **Sin slide propia para `SectionHeader`**: se menciona en las notas de la slide 34.
- **Slide 42**: no nombra la lectura *fuera de clase* del planeador, que el profesor no ha definido.

## Dónde queda

`SeminarioSoftware/presentaciones/sesion3/` → `presentacion.html`, publicado en
https://domicianorincon.github.io/SeminarioSoftware/presentaciones/3/ y enlazado al inicio de
la lección `S0026`, el taller (así lo pidió el profesor; en las sesiones 1 y 2 el enlace va en
la primera lección).

Las figuras se copian al deck con `figuras.py`, que las lee de `SeminarioSoftware/content/` y
escribe `slides/00-figuras.js`. Si una lección cambia su figura: `python3 figuras.py`, build y
commit del `presentacion.html` nuevo.
