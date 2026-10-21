# setState: el contador de flutter create

<!-- tags: setState, contador de flutter create, árbol de widgets, _incrementCounter, la pantalla no se actualiza, reconstrucción con build, print en build, FloatingActionButton -->

Cuando creas un proyecto con `flutter create`, la app que viene de ejemplo es un contador: un número en el centro y un botón `+` que lo sube. En la sesión 2 la borraste para empezar con tu propia `HomeScreen`. Ahora vale la pena volver a ella, porque es el ejemplo más corto de estado que existe.

Empieza por usarlo. `_counter` vive en el bloque **Estado**, dentro de `_MyHomePageState`, y una línea la une con el widget que la usa: el `Text`. Pulsa `+` y sigue los cinco pasos. Con *Paso a paso* avanzas tú, uno a la vez.

```interactive
state-tree forget
```

Cambia a **Código** cuando quieras: el estado se conserva. Ahí se ilumina la línea que corre en cada paso, y la única línea que amarra `_counter` a un widget es `body: Text('$_counter')`, marcada en violeta y unida al bloque Estado.

## El contador, sin lo que sobra

Este es el State del contador, con los comentarios del ejemplo original quitados y un `print` agregado en `build`:

```dart
class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    print('build() con _counter = $_counter');
    return Scaffold(
      body: Text('$_counter'),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
      ),
    );
  }
}
```

- `_counter` es el estado: un campo del State.
- `_incrementCounter` es la función que lo cambia.
- `build` lee `_counter` y lo pone en un `Text`.

Cuando lo corras en tu proyecto, cada toque escribe una línea nueva en la consola de depuración: `build()` corrió otra vez. Ese `print` es la forma más directa de ver **cuándo** se vuelve a construir una pantalla. Ponlo en tus propias Screens mientras aprendes, y quítalo después.

## Qué hace setState

`setState` no dibuja nada. Hace dos cosas: ejecuta la función que le pasas, que es donde cambias el dato, y **le avisa a Flutter** que este State cambió. Flutter responde volviendo a llamar a `build()`, y `build()` lee el valor nuevo.

```svg
<svg id="ssCiclo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 372" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ssCiclo-ttl ssCiclo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ssCiclo-ttl">Lo que pasa cuando se pulsa +</title>
  <desc id="ssCiclo-dsc">Cuatro pasos en fila. Uno: el toque llama a _incrementCounter. Dos: setState suma uno a _counter y marca el State como sucio. Tres: Flutter vuelve a llamar build. Cuatro: el Text muestra el valor nuevo. Una flecha vuelve al inicio. Debajo del paso dos, un aviso: sin setState el dato cambia pero build no corre y la pantalla no cambia.</desc>
  <defs>
    <style>
      #ssCiclo .title{fill:#161A26;font-size:22px;font-weight:700}
      #ssCiclo .sub{fill:#79809A;font-size:13.5px}
      #ssCiclo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ssCiclo .nt{font-size:15px;font-weight:700;fill:#161A26}
      #ssCiclo .nb{fill:#454C61;font-size:13px}
      #ssCiclo .lbl{fill:#556074;font-size:12px;font-weight:600}
      #ssCiclo .foot{fill:#79809A;font-size:12px}
      #ssCiclo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ssCiclo .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#ssCiclo-arrow)}
    </style>
    <marker id="ssCiclo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="372" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Lo que pasa cuando se pulsa <tspan class="mono">+</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">setState no dibuja nada: cambia el dato y le avisa a Flutter que el State quedó sucio.</text>
  <rect x="48" y="120" width="196" height="140" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <circle cx="74" cy="148" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="74" y="152.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">1</text>
  <text x="96" y="153" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="136">El toque</text>
  <text x="66" y="186" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="164">onPressed llama a</text>
  <text x="66" y="211" font-size="13" font-weight="600" fill="#A96C05" text-anchor="start" class="mono" data-fit="164">_incrementCounter()</text>
  <path class="link" d="M246,190 H266"/>
  <rect x="268" y="120" width="196" height="140" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <circle cx="294" cy="148" r="13" fill="#FFFFFF" stroke="#7439B8" stroke-width="2"/><text x="294" y="152.5" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle">2</text>
  <text x="316" y="153" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="136">setState</text>
  <text x="286" y="186" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="164">Cambia el dato y marca</text><text x="286" y="205" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="164">el State como sucio.</text>
  <text x="286" y="230" font-size="13" font-weight="600" fill="#7439B8" text-anchor="start" class="mono" data-fit="164">_counter++</text>
  <path class="link" d="M466,190 H486"/>
  <rect x="488" y="120" width="196" height="140" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <circle cx="514" cy="148" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="514" y="152.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle">3</text>
  <text x="536" y="153" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="136">build()</text>
  <text x="506" y="186" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="164">Flutter lo vuelve a</text><text x="506" y="205" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="164">llamar en el siguiente</text><text x="506" y="224" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="164">cuadro de la pantalla.</text>
  <path class="link" d="M686,190 H706"/>
  <rect x="708" y="120" width="196" height="140" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
  <circle cx="734" cy="148" r="13" fill="#FFFFFF" stroke="#3A8235" stroke-width="2"/><text x="734" y="152.5" font-size="13" font-weight="700" fill="#3A8235" text-anchor="middle">4</text>
  <text x="756" y="153" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="136">La pantalla</text>
  <text x="726" y="186" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="164">Text muestra el</text><text x="726" y="205" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="164">valor nuevo.</text>
  <text x="726" y="230" font-size="13" font-weight="600" fill="#3A8235" text-anchor="start" class="mono" data-fit="164">Text('$_counter')</text>
  <path class="link" d="M806,262 V288 H146 V264"/>
  <text x="476" y="282" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">el siguiente toque empieza otra vuelta</text>
  <rect x="48" y="304" width="864" height="44" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/>
  <text x="68" y="331" font-size="13" font-weight="600" fill="#C2354F" text-anchor="start" data-fit="824">Sin setState el paso 2 solo cambia el dato: build() no corre y la pantalla se queda con el valor viejo.</text>
</svg>
```

