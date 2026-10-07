# Armar una pantalla

<!-- tags: crear una pantalla nueva, registrar una pantalla en main.dart, routes e initialRoute, Scaffold como raíz de la pantalla, clase que termina en Screen, lib/screens, Could not find a generator for route, Target of URI doesn't exist, la app abre en otra pantalla, import de la pantalla -->

Toda pantalla nueva se hace igual, en dos pasos: escribes la pantalla en su archivo y la anotas en `main.dart`.

## La estructura de una pantalla

```svg
<svg id="apEstructura" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 636" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="apEstructura-ttl apEstructura-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="apEstructura-ttl">La estructura de una pantalla</title>
  <desc id="apEstructura-dsc">El archivo profile_screen.dart: una clase ProfileScreen que extiende StatelessWidget y cuyo build devuelve un Scaffold con appBar y body. A la derecha, la pantalla que produce: el Scaffold ocupa todo, la barra queda arriba y el contenido debajo.</desc>
  <defs>
    <style>
      #apEstructura .title{fill:#161A26;font-size:22px;font-weight:700}
      #apEstructura .sub{fill:#79809A;font-size:13.5px}
      #apEstructura .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #apEstructura .cl{font-size:13px;fill:#C9CFDA}
      #apEstructura .s{fill:#A8D8A0} #apEstructura .n{fill:#F2B880} #apEstructura .c{fill:#7FD1E8}
      #apEstructura .p{fill:#D5B8F5} #apEstructura .k{fill:#F08FB0}
      #apEstructura .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #apEstructura .ct{fill:#161A26;font-size:14px;font-weight:700}
      #apEstructura .cb{fill:#454C61;font-size:13px}
      #apEstructura .rt{fill:#161A26;font-size:14px} #apEstructura .rs{fill:#79809A;font-size:12px}
      #apEstructura .foot{fill:#79809A;font-size:12px}
      #apEstructura .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #apEstructura .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #apEstructura .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#apEstructura-ar-amber)}
      #apEstructura .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #apEstructura .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #apEstructura .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#apEstructura-ar-green)}
      #apEstructura .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #apEstructura .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #apEstructura .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#apEstructura-ar-indigo)}
    </style>
    <marker id="apEstructura-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="apEstructura-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="apEstructura-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
  </defs>
  <rect width="960" height="636" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La estructura de una pantalla</text>
  <text class="sub" x="48" y="80" data-fit="860">Una clase cuyo build devuelve un Scaffold. Todas las pantallas del curso empiezan así.</text>
  <rect x="48" y="112" width="456" height="492" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/profile_screen.dart</text>
  <rect x="552" y="112" width="360" height="492" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="149.8" y="348" width="70.4" height="22" rx="5"/>
  <rect class="hl-amber" x="110.8" y="372" width="54.8" height="22" rx="5"/>
  <rect class="hl-green" x="110.8" y="396" width="39.2" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="304.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">import</tspan> <tspan class="s">'package:flutter/material.dart'</tspan>;</text>
  <text class="cl mono" font-size="13" x="68.0" y="220" textLength="187.2" lengthAdjust="spacingAndGlyphs" data-fit="432">/// <tspan class="c">Profile</tspan> of a person.</text>
  <text class="cl mono" font-size="13" x="68.0" y="244" textLength="351.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">class</tspan> <tspan class="c">ProfileScreen</tspan> <tspan class="k">extends</tspan> <tspan class="c">StatelessWidget</tspan> {</text>
  <text class="cl mono" font-size="13" x="83.6" y="268" textLength="257.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">const</tspan> <tspan class="c">ProfileScreen</tspan>({<tspan class="k">super</tspan>.key});</text>
  <text class="cl mono" font-size="13" x="83.6" y="316" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">@override</tspan></text>
  <text class="cl mono" font-size="13" x="83.6" y="340" textLength="280.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Widget</tspan> build(<tspan class="c">BuildContext</tspan> context) {</text>
  <text class="cl mono" font-size="13" x="99.2" y="364" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="c">Scaffold</tspan>(</text>
  <text class="cl mono" font-size="13" x="114.8" y="388" textLength="343.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">appBar</tspan>: <tspan class="c">AppBar</tspan>(<tspan class="p">title</tspan>: <tspan class="k">const</tspan> <tspan class="c">Text</tspan>(<tspan class="s">'Perfil'</tspan>)),</text>
  <text class="cl mono" font-size="13" x="114.8" y="412" textLength="163.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">body</tspan>: <tspan class="k">const</tspan> <tspan class="c">SafeArea</tspan>(</text>
  <text class="cl mono" font-size="13" x="130.4" y="436" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Center</tspan>(</text>
  <text class="cl mono" font-size="13" x="146.0" y="460" textLength="195.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Text</tspan>(<tspan class="s">'Contenido'</tspan>),</text>
  <text class="cl mono" font-size="13" x="130.4" y="484" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="114.8" y="508" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="99.2" y="532" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">);</text>
  <text class="cl mono" font-size="13" x="83.6" y="556" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="580" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <g transform="translate(552,144)">
<rect x="78" y="22" width="204" height="396" rx="26" fill="#F0F1F4" stroke="#2A3040" stroke-width="3"/><rect x="84" y="28" width="192" height="384" rx="20" fill="#4453C9" fill-opacity=".08" stroke="#4453C9" stroke-width="2"/><rect x="92" y="60" width="176" height="54" rx="12" fill="#A96C05" fill-opacity=".08" stroke="#A96C05" stroke-width="2"/><text dy="0.35em" x="108" y="87" font-size="17" font-weight="500" fill="#161A26" text-anchor="start">Perfil</text><rect x="92" y="122" width="176" height="282" rx="12" fill="#3A8235" fill-opacity=".08" stroke="#3A8235" stroke-width="2"/><text x="180" y="268" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="middle">Contenido</text>
  </g>
  <path class="ld-indigo" d="M230.0,359 H504"/>
  <path class="ar-indigo" d="M504,359 H514 V188 H636"/>
  <path class="ld-amber" d="M464.0,383 H504"/>
  <path class="ar-amber" d="M504,383 H523 V231 H644"/>
  <path class="ld-green" d="M284.6,407 H504"/>
  <path class="ar-green" d="M504,407 H532 V434 H644"/>
</svg>
```

