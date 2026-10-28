# Paleta de widgets

Solo estos. Entre paréntesis, las propiedades que se usan.

## Contenido

- `Text` (`style`, `maxLines`, `overflow`) con `TextStyle` (`fontSize`, `fontWeight`, `color`). Colores con `Colors.` o `Color(0xFF...)`.
- `Icon` (`size`, `color`).
- `Image.network` e `Image.asset` (`width`, `height`, `fit`). Imagen de ejemplo: `https://picsum.photos/400`.
- `CircleAvatar` (`radius`, `backgroundImage: NetworkImage(...)`).

## Botones

- `ElevatedButton`, `OutlinedButton`, `TextButton` (`onPressed`, `child`, `style` con `styleFrom`) e `IconButton` (`onPressed`, `icon`).

## Entrada

- `TextField`, solo su aspecto: `decoration: InputDecoration(labelText, hintText, prefixIcon, border)`, `obscureText`, `keyboardType`. Sin `controller`.

## Acomodar

- `Column` y `Row` (`mainAxisAlignment`, `crossAxisAlignment`, `mainAxisSize`, `spacing`, `children`).
- `SizedBox` para separar (`width`, `height`).
- `Expanded` (`flex`) y `Spacer`, solo dentro de `Row` o `Column`.
- `Padding` con `EdgeInsets.all`, `symmetric` u `only`.
- `Container` (`width`, `height`, `padding`, `margin`, `decoration: BoxDecoration(color, border, borderRadius)`). Para recortar al hijo, `clipBehavior: Clip.antiAlias`.
- `Card` (`elevation`, `color`, `shape: RoundedRectangleBorder(borderRadius, side)`), para una tarjeta.
- `Center`.
- `SingleChildScrollView` (`padding`, `scrollDirection`). Adentro no van `Expanded` ni `Spacer`.

## Estructura de la pantalla

- `Scaffold` (`appBar`, `body`, `backgroundColor`, `floatingActionButton`, `bottomNavigationBar`).
- `SafeArea`: el `body` siempre empieza con uno.
- `AppBar` (`title`, `leading`, `actions`, `centerTitle`, `backgroundColor`, `foregroundColor`).
- `BottomNavigationBar` (`items`, `currentIndex` fijo). Solo se ve: no responde al toque.
- `FloatingActionButton` (`onPressed`, `child`).

## Fuera de la paleta

No se usan todavía. En su lugar:

- `ListView`, `GridView`: una `Column` o una `Row` dentro de un `SingleChildScrollView`.
- `ListTile`: una `Row` dentro de un `Card` o de un `Container`.
- `Stack`, `Positioned`, `Wrap`, `Align`: reorganiza con `Column`, `Row` y `mainAxisAlignment`.
- `ClipRRect`: `Container` con `clipBehavior`.
- `GestureDetector`, `InkWell`: un botón de la paleta.
- `StatefulWidget`, `setState`, `Switch`, `Checkbox`: no hay estado.
- `Navigator`, `showDialog`, `SnackBar`: no hay navegación.
- `FutureBuilder`, `StreamBuilder` y cualquier paquete nuevo.
