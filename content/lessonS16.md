# Column

<!-- tags: Column, mainAxisAlignment, crossAxisAlignment, poner un widget debajo de otro, eje principal y eje cruzado, RenderFlex overflowed on the bottom, SizedBox, centrar en una columna, spaceBetween, mainAxisSize -->

Hasta ahora has puesto un solo widget en la pantalla. `Column` recibe **varios** y los pone uno debajo del otro. Junto con `Row`, que es la siguiente lección, es la base de casi cualquier diseño.

## Uso básico

Lo único obligatorio es `children`, la lista de widgets en el orden en que se apilan:

```dart
Column(
  children: [
    Text('Ana Torres'),
    Text('Estudiante'),
    Text('Cali'),
  ],
)
```

Fíjate en la diferencia con los widgets anteriores. Un botón tiene `child`, en singular, porque contiene un solo widget. `Column` tiene `children`, en plural, y recibe una lista entre `[ ]`.

## Los dos ejes

Una `Column` tiene dos direcciones, y cada una tiene su propiedad:

```svg
<svg id="clAnatomia" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 456" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="clAnatomia-ttl clAnatomia-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="clAnatomia-ttl">Las partes de una Column</title>
  <desc id="clAnatomia-dsc">Una Column con mainAxisAlignment center, crossAxisAlignment start y tres Text como children. A la derecha, los tres textos apilados dentro del espacio de la columna, con el eje principal vertical y el eje cruzado horizontal señalados.</desc>
  <defs>
    <style>
      #clAnatomia .title{fill:#161A26;font-size:22px;font-weight:700}
      #clAnatomia .sub{fill:#79809A;font-size:13.5px}
      #clAnatomia .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #clAnatomia .cl{font-size:13px;fill:#C9CFDA}
      #clAnatomia .s{fill:#A8D8A0} #clAnatomia .n{fill:#F2B880} #clAnatomia .c{fill:#7FD1E8}
      #clAnatomia .p{fill:#D5B8F5} #clAnatomia .k{fill:#F08FB0}
      #clAnatomia .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #clAnatomia .ct{fill:#161A26;font-size:14px;font-weight:700}
      #clAnatomia .cb{fill:#454C61;font-size:13px}
      #clAnatomia .rt{fill:#161A26;font-size:14px} #clAnatomia .rs{fill:#79809A;font-size:12px}
      #clAnatomia .foot{fill:#79809A;font-size:12px}
      #clAnatomia .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #clAnatomia .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #clAnatomia .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#clAnatomia-ar-amber)}
      #clAnatomia .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #clAnatomia .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #clAnatomia .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#clAnatomia-ar-green)}
      #clAnatomia .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #clAnatomia .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #clAnatomia .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#clAnatomia-ar-indigo)}
    </style>
    <marker id="clAnatomia-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="clAnatomia-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="clAnatomia-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
  </defs>
  <rect width="960" height="456" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las partes de una <tspan class="mono">Column</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">children es la lista de widgets que apila. Las otras dos propiedades dicen dónde quedan dentro de su espacio.</text>
  <rect x="48" y="112" width="456" height="312" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/main.dart</text>
  <rect x="552" y="112" width="360" height="312" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="79.6" y="180" width="343.4" height="22" rx="5"/>
  <rect class="hl-green" x="79.6" y="204" width="351.2" height="22" rx="5"/>
  <rect class="hl-indigo" x="79.6" y="228" width="70.4" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="54.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Column</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="343.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">mainAxisAlignment</tspan>: <tspan class="c">MainAxisAlignment</tspan>.center,</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="351.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">crossAxisAlignment</tspan>: <tspan class="c">CrossAxisAlignment</tspan>.start,</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">children</tspan>: [</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(<tspan class="s">'Ana Torres'</tspan>),</text>
  <text class="cl mono" font-size="13" x="99.2" y="292" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(<tspan class="s">'Estudiante'</tspan>),</text>
  <text class="cl mono" font-size="13" x="99.2" y="316" textLength="101.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(<tspan class="s">'Cali'</tspan>),</text>
  <text class="cl mono" font-size="13" x="83.6" y="340" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="68.0" y="364" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<rect x="130" y="88" width="160" height="176" rx="8" fill="#FBFBFD" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/><rect x="138" y="132" width="96" height="24" rx="6" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="186.0" y="144.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#4453C9">Ana Torres</text><rect x="138" y="164" width="92" height="24" rx="6" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="184.0" y="176.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#4453C9">Estudiante</text><rect x="138" y="196" width="48" height="24" rx="6" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="162.0" y="208.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#4453C9">Cali</text><path d="M130,71 H288" stroke="#3A8235" stroke-width="1.75" marker-end="url(#clAnatomia-ar-green)"/><text x="210" y="63" text-anchor="middle" font-size="11.5" font-weight="700" fill="#3A8235">eje cruzado</text><path d="M312,92 V262" stroke="#A96C05" stroke-width="1.75" marker-end="url(#clAnatomia-ar-amber)"/><text x="330" y="176" text-anchor="middle" font-size="11.5" font-weight="700" fill="#A96C05" transform="rotate(90 330 176)">eje principal</text>
  </g>
  <path class="ld-amber" d="M432.8,191 H504"/>
  <path class="ar-amber" d="M504,191 H864 V232"/>
  <path class="ld-green" d="M440.6,215 H504"/>
  <path class="ar-green" d="M504,215 H678"/>
  <path class="ld-indigo" d="M175.4,239 H504"/>
  <path class="ar-indigo" d="M504,239 H514 V320 H686"/>
</svg>
```

