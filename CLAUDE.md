# CLAUDE.md

Guía para Claude Code al trabajar en este repositorio.

## Qué es esto

Repositorio del curso **Seminario de Ingeniería de Software**. Nació el 2026-09-29
como copia de `FlutterLearning` (Aplicaciones Móviles): misma app, mismo tema azul y,
de arranque, las mismas lecciones. Ese mismo día se vació `toc.md` y el temario se
empezó a armar **sesión por sesión** a partir del plan de curso (ver *Temario* abajo).
Contiene:

- `classnotesapp/` — SPA en React + Vite que muestra las notas de clase como un visor
  de lecciones navegable.
- `content/` — las lecciones en Markdown, **en la raíz del repo**.
- `toc.md` — la tabla de contenidos, también en la raíz.
- `manifest.md` — qué sesiones del plan ya tienen su contenido en el visor.
- `presentaciones/sesionN/` — la presentación de cada sesión, publicada en
  `/presentaciones/N/` (ver *Presentaciones de las sesiones*).
- `docs/syllabus.md` — el syllabus oficial del curso (RAA, evaluación, unidades, niveles
  de IAG), transcrito del PDF de la universidad.
- `docs/planeador.md` — el plan de curso: qué se hace en clase, fuera de clase y qué
  se entrega en cada sesión.

El contenido **no está dentro de `classnotesapp/`**: la app lo descarga en tiempo de
ejecución desde `raw.githubusercontent.com`, así que editar una lección y pushear la
actualiza en el sitio ya desplegado, sin rebuild.

### Diferencia con los otros cursos: el inicio de sesión es opcional

El contenido es **público**. `AuthGate` deja pasar a quien no ha iniciado sesión; el
botón «Iniciar sesión» de la barra (`AccountMenu`) es opcional y, al usarlo, lleva por
términos y perfil como en los otros cursos. Sin sesión no hay analítica ni asistente
de IA (los dos dependen del `uid`).

**Todavía no hay proyecto Firebase**: `src/auth/firebaseConfig.js` y `.firebaserc`
tienen `REPLACE_*`, así que hoy la app es un visor público sin botón de inicio de
sesión. Al pegar la config de un proyecto **propio del curso** (uno por curso, no
reusar `facelogprueba` ni `computacion-fcc47`) aparece el botón. `courseId` es
`seminario`.

Todo lo que no sea contenido, tema, remotos o esta puerta opcional debe mantenerse
**idéntico** a los otros cursos — ver el `CLAUDE.md` de la carpeta contenedora
`CoursesPlatform/`.

## Comandos (desde `classnotesapp/`)

```bash
npm install
npm run dev       # servidor de desarrollo con hot reload
npm run build     # build de producción
npm run preview   # previsualizar el build
npm run lint      # ESLint
npm run test      # Vitest
npx vitest run <file>   # un solo archivo de test
```

Alias de import: `@/` → `src/`. Tema por defecto: `dark`.

## Remotos git

Un solo remoto, rama `main`:

- `origin` → `https://github.com/DomicianoRincon/SeminarioSoftware`

`classnotesapp/src/content/config.js` y los enlaces de `toc.md` descargan el contenido
de `raw.githubusercontent.com/DomicianoRincon/SeminarioSoftware/...`.

El repo pertenece a la cuenta `DomicianoRincon`, así que el push necesita el Personal
Access Token de `$PAT_GITHUB_DOMICIANO_RINCON` (en `~/.zshrc`, nunca en el repo):

```bash
git push "https://domicianorincon:$PAT_GITHUB_DOMICIANO_RINCON@github.com/DomicianoRincon/SeminarioSoftware.git" main
```

Nunca escribir el valor literal del token en un archivo ni en un commit.

**Sitio publicado: https://domicianorincon.github.io/SeminarioSoftware/** (base path
derivado del nombre del repo en el workflow). No renombrar el repo.

## Temario: planeador, manifest y toc

Cuatro archivos, cada uno con una sola responsabilidad:

