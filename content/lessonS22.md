# Container y Padding

<!-- tags: Padding, EdgeInsets, Container, BoxDecoration, margin y padding, borderRadius, contenido pegado al borde, both a color and a decoration, clipBehavior, esquinas redondeadas en una imagen, tarjeta con borde -->

Si pones tus componentes directamente en el `body`, quedan pegados al borde de la pantalla y unos a otros. Falta aire. Estos dos widgets lo ponen: `Padding` solo separa, y `Container` además dibuja una caja.

## Padding

```svg
<svg id="cpPadding" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 432" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="cpPadding-ttl cpPadding-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="cpPadding-ttl">Padding: aire alrededor de un widget</title>
  <desc id="cpPadding-dsc">Un Padding con EdgeInsets.all(16) y un Text como child. En el resultado, el texto queda separado 16 píxeles de cada borde del espacio que le dieron.</desc>
  <defs>
    <style>
      #cpPadding .title{fill:#161A26;font-size:22px;font-weight:700}
      #cpPadding .sub{fill:#79809A;font-size:13.5px}
      #cpPadding .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #cpPadding .cl{font-size:13px;fill:#C9CFDA}
      #cpPadding .s{fill:#A8D8A0} #cpPadding .n{fill:#F2B880} #cpPadding .c{fill:#7FD1E8}
      #cpPadding .p{fill:#D5B8F5} #cpPadding .k{fill:#F08FB0}
      #cpPadding .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #cpPadding .ct{fill:#161A26;font-size:14px;font-weight:700}
      #cpPadding .cb{fill:#454C61;font-size:13px}
      #cpPadding .rt{fill:#161A26;font-size:14px} #cpPadding .rs{fill:#79809A;font-size:12px}
      #cpPadding .foot{fill:#79809A;font-size:12px}
      #cpPadding .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #cpPadding .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #cpPadding .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#cpPadding-ar-amber)}
      #cpPadding .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #cpPadding .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #cpPadding .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#cpPadding-ar-indigo)}
    </style>
    <marker id="cpPadding-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="cpPadding-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
  </defs>
  <rect width="960" height="432" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56"><tspan class="mono">Padding</tspan>: aire alrededor de un widget</text>
  <text class="sub" x="48" y="80" data-fit="860">Envuelve a un widget y lo separa de lo que tiene alrededor. No se ve: solo ocupa espacio.</text>
  <rect x="48" y="112" width="456" height="288" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/profile_screen.dart</text>
  <rect x="552" y="112" width="360" height="288" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="79.6" y="180" width="62.6" height="22" rx="5"/>
  <rect class="hl-indigo" x="79.6" y="204" width="47.0" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="62.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Padding</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="218.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">padding</tspan>: <tspan class="c">EdgeInsets</tspan>.all(<tspan class="n">16</tspan>),</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="265.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Text</tspan>(<tspan class="s">'Mariana Valenzuela'</tspan>),</text>
  <text class="cl mono" font-size="13" x="68.0" y="244" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<rect x="40" y="36" width="280" height="150" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5" stroke-dasharray="5 4"/><rect x="72" y="68" width="216" height="86" rx="6" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="180.0" y="111.0" dy="0.35em" text-anchor="middle" font-size="13" font-weight="600" fill="#4453C9">Mariana Valenzuela</text><path d="M56,36 L56,68 M52,36 H60 M52,68 H60" stroke="#A96C05" stroke-width="1.5" fill="none"/><text x="64" y="52.0" dy="0.35em" font-size="12" font-weight="700" fill="#A96C05" text-anchor="start">16</text><path d="M288,200 L320,200 M288,196 V204 M320,196 V204" stroke="#A96C05" stroke-width="1.5" fill="none"/><text x="304.0" y="193" dy="0.35em" font-size="12" font-weight="700" fill="#A96C05" text-anchor="middle">16</text><text x="180" y="232" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="300">La zona amarilla es el padding.</text>
  </g>
  <path class="ld-amber" d="M308.0,191 H504"/>
  <path class="ar-amber" d="M504,191 H592"/>
  <path class="ld-indigo" d="M354.8,215 H504"/>
  <path class="ar-indigo" d="M504,215 H523 V274 H624"/>
</svg>
```

```dart
Padding(
  padding: EdgeInsets.all(16),
  child: Text('Mariana Valenzuela'),
)
```

`Padding` envuelve a un widget y le deja espacio alrededor. No dibuja nada.

Ya conoces `SizedBox` para separar los hijos de una `Column`. La diferencia es de lugar: `SizedBox` va **entre** dos widgets, y `Padding` va **alrededor** de uno. Para separar todo el contenido del borde de la pantalla, un solo `Padding` envuelve la `Column` completa.

