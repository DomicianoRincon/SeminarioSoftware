# Button

<!-- tags: ElevatedButton, onPressed, el botón sale gris, OutlinedButton, TextButton, IconButton, botón deshabilitado, onPressed null, child de un botón, función anónima -->

Un botón es la forma más directa de que una persona le pida algo a tu app. Flutter trae varios, pero todos se arman con las mismas dos piezas.

## onPressed y child

```svg
<svg id="btAnatomia" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 436" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="btAnatomia-ttl btAnatomia-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="btAnatomia-ttl">Las dos partes de un botón</title>
  <desc id="btAnatomia-dsc">Un ElevatedButton con onPressed, una función que imprime Guardado, y child, un Text que dice Guardar. A la derecha el botón dibujado y la consola con el mensaje que aparece al tocarlo.</desc>
  <defs>
    <style>
      #btAnatomia .title{fill:#161A26;font-size:22px;font-weight:700}
      #btAnatomia .sub{fill:#79809A;font-size:13.5px}
      #btAnatomia .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #btAnatomia .cl{font-size:13px;fill:#C9CFDA}
      #btAnatomia .s{fill:#A8D8A0} #btAnatomia .n{fill:#F2B880} #btAnatomia .c{fill:#7FD1E8}
      #btAnatomia .p{fill:#D5B8F5} #btAnatomia .k{fill:#F08FB0}
      #btAnatomia .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #btAnatomia .ct{fill:#161A26;font-size:14px;font-weight:700}
      #btAnatomia .cb{fill:#454C61;font-size:13px}
      #btAnatomia .rt{fill:#161A26;font-size:14px} #btAnatomia .rs{fill:#79809A;font-size:12px}
      #btAnatomia .foot{fill:#79809A;font-size:12px}
      #btAnatomia .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #btAnatomia .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #btAnatomia .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#btAnatomia-ar-amber)}
      #btAnatomia .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #btAnatomia .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #btAnatomia .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#btAnatomia-ar-indigo)}
    </style>
    <marker id="btAnatomia-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="btAnatomia-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
  </defs>
  <rect width="960" height="436" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las dos partes de un botón</text>
  <text class="sub" x="48" y="80" data-fit="860">Un botón siempre responde dos preguntas: qué muestra y qué hace cuando lo tocan.</text>
  <rect x="48" y="112" width="456" height="292" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/main.dart</text>
  <rect x="552" y="112" width="360" height="292" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="79.6" y="180" width="78.2" height="22" rx="5"/>
  <rect class="hl-indigo" x="79.6" y="252" width="179.6" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="117.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">ElevatedButton</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="117.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">onPressed</tspan>: () {</text>
  <text class="cl mono" font-size="13" x="99.2" y="220" textLength="140.4" lengthAdjust="spacingAndGlyphs" data-fit="432">print(<tspan class="s">'Guardado'</tspan>);</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">},</text>
  <text class="cl mono" font-size="13" x="83.6" y="268" textLength="179.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Text</tspan>(<tspan class="s">'Guardar'</tspan>),</text>
  <text class="cl mono" font-size="13" x="68.0" y="292" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<text x="24" y="28" font-size="12" font-weight="700" fill="#79809A" letter-spacing=".06em">LO QUE HACE AL TOCARLO</text><rect x="24" y="40" width="312" height="56" rx="8" fill="#1F2430"/><text x="40" y="60" font-size="11.5" fill="#8A93A6" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">Consola</text><text x="40" y="82" font-size="13" fill="#C9CFDA" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">Guardado</text><text x="24" y="150" font-size="12" font-weight="700" fill="#79809A" letter-spacing=".06em">LO QUE MUESTRA</text><rect x="112" y="170" width="136" height="44" rx="22" fill="#0B1020" fill-opacity=".10"/><rect x="112" y="166" width="136" height="44" rx="22" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="180" y="188" dy="0.35em" text-anchor="middle" font-size="15" font-weight="600" fill="#4453C9">Guardar</text>
  </g>
  <path class="ld-amber" d="M206.6,191 H504"/>
  <path class="ar-amber" d="M504,191 H523 V212 H576"/>
  <path class="ld-indigo" d="M269.0,263 H504"/>
  <path class="ar-indigo" d="M504,263 H514 V332 H660"/>
</svg>
```

```dart
ElevatedButton(
  onPressed: () {
    print('Guardado');
  },
  child: Text('Guardar'),
)
```

- **`child`** es lo que el botón muestra. Es un widget cualquiera, y casi siempre un `Text`.
- **`onPressed`** es lo que el botón hace. Recibe una **función**: el código entre `{ }` no se ejecuta cuando la pantalla se dibuja, sino cada vez que alguien toca el botón.

