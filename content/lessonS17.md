# Row

<!-- tags: Row, poner un widget al lado de otro, RenderFlex overflowed on the right, mainAxisAlignment en Row, crossAxisAlignment en Row, Row dentro de Column, spaceEvenly, SizedBox width, franja amarilla y negra, alinear icono y texto -->

`Row` pone sus hijos uno al lado del otro. Es una `Column` acostada: tiene las mismas propiedades y se escribe igual. Lo único que cambia es la dirección.

## Uso básico

```dart
Row(
  children: [
    Icon(Icons.star),
    Text('4.8'),
    Text('(120 reseñas)'),
  ],
)
```

## Los dos ejes

Las propiedades se llaman igual que en `Column`, pero los ejes están cambiados:

```svg
<svg id="rwAnatomia" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 444" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="rwAnatomia-ttl rwAnatomia-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="rwAnatomia-ttl">Las partes de una Row</title>
  <desc id="rwAnatomia-dsc">Una Row con mainAxisAlignment center, crossAxisAlignment center y tres widgets como children: un icono y dos textos. A la derecha, los tres en fila dentro del espacio de la fila, con el eje principal horizontal y el eje cruzado vertical señalados.</desc>
  <defs>
    <style>
      #rwAnatomia .title{fill:#161A26;font-size:22px;font-weight:700}
      #rwAnatomia .sub{fill:#79809A;font-size:13.5px}
      #rwAnatomia .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #rwAnatomia .cl{font-size:13px;fill:#C9CFDA}
      #rwAnatomia .s{fill:#A8D8A0} #rwAnatomia .n{fill:#F2B880} #rwAnatomia .c{fill:#7FD1E8}
      #rwAnatomia .p{fill:#D5B8F5} #rwAnatomia .k{fill:#F08FB0}
      #rwAnatomia .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #rwAnatomia .ct{fill:#161A26;font-size:14px;font-weight:700}
      #rwAnatomia .cb{fill:#454C61;font-size:13px}
      #rwAnatomia .rt{fill:#161A26;font-size:14px} #rwAnatomia .rs{fill:#79809A;font-size:12px}
      #rwAnatomia .foot{fill:#79809A;font-size:12px}
      #rwAnatomia .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #rwAnatomia .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #rwAnatomia .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#rwAnatomia-ar-amber)}
      #rwAnatomia .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #rwAnatomia .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #rwAnatomia .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#rwAnatomia-ar-green)}
      #rwAnatomia .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #rwAnatomia .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #rwAnatomia .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#rwAnatomia-ar-indigo)}
    </style>
    <marker id="rwAnatomia-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="rwAnatomia-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="rwAnatomia-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
  </defs>
  <rect width="960" height="444" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las partes de una <tspan class="mono">Row</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Es una Column acostada: las mismas propiedades, con los ejes cambiados.</text>
  <rect x="48" y="112" width="456" height="300" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/main.dart</text>
  <rect x="552" y="112" width="360" height="300" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="79.6" y="180" width="343.4" height="22" rx="5"/>
  <rect class="hl-green" x="79.6" y="204" width="359.0" height="22" rx="5"/>
  <rect class="hl-indigo" x="79.6" y="228" width="70.4" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="31.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Row</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="343.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">mainAxisAlignment</tspan>: <tspan class="c">MainAxisAlignment</tspan>.center,</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="358.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">crossAxisAlignment</tspan>: <tspan class="c">CrossAxisAlignment</tspan>.center,</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">children</tspan>: [</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="132.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Icon</tspan>(<tspan class="c">Icons</tspan>.star),</text>
  <text class="cl mono" font-size="13" x="99.2" y="292" textLength="93.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(<tspan class="s">'4.8'</tspan>),</text>
  <text class="cl mono" font-size="13" x="99.2" y="316" textLength="171.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(<tspan class="s">'(120 reseñas)'</tspan>),</text>
  <text class="cl mono" font-size="13" x="83.6" y="340" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="68.0" y="364" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<path d="M52,47 H326" stroke="#A96C05" stroke-width="1.75" marker-end="url(#rwAnatomia-ar-amber)"/><text x="190" y="66" text-anchor="middle" font-size="11.5" font-weight="700" fill="#A96C05">eje principal</text><rect x="52" y="96" width="276" height="80" rx="8" fill="#FBFBFD" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M32,98 V174" stroke="#3A8235" stroke-width="1.75" marker-end="url(#rwAnatomia-ar-green)"/><text x="18" y="136" text-anchor="middle" font-size="11.5" font-weight="700" fill="#3A8235" transform="rotate(-90 18 136)">eje cruzado</text><path d="M106,125 l3.5,7.5 l8,1 l-6,5.5 l1.5,8 l-7,-4 l-7,4 l1.5,-8 l-6,-5.5 l8,-1 Z" fill="#F7C948" stroke="#A96C05" stroke-width="1.25"/><rect x="126" y="124" width="44" height="24" rx="6" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="148.0" y="136.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#4453C9">4.8</text><rect x="178" y="124" width="108" height="24" rx="6" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="232.0" y="136.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#4453C9">(120 reseñas)</text>
  </g>
  <path class="ld-amber" d="M432.8,191 H504"/>
  <path class="ar-amber" d="M504,191 H600"/>
  <path class="ld-green" d="M448.4,215 H504"/>
  <path class="ar-green" d="M504,215 H584 V238"/>
  <path class="ld-indigo" d="M175.4,239 H504"/>
  <path class="ar-indigo" d="M504,239 H514 V348 H742 V324 H742"/>
</svg>
```

