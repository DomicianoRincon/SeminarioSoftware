# Plan · Estado: StatefulWidget y setState

**Curso:** Seminario de Ingeniería de Software · Universidad Icesi  
**Sesión:** 6 del bloque de Domiciano (sesión 22 del planeador), semana 11 · *Stateful widget y setState*  
**Duración:** 2 horas en clase  
**Público:** estudiantes de Ingeniería de Sistemas que ya hicieron componentes `StatelessWidget` (sesión 2) y pantallas estáticas (sesión 3).  
**Fuente:** las cinco lecciones de la sección *Sesión 6 · Stateful widget y setState* del visor (`S0040` a `S0044`; el taller `S0045` pasó a la sesión 7 el 2026-10-22). El plan sigue su orden y su contenido.  
**Sin entregables:** es una sesión de clase. El cierre anuncia la sesión 7, que arranca del ejemplo completo de `S0044`. No deja tarea.

**Estado:** borrador, pendiente de aprobación del profesor.

## Qué tiene que lograr

1. Que distingan lo que es estado (datos que cambian con la pantalla abierta) de lo que no.
2. Que entiendan por qué un `StatefulWidget` son dos clases y por qué el estado vive en el `State`.
3. Que vean, con el contador de `flutter create`, que `setState` cambia el dato y pide un `build()`, y qué pasa si se olvida.
4. Que ubiquen `initState` y `dispose`, y creen y liberen un `TextEditingController`.
5. Que armen el creador de playlists: formulario, lista en el estado, primero pintada con `Text` y luego con el componente `SongCard`.

## Lo nuevo de esta presentación: diagramas interactivos en vivo

Cinco slides llevan un **simulador que se usa en vivo** durante la clase: el profesor pulsa, escribe y
los estudiantes ven cambiar el teléfono, el objeto State, la línea de código y la consola. Son los mismos
simuladores de las lecciones (`classnotesapp/src/components/interactive/flutterStateSims.js`), copiados al
deck. En las capturas de la revisión visual se verán en su estado inicial.

- Se pegan como `helpers.js` del deck (o un script aparte que incluya `build.py`), sin cambiar el archivo.
- Ocupan la slide entera bajo un título corto: el simulador mide unos 960 × 640 px y el lienzo es 1280 × 720.
- Reveal no captura el teclado cuando el foco está en un campo, así que el formulario de la playlist se
  puede llenar en vivo. Hay que comprobarlo en el navegador, con `F` (pantalla completa) incluida.

## Tiempos

| Bloque | Slides | Minutos |
|---|---|---|
| Apertura | 1 a 4 | 10 |
| ¿Qué es el estado? | 5 a 10 | 20 |
| setState: el contador | 11 a 17 | 25 |
| Ciclo de vida | 18 a 21 | 15 |
| Creador de playlists | 22 a 30 | 40 |
| Cierre | 31 y 32 | 10 |

Total: 120 minutos. El bloque de la playlist incluye el arranque del taller en clase.

## Slides

