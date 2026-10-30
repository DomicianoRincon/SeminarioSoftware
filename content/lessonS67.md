# El índice en el estado

<!-- tags: _currentIndex, setState en onTap, cambiar de pestaña, Screen y Page, lib/pages, switch case, if else, la barra no cambia al tocar, Page sin Scaffold, cambiar de tab es setState y abrir un detalle es push -->

La barra ya avisa qué botón se tocó, pero la pantalla no hace nada con ese número. Para que responda hace falta lo de siempre: guardar el número en el estado y cambiarlo con `setState`. Con ese mismo número, el `body` elige cuál de tres Pages mostrar.

## Un número en el estado

Todo lo que cambia en la pantalla vive en el `State`. Aquí lo que cambia es la pestaña abierta, y una pestaña se identifica con un número: el mismo que usa `currentIndex`. Así que `HomeScreen` pasa a ser un `StatefulWidget` con un campo:

```dart
int _currentIndex = 0;
```

La barra lee ese campo y lo cambia al tocarla:

```dart
bottomNavigationBar: BottomNavigationBar(
  currentIndex: _currentIndex,
  onTap: (index) => setState(() => _currentIndex = index),
  items: const [
    BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Inicio'),
    BottomNavigationBarItem(icon: Icon(Icons.chat), label: 'Chats'),
    BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Perfil'),
  ],
),
```

`onTap` recibe el número del botón tocado y lo guarda. Como lo guarda dentro de `setState`, Flutter vuelve a correr `build()`, y esta vez `currentIndex` vale el número nuevo: el resaltado se mueve.

Si tocas un botón y el resaltado no se mueve, revisa dos cosas: que `currentIndex` diga `_currentIndex` y no un número escrito a mano, y que el cambio esté dentro de `setState`. Sin `setState` el número cambia, pero nadie vuelve a dibujar la pantalla.

## Tres Pages

El `body` es lo que cambia con cada pestaña. Cada contenido es una **Page**: un widget **sin `Scaffold`**, porque el `Scaffold` ya lo pone la Screen que la hospeda. Las Pages van en `lib/pages/` y se llaman `XxxPage`.

```dart
/// Section with the latest news.
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return const Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.home, size: 64, color: Colors.deepPurple),
          SizedBox(height: 12),
          Text('Inicio', style: TextStyle(fontSize: 24)),
        ],
      ),
    );
  }
}
```

`ChatsPage` y `ProfilePage` son iguales, con su icono y su texto. Si una Page empezara con `Scaffold`, verías dos barras de arriba y dos fondos: un `Scaffold` dentro de otro.

## Elegir la Page con if y else

Falta decidir qué Page va en el `body` según el número. Lo más directo es un método que pregunta con `if`:

```dart
Widget _buildPage() {
  if (_currentIndex == 0) {
    return const HomePage();
  } else if (_currentIndex == 1) {
    return const ChatsPage();
  } else {
    return const ProfilePage();
  }
}
```

Y el `body` lo llama:

```dart
body: SafeArea(child: _buildPage()),
```

El último caso es un `else` y no un `else if (_currentIndex == 2)`. Así el método siempre devuelve una Page, y Dart no se queja de que podría terminar sin devolver nada.

## Lo mismo con switch

Cuando se compara una misma variable contra varios valores, `switch` lo dice más claro: se nombra la variable una vez y cada caso queda en su línea.