```dart
Row(
  mainAxisAlignment: MainAxisAlignment.center,
  crossAxisAlignment: CrossAxisAlignment.center,
  children: [
    Icon(Icons.star),
    Text('4.8'),
    Text('(120 reseñas)'),
  ],
)
```

| | Eje principal (`mainAxisAlignment`) | Eje cruzado (`crossAxisAlignment`) |
|---|---|---|
| `Column` | Vertical | Horizontal |
| `Row` | Horizontal | Vertical |

La regla para no confundirse: el eje principal es **la dirección en la que el widget acomoda a sus hijos**. Una `Row` los acomoda a lo ancho, así que `mainAxisAlignment` los mueve a lo ancho.

## Alinear los hijos

```svg
<svg id="rwAlineacion" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="rwAlineacion-ttl rwAlineacion-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="rwAlineacion-ttl">Dónde quedan los hijos de una Row</title>
  <desc id="rwAlineacion-dsc">Los valores de MainAxisAlignment en una Row: start, center, end, spaceBetween y spaceEvenly reparten los hijos a lo ancho. Los valores de CrossAxisAlignment: start, center, end y stretch los ubican a lo alto.</desc>
  <defs>
    <style>
      #rwAlineacion .title{fill:#161A26;font-size:22px;font-weight:700}
      #rwAlineacion .sub{fill:#79809A;font-size:13.5px}
      #rwAlineacion .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #rwAlineacion .nt{font-size:15px;font-weight:700;fill:#161A26}
      #rwAlineacion .nb{fill:#454C61;font-size:13px}
      #rwAlineacion .lbl{fill:#556074;font-size:12px;font-weight:600}
      #rwAlineacion .foot{fill:#79809A;font-size:12px}
      #rwAlineacion .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #rwAlineacion .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#rwAlineacion-arrow)}
    </style>
    <marker id="rwAlineacion-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="560" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Dónde quedan los hijos de una <tspan class="mono">Row</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Cada caja punteada es el espacio de la misma fila. Solo cambia la propiedad.</text>
  <text class="h" x="48" y="124" fill="#A96C05">mainAxisAlignment · A LO ANCHO</text>
  <g transform="translate(48,140)">
    <rect width="258" height="56" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="8" y="18" width="44" height="20" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="58" y="8" width="44" height="40" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="108" y="14" width="44" height="28" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="274" y="28.0" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" data-fit="130">start</text>
  </g>
  <g transform="translate(48,212)">
    <rect width="258" height="56" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="57" y="18" width="44" height="20" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="107" y="8" width="44" height="40" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="157" y="14" width="44" height="28" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="274" y="28.0" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" data-fit="130">center</text>
  </g>
  <g transform="translate(48,284)">
    <rect width="258" height="56" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="106" y="18" width="44" height="20" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="156" y="8" width="44" height="40" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="206" y="14" width="44" height="28" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="274" y="28.0" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" data-fit="130">end</text>
  </g>
  <g transform="translate(48,356)">
    <rect width="258" height="56" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="8" y="18" width="44" height="20" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="107" y="8" width="44" height="40" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="206" y="14" width="44" height="28" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="274" y="28.0" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" data-fit="130">spaceBetween</text>
  </g>
  <g transform="translate(48,428)">
    <rect width="258" height="56" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="36" y="18" width="44" height="20" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="107" y="8" width="44" height="40" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="178" y="14" width="44" height="28" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="274" y="28.0" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" data-fit="130">spaceEvenly</text>
  </g>
  <text class="h" x="504" y="124" fill="#3A8235">crossAxisAlignment · A LO ALTO</text>
  <g transform="translate(504,140)">
    <rect width="258" height="72" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="8" y="8" width="44" height="20" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="58" y="8" width="44" height="40" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="108" y="8" width="44" height="28" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="274" y="36.0" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" data-fit="130">start</text>
  </g>
  <g transform="translate(504,230)">
    <rect width="258" height="72" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="8" y="26" width="44" height="20" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="58" y="16" width="44" height="40" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="108" y="22" width="44" height="28" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="274" y="36.0" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" data-fit="130">center</text>
  </g>
  <g transform="translate(504,320)">
    <rect width="258" height="72" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="8" y="44" width="44" height="20" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="58" y="24" width="44" height="40" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="108" y="36" width="44" height="28" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="274" y="36.0" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" data-fit="130">end</text>
  </g>
  <g transform="translate(504,410)">
    <rect width="258" height="72" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
    <rect x="8" y="8" width="44" height="56" rx="5" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
    <rect x="58" y="8" width="44" height="56" rx="5" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
    <rect x="108" y="8" width="44" height="56" rx="5" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
    <text class="mono" x="274" y="36.0" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" data-fit="130">stretch</text>
  </g>
  <text class="foot" x="48" y="532" data-fit="860">Los valores por defecto son start a lo ancho y center a lo alto.</text>
</svg>
```

