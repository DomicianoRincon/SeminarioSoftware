# Plan · Frontend developing

**Curso:** Seminario de Ingeniería de Software · Universidad Icesi
**Sesión:** 1 del bloque de Domiciano (sesión 17 del planeador), semana 9 · *Entorno y primera aplicación*
**Duración:** 2 horas en clase
**Público:** estudiantes de Ingeniería de Sistemas; primer acercamiento al frontend.
**Fuente:** las cinco lecciones de la sección *Sesión 1 · Entorno y primera aplicación* del visor
(`S0003`, `S0004`, `S0005`, `S0006`, `S0001`). El plan sigue su orden y su contenido; no
agrega temas nuevos.

**Estado:** aprobado por el profesor el 2026-09-30, sin la slide "Qué te llevas hoy".

## Qué tiene que lograr

1. Que entiendan qué es el frontend y por qué es un problema de ingeniería distinto del backend.
2. Que ubiquen Flutter en el mapa (web, escritorio, móvil, multiplataforma) y la nube (Supabase vía SDK).
3. Que lleguen con la idea correcta del desarrollo con IA: la IA escribe y ejecuta, ellos dirigen.
4. Que salgan con Flutter instalado y una app corriendo en Chrome.

## Cómo se reutilizan las ilustraciones

Las figuras SVG de las lecciones se pegan tal cual, con dos ajustes:

- **Se recorta el título propio de cada figura** (la franja de arriba del `viewBox`): el título
  lo pone la slide, y así no aparece dos veces.
- **Se escalan al área de contenido** (~1216 × 450 px), con `width` y `height` explícitos.

Las figuras de consola se recortan a la ventana de la terminal y sus tarjetas explicativas
pasan a una columna de texto a la derecha, para que la letra de la consola no quede chica al
escalar. Las figuras ya tienen fondo claro fijo e ids prefijados, así que no chocan entre slides.

El **mapa de las cuatro familias** (728 px de alto) se arma como `slideFourCards`, que se lee
mejor proyectado.

## Slides

