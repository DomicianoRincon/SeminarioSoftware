# Manifest · Seminario de Ingeniería de Software

Qué sesiones del plan de curso ya tienen su contenido en el visor. El plan completo, con lo que se hace en clase, fuera de clase y los entregables, está en [`docs/planeador.md`](docs/planeador.md). Los resultados de aprendizaje y la evaluación están en [`docs/syllabus.md`](docs/syllabus.md).

Este repositorio cubre **las últimas 8 semanas del curso (semanas 9 a 16)**, que según el syllabus son las unidades 3 y 4. El planeador numera sus sesiones de la **17 a la 32**, porque las 16 primeras son de las unidades 1 y 2, que dicta otro docente. Aquí se cuentan como **sesión 1 a 16**: `sesión del visor = sesión del planeador − 16`, con dos sesiones por semana.

**Estados:** ✅ completa en el visor · 🟡 parcial · ⬜ pendiente

## Sesiones

| Sesión | Planeador | Semana | Unidad | Tema | Estado | Lecciones en el visor |
|---|---|---|---|---|---|---|
| 1 | 17 | 9 | 4 | Entorno y primera aplicación | 🟡 | `S0003` ¿Qué es el frontend? · `S0004` Panorama del frontend · `S0005` Frontend y la nube · `S0006` Desarrollar con IA · `S0001` Instalación básica · sección *Instalación avanzada*: `0019`, `0020`, `0021`, `0022` |
| 2 | 18 | 9 | 4 | Componentes | ✅ | `S0056` Repositorio de arranque · `S0010` El proyecto por dentro · `S0011` Text · `S0012` Image · `S0013` Button · `S0014` TextField · `S0016` Column · `S0017` Row · `S0015` StatelessWidget: tu primer componente · `S0018` Taller · Componentes |
| 3 | 19 | 10 | 4 | Pantallas con componentes | 🟡 | `S0057` Repositorio de arranque · `S0020` Scaffold · `S0021` SafeArea · `S0022` Container y Padding · `S0023` Expanded · `S0024` SingleChildScrollView · `S0025` Armar una pantalla · `S0026` Taller · Pantallas |
| 4 | 20 | 10 | 3 | El agente en consola y el archivo de contexto | 🟡 | `S0058` Repositorio de arranque · `S0029` El agente en consola · `S0030` El archivo de contexto · `S0031` Skills · `S0032` Taller · Tu primera skill · `S0033` Una skill para armar pantallas |
| 5 | 21 | 11 | 3 | Servidores MCP | 🟡 | `S0059` Repositorio de arranque · `S0034` ¿Qué es MCP? · `S0035` Configurar MCP en Antigravity · `S0036` Prototipado con Stitch MCP · `S0037` Automatización con Playwright MCP · `S0039` Colaboración con GitHub MCP · `S0038` Taller · Servidores MCP |
| 6 | 22 | 11 | 4 | Stateful widget y setState | 🟡 | `S0060` Repositorio de arranque · `S0040` Estado: Stateless frente a Stateful · `S0041` setState: el contador de flutter create · `S0042` Ciclo de vida: initState, dispose y TextEditingController · `S0043` Creador de playlists: la lista en texto · `S0044` Creador de playlists: el componente SongCard |
| 7 | 23 | 12 | 4 | Elevación de estado y funciones como parámetro | 🟡 | `S0061` Repositorio de arranque · `S0046` El estado entra como parámetro · `S0047` Funciones como parámetro · `S0048` Modelos con copyWith · `S0049` Prop drilling · `S0045` Taller · Playlist con estado elevado |
| 8 | 24 | 12 | 4 | Navegación entre pantallas | 🟡 | `S0062` Repositorio de arranque · `S0050` Taller · Playlist navegable · `S0051` La pila de pantallas · `S0052` Rutas nombradas: pushNamed y pop · `S0053` pushNamedAndRemoveUntil: rehacer la pila · `S0054` Pasar datos a la pantalla nueva · `S0055` Devolver un resultado al cerrar |
| 9 | 25 | 13 | 4 | Navegación con bottom navigation bar | 🟡 | `S0064` Repositorio de arranque · `S0065` Taller · Playlist con secciones · `S0066` BottomNavigationBar: una pieza del Scaffold · `S0067` El índice en el estado · `S0068` IndexedStack: Pages que recuerdan |
| 10 | 26 | 13 | 3 | Spec Driven Development | ⬜ | |
| 11 | 27 | 14 | 3 y 4 | Servicio de base de datos | ⬜ | |
| 12 | 28 | 14 | 3 y 4 | Servicio de autenticación | ⬜ | |
| 13 | 29 | 15 | 3 y 4 | Servicio de storage | ⬜ | |
| 14 | 30 | 15 | 3 y 4 | Funciones como servicio | ⬜ | |
| 15 | 31 | 16 | 3 y 4 | Entrega final I (equipos 1 a 3) | ⬜ | |
| 16 | 32 | 16 | 3 y 4 | Entrega final II (equipos 4 a 6) y cierre | ⬜ | |

## Material de apoyo (no atado a una sesión)

| Sección del visor | Lecciones | Origen |
|---|---|---|
| Curso | `S0002` Programa del curso · `S0019` Playground | Propias. El programa, hecho a partir de `docs/syllabus.md`. El Playground es un DartPad con la app mínima de `S0010` (el mismo gist de su *Ejemplo completo*) |
| Entregables | `S0007`, `S0008`, `S0009`: las tres entregas del proyecto, **solo qué se entrega** | Propias, hechas a partir de la tabla *Entregas* de `docs/planeador.md`. Fechas, sesiones, uso de IA y pesos están ocultos en `docs/entregables.md` hasta que se confirmen |
| Dart | `0001`, `0006` a `0012` | Sección *Dart basics* de Aplicaciones Móviles |
| IA | `S0063` Skills para tu proyecto | Propia (2026-10-28, pedido del profesor). Cuatro skills en el interactivo `skill-files`, portado de `0047` de Computación 2: `disenador-bd` y `flutter-componentes`, nuevas, y `mer-svg` y `flutter-pantallas`, copiadas de `recursos/sesion4/` (a `flutter-pantallas` se le quitó «componente» de la description). Fuente en `tools/skills/`, se pasan al simulador con `python3 tools/skills_data.py`. Figura `iaSkillsMapa` en `tools/ia_figuras.py`. Las plantillas de `flutter-componentes` son de una lista de compras y no de la playlist, para no entregar la solución del taller de la sesión 8 |

