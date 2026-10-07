# SingleChildScrollView

<!-- tags: SingleChildScrollView, RenderFlex overflowed on the bottom, la pantalla no hace scroll, scrollDirection, scroll horizontal, fila deslizable, RenderFlex children have non-zero flex, Expanded dentro de un scroll, contenido que no cabe, Spacer no funciona -->

Una `Column` no sabe deslizarse. Si sus hijos miden más que la pantalla, aparece la franja amarilla y negra abajo y la consola dice `A RenderFlex overflowed by 120 pixels on the bottom`. Con todos tus componentes apilados en el perfil, eso es justo lo que pasa.

## La pantalla es una ventana

```svg
<svg id="scVentana" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 664" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="scVentana-ttl scVentana-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="scVentana-ttl">La pantalla es una ventana</title>
  <desc id="scVentana-dsc">La misma pila de componentes en dos celulares. A la izquierda, sin scroll, lo que no cabe queda por fuera de la pantalla y aparece la franja amarilla y negra abajo. A la derecha, con SingleChildScrollView, la columna conserva todo su alto y sigue por debajo del celular: la pantalla es una ventana que se desliza sobre ella.</desc>
  <defs>
    <style>
      #scVentana .title{fill:#161A26;font-size:22px;font-weight:700}
      #scVentana .sub{fill:#79809A;font-size:13.5px}
      #scVentana .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #scVentana .nt{font-size:15px;font-weight:700;fill:#161A26}
      #scVentana .nb{fill:#454C61;font-size:13px}
      #scVentana .lbl{fill:#556074;font-size:12px;font-weight:600}
      #scVentana .foot{fill:#79809A;font-size:12px}
      #scVentana .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #scVentana .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#scVentana-arrow)}
    </style>
    <marker id="scVentana-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="664" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La pantalla es una ventana</text>
  <text class="sub" x="48" y="80" data-fit="860">Los componentes del perfil miden más que la pantalla. Con scroll, la pantalla se desliza sobre ellos.</text>
  <defs><pattern id="scVentana-warn" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#FFD600"/><rect width="5" height="10" fill="#1F2430"/></pattern></defs>
  <clipPath id="scVentana-a"><rect width="200" height="300" rx="20"/></clipPath><rect x="105" y="125" width="214" height="314" rx="27" fill="#1F2430"/><g transform="translate(112,132)"><g clip-path="url(#scVentana-a)"><rect width="200" height="300" rx="20" fill="#FFFFFF"/><g><rect x="10" y="10" width="180" height="90" rx="8" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="100.0" y="55.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#7439B8" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ProfileInfo</text></g><g><rect x="10" y="110" width="180" height="56" rx="8" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="100.0" y="138.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#4453C9" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">StatsRow</text></g><g><rect x="10" y="176" width="180" height="36" rx="8" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="100.0" y="194.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0F8478" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">PrimaryButton</text></g><g><rect x="10" y="222" width="180" height="72" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="100.0" y="258.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#A96C05" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ContactCard × 4</text></g><g><rect x="10" y="304" width="180" height="48" rx="8" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="100.0" y="328.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#C2354F" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ChatItem</text></g><g><rect x="10" y="362" width="180" height="48" rx="8" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="100.0" y="386.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#C2354F" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ChatItem</text></g><g><rect x="10" y="420" width="180" height="48" rx="8" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="100.0" y="444.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#C2354F" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ChatItem</text></g><rect y="288" width="200" height="12" fill="url(#scVentana-warn)"/></g></g>
  <text x="212" y="476" font-size="15" font-weight="700" fill="#C2354F" text-anchor="middle">Sin scroll</text>
  <text x="212" y="498" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">Lo que no cabe queda por fuera.</text>
  <rect x="496" y="132" width="200" height="300" rx="20" fill="#FFFFFF"/>
  <g><rect x="506" y="142" width="180" height="90" rx="8" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="596.0" y="187.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#7439B8" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ProfileInfo</text></g><g><rect x="506" y="242" width="180" height="56" rx="8" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="596.0" y="270.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#4453C9" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">StatsRow</text></g><g><rect x="506" y="308" width="180" height="36" rx="8" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="596.0" y="326.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0F8478" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">PrimaryButton</text></g><g><rect x="506" y="354" width="180" height="72" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="596.0" y="390.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#A96C05" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ContactCard × 4</text></g><g opacity=".42"><rect x="506" y="436" width="180" height="48" rx="8" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/><text x="596.0" y="460.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#C2354F" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ChatItem</text></g><g opacity=".42"><rect x="506" y="494" width="180" height="48" rx="8" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/><text x="596.0" y="518.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#C2354F" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ChatItem</text></g><g opacity=".42"><rect x="506" y="552" width="180" height="48" rx="8" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/><text x="596.0" y="576.0" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#C2354F" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ChatItem</text></g>
  <rect x="492.5" y="128.5" width="207" height="307" rx="23.5" fill="none" stroke="#1F2430" stroke-width="7"/>
  <path d="M728,240 V560" fill="none" stroke="#556074" stroke-width="1.75" marker-start="url(#scVentana-arrow)" marker-end="url(#scVentana-arrow)"/>
  <text x="748" y="366" font-size="15" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="180">Con scroll</text>
  <text x="748" y="394" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="180">La Column conserva</text>
  <text x="748" y="413" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="180">todo su alto.</text>
  <text x="748" y="448" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="180">La pantalla se desliza</text>
  <text x="748" y="467" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="180">sobre ella.</text>
</svg>
```