```svg
<svg id="biSwitch" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 600" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="biSwitch-ttl biSwitch-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="biSwitch-ttl">Un número elige la Page</title>
  <desc id="biSwitch-dsc">El método _buildPage con un switch sobre _currentIndex: case 0 devuelve HomePage, case 1 devuelve ChatsPage y default devuelve ProfilePage. A la derecha, una tarjeta dice que _currentIndex vale 1, y debajo las tres Pages; ChatsPage está resaltada porque es la que se ve. Debajo, dos tarjetas: con if y else se elige igual, y default atrapa cualquier otro número.</desc>
  <defs>
    <style>
      #biSwitch .title{fill:#161A26;font-size:22px;font-weight:700}
      #biSwitch .sub{fill:#79809A;font-size:13.5px}
      #biSwitch .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #biSwitch .cl{font-size:13px;fill:#C9CFDA}
      #biSwitch .s{fill:#A8D8A0} #biSwitch .n{fill:#F2B880} #biSwitch .c{fill:#7FD1E8}
      #biSwitch .p{fill:#D5B8F5} #biSwitch .k{fill:#F08FB0}
      #biSwitch .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #biSwitch .ct{fill:#161A26;font-size:14px;font-weight:700}
      #biSwitch .cb{fill:#454C61;font-size:13px}
      #biSwitch .rt{fill:#161A26;font-size:14px} #biSwitch .rs{fill:#79809A;font-size:12px}
      #biSwitch .foot{fill:#79809A;font-size:12px}
      #biSwitch .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #biSwitch .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #biSwitch .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#biSwitch-ar-amber)}
      #biSwitch .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #biSwitch .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #biSwitch .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#biSwitch-ar-indigo)}
      #biSwitch .hl-teal{fill:#86D3CA;fill-opacity:.16;stroke:#86D3CA;stroke-width:1.5}
      #biSwitch .ld-teal{fill:none;stroke:#86D3CA;stroke-width:1.5;stroke-dasharray:3 4}
      #biSwitch .ar-teal{fill:none;stroke:#0F8478;stroke-width:1.75;marker-end:url(#biSwitch-ar-teal)}
      #biSwitch .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #biSwitch .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #biSwitch .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#biSwitch-ar-violet)}
    </style>
    <marker id="biSwitch-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="biSwitch-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="biSwitch-ar-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#0F8478"/></marker>
    <marker id="biSwitch-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="600" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Un número elige la <tspan class="mono">Page</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">build() llama a _buildPage(), y el switch devuelve la Page que corresponde al número.</text>
  <rect x="48" y="112" width="456" height="330" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/home_screen.dart</text>
  <rect x="552" y="112" width="360" height="330" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">QUÉ DEVUELVE CADA CASO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="142.0" y="180" width="109.4" height="22" rx="5"/>
  <rect class="hl-violet" x="212.2" y="228" width="86.0" height="22" rx="5"/>
  <rect class="hl-teal" x="212.2" y="276" width="93.8" height="22" rx="5"/>
  <rect class="hl-indigo" x="212.2" y="324" width="109.4" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="163.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Widget</tspan> _buildPage() {</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="187.2" lengthAdjust="spacingAndGlyphs" data-fit="432">switch (_currentIndex) {</text>
  <text class="cl mono" font-size="13" x="99.2" y="220" textLength="54.6" lengthAdjust="spacingAndGlyphs" data-fit="432">case <tspan class="n">0</tspan>:</text>
  <text class="cl mono" font-size="13" x="114.8" y="244" textLength="187.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="k">const</tspan> <tspan class="c">HomePage</tspan>();</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="54.6" lengthAdjust="spacingAndGlyphs" data-fit="432">case <tspan class="n">1</tspan>:</text>
  <text class="cl mono" font-size="13" x="114.8" y="292" textLength="195.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="k">const</tspan> <tspan class="c">ChatsPage</tspan>();</text>
  <text class="cl mono" font-size="13" x="99.2" y="316" textLength="62.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">default</tspan>:</text>
  <text class="cl mono" font-size="13" x="114.8" y="340" textLength="210.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="k">const</tspan> <tspan class="c">ProfilePage</tspan>();</text>
  <text class="cl mono" font-size="13" x="83.6" y="364" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="388" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <g transform="translate(552,144)">
<rect x="16" y="16" width="328" height="56" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="30" y="40" font-size="13.5" font-weight="700" fill="#A96C05" text-anchor="start" class="mono">_currentIndex vale 1</text><text x="30" y="59" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start">Lo puso el onTap al tocar Chats.</text><rect x="16" y="96" width="328" height="56" rx="12" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><circle cx="44" cy="124" r="16" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><path transform="translate(44,124) scale(0.9)" d="M-8,1 L0,-7 L8,1 M-6,-0.5 V7 H6 V-0.5" fill="none" stroke="#7439B8" stroke-width="2.22" stroke-linecap="round" stroke-linejoin="round"/><text x="72" y="120" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">HomePage()</text><text x="72" y="139" font-size="12" font-weight="400" fill="#556074" text-anchor="start" class="mono">case 0</text><rect x="16" y="164" width="328" height="56" rx="12" fill="#E3F6F3" stroke="#0F8478" stroke-width="2"/><circle cx="44" cy="192" r="16" fill="#FFFFFF" stroke="#86D3CA" stroke-width="1.5"/><path transform="translate(44,192) scale(0.9)" d="M-7,-7 h14 a2,2 0 0 1 2,2 v7 a2,2 0 0 1 -2,2 h-8 l-4,3 v-3 h-2 a2,2 0 0 1 -2,-2 v-7 a2,2 0 0 1 2,-2 Z" fill="none" stroke="#0F8478" stroke-width="2.22" stroke-linecap="round" stroke-linejoin="round"/><text x="72" y="188" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">ChatsPage()</text><text x="72" y="207" font-size="12" font-weight="400" fill="#556074" text-anchor="start" class="mono">case 1</text><rect x="262" y="181" width="70" height="22" rx="11" fill="#FFFFFF" stroke="#0F8478"/><text x="297" y="196" font-size="12" font-weight="700" fill="#0F8478" text-anchor="middle">se ve</text><rect x="16" y="232" width="328" height="56" rx="12" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="44" cy="260" r="16" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.5"/><path transform="translate(44,260) scale(0.9)" d="M-3.5,-4 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M-7,7 a7,6 0 0 1 14,0" fill="none" stroke="#4453C9" stroke-width="2.22" stroke-linecap="round" stroke-linejoin="round"/><text x="72" y="256" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">ProfilePage()</text><text x="72" y="275" font-size="12" font-weight="400" fill="#556074" text-anchor="start" class="mono">default</text>
  </g>
  <path class="ld-amber" d="M276.8,191 H504"/>
  <path class="ar-amber" d="M504,191 H541 V188 H568"/>
  <path class="ld-violet" d="M308.0,239 H504"/>
  <path class="ar-violet" d="M504,239 H532 V268 H568"/>
  <path class="ld-teal" d="M315.8,287 H504"/>
  <path class="ar-teal" d="M504,287 H523 V336 H568"/>
  <path class="ld-indigo" d="M331.4,335 H504"/>
  <path class="ar-indigo" d="M504,335 H514 V404 H568"/>
  <g transform="translate(48.0,466)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#FFF3DC" stroke="#A96C05" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="366">if / else if / else</text>
    <text class="cb" x="16" y="60" data-fit="392">La misma elección, con if. El switch</text>
    <text class="cb" x="16" y="79" data-fit="392">se lee mejor cuando hay tres o más.</text>
  </g>
  <g transform="translate(488.0,466)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#E8F6E3" stroke="#3A8235" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="366">default</text>
    <text class="cb" x="16" y="60" data-fit="392">Atrapa cualquier otro número: el</text>
    <text class="cb" x="16" y="79" data-fit="392">método siempre devuelve una Page.</text>
  </g>
</svg>
```