## Detalle por sesión

### Sesión 1 · Entorno y primera aplicación

**Presentación:** `presentaciones/sesion1/` · *Frontend developing*, publicada en
https://domicianorincon.github.io/SeminarioSoftware/presentaciones/1/ y enlazada al inicio de `S0003`.

| Lo que pide el planeador | Dónde está en el visor |
|---|---|
| Presentación de los profesores y de las unidades 3 y 4 | En vivo, sin lección |
| Qué es el desarrollo frontend multiplataforma | `S0003` ¿Qué es el frontend? y `S0004` Panorama del frontend |
| Instalación del SDK, el editor y el emulador | `S0001` Instalación básica (VS Code + Chrome). El emulador está en *Instalación avanzada*: `0019`, `0022` |
| Primera aplicación y hola mundo | `S0001` (crear y ejecutar en Chrome, hot reload) y `0020` Tu primera app Flutter |
| Introducción a los servicios de la nube *(el planeador la pone en la sesión 20; se adelantó)* | `S0005` Frontend y la nube: autenticación, base de datos y storage vía SDK |
| Instalar entorno Supabase | ⬜ **Pendiente.** Móviles tiene `lessonH1.md` (*Instalación de supabase*, `0051`) y `lessonX5.md` (*Self-hosted Supabase*, `0054`) para reutilizar |
| *Fuera de clase:* entorno verificado, corriendo en emulador o dispositivo propio | *Instalación avanzada*: `0021` Ejecutar las apps y `0022` Configurando dispositivos virtuales |

### Sesión 2 · Componentes

**Presentación:** `presentaciones/sesion2/` · *Componentes* · 36 slides. Enlazada al inicio de `S0010`.

| Lo que pide el planeador | Dónde está en el visor |
|---|---|
| Recorrido por main.dart y por la estructura de carpetas | `S0010` El proyecto por dentro. Usa la convención del curso (`theme/`, `models/`, `components/`, `screens/`, `pages/`) y arranca con `routes:` + `initialRoute`, con una sola ruta |
| Paradigma declarativo frente a imperativo | **Fuera del visor**: el profesor quitó el apartado de `S0010` el 2026-10-02. Queda `interfaz = f(estado)` en `S0003`, de la sesión 1 |
| Widgets básicos: Text, Image (asset y network) y botones | `S0011` Text · `S0012` Image · `S0013` Button |
| *(añadido por el profesor)* TextField | `S0014` TextField, **solo apariencia**: `InputDecoration`, `obscureText`, `keyboardType`. Leer el texto (controller y estado) queda para la sesión 6 |
| *(añadido por el profesor; el planeador lo pone en la sesión 19)* Column y Row | `S0016` Column · `S0017` Row: `children`, los dos ejes, `mainAxisAlignment`, `crossAxisAlignment` y `SizedBox`. `Expanded`, `Container`, `Padding` y `SingleChildScrollView` quedan para la sesión 3 |
| Concepto de componente como pieza reutilizable | `S0015` StatelessWidget: tu primer componente |
| Taller: componentes Stateless montados en una pantalla | `S0018` Taller · Componentes: **solo componentes**, seis. Empieza por dos nuevos, `PrimaryButton` (azul) y `SecondaryButton` (con borde), los dos con un icono y un texto en una `Row`. Sigue `StatsRow`, un componente compuesto con tres `StatCard` (el de `S0015`), y dos del Lab 1 de Móviles (elemento de conversación, bloque de información de perfil) y cierra con `ContactCard`, una versión mínima del perfil (foto, nombre y usuario) pensada para una fila horizontal de contactos sugeridos |
| *Fuera de clase:* terminar los componentes del taller | `S0018`. Armar la pantalla de perfil con ellos es el taller de la sesión 3 (`S0026`) |

Notas:

- Las lecciones heredadas `lessonD4A` a `lessonD4D` (`0027` a `0030`) y `lessonD1` (`0023`) **no** se usaron: se escribieron propias, con figuras de código anotado. Siguen en `content/` como cantera.
- El Lab 1 pide `Row` y `Column`, que el planeador pone en la sesión 3. Se adelantaron a esta sesión (`S0016`, `S0017`), antes de `S0015`, para que el taller se pueda hacer. La sesión 3 retoma el layout desde `Expanded`.
- El taller **no** es `lab1.md` (`0033`): ese mezcla componentes y pantallas. `S0018` reutiliza sus imágenes `Lab1Item1.png` a `Lab1Item3.png` y el mismo Figma, y deja el armado para la sesión 3. `lab1.md` sigue en `content/` como cantera.
- El scroll horizontal de los contactos sugeridos **no** está en el taller: `ContactCard` se prueba en una `Row`. La fila deslizable es para la sesión 3.
- Las 24 figuras salen de `tools/sesion2_figuras.py` (ver `CLAUDE.md` → *Código: frame de editor SVG*).

### Sesión 3 · Pantallas con componentes

**Presentación:** `presentaciones/sesion3/` · *Pantallas con componentes* · 42 slides · https://domicianorincon.github.io/SeminarioSoftware/presentaciones/3/. Enlazada al inicio de `S0026`, el taller, por pedido del profesor (en las sesiones 1 y 2 va en la primera lección). Pendiente la revisión del profesor.

