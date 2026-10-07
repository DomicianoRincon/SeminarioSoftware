# Expanded

<!-- tags: Expanded, RenderFlex overflowed on the right, franja amarilla y negra, ocupar el espacio que sobra, flex, Spacer, Incorrect use of ParentDataWidget, texto largo en una Row, dos botones del mismo ancho, empujar un widget al fondo -->

En el taller de componentes te encontraste con la franja amarilla y negra: un mensaje largo no cabía en la fila de `ChatItem`. La pista fue envolver los textos en un `Expanded`. Esta lección explica por qué funciona.

## El problema

Una `Row` le pregunta a cada hijo cuánto ancho quiere, y se lo da. Un `Text` quiere todo el que necesita para escribirse en un solo renglón, aunque sea más que la pantalla.

```svg
<svg id="exSobra" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 432" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="exSobra-ttl exSobra-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="exSobra-ttl">Una fila con un texto largo</title>
  <desc id="exSobra-dsc">La misma fila de chat dos veces. Arriba, sin Expanded, el mensaje se sale por la derecha de la pantalla y aparece la franja amarilla y negra. Abajo, con Expanded, la columna de textos ocupa el espacio que dejan la foto y la hora, y el mensaje se corta con puntos suspensivos.</desc>
  <defs>
    <style>
      #exSobra .title{fill:#161A26;font-size:22px;font-weight:700}
      #exSobra .sub{fill:#79809A;font-size:13.5px}
      #exSobra .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #exSobra .nt{font-size:15px;font-weight:700;fill:#161A26}
      #exSobra .nb{fill:#454C61;font-size:13px}
      #exSobra .lbl{fill:#556074;font-size:12px;font-weight:600}
      #exSobra .foot{fill:#79809A;font-size:12px}
      #exSobra .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #exSobra .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#exSobra-arrow)}
    </style>
    <marker id="exSobra-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="432" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Una fila con un texto largo</text>
  <text class="sub" x="48" y="80" data-fit="860">Sin Expanded, el texto pide todo el ancho que necesita. Con Expanded, recibe solo el que sobra.</text>
  <defs><pattern id="exSobra-warn" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#FFD600"/><rect width="5" height="10" fill="#1F2430"/></pattern></defs>
  <rect x="232" y="128" width="560" height="80" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <circle cx="272" cy="168" r="24" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="272" cy="163.2" r="7.9" fill="#F0C572"/><path d="M257.1,185.8 a14.9,13.4 0 0 1 29.8,0 Z" fill="#F0C572"/>
  <text x="312" y="162" font-size="15" font-weight="700" fill="#161A26" text-anchor="start">Javier Montes</text>
  <rect x="232" y="264" width="560" height="80" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <circle cx="272" cy="304" r="24" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="272" cy="299.2" r="7.9" fill="#F0C572"/><path d="M257.1,321.8 a14.9,13.4 0 0 1 29.8,0 Z" fill="#F0C572"/>
  <text x="312" y="298" font-size="15" font-weight="700" fill="#161A26" text-anchor="start">Javier Montes</text>
  <text x="312" y="184" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start">¿Te parece si revisamos los avances del proyecto antes de la reunión de mañana con el cliente?</text>
  <rect x="792" y="120" width="140" height="96" fill="#FBFBFD" fill-opacity=".72"/>
  <rect x="778" y="128" width="14" height="80" fill="url(#exSobra-warn)"/>
  <rect x="304" y="272" width="412" height="64" rx="8" fill="#3A8235" fill-opacity=".08" stroke="#3A8235" stroke-width="2"/>
  <text x="312" y="320" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="400">¿Te parece si revisamos los avances del proyecto antes…</text>
  <text x="776" y="309" font-size="13" font-weight="400" fill="#79809A" text-anchor="end">10:24</text>
  <path d="M244,364 V370 H300 V364" fill="none" stroke="#556074" stroke-width="1.5"/>
  <text x="272.0" y="390" font-size="12.5" font-weight="700" fill="#556074" text-anchor="middle">fijo</text>
  <path d="M304,364 V370 H716 V364" fill="none" stroke="#3A8235" stroke-width="1.5"/>
  <text x="510.0" y="390" font-size="12.5" font-weight="700" fill="#3A8235" text-anchor="middle">Expanded: lo que sobra</text>
  <path d="M724,364 V370 H784 V364" fill="none" stroke="#556074" stroke-width="1.5"/>
  <text x="754.0" y="390" font-size="12.5" font-weight="700" fill="#556074" text-anchor="middle">fijo</text>
  <text x="48" y="162" font-size="15" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="170">Sin Expanded</text>
  <text x="48" y="184" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="170">El texto se sale.</text>
  <text x="48" y="298" font-size="15" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="170">Con Expanded</text>
  <text x="48" y="320" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="170">El texto se ajusta.</text>
</svg>
```

