# BottomNavigationBar: una pieza del Scaffold

<!-- tags: BottomNavigationBar, bottomNavigationBar del Scaffold, BottomNavigationBarItem, icon y label, currentIndex, onTap, BottomNavigationBarType.fixed, los iconos de la barra salen blancos, solo se ve el label del seleccionado, items debe tener al menos dos -->

La barra de abajo no es un widget que se pone en el `body` y se acomoda con un `Column`. El `Scaffold` ya tiene un lugar reservado para ella, igual que para la barra de arriba. En esta lección se ve dónde va, de qué partes está hecha y qué hace cuando se toca. Todavía no cambia el contenido: eso es la lección siguiente.

## Un lugar más del Scaffold

En la sesión 3 viste que un `Scaffold` es un andamio con lugares fijos: `appBar` arriba, `body` en medio, `floatingActionButton` flotando abajo a la derecha. El cuarto es `bottomNavigationBar`, pegado al borde de abajo.

```svg
<svg id="bpScaffold" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 600" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="bpScaffold-ttl bpScaffold-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="bpScaffold-ttl">La barra tiene su lugar en el Scaffold</title>
  <desc id="bpScaffold-dsc">Un celular con una pantalla armada con Scaffold. Arriba, la barra con el título Mi app: es appBar. En medio, el contenido: es body. Abajo a la derecha, un botón redondo: es floatingActionButton. Pegada al borde de abajo, una barra con tres botones, Inicio, Chats y Perfil: es bottomNavigationBar, resaltada. El body ocupa lo que queda entre las dos barras, y el botón flotante queda encima de la de abajo.</desc>
  <defs>
    <style>
      #bpScaffold .title{fill:#161A26;font-size:22px;font-weight:700}
      #bpScaffold .sub{fill:#79809A;font-size:13.5px}
      #bpScaffold .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #bpScaffold .nt{font-size:15px;font-weight:700;fill:#161A26}
      #bpScaffold .nb{fill:#454C61;font-size:13px}
      #bpScaffold .lbl{fill:#556074;font-size:12px;font-weight:600}
      #bpScaffold .foot{fill:#79809A;font-size:12px}
      #bpScaffold .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #bpScaffold .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#bpScaffold-arrow)}
    </style>
    <marker id="bpScaffold-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="600" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La barra tiene su lugar en el <tspan class="mono">Scaffold</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">bottomNavigationBar es un lugar más del Scaffold, como appBar o body. Queda fija en el borde de abajo.</text>
  <clipPath id="bpScaffold-scr"><rect width="220" height="440" rx="20"/></clipPath><rect x="363" y="113" width="234" height="454" rx="27" fill="#1F2430"/><g transform="translate(370,120)"><g clip-path="url(#bpScaffold-scr)"><rect width="220" height="440" rx="20" fill="#FFFFFF"/><rect width="220" height="52" fill="#F1ECF8"/><text x="18" y="32" font-size="17" font-weight="500" fill="#161A26" text-anchor="start">Mi app</text><text x="110.0" y="220" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="middle">Contenido</text><rect x="156" y="316" width="48" height="48" rx="14" fill="#EADDFF"/><path d="M180,328 V348 M170,338 H190" stroke="#21005D" stroke-width="2.5" stroke-linecap="round"/><rect x="0" y="380" width="220" height="60" fill="#F3EDF7"/><rect x="10.7" y="389.8" width="52.0" height="26.0" rx="13.0" fill="#E8DEF8"/><path transform="translate(36.7,402.8) scale(1.0)" d="M-8,1 L0,-7 L8,1 M-6,-0.5 V7 H6 V-0.5" fill="none" stroke="#6750A4" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><text x="36.7" y="429.2" font-size="11.5" font-weight="600" fill="#6750A4" text-anchor="middle">Inicio</text><path transform="translate(110.0,402.8) scale(1.0)" d="M-7,-7 h14 a2,2 0 0 1 2,2 v7 a2,2 0 0 1 -2,2 h-8 l-4,3 v-3 h-2 a2,2 0 0 1 -2,-2 v-7 a2,2 0 0 1 2,-2 Z" fill="none" stroke="#556074" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><text x="110.0" y="429.2" font-size="11.5" font-weight="600" fill="#556074" text-anchor="middle">Chats</text><path transform="translate(183.3,402.8) scale(1.0)" d="M-3.5,-4 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M-7,7 a7,6 0 0 1 14,0" fill="none" stroke="#556074" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><text x="183.3" y="429.2" font-size="11.5" font-weight="600" fill="#556074" text-anchor="middle">Perfil</text></g></g>
  <rect x="376" y="126" width="208" height="42" rx="10" fill="#A96C05" fill-opacity=".08" stroke="#A96C05" stroke-width="2"/>
  <path d="M376,147.0 H342" stroke="#A96C05" stroke-width="1.75" stroke-dasharray="4 4"/>
  <text x="334" y="143.0" font-size="15" font-weight="700" fill="#A96C05" text-anchor="end" class="mono">appBar</text>
  <text x="334" y="163.0" font-size="13" font-weight="400" fill="#556074" text-anchor="end" data-fit="280">La barra de arriba, con el título.</text>
  <rect x="376" y="178" width="208" height="316" rx="10" fill="#3A8235" fill-opacity=".08" stroke="#3A8235" stroke-width="2"/>
  <path d="M376,336.0 H342" stroke="#3A8235" stroke-width="1.75" stroke-dasharray="4 4"/>
  <text x="334" y="332.0" font-size="15" font-weight="700" fill="#3A8235" text-anchor="end" class="mono">body</text>
  <text x="334" y="352.0" font-size="13" font-weight="400" fill="#556074" text-anchor="end" data-fit="280">El contenido. Ocupa lo que sobra.</text>
  <rect x="522" y="432" width="56" height="56" rx="10" fill="#C2354F" fill-opacity=".08" stroke="#C2354F" stroke-width="2"/>
  <path d="M578,460.0 H618" stroke="#C2354F" stroke-width="1.75" stroke-dasharray="4 4"/>
  <text x="626" y="456.0" font-size="15" font-weight="700" fill="#C2354F" text-anchor="start" class="mono">floatingActionButton</text>
  <text x="626" y="476.0" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="300">Flota sobre el body.</text>
  <rect x="374" y="502" width="212" height="54" rx="10" fill="#4453C9" fill-opacity=".08" stroke="#4453C9" stroke-width="2"/>
  <path d="M586,529.0 H618" stroke="#4453C9" stroke-width="1.75" stroke-dasharray="4 4"/>
  <text x="626" y="525.0" font-size="15" font-weight="700" fill="#4453C9" text-anchor="start" class="mono">bottomNavigationBar</text>
  <text x="626" y="545.0" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="300">La barra de abajo. Hoy, esta.</text>
</svg>
```

