# AppBar

<!-- tags: AppBar, barra de arriba, title del AppBar, actions, leading, centerTitle, título centrado, backgroundColor y foregroundColor, color del AppBar, el título no se ve sobre la barra, botones en la barra, flecha de volver -->

Tu `ProfileScreen` ya tiene una barra con título. El widget que la dibuja es `AppBar`, y tiene más lugares que ese.

## Las partes de un AppBar

```svg
<svg id="abPartes" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 412" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="abPartes-ttl abPartes-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="abPartes-ttl">Las partes de un AppBar</title>
  <desc id="abPartes-dsc">La parte de arriba de un celular con una barra. A la izquierda, un botón de menú: es leading. Después, el título Perfil: es title. A la derecha, dos botones, buscar y ajustes: son actions.</desc>
  <defs>
    <style>
      #abPartes .title{fill:#161A26;font-size:22px;font-weight:700}
      #abPartes .sub{fill:#79809A;font-size:13.5px}
      #abPartes .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #abPartes .nt{font-size:15px;font-weight:700;fill:#161A26}
      #abPartes .nb{fill:#454C61;font-size:13px}
      #abPartes .lbl{fill:#556074;font-size:12px;font-weight:600}
      #abPartes .foot{fill:#79809A;font-size:12px}
      #abPartes .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #abPartes .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#abPartes-arrow)}
    </style>
    <marker id="abPartes-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="412" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las partes de un <tspan class="mono">AppBar</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Tres lugares, de izquierda a derecha. Solo title es de uso diario; los otros dos son opcionales.</text>
  <clipPath id="abPartes-ac"><rect x="250" y="218" width="460" height="160"/></clipPath><linearGradient id="abPartes-af" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBFBFD" stop-opacity="0"/><stop offset="1" stop-color="#FBFBFD"/></linearGradient><g clip-path="url(#abPartes-ac)"><clipPath id="abPartes-as"><rect width="440" height="230" rx="20"/></clipPath><rect x="253" y="221" width="454" height="244" rx="27" fill="#1F2430"/><g transform="translate(260,228)"><g clip-path="url(#abPartes-as)"><rect width="440" height="230" rx="20" fill="#FFFFFF"/><rect width="440" height="72" fill="#F1ECF8"/><path transform="translate(36,36.0) scale(1)" d="M-9,-6 H9 M-9,0 H9 M-9,6 H9" fill="none" stroke="#161A26" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><text dy="0.35em" x="76" y="36.0" font-size="22" font-weight="500" fill="#161A26" text-anchor="start">Perfil</text><path transform="translate(348,36.0) scale(1)" d="M-8,-2 a6,6 0 1 0 12,0 a6,6 0 1 0 -12,0 M2.5,2.5 L8,8" fill="none" stroke="#161A26" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><path transform="translate(404,36.0) scale(1)" d="M-3.5,0 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M0,-9 V-6.5 M0,6.5 V9 M-9,0 H-6.5 M6.5,0 H9 M-6.4,-6.4 L-4.6,-4.6 M4.6,4.6 L6.4,6.4 M-6.4,6.4 L-4.6,4.6 M4.6,-4.6 L6.4,-6.4" fill="none" stroke="#161A26" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/></g></g></g><rect x="250" y="334" width="460" height="46" fill="url(#abPartes-af)"/>
  <rect x="272" y="240" width="48" height="48" rx="12" fill="#4453C9" fill-opacity=".08" stroke="#4453C9" stroke-width="2"/>
  <path d="M180,184 V204 H296 V240" fill="none" stroke="#4453C9" stroke-width="1.75"/>
  <text x="180" y="132" font-size="15" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono">leading</text>
  <text x="180" y="154" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">Un widget a la izquierda.</text>
  <text x="180" y="172" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">Casi siempre un IconButton.</text>
  <rect x="326" y="240" width="84" height="48" rx="12" fill="#A96C05" fill-opacity=".08" stroke="#A96C05" stroke-width="2"/>
  <path d="M480,184 V204 H368 V240" fill="none" stroke="#A96C05" stroke-width="1.75"/>
  <text x="480" y="132" font-size="15" font-weight="700" fill="#A96C05" text-anchor="middle" class="mono">title</text>
  <text x="480" y="154" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">El nombre de la pantalla.</text>
  <text x="480" y="172" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">Casi siempre un Text.</text>
  <rect x="578" y="240" width="112" height="48" rx="12" fill="#3A8235" fill-opacity=".08" stroke="#3A8235" stroke-width="2"/>
  <path d="M770,184 V204 H634 V240" fill="none" stroke="#3A8235" stroke-width="1.75"/>
  <text x="770" y="132" font-size="15" font-weight="700" fill="#3A8235" text-anchor="middle" class="mono">actions</text>
  <text x="770" y="154" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">Una lista de widgets a la derecha.</text>
  <text x="770" y="172" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">Los botones de la pantalla.</text>
</svg>
```