`Expanded` cambia el trato para un hijo: en vez de preguntarle cuánto quiere, la `Row` primero mide a los demás y a él le entrega **lo que sobra**. Con un ancho definido, el texto ya sabe dónde cortarse.

## Cómo se usa

```svg
<svg id="exCodigo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 684" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="exCodigo-ttl exCodigo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="exCodigo-ttl">Expanded dentro de una Row</title>
  <desc id="exCodigo-dsc">Una Row con un CircleAvatar, un Expanded que envuelve una Column con dos textos, y un Text con la hora. En el resultado, la foto y la hora ocupan su tamaño y la columna de textos ocupa todo el espacio que queda entre las dos.</desc>
  <defs>
    <style>
      #exCodigo .title{fill:#161A26;font-size:22px;font-weight:700}
      #exCodigo .sub{fill:#79809A;font-size:13.5px}
      #exCodigo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #exCodigo .cl{font-size:13px;fill:#C9CFDA}
      #exCodigo .s{fill:#A8D8A0} #exCodigo .n{fill:#F2B880} #exCodigo .c{fill:#7FD1E8}
      #exCodigo .p{fill:#D5B8F5} #exCodigo .k{fill:#F08FB0}
      #exCodigo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #exCodigo .ct{fill:#161A26;font-size:14px;font-weight:700}
      #exCodigo .cb{fill:#454C61;font-size:13px}
      #exCodigo .rt{fill:#161A26;font-size:14px} #exCodigo .rs{fill:#79809A;font-size:12px}
      #exCodigo .foot{fill:#79809A;font-size:12px}
      #exCodigo .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #exCodigo .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #exCodigo .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#exCodigo-ar-amber)}
      #exCodigo .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #exCodigo .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #exCodigo .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#exCodigo-ar-green)}
      #exCodigo .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #exCodigo .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #exCodigo .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#exCodigo-ar-indigo)}
    </style>
    <marker id="exCodigo-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="exCodigo-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="exCodigo-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
  </defs>
  <rect width="960" height="684" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56"><tspan class="mono">Expanded</tspan> dentro de una <tspan class="mono">Row</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Se envuelve al hijo que debe adaptarse. Los demás conservan su tamaño.</text>
  <rect x="48" y="112" width="456" height="540" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/components/chat_item.dart</text>
  <rect x="552" y="112" width="360" height="540" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="95.2" y="204" width="101.6" height="22" rx="5"/>
  <rect class="hl-green" x="95.2" y="252" width="70.4" height="22" rx="5"/>
  <rect class="hl-indigo" x="95.2" y="564" width="109.4" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="31.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Row</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">children</tspan>: [</text>
  <text class="cl mono" font-size="13" x="99.2" y="220" textLength="195.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">CircleAvatar</tspan>(<tspan class="p">radius</tspan>: <tspan class="n">24</tspan>),</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="156.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">SizedBox</tspan>(<tspan class="p">width</tspan>: <tspan class="n">12</tspan>),</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Expanded</tspan>(</text>
  <text class="cl mono" font-size="13" x="114.8" y="292" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Column</tspan>(</text>
  <text class="cl mono" font-size="13" x="130.4" y="316" textLength="351.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">crossAxisAlignment</tspan>: <tspan class="c">CrossAxisAlignment</tspan>.start,</text>
  <text class="cl mono" font-size="13" x="130.4" y="340" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">children</tspan>: [</text>
  <text class="cl mono" font-size="13" x="146.0" y="364" textLength="171.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(<tspan class="s">'Javier Montes'</tspan>),</text>
  <text class="cl mono" font-size="13" x="146.0" y="388" textLength="39.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(</text>
  <text class="cl mono" font-size="13" x="161.6" y="412" textLength="304.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">'¿Te parece si revisamos los avances?'</tspan>,</text>
  <text class="cl mono" font-size="13" x="161.6" y="436" textLength="93.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">maxLines</tspan>: <tspan class="n">1</tspan>,</text>
  <text class="cl mono" font-size="13" x="161.6" y="460" textLength="249.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">overflow</tspan>: <tspan class="c">TextOverflow</tspan>.ellipsis,</text>
  <text class="cl mono" font-size="13" x="146.0" y="484" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="130.4" y="508" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="114.8" y="532" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="99.2" y="556" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="99.2" y="580" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(<tspan class="s">'10:24'</tspan>),</text>
  <text class="cl mono" font-size="13" x="83.6" y="604" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="68.0" y="628" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<text x="180" y="150" font-size="12.5" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="320">La foto y la hora miden lo suyo.</text><text x="180" y="170" font-size="12.5" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="320">Expanded se queda con el resto.</text><rect x="12" y="268" width="336" height="64" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><circle cx="44" cy="300" r="20" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="44" cy="296.0" r="6.6" fill="#F0C572"/><path d="M31.6,314.8 a12.4,11.2 0 0 1 24.8,0 Z" fill="#F0C572"/><rect x="74" y="276" width="208" height="48" rx="8" fill="#3A8235" fill-opacity=".08" stroke="#3A8235" stroke-width="2"/><text x="84" y="296" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Javier Montes</text><text x="84" y="314" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="190">¿Te parece si revisamos…</text><text x="338" y="304" font-size="12.5" font-weight="400" fill="#79809A" text-anchor="end">10:24</text>
  </g>
  <path class="ld-amber" d="M300.2,215 H504"/>
  <path class="ar-amber" d="M504,215 H532 V444 H574"/>
  <path class="ld-green" d="M175.4,263 H504"/>
  <path class="ar-green" d="M504,263 H523 V512 H730 V472 H730"/>
  <path class="ld-indigo" d="M214.4,575 H504"/>
  <path class="ar-indigo" d="M504,575 H514 V575 H874 V460 H874"/>
</svg>
```

