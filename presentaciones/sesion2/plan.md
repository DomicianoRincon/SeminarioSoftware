# Plan · Componentes

**Curso:** Seminario de Ingeniería de Software · Universidad Icesi
**Sesión:** 2 del bloque de Domiciano (sesión 18 del planeador), semana 9 · *Componentes*
**Duración:** 2 horas en clase
**Público:** estudiantes de Ingeniería de Sistemas, con Flutter instalado y `miapp1` corriendo en Chrome.
**Fuente:** las nueve lecciones de la sección *Sesión 2 · Componentes* del visor
(`S0010`, `S0011`, `S0012`, `S0013`, `S0014`, `S0016`, `S0017`, `S0015`, `S0018`). El plan sigue su
orden y su contenido; no agrega temas nuevos.

**Estado:** plan aprobado por el profesor el 2026-10-02. Deck construido y enlazado en `S0010`.

## Qué tiene que lograr

1. Que sepan dónde está cada cosa en el proyecto y qué hace `main.dart`.
2. Que reconozcan los widgets básicos (`Text`, `Image`, botones, `TextField`) y sus propiedades más usadas.
3. Que acomoden widgets con `Column` y `Row` y entiendan los dos ejes.
4. Que vean una pantalla como un conjunto de piezas y escriban su primer componente.
5. Que salgan con el taller empezado: seis componentes en `lib/components/`.

## Cómo se reutilizan las ilustraciones

Mismo criterio de la sesión 1: poco texto, la figura de la lección ocupa la slide y lo que
dice la lección va en las notas de orador.

- **Se recorta el título propio de cada figura**: lo pone la slide.
- **Figuras de código anotado**: se recortan al editor y al panel de resultado. Las tarjetas de
  abajo se quitan y su texto pasa a las notas, para que el código no quede chico al escalar.
- **Figuras altas se parten o se recortan**: `ppMain` va en dos slides (arranque y
  `MaterialApp`); `ppCarpetas`, `ppScaffold`, `clAlineacion`, `rwAlineacion` y `swAnatomia` se
  recortan a lo esencial. Si en la revisión visual el código queda ilegible, se parte en dos.
- **La pantalla de perfil y sus piezas** (`swPantalla`, `swPiezas`, 866 px de alto): se usa solo
  el celular de la figura, y los nombres de los componentes van como tarjetas nativas de la
  slide a los lados, con los mismos colores de las marcas.

## Slides