```dart
Column(
  mainAxisAlignment: MainAxisAlignment.center,
  crossAxisAlignment: CrossAxisAlignment.start,
  children: [
    Text('Ana Torres'),
    Text('Estudiante'),
    Text('Cali'),
  ],
)
```

- El **eje principal** es la dirección en la que se apilan los hijos. En una `Column` es el vertical, y lo controla `mainAxisAlignment`.
- El **eje cruzado** es el otro. En una `Column` es el horizontal, y lo controla `crossAxisAlignment`.

Los nombres parecen rebuscados, pero tienen una razón: `Row` usa exactamente las mismas dos propiedades, con los ejes cambiados. Si dijeran *vertical* y *horizontal* habría que aprenderlas dos veces.

## Alinear los hijos

```svg
<svg id="clAlineacion" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 644" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="clAlineacion-ttl clAlineacion-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="clAlineacion-ttl">Dónde quedan los hijos de una Column</title>
  <desc id="clAlineacion-dsc">Los valores de MainAxisAlignment en una Column: start, center, end, spaceBetween y spaceEvenly reparten los hijos a lo alto. Los valores de CrossAxisAlignment: start, center, end y stretch los ubican a lo ancho.</desc>
  <defs>
    <style>
      #clAlineacion .title{fill:#161A26;font-size:22px;font-weight:700}
      #clAlineacion .sub{fill:#79809A;font-size:13.5px}
      #clAlineacion .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #clAlineacion .nt{font-size:15px;font-weight:700;fill:#161A26}
      #clAlineacion .nb{fill:#454C61;font-size:13px}
      #clAlineacion .lbl{fill:#556074;font-size:12px;font-weight:600}
      #clAlineacion .foot{fill:#79809A;font-size:12px}
      #clAlineacion .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #clAlineacion .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#clAlineacion-arrow)}
    </style>
    <marker id="clAlineacion-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="644" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Dónde quedan los hijos de una <tspan class="mono">Column</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Cada caja punteada es el espacio de la misma columna. Solo cambia la propiedad.</text>
  <text class="h" x="48" y="124" fill="#A96C05">mainAxisAlignment · A LO ALTO</text>
  <g transform="translate(48,140)">
    <rect width="136" height="168" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="40" y="8" width="56" height="22" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="24" y="36" width="88" height="22" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="48" y="64" width="40" height="22" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="68.0" y="190" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="166">start</text>
  </g>
  <g transform="translate(230,140)">
    <rect width="136" height="168" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="40" y="45" width="56" height="22" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="24" y="73" width="88" height="22" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="48" y="101" width="40" height="22" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="68.0" y="190" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="166">center</text>
  </g>
  <g transform="translate(412,140)">
    <rect width="136" height="168" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="40" y="82" width="56" height="22" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="24" y="110" width="88" height="22" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="48" y="138" width="40" height="22" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="68.0" y="190" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="166">end</text>
  </g>
  <g transform="translate(594,140)">
    <rect width="136" height="168" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="40" y="8" width="56" height="22" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="24" y="73" width="88" height="22" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="48" y="138" width="40" height="22" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="68.0" y="190" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="166">spaceBetween</text>
  </g>
  <g transform="translate(776,140)">
    <rect width="136" height="168" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="40" y="30" width="56" height="22" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="24" y="73" width="88" height="22" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="48" y="116" width="40" height="22" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="68.0" y="190" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="166">spaceEvenly</text>
  </g>
  <text class="h" x="48" y="372" fill="#3A8235">crossAxisAlignment · A LO ANCHO</text>
  <g transform="translate(48,388)">
    <rect width="136" height="168" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="8" y="8" width="56" height="22" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="8" y="36" width="88" height="22" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="8" y="64" width="40" height="22" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="68.0" y="190" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="166">start</text>
  </g>
  <g transform="translate(230,388)">
    <rect width="136" height="168" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="40" y="8" width="56" height="22" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="24" y="36" width="88" height="22" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="48" y="64" width="40" height="22" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="68.0" y="190" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="166">center</text>
  </g>
  <g transform="translate(412,388)">
    <rect width="136" height="168" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="72" y="8" width="56" height="22" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="40" y="36" width="88" height="22" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="88" y="64" width="40" height="22" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="68.0" y="190" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="166">end</text>
  </g>
  <g transform="translate(594,388)">
    <rect width="136" height="168" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="8" y="8" width="120" height="22" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="8" y="36" width="120" height="22" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="8" y="64" width="120" height="22" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="68.0" y="190" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="166">stretch</text>
  </g>
  <text class="foot" x="48" y="616" data-fit="860">Los valores por defecto son start a lo alto y center a lo ancho.</text>
</svg>
```

