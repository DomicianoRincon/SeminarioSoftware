# IndexedStack: Pages que recuerdan

<!-- tags: IndexedStack, la pestaña pierde lo que escribí, la Page se destruye al cambiar de tab, dispose al cambiar de pestaña, initState otra vez, conservar el estado de una pestaña, children e index, scroll que vuelve arriba, AutomaticKeepAliveClientMixin, PageStorageKey -->

Con el `switch` de la lección anterior, cada pestaña muestra su Page. Pero hay algo que todavía no has notado: cuando sales de una pestaña, su Page deja de existir. Si tenía algo guardado en su `State`, se pierde. En esta lección se ve por qué pasa y cómo evitarlo con `IndexedStack`.

## Una Page con borrador

Para verlo hace falta una Page con estado propio. `ChatsPage` tiene ahora un campo para escribir un mensaje; el texto vive en su `TextEditingController`, y el controller vive en el `State` de la Page. Es estado que solo ella usa, así que es suyo.

```dart
/// Section with the conversations and a message draft.
class ChatsPage extends StatefulWidget {
  const ChatsPage({super.key});

  @override
  State<ChatsPage> createState() => _ChatsPageState();
}

class _ChatsPageState extends State<ChatsPage> {
  final _messageController = TextEditingController();

  @override
  void initState() {
    super.initState();
    debugPrint('ChatsPage: initState');
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(24),
      child: Column(
        children: [
          const Icon(Icons.chat, size: 64, color: Colors.teal),
          const SizedBox(height: 12),
          TextField(
            controller: _messageController,
            decoration: const InputDecoration(labelText: 'Mensaje'),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    debugPrint('ChatsPage: dispose');
    _messageController.dispose();
    super.dispose();
  }
}
```

Los dos `debugPrint` están para mirar la consola mientras cambias de pestaña.

## El borrador se pierde

Ve a *Chats*, escribe *Hola*, cambia a *Perfil* y vuelve a *Chats*. El campo está vacío. La consola cuenta lo que pasó:

```text
ChatsPage: initState
ChatsPage: dispose
ChatsPage: initState
```

Al ir a *Perfil*, el `switch` devolvió `ProfilePage`. `ChatsPage` ya no estaba en lo que devolvió `build()`, así que Flutter la sacó del árbol y su `State` corrió `dispose()`, igual que una pantalla que se cierra con `pop`. Al volver, el `switch` devolvió una `ChatsPage` nueva, con un `State` nuevo y un controller vacío.

Pruébalo aquí. Escribe en *Chats*, cambia de pestaña y mira qué hay en el `body` en cada paso:

```interactive
tab-state
```

No es un error del `switch`: así funciona Flutter. Lo que no está en el árbol no existe. Lo mismo le pasa al scroll de una lista larga: al volver a la pestaña, empieza otra vez desde arriba.

## IndexedStack

`IndexedStack` es un widget que recibe **todos** los hijos a la vez y un `index` que dice cuál se pinta. Los demás siguen en el árbol, ocultos y vivos: no corren `dispose()` y conservan su `State`.

```dart
body: SafeArea(
  child: IndexedStack(
    index: _currentIndex,
    children: const [HomePage(), ChatsPage(), ProfilePage()],
  ),
),
```

Reemplaza al `switch` completo: ya no hace falta `_buildPage()`. `index` hace el papel del número del `switch`, y el orden de `children` es el mismo de los botones de la barra.

