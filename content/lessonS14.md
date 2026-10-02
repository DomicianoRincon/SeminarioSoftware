# TextField

<!-- tags: TextField, InputDecoration, labelText y hintText, campo de contraseña, obscureText, keyboardType, OutlineInputBorder, prefixIcon, No Material widget found, teclado numérico -->

`TextField` es el campo donde una persona escribe: un correo, una contraseña, una búsqueda. En esta lección aprendes a **dibujarlo** como lo pide un diseño. Leer lo que la persona escribió necesita estado, y se ve en la sesión 6.

## Uso básico

Un campo sin nada más es una línea sobre la que se puede escribir:

```dart
TextField()
```

Funciona, pero nadie sabe qué debe escribir ahí. Casi todo el trabajo con un `TextField` es decorarlo.

Si al probarlo aparece `No Material widget found`, el campo quedó fuera de un `Scaffold`. Ponlo dentro del `body` de tu `HomeScreen`.

## InputDecoration

Igual que `Text` agrupa su aspecto en `TextStyle`, `TextField` agrupa el suyo en un objeto `InputDecoration`, que se entrega en `decoration`:

```svg
<svg id="tfAnatomia" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tfAnatomia-ttl tfAnatomia-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tfAnatomia-ttl">Las partes de un TextField</title>
  <desc id="tfAnatomia-dsc">Un TextField con InputDecoration: labelText Correo, hintText con un correo de ejemplo, prefixIcon con un sobre y border OutlineInputBorder. A la derecha el campo dibujado, con cada parte señalada.</desc>
  <defs>
    <style>
      #tfAnatomia .title{fill:#161A26;font-size:22px;font-weight:700}
      #tfAnatomia .sub{fill:#79809A;font-size:13.5px}
      #tfAnatomia .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tfAnatomia .cl{font-size:13px;fill:#C9CFDA}
      #tfAnatomia .s{fill:#A8D8A0} #tfAnatomia .n{fill:#F2B880} #tfAnatomia .c{fill:#7FD1E8}
      #tfAnatomia .p{fill:#D5B8F5} #tfAnatomia .k{fill:#F08FB0}
      #tfAnatomia .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tfAnatomia .ct{fill:#161A26;font-size:14px;font-weight:700}
      #tfAnatomia .cb{fill:#454C61;font-size:13px}
      #tfAnatomia .rt{fill:#161A26;font-size:14px} #tfAnatomia .rs{fill:#79809A;font-size:12px}
      #tfAnatomia .foot{fill:#79809A;font-size:12px}
      #tfAnatomia .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #tfAnatomia .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #tfAnatomia .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#tfAnatomia-ar-amber)}
      #tfAnatomia .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #tfAnatomia .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #tfAnatomia .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#tfAnatomia-ar-green)}
      #tfAnatomia .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #tfAnatomia .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #tfAnatomia .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#tfAnatomia-ar-indigo)}
      #tfAnatomia .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #tfAnatomia .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #tfAnatomia .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#tfAnatomia-ar-violet)}
    </style>
    <marker id="tfAnatomia-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="tfAnatomia-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="tfAnatomia-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="tfAnatomia-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="480" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las partes de un <tspan class="mono">TextField</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">El campo en sí no tiene propiedades de aspecto. Todo lo que se ve va en decoration.</text>
  <rect x="48" y="112" width="456" height="336" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/main.dart</text>
  <rect x="552" y="112" width="360" height="336" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="95.2" y="204" width="156.2" height="22" rx="5"/>
  <rect class="hl-amber" x="95.2" y="228" width="249.8" height="22" rx="5"/>
  <rect class="hl-green" x="95.2" y="252" width="226.4" height="22" rx="5"/>
  <rect class="hl-violet" x="95.2" y="276" width="226.4" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="78.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">TextField</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="218.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">decoration</tspan>: <tspan class="c">InputDecoration</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="220" textLength="156.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">labelText</tspan>: <tspan class="s">'Correo'</tspan>,</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="249.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">hintText</tspan>: <tspan class="s">'nombre@icesi.edu.co'</tspan>,</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="226.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">prefixIcon</tspan>: <tspan class="c">Icon</tspan>(<tspan class="c">Icons</tspan>.mail),</text>
  <text class="cl mono" font-size="13" x="99.2" y="292" textLength="226.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">border</tspan>: <tspan class="c">OutlineInputBorder</tspan>(),</text>
  <text class="cl mono" font-size="13" x="83.6" y="316" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="68.0" y="340" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<rect x="56" y="180" width="280" height="56" rx="6" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><rect x="68" y="172" width="56" height="16" fill="#FFFFFF"/><text x="74" y="180" dy="0.35em" font-size="12.5" font-weight="600" fill="#4453C9">Correo</text><g transform="translate(82,208)"><rect x="-9" y="-7" width="18" height="14" rx="2" fill="none" stroke="#556074" stroke-width="1.75"/><path d="M-9,-6 L0,1 L9,-6" fill="none" stroke="#556074" stroke-width="1.75"/></g><path d="M104,198 V218" stroke="#4453C9" stroke-width="1.5"/><text x="110" y="208" dy="0.35em" font-size="15" fill="#A0A8B8">nombre@icesi.edu.co</text><text x="196" y="296" text-anchor="middle" font-size="12" fill="#79809A" data-fit="300">Así se ve al tocarlo, antes de escribir.</text>
  </g>
  <path class="ld-indigo" d="M261.2,215 H504"/>
  <path class="ar-indigo" d="M504,215 H648 V312"/>
  <path class="ld-amber" d="M354.8,239 H504"/>
  <path class="ar-amber" d="M504,239 H532 V420 H722 V364 H722"/>
  <path class="ld-green" d="M331.4,263 H504"/>
  <path class="ar-green" d="M504,263 H523 V408 H634 V366 H634"/>
  <path class="ld-violet" d="M331.4,287 H504"/>
  <path class="ar-violet" d="M504,287 H514 V370 H604"/>
</svg>
```

