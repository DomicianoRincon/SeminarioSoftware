---
name: sdd-requisitos
description: Saca los requisitos funcionales y no funcionales del PRD y los deja numerados y verificables en docs/requisitos.md, cada uno ligado al objetivo que atiende. Úsala cuando pidan crear los requerimientos o los requisitos, sacar los RF y RNF, o pasar del PRD a una lista de lo que el sistema debe hacer.
---

# Requisitos del proyecto

Un requisito es una frase que se puede comprobar. Si no se puede comprobar, todavía no es un requisito.

## Pasos

1. Lee `docs/prd.md`. Si no existe, dilo, sugiere la skill `sdd-prd` y no sigas.
2. Lee `references/reglas.md`.
3. Por cada objetivo del PRD (`O-01`, `O-02`…), escribe los requisitos funcionales que lo hacen posible. Después, los no funcionales.
4. **Muéstralos agrupados por objetivo.** Señala los que dudas y pregunta. Pregunta también la prioridad de cada uno: *Debe*, *Debería* o *Podría*.
5. Escribe `docs/requisitos.md` con el formato de `assets/requisitos.md`: fecha de hoy, versión `0.1.0`, estado `borrador` y la versión del PRD en que te basaste.
6. Termina con un resumen: cuántos RF y RNF, cuántos *Debe*, y si algún objetivo del PRD quedó sin requisito (debería ser ninguno). Sugiere seguir con la skill `sdd-arquitectura`.

## Reglas

- Una línea por requisito, con su id (`RF-01`, `RNF-01`) y el objetivo que atiende.
- Sin tecnología: nada de Supabase, Flutter, tablas, pantallas ni botones.
- Los ids no se renumeran. Si un requisito se quita, se marca *(retirado)* y su id no se reusa.
- No agregues requisitos que el equipo no pidió. Si crees que falta algo, pregúntalo.