```dart
Widget _buildPage() {
  switch (_currentIndex) {
    case 0:
      return const HomePage();
    case 1:
      return const ChatsPage();
    default:
      return const ProfilePage();
  }
}
```

`default` cumple el papel del último `else`: atrapa cualquier número que no tenga su `case`. Las dos versiones hacen exactamente lo mismo; usa la que te resulte más fácil de leer. Si mañana agregas una cuarta pestaña, en las dos se agrega un caso.

## El ciclo completo

Ahora junta todo. Toca **Chats** o **Perfil** en el simulador y sigue los pasos: primero cambia `_currentIndex` en el estado, después `build()` corre otra vez, el `switch` lee el número y devuelve otra Page, y solo al final cambia la pantalla. En *Código* ves qué línea corre en cada paso.

```interactive
state-tree tabs forget
```

Marca *Olvidar setState* y toca otra pestaña: el número cambia en el estado, pero la barra y el `body` se quedan como estaban. Es el error de la barra que no responde.

## Pestaña o pantalla nueva

Ahora tienes dos formas de cambiar lo que se ve, y no son intercambiables:

- **Cambiar de pestaña es `setState`.** La Screen es la misma, el `Scaffold` es el mismo y solo cambia la Page del `body`. No hay nada en la pila del `Navigator`: el botón atrás del sistema no vuelve a la pestaña anterior, y la barra de arriba no muestra la flecha.
- **Abrir un detalle es `push`.** Una Screen nueva, con su propio `Scaffold`, entra encima de la pila. La barra de abajo desaparece porque es de la Screen de abajo, y atrás vuelve a ella.

Por eso una Page nunca llama al `Navigator`. Si una Page quiere abrir algo, avisa con una función, como `SongCard` en la sesión 7, y es la Screen la que hace el `pushNamed`.

## Ejemplo completo

Una Screen con tres Pages que cambian con la barra. Toca los botones: el resaltado se mueve y el contenido cambia.

```dart trycode=64958c1df962ff69e3815cf8805ae892 tab=run
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
      initialRoute: '/',
      routes: {'/': (context) => const HomeScreen()},
    );
  }
}

/// Section with the latest news.
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return const Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.home, size: 64, color: Colors.deepPurple),
          SizedBox(height: 12),
          Text('Inicio', style: TextStyle(fontSize: 24)),
        ],
      ),
    );
  }
}

/// Section with the conversations.
class ChatsPage extends StatelessWidget {
  const ChatsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return const Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.chat, size: 64, color: Colors.teal),
          SizedBox(height: 12),
          Text('Chats', style: TextStyle(fontSize: 24)),
        ],
      ),
    );
  }
}

/// Section with the user's profile.
class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {
    return const Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.person, size: 64, color: Colors.orange),
          SizedBox(height: 12),
          Text('Perfil', style: TextStyle(fontSize: 24)),
        ],
      ),
    );
  }
}

/// Screen that hosts three pages and switches them with the bar.
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _currentIndex = 0;

  Widget _buildPage() {
    switch (_currentIndex) {
      case 0:
        return const HomePage();
      case 1:
        return const ChatsPage();
      default:
        return const ProfilePage();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Mi app')),
      body: SafeArea(child: _buildPage()),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) => setState(() => _currentIndex = index),
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Inicio',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.chat),
            label: 'Chats',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: 'Perfil',
          ),
        ],
      ),
    );
  }
}
```

En tu proyecto, `HomeScreen` va en `lib/screens/` y cada Page en su archivo de `lib/pages/`.
