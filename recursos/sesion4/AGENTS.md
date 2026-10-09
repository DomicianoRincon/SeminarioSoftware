# Biblioteca de préstamos

## Qué es

App para la biblioteca de un colegio. Quien la usa busca libros por categoría, abre el
detalle de un libro y lo pide prestado. También ve la lista de sus préstamos.
No hay compras, reseñas ni lectura dentro de la app.

## Cómo se ejecuta y se revisa

- Ejecutar: `flutter run -d chrome`
- Revisar: `flutter analyze`. El único aviso aceptado es `avoid_print`.

## Estructura

- `lib/main.dart`: la app y la tabla de rutas.
- `lib/screens/`: una pantalla por archivo, `XxxScreen`.
- `lib/components/`: componentes y secciones reutilizables.
- `docs/modelo.md`: el modelo de datos.

## Convenciones

- Una Screen tiene `Scaffold` y su `body` empieza con `SafeArea`.
- Cada bloque de una pantalla es una sección en `lib/components/`, en su propio archivo. Nada de clases privadas dentro de la pantalla.
- Antes de crear un componente, revisa si ya existe en `lib/components/`.
- Imports propios con `package:miapp1/`.
- Código en inglés, también los nombres que vienen del modelo de datos: `titulo` se escribe `title`. Textos de la interfaz en español.
- Solo `StatelessWidget`. Los botones todavía no hacen nada: `print`.

## Modelo de datos

Está en `docs/modelo.md`. Una pantalla solo muestra datos que existan ahí: no inventes atributos.

## Reglas para el agente

- No agregues paquetes a `pubspec.yaml` sin preguntar.
- No toques archivos fuera de `lib/` y `docs/` sin avisar.
- Al terminar, ejecuta `flutter analyze` y di qué archivos creaste o cambiaste.
