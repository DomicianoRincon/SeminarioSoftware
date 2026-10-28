# Reglas de los componentes

## Quién guarda estado

Solo dos tipos de widget son `StatefulWidget`:

- **La Screen**, dueña de los datos de la pantalla, por ejemplo `List<Product> _products`.
- **El formulario**, que guarda solo el borrador: sus `TextEditingController` y el aviso de error.

Todo lo demás es `StatelessWidget`: cards, listas, encabezados y botones.

## Los datos bajan

- Llegan por el constructor, en campos `final` con `required`.
- El componente no los cambia. Para cambiar un objeto, la Screen lo reemplaza con `copyWith`:
  `_products[index] = product.copyWith(isBought: true)`.
- Si una lista no usa un dato y solo lo pasa a sus cards, está bien. Si son más de tres niveles, avísalo: es prop drilling.

## Los eventos suben

- Con el tipo función: `Function()` si no lleva datos y `Function(Product)` si lleva el objeto.
- Nunca uses `VoidCallback` ni `ValueChanged`.
- Al widget de Flutter se le pasa envuelta: `onPressed: () => onDelete()`.
- La card avisa sin datos (`onDelete()`) y la lista le agrega el objeto (`onDelete: () => onDelete(product)`).
- Para tocar una card entera, envuelve su `Container` en un `GestureDetector` con `onTap`.
- El formulario sube el objeto terminado (`widget.onAdd(product)`), limpia sus campos y no se lo queda.

## Navegación

- Solo la Screen llama al `Navigator`. Un componente avisa con una función, como `onOpen`, y la Screen hace el `pushNamed`.
- Solo hay rutas nombradas, registradas en `routes:` de `lib/main.dart`.
- Los datos para la pantalla nueva van en `arguments`.

## Código

- Imports del proyecto con `package:`, nunca relativos.
- El código va en inglés y los textos que ve el usuario, en español.
- Sin comentarios, salvo una línea `///` sobre cada clase pública.
- Un archivo por componente, con el nombre en `snake_case`: `product_card.dart` para `ProductCard`.
- Para redondear una imagen, usa un `Container` con `borderRadius` y `clipBehavior: Clip.antiAlias`. Nunca uses `ClipRRect`.
- Si un formulario tiene un `TextEditingController`, debe tener también su `dispose()`.