Vuelve al diagrama del inicio y fíjate en el paso 2: `_counter` ya vale el número nuevo, pero la pantalla sigue mostrando el viejo. El estado cambia primero, y la pantalla solo se entera cuando `build()` vuelve a correr y el `Text` nuevo lee el valor, en los pasos 3 a 5. También mira los `#n`: en cada `build()` el `Scaffold`, el `Text` y el botón son objetos nuevos, y `_MyHomePageState` es siempre el mismo.

Por eso `build()` tiene que poder correr muchas veces: no crea el estado, solo lo lee. Si en `build()` escribieras `int counter = 0;`, el contador volvería a 0 en cada reconstrucción.

## El error más común: olvidar setState

Vuelve al diagrama del inicio y activa *Olvidar setState*. El código cambia: ahora `_incrementCounter` solo hace `_counter++`. Pulsa `+` varias veces.

El bloque Estado sube, pero la pantalla se queda quieta y la etiqueta dice *Flutter no se enteró*: el dato cambió y nadie le avisó a Flutter. Desactiva el interruptor y pulsa `+` una vez más: la pantalla salta de golpe al valor real, con todos los toques que se habían perdido. No sale ningún error, la app simplemente "no hace nada", y eso lo hace difícil de encontrar. Cuando una pantalla no refleja un cambio, lo primero que se revisa es si el cambio está dentro de un `setState`.

## Ejemplo completo

El contador con el estilo del curso: `App` con su tabla de rutas, una `CounterScreen` y el `print` en `build`. En DartPad, la salida del `print` sale en la consola debajo de la app.

```dart trycode=385eb89f0f317f17fc9343f527407a71
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
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => const CounterScreen(),
      },
    );
  }
}

/// Counter screen: the flutter create example.
class CounterScreen extends StatefulWidget {
  const CounterScreen({super.key});

  @override
  State<CounterScreen> createState() => _CounterScreenState();
}

class _CounterScreenState extends State<CounterScreen> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    print('build() con _counter = $_counter');
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Contador'),
      ),
      body: SafeArea(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Text('Has pulsado el botón estas veces:'),
              Text(
                '$_counter',
                style: Theme.of(context).textTheme.headlineMedium,
              ),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => _incrementCounter(),
        child: const Icon(Icons.add),
      ),
    );
  }
}
```
