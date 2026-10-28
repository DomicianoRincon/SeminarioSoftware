---
name: disenador-bd
description: Diseña la base de datos de la app entrevistando al usuario y la normaliza paso a paso hasta la tercera forma normal (3FN). Deja el modelo en docs/modelo.md. Úsala cuando pidan diseñar la base de datos, armar el modelo de datos, decidir qué tablas hacen falta, normalizar o llevar un modelo a primera, segunda o tercera forma normal.
---

# Diseñador de base de datos

No inventas el modelo: lo sacas de las respuestas del usuario y le muestras cada cambio.

## Pasos

1. Si ya existe `docs/modelo.md`, léelo y pregunta si se parte de él o de cero.
2. **Entrevista.** Haz las preguntas de `references/preguntas.md` en rondas de máximo cuatro, y espera las respuestas antes de seguir. Si una respuesta deja una duda, pregunta otra vez. No supongas.
3. **Borrador.** Con las respuestas, escribe una lista de entidades con sus atributos, sin normalizar todavía. Muéstrala y pregunta si falta algo.
4. **Normaliza.** Sigue `references/normalizacion.md`, una forma normal a la vez: 1FN, luego 2FN y luego 3FN. En cada una:
   - di qué regla revisas;
   - señala qué atributo o tabla la rompe y por qué, con un dato de ejemplo;
   - muestra el cambio, que puede ser una tabla nueva, un atributo que se mueve o una llave nueva;
   - pregunta si el usuario está de acuerdo antes de pasar a la siguiente.

   Si una forma normal ya se cumple, dilo y explica por qué.
5. **Relaciones.** Para cada FK, pregunta la cardinalidad si no quedó clara: uno a uno, uno a muchos o muchos a muchos. Una relación muchos a muchos se resuelve con una tabla intermedia.
6. Escribe el resultado en `docs/modelo.md` con el formato de `assets/modelo.md`.
7. Termina con un resumen: cuántas tablas quedaron, qué cambió en cada forma normal y qué le preguntarías al cliente si hubiera dudas. Sugiere dibujarlo con la skill `mer-svg`.

## Reglas

- Las tablas van en plural y en `snake_case`, igual que sus atributos: `canciones`, `fecha_creacion`.
- Cada tabla tiene `id (PK)`. Una FK se escribe `<tabla_en_singular>_id (FK a <tabla>)`.
- No agregues tablas ni atributos que el usuario no haya mencionado. Si crees que falta algo, pregúntalo.
- No escribas SQL ni código: el resultado es `docs/modelo.md`.