```dart
Row(
  children: [
    CircleAvatar(radius: 24),
    SizedBox(width: 12),
    Expanded(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('Javier Montes'),
          Text(
            '¿Te parece si revisamos los avances?',
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
          ),
        ],
      ),
    ),
    Text('10:24'),
  ],
)
```

Se envuelve al hijo que debe adaptarse, no a todos. Aquí es la `Column` de los textos: la foto y la hora conservan su tamaño.

`Expanded` solo puede ser hijo directo de una `Row` o de una `Column`. En cualquier otro lugar la consola dice `Incorrect use of ParentDataWidget`.

## Varios Expanded

Si dos hijos de la misma fila son `Expanded`, se reparten lo que sobra por partes iguales. Con `flex` cambias la proporción.

```svg
<svg id="exFlex" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 392" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="exFlex-ttl exFlex-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="exFlex-ttl">Repartir el espacio con flex</title>
  <desc id="exFlex-dsc">Tres filas del mismo ancho. En la primera, dos Expanded se reparten la fila por mitades. En la segunda, uno con flex 2 y otro con flex 1 se la reparten en dos tercios y un tercio. En la tercera, un hijo de ancho fijo conserva su tamaño y un Expanded ocupa el resto.</desc>
  <defs>
    <style>
      #exFlex .title{fill:#161A26;font-size:22px;font-weight:700}
      #exFlex .sub{fill:#79809A;font-size:13.5px}
      #exFlex .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #exFlex .nt{font-size:15px;font-weight:700;fill:#161A26}
      #exFlex .nb{fill:#454C61;font-size:13px}
      #exFlex .lbl{fill:#556074;font-size:12px;font-weight:600}
      #exFlex .foot{fill:#79809A;font-size:12px}
      #exFlex .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #exFlex .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#exFlex-arrow)}
    </style>
    <marker id="exFlex-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="392" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Repartir el espacio con <tspan class="mono">flex</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Cuando hay varios Expanded en la misma fila, se reparten lo que sobra. flex dice en qué proporción.</text>
  <text x="48" y="150" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="290">Mitad y mitad</text>
  <text x="48" y="171" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="290">Dos Expanded sin flex.</text>
  <rect x="368" y="128" width="268" height="56" rx="8" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text dy="0.35em" x="502" y="156" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono" data-fit="252">Expanded</text>
  <rect x="644" y="128" width="268" height="56" rx="8" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text dy="0.35em" x="778" y="156" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle" class="mono" data-fit="252">Expanded</text>
  <text x="48" y="230" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="290">Dos partes y una</text>
  <text x="48" y="251" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="290">El primero recibe el doble.</text>
  <rect x="368" y="208" width="357" height="56" rx="8" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text dy="0.35em" x="547" y="236" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono" data-fit="341">Expanded(flex: 2)</text>
  <rect x="733" y="208" width="179" height="56" rx="8" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text dy="0.35em" x="823" y="236" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle" class="mono" data-fit="163">Expanded(flex: 1)</text>
  <text x="48" y="310" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="290">Uno fijo y uno flexible</text>
  <text x="48" y="331" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="290">Primero se mide el fijo.</text>
  <rect x="368" y="288" width="136" height="56" rx="8" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text dy="0.35em" x="436" y="316" font-size="13" font-weight="700" fill="#556074" text-anchor="middle" class="mono" data-fit="120">ancho fijo</text>
  <rect x="512" y="288" width="400" height="56" rx="8" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text dy="0.35em" x="712" y="316" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono" data-fit="384">Expanded</text>
</svg>
```