`SingleChildScrollView` deja que su hijo mida todo lo que necesite, aunque sea más que la pantalla, y muestra solo el pedazo que cabe. La persona mueve ese pedazo con el dedo.

## Cómo se usa

Tiene un solo hijo, como dice su nombre. Casi siempre es la `Column` con el contenido de la pantalla.

```svg
<svg id="scCodigo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 564" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="scCodigo-ttl scCodigo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="scCodigo-ttl">SingleChildScrollView envuelve la Column</title>
  <desc id="scCodigo-dsc">Un SafeArea cuyo child es un SingleChildScrollView con padding y una Column de componentes. En el resultado, el scroll ocupa la pantalla y la columna sigue por debajo de ella.</desc>
  <defs>
    <style>
      #scCodigo .title{fill:#161A26;font-size:22px;font-weight:700}
      #scCodigo .sub{fill:#79809A;font-size:13.5px}
      #scCodigo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #scCodigo .cl{font-size:13px;fill:#C9CFDA}
      #scCodigo .s{fill:#A8D8A0} #scCodigo .n{fill:#F2B880} #scCodigo .c{fill:#7FD1E8}
      #scCodigo .p{fill:#D5B8F5} #scCodigo .k{fill:#F08FB0}
      #scCodigo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #scCodigo .ct{fill:#161A26;font-size:14px;font-weight:700}
      #scCodigo .cb{fill:#454C61;font-size:13px}
      #scCodigo .rt{fill:#161A26;font-size:14px} #scCodigo .rs{fill:#79809A;font-size:12px}
      #scCodigo .foot{fill:#79809A;font-size:12px}
      #scCodigo .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #scCodigo .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #scCodigo .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#scCodigo-ar-green)}
      #scCodigo .hl-rose{fill:#F3A3B2;fill-opacity:.16;stroke:#F3A3B2;stroke-width:1.5}
      #scCodigo .ld-rose{fill:none;stroke:#F3A3B2;stroke-width:1.5;stroke-dasharray:3 4}
      #scCodigo .ar-rose{fill:none;stroke:#C2354F;stroke-width:1.75;marker-end:url(#scCodigo-ar-rose)}
    </style>
    <marker id="scCodigo-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="scCodigo-ar-rose" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/></marker>
  </defs>
  <rect width="960" height="564" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56"><tspan class="mono">SingleChildScrollView</tspan> envuelve la <tspan class="mono">Column</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">El scroll mide lo que mide la pantalla. La Column, adentro, mide lo que necesiten sus hijos.</text>
  <rect x="48" y="112" width="456" height="420" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/profile_screen.dart</text>
  <rect x="552" y="112" width="360" height="420" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-green" x="134.2" y="180" width="171.8" height="22" rx="5"/>
  <rect class="hl-rose" x="149.8" y="228" width="54.8" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="117.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">body</tspan>: <tspan class="c">SafeArea</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="226.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">SingleChildScrollView</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="220" textLength="218.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">padding</tspan>: <tspan class="c">EdgeInsets</tspan>.all(<tspan class="n">16</tspan>),</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Column</tspan>(</text>
  <text class="cl mono" font-size="13" x="114.8" y="268" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">children</tspan>: [</text>
  <text class="cl mono" font-size="13" x="130.4" y="292" textLength="132.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">ProfileInfo</tspan>(...),</text>
  <text class="cl mono" font-size="13" x="130.4" y="316" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">StatsRow</tspan>(...),</text>
  <text class="cl mono" font-size="13" x="130.4" y="340" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">ChatItem</tspan>(...),</text>
  <text class="cl mono" font-size="13" x="130.4" y="364" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">ChatItem</tspan>(...),</text>
  <text class="cl mono" font-size="13" x="114.8" y="388" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="99.2" y="412" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="83.6" y="436" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="68.0" y="460" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <g transform="translate(552,144)">
<rect x="96" y="20" width="168" height="226" rx="22" fill="#FFFFFF" stroke="#2A3040" stroke-width="3"/><rect x="102" y="26" width="156" height="214" rx="16" fill="#3A8235" fill-opacity=".08" stroke="#3A8235" stroke-width="2"/><g><rect x="114" y="38" width="132" height="84" rx="7" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="180" y="80.0" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="#7439B8" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ProfileInfo</text></g><g><rect x="114" y="130" width="132" height="52" rx="7" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="180" y="156.0" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="#4453C9" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">StatsRow</text></g><g><rect x="114" y="190" width="132" height="44" rx="7" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="180" y="212.0" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="#C2354F" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ChatItem</text></g><g opacity=".42"><rect x="114" y="258" width="132" height="44" rx="7" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/><text x="180" y="280.0" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="#C2354F" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ChatItem</text></g><g opacity=".42"><rect x="114" y="310" width="132" height="44" rx="7" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/><text x="180" y="332.0" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="#C2354F" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace">ChatItem</text></g>
  </g>
  <path class="ld-green" d="M315.8,191 H504"/>
  <path class="ar-green" d="M504,191 H523 V294 H654"/>
  <path class="ld-rose" d="M214.4,239 H504"/>
  <path class="ar-rose" d="M504,239 H514 V476 H666"/>
</svg>
```