| Lo que pide el planeador | Dónde está en el visor |
|---|---|
| Scaffold y SafeArea como andamiaje de una pantalla | `S0020` Scaffold (`appBar`, `body`, `backgroundColor`, `floatingActionButton`) · `S0021` SafeArea, con la regla del curso: el `body` de toda Screen empieza con un `SafeArea` · `S0028` AppBar *(añadido por el profesor, 2026-10-07)*: `title`, `actions`, `leading`, `centerTitle`, `backgroundColor` y `foregroundColor` · `S0027` BottomNavigationBar *(añadido por el profesor, 2026-10-07)*: **solo cómo se ve**, con tres botones y `currentIndex` fijo. Que responda al toque queda para la sesión 9 |
| Composición: armar una pantalla a partir de componentes propios | `S0025` Armar una pantalla: **solo** la estructura de una Screen (archivo en `lib/screens/`, clase `XxxScreen`, `Scaffold` como raíz) y cómo anotarla en `main.dart` (`import`, `routes`, `initialRoute`), reescrita a pedido del profesor el 2026-10-07. El orden de las capas (figura `apCapas`) y el `import` de componentes pasaron a `S0026`, donde el estudiante arma `ProfileInfo` + `StatsRow` como bloque 1 |
| Layout con Column, Row, Expanded, Container, Padding y SingleChildScrollView | `Column` y `Row` se adelantaron a la sesión 2 (`S0016`, `S0017`). Aquí: `S0022` Container y Padding · `S0023` Expanded (con `flex` y `Spacer`) · `S0024` SingleChildScrollView (vertical y horizontal) |
| Convención Screen frente a Page | Apartado *Una pantalla es una Screen* de `S0020`. **Solo Screen**: Page se nombra con una figura y se remite a la sesión 9 (decisión del profesor, 2026-10-07) |
| Taller: armar dos pantallas del reto con componentes propios y suministrados | `S0026` Taller · Pantallas: **una sola pantalla**, `ProfileScreen` (`/profile`, con barra y scroll, la pantalla de la figura `swPantalla` de `S0015`). La de inicio de sesión se quitó del taller (decisión del profesor, 2026-10-07). Va en **cuatro bloques numerados**, cada uno con su figura (`tpBloque1` a `tpBloque4`): información del perfil, botones, contactos sugeridos y últimas conversaciones. Primero se arman en la pantalla y después cada uno se saca a una **sección** en `lib/components/` (`ProfileSummarySection`, `ProfileActionsSection`, `SuggestedContactsSection`, `RecentChatsSection`); la primera va resuelta como ejemplo (reescritura pedida por el profesor, 2026-10-07). El componente suministrado es `SectionHeader`, con su código completo |
| *Fuera de clase:* lectura sobre archivos de contexto para agentes (CLAUDE.md / AGENTS.md) | ⬜ **Pendiente.** El profesor no ha definido la lectura; `S0026` no la menciona |

Notas:

- **Sin tablas** en las siete lecciones (regla del profesor del 2026-10-04): una figura y uno o dos párrafos por apartado. Las de la sesión 2 sí tienen tablas.
- **Imports con `package:miapp1/`** desde esta sesión. Se corrigieron los tres imports relativos que quedaban en `S0010`, `S0015` y `S0018`.
- **SafeArea no se nota en Chrome.** `S0021` lo dice, y su *Ejemplo completo* finge las zonas del sistema con un `MediaQuery` en el `builder` de `MaterialApp`.
- Se cambia de pantalla editando `initialRoute`: la navegación es de la sesión 8. Los botones siguen con `print`.
- El taller se comprobó armando las dos pantallas en un proyecto de prueba con los siete componentes de `S0018`: `flutter analyze` solo reporta `avoid_print`.
- `StatsRow` con `spaceEvenly` se desborda en pantallas de 360 px de ancho. El taller lo convierte en una pista: envolver cada `StatCard` en un `Expanded`.
- El paso de separar en secciones del taller **no se ha comprobado en un proyecto real**: la comprobación de arriba es anterior a la reescritura.
- Las 28 figuras salen de `tools/sesion3_figuras.py`, que reutiliza `code_frame.py` y varios dibujos de `sesion2_figuras.py`.
- El *Ejemplo completo* de `S0020` a `S0025` y los de `S0027` y `S0028` necesita su gist público en la cuenta `Domiciano`. Mientras el bloque diga `trycode=PENDIENTE_S2x`, la lección no se debe publicar.

### Sesión 4 · El agente en consola y el archivo de contexto

**Presentación:** ⬜ pendiente (`presentaciones/sesion4/`).

| Lo que pide el planeador | Dónde está en el visor |
|---|---|
| Asistentes de IA en consola: qué son y cómo se opera con ellos | `S0029` El agente en consola: OpenCode o Antigravity CLI, cada uno con su instalación, y la primera pregunta de solo lectura. `S0006`, de la sesión 1, ya había presentado la idea |
| Modos de operación y niveles de autonomía | `S0029`: las reglas de permiso de cada agente (qué hace sin preguntar), planear antes de hacer y `/undo` |
| Gestión del contexto: qué ve el agente | `S0030` El archivo de contexto, apartados *Lo que el agente ve* y *El mismo pedido, dos veces* |
| Construcción del primer CLAUDE.md/AGENTS.md con /init | `S0030`: `/init` y los seis apartados, con el `AGENTS.md` completo de la red profesional y su `docs/modelo.md` |
| El archivo de contexto es un documento vivo | `S0030`, apartado *Un documento vivo* |
| Introducción a los 3 servicios básicos: data, storage y auth | Se adelantó a la sesión 1: `S0005` Frontend y la nube |
| *(adelantado de la sesión 5, decisión del profesor del 2026-10-09)* Skills: qué son y cómo se crean | `S0031` Skills (la carpeta, `SKILL.md`, cuándo se carga) y `S0032` Taller · Tu primera skill: arman `mer-svg`, que dibuja el MER de la Entrega 1 en SVG a partir de `docs/modelo.md` |
| *Fuera de clase:* completar el CLAUDE.md del repositorio del equipo | Cierre de `S0030` y de `S0032`: escribir el `AGENTS.md` y el `docs/modelo.md` de la app del equipo y llevar la skill a su repo |

Notas:

