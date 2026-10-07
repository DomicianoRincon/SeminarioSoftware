# Manifest · Seminario de Ingeniería de Software

Qué sesiones del plan de curso ya tienen su contenido en el visor. El plan completo, con lo que se hace en clase, fuera de clase y los entregables, está en [`docs/planeador.md`](docs/planeador.md). Los resultados de aprendizaje y la evaluación están en [`docs/syllabus.md`](docs/syllabus.md).

Este repositorio cubre **las últimas 8 semanas del curso (semanas 9 a 16)**, que según el syllabus son las unidades 3 y 4. El planeador numera sus sesiones de la **17 a la 32**, porque las 16 primeras son de las unidades 1 y 2, que dicta otro docente. Aquí se cuentan como **sesión 1 a 16**: `sesión del visor = sesión del planeador − 16`, con dos sesiones por semana.

**Estados:** ✅ completa en el visor · 🟡 parcial · ⬜ pendiente

## Sesiones

| Sesión | Planeador | Semana | Unidad | Tema | Estado | Lecciones en el visor |
|---|---|---|---|---|---|---|
| 1 | 17 | 9 | 4 | Entorno y primera aplicación | 🟡 | `S0003` ¿Qué es el frontend? · `S0004` Panorama del frontend · `S0005` Frontend y la nube · `S0006` Desarrollar con IA · `S0001` Instalación básica · sección *Instalación avanzada*: `0019`, `0020`, `0021`, `0022` |
| 2 | 18 | 9 | 4 | Componentes | ✅ | `S0010` El proyecto por dentro · `S0011` Text · `S0012` Image · `S0013` Button · `S0014` TextField · `S0016` Column · `S0017` Row · `S0015` StatelessWidget: tu primer componente · `S0018` Taller · Componentes |
| 3 | 19 | 10 | 4 | Pantallas con componentes | 🟡 | `S0020` Scaffold · `S0021` SafeArea · `S0022` Container y Padding · `S0023` Expanded · `S0024` SingleChildScrollView · `S0025` Armar una pantalla · `S0026` Taller · Pantallas |
| 4 | 20 | 10 | 3 | El agente en consola y el archivo de contexto | ⬜ | |
| 5 | 21 | 11 | 3 | Skills: extender el agente | ⬜ | |
| 6 | 22 | 11 | 4 | Stateful widget y setState | ⬜ | |
| 7 | 23 | 12 | 4 | Elevación de estado y funciones como parámetro | ⬜ | |
| 8 | 24 | 12 | 4 | Navegación entre pantallas | ⬜ | |
| 9 | 25 | 13 | 4 | Navegación con bottom navigation bar | ⬜ | |
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