```dart
body: SafeArea(
  child: SingleChildScrollView(
    padding: EdgeInsets.all(16),
    child: Column(
      children: [
        ProfileInfo(...),
        StatsRow(...),
        ChatItem(...),
        ChatItem(...),
      ],
    ),
  ),
),
```

El scroll tiene su propio `padding`, y conviene usarlo en lugar de envolverlo en un `Padding`. Así el aire se desliza junto con el contenido y no queda una franja fija arriba y abajo.

Con esto ya tienes el orden de casi cualquier pantalla del curso: `Scaffold`, `SafeArea`, `SingleChildScrollView` y adentro la `Column`.

## De lado

El scroll también funciona a lo ancho. Se le dice con `scrollDirection`, y adentro va una `Row`:

```svg
<svg id="scHorizontal" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="scHorizontal-ttl scHorizontal-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="scHorizontal-ttl">El mismo scroll, de lado</title>
  <desc id="scHorizontal-dsc">Una fila de seis tarjetas de contacto más ancha que la pantalla. Un marco muestra el ancho de la pantalla: tres tarjetas se ven completas y las demás quedan por fuera, a los lados, hasta que la persona desliza la fila.</desc>
  <defs>
    <style>
      #scHorizontal .title{fill:#161A26;font-size:22px;font-weight:700}
      #scHorizontal .sub{fill:#79809A;font-size:13.5px}
      #scHorizontal .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #scHorizontal .nt{font-size:15px;font-weight:700;fill:#161A26}
      #scHorizontal .nb{fill:#454C61;font-size:13px}
      #scHorizontal .lbl{fill:#556074;font-size:12px;font-weight:600}
      #scHorizontal .foot{fill:#79809A;font-size:12px}
      #scHorizontal .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #scHorizontal .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#scHorizontal-arrow)}
    </style>
    <marker id="scHorizontal-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="420" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">El mismo scroll, de lado</text>
  <text class="sub" x="48" y="80" data-fit="860">Con scrollDirection horizontal, lo que se desliza es una Row. Es la fila de contactos sugeridos.</text>
  <g opacity=".4"><rect x="156" y="144" width="96" height="124" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><circle cx="204" cy="186" r="24" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="204" cy="181.2" r="7.9" fill="#A9B4F2"/><path d="M189.1,203.8 a14.9,13.4 0 0 1 29.8,0 Z" fill="#A9B4F2"/><text x="204" y="234" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="middle">Ana</text><text x="204" y="252" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@ana</text></g>
  <g opacity=".4"><rect x="268" y="144" width="96" height="124" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><circle cx="316" cy="186" r="24" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><circle cx="316" cy="181.2" r="7.9" fill="#86D3CA"/><path d="M301.1,203.8 a14.9,13.4 0 0 1 29.8,0 Z" fill="#86D3CA"/><text x="316" y="234" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="middle">Luis Peña</text><text x="316" y="252" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@luisp</text></g>
  <g><rect x="380" y="144" width="96" height="124" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><circle cx="428" cy="186" r="24" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><circle cx="428" cy="181.2" r="7.9" fill="#F3A3B2"/><path d="M413.1,203.8 a14.9,13.4 0 0 1 29.8,0 Z" fill="#F3A3B2"/><text x="428" y="234" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="middle">Sofía Ruiz</text><text x="428" y="252" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@sofiaruiz</text></g>
  <g><rect x="492" y="144" width="96" height="124" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><circle cx="540" cy="186" r="24" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="540" cy="181.2" r="7.9" fill="#F0C572"/><path d="M525.1,203.8 a14.9,13.4 0 0 1 29.8,0 Z" fill="#F0C572"/><text x="540" y="234" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="middle">Javier M…</text><text x="540" y="252" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@javim</text></g>
  <g><rect x="604" y="144" width="96" height="124" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><circle cx="652" cy="186" r="24" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><circle cx="652" cy="181.2" r="7.9" fill="#C9A6EE"/><path d="M637.1,203.8 a14.9,13.4 0 0 1 29.8,0 Z" fill="#C9A6EE"/><text x="652" y="234" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="middle">Mariana V…</text><text x="652" y="252" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@marianav</text></g>
  <g opacity=".4"><rect x="716" y="144" width="96" height="124" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><circle cx="764" cy="186" r="24" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><circle cx="764" cy="181.2" r="7.9" fill="#9FD68D"/><path d="M749.1,203.8 a14.9,13.4 0 0 1 29.8,0 Z" fill="#9FD68D"/><text x="764" y="234" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="middle">David Luna</text><text x="764" y="252" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@davidl</text></g>
  <rect x="368" y="128" width="344" height="156" rx="14" fill="none" stroke="#1F2430" stroke-width="3"/>
  <path d="M368,304 V310 H712 V304" fill="none" stroke="#556074" stroke-width="1.5"/>
  <text x="540" y="330" font-size="12.5" font-weight="700" fill="#556074" text-anchor="middle">ancho de la pantalla</text>
  <path d="M96,206 H132" fill="none" stroke="#556074" stroke-width="1.75" marker-start="url(#scHorizontal-arrow)"/>
  <path d="M836,206 H872" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#scHorizontal-arrow)"/>
  <text x="480" y="376" font-size="14" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono">scrollDirection: Axis.horizontal</text>
</svg>
```

