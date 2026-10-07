# BottomNavigationBar

<!-- tags: BottomNavigationBar, barra de navegación inferior, BottomNavigationBarItem, botones de abajo, bottomNavigationBar del Scaffold, icon y label, currentIndex, la barra no cambia al tocar, items debe tener al menos dos, pestañas de abajo -->

Al `Scaffold` le quedaba un lugar por llenar: `bottomNavigationBar`, el borde de abajo. Ahí va la barra con la que muchas apps muestran sus secciones.

## Tres botones abajo

```svg
<svg id="bnCodigo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 834" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="bnCodigo-ttl bnCodigo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="bnCodigo-ttl">Tres botones en bottomNavigationBar</title>
  <desc id="bnCodigo-dsc">Un Scaffold con appBar, body y bottomNavigationBar. La barra de abajo es un BottomNavigationBar con tres BottomNavigationBarItem: Inicio, Chats y Perfil. En el resultado, la barra queda pegada al borde de abajo con los tres botones repartidos a lo ancho, y el primero, Inicio, aparece resaltado.</desc>
  <defs>
    <style>
      #bnCodigo .title{fill:#161A26;font-size:22px;font-weight:700}
      #bnCodigo .sub{fill:#79809A;font-size:13.5px}
      #bnCodigo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #bnCodigo .cl{font-size:13px;fill:#C9CFDA}
      #bnCodigo .s{fill:#A8D8A0} #bnCodigo .n{fill:#F2B880} #bnCodigo .c{fill:#7FD1E8}
      #bnCodigo .p{fill:#D5B8F5} #bnCodigo .k{fill:#F08FB0}
      #bnCodigo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #bnCodigo .ct{fill:#161A26;font-size:14px;font-weight:700}
      #bnCodigo .cb{fill:#454C61;font-size:13px}
      #bnCodigo .rt{fill:#161A26;font-size:14px} #bnCodigo .rs{fill:#79809A;font-size:12px}
      #bnCodigo .foot{fill:#79809A;font-size:12px}
      #bnCodigo .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #bnCodigo .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #bnCodigo .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#bnCodigo-ar-amber)}
    </style>
    <marker id="bnCodigo-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
  </defs>
  <rect width="960" height="834" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Tres botones en <tspan class="mono">bottomNavigationBar</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">La barra queda fija abajo. El body ocupa lo que queda entre ella y la barra de arriba.</text>
  <rect x="48" y="112" width="456" height="564" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/home_screen.dart</text>
  <rect x="552" y="112" width="360" height="564" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="79.6" y="228" width="156.2" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="c">Scaffold</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="343.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">appBar</tspan>: <tspan class="c">AppBar</tspan>(<tspan class="p">title</tspan>: <tspan class="k">const</tspan> <tspan class="c">Text</tspan>(<tspan class="s">'Inicio'</tspan>)),</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="351.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">body</tspan>: <tspan class="k">const</tspan> <tspan class="c">Center</tspan>(<tspan class="p">child</tspan>: <tspan class="c">Text</tspan>(<tspan class="s">'Contenido'</tspan>)),</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="319.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">bottomNavigationBar</tspan>: <tspan class="c">BottomNavigationBar</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">currentIndex</tspan>: <tspan class="n">0</tspan>,</text>
  <text class="cl mono" font-size="13" x="99.2" y="292" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">items</tspan>: <tspan class="k">const</tspan> [</text>
  <text class="cl mono" font-size="13" x="114.8" y="316" textLength="187.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">BottomNavigationBarItem</tspan>(</text>
  <text class="cl mono" font-size="13" x="130.4" y="340" textLength="179.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">icon</tspan>: <tspan class="c">Icon</tspan>(<tspan class="c">Icons</tspan>.home),</text>
  <text class="cl mono" font-size="13" x="130.4" y="364" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">label</tspan>: <tspan class="s">'Inicio'</tspan>,</text>
  <text class="cl mono" font-size="13" x="114.8" y="388" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="114.8" y="412" textLength="187.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">BottomNavigationBarItem</tspan>(</text>
  <text class="cl mono" font-size="13" x="130.4" y="436" textLength="179.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">icon</tspan>: <tspan class="c">Icon</tspan>(<tspan class="c">Icons</tspan>.chat),</text>
  <text class="cl mono" font-size="13" x="130.4" y="460" textLength="117.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">label</tspan>: <tspan class="s">'Chats'</tspan>,</text>
  <text class="cl mono" font-size="13" x="114.8" y="484" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="114.8" y="508" textLength="187.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">BottomNavigationBarItem</tspan>(</text>
  <text class="cl mono" font-size="13" x="130.4" y="532" textLength="195.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">icon</tspan>: <tspan class="c">Icon</tspan>(<tspan class="c">Icons</tspan>.person),</text>
  <text class="cl mono" font-size="13" x="130.4" y="556" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">label</tspan>: <tspan class="s">'Perfil'</tspan>,</text>
  <text class="cl mono" font-size="13" x="114.8" y="580" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="99.2" y="604" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="83.6" y="628" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="68.0" y="652" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">);</text>
  <g transform="translate(552,144)">
<clipPath id="bnCodigo-scr"><rect width="204" height="440" rx="26"/></clipPath><g transform="translate(78,40)"><rect width="204" height="440" rx="26" fill="#FFFFFF"/><g clip-path="url(#bnCodigo-scr)"><rect width="204" height="52" fill="#F1ECF8"/><text x="18" y="31" font-size="17" font-weight="500" fill="#161A26" text-anchor="start">Inicio</text><text x="102.0" y="216" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="middle">Contenido</text><rect y="380" width="204" height="60" fill="#F3EDF7"/><path transform="translate(34,402)" d="M-8,1 L0,-7 L8,1 M-6,-0.5 V7 H6 V-0.5" fill="none" stroke="#6750A4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="34" y="426" font-size="12" font-weight="600" fill="#6750A4" text-anchor="middle">Inicio</text><path transform="translate(102,402)" d="M-7,-7 h14 a2,2 0 0 1 2,2 v7 a2,2 0 0 1 -2,2 h-8 l-4,3 v-3 h-2 a2,2 0 0 1 -2,-2 v-7 a2,2 0 0 1 2,-2 Z" fill="none" stroke="#556074" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="102" y="426" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Chats</text><path transform="translate(170,402)" d="M-3.5,-4 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M-7,7 a7,6 0 0 1 14,0" fill="none" stroke="#556074" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="170" y="426" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Perfil</text></g></g><rect x="78" y="40" width="204" height="440" rx="26" fill="none" stroke="#2A3040" stroke-width="3"/><rect x="84" y="424" width="192" height="52" rx="14" fill="#A96C05" fill-opacity=".08" stroke="#A96C05" stroke-width="2"/>
  </g>
  <path class="ld-amber" d="M409.4,239 H504"/>
  <path class="ar-amber" d="M504,239 H523 V594 H636"/>
  <g transform="translate(48.0,700)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#FFF3DC" stroke="#A96C05" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="219">items</text>
    <text class="cb" x="16" y="60" data-fit="245">Los botones, de izquierda</text>
    <text class="cb" x="16" y="79" data-fit="245">a derecha. Mínimo dos.</text>
  </g>
  <g transform="translate(341.3,700)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#EEF1FF" stroke="#4453C9" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="219">icon y label</text>
    <text class="cb" x="16" y="60" data-fit="245">Cada botón lleva un icono</text>
    <text class="cb" x="16" y="79" data-fit="245">y un texto debajo.</text>
  </g>
  <g transform="translate(634.7,700)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#E8F6E3" stroke="#3A8235" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="219">currentIndex</text>
    <text class="cb" x="16" y="60" data-fit="245">El botón resaltado. Se cuenta</text>
    <text class="cb" x="16" y="79" data-fit="245">desde 0: aquí es Inicio.</text>
  </g>
</svg>
```

