# Plan · El agente en consola y su contexto

**Curso:** Seminario de Ingeniería de Software · Universidad Icesi
**Sesión:** 4 del bloque de Domiciano (sesión 20 del planeador), semana 10 · *El agente en consola y el archivo de contexto*
**Duración:** 2 horas en clase
**Público:** estudiantes de Ingeniería de Sistemas, con `mi_app_1` como quedó en el taller de la sesión 3 y la Entrega 1 en curso.
**Proyecto de referencia:** `mi_app_1`, la red social profesional del curso.
**Fuente:** las cuatro lecciones de la sección *Sesión 4* del visor (`S0029`, `S0030`, `S0031`, `S0032`). El plan sigue su
orden y su contenido; no agrega temas nuevos.

**Estado:** plan escrito el 2026-10-09 y ajustado ese mismo día al proyecto de la red profesional. **Pendiente la aprobación del profesor**: el deck no se ha construido.

## Qué tiene que lograr

1. Que abran un agente dentro de su proyecto, con un modelo gratuito, y lean lo que hace.
2. Que distingan `plan` de `build` y dejen al agente pidiendo permiso.
3. Que vean, con su propio proyecto, que el agente copia lo que ve e inventa lo que no ve.
4. Que escriban un `AGENTS.md` de seis apartados con lo que ya decidieron en las sesiones 1 a 3 y en la Entrega 1.
5. Que sepan qué es una skill, cómo es su carpeta y por qué la `description` decide.
6. Que salgan con la skill `mer-svg` armada y el MER de su app en `docs/mer.svg`.

## Tiempos

| Bloque | Slides | Minutos |
|---|---|---|
| Apertura | 1 a 3 | 10 |
| El agente en consola | 4 a 10 | 20 |
| El archivo de contexto | 11 a 18 | 25 |
| Skills | 19 a 23 | 15 |
| Taller | 24 a 30 | 35 |
| Cierre | 31 y 32 | 10 |

Quedan 5 minutos de margen. La instalación es tarea previa: en clase solo se comprueba con `opencode --version` o `agy --version`.

## Cómo se reutilizan las ilustraciones

Mismo criterio de las sesiones 1 a 3: poco texto, la figura de la lección ocupa la slide y lo que dice la lección va en
las notas de orador.

- **Se recorta el título propio de cada figura**: lo pone la slide.
- **Frames de consola**: se recortan a la terminal y sus tarjetas.
- **`skSkillMd`** se recorta al editor y al panel.
- **De `tsCarpetas` y `skCarpeta`** se usa el árbol completo.
- **El fondo `#FBFBFD` de las lecciones pasa a blanco**.

## Slides

