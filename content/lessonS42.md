# Ciclo de vida: initState, dispose y TextEditingController

<!-- tags: initState, dispose, TextEditingController, leer el texto de un TextField, ciclo de vida de un State, controller.text, liberar el controller, setState() called after dispose(), mounted, late -->

En la lección de `TextField` los campos se dejaban escribir, pero la app no podía leer lo escrito. Para leerlo hace falta un `TextEditingController`, y ese controller tiene que nacer y morir junto con la pantalla. Para eso el State tiene dos métodos: `initState` y `dispose`.

## La vida de un State

Un objeto State nace una vez, se dibuja muchas veces y muere una vez. Pruébalo: abre la pantalla de saludo, escribe tu nombre, pulsa *Saludar* y vuelve con la flecha. A la derecha se enciende la fase por la que va el State, y cada bloque cuenta cuántas veces corrió.

```interactive
state-lifecycle
```

Fíjate en dos cosas. Escribir en el campo no enciende nada: cambia el texto del controller, pero no llama a `setState`. Y al volver y abrir otra vez, el State es otro (`#2`), con un controller nuevo.

- **`initState`** corre una sola vez, antes del primer `build`. Ahí se crea lo que el State necesita.
- **`build`** corre cada vez que algo pide reconstruir, como `setState`.
- **`dispose`** corre una sola vez, cuando la pantalla se va. Ahí se libera lo que se creó en `initState`.

## El TextEditingController

El controller es el objeto que guarda el texto de un campo. Se crea en `initState`, se conecta al `TextField` y se libera en `dispose`:

```dart
class _GreetingScreenState extends State<GreetingScreen> {
  late TextEditingController _nameController;

  @override
  void initState() {
    super.initState();
    _nameController = TextEditingController();
  }

  @override
  Widget build(BuildContext context) {
    return TextField(controller: _nameController);
  }

  @override
  void dispose() {
    _nameController.dispose();
    super.dispose();
  }
}
```

- `late` le dice a Dart que el campo tendrá valor antes de usarse, aunque no se le dé en la declaración. Se lo damos en `initState`.
- En `initState`, `super.initState()` va **primero**. En `dispose`, `super.dispose()` va **al final**.
- Para leer lo escrito: `_nameController.text`. Para borrarlo: `_nameController.clear()`.

Si no se llama `_nameController.dispose()`, el controller queda ocupando memoria aunque la pantalla ya no exista. Por eso la regla del curso es: **todo componente con un campo de texto es un `StatefulWidget` dueño de su controller, con su `dispose`**.

## Leer el texto con un botón

Lo más común es leer el campo cuando se pulsa un botón. El valor se copia a un campo del State dentro de `setState`, para que la pantalla lo muestre:

```dart
String _greeting = 'Hola';

void _greet() {
  setState(() {
    _greeting = 'Hola, ${_nameController.text}';
  });
}
```

```dart
FilledButton(
  onPressed: () => _greet(),
  child: const Text('Saludar'),
),
Text(_greeting),
```

## setState() called after dispose()

Si algo tarda (una espera, una descarga, una consulta) y el usuario se va de la pantalla antes de que termine, el `setState` del final llega a un State que ya pasó por `dispose`. La consola muestra:

```text
setState() called after dispose(): _GreetingScreenState#…
```

La salida es preguntar antes si el State sigue montado:

```dart
if (!mounted) return;
setState(() {
  _saved = true;
});
```

Con los servicios de las sesiones 11 a 14 lo vas a ver seguido.

## Ejemplo completo

Una pantalla que pide un nombre y saluda al pulsar el botón, con el controller creado en `initState` y liberado en `dispose`.

```dart trycode=03a91a720d6158b2fc3f377b71a7c2ca
import 'package:flutter/material.dart';

void main() {
  runApp(const App());
}

/// Root of the app, with the route table.
class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      routes: {
        '/': (context) => const GreetingScreen(),
      },
    );
  }
}

/// Screen that greets the name typed in the field.
class GreetingScreen extends StatefulWidget {
  const GreetingScreen({super.key});

  @override
  State<GreetingScreen> createState() => _GreetingScreenState();
}

class _GreetingScreenState extends State<GreetingScreen> {
  late TextEditingController _nameController;
  String _greeting = 'Hola';

  @override
  void initState() {
    super.initState();
    _nameController = TextEditingController();
  }

  void _greet() {
    setState(() {
      _greeting = 'Hola, ${_nameController.text}';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Saludo')),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextField(
                controller: _nameController,
                decoration: const InputDecoration(
                  labelText: 'Nombre',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 12),
              FilledButton(
                onPressed: () => _greet(),
                child: const Text('Saludar'),
              ),
              const SizedBox(height: 24),
              Text(_greeting, style: const TextStyle(fontSize: 24)),
            ],
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _nameController.dispose();
    super.dispose();
  }
}
```