La forma `() { ... }` es una función sin nombre. Los paréntesis vacíos dicen que no recibe datos, y las llaves encierran lo que hace. Si necesitas repasarlas, están en *Métodos en Dart*.

El `print` escribe en la consola desde donde ejecutaste la app, no en la pantalla. Es suficiente para comprobar que el botón responde. El editor lo subraya con el aviso `Don't invoke 'print' in production code`: es una recomendación, no un error, y aquí se puede ignorar. Hacer que un toque **cambie la pantalla** exige estado, y eso es la sesión 6.

## Los cuatro botones

Se escriben igual. Lo que cambia es cuánto resaltan, y eso le dice a la persona cuál es la acción importante:

```svg
<svg id="btTipos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 468" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="btTipos-ttl btTipos-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="btTipos-ttl">Los cuatro botones de siempre</title>
  <desc id="btTipos-dsc">Los cuatro botones básicos de Flutter y su aspecto: ElevatedButton, OutlinedButton, TextButton e IconButton, en estado normal y deshabilitados con onPressed null.</desc>
  <defs>
    <style>
      #btTipos .title{fill:#161A26;font-size:22px;font-weight:700}
      #btTipos .sub{fill:#79809A;font-size:13.5px}
      #btTipos .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #btTipos .nt{font-size:15px;font-weight:700;fill:#161A26}
      #btTipos .nb{fill:#454C61;font-size:13px}
      #btTipos .lbl{fill:#556074;font-size:12px;font-weight:600}
      #btTipos .foot{fill:#79809A;font-size:12px}
      #btTipos .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #btTipos .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#btTipos-arrow)}
    </style>
    <marker id="btTipos-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="468" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Los cuatro botones de siempre</text>
  <text class="sub" x="48" y="80" data-fit="860">Se escriben igual. Lo que cambia es cuánto llaman la atención.</text>
  <text class="h" x="48" y="124">CON UNA FUNCIÓN EN onPressed</text>
  <text class="h" x="48" y="316">CON onPressed: null · DESHABILITADO</text>
  <g transform="translate(48,140)">
    <rect width="192" height="136" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <g transform="translate(0,6)"><rect x="36" y="14" width="120" height="40" rx="20" fill="#0B1020" fill-opacity=".10"/><rect x="36" y="10" width="120" height="40" rx="20" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="96" y="30" dy="0.35em" text-anchor="middle" font-size="14.5" font-weight="600" fill="#4453C9">Guardar</text></g>
    <text class="mono" x="96" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#161A26" data-fit="176">ElevatedButton</text>
    <text class="nb" x="96" y="106" text-anchor="middle" data-fit="176">La acción principal</text>
    <text class="nb" x="96" y="124" text-anchor="middle" data-fit="176">de la pantalla</text>
  </g>
  <g transform="translate(48,332)">
    <rect width="192" height="64" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <g transform="translate(0,2)"><rect x="36" y="10" width="120" height="40" rx="20" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.5"/><text x="96" y="30" dy="0.35em" text-anchor="middle" font-size="14.5" font-weight="600" fill="#A0A8B8">Guardar</text></g>
  </g>
  <g transform="translate(272,140)">
    <rect width="192" height="136" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <g transform="translate(0,6)"><rect x="36" y="10" width="120" height="40" rx="20" fill="none" stroke="#79809A" stroke-width="1.5"/><text x="96" y="30" dy="0.35em" text-anchor="middle" font-size="14.5" font-weight="600" fill="#4453C9">Guardar</text></g>
    <text class="mono" x="96" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#161A26" data-fit="176">OutlinedButton</text>
    <text class="nb" x="96" y="106" text-anchor="middle" data-fit="176">Una acción secundaria</text>
    <text class="nb" x="96" y="124" text-anchor="middle" data-fit="176">que debe verse</text>
  </g>
  <g transform="translate(272,332)">
    <rect width="192" height="64" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <g transform="translate(0,2)"><rect x="36" y="10" width="120" height="40" rx="20" fill="none" stroke="#D9DEE8" stroke-width="1.5"/><text x="96" y="30" dy="0.35em" text-anchor="middle" font-size="14.5" font-weight="600" fill="#A0A8B8">Guardar</text></g>
  </g>
  <g transform="translate(496,140)">
    <rect width="192" height="136" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <g transform="translate(0,6)"><text x="96" y="30" dy="0.35em" text-anchor="middle" font-size="14.5" font-weight="600" fill="#4453C9">Guardar</text></g>
    <text class="mono" x="96" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#161A26" data-fit="176">TextButton</text>
    <text class="nb" x="96" y="106" text-anchor="middle" data-fit="176">Acciones discretas:</text>
    <text class="nb" x="96" y="124" text-anchor="middle" data-fit="176">cancelar, ver más</text>
  </g>
  <g transform="translate(496,332)">
    <rect width="192" height="64" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <g transform="translate(0,2)"><text x="96" y="30" dy="0.35em" text-anchor="middle" font-size="14.5" font-weight="600" fill="#A0A8B8">Guardar</text></g>
  </g>
  <g transform="translate(720,140)">
    <rect width="192" height="136" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <g transform="translate(0,6)"><path d="M96,26 c-5,-9 -18,-4 -14,6 c2,6 9,10 14,14 c5,-4 12,-8 14,-14 c4,-10 -9,-15 -14,-6 Z" fill="#C2354F"/></g>
    <text class="mono" x="96" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#161A26" data-fit="176">IconButton</text>
    <text class="nb" x="96" y="106" text-anchor="middle" data-fit="176">Una acción que se</text>
    <text class="nb" x="96" y="124" text-anchor="middle" data-fit="176">entiende con un icono</text>
  </g>
  <g transform="translate(720,332)">
    <rect width="192" height="64" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <g transform="translate(0,2)"><path d="M96,26 c-5,-9 -18,-4 -14,6 c2,6 9,10 14,14 c5,-4 12,-8 14,-14 c4,-10 -9,-15 -14,-6 Z" fill="#C4CBD8"/></g>
  </g>
  <text class="foot" x="48" y="440" data-fit="860">Un botón sin función se pinta gris y no responde. Flutter lo hace solo: no hay una propiedad «enabled».</text>
</svg>
```

