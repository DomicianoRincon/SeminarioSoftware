# AGENTS.md — Seminario de Ingeniería de Software (SeminarioSoftware)

Instrucciones y reglas para agentes de IA (Antigravity) que operan en este proyecto.

---

## 1. Visión general del proyecto

Este repositorio contiene el material y visor del curso **Seminario de Ingeniería de Software** (Especialidad: Desarrollo Frontend y Flutter):
- [`classnotesapp/`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/classnotesapp): SPA en React + Vite + MUI para navegación interactiva de las notas.
- [`content/`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/content): Lecciones en Markdown en la raíz del repositorio.
- [`toc.md`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/toc.md): Tabla de contenidos oficial que alimenta la navegación.
- [`manifest.md`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/manifest.md): Estado y correlación de sesiones entre el planeador y el visor.
- [`docs/syllabus.md`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/docs/syllabus.md): Syllabus oficial (RAA, evaluación, unidades, lineamientos de IAG).
- [`docs/planeador.md`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/docs/planeador.md): Planeador de curso (actividades en clase y fuera de clase por sesión).
- [`presentaciones/sesionN/`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/presentaciones): Presentaciones Reveal.js publicadas junto al sitio.
- [`tools/`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/tools): Generadores de figuras SVG (`console_frame.py`, `code_frame.py`, scripts por sesión).

### Alcance del bloque
El docente tiene a cargo las **últimas 8 semanas del semestre** (semanas 9 a 16), correspondientes a las **Unidades 3 y 4** del syllabus.

### Diferencia clave: Visor público con login opcional
- El contenido es público y accesible sin autenticación (`AuthGate` no bloquea el visor).
- El botón «Iniciar sesión» en la barra (`AccountMenu`) es opcional.
- Sin sesión activa no se emite analítica ni opera el asistente de IA (ambos requieren `uid`).
- Proyecto Firebase actualmente con placeholders (`REPLACE_*`), `courseId: seminario`.

---

## 2. Remotos Git y Despliegue en Vivo

Un único remoto, rama `main`:
- **`origin`** → `https://github.com/DomicianoRincon/SeminarioSoftware`

### Descarga de contenido en runtime:
`classnotesapp/src/content/config.js` y `toc.md` descargan el contenido desde `raw.githubusercontent.com/DomicianoRincon/SeminarioSoftware/...`.

### Comando de Push:
El repositorio pertenece a la cuenta `DomicianoRincon` y requiere el PAT de la variable de entorno `$PAT_GITHUB_DOMICIANO_RINCON`:
```bash
git push "https://domicianorincon:$PAT_GITHUB_DOMICIANO_RINCON@github.com/DomicianoRincon/SeminarioSoftware.git" main
```
> **SEGURIDAD**: Nunca escribir, imprimir ni commitear el valor del token en ningún archivo.

### URL Oficial y Base Path:
- **Sitio publicado**: **https://domicianorincon.github.io/SeminarioSoftware/**
- El workflow `.github/workflows/deploy-pages.yml` calcula el base path dinámicamente.

---

## 3. Comandos de desarrollo

Ejecutar desde `classnotesapp/`:

```bash
npm install           # Instalar dependencias
npm run dev           # Servidor de desarrollo con hot reload
npm run build         # Build de producción para dist/
npm run preview       # Previsualizar build local
npm run lint          # Linting con ESLint
npm run test          # Vitest (suite completa)
npx vitest run <file> # Ejecutar un único archivo de pruebas
```

- Alias `@/` configurado hacia `src/`.
- Tema por defecto: `dark` (paleta azul en `src/theme/colors.js`).
- **Soporte Iframe (`src/theme/embedded.js`)**: Cuando la app está embebida en un iframe (ej. plataforma institucional LMS), arranca en modo claro (`embeddedLight`) con barra superior blanca `#FFFFFF` y guarda preferencia independiente en `themeModeEmbedded`.

---

## 4. Cadena de Verdad: Syllabus, Planeador, Manifest y TOC

| Documento | Función | Autoridad |
|---|---|---|
| [`docs/syllabus.md`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/docs/syllabus.md) | Syllabus oficial de la universidad | **Autoridad máxima** sobre qué debe lograr el curso |
| [`docs/planeador.md`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/docs/planeador.md) | Plan de curso clase a clase | **Autoridad** sobre qué se hace en cada sesión |
| [`manifest.md`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/manifest.md) | Seguimiento de sesiones implementadas | Se actualiza **cada vez que se edita `toc.md`** |
| [`toc.md`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/toc.md) | Navegación para el estudiante | Se deriva del manifest y del planeador |