El caso más común es el de dos botones que deben medir lo mismo:

```dart
Row(
  children: [
    Expanded(
      child: PrimaryButton(label: 'Seguir', icon: Icons.person_add),
    ),
    SizedBox(width: 12),
    Expanded(
      child: SecondaryButton(label: 'Mensaje', icon: Icons.chat),
    ),
  ],
)
```

## En una Column, y Spacer

En una `Column` funciona igual, pero a lo alto: el hijo que es `Expanded` ocupa el alto que dejan los demás.

`Spacer()` es un `Expanded` vacío. No muestra nada: solo se queda con el espacio libre y empuja lo que viene después hasta el final. Sirve para dejar un botón pegado abajo de la pantalla:

```dart
Column(
  children: [
    Text('Bienvenido'),
    Spacer(),
    PrimaryButton(label: 'Entrar', icon: Icons.login),
  ],
)
```

## Ejemplo completo

Dos botones del mismo ancho, una fila de chat con un mensaje largo y un texto empujado al fondo con `Spacer`. Quita el `Expanded` de la fila de chat para ver la franja, y ponle `flex: 2` a uno de los botones.

```dart trycode=PENDIENTE_S23
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
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              Row(
                children: [
                  Expanded(
                    child: ElevatedButton(
                      onPressed: () {
                        print('Seguir');
                      },
                      child: const Text('Seguir'),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: OutlinedButton(
                      onPressed: () {
                        print('Mensaje');
                      },
                      child: const Text('Mensaje'),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 24),
              const Row(
                children: [
                  Icon(Icons.account_circle, size: 48),
                  SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Javier Montes',
                          style: TextStyle(fontWeight: FontWeight.bold),
                        ),
                        Text(
                          '¿Te parece si revisamos los avances del proyecto antes de la reunión de mañana?',
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                        ),
                      ],
                    ),
                  ),
                  SizedBox(width: 12),
                  Text('10:24'),
                ],
              ),
              const Spacer(),
              const Text('Versión 1.0'),
            ],
          ),
        ),
      ),
    );
  }
}
```

Aquí `App` y `ProfileScreen` van en un solo archivo porque el editor en línea solo tiene uno; en tu proyecto siguen separados.
