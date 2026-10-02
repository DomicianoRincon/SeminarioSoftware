# Playground

<!-- tags: DartPad, probar código sin instalar, editor en línea, Scaffold, runApp, MaterialApp, punto de partida, Run -->

Un editor de Flutter que corre en el navegador, para probar una idea sin abrir tu proyecto. Arranca con la app mínima del curso: una `MaterialApp` con una ruta y una pantalla con su `Scaffold`.

## Pruébalo

Cambia el código de la izquierda y pulsa **Run** para ver el resultado a la derecha. Un buen comienzo es reemplazar el `Text('Hola, Icesi')` por el widget que quieras probar.

```dartpad
c7ed2d4963223915971ae8ebda848400
```

## Qué tener en cuenta

- **Nada se guarda.** Al recargar la página vuelve el código inicial. Si algo te sirvió, cópialo a tu proyecto.
- **Es un solo archivo.** Aquí `App` y `HomeScreen` van juntos. En tu proyecto van separados: `App` en `lib/main.dart` y cada pantalla en `lib/screens/`.
- **No hay archivos ni paquetes propios.** Las imágenes de `assets/` y lo que declares en `pubspec.yaml` no existen aquí. Para eso usa tu proyecto.