| # | Título | Layout | Contenido | Gráfico |
|---|---|---|---|---|
| 1 | Frontend developing | `titleSlideA` | Subtítulo: *Entorno y primera aplicación*. Etiqueta: *Seminario de Ingeniería de Software · Universidad Icesi* | · |
| 2 | El recorrido de hoy | `slideStandard` | Cinco pasos: frontend → panorama → la nube → IA → instalar | `H.pipeline` con íconos |
| 3 | ¿Qué es el frontend? | `sectionSlideEBlue` | Divisor de bloque | · |
| 4 | Dos lados de una misma app | `slideStandard` | Frontend en el dispositivo, backend en servidores, se hablan por internet | SVG `feLados` |
| 5 | Una pantalla, cuatro estados | `slideStandard` | Cargando · vacía · con error · lista. El usuario ve todos; casi siempre solo se diseña el último | SVG `feEstados` |
| 6 | Una base de código, muchas pantallas | `slideStandard` | Celular, tablet, navegador | SVG `feLugares` |
| 7 | interfaz = f(estado) | `sectionSlideEGreen` | La idea que guía el curso: la pantalla se describe a partir del estado | · |
| 8 | Panorama del frontend | `sectionSlideEBlue` | Divisor de bloque | · |
| 9 | Las cuatro familias del frontend | `slideFourCards` | Web · Escritorio · Móvil nativo · Multiplataforma: definición de una línea y frameworks más usados | Componente nativo |
| 10 | ¿Nativo o multiplataforma? | `slideStandard` | Un código por sistema frente a un código para todos | SVG `pfNativo` |
| 11 | ¿Por qué Flutter en este curso? | `slideSidebarLeftBlue` | Un lenguaje (Dart) · Android, iOS, web y escritorio · hoy probamos en Chrome sin emuladores | Panel lateral: íconos de los cuatro destinos |
| 12 | Frontend y la nube | `sectionSlideEBlue` | Divisor de bloque | · |
| 13 | Tu app y los servicios de la nube | `slideStandard` | SDK de Supabase dentro de la app; autenticación, base de datos, storage | SVG `fnServicios` |
| 14 | Un ejemplo: cambiar la foto de perfil | `slideStandard` | Auth → Storage → Base de datos → la pantalla | SVG `fnEjemplo` |
| 15 | Desarrollar con IA | `sectionSlideEBlue` | Divisor de bloque | · |
| 16 | A mano o potenciado con IA | `slideStandard` | Cambia quién escribe el código, no quién tiene que entenderlo | SVG `iaManos` |
| 17 | De un chat a un agente | `slideStandard` | El tool system: leer, buscar, editar, ejecutar sobre tu proyecto | SVG `iaTools` |
| 18 | Un agente en acción | `slideStandard` | Tú pides · la IA usa herramientas · tú autorizas | SVG `iaAgente` (terminal) + explicación a la derecha |
| 19 | Tú al mando | `slideStandard` | Human in the lead frente a human in the loop | SVG `iaMando` |
| 20 | Manos a la obra | `titleSlideF` | Separador de la parte práctica: instalación básica | · |
| 21 | Las piezas de la instalación básica | `slideStandard` | Ya tienes Git y VS Code; la extensión hace el resto | SVG `fiPiezas` |
| 22 | Instalar Flutter con la extensión | `slideStandard` | Los seis pasos dentro de VS Code | SVG `fiPasos` |
| 23 | Comprobar que Flutter responde | `slideStandard` | `flutter --version` | SVG `tcVersion` (terminal) + explicación |
| 24 | Crear el proyecto | `slideStandard` | `flutter create --org icesi.edu.co miapp1` y `cd miapp1` | SVG `tcCreate` (terminal) + explicación |
| 25 | Ver los dispositivos | `slideStandard` | `flutter devices`: el id de Chrome es `chrome` | SVG `tcDevices` (terminal) + explicación |
| 26 | Ejecutar en el navegador | `slideStandard` | `flutter run -d chrome`; teclas `r`, `R`, `q` | SVG `tcRun` (terminal) + explicación |
| 27 | Pruébalo: cambia el título | `slideStandard` | Abre `lib/main.dart` · cambia el texto · guarda · presiona `r` | `H.pipeline` de 4 pasos |
| 28 | Para la próxima sesión | `slideSidebarLeftOrange` | Entorno verificado, corriendo la app de ejemplo (en Chrome, o en emulador o celular con la *Instalación avanzada*) · todo el material está en el visor del curso | Panel lateral: íconos |

**28 slides.** Cada slide de contenido lleva **notas de orador** (tecla `S`) con lo que dice la
lección en texto corrido, para no tener que leerlo de la pantalla.

## Decisiones

- **Sin "Qué te llevas hoy"**: se quitó a pedido del profesor.
- **Título de la portada**: "Frontend developing" (antes "Frontend developing"; cambiado a pedido del profesor el 2026-09-30).
- **Sin agenda con horas**: no hay horario definido para la sesión; si se necesita, se agrega
  una tabla en la slide 2.
- **"Instalar entorno Supabase"** está en el planeador de esta sesión pero no tiene lección
  todavía, así que no entra en el deck.
- **Slide 28** toma la actividad *fuera de clase* del planeador para la sesión 17.

## Dónde queda

`SeminarioSoftware/presentaciones/sesion1/` → `presentacion.html`, publicado en
https://domicianorincon.github.io/SeminarioSoftware/presentaciones/1/ y enlazado al inicio de
la lección `S0003`, la primera de la sesión.

Las figuras de las lecciones se copian al deck con `figuras.py` (en esta carpeta), que las
lee de `SeminarioSoftware/content/` y escribe `slides/00-figuras.js`. Si una lección cambia su
figura, se vuelve a correr `python3 figuras.py` y después el build.