| Archivo | Qué es | Quién manda |
|---|---|---|
| `docs/syllabus.md` | El syllabus oficial: resultados de aprendizaje, evaluación, unidades y acuerdos de uso de IAG | Es la **autoridad** sobre qué debe lograr el curso |
| `docs/planeador.md` | El plan de curso transcrito de la hoja *PlaneadorF* del departamento | Es la **autoridad** sobre qué va en cada sesión |
| `manifest.md` | Qué sesiones ya están en el visor, con qué lecciones y qué falta | Se actualiza **cada vez que se toca `toc.md`** |
| `toc.md` | Lo que ve el estudiante | Se arma desde el manifest |

**El bloque de este repositorio.** El profesor tiene a cargo **las últimas 8 semanas** del
curso (semanas 9 a 16), que según el syllabus son las **unidades 3 y 4** (RA3 y RA4). Las
unidades 1 y 2 las dicta otro docente y no tienen contenido aquí.

**Numeración.** El planeador cuenta las sesiones de este bloque de la 17 a la 32 (las 16
primeras son de las unidades 1 y 2). En el visor y en el manifest se cuentan de la 1 a la
16: `sesión del visor = sesión del planeador − 16`. La semana del semestre es
`8 + ⌈sesión del visor / 2⌉` (dos sesiones por semana).

**Cómo se arma una sesión:**

1. Leer la sesión en `docs/planeador.md`, en clase y fuera de clase.
2. Buscar primero qué se puede **reutilizar de Aplicaciones Móviles** (ver abajo) y
   escribir solo lo que falta.
3. En `toc.md`, la sesión va bajo `[t] Sesión N · <tema del planeador>`. El material de
   apoyo que no pertenece a una sola sesión va en secciones temáticas aparte
   (*Instalación avanzada*, *Dart*). La primera sección es siempre **Curso**, con
   *Programa del curso* (`lessonS2.md`), igual que en Móviles: es la versión para el
   estudiante de `docs/syllabus.md`, y si cambia el syllabus hay que actualizarla.
4. Actualizar `manifest.md`: estado de la sesión, ids y la tabla de lo que pide el
   planeador frente a dónde quedó.

**`toc.md` se vació el 2026-09-29.** Las ~80 lecciones heredadas de Móviles siguen en
`content/` aunque ya no estén en el temario. No borrarlas: son la cantera de donde se
reutiliza.

**Mientras no haya proyecto Firebase no hay traza**, así que reorganizar el temario todavía
no hay que anotarlo en `analitics/schedule.md`. Cuando el login se active, sí. El `toc.md`
nuevo tampoco nombra `SEMANA`, y `courseStartDate` en `content/config.js` sigue siendo el de
Móviles: hay que fijar las fechas del Seminario antes de que la analítica sirva para H3.

### Reutilizar lecciones de Aplicaciones Móviles

- La lección se copia de `FlutterLearning/content/` con el **mismo nombre de archivo y el
  mismo id**. Así una misma lección tiene el mismo id en los dos cursos, y comparar su uso
  entre cursos es unir por id.
- Lo que cambia es la **sección** del `toc.md`, no el archivo. Ejemplos: la sección
  *Dart basics* de Móviles aquí se llama **Dart**. *Flutter · SEMANA 1* (`lessonC1` a
  `lessonC4`) aquí es **Instalación avanzada**.
- Son copias, no enlaces: si se corrige la lección en Móviles, hay que copiarla otra vez.
  La tabla de reutilizadas está en `manifest.md`.

### Ids de las lecciones propias

Las lecciones que nacen en el Seminario usan **`S` + cuatro dígitos** (`S0001`,
`S0002`…), en archivos `lessonS<n>.md`. Los números de Móviles (`0001`–`0088`) siguen
creciendo en ese curso; con el prefijo, una lección que viaje entre cursos nunca choca con
otra.

### Estilo de las lecciones: todo explicado con ilustraciones SVG

Preferencia explícita del profesor: las lecciones tienen que estar **muy explicadas por
medio de ilustraciones y esquemas en SVG**, no solo con texto. Como referencia de nivel,
ver `lessonS1.md`, que trae los tres tipos:

| Tipo | Para qué | Ejemplo en `lessonS1.md` |
|---|---|---|
| Piezas | Qué componentes hay y cómo se conectan | *Las piezas de la instalación básica* |
| Pasos con maqueta de la interfaz | Un procedimiento en pasos numerados, dibujando la pantalla real con un recuadro donde se hace clic | *Instalar Flutter con la extensión* |
| Frame de consola | Un comando y su salida, con lo importante señalado | *Crear el proyecto con `flutter create`* y los otros tres |