```dart
import 'package:flutter/material.dart';

/// Profile of a person.
class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Perfil')),
      body: const SafeArea(
        child: Center(
          child: Text('Contenido'),
        ),
      ),
    );
  }
}
```

Es un `StatelessWidget` como tus componentes. Lo que la hace pantalla son tres cosas:

- El archivo va en `lib/screens/`, uno por pantalla: `profile_screen.dart`.
- La clase termina en `Screen`: `ProfileScreen`.
- Su `build` devuelve un `Scaffold`. Nada lo envuelve.

Dentro del `Scaffold` van la barra, en `appBar`, y el contenido, en `body`. El `body` empieza con un `SafeArea`.

## Anotarla en main.dart

```svg
<svg id="apRutas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 516" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="apRutas-ttl apRutas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="apRutas-ttl">Anotar la pantalla en main.dart</title>
  <desc id="apRutas-dsc">El archivo main.dart con tres líneas señaladas. El import trae el archivo de la pantalla. La entrada de routes le da un nombre, /profile, y dice qué pantalla se construye. initialRoute dice con cuál abre la app.</desc>
  <defs>
    <style>
      #apRutas .title{fill:#161A26;font-size:22px;font-weight:700}
      #apRutas .sub{fill:#79809A;font-size:13.5px}
      #apRutas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #apRutas .cl{font-size:13px;fill:#C9CFDA}
      #apRutas .s{fill:#A8D8A0} #apRutas .n{fill:#F2B880} #apRutas .c{fill:#7FD1E8}
      #apRutas .p{fill:#D5B8F5} #apRutas .k{fill:#F08FB0}
      #apRutas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #apRutas .ct{fill:#161A26;font-size:14px;font-weight:700}
      #apRutas .cb{fill:#454C61;font-size:13px}
      #apRutas .rt{fill:#161A26;font-size:14px} #apRutas .rs{fill:#79809A;font-size:12px}
      #apRutas .foot{fill:#79809A;font-size:12px}
      #apRutas .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #apRutas .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #apRutas .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#apRutas-ar-amber)}
      #apRutas .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #apRutas .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #apRutas .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#apRutas-ar-green)}
      #apRutas .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #apRutas .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #apRutas .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#apRutas-ar-indigo)}
    </style>
    <marker id="apRutas-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="apRutas-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="apRutas-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
  </defs>
  <rect width="960" height="516" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Anotar la pantalla en <tspan class="mono">main.dart</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Tres líneas. Sin ellas la pantalla existe, pero la app no sabe llegar a ella.</text>
  <rect x="48" y="112" width="456" height="372" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/main.dart</text>
  <rect x="552" y="112" width="360" height="372" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">QUÉ HACE CADA LÍNEA</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="305.8" y="180" width="156.2" height="22" rx="5"/>
  <rect class="hl-green" x="79.6" y="276" width="101.6" height="22" rx="5"/>
  <rect class="hl-amber" x="95.2" y="324" width="86.0" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="304.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">import</tspan> <tspan class="s">'package:flutter/material.dart'</tspan>;</text>
  <text class="cl mono" font-size="13" x="68.0" y="196" textLength="405.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">import</tspan> <tspan class="s">'package:miapp1/screens/profile_screen.dart'</tspan>;</text>
  <text class="cl mono" font-size="13" x="68.0" y="244" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="c">MaterialApp</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="268" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">title</tspan>: <tspan class="s">'Mi app'</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="292" textLength="195.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">initialRoute</tspan>: <tspan class="s">'/profile'</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="316" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">routes</tspan>: {</text>
  <text class="cl mono" font-size="13" x="99.2" y="340" textLength="366.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">'/profile'</tspan>: (context) =&gt; <tspan class="k">const</tspan> <tspan class="c">ProfileScreen</tspan>(),</text>
  <text class="cl mono" font-size="13" x="83.6" y="364" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">},</text>
  <text class="cl mono" font-size="13" x="68.0" y="388" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">);</text>
  <g transform="translate(552,144)">
<g transform="translate(16,16)"><rect width="328" height="76" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#4453C9" data-fit="300">El import</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Trae el archivo de la pantalla.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">Sin él, main.dart no la conoce.</text></g><g transform="translate(16,124)"><rect width="328" height="76" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#3A8235" data-fit="300">initialRoute</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">La pantalla con la que abre la app.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">Tiene que ser un nombre de routes.</text></g><g transform="translate(16,232)"><rect width="328" height="76" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#A96C05" data-fit="300">La entrada de routes</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Un nombre que empieza con /</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">y la pantalla que se construye.</text></g>
  </g>
  <path class="ld-indigo" d="M479.6,191 H504"/>
  <path class="ar-indigo" d="M504,191 H514 V198 H568"/>
  <path class="ld-green" d="M284.6,287 H504"/>
  <path class="ar-green" d="M504,287 H523 V306 H568"/>
  <path class="ld-amber" d="M471.8,335 H504"/>
  <path class="ar-amber" d="M504,335 H532 V414 H568"/>
</svg>
```