```svg
<svg id="isPila" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="isPila-ttl isPila-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="isPila-ttl">Lo que hay en el body, pestaña por pestaña</title>
  <desc id="isPila-dsc">Dos columnas con la pestaña Chats abierta. La primera, con el switch: solo existe ChatsPage, visible; HomePage y ProfilePage aparecen punteadas y tachadas porque no existen. La segunda, con IndexedStack: los tres hijos existen; ChatsPage, el número 1, es la visible, y HomePage y ProfilePage están ocultas pero vivas. Debajo, tres tarjetas: al cambiar de pestaña con el switch la Page sale y pierde su State; IndexedStack las conserva; y el costo es que las tres viven en memoria desde el arranque.</desc>
  <defs>
    <style>
      #isPila .title{fill:#161A26;font-size:22px;font-weight:700}
      #isPila .sub{fill:#79809A;font-size:13.5px}
      #isPila .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #isPila .nt{font-size:15px;font-weight:700;fill:#161A26}
      #isPila .nb{fill:#454C61;font-size:13px}
      #isPila .lbl{fill:#556074;font-size:12px;font-weight:600}
      #isPila .foot{fill:#79809A;font-size:12px}
      #isPila .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #isPila .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#isPila-arrow)}
    </style>
    <marker id="isPila-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="isPila-push" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="isPila-pop" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="isPila-tab" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
  </defs>
  <rect width="960" height="520" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Lo que hay en el body, pestaña por pestaña</text>
  <text class="sub" x="48" y="80" data-fit="860">Con el switch solo existe la Page que se ve. Con IndexedStack existen las tres y solo se pinta una.</text>
  <text x="48" y="128" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="392">switch (_currentIndex)</text>
  <text x="48" y="148" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="392">Solo existe la que se ve</text>
  <text x="520" y="128" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="392">IndexedStack(index: 1)</text>
  <text x="520" y="148" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="392">Existen las tres, se pinta una</text>
  <rect x="48" y="172" width="392" height="56" rx="10" fill="#FBFBFD" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 5"/><text x="64" y="195" font-size="12.5" font-weight="700" fill="#79809A" text-anchor="start" class="mono">case 0</text><text x="64" y="215" font-size="13" font-weight="400" fill="#79809A" text-anchor="start" class="mono">HomePage()</text><path d="M62,211 H144.0" stroke="#79809A" stroke-width="1.5"/><rect x="346.8" y="189" width="81.2" height="22" rx="11" fill="#EFF1F5"/><text x="387.4" y="204" font-size="11.5" font-weight="600" fill="#556074" text-anchor="middle">no existe</text>
  <rect x="520" y="172" width="392" height="56" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="536" y="195" font-size="12.5" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">children[0]</text><text x="536" y="215" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" class="mono">HomePage()</text><rect x="750.8" y="189" width="149.2" height="22" rx="11" fill="#EEF1FF"/><text x="825.4" y="204" font-size="11.5" font-weight="600" fill="#4453C9" text-anchor="middle">oculta · sigue viva</text>
  <rect x="48" y="240" width="392" height="56" rx="10" fill="#FFFFFF" stroke="#6750A4" stroke-width="1.5"/><text x="64" y="263" font-size="12.5" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">case 1</text><text x="64" y="283" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" class="mono">ChatsPage()</text><rect x="244.8" y="257" width="183.2" height="22" rx="11" fill="#E8F6E3"/><text x="336.4" y="272" font-size="11.5" font-weight="600" fill="#3A8235" text-anchor="middle">visible · borrador: Hola</text>
  <rect x="520" y="240" width="392" height="56" rx="10" fill="#FFFFFF" stroke="#6750A4" stroke-width="1.5"/><text x="536" y="263" font-size="12.5" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">children[1]</text><text x="536" y="283" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" class="mono">ChatsPage()</text><rect x="716.8" y="257" width="183.2" height="22" rx="11" fill="#E8F6E3"/><text x="808.4" y="272" font-size="11.5" font-weight="600" fill="#3A8235" text-anchor="middle">visible · borrador: Hola</text>
  <rect x="48" y="308" width="392" height="56" rx="10" fill="#FBFBFD" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 5"/><text x="64" y="331" font-size="12.5" font-weight="700" fill="#79809A" text-anchor="start" class="mono">default</text><text x="64" y="351" font-size="13" font-weight="400" fill="#79809A" text-anchor="start" class="mono">ProfilePage()</text><path d="M62,347 H167.39999999999998" stroke="#79809A" stroke-width="1.5"/><rect x="346.8" y="325" width="81.2" height="22" rx="11" fill="#EFF1F5"/><text x="387.4" y="340" font-size="11.5" font-weight="600" fill="#556074" text-anchor="middle">no existe</text>
  <rect x="520" y="308" width="392" height="56" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="536" y="331" font-size="12.5" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">children[2]</text><text x="536" y="351" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" class="mono">ProfilePage()</text><rect x="750.8" y="325" width="149.2" height="22" rx="11" fill="#EEF1FF"/><text x="825.4" y="340" font-size="11.5" font-weight="600" fill="#4453C9" text-anchor="middle">oculta · sigue viva</text>
  <path d="M480,120 V376" stroke="#D9DEE8" stroke-width="1.5" stroke-dasharray="4 5"/>
  <rect x="48" y="400" width="272" height="88" rx="12" fill="#FFFFFF" stroke="#F3A3B2" stroke-width="1.5"/><text x="64" y="431" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="244">Con switch, se pierde</text><text x="64" y="458" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Al cambiar de pestaña sale del árbol:</text><text x="64" y="477" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">dispose(). Al volver, State nuevo.</text>
  <rect x="344" y="400" width="272" height="88" rx="12" fill="#FFFFFF" stroke="#9FD68D" stroke-width="1.5"/><text x="360" y="431" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="244">Con IndexedStack, se queda</text><text x="360" y="458" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">index solo decide cuál se pinta.</text><text x="360" y="477" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">El borrador sigue ahí al volver.</text>
  <rect x="640" y="400" width="272" height="88" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><text x="656" y="431" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="244">El costo</text><text x="656" y="458" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Las tres viven en memoria y corren</text><text x="656" y="477" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">su initState() al arrancar la app.</text>
</svg>
```