- **Proyecto de referencia: `mi_app_1`**, el del profesor (`github.com/Domiciano/262SeminarioApp1`), tratado como una **red social profesional** al estilo de LinkedIn (decisión del profesor, 2026-10-09; antes el ejemplo era una biblioteca). Las cuatro lecciones usan ese nombre de paquete, sus componentes y un modelo de cuatro tablas: `usuarios`, `publicaciones`, `seguidores` y `mensajes`.
- **Dos agentes, a elección**: `S0029` tiene una sección para OpenCode y otra para Antigravity CLI (`agy`), cada una con instalación, apertura y reglas de permiso (`opencode.json` en uno, `/permissions` en el otro). Las demás lecciones enseñan el estándar que leen los dos: `AGENTS.md` y `.agents/skills/<nombre>/SKILL.md`. Se dice una vez que en Claude Code el archivo se llama `CLAUDE.md`.
- **El experimento de `S0030` se corrió de verdad** el 2026-10-09 sobre una copia de `mi_app_1`, con OpenCode 2.0.25 y el modelo gratuito `opencode/big-pickle`. Pedido: *Crea la pantalla de inicio con las publicaciones recientes y regístrala en la app*. Sin contexto el agente copió el estilo (tarjetas, colores, avatar, imports `package:`) e inventó foto por publicación, contadores de "me gusta" y de comentarios y un botón de compartir; además borró la `HomeScreen` de prueba de `main.dart` y reescribió `test/widget_test.dart`. Con el `AGENTS.md` y el `docs/modelo.md` de la lección mostró solo autor, usuario, cargo, texto y fecha, en un componente `PostItem`, y no tocó `test/` (lo avisó). Siguió borrando la `HomeScreen` de prueba: es el ejemplo de *Un documento vivo*.
- **La skill `mer-svg` se probó** el mismo día con ese modelo. El primer diagrama de la red profesional salió con un error real: la línea de `seguidores` unida a `mensajes` y el pie desbordado (figura `tsPrimerIntento`). Se agregaron dos reglas a `SKILL.md` y el segundo salió correcto (figura `tsResultado`). Las dos figuras van sin retoques y son la historia de los pasos 6 a 8 de `S0032`. El `assets/ejemplo.svg` de la skill es un diagrama de reserva de canchas, generado con la misma skill en una prueba anterior.
- Cada diagrama tarda entre tres y cinco minutos, y varias corridas se quedaron sin responder hasta cortarlas a los ocho o nueve minutos.
- Los modelos gratuitos de OpenCode Zen funcionaron **sin cuenta ni tarjeta**. La lista rota: si `big-pickle` desaparece, se elige otro.
- **Sin comprobar**: la instalación en Windows de los dos agentes; el aviso de permiso de OpenCode en pantalla (la figura está simplificada); y todo lo de Antigravity CLI, que sale de su documentación oficial (`antigravity.google/docs/permissions` y `/docs/cli`) porque faltó iniciar sesión en `agy`: los pasos de `/permissions`, el alcance *Project*, `/model`, `/undo` y que reconozca `AGENTS.md` y `.agents/skills/`.
- Los archivos probados están en `recursos/sesion4/` (`AGENTS.md`, `opencode.json`, `docs/modelo.md`, los dos diagramas y la skill con sus reglas finales). `S0030` y `S0032` se generaron desde ahí: si se cambia un archivo, hay que cambiar la lección.
- Las 30 figuras salen de `tools/sesion4_figuras.py`. `agAgente` es el panel *Agente en consola* de la figura `iaTools` de `S0006`, recortado: si esa figura cambia, hay que volver a inyectar. `check.py` marca como error la URL del instalador en `agAntigravity`: es texto del comando mostrado, no un recurso que el SVG cargue.
- `S0032` muestra primero la estructura completa de la skill (`tsEstructura`) y la arma un elemento por paso (`tsPaso1` a `tsPaso4`). Las lecciones no llevan *Ejemplo completo*: no tienen código Dart.
- **`S0033` Una skill para armar pantallas** *(adelantada de la sesión 5, pedido del profesor del 2026-10-09)*: entrega la skill `flutter-pantallas` ya escrita (`SKILL.md`, `references/widgets.md` y dos plantillas en `assets/`). Limita al agente a la paleta de widgets de las sesiones 2 y 3 más lo que ya usa `mi_app_1` (`Card`, `spacing`), sin estado ni navegación, y le hace pensar en componentes reutilizables. Se probó el 2026-10-09 con el modelo gratuito: al pedirle la pantalla de mensajes reutilizó `ChatItem`, usó `Column` dentro de `SingleChildScrollView` en vez de `ListView` y no creó componentes repetidos. Esa corrida es la de las figuras `fpUso` y `fpComponentes`. `S0031` muestra además la carpeta `scripts/` en su figura de estructura, atenuada, aunque ninguna de las dos skills la usa.
- `S0033` **no lleva *Ejemplo completo***, aunque tiene bloques `dart`: son las plantillas de la skill, no código para ejecutar. Si el profesor lo quiere, falta crear el gist.
- La sesión 5 queda para practicar con esa skill: generar pantallas de la app del equipo y auditarlas contra el `AGENTS.md`.

### Sesión 6 · Stateful widget y setState

**Presentación:** ⬜ pendiente (`presentaciones/sesion6/`). Su `plan.md` necesita la aprobación del profesor antes de armar las slides.

| Lo que pide el planeador | Dónde está en el visor |
|---|---|
| Stateless frente a Stateful: por qué el estado vive en el objeto State | `S0040`, con las figuras `ewPantalla` (una app de música con sus datos y flechas desde cada variable de estado a lo que la muestra) y `ewAnatomia` y el interactivo `state-tree bulb`: el bombillo de su ejemplo, con `_isOn` en la sección *Estado* unida a `Icon`, `Text` y `FilledButton`; *Reconstruir App* cambia el número del widget y conserva el State y `_isOn` |
| El árbol de widgets y su reconstrucción, con un print en build | `S0041` abre con el interactivo `state-tree forget`: árbol del contador (con vista de código alternable) y `_counter` en el bloque *Estado*, unido al `Text`; cada toque se anima en cinco pasos y el interruptor *Olvidar setState* quita el `setState` del código. Luego el `print` en `build` y la figura `ssCiclo`. El simulador `state-counter` se retiró de la lección (2026-10-15): el árbol lo cubre |
| Ciclo de vida: initState y dispose, con el TextEditingController | `S0042`: figura `lcLinea`, interactivo `state-lifecycle` y el error `setState() called after dispose()` con `mounted`. Cierra lo que `S0014` dejó pendiente (leer un `TextField`) |
| Contador hola mundo sobre estados | `S0041`: el sumador de `flutter create` línea a línea, con el interactivo `state-tree forget` |
| Primera interacción de usuario: funciones | `S0043` con `_addSong` (`onPressed: () => _addSong()`). El apartado *Pasar una función al botón* de `S0041` se quitó el 2026-10-21 (pedido del profesor) |
| Taller de dos sesiones, parte 1 | **Creador de playlists** en vez de la agenda de contactos (decisión del profesor, 2026-10-15). `S0043` (lista en `Text`) y `S0044` (componente `SongCard`, entregado) lo explican con el interactivo `playlist`. **El taller `S0045` se movió a la sesión 7 el 2026-10-22** (decisión del profesor: lo más probable es que los estudiantes no lo hagan, así que la sesión 7 arranca del *Ejemplo completo* de `S0044`). Sus cuatro mejoras se repartieron: la lista vacía en `S0046`, quitar con `Function()` y el aviso de datos faltantes en `S0047`, y el contador en el nuevo taller |
| *Fuera de clase:* dar estado a un formulario de la app del equipo | No se asigna: las sesiones del bloque son de clase y no dejan tarea (decisión del profesor, 2026-10-15) |