Los valores son los mismos de `Column`. En una `Row`, `mainAxisAlignment` reparte a lo ancho:

- `MainAxisAlignment.spaceBetween` es el típico de un encabezado: el título a la izquierda y un enlace o un icono a la derecha.
- `MainAxisAlignment.spaceEvenly` reparte varios elementos iguales, como una fila de indicadores.

`crossAxisAlignment` los ubica a lo alto. Se nota cuando los hijos tienen alturas distintas, como una foto al lado de un texto. El valor por defecto, `center`, es casi siempre el que quieres.

Para separar los hijos se usa el mismo `SizedBox`, ahora con `width`:

```dart
Row(
  children: [
    Icon(Icons.star),
    SizedBox(width: 4),
    Text('4.8'),
    SizedBox(width: 8),
    Text('(120 reseñas)'),
  ],
)
```

## Filas dentro de columnas

Un hijo de una `Column` puede ser una `Row`, y al revés. Así se arma casi cualquier diseño: se mira el boceto y se parte en filas y columnas, de afuera hacia adentro.

Una fila de chat, por ejemplo, es una `Row` con una foto y una `Column` de dos textos:

```dart
Row(
  children: [
    Icon(Icons.account_circle, size: 48),
    SizedBox(width: 12),
    Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Ana Torres',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        Text('Nos vemos mañana en clase'),
      ],
    ),
  ],
)
```

Antes de escribir código, dibuja las cajas sobre el diseño. Si una caja tiene cosas una al lado de otra, es una `Row`. Si las tiene una debajo de otra, es una `Column`.

## Cuando no cabe

Una `Row` no parte sus hijos en dos renglones. Si no caben a lo ancho, aparece la franja amarilla y negra en el borde derecho, y la consola dice `A RenderFlex overflowed by 48 pixels on the right`.

Pasa sobre todo con textos largos dentro de una fila. La solución es `Expanded`, que le dice a un hijo que ocupe solo el espacio que sobra, y se ve en la sesión 3. Por ahora, si te ocurre en el taller, acorta el texto de prueba.

## Ejemplo completo

Las dos filas de la lección, una debajo de la otra: la de la calificación, centrada, y la del chat, que lleva una `Column` adentro.

```dart trycode=0a47cdf04c1ad701366753a6e89105f7
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
      appBar: AppBar(title: const Text('Row')),
      body: const Padding(
        padding: EdgeInsets.all(24),
        child: Column(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(Icons.star),
                SizedBox(width: 4),
                Text('4.8'),
                SizedBox(width: 8),
                Text('(120 reseñas)'),
              ],
            ),
            SizedBox(height: 24),
            Row(
              children: [
                Icon(Icons.account_circle, size: 48),
                SizedBox(width: 12),
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Ana Torres',
                      style: TextStyle(fontWeight: FontWeight.bold),
                    ),
                    Text('Nos vemos mañana en clase'),
                  ],
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
```

Aquí `App` y `HomeScreen` van en un solo archivo porque el editor en línea solo tiene uno; en tu proyecto siguen separados.