Cómo se hacen:

- Con la skill **`svg-diagrams`** (paleta, tipografía, rejilla de 8 px), validadas con su
  `check.py` y **renderizadas y miradas** con `render.sh` antes de darlas por buenas.
- Van dentro de la lección como bloque ` ```svg `. El visor las inyecta **en el mismo DOM
  que la app**, así que:
  - la raíz lleva un `id` único (`<svg id="fiPasos" …>`) y **todo** selector del
    `<style>` va prefijado con él (`#fiPasos .card`). Un `.card` suelto cambia el
    estilo de la app entera;
  - los `id` de `<marker>`, `<filter>`, `<title>` y `<desc>` llevan el mismo prefijo
    (`fiPasos-arrow`). Dos SVG con `id="arrow"` en la misma página se pisan.
- **Fondo claro fijo** (`<rect … fill="#FBFBFD" rx="16">`) y **sin**
  `@media (prefers-color-scheme: dark)`: el tema del visor lo cambia su propio botón, no el
  del sistema, así que esa media query mostraría la figura oscura sobre un visor claro o al
  revés. En modo oscuro se ve como una tarjeta clara.
- `viewBox="0 0 960 …"`, `width="100%"` y `style="max-width:960px;display:block;margin:0 auto"`.
  Texto de 12 px como mínimo, porque la figura se reduce en pantallas angostas.
- Textos de la figura en español. Nombres de botones, comandos y mensajes se dejan como
  aparecen en pantalla (en inglés).
- **Animadas, si el tema lo pide**: con CSS dentro del propio SVG (`@keyframes` prefijados
  con el `id`), por pasos de duración fija. Si la raíz declara `data-steps` y
  `data-step-seconds`, el visor (`SvgBlock.jsx`) añade debajo los botones de anterior,
  reproducir/pausar y siguiente; toda animación que siga los pasos debe durar exactamente
  `pasos × segundos`. Ejemplo y generador: `FlutterLearning/tools/bloc_figuras.py`.

### Consola: siempre en un frame SVG

Decisión del profesor (2026-09-29): **de aquí en adelante, todo lo que se hace en consola
se muestra con un frame de consola en SVG**, no solo con un bloque de código. Se generan
con `tools/console_frame.py`, que fija el estilo; no se dibujan a mano. Las reglas:

- **Ventana oscura** con barra de título (tres puntos y `Terminal · <carpeta>`) sobre la
  tarjeta clara de siempre.
- **Prompt = carpeta actual + `>`**, en gris: `miapp1> flutter devices`. Nunca `$` ni
  `PS C:\...>`: así no se ata a un sistema operativo, y enseña en qué carpeta se está
  parado. La lección dice una vez que lo que va antes de `>` no se escribe.
- **Comando en blanco y negrita; salida en gris claro; lo irrelevante, más tenue; el
  éxito (`All done!`), en verde.** La salida es la real del comando, recortada a lo que
  importa. Versiones y números que cambian se escriben con `x` (`Flutter 3.x.x`).
- **Lo importante se señala con un recuadro amarillo numerado**, y cada número tiene su
  tarjeta debajo de la terminal que lo explica. Máximo tres por figura.
- **Siempre acompañado de un bloque ` ```shell `** con los comandos, justo debajo: el
  texto de un SVG no se copia bien, y el estudiante tiene que poder pegar el comando.
- Rutas de ejemplo de Windows (`C:\develop`). Cuando un comando cambia por sistema
  (`cd C:\develop` / `cd ~/develop`), la figura muestra Windows y el bloque de código trae
  las dos versiones.

### Código: frame de editor SVG

Desde la sesión 2 (2026-10-01), **cada widget se explica con una figura de código anotado**:
editor oscuro a la izquierda, el resultado dibujado a la derecha y una flecha de cada
propiedad a lo que cambia en el resultado. Se generan con `tools/code_frame.py`, hermano de
`console_frame.py`; no se dibujan a mano. Las reglas:

- **Una flecha por propiedad, cada una con su color**: el recuadro sobre el código, la
  flecha y lo que señala comparten color. Máximo cuatro por figura.
- **Las flechas no se cruzan.** `lane` elige el carril entre el editor y el panel, y `via`
  rodea el dibujo para llegar desde abajo. Se comprueba mirando el render.
- Cuando no hay nada que dibujar (anatomía de una clase, `main.dart`), el panel derecho
  lleva **tarjetas de explicación** y las flechas apuntan a ellas.
- **Siempre acompañado de un bloque ` ```dart `** con el mismo código, justo debajo.
- El código de la figura sigue el estilo del curso: identificadores en inglés, textos de
  interfaz en español, sin comentarios.