| # | Título | Layout | Contenido | Gráfico |
|---|---|---|---|---|
| 1 | Componentes | `titleSlideA` | Subtítulo: *Widgets básicos y tu primer componente*. Etiqueta: *Seminario de Ingeniería de Software · Universidad Icesi* | · |
| 2 | El recorrido de hoy | `slideStandard` | Cinco pasos: el proyecto → widgets básicos → Column y Row → componentes → taller | `H.bigPipeline` con íconos |
| 3 | El proyecto por dentro | `sectionSlideEBlue` | Divisor de bloque | · |
| 4 | Las carpetas del proyecto | `slideStandard` | Casi todo ocurre en `lib/`; hoy se trabaja en `components/` | SVG `ppCarpetas` |
| 5 | main.dart: el arranque | `slideStandard` | `import`, `main()`, `runApp`, `App` | SVG `ppMain`, mitad de arriba |
| 6 | main.dart: MaterialApp | `slideStandard` | Título, tema, `initialRoute` y `routes` | SVG `ppMain`, mitad de abajo |
| 7 | Las partes de un Scaffold | `slideStandard` | `Scaffold`, `appBar`, `body` y el `Text` del centro | SVG `ppScaffold` |
| 8 | Widgets básicos | `sectionSlideEBlue` | Divisor de bloque | · |
| 9 | Text y su estilo | `slideStandard` | `fontSize`, `fontWeight`, `color` | SVG `txAnatomia` |
| 10 | Cuando el texto no cabe | `slideStandard` | `maxLines` y `overflow` | SVG `txLargo` |
| 11 | Una imagen desde internet | `slideStandard` | `Image.network` | SVG `imNetwork` |
| 12 | Una imagen que viaja con la app | `slideStandard` | `assets/`, `pubspec.yaml`, `Image.asset` | SVG `imAsset` |
| 13 | fit: cuando la forma no coincide | `slideStandard` | `cover`, `contain`, `fill` | SVG `imFit` |
| 14 | Button: onPressed y child | `slideStandard` | Qué hace y qué muestra | SVG `btAnatomia` |
| 15 | Los cuatro botones | `slideStandard` | Elevated, Filled, Outlined, Text | SVG `btTipos` |
| 16 | TextField e InputDecoration | `slideStandard` | `labelText`, `hintText`, icono, borde | SVG `tfAnatomia` |
| 17 | Contraseña y teclado | `slideStandard` | `obscureText` y `keyboardType` | SVG `tfTipos` |
| 18 | Column y Row | `sectionSlideEBlue` | Divisor de bloque | · |
| 19 | Column: los dos ejes | `slideStandard` | `children`, eje principal vertical, eje cruzado horizontal | SVG `clAnatomia` |
| 20 | Alinear los hijos de una Column | `slideStandard` | `mainAxisAlignment` y `crossAxisAlignment` | SVG `clAlineacion` |
| 21 | Row: los mismos ejes, girados | `slideStandard` | Eje principal horizontal | SVG `rwAnatomia` |
| 22 | Alinear los hijos de una Row | `slideStandard` | Las mismas dos propiedades | SVG `rwAlineacion` |
| 23 | Tu primer componente | `sectionSlideEBlue` | Divisor de bloque | · |
| 24 | Una pantalla de perfil | `slideGraphicRight` | Una pregunta: ¿cuántos bloques se parecen entre sí? | Celular de `swPantalla` |
| 25 | La pantalla, como la ve quien la programa | `slideStandard` | Siete piezas, usadas trece veces: nombre de cada componente con su color y cuántas veces aparece | Celular de `swPiezas` al centro, tarjetas a los lados |
| 26 | De copiar y pegar a un componente | `slideStandard` | Lo que se repite se escribe una vez | SVG `swRepetido` |
| 27 | Anatomía de un componente | `slideStandard` | Campos `final`, constructor con nombre, `build` | SVG `swAnatomia` |
| 28 | Usarlo en una pantalla | `slideStandard` | Se importa y se le pasan datos | SVG `swUso` |
| 29 | Dónde vive y cómo se llama | `slideStandard` | Carpeta `lib/components/` · archivo `stat_card.dart` · clase `StatCard` | Tres tarjetas con ícono |
| 30 | Manos a la obra | `titleSlideF` | Separador de la parte práctica: *Taller · Componentes* | · |
| 31 | Seis componentes, ninguna pantalla | `slideStandard` | `PrimaryButton`, `SecondaryButton`, `StatsRow`, `ChatItem`, `ProfileInfo`, `ContactCard`, cada uno con su vista previa | SVG `tlTodos`, la figura que abre el taller, en tres columnas |
| 32 | PrimaryButton y SecondaryButton | `slideStandard` | Un icono y un texto en una `Row` | SVG `tlBoton` |
| 33 | StatsRow | `slideStandard` | Un componente hecho de tres `StatCard` | SVG `tlStats` |
| 34 | ContactCard | `slideStandard` | Avatar, nombre y usuario | SVG `tlContacto` |
| 35 | La prueba de un buen componente | `sectionSlideEGreen` | *Todo lo que cambia entre un uso y otro llega por el constructor* | · |
| 36 | Para la próxima sesión | `slideSidebarLeftOrange` | Los seis componentes terminados y probados con dos juegos de datos · la sesión 3 arma pantallas con ellos · el Playground del visor para probar sin abrir el proyecto | Panel lateral: íconos |

**36 slides.** Son más que las 28 de la sesión 1 porque la sesión tiene nueve lecciones y 25
figuras; casi todas las slides son una sola figura. Cada slide de contenido lleva **notas de
orador** (tecla `S`) con lo que dice la lección.

## Decisiones

- **Título de la portada**: "Componentes", el tema del planeador para la sesión.
- **`ppMain` en dos slides**: entera, el código quedaría a la mitad de su tamaño.
- **Sin el paradigma declarativo**: el profesor quitó ese apartado de `S0010` y su slide
  (*Dar órdenes o describir*) el 2026-10-02. `interfaz = f(estado)` quedó en la sesión 1.
- **Sin slides de "Ejemplo completo"** de cada lección: es código para ejecutar en el visor, no
  para proyectar. Se menciona en las notas.
- **Del taller se muestran tres figuras**, las que tiene la lección. `ChatItem` y `ProfileInfo`
  no tienen figura y quedan nombrados en la slide 31.
- **Slide 36** toma la actividad *fuera de clase* del planeador para la sesión 18.

## Dónde queda

`SeminarioSoftware/presentaciones/sesion2/` → `presentacion.html`, publicado en
https://domicianorincon.github.io/SeminarioSoftware/presentaciones/2/ y enlazado al inicio de
la lección `S0010`, la primera de la sesión.

Las figuras se copian al deck con `figuras.py` (en esta carpeta), que las lee de
`SeminarioSoftware/content/` y escribe `slides/00-figuras.js`. Si una lección cambia su
figura, se vuelve a correr `python3 figuras.py` y después el build.