```dart
return Scaffold(
  appBar: AppBar(title: const Text('Inicio')),
  body: const Center(child: Text('Contenido')),
  bottomNavigationBar: BottomNavigationBar(
    currentIndex: 0,
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
```

`items` es la lista de botones, y se dibujan de izquierda a derecha en el orden en que los escribes. Cada uno es un `BottomNavigationBarItem` con un `icon` y un `label`. La barra pide al menos dos; con uno solo la app falla al arrancar.

`currentIndex` dice cuál aparece resaltado. Se cuenta desde 0, así que `0` es *Inicio*. Cámbialo a `2` y el resaltado pasa a *Perfil*.

## Por ahora solo se ve

Toca *Chats*: no pasa nada. El resaltado está fijo porque `currentIndex` tiene un número escrito a mano, y el `body` sigue mostrando lo mismo.

Hacer que la barra responda, y que cada botón muestre un contenido distinto, es la sesión 9. Hoy basta con saber dónde va y cómo se ve.

La pantalla del taller no lleva esta barra. Pruébala en `HomeScreen`.

## Ejemplo completo

Una pantalla con la barra de arriba, el contenido y los tres botones de abajo. Cambia `currentIndex` o el icono de un botón y mira el resultado.

```dart trycode=PENDIENTE_S27
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
      initialRoute: '/home',
      routes: {'/home': (context) => const HomeScreen()},
    );
  }
}

/// First screen of the app.
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Inicio')),
      body: const SafeArea(
        child: Center(
          child: Text('Contenido'),
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: 0,
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

Aquí `App` y `HomeScreen` van en un solo archivo porque el editor en línea solo tiene uno; en tu proyecto siguen separados.