- Cada línea lleva `textLength`, así el resaltado cae sobre el texto aunque la fuente
  monoespaciada del visitante tenga otro ancho.

Las figuras de una sesión viven juntas en un script (`tools/sesion2_figuras.py`, `tools/sesion3_figuras.py`, `tools/sesion4_figuras.py`): con una
carpeta como argumento escribe los `.svg` para revisarlos, y con `--inject` reemplaza cada
bloque ` ```svg ` de las lecciones por la figura del mismo `id`. **No editar esos SVG dentro
del Markdown**: se cambia el script y se vuelve a inyectar.

El script de una sesión puede importar dibujos del de otra (`sesion3_figuras.py` toma `phone`, `avatar` y `head` de
`sesion2_figuras.py`): si se cambia uno de esos, hay que volver a inyectar las dos sesiones.

`check.py` marca como error la URL de ejemplo de `imNetwork` (`Image.network('https://…')`).
Es un falso positivo: es texto del código mostrado, no un recurso que el SVG cargue.

## Presentaciones de las sesiones

Cada sesión puede tener su presentación, hecha con la skill **`presentaciones-icesi`** (ver
el workflow global `~/.claude/workflows/presentaciones.md`). En este curso, a diferencia
de los otros, **las presentaciones viven en el repo y se publican con el sitio**:

| | |
|---|---|
| Carpeta | `presentaciones/sesionN/` (N = sesión del visor, no la del planeador) |
| Entregable | `presentaciones/sesionN/presentacion.html`, **commiteado** |
| URL | `https://domicianorincon.github.io/SeminarioSoftware/presentaciones/N/` |
| Enlace | Al inicio de la **primera lección de la sesión** en el `toc.md`, justo bajo los tags: `**Presentación de la sesión:** [<título>](<URL>)` |

**Cómo se publica.** `.github/workflows/deploy-pages.yml` tiene un paso *Add session
presentations* que copia cada `presentaciones/sesion*/presentacion.html` a
`dist/presentaciones/N/index.html` antes de subir el sitio. El workflow **no construye** la
presentación: el HTML se arma en local con el `build.py` de la skill y se commitea. Un push
que solo toque un `presentacion.html` también dispara el despliegue.

**Qué se commitea y qué no.** Sí: `plan.md`, `deck.json`, `helpers.js`, `slides/*.js`,
`figuras.py` y `presentacion.html`. No: `build/`, con las capturas de la revisión visual (ya
lo ignora el `.gitignore`). El repo es público: nada de datos de estudiantes en un deck.

**Figuras reutilizadas.** `figuras.py` copia a `slides/00-figuras.js` las figuras SVG de las
lecciones (les quita el título y las escala al lienzo). Si una lección cambia su figura:
`python3 figuras.py`, luego el build, y se commitea el `presentacion.html` nuevo.

| Sesión | Presentación | Primera lección |
|---|---|---|
| 1 | `presentaciones/sesion1/` · *Frontend developing* · 28 slides | `S0003` ¿Qué es el frontend? |
| 2 | `presentaciones/sesion2/` · *Componentes* · 36 slides | `S0010` El proyecto por dentro |
| 3 | `presentaciones/sesion3/` · *Pantallas con componentes* · 42 slides | Enlazada en `S0026` Taller · Pantallas, no en la primera lección (pedido del profesor) |

## Cómo se escribe una lección

Una lección es un archivo Markdown en `content/` **en la raíz del repo** (hermano de
`classnotesapp/`, no dentro).

### Esqueleto obligatorio

```markdown
# Streams y funciones async*

<!-- tags: Stream, StreamController, async*, yield, await for, StreamBuilder,
     StreamSubscription, broadcast stream, Bad state: Stream has already been listened to -->

Párrafo de entrada que dice de qué va la lección.

## Qué es un Stream

Texto del apartado.

## Escuchar un stream

Texto del apartado.
```