```dart
SingleChildScrollView(
  scrollDirection: Axis.horizontal,
  child: Row(
    children: [
      ContactCard(...),
      SizedBox(width: 12),
      ContactCard(...),
      SizedBox(width: 12),
      ContactCard(...),
    ],
  ),
)
```

Es la fila de contactos sugeridos que quedó pendiente en el taller. `ContactCard` no cambia: el ancho fijo que le diste es lo que hace que todas las tarjetas midan igual dentro de la fila.

Un scroll horizontal puede ir dentro de uno vertical sin problema, porque se mueven en direcciones distintas.

## Lo que no va dentro de un scroll

`Expanded` y `Spacer` reparten el espacio que sobra. Dentro de un scroll no sobra nada: el contenido puede medir lo que quiera, así que no hay un límite contra el cual repartir. Si pones cualquiera de los dos en la `Column` que se desliza, la pantalla queda en blanco y la consola dice `RenderFlex children have non-zero flex but incoming height constraints are unbounded`.

La solución es quitarlo y separar con `SizedBox`. Dentro de las filas de esa columna sí puedes seguir usando `Expanded`: el ancho sigue teniendo límite.

## Ejemplo completo

Una fila de contactos que se desliza de lado, dentro de una pantalla que se desliza hacia abajo. Quita el `SingleChildScrollView` de afuera, dejando la `Column` como hijo del `SafeArea`, para ver la franja.