## Cuánto aire

El espacio se describe con `EdgeInsets`, y hay tres formas de escribirlo:

```svg
<svg id="cpInsets" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 408" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="cpInsets-ttl cpInsets-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="cpInsets-ttl">Tres formas de decir cuánto aire</title>
  <desc id="cpInsets-dsc">Tres cajas. En la primera, EdgeInsets.all(16) deja el mismo espacio por los cuatro lados. En la segunda, EdgeInsets.symmetric deja 24 a los lados y 8 arriba y abajo. En la tercera, EdgeInsets.only deja espacio solo arriba.</desc>
  <defs>
    <style>
      #cpInsets .title{fill:#161A26;font-size:22px;font-weight:700}
      #cpInsets .sub{fill:#79809A;font-size:13.5px}
      #cpInsets .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #cpInsets .nt{font-size:15px;font-weight:700;fill:#161A26}
      #cpInsets .nb{fill:#454C61;font-size:13px}
      #cpInsets .lbl{fill:#556074;font-size:12px;font-weight:600}
      #cpInsets .foot{fill:#79809A;font-size:12px}
      #cpInsets .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #cpInsets .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#cpInsets-arrow)}
    </style>
    <marker id="cpInsets-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="408" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Tres formas de decir cuánto aire</text>
  <text class="sub" x="48" y="80" data-fit="860">EdgeInsets dice cuántos píxeles dejar en cada lado. Se elige el constructor según qué lados sean iguales.</text>
  <rect x="48" y="128" width="272" height="152" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5" stroke-dasharray="5 4"/><rect x="72" y="152" width="224" height="104" rx="6" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="184.0" y="204.0" dy="0.35em" text-anchor="middle" font-size="13" font-weight="600" fill="#4453C9">child</text>
  <text x="48" y="316" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="272">EdgeInsets.all(16)</text>
  <text x="48" y="342" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="272">Lo mismo por los cuatro lados</text>
  <rect x="344" y="128" width="272" height="152" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5" stroke-dasharray="5 4"/><rect x="380" y="140" width="200" height="128" rx="6" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="480.0" y="204.0" dy="0.35em" text-anchor="middle" font-size="13" font-weight="600" fill="#4453C9">child</text>
  <text x="344" y="316" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="272">EdgeInsets.symmetric(</text>
  <text xml:space="preserve" x="344" y="336" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="272">  horizontal: 24, vertical: 8)</text>
  <text x="344" y="362" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="272">Unos lados y otros, por parejas</text>
  <rect x="640" y="128" width="272" height="152" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5" stroke-dasharray="5 4"/><rect x="640" y="164" width="272" height="116" rx="6" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="776.0" y="222.0" dy="0.35em" text-anchor="middle" font-size="13" font-weight="600" fill="#4453C9">child</text>
  <text x="640" y="316" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="272">EdgeInsets.only(top: 24)</text>
  <text x="640" y="342" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="272">Solo los lados que nombres</text>
</svg>
```

En `only` puedes nombrar `left`, `top`, `right` y `bottom`, los que necesites. Igual que con `SizedBox`, usa pocos valores y repítelos: `8`, `16` y `24` alcanzan para casi todo.

## Container

En el taller usaste un `Container` para darle fondo y borde a `StatCard`. Ahora sí, parte por parte:

```svg
<svg id="cpContainer" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="cpContainer-ttl cpContainer-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="cpContainer-ttl">Container: una caja que se ve</title>
  <desc id="cpContainer-dsc">Un Container con padding y un BoxDecoration con color blanco, borde índigo y esquinas redondeadas, y un Text como child. En el resultado, una tarjeta blanca con borde y esquinas redondas, con el texto separado del borde.</desc>
  <defs>
    <style>
      #cpContainer .title{fill:#161A26;font-size:22px;font-weight:700}
      #cpContainer .sub{fill:#79809A;font-size:13.5px}
      #cpContainer .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #cpContainer .cl{font-size:13px;fill:#C9CFDA}
      #cpContainer .s{fill:#A8D8A0} #cpContainer .n{fill:#F2B880} #cpContainer .c{fill:#7FD1E8}
      #cpContainer .p{fill:#D5B8F5} #cpContainer .k{fill:#F08FB0}
      #cpContainer .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #cpContainer .ct{fill:#161A26;font-size:14px;font-weight:700}
      #cpContainer .cb{fill:#454C61;font-size:13px}
      #cpContainer .rt{fill:#161A26;font-size:14px} #cpContainer .rs{fill:#79809A;font-size:12px}
      #cpContainer .foot{fill:#79809A;font-size:12px}
      #cpContainer .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #cpContainer .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #cpContainer .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#cpContainer-ar-amber)}
      #cpContainer .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #cpContainer .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #cpContainer .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#cpContainer-ar-green)}
      #cpContainer .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #cpContainer .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #cpContainer .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#cpContainer-ar-indigo)}
      #cpContainer .hl-rose{fill:#F3A3B2;fill-opacity:.16;stroke:#F3A3B2;stroke-width:1.5}
      #cpContainer .ld-rose{fill:none;stroke:#F3A3B2;stroke-width:1.5;stroke-dasharray:3 4}
      #cpContainer .ar-rose{fill:none;stroke:#C2354F;stroke-width:1.75;marker-end:url(#cpContainer-ar-rose)}
    </style>
    <marker id="cpContainer-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="cpContainer-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="cpContainer-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="cpContainer-ar-rose" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/></marker>
  </defs>
  <rect width="960" height="480" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56"><tspan class="mono">Container</tspan>: una caja que se ve</text>
  <text class="sub" x="48" y="80" data-fit="860">Hace lo mismo que Padding y además pinta: fondo, borde y esquinas van en decoration.</text>
  <rect x="48" y="112" width="456" height="336" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/profile_screen.dart</text>
  <rect x="552" y="112" width="360" height="336" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="79.6" y="180" width="62.6" height="22" rx="5"/>
  <rect class="hl-green" x="95.2" y="228" width="47.0" height="22" rx="5"/>
  <rect class="hl-indigo" x="95.2" y="252" width="54.8" height="22" rx="5"/>
  <rect class="hl-rose" x="95.2" y="276" width="101.6" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="78.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Container</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="218.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">padding</tspan>: <tspan class="c">EdgeInsets</tspan>.all(<tspan class="n">16</tspan>),</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="202.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">decoration</tspan>: <tspan class="c">BoxDecoration</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="156.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">color</tspan>: <tspan class="c">Colors</tspan>.white,</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="319.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">border</tspan>: <tspan class="c">Border</tspan>.all(<tspan class="p">color</tspan>: <tspan class="c">Colors</tspan>.indigo),</text>
  <text class="cl mono" font-size="13" x="99.2" y="292" textLength="312.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">borderRadius</tspan>: <tspan class="c">BorderRadius</tspan>.circular(<tspan class="n">16</tspan>),</text>
  <text class="cl mono" font-size="13" x="83.6" y="316" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="83.6" y="340" textLength="265.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Text</tspan>(<tspan class="s">'Mariana Valenzuela'</tspan>),</text>
  <text class="cl mono" font-size="13" x="68.0" y="364" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<rect x="24" y="84" width="312" height="180" rx="8" fill="#EEF0F4"/><rect x="60" y="120" width="240" height="100" rx="18" fill="#FFFFFF" stroke="#4453C9" stroke-width="2.5"/><text x="180" y="175" font-size="15" font-weight="600" fill="#161A26" text-anchor="middle">Mariana Valenzuela</text>
  </g>
  <path class="ld-amber" d="M308.0,191 H504"/>
  <path class="ar-amber" d="M504,191 H792 V268"/>
  <path class="ld-green" d="M261.2,239 H504"/>
  <path class="ar-green" d="M504,239 H532 V284 H656"/>
  <path class="ld-indigo" d="M425.0,263 H504"/>
  <path class="ar-indigo" d="M504,263 H523 V334 H612"/>
  <path class="ld-rose" d="M417.2,287 H504"/>
  <path class="ar-rose" d="M504,287 H514 V388 H622 V364 H622"/>
</svg>
```

```dart
Container(
  padding: EdgeInsets.all(16),
  decoration: BoxDecoration(
    color: Colors.white,
    border: Border.all(color: Colors.indigo),
    borderRadius: BorderRadius.circular(16),
  ),
  child: Text('Mariana Valenzuela'),
)
```

Todo lo que se pinta va dentro de `decoration`, en un `BoxDecoration`. `Container` también acepta `color` por fuera, como atajo para una caja de un solo color, pero no los dos a la vez: si usas `decoration`, el color va adentro. Si lo dejas en los dos lugares, la app falla con `Cannot provide both a color and a decoration`.

## Las capas de un Container