Repite la prueba. Escribe *Hola*, cambia a *Perfil* y vuelve: el mensaje sigue ahí. La consola muestra un solo `initState` y ningún `dispose`:

```text
ChatsPage: initState
```

El mismo experimento, ahora con `IndexedStack`:

```interactive
tab-state indexed
```

## Cuándo usarlo

`IndexedStack` no es gratis. Las tres Pages se construyen cuando arranca la Screen, aunque nunca abras dos de ellas: fíjate en que `ChatsPage: initState` aparece apenas abre la app, sin haber tocado *Chats*. Y las tres viven en memoria todo el tiempo. Con tres Pages sencillas no se nota; con Pages que cargan datos al abrirse, puede ser mucho trabajo de entrada.

La pregunta es qué se pierde si la Page vuelve a empezar:

- **Un borrador, el scroll, lo que la persona estaba haciendo ahí.** Eso es de la Page y conviene conservarlo: usa `IndexedStack`.
- **Datos que comparten varias pestañas**, como la lista de canciones de la playlist. Esos no deberían vivir en una Page: viven en la Screen anfitriona y les llegan a las Pages por constructor. Así sobreviven aunque la Page se destruya, con o sin `IndexedStack`.

## Otros que recuerdan

`IndexedStack` es la forma más simple, pero no la única. Para que los reconozcas si los ves en otro proyecto:

- **`AutomaticKeepAliveClientMixin`** se usa con `PageView` o `TabBarView`, donde las pestañas se deslizan con el dedo. La Page le pide a Flutter que no la destruya aunque salga de la pantalla.
- **`PageStorageKey`** guarda solo la posición del scroll de una lista, para que vuelva donde estaba aunque la Page se haya reconstruido.

En este curso basta con `IndexedStack`.

## Ejemplo completo

La Screen con `IndexedStack` y `ChatsPage` con su borrador. Escribe un mensaje, cambia de pestaña y vuelve. Después cambia el `IndexedStack` por el `switch` de la lección anterior y repite.

```dart trycode=PENDIENTE_S68 tab=run
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

/// Section with the conversations and a message draft.
class ChatsPage extends StatefulWidget {
  const ChatsPage({super.key});

  @override
  State<ChatsPage> createState() => _ChatsPageState();
}

class _ChatsPageState extends State<ChatsPage> {
  final _messageController = TextEditingController();

  @override
  void initState() {
    super.initState();
    debugPrint('ChatsPage: initState');
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(24),
      child: Column(
        children: [
          const Icon(Icons.chat, size: 64, color: Colors.teal),
          const SizedBox(height: 12),
          TextField(
            controller: _messageController,
            decoration: const InputDecoration(labelText: 'Mensaje'),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    debugPrint('ChatsPage: dispose');
    _messageController.dispose();
    super.dispose();
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

/// Screen that hosts three pages and keeps them alive.
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _currentIndex = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Mi app')),
      body: SafeArea(
        child: IndexedStack(
          index: _currentIndex,
          children: const [HomePage(), ChatsPage(), ProfilePage()],
        ),
      ),
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
