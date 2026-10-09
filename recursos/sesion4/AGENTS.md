# Red profesional

## Qué es

Red social profesional, al estilo de LinkedIn. Cada persona tiene un perfil con su cargo
y su ciudad, publica textos cortos sobre su trabajo, sigue a otras personas y conversa
con ellas por mensajes.
No hay fotos en las publicaciones, ni "me gusta", ni comentarios, ni compartir.

## Cómo se ejecuta y se revisa

- Ejecutar: `flutter run -d chrome`
- Revisar: `flutter analyze`. No debe quedar ningún error en `lib/`.

## Estructura

- `lib/main.dart`: la app y la tabla de rutas.
- `lib/screens/`: una pantalla por archivo, `XxxScreen`.
- `lib/components/`: componentes reutilizables, uno por archivo.
- `docs/modelo.md`: el modelo de datos.

## Convenciones

- Una Screen tiene `Scaffold` y su `body` empieza con `SafeArea`.
- Lo que se repite en una pantalla es un componente en `lib/components/`. Nada de clases privadas.
- Antes de crear un componente, revisa si ya existe en `lib/components/`.
- Imports propios con `package:mi_app_1/`.
- Código en inglés, también los nombres que vienen del modelo de datos: `cargo` se escribe `role`. Textos de la interfaz en español.
- Solo `StatelessWidget`. Los botones todavía no hacen nada: `onPressed: () {}`.

## Modelo de datos

Está en `docs/modelo.md`. Una pantalla solo muestra datos que existan ahí: no inventes atributos.

## Reglas para el agente

- No agregues paquetes a `pubspec.yaml` sin preguntar.
- No toques archivos fuera de `lib/` y `docs/` sin avisar.
- Al terminar, ejecuta `flutter analyze` y di qué archivos creaste o cambiaste.