### Numeración y Correspondencias
- El planeador numera las sesiones del bloque de la **17 a la 32**.
- En el visor y en el manifest se numeran de la **1 a la 16**:
  $$\text{sesión del visor} = \text{sesión del planeador} - 16$$
- Semana del semestre correspondiente:
  $$\text{semana} = 8 + \lceil \text{sesión del visor} / 2 \rceil$$

### Identificadores de Lección
- **Lecciones propias del Seminario**: Utilizan prefijo **`S` + cuatro dígitos** (`S0001`, `S0002`...) en archivos `lessonS<n>.md`.
- **Lecciones reutilizadas de Aplicaciones Móviles**: Se copian de `FlutterLearning/content/` conservando el **mismo nombre de archivo y el mismo id** (`0001`–`0088`), cambiando solo la sección `[t]` en `toc.md`.

---

## 5. Estilo de Lecciones e Ilustraciones SVG

### Regla General del Profesor
Las lecciones deben estar **ampliamente ilustradas mediante figuras vectoriales SVG**, no solamente con bloques de texto.
- **PROHIBIDO el uso de tablas Markdown** (`|---|`). Explicar en prosa corta, listas o diagramas SVG.
- **PROHIBIDO árboles de carpetas en texto ASCII (`├──`)**. Usar figuras SVG.
- Fondo claro fijo (`<rect fill="#FBFBFD" rx="16">`) sin media queries de modo oscuro (en modo oscuro se muestra como tarjeta clara aislada).
- Cada SVG lleva `id` raíz único (`<svg id="fiPasos" ...>`) y **todo** selector de estilo va prefijado (`#fiPasos .card`).

### A. Consola: Frame de Terminal SVG
Todo comando de consola se explica mediante un frame generado por [`tools/console_frame.py`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/tools/console_frame.py):
- Ventana oscura con barra de título (`Terminal · <carpeta>`) sobre tarjeta clara.
- **Prompt**: `carpeta> comando` (ej. `miapp1> flutter devices`). Nunca `$` ni `PS C:\>`.
- Comando en blanco negrita; salida en gris claro; éxito en verde.
- Elementos clave destacados con recuadros amarillos numerados (máximo 3 por figura), con sus tarjetas explicativas debajo.
- **Obligatorio**: Siempre acompañado inmediatamente debajo por un bloque cercado ` ```shell ` con el comando para facilitar el copiado.

### B. Código: Frame de Editor Anotado
Los widgets y conceptos de código se explican con frames generados por [`tools/code_frame.py`](file:///Users/domicianorincon/Documents/GIT/CoursesPlatform/SeminarioSoftware/tools/code_frame.py):
- Editor oscuro a la izquierda, vista previa o tarjetas explicativas a la derecha.
- Flechas de color que conectan cada propiedad con su efecto visual sin cruzarse.
- **Obligatorio**: Siempre acompañado inmediatamente debajo por un bloque cercado ` ```dart ` con el código real.
- Las figuras de una sesión viven en `tools/sesionN_figuras.py`. Se prueban pasándole una carpeta y se inyectan a las lecciones con `--inject`.

### C. Ejemplo Completo con *Fire it up!*
Toda lección que contenga código termina con la sección **`## Ejemplo completo`**:
- Bloque ` ```dart trycode=<gistId> ` ejecutable en DartPad.
- Programa autónomo completo en un solo archivo (`main`, `App`, rutas, pantallas).
- Gist creado como público en la cuenta `Domiciano` (`gh gist create --public`) con nombre `lessonS<n>code1.dart`.
- Validado previamente con la API de análisis de DartPad (`https://stable.api.dartpad.dev/api/v3/analyze`).

### D. Imágenes por URL en código
Cuando un ejemplo descargue imágenes de la web (`Image.network`), usar **siempre** la URL fija **`https://picsum.photos/400`** para garantizar compatibilidad con DartPad.

---

## 6. Presentaciones de las Sesiones

Las presentaciones se construyen con la skill **`presentaciones-icesi`** (disponible en el workspace en `.agents/skills/presentaciones-icesi`):
- Carpeta: `presentaciones/sesionN/` ($N$ = sesión del visor 1..16).
- Entregable: `presentacion.html` generado y commiteado en el repositorio.
- URL publicada: `https://domicianorincon.github.io/SeminarioSoftware/presentaciones/N/`
- Enlace en el visor: Al inicio de la primera lección de la sesión en `toc.md`, inmediatamente después de los tags:
  `**Presentación de la sesión:** [<título>](<URL>)`
- El workflow copia automáticamente `presentaciones/sesion*/presentacion.html` a `dist/presentaciones/N/index.html`.