```dart
appBar: AppBar(
  leading: IconButton(
    onPressed: () {
      print('Menú');
    },
    icon: const Icon(Icons.menu),
  ),
  title: const Text('Perfil'),
  actions: [
    IconButton(
      onPressed: () {
        print('Buscar');
      },
      icon: const Icon(Icons.search),
    ),
    IconButton(
      onPressed: () {
        print('Ajustes');
      },
      icon: const Icon(Icons.settings),
    ),
  ],
),
```

`title` es el nombre de la pantalla. Es el único que pones siempre.

`actions` es una lista: sus widgets se dibujan a la derecha, en el orden en que los escribes. Van los botones de esa pantalla, y conviene que sean pocos. Con más de tres, el título se queda sin espacio.

`leading` recibe un solo widget y lo pone a la izquierda. Casi nunca lo escribes: cuando llegas a una pantalla desde otra, Flutter pone ahí la flecha de volver por su cuenta. Eso es la sesión 8.

## Centrar y colorear

```svg
<svg id="abVariantes" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 372" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="abVariantes-ttl abVariantes-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="abVariantes-ttl">La misma barra, con tres ajustes</title>
  <desc id="abVariantes-dsc">Tres barras con el mismo título y los mismos botones. La primera, sin ajustes: el título queda a la izquierda. La segunda, con centerTitle en true: el título queda centrado. La tercera, con backgroundColor morado y foregroundColor blanco: fondo oscuro con el título y los iconos en blanco.</desc>
  <defs>
    <style>
      #abVariantes .title{fill:#161A26;font-size:22px;font-weight:700}
      #abVariantes .sub{fill:#79809A;font-size:13.5px}
      #abVariantes .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #abVariantes .nt{font-size:15px;font-weight:700;fill:#161A26}
      #abVariantes .nb{fill:#454C61;font-size:13px}
      #abVariantes .lbl{fill:#556074;font-size:12px;font-weight:600}
      #abVariantes .foot{fill:#79809A;font-size:12px}
      #abVariantes .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #abVariantes .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#abVariantes-arrow)}
    </style>
    <marker id="abVariantes-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="372" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La misma barra, con tres ajustes</text>
  <text class="sub" x="48" y="80" data-fit="860">El contenido no cambia. Cambian dónde queda el título y de qué color es la barra.</text>
  <clipPath id="abVariantes-ac"><rect x="54" y="122" width="276" height="130"/></clipPath><linearGradient id="abVariantes-af" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBFBFD" stop-opacity="0"/><stop offset="1" stop-color="#FBFBFD"/></linearGradient><g clip-path="url(#abVariantes-ac)"><clipPath id="abVariantes-as"><rect width="256" height="200" rx="20"/></clipPath><rect x="57" y="125" width="270" height="214" rx="27" fill="#1F2430"/><g transform="translate(64,132)"><g clip-path="url(#abVariantes-as)"><rect width="256" height="200" rx="20" fill="#FFFFFF"/><rect width="256" height="52" fill="#F1ECF8"/><path transform="translate(25.919999999999998,26.0) scale(0.72)" d="M-9,-6 H9 M-9,0 H9 M-9,6 H9" fill="none" stroke="#161A26" stroke-width="2.78" stroke-linecap="round" stroke-linejoin="round"/><text dy="0.35em" x="54.72" y="26.0" font-size="16" font-weight="500" fill="#161A26" text-anchor="start">Perfil</text><path transform="translate(189.76,26.0) scale(0.72)" d="M-8,-2 a6,6 0 1 0 12,0 a6,6 0 1 0 -12,0 M2.5,2.5 L8,8" fill="none" stroke="#161A26" stroke-width="2.78" stroke-linecap="round" stroke-linejoin="round"/><path transform="translate(230.08,26.0) scale(0.72)" d="M-3.5,0 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M0,-9 V-6.5 M0,6.5 V9 M-9,0 H-6.5 M6.5,0 H9 M-6.4,-6.4 L-4.6,-4.6 M4.6,4.6 L6.4,6.4 M-6.4,6.4 L-4.6,4.6 M4.6,-4.6 L6.4,-6.4" fill="none" stroke="#161A26" stroke-width="2.78" stroke-linecap="round" stroke-linejoin="round"/></g></g></g><rect x="54" y="208" width="276" height="46" fill="url(#abVariantes-af)"/>
  <text x="192.0" y="292" font-size="14" font-weight="700" fill="#161A26" text-anchor="middle" data-fit="272">Sin ajustes</text>
  <text x="192.0" y="314" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="272">El título queda a la izquierda.</text>
  <clipPath id="abVariantes-bc"><rect x="342" y="122" width="276" height="130"/></clipPath><linearGradient id="abVariantes-bf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBFBFD" stop-opacity="0"/><stop offset="1" stop-color="#FBFBFD"/></linearGradient><g clip-path="url(#abVariantes-bc)"><clipPath id="abVariantes-bs"><rect width="256" height="200" rx="20"/></clipPath><rect x="345" y="125" width="270" height="214" rx="27" fill="#1F2430"/><g transform="translate(352,132)"><g clip-path="url(#abVariantes-bs)"><rect width="256" height="200" rx="20" fill="#FFFFFF"/><rect width="256" height="52" fill="#F1ECF8"/><path transform="translate(25.919999999999998,26.0) scale(0.72)" d="M-9,-6 H9 M-9,0 H9 M-9,6 H9" fill="none" stroke="#161A26" stroke-width="2.78" stroke-linecap="round" stroke-linejoin="round"/><text dy="0.35em" x="128.0" y="26.0" font-size="16" font-weight="500" fill="#161A26" text-anchor="middle">Perfil</text><path transform="translate(189.76,26.0) scale(0.72)" d="M-8,-2 a6,6 0 1 0 12,0 a6,6 0 1 0 -12,0 M2.5,2.5 L8,8" fill="none" stroke="#161A26" stroke-width="2.78" stroke-linecap="round" stroke-linejoin="round"/><path transform="translate(230.08,26.0) scale(0.72)" d="M-3.5,0 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M0,-9 V-6.5 M0,6.5 V9 M-9,0 H-6.5 M6.5,0 H9 M-6.4,-6.4 L-4.6,-4.6 M4.6,4.6 L6.4,6.4 M-6.4,6.4 L-4.6,4.6 M4.6,-4.6 L6.4,-6.4" fill="none" stroke="#161A26" stroke-width="2.78" stroke-linecap="round" stroke-linejoin="round"/></g></g></g><rect x="342" y="208" width="276" height="46" fill="url(#abVariantes-bf)"/>
  <text x="480.0" y="292" font-size="14" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="272">centerTitle: true</text>
  <text x="480.0" y="314" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="272">El título queda en el centro.</text>
  <clipPath id="abVariantes-cc"><rect x="630" y="122" width="276" height="130"/></clipPath><linearGradient id="abVariantes-cf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBFBFD" stop-opacity="0"/><stop offset="1" stop-color="#FBFBFD"/></linearGradient><g clip-path="url(#abVariantes-cc)"><clipPath id="abVariantes-cs"><rect width="256" height="200" rx="20"/></clipPath><rect x="633" y="125" width="270" height="214" rx="27" fill="#1F2430"/><g transform="translate(640,132)"><g clip-path="url(#abVariantes-cs)"><rect width="256" height="200" rx="20" fill="#FFFFFF"/><rect width="256" height="52" fill="#673AB7"/><path transform="translate(25.919999999999998,26.0) scale(0.72)" d="M-9,-6 H9 M-9,0 H9 M-9,6 H9" fill="none" stroke="#FFFFFF" stroke-width="2.78" stroke-linecap="round" stroke-linejoin="round"/><text dy="0.35em" x="54.72" y="26.0" font-size="16" font-weight="500" fill="#FFFFFF" text-anchor="start">Perfil</text><path transform="translate(189.76,26.0) scale(0.72)" d="M-8,-2 a6,6 0 1 0 12,0 a6,6 0 1 0 -12,0 M2.5,2.5 L8,8" fill="none" stroke="#FFFFFF" stroke-width="2.78" stroke-linecap="round" stroke-linejoin="round"/><path transform="translate(230.08,26.0) scale(0.72)" d="M-3.5,0 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M0,-9 V-6.5 M0,6.5 V9 M-9,0 H-6.5 M6.5,0 H9 M-6.4,-6.4 L-4.6,-4.6 M4.6,4.6 L6.4,6.4 M-6.4,6.4 L-4.6,4.6 M4.6,-4.6 L6.4,-6.4" fill="none" stroke="#FFFFFF" stroke-width="2.78" stroke-linecap="round" stroke-linejoin="round"/></g></g></g><rect x="630" y="208" width="276" height="46" fill="url(#abVariantes-cf)"/>
  <text x="768.0" y="292" font-size="14" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="272">backgroundColor</text>
  <text x="768.0" y="314" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="272">Con foregroundColor: Colors.white.</text>
</svg>
```