```dart
ElevatedButton(
  onPressed: () {
    print('Guardado');
  },
  child: Text('Guardar'),
)
```

```dart
OutlinedButton(
  onPressed: () {
    print('Detalles');
  },
  child: Text('Ver detalles'),
)
```

```dart
TextButton(
  onPressed: () {
    print('Cancelado');
  },
  child: Text('Cancelar'),
)
```

`IconButton` es el único distinto: no tiene `child` sino `icon`.

```dart
IconButton(
  onPressed: () {
    print('Me gusta');
  },
  icon: Icon(Icons.favorite),
  color: Colors.red,
  iconSize: 32,
)
```

Los iconos salen de la clase `Icons`, que trae cientos: `Icons.favorite`, `Icons.settings`, `Icons.add`, `Icons.delete`. El autocompletado del editor te los muestra al escribir `Icons.`.

Una regla de diseño sencilla: **un solo `ElevatedButton` por pantalla**, para la acción principal. Si todo resalta, nada resalta.

## Un botón deshabilitado

No existe una propiedad `enabled`. Un botón se deshabilita entregándole `null` en lugar de una función:

```dart
ElevatedButton(
  onPressed: null,
  child: Text('Guardar'),
)
```

Flutter lo pinta gris y deja de responder. Por eso, si un botón te sale gris sin que lo hayas pedido, revisa su `onPressed`: lo más probable es que esté recibiendo `null`.

`onPressed` es obligatorio. Si lo omites, el código no compila.

## Ejemplo completo

Los cuatro tipos y la variante con icono y texto (`ElevatedButton.icon`):

```dart trycode=34399fb97053ae4160c3d796847add65
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Ejemplo Botones',
      home: Scaffold(
        appBar: AppBar(title: const Text('Widgets Button')),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              ElevatedButton(
                onPressed: () {
                  print('ElevatedButton presionado!');
                },
                child: const Text('Botón Elevado'),
              ),
              const SizedBox(height: 20),
              TextButton(
                onPressed: () {
                  print('TextButton presionado!');
                },
                child: const Text('Botón de Texto'),
              ),
              const SizedBox(height: 20),
              OutlinedButton(
                onPressed: () {
                  print('OutlinedButton presionado!');
                },
                child: const Text('Botón con Borde'),
              ),
              const SizedBox(height: 20),
              IconButton(
                icon: const Icon(Icons.settings),
                onPressed: () {
                  print('IconButton presionado!');
                },
                color: Colors.blue,
                iconSize: 40.0,
              ),
              const SizedBox(height: 20),
              ElevatedButton.icon(
                onPressed: () {
                  print('ElevatedButton.icon presionado!');
                },
                icon: const Icon(Icons.add),
                label: const Text('Añadir'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

Este ejemplo viene de Aplicaciones Móviles y arranca con `home:` en lugar de la tabla de rutas. Sirve para experimentar en el navegador; en tu proyecto sigue usando tu `main.dart`.
