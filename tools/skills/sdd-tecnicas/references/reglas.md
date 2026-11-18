# Qué va en una spec técnica

## Sí va

- Las piezas: qué archivos se crean y cuáles cambian, en qué carpeta y de qué tipo (Screen, Page, componente, formulario, servicio, modelo).
- Dónde vive cada estado y quién lo cambia, siguiendo `docs/standard_code.md`.
- Los métodos nuevos de cada servicio: nombre, qué recibe y qué devuelve.
- Los datos: columnas, buckets y rutas de archivos.
- Los paquetes nuevos y lo que pide cada plataforma (permisos, `Info.plist`, entitlements).
- La navegación: rutas nuevas y qué viaja en `arguments` o en el `pop`.
- La preparación a mano en Supabase.
- Cómo se muestran los errores (`SnackBar`, texto bajo el formulario) y qué se deshabilita mientras carga.

## No va

- El código completo. Una firma o un nombre de método, sí; el cuerpo, no.
- Decisiones que contradigan la spine o el estándar de código.
- Comportamiento nuevo que la spec funcional no pide.

## Tareas

Una tarea es lo que el implementador hace de una sentada y se puede probar al terminar.

- Bien: **T-09** Cambiar la foto desde la galería: modal inferior con *Galería*, subir al bucket y mostrarla en el perfil.
- Mal: **T-09** Hacer la foto de perfil.

Cada tarea tiene:

- Los CA que cubre.
- De qué tareas depende.
- Cómo se prueba a mano: qué hacer y qué se debe ver.

En *Piezas*, marca cada archivo con la tarea que lo crea o lo cambia, `(T-09)`. Si un componente crece en varias tareas, di qué agrega cada una.

Si una tarea toca más de cinco archivos, pártela.
