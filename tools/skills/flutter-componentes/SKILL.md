---
name: flutter-componentes
description: Crea y conecta componentes reutilizables de Flutter al estilo del curso. Los datos bajan por el constructor, los eventos suben con funciones y el estado vive en la Screen o en un formulario. Úsala cuando pidan crear un componente, sacar un pedazo de pantalla a un componente, agregarle un evento (onTap, onDelete, onAdd) a una card o a una lista, o conectar un componente con el estado de la pantalla.
---

# Componentes de Flutter

Un componente no sabe quién lo usa: recibe lo que muestra y avisa lo que pasó.

## Pasos

1. Lee `references/reglas.md`. Dice quién guarda estado, cómo bajan los datos y cómo suben los eventos.
2. Mira `lib/components/` y `lib/models/`. Si ya hay un componente o un modelo que sirve, úsalo o amplíalo.
3. Decide el tipo de componente:
   - Si solo muestra datos y avisa toques, es un `StatelessWidget`. Plantilla: `assets/product_card.dart`.
   - Si solo reparte una lista entre cards, es un `StatelessWidget` que pasa las funciones. Plantilla: `assets/product_list.dart`.
   - Si el usuario escribe en él, es un formulario `StatefulWidget`. Plantilla: `assets/product_form.dart`.
4. Haz la lista de lo que recibe: los datos, como campos `final`, y los eventos, como `Function()` o `Function(Tipo)`.
5. Si el componente trabaja con un objeto, búscalo o créalo en `lib/models/` con `copyWith`. Plantilla: `assets/product.dart`.
6. Escribe el componente en su propio archivo de `lib/components/`.
7. Conéctalo en la Screen, que es la dueña del estado. Plantilla: `assets/shopping_screen.dart`. Cada función que pasa la Screen hace su `setState` o su llamada al `Navigator`.
8. Ejecuta `flutter analyze` y corrige hasta que no haya avisos.
9. Termina con un resumen de tres líneas: qué recibe el componente, qué avisa y quién guarda el estado.

## Reglas

- Las plantillas usan `my_app` como paquete. Cámbialo por el `name` de `pubspec.yaml`.
- Nunca pongas `setState` ni `Navigator` dentro de un componente que no sea la Screen.
- No agregues paquetes nuevos.
- Si lo pedido rompe una regla de `references/reglas.md`, no lo hagas: di cuál y propón cómo hacerlo dentro de las reglas.