```dart trycode=PENDIENTE_S24
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
      appBar: AppBar(title: const Text('Perfil')),
      body: const SafeArea(
        child: SingleChildScrollView(
          padding: EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Contactos sugeridos',
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 12),
              SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: Row(
                  children: [
                    ContactCard(name: 'Ana Torres', username: '@anatorres'),
                    SizedBox(width: 12),
                    ContactCard(name: 'Luis Peña', username: '@luisp'),
                    SizedBox(width: 12),
                    ContactCard(name: 'Sofía Ruiz', username: '@sofiaruiz'),
                    SizedBox(width: 12),
                    ContactCard(name: 'Javier Montes', username: '@javim'),
                    SizedBox(width: 12),
                    ContactCard(name: 'David Luna', username: '@davidl'),
                    SizedBox(width: 12),
                    ContactCard(name: 'Alex Torres', username: '@alext'),
                  ],
                ),
              ),
              SizedBox(height: 24),
              Text(
                'Últimas conversaciones',
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 12),
              ChatItem(name: 'Javier Montes', message: '¿Revisamos los avances?'),
              ChatItem(name: 'Sofía Ruiz', message: 'Listo, ya subí los cambios'),
              ChatItem(name: 'Alex Torres', message: 'Mañana enviamos el informe'),
              ChatItem(name: 'David Luna', message: 'Hola, ¿tienes un minuto?'),
              ChatItem(name: 'Ana Torres', message: 'Nos vemos en clase'),
              ChatItem(name: 'Luis Peña', message: 'Gracias por la ayuda'),
              ChatItem(name: 'Mariana Valenzuela', message: 'Te mando el diseño'),
              ChatItem(name: 'Camila Rojas', message: '¿A qué hora es la reunión?'),
            ],
          ),
        ),
      ),
    );
  }
}

/// Small card of a suggested contact.
class ContactCard extends StatelessWidget {
  final String name;
  final String username;

  const ContactCard({super.key, required this.name, required this.username});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 96,
      child: Column(
        children: [
          const CircleAvatar(
            radius: 30,
            backgroundImage: NetworkImage('https://picsum.photos/400'),
          ),
          const SizedBox(height: 8),
          Text(name, maxLines: 1, overflow: TextOverflow.ellipsis),
          Text(username, maxLines: 1, overflow: TextOverflow.ellipsis),
        ],
      ),
    );
  }
}

/// Row of a conversation.
class ChatItem extends StatelessWidget {
  final String name;
  final String message;

  const ChatItem({super.key, required this.name, required this.message});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 12),
      child: Row(
        children: [
          const CircleAvatar(
            radius: 24,
            backgroundImage: NetworkImage('https://picsum.photos/400'),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(name, style: const TextStyle(fontWeight: FontWeight.bold)),
                Text(message, maxLines: 1, overflow: TextOverflow.ellipsis),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
```

Aquí las pantallas y los componentes van en un solo archivo porque el editor en línea solo tiene uno. `ContactCard` y `ChatItem` son versiones cortas de los tuyos: en tu proyecto usa los que hiciste en el taller.
