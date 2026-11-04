---
name: sdd-arquitectura
description: Escribe la architectural spine del proyecto en docs/architectural_spine.md, con un resumen, un diagrama mermaid, el stack tecnológico, qué cubre cada servicio y las invariantes que nadie del equipo puede decidir distinto. Pensada para una app Flutter con backend en Supabase (Auth, base de datos con PostgREST y Storage). Úsala cuando pidan especificar o definir la arquitectura, el stack, la spine o el diagrama de la app.
---

# Architectural spine

La spine fija solo lo que, si cada integrante lo decide por su lado, rompe la app. Lo demás se deja para después.

## Pasos

1. Lee `docs/prd.md` y `docs/requisitos.md`. Si falta alguno, dilo y sugiere la skill que lo crea. Lee también `AGENTS.md` y `docs/modelo.md` si existen.
2. Lee `references/supabase.md`.
3. Si el pedido no lo dice, pregunta en una sola ronda: para qué se usa la autenticación, qué se guarda en la base de datos, qué archivos van a Storage y en qué plataformas corre la app.
4. **Borrador.** Muestra el diagrama y la lista de invariantes (`AD-01`, `AD-02`…). Pregunta si algo no cuadra.
5. Escribe `docs/architectural_spine.md` con el formato de `assets/architectural_spine.md`: fecha de hoy, versión `0.1.0`, estado `borrador` y las versiones del PRD y de los requisitos en que te basaste.
6. Termina con un resumen de tres líneas: el stack, cuántas invariantes y qué quedó en *Diferido*. Sugiere seguir con la skill `sdd-specs`.

## Reglas

- Corta: que quepa en una o dos páginas.
- Cada invariante tiene **Regla** (lo que siempre se hace) y **Evita** (el problema que previene).
- Sin código, sin nombres de widgets y sin el detalle de las tablas: para eso está `docs/modelo.md`.
- El diagrama es un `flowchart` de mermaid que se pueda leer en GitHub.
- No agregues servicios que el equipo no nombró. Si crees que hace falta uno, ponlo en *Diferido* y pregunta.
- No agregues paquetes además de `supabase_flutter` sin preguntar.