| `mainAxisAlignment` | Qué hace a lo alto |
|---|---|
| `MainAxisAlignment.start` | Todos arriba. Es el valor por defecto |
| `MainAxisAlignment.center` | Todos juntos, en el centro |
| `MainAxisAlignment.end` | Todos abajo |
| `MainAxisAlignment.spaceBetween` | El primero arriba, el último abajo, y el espacio repartido entre ellos |
| `MainAxisAlignment.spaceEvenly` | El mismo espacio entre ellos y también en los extremos |

| `crossAxisAlignment` | Qué hace a lo ancho |
|---|---|
| `CrossAxisAlignment.start` | Pegados a la izquierda |
| `CrossAxisAlignment.center` | Centrados. Es el valor por defecto |
| `CrossAxisAlignment.end` | Pegados a la derecha |
| `CrossAxisAlignment.stretch` | Cada hijo se estira hasta ocupar todo el ancho |

`crossAxisAlignment: CrossAxisAlignment.start` es el que más vas a escribir: el texto de una tarjeta casi siempre va alineado a la izquierda, y por defecto sale centrado.

Si `mainAxisAlignment` no parece hacer nada, la causa suele ser el tamaño de la columna. A lo alto, una `Column` ocupa todo el espacio que le den, pero a lo ancho mide lo mismo que su hijo más ancho. Dentro de un `Center` eso significa pantalla completa a lo alto.

Para que mida solo lo que necesitan sus hijos, por ejemplo dentro de una tarjeta, se usa `mainAxisSize`:

```dart
Column(
  mainAxisSize: MainAxisSize.min,
  children: [
    Text('Ana Torres'),
    Text('Estudiante'),
  ],
)
```

## Separar los hijos

Una `Column` pega a sus hijos, sin aire entre ellos. La forma más simple de separarlos es intercalar un `SizedBox`, una caja vacía con la altura que le digas:

```dart
Column(
  children: [
    Text('Ana Torres'),
    SizedBox(height: 8),
    Text('Estudiante'),
    SizedBox(height: 24),
    ElevatedButton(
      onPressed: () {
        print('Editar');
      },
      child: Text('Editar perfil'),
    ),
  ],
)
```

Usa pocos valores y repítelos: `8` entre cosas que van juntas, `16` o `24` entre bloques distintos. Un diseño con separaciones de 7, 13 y 22 se ve desordenado aunque nadie sepa decir por qué.

## Cuando no cabe

Si los hijos necesitan más alto del que hay, la pantalla muestra una franja amarilla y negra, y la consola dice `A RenderFlex overflowed by 120 pixels on the bottom`. No es un error tuyo de sintaxis: la columna no sabe hacer scroll. La solución, `SingleChildScrollView`, es parte de la sesión 3.

## Ejemplo completo

Una `Column` con textos, separaciones y un botón, centrada a lo alto y con los hijos alineados a la izquierda. Cambia `mainAxisAlignment` y `crossAxisAlignment` para ver cómo se mueven.

```dart trycode=ed1eab67616a0fda8b2ce06f4821cd62
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
      appBar: AppBar(title: const Text('Column')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Ana Torres',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            const Text('Estudiante'),
            const Text('Cali'),
            const SizedBox(height: 24),
            ElevatedButton(
              onPressed: () {
                print('Editar');
              },
              child: const Text('Editar perfil'),
            ),
          ],
        ),
      ),
    );
  }
}
```

Aquí `App` y `HomeScreen` van en un solo archivo porque el editor en línea solo tiene uno; en tu proyecto siguen separados.