| Elemento | Regla |
|---|---|
| `#` (un solo h1) | Título de la lección. Es lo que se muestra arriba y lo que el asistente cita |
| `<!-- tags: … -->` | **Obligatorio.** Ver abajo |
| `##` | Apartados. Alimentan el índice lateral, el `subsection_dwell` de la analítica y el contexto que se le manda a la IA |
| `###` en adelante | Estructura interna del apartado; no salen en el índice ni cortan la subsección |

### La sección de tags

Va en un **comentario HTML** justo bajo el `#`. GitHub no lo muestra, el visor tampoco:
solo lo leen el asistente de IA y los chips que ve el estudiante.

```markdown
<!-- tags: Stream, StreamBuilder, await for -->
```

Sirve para dos cosas a la vez, y por eso importa:

1. **Contexto de la IA.** Entran en la instrucción del sistema como "Temas de esta
   lección: …". El modelo ya recibe el markdown completo, pero el texto entero no le
   dice *qué es lo importante*; los tags sí. Es la diferencia entre que entienda que
   la lección va de `StreamBuilder` y del `await for`, y que tenga que deducirlo de
   6 KB de prosa.
2. **Los chips** que el estudiante ve bajo el chat. Se muestran los **primeros 6**; el
   resto (hasta 12) sigue yendo al modelo. Escribe primero los que más te interese que
   un estudiante pulse.

**Cómo escribir tags que sirvan.** El criterio es: *¿con qué palabras preguntaría un
estudiante que se atascó en esta lección?* Eso lleva a incluir tres tipos:

| Tipo | Ejemplos (Móviles) |
|---|---|
| El nombre técnico exacto | `StreamBuilder`, `setState`, `BuildContext`, `Navigator.push`, `BlocProvider` |
| El concepto en español, como lo diría el estudiante | `estado de un widget`, `paso de parámetros entre pantallas`, `reconstrucción del árbol` |
| El error o la confusión típica de ese tema | `setState() called after dispose()`, `RenderFlex overflowed`, `Null check operator used on a null value` |

Los del tercer tipo son los que más rinden: son las palabras que aparecen cuando alguien
llega con un problema, no con curiosidad. En Flutter, además, los mensajes de error son
larguísimos y muy reconocibles — vale la pena meter el fragmento por el que un estudiante
buscaría.

**Qué NO poner.** Nada genérico (`Flutter`, `Dart`, `móviles`, `widgets`): no distingue
esta lección de las otras 79 y desperdicia un chip. Tampoco frases largas — más de 42
caracteres se descarta, porque desborda el chip.

**Si no pones tags, la lección sigue funcionando**: se usan los títulos de los `##` como
respaldo. Pero los títulos describen la *estructura* del texto, no el *vocabulario* del
tema, así que el asistente queda peor contextualizado. Anotar es opcional para que nada
se rompa, no porque dé igual.

### Bloques especiales

Markdown estándar (CommonMark + GFM) para todo, más estos bloques cercados:

| Bloque | Para qué |
|---|---|
| ` ```mermaid ` | Diagrama Mermaid |
| ` ```svg ` | SVG en crudo |
| ` ```youtube ` | `<videoId> \| <título>` |
| ` ```dartpad ` | Editor DartPad; el cuerpo es el id del Gist |
| ` ```dart trycode=<gistId> ` | Bloque con pestañas *Código* / *Fire it up!* |

Toda valla cercada **debe declarar lenguaje** (` ```dart `, nunca ` ``` ` a secas): sin
él, el renderizador la confunde con código en línea.

> DartPad corre en un iframe de `dartpad.dev`. Por la política de mismo origen no se
> puede leer el código que escribe el estudiante, ni si compila, ni el error. Solo se
> registra que lo abrió y cuánto tiempo tuvo el foco.

### Ejemplo completo con *Fire it up!* en toda lección con código

Regla del profesor (2026-10-02): **toda lección que tenga código termina con un apartado
`## Ejemplo completo`**, con un bloque ` ```dart trycode=<gistId> ` que corre en DartPad.

- El ejemplo es **un programa entero en un solo archivo**: `main`, `App` con la tabla de rutas
  y `HomeScreen`, igual que el de `S0010`. La lección aclara que en el proyecto van separados.
