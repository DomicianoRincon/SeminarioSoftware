---
name: sdd-specs
description: Escribe las specs funcionales del proyecto, una por funcionalidad, en docs/specs/, con metadatos (id, versión, fecha, estado), flujos, reglas, estados y criterios de aceptación, más un índice con el estado de cada una. Úsala cuando pidan crear o actualizar las specs funcionales, especificar una funcionalidad o pasar de los requisitos a specs.
---

# Specs funcionales

Una spec dice qué hace el sistema y cómo se comporta, nunca con qué se construye.

## Pasos

1. Lee `docs/prd.md`, `docs/requisitos.md` y `docs/architectural_spine.md`, y `docs/modelo.md` si existe. Si falta uno de los tres primeros, dilo y sugiere la skill que lo crea.
2. Lee `references/reglas.md`.
3. Si ya existe `docs/specs/`, léela: vas a actualizar, no a empezar de cero.
4. **Propón la lista de funcionalidades** (`F-01`, `F-02`…), cada una con los RF que cubre. Todo RF debe quedar en alguna. Pregunta si la lista está bien antes de escribir.
5. Escribe cada spec en `docs/specs/F-01-nombre-corto.md` con el formato de `assets/spec.md`: versión `0.1.0`, estado `borrador`, fecha de hoy.
6. Escribe `docs/specs/README.md` con el formato de `assets/indice.md`.
7. Termina con un resumen: cuántas specs, si quedó algún RF sin spec y cuántas preguntas abiertas hay. Sugiere revisar el conjunto con la skill `sdd-critica`.

## Reglas

- Sin tecnología: nada de Supabase, Flutter, widgets, `setState`, tablas ni SQL. Los datos se nombran como los nombra el usuario: *publicación*, *foto de perfil*.
- Una spec, una funcionalidad. Si mezcla dos, pártela.
- Los ids no se renumeran. Una spec que se quita pasa a estado `obsoleta`.
- Si cambias una spec, sube su versión, cambia la fecha, anota el cambio en *Historial* y actualiza el índice.
- Lo que no sepas va en *Preguntas abiertas*. No lo inventes.