| # | Título | Layout | Contenido | Gráfico |
|---|---|---|---|---|
| 1 | El agente en consola y su contexto | `titleSlideA` | Subtítulo: *AGENTS.md y tu primera skill* | · |
| 2 | El recorrido de hoy | `slideStandard` | El agente → el contexto → las skills → taller | `H.bigPipeline` |
| 3 | Lo que te llevas hoy | `slideStandard` | Tres archivos nuevos: `AGENTS.md`, la skill `mer-svg` y `docs/mer.svg` | SVG `tsFlujo` |
| 4 | El agente en consola | `sectionSlideEBlue` | Divisor de bloque | · |
| 5 | Un modelo con herramientas | `slideStandard` | Repaso de la sesión 1: el tool system | SVG `agAgente` |
| 6 | Dos agentes, a elección | `slideStandard` | OpenCode o Antigravity CLI · qué hace cada uno sin preguntar | SVG `agReglas` |
| 7 | Se abre dentro del proyecto | `slideSidebarLeftOrange` | `cd` al proyecto · `opencode` · `/models` y un modelo gratuito · nada de datos personales | Panel lateral con íconos |
| 8 | La primera pregunta | `slideStandard` | Tú preguntas · el agente lee · responde | SVG `agSesion` |
| 9 | Dos modos | `slideStandard` | `plan` propone, `build` hace, Tab cambia | SVG `agModos` |
| 10 | Que pida permiso | `slideStandard` | `opencode.json` en OpenCode · `/permissions` en Antigravity CLI | SVG `agPermiso` |
| 11 | El archivo de contexto | `sectionSlideEBlue` | Divisor de bloque | · |
| 12 | Lo que el agente ve y lo que no | `slideStandard` | Pedido, archivos y `AGENTS.md` · lo que no ve, lo inventa | SVG `cxQueVe` |
| 13 | Haz la prueba | `titleSlideF` | Separador: *Crea la pantalla de inicio con las publicaciones recientes* | · |
| 14 | El mismo pedido, sin y con contexto | `slideStandard` | Copió el estilo · inventó los datos · inventó la app | SVG `cxAntesDespues` |
| 15 | El agente copia lo que ve e inventa lo que no ve | `sectionSlideEGreen` | La idea de la sesión | · |
| 16 | Crear el archivo con /init | `slideStandard` | Un borrador que sale de tu código | SVG `cxInit` |
| 17 | Los seis apartados | `slideStandard` | De dónde sale cada uno | SVG `cxPartes` |
| 18 | Un documento vivo | `slideSidebarLeftOrange` | Error de una vez: se corrige el código · error que se repite: una línea en `AGENTS.md` · corto, una página | Panel lateral con íconos |
| 19 | Skills | `sectionSlideEBlue` | Divisor de bloque | · |
| 20 | Una skill es una carpeta | `slideStandard` | `SKILL.md`, `references/` y `assets/` | SVG `skCarpeta` |
| 21 | Las partes de SKILL.md | `slideStandard` | `name`, `description` y el cuerpo | SVG `skSkillMd` |
| 22 | Cuándo se carga | `slideStandard` | Siempre · si coincide · si un paso lo pide | SVG `skCarga` |
| 23 | AGENTS.md o skill | `slideSidebarLeftOrange` | Todo el proyecto: `AGENTS.md` · una tarea que se repite: skill · una sola vez: el pedido | Panel lateral con íconos |
| 24 | Manos a la obra | `titleSlideF` | Separador: *Taller · Tu primera skill* | · |
| 25 | Tu modelo, en texto | `slideStandard` | `docs/modelo.md`: una lista por tabla y las relaciones | Bloque de código |
| 26 | Tres archivos | `slideStandard` | `SKILL.md`, `references/estilo.md` y `assets/ejemplo.svg` | SVG `skCarpeta`, resaltando `mer-svg/` |
| 27 | Pide el diagrama | `slideStandard` | Sin nombrar la skill · tarda de tres a cinco minutos | SVG `tsUso` |
| 28 | Así salió la primera vez | `slideStandard` | Se ve ordenado y está mal: `seguidores` quedó unida a `mensajes` | SVG `tsPrimerIntento` |
| 29 | Dos reglas más en la skill | `slideStandard` | El mismo modelo, después de corregir `SKILL.md` | SVG `tsResultado` |
| 30 | Tu proyecto al terminar | `slideStandard` | Lo nuevo dirige al agente o lo produjo el agente | SVG `tsCarpetas` |
| 31 | Qué se corrige dónde | `sectionSlideEGreen` | *Lo que se va a repetir se corrige en las instrucciones, no en el resultado* | · |
| 32 | Para la próxima sesión | `slideSidebarLeftOrange` | Llevar todo al repo del equipo · el MER a la Entrega 1 · la sesión 5: generar una pantalla y auditarla | Panel lateral con íconos |

**32 slides.** Cada slide de contenido lleva **notas de orador** (tecla `S`) con lo que dice la lección.

## Decisiones

- **Título de la portada**: "El agente en consola y su contexto". El del planeador es más largo; el subtítulo nombra la skill.
- **La demo en vivo va entre las slides 13 y 14**: primero el pedido sin contexto en el proyecto del profesor, después la figura.
- **Antigravity CLI comparte slides con OpenCode** (6 y 10): la lección tiene una sección para cada uno.
- **La slide 5 usa `agAgente`**, el panel de la figura `iaTools` de la sesión 1, que también abre `S0029`.

## Por confirmar con el profesor

- Si el enlace a la presentación va al inicio de `S0029`, la primera lección, o en `S0032`, el taller, como se hizo en la sesión 3.