```dart
import 'package:flutter/material.dart';
import 'package:miapp1/screens/profile_screen.dart';
```

```dart
return MaterialApp(
  title: 'Mi app',
  initialRoute: '/profile',
  routes: {
    '/profile': (context) => const ProfileScreen(),
  },
);
```

El `import` trae el archivo. Empieza con `package:miapp1/`, el nombre de tu proyecto, y sigue con la ruta desde `lib/`. Si la ruta tiene un error, el editor dice `Target of URI doesn't exist`.

La entrada de `routes` le pone nombre a la pantalla. El nombre empieza con `/` y lo eliges tú; lo normal es que se parezca al de la clase.

`initialRoute` dice con cuál pantalla abre la app. Tiene que ser uno de los nombres de `routes`, escrito igual. Si no coincide, la app falla al arrancar con `Could not find a generator for route`.

## Ejemplo completo

La pantalla y su ruta. Cambia el nombre `'/profile'` solo en `initialRoute` y mira el error.

```dart trycode=PENDIENTE_S25
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
      routes: {
        '/profile': (context) => const ProfileScreen(),
      },
    );
  }
}

/// Profile of a person.
class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Perfil')),
      body: const SafeArea(
        child: Center(
          child: Text('Contenido'),
        ),
      ),
    );
  }
}
```

Aquí `App` y `ProfileScreen` van en un solo archivo porque el editor en línea solo tiene uno; en tu proyecto la pantalla está en `lib/screens/` y `main.dart` la importa.
