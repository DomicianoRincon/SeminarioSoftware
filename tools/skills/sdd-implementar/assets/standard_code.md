# Estándar de código

Las reglas con las que se escribe el código de esta app. El implementador las sigue siempre, y si una spec técnica dice otra cosa, gana este archivo.

## Carpetas

- `lib/main.dart`: el `MaterialApp` y la tabla de rutas nombradas.
- `lib/models/`: los modelos, con `fromMap`, `toMap` y `copyWith`.
- `lib/services/`: las únicas clases que hablan con Supabase o con el dispositivo (la galería, por ejemplo).
- `lib/components/`: widgets reutilizables.
- `lib/screens/`: `XxxScreen`, pantallas completas con `Scaffold` a las que se navega.
- `lib/pages/`: `XxxPage`, partes de una Screen (una pestaña, un paso). No tienen `Scaffold`.

## Quién guarda estado

Solo tres tipos de widget son `StatefulWidget`:

1. Las **Screens**.
2. Las **Pages**.
3. Los **formularios** y componentes con campos de texto, que guardan solo su borrador.

Todo lo demás es `StatelessWidget`.

## Cómo se mueve el estado

- El estado vive en el `State` de la Screen, y solo se cambia con `setState`.
- Una Page guarda solo lo que nadie más usa. Lo compartido vive en la Screen y le llega a la Page por el constructor.
- Los datos **bajan** por el constructor. Los eventos **suben** con funciones: `Function()` o `Function(Tipo)`, nunca `VoidCallback` ni `ValueChanged`.
- Un modelo no se modifica: se reemplaza con `copyWith`.
- Un formulario no se queda con el dato: al enviarlo, lo entrega con su función (`onAdd(track)`).

## Supabase

- Las Screens llaman a los servicios; los servicios llaman a Supabase.
- Los métodos que van a Supabase devuelven un `Future` y se usan con `await`.
- Después de un `await`, `if (!mounted) return;` antes de usar `context` o `setState`.

## Navegación

- Solo rutas nombradas, registradas en `routes:` del `MaterialApp`.
- Se pasa un dato con `arguments` y se devuelve un resultado con `Navigator.pop(context, resultado)`.

## Escritura

- Código en inglés: clases, archivos, variables y rutas. Los textos que ve el usuario, en español.
- Imports del proyecto con `package:<nombre_del_paquete>/...` (el `name` de `pubspec.yaml`), nunca relativos.
- Sin comentarios, salvo una línea `///` que describe cada clase pública.
- Para redondear una imagen: `Container` con `borderRadius` y `clipBehavior: Clip.antiAlias`, sin `ClipRRect`.