Como es un lugar del `Scaffold`, no tienes que medir nada. El `body` se encoge solo para no quedar debajo de la barra, y el botón flotante sube para quedar encima de ella. Por eso la barra va en la **Screen**, la que tiene el `Scaffold`, y nunca dentro de una Page.

## Sus partes

`BottomNavigationBar` pide dos cosas: la lista de botones y cuál de ellos está resaltado.

```svg
<svg id="bpPartes" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 738" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="bpPartes-ttl bpPartes-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="bpPartes-ttl">Las partes de un BottomNavigationBar</title>
  <desc id="bpPartes-dsc">El código de un BottomNavigationBar con currentIndex en 0 y una lista items con tres BottomNavigationBarItem, cada uno con icon y label: Inicio, Chats y Perfil. A la derecha, la barra de cerca: currentIndex señala el primer botón, resaltado con una píldora; items señala la barra completa. Debajo, un botón desarmado: icon es el dibujo de la casa y label es el texto Inicio.</desc>
  <defs>
    <style>
      #bpPartes .title{fill:#161A26;font-size:22px;font-weight:700}
      #bpPartes .sub{fill:#79809A;font-size:13.5px}
      #bpPartes .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #bpPartes .cl{font-size:13px;fill:#C9CFDA}
      #bpPartes .s{fill:#A8D8A0} #bpPartes .n{fill:#F2B880} #bpPartes .c{fill:#7FD1E8}
      #bpPartes .p{fill:#D5B8F5} #bpPartes .k{fill:#F08FB0}
      #bpPartes .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #bpPartes .ct{fill:#161A26;font-size:14px;font-weight:700}
      #bpPartes .cb{fill:#454C61;font-size:13px}
      #bpPartes .rt{fill:#161A26;font-size:14px} #bpPartes .rs{fill:#79809A;font-size:12px}
      #bpPartes .foot{fill:#79809A;font-size:12px}
      #bpPartes .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #bpPartes .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #bpPartes .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#bpPartes-ar-amber)}
      #bpPartes .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #bpPartes .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #bpPartes .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#bpPartes-ar-green)}
      #bpPartes .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #bpPartes .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #bpPartes .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#bpPartes-ar-indigo)}
      #bpPartes .hl-teal{fill:#86D3CA;fill-opacity:.16;stroke:#86D3CA;stroke-width:1.5}
      #bpPartes .ld-teal{fill:none;stroke:#86D3CA;stroke-width:1.5;stroke-dasharray:3 4}
      #bpPartes .ar-teal{fill:none;stroke:#0F8478;stroke-width:1.75;marker-end:url(#bpPartes-ar-teal)}
    </style>
    <marker id="bpPartes-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="bpPartes-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="bpPartes-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="bpPartes-ar-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#0F8478"/></marker>
  </defs>
  <rect width="960" height="738" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las partes de un <tspan class="mono">BottomNavigationBar</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">La barra es una lista de botones y un número que dice cuál está resaltado.</text>
  <rect x="48" y="112" width="456" height="468" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/home_screen.dart</text>
  <rect x="552" y="112" width="360" height="468" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-green" x="79.6" y="180" width="101.6" height="22" rx="5"/>
  <rect class="hl-amber" x="79.6" y="204" width="47.0" height="22" rx="5"/>
  <rect class="hl-indigo" x="110.8" y="252" width="39.2" height="22" rx="5"/>
  <rect class="hl-teal" x="110.8" y="276" width="47.0" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="319.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">bottomNavigationBar</tspan>: <tspan class="c">BottomNavigationBar</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">currentIndex</tspan>: <tspan class="n">0</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">items</tspan>: <tspan class="k">const</tspan> [</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="187.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">BottomNavigationBarItem</tspan>(</text>
  <text class="cl mono" font-size="13" x="114.8" y="268" textLength="179.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">icon</tspan>: <tspan class="c">Icon</tspan>(<tspan class="c">Icons</tspan>.home),</text>
  <text class="cl mono" font-size="13" x="114.8" y="292" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">label</tspan>: <tspan class="s">'Inicio'</tspan>,</text>
  <text class="cl mono" font-size="13" x="99.2" y="316" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="99.2" y="340" textLength="187.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">BottomNavigationBarItem</tspan>(</text>
  <text class="cl mono" font-size="13" x="114.8" y="364" textLength="179.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">icon</tspan>: <tspan class="c">Icon</tspan>(<tspan class="c">Icons</tspan>.chat),</text>
  <text class="cl mono" font-size="13" x="114.8" y="388" textLength="117.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">label</tspan>: <tspan class="s">'Chats'</tspan>,</text>
  <text class="cl mono" font-size="13" x="99.2" y="412" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="99.2" y="436" textLength="187.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">BottomNavigationBarItem</tspan>(</text>
  <text class="cl mono" font-size="13" x="114.8" y="460" textLength="195.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">icon</tspan>: <tspan class="c">Icon</tspan>(<tspan class="c">Icons</tspan>.person),</text>
  <text class="cl mono" font-size="13" x="114.8" y="484" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">label</tspan>: <tspan class="s">'Perfil'</tspan>,</text>
  <text class="cl mono" font-size="13" x="99.2" y="508" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="83.6" y="532" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="68.0" y="556" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <g transform="translate(552,144)">
<text x="16" y="40" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="h">LA BARRA, DE CERCA</text><rect x="16" y="56" width="328" height="100" rx="14" fill="#F3EDF7" stroke="#E6E0F2"/><rect x="38.7" y="68" width="64" height="34" rx="17" fill="#E8DEF8"/><path transform="translate(70.7,85) scale(1.4)" d="M-8,1 L0,-7 L8,1 M-6,-0.5 V7 H6 V-0.5" fill="none" stroke="#6750A4" stroke-width="1.43" stroke-linecap="round" stroke-linejoin="round"/><text x="70.7" y="132" font-size="14" font-weight="600" fill="#6750A4" text-anchor="middle">Inicio</text><path transform="translate(180.0,85) scale(1.4)" d="M-7,-7 h14 a2,2 0 0 1 2,2 v7 a2,2 0 0 1 -2,2 h-8 l-4,3 v-3 h-2 a2,2 0 0 1 -2,-2 v-7 a2,2 0 0 1 2,-2 Z" fill="none" stroke="#556074" stroke-width="1.43" stroke-linecap="round" stroke-linejoin="round"/><text x="180.0" y="132" font-size="14" font-weight="600" fill="#556074" text-anchor="middle">Chats</text><path transform="translate(289.3,85) scale(1.4)" d="M-3.5,-4 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M-7,7 a7,6 0 0 1 14,0" fill="none" stroke="#556074" stroke-width="1.43" stroke-linecap="round" stroke-linejoin="round"/><text x="289.3" y="132" font-size="14" font-weight="600" fill="#556074" text-anchor="middle">Perfil</text><path d="M70.7,160 V196" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="4 4"/><rect x="16" y="196" width="328" height="124" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><text x="32" y="218" font-size="12.5" font-weight="700" fill="#556074" text-anchor="start" class="mono">Un BottomNavigationBarItem</text><rect x="32" y="230" width="40" height="40" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><path transform="translate(52,250) scale(1.2)" d="M-8,1 L0,-7 L8,1 M-6,-0.5 V7 H6 V-0.5" fill="none" stroke="#4453C9" stroke-width="1.67" stroke-linecap="round" stroke-linejoin="round"/><text x="84" y="255" font-size="13" font-weight="400" fill="#454C61" text-anchor="start">icon · el dibujo</text><rect x="32" y="280" width="64" height="28" rx="8" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="64" y="299" font-size="13" font-weight="600" fill="#0F8478" text-anchor="middle">Inicio</text><text x="108" y="299" font-size="13" font-weight="400" fill="#454C61" text-anchor="start">label · el texto</text>
  </g>
  <path class="ld-green" d="M214.4,191 H504"/>
  <path class="ar-green" d="M504,191 H541 V229 H592"/>
  <path class="ld-amber" d="M198.8,215 H504"/>
  <path class="ar-amber" d="M504,215 H532 V286 H568"/>
  <path class="ld-indigo" d="M300.2,263 H504"/>
  <path class="ar-indigo" d="M504,263 H523 V394 H584"/>
  <path class="ld-teal" d="M245.6,287 H504"/>
  <path class="ar-teal" d="M504,287 H514 V438 H584"/>
  <g transform="translate(48.0,604)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#E8F6E3" stroke="#3A8235" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="219">currentIndex</text>
    <text class="cb" x="16" y="60" data-fit="245">El botón resaltado. Se cuenta</text>
    <text class="cb" x="16" y="79" data-fit="245">desde 0: aquí es Inicio.</text>
  </g>
  <g transform="translate(341.3,604)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#FFF3DC" stroke="#A96C05" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="219">items</text>
    <text class="cb" x="16" y="60" data-fit="245">Los botones, de izquierda a</text>
    <text class="cb" x="16" y="79" data-fit="245">derecha. Mínimo dos.</text>
  </g>
  <g transform="translate(634.7,604)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#EEF1FF" stroke="#4453C9" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="219">icon y label</text>
    <text class="cb" x="16" y="60" data-fit="245">Cada botón: un Icon y un</text>
    <text class="cb" x="16" y="79" data-fit="245">texto. Los dos obligatorios.</text>
  </g>
</svg>
```