- El gist se crea **público en la cuenta `Domiciano`** (`gh gist create --public`), con el
  archivo `lessonS<n>code1.dart` y la descripción
  `Snippet Dart extraído de content/lessonS<n>.md (lessonS<n>code1.dart)`. El bloque de la
  lección y el gist llevan exactamente el mismo código.
- Lo que no puede correr en DartPad (un `Image.asset`, un paquete propio) **va comentado** en
  el ejemplo, y la lección dice por qué.
- Antes de crear el gist, el código se pasa por el analizador de DartPad
  (`POST https://stable.api.dartpad.dev/api/v3/analyze` con `{"source": ...}`).
- El *Taller · Componentes* (`S0018`) no lleva ejemplo completo: sería entregar la solución.

### Imágenes por URL en el código: siempre `https://picsum.photos/400`

Regla del profesor (2026-10-02): cuando el código de una lección muestra una imagen desde
internet (`Image.network`, `NetworkImage`, un parámetro `imageUrl` de ejemplo), la dirección
es **`https://picsum.photos/400`**, siempre la misma. Varias de las direcciones que se usaban
antes no son compatibles con DartPad (se reemplazaron las de `i.pravatar.cc`,
`yt3.googleusercontent.com` y `flutter.dev`).
Aplica también al gist de un bloque `trycode` o `dartpad`: el gist y el bloque de la lección
llevan la misma dirección.

### Darla de alta en `toc.md`

```
[t] Render de Listas · SEMANA 3
[lesson:url] https://raw.githubusercontent.com/DomicianoRincon/SeminarioSoftware/main/content/lessonXX.md | Streams y async* | lessonStreams
```

- El **tercer campo es el id estable** (SPEC-12) y es la clave contra la que se guarda
  toda la analítica y todo el corpus de preguntas. **Nunca lo cambies** al reorganizar
  el temario: mover, renombrar o reescribir una lección está bien; cambiarle el id parte
  sus datos en dos y no hay forma de reunirlos.
- El `[t]` que la precede aporta dos cosas automáticamente: la **sección del temario**
  (`tocSection`, que ancla cada pregunta al bloque) y, si el título nombra una semana
  (`SEMANA 3`, en cualquier posición del título), la **fecha planeada** de la lección
  (SPEC-13/14).
- ⚠️ El `toc.md` del Seminario **todavía no nombra `SEMANA`** en ningún título. Sin ella
  no hay fecha planeada y la lección queda fuera de H3 (la alerta temprana del estudio).
  Cuando estén las fechas del curso, añadir `· SEMANA N` a los `[t]` de cada sesión.

### Antes de dar por hecha la lección

1. Imágenes locales: tienen que existir en `classnotesapp/src/assets/` y se referencian
   **solo por nombre de archivo**, sin ruta. No se descargan, van en el bundle.
2. Push a `origin`, el único remoto (con el PAT, ver *Remotos git*).
   `raw.githubusercontent.com` sirve desde ahí.
3. Actualizar `manifest.md` si la lección entra o sale del temario.
4. Si cambiaste algo a mitad de semestre —moviste la lección de semana, la reescribiste,
   añadiste una nueva—, anótalo en `analitics/schedule.md` § 4.3 de la carpeta
   contenedora. Sin eso, el análisis ve el temario final y supone que siempre fue así.

## Arquitectura

### Flujo del contenido

1. `src/content/config.js` apunta `tocUrl` a la URL raw de `toc.md`.
2. `App.jsx` la descarga al arrancar; `TableOfContentsParser`
   (`src/utils/tableOfContentsParser.js`) la convierte en un arreglo de secciones —
   `[t]` título, `[d]` divisor, `[lesson:url]` lección.
3. `LessonPage.jsx` resuelve la lección por el id de la ruta y descarga su Markdown
   (con caché en `LessonContentCache`).
4. `LessonParser.jsx` lo convierte en componentes React.

### Rutas

`/{base}/lesson/:lessonId`, donde `lessonId` es el id estable de `toc.md`. Los enlaces
viejos con el ordinal siguen resolviéndose. Los deep links en GitHub Pages funcionan vía
`public/404.html` + el redirect `?p=` de `App.jsx`.

