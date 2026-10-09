---
name: flutter-pantallas
description: Construye pantallas y componentes de Flutter con la paleta mínima de widgets del curso y componentes reutilizables. Úsala cuando pidan crear o cambiar una pantalla, una sección o un componente de la app.
---

# Pantallas de Flutter

Armas pantallas estáticas: se ven, pero todavía no navegan ni guardan estado.

## Pasos

1. Lee `references/widgets.md`. Es la paleta: los únicos widgets que puedes usar.
2. Mira qué hay en `lib/components/`. Si un componente ya sirve, úsalo.
3. Divide la pantalla en bloques, de arriba hacia abajo.
4. Lo que se repite, o lo que podría servir en otra pantalla, es un componente: se escribe una vez y recibe sus datos por parámetros.
5. Escribe cada componente nuevo en su archivo de `lib/components/`, a partir de `assets/component.dart`.
6. Escribe la pantalla en `lib/screens/`, a partir de `assets/screen.dart`. La pantalla solo acomoda componentes.
7. Registra la pantalla en `routes` de `lib/main.dart`.
8. Ejecuta `flutter analyze`.

## Reglas

- Solo `StatelessWidget`. Los datos de ejemplo van escritos en el código.
- Los botones no navegan ni cambian nada: `onPressed: () {}`.
- Un componente no conoce la pantalla que lo usa: todo lo que cambia entre un uso y otro llega por el constructor.
- Si lo pedido necesita algo fuera de la paleta, no lo uses: dilo y propón cómo acercarse con la paleta.
