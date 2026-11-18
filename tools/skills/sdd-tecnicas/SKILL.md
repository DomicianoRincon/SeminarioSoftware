---
name: sdd-tecnicas
description: Pasa cada spec funcional de docs/specs/ a una spec técnica en docs/tecnicas/ (pantallas, componentes, servicios, datos, paquetes y plataformas) y la parte en tareas T-xx que agrega como pendientes a docs/impl_progress.md. Úsala cuando pidan la spec técnica, el diseño técnico, el plan de implementación o las tareas de una funcionalidad.
---

# Specs técnicas

La spec funcional dice qué hace el sistema. La técnica dice con qué piezas del proyecto se construye, y la parte en tareas que un implementador puede hacer de a una.

## Pasos

1. Lee `AGENTS.md`, `docs/architectural_spine.md`, `docs/standard_code.md` y la spec funcional pedida en `docs/specs/`. Si falta alguno, dilo y sugiere la skill que lo crea (`docs/standard_code.md` lo crea `sdd-implementar`).
2. Lee `references/reglas.md`.
3. Mira `lib/` para saber qué ya existe. Reusa lo que sirva: una pieza nueva solo si no hay otra que sirva.
4. Si ya existe `docs/tecnicas/`, léela: vas a actualizar, no a empezar de cero.
5. **Borrador.** Muestra las piezas (archivos nuevos y archivos que cambian) y la lista de tareas, cada una con los CA que cubre. Pregunta si está bien antes de escribir.
6. Escribe `docs/tecnicas/TS-xx-nombre-corto.md` con el formato de `assets/tecnica.md`. `TS-04` es la técnica de `F-04`.
7. Agrega las tareas, todas `[ ]`, a `docs/impl_progress.md` bajo el título de su TS. Si el archivo no existe, créalo con `assets/impl_progress.md`. Las tareas siguen la numeración del archivo: si la última es `T-08`, la primera nueva es `T-09`.
8. Termina con un resumen: cuántas tareas, cuáles necesitan algo hecho a mano en Supabase y qué CA quedó sin tarea. Sugiere seguir con la skill `sdd-implementar`.

## Reglas

- Cada CA de la spec funcional queda en al menos una tarea.
- Lo que se hace a mano en el dashboard de Supabase (buckets, policies, columnas) va en *Preparación*, no en una tarea: el implementador no lo puede hacer.
- No cambies la spec funcional. Si encuentras un hueco, ponlo en *Preguntas abiertas* y dilo.
- No agregues paquetes que la spine no permita sin preguntar.
- Los ids no se renumeran. Una tarea que ya no aplica se tacha (`~~T-07~~`), no se borra.
