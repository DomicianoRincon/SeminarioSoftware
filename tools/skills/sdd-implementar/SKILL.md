---
name: sdd-implementar
description: Implementa las tareas pendientes de docs/impl_progress.md, de a una, siguiendo su spec técnica de docs/tecnicas/ y el estándar de código de docs/standard_code.md, y marca cada tarea como hecha con sus archivos y la fecha. Úsala cuando pidan implementar, programar o hacer una tarea (T-xx), seguir con la implementación o ver qué falta por implementar.
---

# Implementador

Implementas una tarea a la vez, como dice su spec técnica, y llevas la cuenta en `docs/impl_progress.md`.

## Pasos

1. Lee `docs/impl_progress.md`. Si no existe, dilo y sugiere la skill `sdd-tecnicas`.
2. Lee `docs/standard_code.md`. Si no existe, créalo con `assets/standard_code.md` y avisa.
3. Elige la tarea: la que pidieron, o si no dijeron cuál, la primera `[ ]` cuyas dependencias estén `[x]`. Si una dependencia está pendiente, dilo y no sigas.
4. Lee la spec técnica de la tarea (`docs/tecnicas/TS-xx-*.md`), la spec funcional que cita y los archivos de `lib/` que vas a tocar.
5. Revisa *Preparación en Supabase*. Pregunta si ya está hecha. Si no, explica qué hay que hacer en el dashboard y espera: tú no lo haces.
6. Di en tres líneas qué archivos vas a crear y cuáles vas a cambiar. Sigue sin esperar, salvo que algo no cuadre con la spec.
7. Implementa **solo esa tarea**: las piezas que la TS marca con su id, o las que necesita. Si agregas un paquete, usa `flutter pub add` y haz lo que la TS pida para cada plataforma.
8. Ejecuta `flutter analyze`. Corrige hasta que no haya errores.
9. Revisa tu código contra `references/revision.md`. Corrige lo que no cumpla.
10. Marca la tarea en `docs/impl_progress.md` con el formato de `references/progreso.md` y actualiza *Actualizado* y *Hechas*.
11. Si con esta tarea quedan hechas todas las de una TS, pasa su spec funcional a `implementada` en `docs/specs/README.md` y en la spec.
12. Termina con la prueba a mano de la tarea: qué hacer en la app y qué se debe ver. Si la prueba falla, la persona desmarca la tarea y te la vuelve a pedir. Recuerda que, si se agregó un paquete con código nativo, hay que detener la app y volver a correrla.

## Reglas

- Una tarea por vez. Si el pedido trae varias, hazlas en orden y marca cada una al terminarla.
- No cambies el comportamiento que la spec no pide, ni el código de otras tareas.
- Si la spec técnica choca con `docs/standard_code.md`, gana el estándar. Dilo y anótalo en *Preguntas abiertas* de la TS.
- Nunca marques `[x]` una tarea con errores de `flutter analyze`.
- No inventes nombres de buckets, columnas ni rutas: salen de la spec técnica o de `AGENTS.md`.
