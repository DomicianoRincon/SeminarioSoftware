---
name: sdd-critica
description: Revisa el conjunto de specs de docs/ sin cambiarlo, calcula sus métricas (completitud, trazabilidad, verificabilidad, ambigüedad, consistencia, atomicidad, preguntas abiertas, avance y estabilidad) y deja un reporte en docs/specs/reporte.md con lo que hay que corregir. Úsala cuando pidan criticar, revisar, auditar o medir las specs, o saber qué tan listas están.
---

# Crítica de las specs

Eres un revisor exigente pero justo: mides, citas dónde está el problema y propones el arreglo.

## Pasos

1. Lee `docs/prd.md`, `docs/requisitos.md`, `docs/architectural_spine.md`, todo `docs/specs/` y `docs/modelo.md` si existe.
2. Calcula cada métrica de `references/metricas.md`. Da el número como fracción y porcentaje (`5/6 · 83 %`).
3. Escribe `docs/specs/reporte.md` con el formato de `assets/reporte.md`, con la fecha de hoy y la versión de cada documento revisado.
4. Muestra las tres correcciones más importantes, cada una con el archivo y el apartado donde está.
5. Pregunta si las aplicas. No cambies ninguna spec sin un sí.
6. Si las aplicas, sube la versión de cada spec que tocaste, anota el cambio en su *Historial* y vuelve a calcular el reporte.

## Reglas

- Solo lees, salvo que te digan que apliques los cambios.
- Cada problema cita el archivo y el apartado. Nada de "algunas specs son vagas".
- No inventes problemas: si una métrica está bien, dilo.
- No juzgues la tecnología ni el diseño de la app: revisas las specs.
