---
name: sdd-prd
description: Entrevista al equipo sobre su proyecto y escribe el PRD, el documento de producto, en docs/prd.md con el problema, los usuarios, los objetivos medibles y el alcance. Úsala cuando digan "mi proyecto se trata de…", pidan el PRD o el documento de producto, o quieran definir qué problema resuelve la app y para quién.
---

# PRD del proyecto

No inventas el producto: lo sacas de las respuestas del equipo.

## Pasos

1. Lee `AGENTS.md` o `CLAUDE.md` si existen. Si ya hay `docs/prd.md`, pregunta si se actualiza o se parte de cero.
2. Repite en una frase lo que entendiste del proyecto y pregunta si es así.
3. **Entrevista.** Haz las preguntas de `references/preguntas.md` en rondas de máximo cuatro y espera las respuestas antes de seguir. Si una respuesta es vaga ("que sea fácil", "rápido"), pide un ejemplo o un número.
4. **Borrador.** Muestra en pocas líneas el problema, los usuarios y los objetivos. Pregunta si falta algo.
5. Escribe `docs/prd.md` con el formato de `assets/prd.md`: fecha de hoy, versión `0.1.0` y estado `borrador`.
6. Termina con un resumen: cuántos objetivos quedaron, qué quedó fuera del alcance y qué preguntas siguen abiertas. Sugiere seguir con la skill `sdd-requisitos`.

## Reglas

- El PRD dice qué problema se resuelve y para quién. No escribas tecnologías, pantallas, tablas ni código.
- Cada objetivo tiene id (`O-01`, `O-02`…) y una frase de cómo se sabe que se cumplió.
- Lo que el equipo no sepa va en *Preguntas abiertas*. No lo inventes.
- Si actualizas el PRD, sube la versión (la menor si agregas, la mayor si cambia el problema o los usuarios), cambia la fecha y anota el cambio en *Historial*.