```dart
appBar: AppBar(
  title: const Text('Perfil'),
  centerTitle: true,
  backgroundColor: Colors.deepPurple,
  foregroundColor: Colors.white,
),
```

`centerTitle: true` lleva el título al centro de la barra.

`backgroundColor` es el fondo de la barra. `foregroundColor` es el color de lo que va encima: el título y los iconos. Van en pareja. Si oscureces el fondo y no cambias `foregroundColor`, el título queda oscuro sobre oscuro y no se lee.

En `ProfileScreen`, centra el título y agrega en `actions` un `IconButton` con `Icons.more_vert`, los tres puntos. Así es la barra del diseño del taller.

## Ejemplo completo

Una barra con los tres lugares ocupados, el título centrado y color propio. Quita `foregroundColor` y mira qué pasa con el título.

```dart trycode=PENDIENTE_S28
import 'package:flutter/material.dart';

void main() {
  runApp(const App());
}

/// Root widget of the app.
class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mi app',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      initialRoute: '/profile',
      routes: {'/profile': (context) => const ProfileScreen()},
    );
  }
}

/// Profile of a person.
class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: () {
            print('Menú');
          },
          icon: const Icon(Icons.menu),
        ),
        title: const Text('Perfil'),
        centerTitle: true,
        backgroundColor: Colors.deepPurple,
        foregroundColor: Colors.white,
        actions: [
          IconButton(
            onPressed: () {
              print('Buscar');
            },
            icon: const Icon(Icons.search),
          ),
          IconButton(
            onPressed: () {
              print('Ajustes');
            },
            icon: const Icon(Icons.settings),
          ),
        ],
      ),
      body: const SafeArea(
        child: Center(
          child: Text('Contenido'),
        ),
      ),
    );
  }
}
```

Aquí `App` y `ProfileScreen` van en un solo archivo porque el editor en línea solo tiene uno; en tu proyecto siguen separados.