```dart
TextField(
  decoration: InputDecoration(
    labelText: 'Correo',
    hintText: 'nombre@icesi.edu.co',
    prefixIcon: Icon(Icons.mail),
    border: OutlineInputBorder(),
  ),
)
```

| Propiedad | Qué muestra |
|---|---|
| `labelText` | El nombre del campo. Está adentro mientras el campo está vacío y sube al borde cuando se toca |
| `hintText` | Un ejemplo de lo que se espera. Desaparece al escribir la primera letra |
| `helperText` | Una ayuda fija debajo del campo |
| `prefixIcon` | Un icono al inicio |
| `suffixIcon` | Un icono al final |
| `border` | El borde. `OutlineInputBorder()` dibuja la caja completa; sin esta propiedad queda solo la línea de abajo |

`labelText` y `hintText` se confunden mucho. El primero dice **qué es** el campo y siempre queda visible; el segundo es un **ejemplo** y se va en cuanto hay texto.

Un `TextField` ocupa todo el ancho que tenga disponible. Para que no llegue hasta los bordes de la pantalla, envuélvelo en un `Padding`:

```dart
Padding(
  padding: EdgeInsets.all(24),
  child: TextField(
    decoration: InputDecoration(
      labelText: 'Correo',
      border: OutlineInputBorder(),
    ),
  ),
)
```

## Contraseña y teclado

Estas dos propiedades van **en el `TextField`**, no en la decoración, porque no cambian cómo se ve el campo sino cómo se escribe en él:

```svg
<svg id="tfTipos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 548" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tfTipos-ttl tfTipos-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tfTipos-ttl">Contraseñas y teclados</title>
  <desc id="tfTipos-dsc">Dos TextField. El primero, con obscureText true, muestra puntos en lugar de la contraseña. El segundo, con keyboardType TextInputType.number, abre el teclado numérico.</desc>
  <defs>
    <style>
      #tfTipos .title{fill:#161A26;font-size:22px;font-weight:700}
      #tfTipos .sub{fill:#79809A;font-size:13.5px}
      #tfTipos .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tfTipos .cl{font-size:13px;fill:#C9CFDA}
      #tfTipos .s{fill:#A8D8A0} #tfTipos .n{fill:#F2B880} #tfTipos .c{fill:#7FD1E8}
      #tfTipos .p{fill:#D5B8F5} #tfTipos .k{fill:#F08FB0}
      #tfTipos .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tfTipos .ct{fill:#161A26;font-size:14px;font-weight:700}
      #tfTipos .cb{fill:#454C61;font-size:13px}
      #tfTipos .rt{fill:#161A26;font-size:14px} #tfTipos .rs{fill:#79809A;font-size:12px}
      #tfTipos .foot{fill:#79809A;font-size:12px}
      #tfTipos .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #tfTipos .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #tfTipos .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#tfTipos-ar-green)}
      #tfTipos .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #tfTipos .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #tfTipos .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#tfTipos-ar-violet)}
    </style>
    <marker id="tfTipos-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="tfTipos-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="548" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Contraseñas y teclados</text>
  <text class="sub" x="48" y="80" data-fit="860">Estas dos sí son propiedades del campo, no de la decoración: cambian cómo se escribe.</text>
  <rect x="48" y="112" width="456" height="404" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/main.dart</text>
  <rect x="552" y="112" width="360" height="404" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-violet" x="79.6" y="180" width="140.6" height="22" rx="5"/>
  <rect class="hl-green" x="79.6" y="324" width="273.2" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="78.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">TextField</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="140.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">obscureText</tspan>: <tspan class="k">true</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="218.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">decoration</tspan>: <tspan class="c">InputDecoration</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="187.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">labelText</tspan>: <tspan class="s">'Contraseña'</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="268" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="68.0" y="292" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="68.0" y="316" textLength="78.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">TextField</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="340" textLength="273.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">keyboardType</tspan>: <tspan class="c">TextInputType</tspan>.number,</text>
  <text class="cl mono" font-size="13" x="83.6" y="364" textLength="218.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">decoration</tspan>: <tspan class="c">InputDecoration</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="388" textLength="140.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">labelText</tspan>: <tspan class="s">'Edad'</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="412" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="68.0" y="436" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <g transform="translate(552,144)">
<text x="64" y="30" font-size="12" fill="#79809A">Contraseña</text><text x="64" y="56" font-size="20" fill="#161A26" letter-spacing="3">••••••••</text><path d="M64,68 H296" stroke="#79809A" stroke-width="1.5"/><text x="64" y="150" font-size="12" fill="#79809A">Edad</text><text x="64" y="174" font-size="16" fill="#161A26">21</text><path d="M64,186 H296" stroke="#4453C9" stroke-width="2"/><rect x="96" y="212" width="168" height="124" rx="10" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><rect x="106" y="220" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/><text x="128" y="231" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">1</text><rect x="158" y="220" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/><text x="180" y="231" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">2</text><rect x="210" y="220" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/><text x="232" y="231" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">3</text><rect x="106" y="248" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/><text x="128" y="259" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">4</text><rect x="158" y="248" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/><text x="180" y="259" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">5</text><rect x="210" y="248" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/><text x="232" y="259" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">6</text><rect x="106" y="276" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/><text x="128" y="287" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">7</text><rect x="158" y="276" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/><text x="180" y="287" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">8</text><rect x="210" y="276" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/><text x="232" y="287" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">9</text><rect x="158" y="304" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/><text x="180" y="315" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">0</text><rect x="210" y="304" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/><text x="232" y="315" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">⌫</text>
  </g>
  <path class="ld-violet" d="M230.0,191 H504"/>
  <path class="ar-violet" d="M504,191 H514 V193 H610"/>
  <path class="ld-green" d="M362.6,335 H504"/>
  <path class="ar-green" d="M504,335 H514 V335 H592 V418 H644"/>
</svg>
```

```dart
TextField(
  obscureText: true,
  decoration: InputDecoration(
    labelText: 'Contraseña',
  ),
)
```

```dart
TextField(
  keyboardType: TextInputType.number,
  decoration: InputDecoration(
    labelText: 'Edad',
  ),
)
```

- **`obscureText: true`** reemplaza cada letra por un punto.
- **`keyboardType`** elige el teclado que abre el celular: `TextInputType.number` para números, `TextInputType.emailAddress` para uno con la `@` a la mano, `TextInputType.phone` para un teléfono.

`keyboardType` solo se nota en un celular o en un emulador. En Chrome escribes con el teclado del computador y no verás diferencia.

## Lo que viene

Con lo de esta lección puedes dejar un formulario con el aspecto exacto del diseño, y eso es lo que pide la sesión de hoy. Todavía no puedes **usar** lo que la persona escribe.

Para leer el texto hace falta un `TextEditingController`, y ese controlador tiene que vivir en un widget **con estado**. Los dos temas son de la sesión 6. Hasta entonces, tus campos se ven y se dejan escribir, pero la app no hace nada con el contenido.

## Ejemplo completo

Un formulario con los tres campos de la lección: correo, contraseña y edad. Se ve y se deja escribir, pero todavía no hace nada con el contenido.

```dart trycode=6345d42fcb71475a4ada85c94c8ddd07
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
      appBar: AppBar(title: const Text('Formulario')),
      body: const Padding(
        padding: EdgeInsets.all(24),
        child: Column(
          children: [
            TextField(
              decoration: InputDecoration(
                labelText: 'Correo',
                hintText: 'nombre@icesi.edu.co',
                prefixIcon: Icon(Icons.mail),
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 16),
            TextField(
              obscureText: true,
              decoration: InputDecoration(
                labelText: 'Contraseña',
                prefixIcon: Icon(Icons.lock),
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 16),
            TextField(
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: 'Edad',
                helperText: 'En años cumplidos',
                border: OutlineInputBorder(),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

Aquí `App` y `HomeScreen` van en un solo archivo porque el editor en línea solo tiene uno; en tu proyecto siguen separados.