Notas:

- **Diagramas interactivos**: bloque nuevo ` ```interactive ` del visor (`classnotesapp/src/components/interactive/`). Los simuladores son JavaScript plano en `flutterStateSims.js`, sin React, para que el mismo archivo sirva en la presentación. Cinco: `state-counter`, `hot-reload`, `state-tree`, `state-lifecycle` y `playlist` (con las opciones `cards` y `forget`). Desde el 2026-10-21 `playlist` es un escenario de `state-tree` (árbol, código, bloque Estado y pasos), y `state-lifecycle` se rehízo para `S0042`: teléfono interactivo y fases del ciclo de vida unidas por flechas.
- **`S0043` usa el código mínimo que funciona** (pedido del profesor, 2026-10-15): controllers creados en la declaración, sin `initState`, sin validar, sin `clear()`, sin estilos. `S0044` parte de ese mismo código y solo cambia el `Text` por `SongCard`. Validar y limpiar el formulario pasó a la mejora 2 del taller. El simulador `playlist` hace exactamente lo mismo (agrega canciones vacías).
- **El modelo `Song` no lleva `copyWith`** en la sesión 6: llega en `S0048`, en la sesión 7.
- Los cinco *Ejemplo completo* pasaron el analizador de DartPad sin avisos y tienen su gist público en `Domiciano`. Todas las Screens con `SafeArea` en el `body`.
- Las 9 figuras salen de `tools/sesion6_figuras.py`. `check.py` limpio.
- **El taller se comprobó** el 2026-10-15 armando `playlist_app` resuelto (con las cuatro mejoras y la estructura del curso) en un proyecto de prueba: `flutter analyze` sin avisos. No se ejecutó en un dispositivo.

### Sesión 7 · Elevación de estado y funciones como parámetro

**Presentación:** ⬜ pendiente (`presentaciones/sesion7/`). Su `plan.md` necesita la aprobación del profesor antes de armar las slides.

**Punto de partida:** el *Ejemplo completo* de `S0044`, no el taller de la sesión 6 (decisión del profesor, 2026-10-22). Cada lección termina con un *Ejemplo completo* que es la continuación exacta del anterior. El orden en el visor es `S0045` (el taller como meta), `S0049`, `S0046`, `S0047` y `S0048`.

| Lo que pide el planeador | Dónde está en el visor |
|---|---|
| Se retoma la playlist con todo en un archivo; el estado sube a la Screen y los componentes lo reciben por constructor | `S0046` abre con el problema (pedido del profesor, 2026-10-22): la app no está hecha de piezas. Interactivo `compose` con dos pestañas, *Sin componentes* (el punto de partida, un solo State con líneas a cada widget que usa cada variable) y *Con componentes* (la app del taller, con `PlaylistSummary`, `SongForm`, `SongList` y `SongCard`, y dos dueños de estado). La regla de los tres stateholders (solo la Screen, la Page y el formulario son `StatefulWidget`) no se enuncia en la lección: la sección *Quién guarda y quién muestra* y su figura se quitaron a pedido del profesor (2026-10-22), porque `compose` ya lo muestra. Primer corte: `SongList(songs)`, con la lista vacía resuelta adentro. El apartado *Pruébalo* con `lift` también se quitó (pedido del profesor, 2026-10-22): la lección termina en el primer corte y su *Ejemplo completo* |
| Funciones como parámetro: el hijo reporta hacia arriba sin conocer al padre | `S0047`, rehecha alrededor del botón de eliminar (pedido del profesor, 2026-10-23). Abre con el interactivo `callback` y sigue con tres apartados, uno por nivel: *la función nace junto al estado* (`_deleteSong` en la Screen), *SongList solo la pasa* (`Function(Song)`, prop drilling de una función) y *SongCard la conecta al botón* (`Function()` en `onPressed`). Luego `SongForm` como `StatefulWidget` dueño de su borrador con `widget.onAdd(song)`. La figura `fpFlechas` se retiró: el interactivo la reemplaza |
| Prop drilling: qué es, hasta dónde se tolera y qué señal da | `S0049`, justo después del taller (pedido del profesor, 2026-10-23), reescrita como **artículo corto e introductorio** con tres apartados: *Qué es*, *Cuándo es un problema* y *En este curso*. Figura animada `pdCamino` (6 pasos de 2,5 s): a la izquierda la pantalla se construye desde blanco, la barra de `PlaylistScreen`, el esqueleto de `SongList` y una `SongCard` por vuelta del `for` (3 canciones); a la derecha el código de los tres componentes en vertical, con flechas del parámetro al constructor del siguiente y el bloque activo iluminado. Luego `pdNiveles` (drilling de datos) y las tres señales en una frase. Sin *Ejemplo completo* ni interactivo |
| Modelos simples con copyWith | `S0048`, **más corta** (pedido del profesor, 2026-10-23) y con el botón de me gusta de `SongCard` como ejemplo: `isFavorite` en `Song`, el corazón que sube como la papelera (`onToggleFavorite`), el error `can't be used as a setter because it's final`, `copyWith` y `_songs[index] = song.copyWith(...)`. Figura `cwCopia`. Se quitaron el interactivo `lift fav` y el apartado sobre reemplazar la lista entera |
| Taller de dos sesiones, parte 2 | `S0045`, **primera lección de la sesión** (pedido del profesor, 2026-10-22): presenta el taller en resumen como la meta de la sesión, sobre el **mismo repositorio** `playlist_app` de la sesión 6 (sin `flutter create` ni pasos de montaje). Figuras `taMeta` (la app final, con `PlaylistSummary` arriba del formulario) y `taCarpetas` (un archivo por clase). Dos mejoras en una línea cada una: el resumen y solo favoritas (la calificación con estrellas se quitó a pedido del profesor, 2026-10-22: las tarjetas solo tienen favorita y eliminar), más la prueba de los `print` en `build`. Las pistas detalladas que tenía se quitaron |
| *Fuera de clase:* reorganizar la app del equipo | No se asigna: las sesiones del bloque son de clase y no dejan tarea |

Notas:

- **Interactivo `callback`** (`S0047`): tres niveles apilados (PlaylistScreen con el estado y `_deleteSong`, SongList que solo pasa la función, SongCard con el botón), cada uno con su código, y un teléfono a la izquierda. Recorrido guiado de 6 pasos con *Anterior* y *Siguiente*: el estado, la función, «¿y el botón?» (las papeleras laten y aparece `IconButton(onPressed: ¿?)`), baja a SongList, baja a SongCard y al botón. Después cada papelera sube la llamada un nivel por paso hasta el `setState`.
- **Interactivo `lift`** (`flutterStateSims.js`): ya no lo usa ninguna lección (`S0046`, `S0049`, `S0047` y `S0048` lo fueron quitando a pedido del profesor). Queda registrado con sus opciones `events` y `fav`.
- Los tres *Ejemplo completo* (`S0046`, `S0047` y `S0048`; `S0049` reutiliza el de `S0048`) pasaron `flutter analyze` y el analizador de DartPad sin avisos, y tienen gist público en `Domiciano`.
- **La solución del taller se comprobó** el 2026-10-22 en un proyecto de prueba con la estructura del curso: `flutter analyze` solo marca los tres `avoid_print` que el taller pide a propósito. No se ejecutó en un dispositivo.
- Las 5 figuras salen de `tools/sesion7_figuras.py`. `ptCrear` (crear el proyecto) se eliminó: el taller ya no crea un proyecto. `check.py` sin errores.

### Sesión 8 · Navegación entre pantallas

**Presentación:** ⬜ pendiente (`presentaciones/sesion8/`).

**Punto de partida:** el *Ejemplo completo* de `S0048`, que ya tenía `initialRoute: '/'` y `routes:` con una sola entrada. La sesión sigue en el mismo `playlist_app` y le suma tres pantallas: `LoginScreen` (`'/'`), `SongDetailScreen` (`'/song'`) y `AddSongScreen` (`'/add-song'`); la playlist se muda a `'/playlist'`. Se usa `'/'` para el login y no `initialRoute: '/login'`, porque un `initialRoute` con barra se trata como enlace profundo y Flutter apilaría `'/'` debajo. Las lecciones de navegación de Móviles (`0034`, `0035`) no se copiaron: son de puro texto y usan `MaterialPageRoute` y una clase `ScreenArguments`.

| Lo que pide el planeador | Dónde está en el visor |
|---|---|
| Navigator y tabla de rutas nombradas en MaterialApp | `S0051` (la pila: push, pop, la de abajo sigue viva, atrás es un pop, la app se cierra con la pila vacía) con el interactivo `nav-stack` y la figura `plPila`. `S0052` (la tabla `routes:`, `initialRoute`, sin `home:`) con la figura de código `rnTabla` y el error `Could not find a generator for route` |
| pushNamed para abrir y pop para volver | `S0052`: *Entrar* abre la playlist con `pushNamed` y el ícono de logout hace `pop`. Cierra mostrando el problema: la flecha `←` del AppBar vuelve al login |
| pushNamedAndRemoveUntil con `(route) => false` | `S0053`: el predicado explicado, entrar y cerrar sesión, por qué cerrar sesión ya no puede ser un pop. Figura `ruPila` (estática, tres columnas: con `pushNamed`, el predicado, la pila nueva) e interactivo `nav-stack reset` |
| Paso de datos a la pantalla nueva | `S0054`: `SongCard` con `onTap` envuelta en `GestureDetector`, `SongList` con `onOpen`, `arguments: song` y `ModalRoute.of(context)!.settings.arguments as Song`. Interactivo `nav-result args` (con el interruptor *Olvidar arguments*, que muestra el error del cast) y figura `paArgs` |
| Retorno de un resultado al cerrarla | `S0055`: el formulario se muda a `AddSongScreen`, que cierra con `Navigator.pop(context, song)`; la playlist hace `await Navigator.pushNamed` y filtra con `if (result is Song)`. Interactivo `nav-result` y figura `reAwait` |
| *Fuera de clase:* dejar navegable el prototipo del equipo | No se asigna: las sesiones del bloque son de clase y no dejan tarea |

Notas:

- **`S0050` va primero**, como el taller de la sesión 7: la meta (figura `tnMeta`, las cuatro pantallas y cada flecha con su llamada al Navigator), los archivos al terminar (`tnCarpetas`) y dos mejoras: el saludo (el nombre viaja en `arguments` del `pushNamedAndRemoveUntil`) y *Quitar de la playlist* desde el detalle (`pop(context, true)` y `await` en `_openSong`).
- **Interactivo `nav-stack`**: teléfono funcional con botón atrás del sistema, la pila de rutas como tarjetas (visible, debajo y viva, `dispose()`, tachada por el predicado), la línea que se ejecutó y la tabla `routes:` con la entrada encontrada. Un cambio de la pila por paso y modo *Paso a paso*. Sin opciones, *Entrar* es `pushNamed` y cerrar sesión es `pop`; con `reset`, los dos son `pushNamedAndRemoveUntil` y cada ruta de abajo se tacha en su propio paso.
- **Interactivo `nav-result`**: el código de las dos pantallas, un paquete que viaja entre ellas (azul el que baja en `arguments`, naranja el que sube en el `pop`, la convención de `lift`), la pila y un panel de variables. Sin opciones enseña el retorno: el aviso *en pausa en el await*, la `Song` que sube, y `null` cuando se vuelve con atrás. Con `args`, el envío al detalle.
- Los cuatro *Ejemplo completo* (`S0052` a `S0055`) pasaron `flutter analyze` y el analizador de DartPad sin avisos. Tienen gist público en `Domiciano` y abren en *Fire it up!* (`tab=run`, pedido del profesor del 2026-10-28).
- **La solución del taller se comprobó** el 2026-10-28 en un proyecto de prueba con un archivo por clase e imports `package:`: `flutter analyze` sin avisos. No se ejecutó en un dispositivo.
- Las 7 figuras salen de `tools/sesion8_figuras.py`. `check.py` sin errores.

### Sesión 9 · Navegación con bottom navigation bar

**Presentación:** ⬜ pendiente (`presentaciones/sesion9/`).

**Publicación:** los tres *Ejemplo completo* (`S0066` a `S0068`) pasaron `flutter analyze` y el analizador de DartPad sin avisos, tienen gist público en `Domiciano` y abren en *Fire it up!* (`tab=run`). El repositorio `Domiciano/262SeminarioSesion9` es público desde el 2026-10-30, con un solo commit en `main`.

**Punto de partida:** las lecciones no usan la playlist sino un **ejemplo aparte** (decisión del profesor, 2026-10-30): `HomeScreen` con *Inicio*, *Chats* y *Perfil*, la misma barra de `S0027`. La playlist queda para el taller. `S0027` se queda en la sesión 3 como adelanto de cómo se ve la barra; `S0066` la retoma completa.

| Lo que pide el planeador | Dónde está en el visor |
|---|---|
| Navegación horizontal con BottomNavigationBar | `S0066`: la barra como cuarto lugar del `Scaffold` (figura `bpScaffold`), sus partes `items`, `BottomNavigationBarItem` con `icon` y `label`, y `currentIndex` (figura de código `bpPartes`), `onTap` con `debugPrint` y el problema de cuatro botones o más, `shifting` frente a `type: BottomNavigationBarType.fixed` (figura `bpTipos`) |
| Una Screen anfitriona que cambia de Page según un índice guardado en el estado | `S0067`: `int _currentIndex` en el `State`, `onTap: (index) => setState(...)` (figura animada `biCiclo`, 5 pasos de 2,5 s), tres Pages sin `Scaffold` en `lib/pages/` y `_buildPage()` primero con `if / else if / else` y luego con `switch` (figura `biSwitch`), como pidió el profesor |
| Cambiar de tab es setState y abrir un detalle es push | Apartado *Pestaña o pantalla nueva* de `S0067`, y la figura `tbMeta` del taller con las dos clases de flecha |
| *(Pedido del profesor)* Objetos que recuerdan estado | `S0068`: `ChatsPage` con un borrador en su `TextEditingController` y `debugPrint` en `initState` y `dispose`; con el `switch` el borrador se pierde, con `IndexedStack` no. Interactivo `tab-state` (sin opciones y con `indexed`) y figura `isPila`. Cuándo conviene y cuándo el dato debe subir a la Screen. `AutomaticKeepAliveClientMixin` y `PageStorageKey` solo se nombran |
| *Entrega parcial 1* (maqueta, 3 minutos por equipo) | No es contenido del visor: se hace en clase |
| *Fuera de clase:* terminar la navegación por secciones de la app del equipo | No se asigna: las sesiones del bloque son de clase y no dejan tarea |

Notas:

- **`S0065` va primero**, como los talleres de las sesiones 7 y 8. Por pedido del profesor (2026-10-30), el repositorio de arranque trae todo lo demás hecho y **el taller solo toca `main_screen.dart`**: tres metas, la barra, `_currentIndex` con `setState` y elegir la Page del `body`. Dos extras opcionales en *Si te sobra tiempo*: el botón + solo en Playlist y probar el scroll con `IndexedStack`. Figuras `tbMeta` y `tbCarpetas` (marca solo `main_screen.dart` como el archivo que se edita).
- **La solución del taller se comprobó** el 2026-10-30 en una copia del repositorio de arranque, con un archivo por clase e imports `package:`: `flutter analyze` sin avisos. No se ejecutó en un dispositivo.
- **Interactivo `tab-state`**: teléfono con barra de tres pestañas y `ChatsPage` con un campo; al lado, lo que hay en el `body` (o los hijos del `IndexedStack`), el `State` de `HomeScreen` con `_currentIndex`, el de `ChatsPage` con el texto del controller y sus contadores de `initState` y `dispose`, y el código con la línea que corre. Usa `navRunner` y `navControls` de `nav-stack`. Un cambio por paso: el panel de hijos cambia en `build`, `dispose` o `initState` y el teléfono solo en *Se ve*.
- Las 6 figuras salen de `tools/sesion9_figuras.py`; `raClonar9`, de `tools/arranque_figuras.py`. `check.py` sin errores.

## Repositorios de arranque

Desde el 2026-10-28 (pedido del profesor) cada sesión desde la 2 abre con una lección **Repositorio de arranque** (`S0056` a `S0062` y `S0064` para la sesión 9, siempre la primera de la sesión): el punto de partida de la sesión es lo que quedó al terminar la anterior, en un repositorio público `github.com/Domiciano/262SeminarioSesionN`, con un solo commit en `main`. La lección muestra cómo clonarlo (figura de consola `raClonarN`, de `tools/arranque_figuras.py`) y qué trae.

- **Sesión 2**: `flutter create --org icesi.edu.co miapp1` limpio, lo que deja `S0001`. No se usó el commit «Sesion 2» de `262SeminarioApp1`: ya trae la `HomeScreen` con los ejercicios de `Column` y `Row` de la sesión 2.
- **Sesiones 3 a 5**: el proyecto del profesor, `Domiciano/262SeminarioApp1` (paquete `mi_app_1`), en los commits `2d28b37` (componentes), `5a628f0` (`ProfileScreen`) y `2175ee4` (`AGENTS.md` y `docs/`). Se quitó `test/widget_test.dart`, que no compilaba (busca `MyApp`). Las secciones del taller `S0026` no están: el profesor no las sacó a componentes. La sesión 5 trae además las skills `mer-svg` y `flutter-pantallas` en `.agents/skills/`, copiadas de `recursos/sesion4/` (no estaban en el repo del profesor).
- **Sesión 6**: `flutter create --org icesi.edu.co playlist_app` limpio, con el contador que recorre `S0041`.
- **Sesiones 7 y 8**: el *Ejemplo completo* de `S0044` y de `S0048`, separados en un archivo por clase con imports `package:playlist_app/`. Sin el taller de la sesión anterior. La sesión 8 trae además, sin registrar en `routes:`, `SongDetailScreen` hecha (sin el botón *Quitar*, que es mejora del taller) y `AddSongScreen` con un `Column` vacío, y `SongCard` con un `GestureDetector` cuyo `onTap` solo hace `debugPrint('Navegar a SongDetailScreen')`, sin parámetro en el constructor (pedido del profesor, 2026-10-28).
- **Sesión 9**: el *Ejemplo completo* de `S0055`, separado en un archivo por clase con imports `package:playlist_app/` (commit `2bf9fee`). Un segundo commit, `e39c7ab` (pedido del profesor, 2026-10-30), adelanta todo lo que no es la barra: `PlaylistScreen` renombrada a `MainScreen`, las tres Pages en `lib/pages/` y el nombre del login en `arguments` (`LoginScreen` con `TextField`, título `Hola, <nombre>`). `MainScreen` muestra solo `PlaylistPage`. Sin *Quitar* desde el detalle. Armado el 2026-10-30 a partir de los archivos de plataforma del commit `498eb8a` de `262SeminarioSesion8`; el commit posterior «Semana 13» de ese repositorio es trabajo de clase y no se usó.
- Los ocho pasan `flutter analyze` sin errores; los de las sesiones 3 a 5 dejan los avisos de estilo (`use_key_in_widget_constructors`) del código del profesor.
- `check.py` marca como error la URL de las figuras `raClonarN`: es texto del comando mostrado, no un recurso que el SVG cargue.

## Lecciones reutilizadas de Aplicaciones Móviles

Son copias de las de `FlutterLearning/content/`, con el **mismo nombre de archivo y el mismo id**. El 2026-09-29 eran idénticas byte a byte al original. Si se corrige una en Móviles, la copia de aquí no cambia sola.

| Archivo | Id | Título | Sección aquí | Sección en Móviles |
|---|---|---|---|---|
| `lessonC1.md` | `0019` | Instalación de Flutter | Instalación avanzada | Flutter · SEMANA 1 |
| `lessonC2.md` | `0020` | Tu primera app Flutter | Instalación avanzada | Flutter · SEMANA 1 |
| `lessonC3.md` | `0021` | Ejecutar las apps | Instalación avanzada | Flutter · SEMANA 1 |
| `lessonC4.md` | `0022` | Configurando dispositivos virtuales | Instalación avanzada | Flutter · SEMANA 1 |
| `lessonA1.md` | `0001` | Primeros pasos con Dart | Dart | Dart basics |
| `lessonA2.md` | `0006` | Operadores numéricos | Dart | Dart basics |
| `lessonA3.md` | `0007` | Trabajando con Strings | Dart | Dart basics |
| `lessonA4.md` | `0008` | Condicionales | Dart | Dart basics |
| `lessonA5.md` | `0009` | Tipos opcionales y null safety | Dart | Dart basics |
| `lessonA6.md` | `0010` | Listas y mapas | Dart | Dart basics |
| `lessonA7.md` | `0011` | Métodos en Dart | Dart | Dart basics |
| `lessonA8.md` | `0012` | Clases y objetos en Dart | Dart | Dart basics |

## Lecciones propias del Seminario

| Archivo | Id | Título | Sesión |
|---|---|---|---|
| `lessonS1.md` | `S0001` | Instalación básica | 1 |
| `lessonS2.md` | `S0002` | Programa del curso | *(apoyo, sección Curso)* |
| `lessonS3.md` | `S0003` | ¿Qué es el frontend? | 1 |
| `lessonS4.md` | `S0004` | Panorama del frontend | 1 |
| `lessonS5.md` | `S0005` | Frontend y la nube | 1 |
| `lessonS6.md` | `S0006` | Desarrollar con IA | 1 |
| `lessonS7.md` | `S0007` | Entrega 1 · Prototipo en Stitch/Figma y base de datos | *(apoyo, sección Entregables)* |
| `lessonS8.md` | `S0008` | Entrega 2 · Prototipo no funcional en Flutter | *(apoyo, sección Entregables)* |
| `lessonS9.md` | `S0009` | Entrega 3 · Aplicación final y exhibición | *(apoyo, sección Entregables)* |
| `lessonS10.md` | `S0010` | El proyecto por dentro | 2 |
| `lessonS11.md` | `S0011` | Text | 2 |
| `lessonS12.md` | `S0012` | Image | 2 |
| `lessonS13.md` | `S0013` | Button | 2 |
| `lessonS14.md` | `S0014` | TextField | 2 |
| `lessonS15.md` | `S0015` | StatelessWidget: tu primer componente | 2 |
| `lessonS16.md` | `S0016` | Column | 2 |
| `lessonS17.md` | `S0017` | Row | 2 |
| `lessonS18.md` | `S0018` | Taller · Componentes | 2 |
| `lessonS19.md` | `S0019` | Playground | *(apoyo, sección Curso)* |
| `lessonS20.md` | `S0020` | Scaffold | 3 |
| `lessonS21.md` | `S0021` | SafeArea | 3 |
| `lessonS22.md` | `S0022` | Container y Padding | 3 |
| `lessonS23.md` | `S0023` | Expanded | 3 |
| `lessonS24.md` | `S0024` | SingleChildScrollView | 3 |
| `lessonS25.md` | `S0025` | Armar una pantalla | 3 |
| `lessonS26.md` | `S0026` | Taller · Pantallas | 3 |
| `lessonS27.md` | `S0027` | BottomNavigationBar | 3 |
| `lessonS28.md` | `S0028` | AppBar | 3 |
| `lessonS29.md` | `S0029` | El agente en consola | 4 |
| `lessonS30.md` | `S0030` | El archivo de contexto | 4 |
| `lessonS31.md` | `S0031` | Skills | 4 |
| `lessonS32.md` | `S0032` | Taller · Tu primera skill | 4 |
| `lessonS33.md` | `S0033` | Una skill para armar pantallas | 4 |
| `lessonS34.md` | `S0034` | ¿Qué es MCP? | 5 |
| `lessonS35.md` | `S0035` | Configurar MCP en Antigravity | 5 |
| `lessonS36.md` | `S0036` | Prototipado con Stitch MCP | 5 |
| `lessonS37.md` | `S0037` | Automatización con Playwright MCP | 5 |
| `lessonS39.md` | `S0039` | Colaboración con GitHub MCP | 5 |
| `lessonS38.md` | `S0038` | Taller · Servidores MCP | 5 |
| `lessonS40.md` | `S0040` | Estado: Stateless frente a Stateful | 6 |
| `lessonS41.md` | `S0041` | setState: el contador de flutter create | 6 |
| `lessonS42.md` | `S0042` | Ciclo de vida: initState, dispose y TextEditingController | 6 |
| `lessonS43.md` | `S0043` | Creador de playlists: la lista en texto | 6 |
| `lessonS44.md` | `S0044` | Creador de playlists: el componente SongCard | 6 |
| `lessonS45.md` | `S0045` | Taller · Playlist, parte 1 | 6 |