```svg
<svg id="cpCaja" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 440" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="cpCaja-ttl cpCaja-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="cpCaja-ttl">Las capas de un Container</title>
  <desc id="cpCaja-dsc">Cajas anidadas. La de afuera es margin, el aire por fuera del Container. Sigue el borde y el fondo, que son la decoración. Adentro, padding, el aire entre el borde y el contenido. En el centro, el child.</desc>
  <defs>
    <style>
      #cpCaja .title{fill:#161A26;font-size:22px;font-weight:700}
      #cpCaja .sub{fill:#79809A;font-size:13.5px}
      #cpCaja .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #cpCaja .nt{font-size:15px;font-weight:700;fill:#161A26}
      #cpCaja .nb{fill:#454C61;font-size:13px}
      #cpCaja .lbl{fill:#556074;font-size:12px;font-weight:600}
      #cpCaja .foot{fill:#79809A;font-size:12px}
      #cpCaja .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #cpCaja .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#cpCaja-arrow)}
    </style>
    <marker id="cpCaja-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="440" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las capas de un <tspan class="mono">Container</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">De afuera hacia adentro: margin, la decoración, padding y el child.</text>
  <rect x="96" y="128" width="400" height="264" rx="10" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
  <rect x="136" y="168" width="320" height="184" rx="18" fill="#FFF3DC" stroke="#4453C9" stroke-width="3"/>
  <rect x="172" y="204" width="248" height="112" rx="6" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="296" y="265" font-size="15" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono">child</text>
  <path d="M478,148 H556" stroke="#556074" stroke-width="1.5"/><circle cx="478" cy="148" r="3.5" fill="#556074"/>
  <text x="572" y="144" font-size="15" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="340">margin</text>
  <text x="572" y="165" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="340">Aire por fuera. Separa la caja de sus vecinas.</text>
  <path d="M438,216 H556" stroke="#A96C05" stroke-width="1.5"/><circle cx="438" cy="216" r="3.5" fill="#A96C05"/>
  <text x="572" y="212" font-size="15" font-weight="700" fill="#A96C05" text-anchor="start" class="mono" data-fit="340">padding</text>
  <text x="572" y="233" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="340">Aire por dentro, entre el borde y el contenido.</text>
  <path d="M404,284 H556" stroke="#4453C9" stroke-width="1.5"/><circle cx="404" cy="284" r="3.5" fill="#4453C9"/>
  <text x="572" y="280" font-size="15" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="340">child</text>
  <text x="572" y="301" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="340">El contenido: un solo widget.</text>
  <path d="M456,340 H556" stroke="#4453C9" stroke-width="1.5"/><circle cx="456" cy="340" r="3.5" fill="#4453C9"/>
  <text x="572" y="336" font-size="15" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="340">decoration</text>
  <text x="572" y="357" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="340">El fondo, el borde y las esquinas.</text>
</svg>
```

`padding` y `margin` reciben lo mismo, un `EdgeInsets`, y se confunden fácil. Mira el borde: `padding` es el aire de adentro y `margin` el de afuera. Con un fondo de color se nota enseguida, porque el fondo cubre el `padding` y no cubre el `margin`.

Un `Container` mide lo que mide su `child` más el `padding`. Para fijarle un tamaño tiene `width` y `height`.

## Recortar lo que se sale

`borderRadius` redondea el fondo y el borde, pero no al hijo. Una imagen dentro de un `Container` redondeado sigue mostrando sus esquinas cuadradas. `clipBehavior` le dice al `Container` que recorte lo que tiene adentro con su misma forma:

```dart
Container(
  height: 160,
  clipBehavior: Clip.antiAlias,
  decoration: BoxDecoration(
    borderRadius: BorderRadius.circular(16),
  ),
  child: Image.network(
    'https://picsum.photos/400',
    fit: BoxFit.cover,
  ),
)
```

## Ejemplo completo

Una tarjeta con texto y una imagen con las esquinas redondeadas, separadas del borde de la pantalla por un `Padding`. Cambia el `padding` de la tarjeta por un `margin` y mira qué se mueve.

```dart trycode=PENDIENTE_S22
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
      backgroundColor: Colors.grey.shade100,
      appBar: AppBar(title: const Text('Perfil')),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.white,
                  border: Border.all(color: Colors.indigo),
                  borderRadius: BorderRadius.circular(16),
                ),
                child: const Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Mariana Valenzuela',
                      style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    SizedBox(height: 4),
                    Text('Diseñadora de Producto'),
                  ],
                ),
              ),
              const SizedBox(height: 16),
              Container(
                height: 160,
                clipBehavior: Clip.antiAlias,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(16),
                ),
                child: Image.network(
                  'https://picsum.photos/400',
                  fit: BoxFit.cover,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

Aquí `App` y `ProfileScreen` van en un solo archivo porque el editor en línea solo tiene uno; en tu proyecto siguen separados.
