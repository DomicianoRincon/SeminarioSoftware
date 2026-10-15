# Ciclo de vida: initState, dispose y TextEditingController

<!-- tags: initState, dispose, TextEditingController, leer el texto de un TextField, ciclo de vida de un State, controller.text, liberar el controller, setState() called after dispose(), mounted, late -->

En la lección de `TextField` quedó pendiente algo: los campos se dejaban escribir, pero la app no podía leer lo escrito. Para leerlo hace falta un `TextEditingController`, y ese controlador tiene que nacer y morir junto con la pantalla. Para eso existen dos métodos del State: `initState` y `dispose`.

## La vida de un State

Un objeto State pasa por estos momentos:

```svg
<svg id="lcLinea" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 392" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="lcLinea-ttl lcLinea-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="lcLinea-ttl">La vida de un objeto State</title>
  <desc id="lcLinea-dsc">Línea de tiempo con cinco momentos: createState, initState, build, setState que vuelve a llamar a build, y dispose. createState e initState ocurren una vez, build y setState muchas veces, dispose una vez. Debajo, el TextEditingController se crea en initState y se libera en dispose.</desc>
  <defs>
    <style>
      #lcLinea .title{fill:#161A26;font-size:22px;font-weight:700}
      #lcLinea .sub{fill:#79809A;font-size:13.5px}
      #lcLinea .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #lcLinea .nt{font-size:15px;font-weight:700;fill:#161A26}
      #lcLinea .nb{fill:#454C61;font-size:13px}
      #lcLinea .lbl{fill:#556074;font-size:12px;font-weight:600}
      #lcLinea .foot{fill:#79809A;font-size:12px}
      #lcLinea .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #lcLinea .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#lcLinea-arrow)}
    </style>
    <marker id="lcLinea-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="392" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La vida de un objeto <tspan class="mono">State</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Nace una vez, se dibuja muchas veces y muere una vez. El controller sigue esa misma vida.</text>
  <path d="M80,200 H880" stroke="#C4CBD8" stroke-width="3" stroke-linecap="round"/>
  <circle cx="128" cy="200" r="11" fill="#FFF3DC" stroke="#A96C05" stroke-width="2.5"/>
  <text x="128" y="176" font-size="14" font-weight="700" fill="#A96C05" text-anchor="middle" class="mono">createState</text>
  <text x="128" y="236" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="middle">Flutter crea</text><text x="128" y="253" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="middle">el State</text>
  <circle cx="296" cy="200" r="11" fill="#E8F6E3" stroke="#3A8235" stroke-width="2.5"/>
  <text x="296" y="176" font-size="14" font-weight="700" fill="#3A8235" text-anchor="middle" class="mono">initState</text>
  <text x="296" y="236" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="middle">Preparar lo que</text><text x="296" y="253" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="middle">el State necesita</text>
  <circle cx="480" cy="200" r="11" fill="#EEF1FF" stroke="#4453C9" stroke-width="2.5"/>
  <text x="480" y="176" font-size="14" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono">build</text>
  <text x="480" y="236" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="middle">Dibujar con los</text><text x="480" y="253" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="middle">datos actuales</text>
  <circle cx="640" cy="200" r="11" fill="#F4EBFF" stroke="#7439B8" stroke-width="2.5"/>
  <text x="640" y="176" font-size="14" font-weight="700" fill="#7439B8" text-anchor="middle" class="mono">setState</text>
  <text x="640" y="236" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="middle">Cambiar un dato</text><text x="640" y="253" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="middle">y pedir build</text>
  <circle cx="832" cy="200" r="11" fill="#FFEBEF" stroke="#C2354F" stroke-width="2.5"/>
  <text x="832" y="176" font-size="14" font-weight="700" fill="#C2354F" text-anchor="middle" class="mono">dispose</text>
  <text x="832" y="236" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="middle">Limpiar antes</text><text x="832" y="253" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="middle">de desaparecer</text>
  <path class="link" d="M626,158 C612,138 508,138 494,158"/>
  <path d="M104,132 V124 H320 V132" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="212.0" y="116" font-size="12" font-weight="600" fill="#79809A" text-anchor="middle">una vez</text>
  <path d="M456,132 V124 H664 V132" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="560.0" y="116" font-size="12" font-weight="600" fill="#79809A" text-anchor="middle">muchas veces</text>
  <path d="M808,132 V124 H856 V132" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="832.0" y="116" font-size="12" font-weight="600" fill="#79809A" text-anchor="middle">una vez</text>
  <rect x="208" y="292" width="704" height="72" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="232" y="320" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">TextEditingController</text>
  <text x="232" y="344" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="660">Se crea en initState y se libera en dispose. Si no se libera, queda ocupando memoria.</text>
  <path d="M296,264 V292" stroke="#9FD68D" stroke-width="1.75" stroke-dasharray="3 4"/>
  <path d="M832,264 V292" stroke="#F3A3B2" stroke-width="1.75" stroke-dasharray="3 4"/>
</svg>
```

- **`createState`**: Flutter crea el objeto State. Una vez.
- **`initState`**: corre una sola vez, justo después de crearlo y antes del primer `build`. Aquí se prepara lo que el State necesita.
- **`build`**: corre la primera vez y cada vez que algo pide reconstruir. Muchas veces.
- **`dispose`**: corre una vez, cuando la pantalla se va para siempre. Aquí se libera lo que se creó en `initState`.

Abre la pantalla de saludo, escribe tu nombre y vuelve. Mira cómo se van encendiendo los pasos y qué pasa con el controller.

```interactive
state-lifecycle
```

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

Si no se llama `_nameController.dispose()`, el controller queda ocupando memoria aunque la pantalla ya no exista. Una pantalla no se nota, pero una app que abre y cierra formularios todo el día sí. Por eso la regla del curso es: **todo componente con un campo de texto es un `StatefulWidget` dueño de su controller, con su `dispose`**.

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

En el diagrama de arriba el saludo cambia con cada letra. Eso se logra con `onChanged: (value) => setState(() {})` en el `TextField`: cada tecla pide un `build`, y el `build` lee `_nameController.text`. Sirve para cosas como un contador de caracteres, pero en un formulario normal basta con leer al pulsar el botón.

## setState() called after dispose()

En el diagrama, pulsa *Guardar (tarda 2 s)* y vuelve a la pantalla de inicio antes de que pasen los dos segundos. La consola muestra:

```text
setState() called after dispose(): _GreetingScreenState#…
```

Algo intentó llamar a `setState` en un State que ya se había ido. Pasa con todo lo que termina después de un tiempo: una espera, una descarga, una consulta a una base de datos. La salida es preguntar antes si el State sigue montado:

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