| # | Título | Layout | Contenido | Gráfico |
|---|---|---|---|---|
| 1 | Estado: pantallas que cambian | `titleSlideA` | Subtítulo: *StatefulWidget, setState y un creador de playlists* | · |
| 2 | El recorrido de hoy | `slideStandard` | Estado · setState · ciclo de vida · playlist · taller | `H.bigPipeline` |
| 3 | Hasta ahora, pantallas quietas | `slideStandard` | El perfil de la sesión 3 se ve igual siempre. Una app real cambia mientras se usa | Figura `swPantalla` de `S0015` |
| 4 | Lo que te llevas hoy | `slideStandard` | Saber cuándo usar Stateful · setState · initState y dispose · la playlist con `SongCard` | Lista con íconos |
| 5 | ¿Qué es el estado? | `sectionSlideEBlue` | Divisor | · |
| 6 | Estado es lo que cambia con la pantalla abierta | `slideStandard` | Contador, bombillo, texto de un campo, canciones. La pregunta: *¿puede valer distinto en un minuto?* | Cuatro tarjetas |
| 7 | El estado detrás de una pantalla | `slideStandard` | Una app con sus datos y, al lado, las cuatro variables de estado con flechas a lo que muestran | SVG `ewPantalla` |
| 8 | Las dos clases de un StatefulWidget | `slideStandard` | Widget, `createState`, campos del State, `build` | SVG `ewAnatomia` |
| 9 | **En vivo** · El widget se recrea, el State no | `slideStandard` | Encender el bombillo y luego *Reconstruir App*: `_isOn` sigue en la sección Estado | Interactivo `state-tree bulb` |
| 10 | La idea de la sesión | `sectionSlideEGreen` | *La pantalla es lo que sale de pintar el estado.* | · |
| 11 | setState: el contador | `sectionSlideEBlue` | Divisor | · |
| 12 | El sumador de flutter create | `slideStandard` | `_counter`, `_incrementCounter`, `build` con `print` | Código del State |
| 13 | El print en build | `slideStandard` | Cada toque escribe `build() con _counter = n` en la consola: así se ve cuándo se reconstruye | Código con el `print` |
| 14 | **En vivo** · Lo que pasa cuando se pulsa + | `slideStandard` | Los cinco pasos en el árbol, con *Paso a paso* para narrar cada uno; el resumen fijo (`ssCiclo`) va en las notas | Interactivo `state-tree forget` |
| 15 | **En vivo** · Olvidar setState | `slideStandard` | El árbol con *Olvidar setState*: el Estado sube, la pantalla no, *Flutter no se enteró* | Interactivo `state-tree forget` |
| 16 | **En vivo** · Hot reload frente a hot restart | `slideStandard` | Reload conserva el State; restart crea uno nuevo | Interactivo `hot-reload` |
| 17 | Pasar una función al botón | `slideSidebarLeftOrange` | `onPressed: _increment` · `onPressed: () => _increment()` · el error de los paréntesis | Tres líneas de código |
| 18 | Ciclo de vida | `sectionSlideEBlue` | Divisor | · |
| 19 | La vida de un objeto State | `slideStandard` | Una vez, muchas veces, una vez | SVG `lcLinea` |
| 20 | **En vivo** · Abrir, escribir, cerrar | `slideStandard` | El controller nace en initState y muere en dispose; el error tras dispose | Interactivo `state-lifecycle` |
| 21 | El TextEditingController | `slideStandard` | `late`, `initState`, `dispose`, leer `.text` | Código anotado |
| 22 | Creador de playlists | `sectionSlideEBlue` | Divisor | · |
| 23 | **En vivo** · La playlist en texto | `slideStandard` | Agregar tres canciones y mirar `_songs` | Interactivo `playlist` |
| 24 | El modelo Song | `slideStandard` | Tres campos `final`; lo que cambia es la lista | Código de `Song` |
| 25 | Del formulario a la lista | `slideStandard` | El botón agrega al estado; build pinta todo | SVG `plFlujo` |
| 26 | _addSong y el for en children | `slideStandard` | El add dentro de setState, los `clear()` fuera | Código |
| 27 | El componente SongCard | `slideStandard` | Recibe una Song; portada con `clipBehavior` | SVG `sgCodigo` |
| 28 | **En vivo** · Text o SongCard | `slideStandard` | Misma lista de estado, otra vista | Interactivo `playlist cards` |
| 29 | Del estado a las tarjetas | `slideStandard` | La Screen es la dueña; la tarjeta solo muestra | SVG `sgDatos` |
| 30 | Lo que te llevas | `slideStandard` | Estado en el State · setState · initState/dispose · la lista se pinta desde el estado | Resumen |
| 31 | Para la próxima sesión | `slideSidebarLeftOrange` | La playlist se parte en componentes y el estado sube a la Screen: elevación de estado y funciones como parámetro | · |

**31 slides**, cinco de ellas con simulador en vivo. Cada slide de contenido lleva sus notas de orador
(tecla `S`), sacadas de las lecciones `S0040` a `S0044`.

## Cómo se reutilizan las figuras

- `figuras.py` copia a `slides/00-figuras.js` las 7 figuras de las lecciones de la sesión, les quita el título y las escala al lienzo, como en la sesión 5.
- Fondo `#FBFBFD` de las figuras sobre blanco en las slides con marco institucional.

## Pendiente de decidir con el profesor

- Si el deck se enlaza al inicio de `S0040` (como en las sesiones 1, 2 y 5) o en `S0044`, la última de la sesión.