**Base path**: lo fija `.github/workflows/deploy-pages.yml` derivándolo del nombre del
repo. El valor por defecto de `vite.config.js` solo aplica en `npm run dev`. No volver a
fijarlo a mano: como este repo se publica desde dos remotos y cada uno sirve bajo su
propio nombre, un valor fijo rompe la copia del otro.

### Vista de administrador (`/admin`)

`src/admin/` cruza la **lista de clase** que entrega la universidad
(`students/262.md`: una línea por estudiante, `código nombre completo`, sin encabezado)
con los perfiles de Firestore, para responder quién ya entró al visor, con qué correo y
con qué usuario de GitHub, y **quién falta**. Un botón exporta todo a un `.md`. Se llega
desde el menú de cuenta → *Estudiantes*.

Portado desde Compunet2 el 2026-08-25, y **byte a byte idéntico** al de ese repo —
mismos componentes, mismo `adminData.js`, mismo `studentActivity.js`. Solo cambian, como
en el resto de la app, `courseId` (`moviles`) y `courseTerm` (`'262'`, en
`content/config.js`). La documentación completa de cómo funciona el cruce de listas
(las cuatro pasadas de `matchRoster.js`), el panel de actividad por estudiante y sus
invariantes está en el `CLAUDE.md` de Compunet2 — no se duplica aquí porque el código y
el comportamiento son el mismo.

La llave es el custom claim `profesor: true` sobre la cuenta de Firebase (proyecto
del curso, por crear) — el mismo que exigen las reglas de Firestore. **Pendiente**: asignarlo
a la cuenta del profesor de este curso (ver `classnotesapp/firestore/README.md` → *Marcar
al profesor*) y cargar `students/262.md` desde la propia vista la primera vez que se use.

### Tema

`src/theme/ThemeContext.jsx` con los tokens en `src/theme/colors.js` (azul en este
curso). Persiste la elección en `localStorage`.

**Dentro de un iframe** (por ejemplo, incrustado en la plataforma de la universidad) el
tema cambia, desde el 2026-09-30:

- Arranca en **modo claro**, no en oscuro.
- Usa la paleta `embeddedLight`: fondo y **barra superior en blanco `#FFFFFF`**, para
  fundirse con la página anfitriona. El título de la barra usa `appBarTitle` (azul oscuro).
  `appBarText` sigue siendo blanco, porque también es el texto de los botones y avatares de
  color de acento.
- La preferencia se guarda en `themeModeEmbedded`, aparte de `themeMode`: el iframe comparte
  `localStorage` con el sitio abierto directamente, y el modo de uno no debe cambiar el del otro.
- Si se elige el modo oscuro dentro del iframe, se usa la paleta oscura normal.

La detección está en `src/theme/embedded.js` (`window.self !== window.top`) y tiene sus
pruebas en `ThemeContext.embedded.test.jsx`. **Solo existe en este curso**: si se quiere en
los otros, es un cambio de plataforma que se copia literal (`embedded.js`, `ThemeContext.jsx`,
`colors.js`, `AppBarGlobal.jsx`, `index.css` y la prueba).

## Módulos del estudio de investigación

Documentación completa en `analitics/` de la carpeta contenedora. Lo que vive aquí:

- `src/analytics/` — sensado de interacciones (F1). **Nada se captura sin
  `students.analyticsConsent === true`**, que se recoge en la pantalla de términos y
  condiciones (`src/auth/TermsScreen.jsx`) y es condición para **iniciar sesión** (no para leer: aquí el visor es público).
- `src/ai/` — asistente con Gemini (F2). El estudiante conecta **su propia** clave de
  API, que vive **solo en `localStorage`** y nunca se escribe en Firestore.
- `src/auth/` — login con Google, perfil y consentimientos. Proyecto Firebase
  por crear, `courseId: seminario`. Sin él la app corre sin puerta ni botón de login.

Los tres son **idénticos byte a byte** a los de `Compunet2-252` (salvo `AuthGate.jsx`, `AccountMenu.jsx` y los textos de términos, por la puerta opcional); lo único que cambia son
`firebaseConfig.js`, `loginBranding.js`, `colors.js` y `aiCourseHint` en
`content/config.js`. Cualquier cambio de plataforma se escribe una vez y se copia literal.
