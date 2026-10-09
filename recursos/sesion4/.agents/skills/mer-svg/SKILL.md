---
name: mer-svg
description: Dibuja el diagrama entidad-relación (MER) de la app como un archivo SVG, a partir de docs/modelo.md. Úsala cuando pidan el MER, el diagrama de base de datos, el diagrama entidad-relación o "dibuja el modelo de datos".
---

# MER en SVG

Escribes el SVG a mano, como código. No uses Mermaid ni ninguna librería.

## Pasos

1. Lee `docs/modelo.md`. Es la única fuente: no agregues ni quites tablas o atributos.
2. Lee `references/estilo.md`. Trae las medidas, los colores y cómo se dibuja cada relación.
3. Lee `assets/ejemplo.svg`. Es un diagrama terminado: el tuyo debe verse igual.
4. Ordena las tablas para que las que se relacionan queden vecinas.
5. Calcula la posición de cada tabla con las medidas de `references/estilo.md` antes de escribir.
6. Escribe el resultado en `docs/mer.svg`.
7. Revisa: cada tabla y cada atributo de `docs/modelo.md` está en el SVG, y cada relación tiene su línea.

## Reglas

- El texto en SVG no se parte solo: una línea por `<text>`.
- Fondo claro fijo. Sin modo oscuro, sin imágenes y sin enlaces externos.
- Los nombres de tablas y atributos van igual que en `docs/modelo.md`.
- Si una relación no cabe entre tablas vecinas, cambia el orden de las tablas. No cruces líneas sobre una tabla.
- Una línea solo une las dos tablas de su relación. Si una tabla tiene más de dos relaciones, va en el centro: dos tablas a sus lados y las demás justo debajo, en la misma columna.
- El pie es una sola línea de máximo 100 caracteres.