```dart
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
```

- **`items`** es la lista de botones. Se dibujan de izquierda a derecha en el orden en que los escribes. La barra pide al menos dos; con uno solo, la app falla al arrancar.
- Cada botón es un **`BottomNavigationBarItem`** con un **`icon`**, que casi siempre es un `Icon`, y un **`label`**, el texto que va debajo.
- **`currentIndex`** es el número del botón resaltado. Se cuenta desde 0, como en una lista: `0` es *Inicio* y `2` es *Perfil*.

## Cuando se toca: onTap

Toca *Chats* en una barra como la de arriba y no pasa nada. La barra no cambia sola de botón resaltado: solo avisa que la tocaron. Ese aviso es **`onTap`**, una función que recibe el número del botón tocado. Va dentro de `BottomNavigationBar`, junto a `currentIndex`:

```dart
onTap: (index) => debugPrint('Tocaste el botón $index'),
```

Toca los tres botones y mira la consola de depuración:

```text
Tocaste el botón 1
Tocaste el botón 2
Tocaste el botón 0
```

El número llega bien, pero *Inicio* sigue resaltado: `currentIndex` dice `0`, escrito a mano, y nadie lo cambia. Guardar ese número en el estado para que la barra y el contenido respondan es la lección siguiente.

## Con cuatro botones o más

Agrega un cuarto botón, *Ajustes*, y la barra cambia de aspecto: los iconos se vuelven casi invisibles y los textos desaparecen, salvo el del botón resaltado.

```svg
<svg id="bpTipos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 404" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="bpTipos-ttl bpTipos-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="bpTipos-ttl">Con cuatro botones, la barra cambia de estilo</title>
  <desc id="bpTipos-dsc">Dos barras con cuatro botones: Inicio, Chats, Perfil y Ajustes. La de la izquierda, sin type: es shifting, los iconos quedan casi blancos sobre el fondo y solo el botón resaltado muestra su texto. La de la derecha, con type BottomNavigationBarType.fixed: los cuatro iconos y los cuatro textos se ven, y el resaltado va en morado.</desc>
  <defs>
    <style>
      #bpTipos .title{fill:#161A26;font-size:22px;font-weight:700}
      #bpTipos .sub{fill:#79809A;font-size:13.5px}
      #bpTipos .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #bpTipos .nt{font-size:15px;font-weight:700;fill:#161A26}
      #bpTipos .nb{fill:#454C61;font-size:13px}
      #bpTipos .lbl{fill:#556074;font-size:12px;font-weight:600}
      #bpTipos .foot{fill:#79809A;font-size:12px}
      #bpTipos .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #bpTipos .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#bpTipos-arrow)}
    </style>
    <marker id="bpTipos-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="404" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Con cuatro botones, la barra cambia de estilo</text>
  <text class="sub" x="48" y="80" data-fit="860">Con tres o menos, Flutter usa fixed. Con cuatro o más, shifting: hay que pedir fixed a mano.</text>
  <text x="64" y="132" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="384">Sin type</text>
  <text x="64" y="152" font-size="12.5" font-weight="500" fill="#C2354F" text-anchor="start" data-fit="384">shifting · casi invisible</text>
  <rect x="64" y="176" width="384" height="120" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <g><rect x="64" y="236" width="384" height="60" fill="#FFFFFF"/><path transform="translate(112.0,258.8) scale(1.0)" d="M-8,1 L0,-7 L8,1 M-6,-0.5 V7 H6 V-0.5" fill="none" stroke="#E4DFEC" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><text x="112.0" y="285.2" font-size="11.5" font-weight="600" fill="#E4DFEC" text-anchor="middle">Inicio</text><path transform="translate(208.0,258.8) scale(1.0)" d="M-7,-7 h14 a2,2 0 0 1 2,2 v7 a2,2 0 0 1 -2,2 h-8 l-4,3 v-3 h-2 a2,2 0 0 1 -2,-2 v-7 a2,2 0 0 1 2,-2 Z" fill="none" stroke="#ECE8F2" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><path transform="translate(304.0,258.8) scale(1.0)" d="M-3.5,-4 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M-7,7 a7,6 0 0 1 14,0" fill="none" stroke="#ECE8F2" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><path transform="translate(400.0,258.8) scale(1.0)" d="M-3.5,0 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M0,-9 V-6.5 M0,6.5 V9 M-9,0 H-6.5 M6.5,0 H9 M-6.4,-6.4 L-4.6,-4.6 M4.6,4.6 L6.4,6.4 M-6.4,6.4 L-4.6,4.6 M4.6,-4.6 L6.4,-6.4" fill="none" stroke="#ECE8F2" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/></g>
  <path d="M64,236 H448" stroke="#EFF1F5" stroke-width="1.5"/>
  <text x="80" y="206" font-size="13" font-weight="400" fill="#79809A" text-anchor="start">Contenido</text>
  <text x="512" y="132" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="384">type: BottomNavigationBarType.fixed</text>
  <text x="512" y="152" font-size="12.5" font-weight="500" fill="#3A8235" text-anchor="start" data-fit="384">fixed · se ve todo</text>
  <rect x="512" y="176" width="384" height="120" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <g><rect x="512" y="236" width="384" height="60" fill="#F3EDF7"/><rect x="534.0" y="245.8" width="52.0" height="26.0" rx="13.0" fill="#E8DEF8"/><path transform="translate(560.0,258.8) scale(1.0)" d="M-8,1 L0,-7 L8,1 M-6,-0.5 V7 H6 V-0.5" fill="none" stroke="#6750A4" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><text x="560.0" y="285.2" font-size="11.5" font-weight="600" fill="#6750A4" text-anchor="middle">Inicio</text><path transform="translate(656.0,258.8) scale(1.0)" d="M-7,-7 h14 a2,2 0 0 1 2,2 v7 a2,2 0 0 1 -2,2 h-8 l-4,3 v-3 h-2 a2,2 0 0 1 -2,-2 v-7 a2,2 0 0 1 2,-2 Z" fill="none" stroke="#556074" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><text x="656.0" y="285.2" font-size="11.5" font-weight="600" fill="#556074" text-anchor="middle">Chats</text><path transform="translate(752.0,258.8) scale(1.0)" d="M-3.5,-4 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M-7,7 a7,6 0 0 1 14,0" fill="none" stroke="#556074" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><text x="752.0" y="285.2" font-size="11.5" font-weight="600" fill="#556074" text-anchor="middle">Perfil</text><path transform="translate(848.0,258.8) scale(1.0)" d="M-3.5,0 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M0,-9 V-6.5 M0,6.5 V9 M-9,0 H-6.5 M6.5,0 H9 M-6.4,-6.4 L-4.6,-4.6 M4.6,4.6 L6.4,6.4 M-6.4,6.4 L-4.6,4.6 M4.6,-4.6 L6.4,-6.4" fill="none" stroke="#556074" stroke-width="2.00" stroke-linecap="round" stroke-linejoin="round"/><text x="848.0" y="285.2" font-size="11.5" font-weight="600" fill="#556074" text-anchor="middle">Ajustes</text></g>
  <path d="M512,236 H896" stroke="#EFF1F5" stroke-width="1.5"/>
  <text x="528" y="206" font-size="13" font-weight="400" fill="#79809A" text-anchor="start">Contenido</text>
  <rect x="64" y="320" width="384" height="64" rx="12" fill="#FFFFFF" stroke="#F3A3B2" stroke-width="1.5"/><text x="80" y="351" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="356">Los iconos se pierden</text><text x="80" y="378" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="352">shifting pinta los botones en blanco.</text>
  <rect x="512" y="320" width="384" height="64" rx="12" fill="#FFFFFF" stroke="#9FD68D" stroke-width="1.5"/><text x="528" y="351" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="356">Con fixed, como con tres</text><text x="528" y="378" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="352">Todos los textos y el color del tema.</text>
</svg>
```

No es un error tuyo. Con tres botones o menos, Flutter usa el estilo **`fixed`**; con cuatro o más cambia a **`shifting`**, que pinta los botones en blanco esperando que cada uno traiga su propio color de fondo. Para que se vea igual que con tres, pide el estilo a mano, también dentro de `BottomNavigationBar`:

```dart
type: BottomNavigationBarType.fixed,
selectedItemColor: Colors.deepPurple,
```

`selectedItemColor` es opcional: cambia el color del botón resaltado. Sin él se usa el color del tema.

## Ejemplo completo

Una pantalla con la barra de arriba, el contenido y los tres botones de abajo. Toca los botones y mira la consola: llega el número, pero el resaltado no se mueve.

```dart trycode=d26ef7d7a952d81dd786b68bcd669b55 tab=run
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

/// Screen with a bottom navigation bar of three items.
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Mi app')),
      body: const SafeArea(
        child: Center(child: Text('Contenido')),
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: 0,
        onTap: (index) => debugPrint('Tocaste el botón $index'),
        type: BottomNavigationBarType.fixed,
        selectedItemColor: Colors.deepPurple,
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
