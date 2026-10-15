# Estado: StatelessWidget frente a StatefulWidget

<!-- tags: StatefulWidget, estado de un widget, createState, clase State, StatelessWidget vs StatefulWidget, por qué el estado no va en el widget, campos final, _HomeScreenState, la pantalla no cambia, Stateful Widget -->

Hasta ahora tus pantallas muestran siempre lo mismo: el perfil de la sesión 3 se ve igual la primera vez que se abre y la décima. Una app de verdad cambia mientras la usas. Un contador sube, un campo muestra lo que escribes y una lista crece. A todo lo que puede cambiar mientras la pantalla está abierta se le llama **estado**.

## Qué es el estado

El estado son los **datos que cambian mientras la pantalla está abierta** y que la pantalla tiene que mostrar. Unos ejemplos:

- cuántas veces se pulsó un botón;
- si un bombillo está encendido o apagado;
- lo que alguien escribió en un campo;
- las canciones que lleva una playlist.

El título de la barra o el texto de un botón no son estado, porque no cambian. Una buena pregunta para distinguirlos es: *¿esto puede valer distinto dentro de un minuto, sin salir de la pantalla?* Si la respuesta es sí, es estado.

Mira una app de música con sus datos cargados. A la derecha está su estado: la canción que suena, si está sonando, cuántos "me gusta" tiene y la lista que sigue. Cada flecha llega a la parte de la pantalla que muestra ese dato.

```svg
<svg id="ewPantalla" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 640" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ewPantalla-ttl ewPantalla-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ewPantalla-ttl">El estado detrás de una pantalla</title>
  <desc id="ewPantalla-dsc">Un reproductor de música en un celular: la barra con el título Mi playlist, la canción que suena (Levitating, de Dua Lipa), un botón de pausa, 12 me gusta y una lista de tres canciones. A la derecha, la sección Estado con cuatro variables, cada una con una flecha de su color hacia la parte de la pantalla que la muestra: _current a la canción que suena, _isPlaying al botón de pausa, _likes al contador de me gusta y _songs a la lista. Una nota gris señala que el título de la barra no es estado porque nunca cambia.</desc>
  <defs>
    <style>
      #ewPantalla .title{fill:#161A26;font-size:22px;font-weight:700}
      #ewPantalla .sub{fill:#79809A;font-size:13.5px}
      #ewPantalla .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ewPantalla .nt{font-size:15px;font-weight:700;fill:#161A26}
      #ewPantalla .nb{fill:#454C61;font-size:13px}
      #ewPantalla .lbl{fill:#556074;font-size:12px;font-weight:600}
      #ewPantalla .foot{fill:#79809A;font-size:12px}
      #ewPantalla .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ewPantalla .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#ewPantalla-arrow)}
    </style>
    <marker id="ewPantalla-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="ewPantalla-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker><marker id="ewPantalla-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker><marker id="ewPantalla-rose" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/></marker><marker id="ewPantalla-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#0F8478"/></marker><marker id="ewPantalla-slate" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#79809A"/></marker>
    <linearGradient id="ewPantalla-cover" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B69DF8"/><stop offset="1" stop-color="#6750A4"/></linearGradient>
  </defs>
  <rect width="960" height="640" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">El estado detrás de una pantalla</text>
  <text class="sub" x="48" y="80" data-fit="860">A la izquierda, la app con sus datos. A la derecha, los datos que pueden cambiar: el estado.</text>
  <rect x="86" y="102" width="340" height="476" rx="36" fill="#1F2430"/>
  <rect x="96" y="112" width="320" height="456" rx="26" fill="#FEF7FF"/>
  <path d="M96,138 A26,26 0 0 1 122,112 H390 A26,26 0 0 1 416,138 V168 H96 Z" fill="#D0BCFF"/>
  <text x="114" y="149" font-size="17" font-weight="500" fill="#161A26" text-anchor="start">Mi playlist</text>
  <rect x="110" y="196" width="292" height="148" rx="16" fill="#FFFFFF" stroke="#E6E0F2"/>
  <rect x="124" y="208" width="56" height="56" rx="12" fill="url(#ewPantalla-cover)"/><circle cx="162.1" cy="225.9" r="6.7" fill="#FFFFFF" fill-opacity=".7"/><path d="M124,253.9 L144.2,236.0 L158.7,248.3 L167.7,241.6 L180,252.8 V252 A12,12 0 0 1 168,264 H136 A12,12 0 0 1 124,252 Z" fill="#FFFFFF" fill-opacity=".35"/>
  <text x="122" y="188" font-size="11" font-weight="700" fill="#625B71" text-anchor="start">SONANDO AHORA</text>
  <text x="194" y="230" font-size="16" font-weight="700" fill="#161A26" text-anchor="start">Levitating</text>
  <text x="194" y="250" font-size="13" font-weight="400" fill="#625B71" text-anchor="start">Dua Lipa</text>
  <circle cx="256.0" cy="290" r="20" fill="#6750A4"/>
  <rect x="249.0" y="281" width="5" height="18" rx="1.5" fill="#FFFFFF"/><rect x="258.0" y="281" width="5" height="18" rx="1.5" fill="#FFFFFF"/>
  <path d="M130,331 l-6,-6 a3.6,3.6 0 0 1 6,-4 a3.6,3.6 0 0 1 6,4 Z" fill="#C2354F"/>
  <text x="142" y="330" font-size="13" font-weight="600" fill="#C2354F" text-anchor="start">12 me gusta</text>
  <text x="114" y="376" font-size="13" font-weight="700" fill="#49454F" text-anchor="start">Siguiente en la lista</text>
  <rect x="110" y="388" width="292" height="46" rx="12" fill="#FFFFFF" stroke="#E6E0F2"/>
  <rect x="118" y="395" width="32" height="32" rx="7" fill="url(#ewPantalla-cover)"/><circle cx="139.8" cy="405.2" r="3.8" fill="#FFFFFF" fill-opacity=".7"/><path d="M118,421.2 L129.5,411.0 L137.8,418.0 L143.0,414.2 L150,420.6 V420 A7,7 0 0 1 143,427 H125 A7,7 0 0 1 118,420 Z" fill="#FFFFFF" fill-opacity=".35"/>
  <text x="162" y="409" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Imagine</text>
  <text x="162" y="425" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">John Lennon</text>
  <rect x="110" y="442" width="292" height="46" rx="12" fill="#FFFFFF" stroke="#E6E0F2"/>
  <rect x="118" y="449" width="32" height="32" rx="7" fill="url(#ewPantalla-cover)"/><circle cx="139.8" cy="459.2" r="3.8" fill="#FFFFFF" fill-opacity=".7"/><path d="M118,475.2 L129.5,465.0 L137.8,472.0 L143.0,468.2 L150,474.6 V474 A7,7 0 0 1 143,481 H125 A7,7 0 0 1 118,474 Z" fill="#FFFFFF" fill-opacity=".35"/>
  <text x="162" y="463" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Yellow</text>
  <text x="162" y="479" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">Coldplay</text>
  <rect x="110" y="496" width="292" height="46" rx="12" fill="#FFFFFF" stroke="#E6E0F2"/>
  <rect x="118" y="503" width="32" height="32" rx="7" fill="url(#ewPantalla-cover)"/><circle cx="139.8" cy="513.2" r="3.8" fill="#FFFFFF" fill-opacity=".7"/><path d="M118,529.2 L129.5,519.0 L137.8,526.0 L143.0,522.2 L150,528.6 V528 A7,7 0 0 1 143,535 H125 A7,7 0 0 1 118,528 Z" fill="#FFFFFF" fill-opacity=".35"/>
  <text x="162" y="517" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Bohemian Rhapsody</text>
  <text x="162" y="533" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">Queen</text>
  <rect x="504" y="150" width="424" height="324" rx="16" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="2"/>
  <text x="524" y="178" font-size="13" font-weight="700" fill="#7439B8" text-anchor="start" class="h">ESTADO</text>
  <text x="596" y="178" font-size="12" font-weight="400" fill="#625B71" text-anchor="start" class="mono">vive en _PlayerScreenState</text>
  <path d="M520,192 H912" stroke="#C9A6EE" stroke-width="1.5"/>
  <rect x="520" y="206" width="392" height="32" rx="8" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="534" y="227" font-size="13" font-weight="700" fill="#7439B8" text-anchor="start" class="mono">Song _current</text>
  <rect x="724" y="211" width="180" height="22" rx="6" fill="#FFFFFF" stroke="#C9A6EE"/>
  <text x="814" y="226.5" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="middle" class="mono" data-fit="168">Song('Levitating', …)</text>
  <path d="M520,222 H408" fill="none" stroke="#7439B8" stroke-width="2" marker-end="url(#ewPantalla-violet)"/>
  <circle cx="520" cy="222" r="3.5" fill="#7439B8"/>
  <rect x="520" y="274" width="392" height="32" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="534" y="295" font-size="13" font-weight="700" fill="#A96C05" text-anchor="start" class="mono">bool _isPlaying</text>
  <rect x="724" y="279" width="180" height="22" rx="6" fill="#FFFFFF" stroke="#F0C572"/>
  <text x="814" y="294.5" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="middle" class="mono" data-fit="168">true</text>
  <path d="M520,290 H286.0" fill="none" stroke="#A96C05" stroke-width="2" marker-end="url(#ewPantalla-amber)"/>
  <circle cx="520" cy="290" r="3.5" fill="#A96C05"/>
  <rect x="520" y="310" width="392" height="32" rx="8" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/>
  <text x="534" y="331" font-size="13" font-weight="700" fill="#C2354F" text-anchor="start" class="mono">int _likes</text>
  <rect x="724" y="315" width="180" height="22" rx="6" fill="#FFFFFF" stroke="#F3A3B2"/>
  <text x="814" y="330.5" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="middle" class="mono" data-fit="168">12</text>
  <path d="M520,326 H232" fill="none" stroke="#C2354F" stroke-width="2" marker-end="url(#ewPantalla-rose)"/>
  <circle cx="520" cy="326" r="3.5" fill="#C2354F"/>
  <rect x="520" y="426" width="392" height="32" rx="8" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="534" y="447" font-size="13" font-weight="700" fill="#0F8478" text-anchor="start" class="mono">List&lt;Song&gt; _songs</text>
  <rect x="724" y="431" width="180" height="22" rx="6" fill="#FFFFFF" stroke="#86D3CA"/>
  <text x="814" y="446.5" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="middle" class="mono" data-fit="168">3 canciones</text>
  <path d="M520,442 H408" fill="none" stroke="#0F8478" stroke-width="2" marker-end="url(#ewPantalla-teal)"/>
  <circle cx="520" cy="442" r="3.5" fill="#0F8478"/>
  <path d="M402,380 H410 V542 H402" fill="none" stroke="#0F8478" stroke-width="2"/>
  <path d="M402,200 H408 V266 H402" fill="none" stroke="#7439B8" stroke-width="2"/>
  <text x="520" y="128" font-size="12.5" font-weight="400" fill="#79809A" text-anchor="start">No es estado: el título nunca cambia</text>
  <path d="M512,124 H360 V144 H198" fill="none" stroke="#79809A" stroke-width="1.5" stroke-dasharray="4 4" marker-end="url(#ewPantalla-slate)"/>
  <text x="520" y="504" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="392">Cada flecha va de un dato a la parte de la pantalla</text>
  <text x="520" y="524" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="392">que lo muestra. Si el dato cambia, esa parte cambia.</text>
  <text x="48" y="612" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="864">El estado vive en el objeto State de la pantalla. El build() lo lee para dibujar.</text>
</svg>
```

Cuando alguien pulsa pausa, cambia `_isPlaying` y con él el botón. Cuando da "me gusta", cambia `_likes` y con él el número. La pantalla no se cambia a mano: se cambia el dato, y la pantalla lo muestra.

## Dos tipos de widget

Los componentes que hiciste en la sesión 2 eran `StatelessWidget`: reciben sus datos por el constructor, los guardan en campos `final` y los dibujan. No pueden cambiar por sí solos. Para algo que cambia, Flutter tiene el `StatefulWidget`, que se parte en dos clases:

- **El widget** (`HomeScreen`) solo guarda la configuración. Flutter lo puede tirar y crear otro en cualquier momento.
- **El State** (`_HomeScreenState`) guarda los datos que cambian y tiene el `build()`. Vive mientras la pantalla esté montada.

## Las dos clases en código

```svg
<svg id="ewAnatomia" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 588" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ewAnatomia-ttl ewAnatomia-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ewAnatomia-ttl">Las dos clases de un StatefulWidget</title>
  <desc id="ewAnatomia-dsc">El código de HomeScreen, que hereda de StatefulWidget y en createState devuelve un _HomeScreenState. El State tiene el campo _isOn y el método build. Cuatro tarjetas explican el widget, createState, los datos que cambian y build.</desc>
  <defs>
    <style>
      #ewAnatomia .title{fill:#161A26;font-size:22px;font-weight:700}
      #ewAnatomia .sub{fill:#79809A;font-size:13.5px}
      #ewAnatomia .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ewAnatomia .cl{font-size:13px;fill:#C9CFDA}
      #ewAnatomia .s{fill:#A8D8A0} #ewAnatomia .n{fill:#F2B880} #ewAnatomia .c{fill:#7FD1E8}
      #ewAnatomia .p{fill:#D5B8F5} #ewAnatomia .k{fill:#F08FB0}
      #ewAnatomia .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ewAnatomia .ct{fill:#161A26;font-size:14px;font-weight:700}
      #ewAnatomia .cb{fill:#454C61;font-size:13px}
      #ewAnatomia .rt{fill:#161A26;font-size:14px} #ewAnatomia .rs{fill:#79809A;font-size:12px}
      #ewAnatomia .foot{fill:#79809A;font-size:12px}
      #ewAnatomia .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #ewAnatomia .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #ewAnatomia .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#ewAnatomia-ar-amber)}
      #ewAnatomia .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #ewAnatomia .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #ewAnatomia .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#ewAnatomia-ar-green)}
      #ewAnatomia .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #ewAnatomia .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #ewAnatomia .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#ewAnatomia-ar-indigo)}
      #ewAnatomia .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #ewAnatomia .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #ewAnatomia .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#ewAnatomia-ar-violet)}
    </style>
    <marker id="ewAnatomia-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="ewAnatomia-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="ewAnatomia-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="ewAnatomia-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="588" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las dos clases de un <tspan class="mono">StatefulWidget</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">El widget se declara arriba y el State abajo. El estado y el build van en el State.</text>
  <rect x="48" y="112" width="456" height="444" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/home_screen.dart</text>
  <rect x="552" y="112" width="360" height="444" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">QUÉ HACE CADA PARTE</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="259.0" y="156" width="117.2" height="22" rx="5"/>
  <rect class="hl-amber" x="220.0" y="252" width="93.8" height="22" rx="5"/>
  <rect class="hl-violet" x="118.6" y="372" width="47.0" height="22" rx="5"/>
  <rect class="hl-green" x="134.2" y="444" width="47.0" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="319.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">class</tspan> <tspan class="c">HomeScreen</tspan> <tspan class="k">extends</tspan> <tspan class="c">StatefulWidget</tspan> {</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="234.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">const</tspan> <tspan class="c">HomeScreen</tspan>({<tspan class="k">super</tspan>.key});</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">@override</tspan></text>
  <text class="cl mono" font-size="13" x="83.6" y="268" textLength="265.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">State</tspan>&lt;<tspan class="c">HomeScreen</tspan>&gt; createState() =&gt;</text>
  <text class="cl mono" font-size="13" x="114.8" y="292" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432">_HomeScreenState();</text>
  <text class="cl mono" font-size="13" x="68.0" y="316" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="364" textLength="390.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">class</tspan> _HomeScreenState <tspan class="k">extends</tspan> <tspan class="c">State</tspan>&lt;<tspan class="c">HomeScreen</tspan>&gt; {</text>
  <text class="cl mono" font-size="13" x="83.6" y="388" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432">bool _isOn = <tspan class="k">false</tspan>;</text>
  <text class="cl mono" font-size="13" x="83.6" y="436" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">@override</tspan></text>
  <text class="cl mono" font-size="13" x="83.6" y="460" textLength="280.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Widget</tspan> build(<tspan class="c">BuildContext</tspan> context) {</text>
  <text class="cl mono" font-size="13" x="99.2" y="484" textLength="257.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="c">Text</tspan>(_isOn ? <tspan class="s">'Sí'</tspan> : <tspan class="s">'No'</tspan>);</text>
  <text class="cl mono" font-size="13" x="83.6" y="508" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="532" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <g transform="translate(552,144)">
<g transform="translate(16,16)"><rect width="328" height="72" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#4453C9" data-fit="300">El widget</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Hereda de StatefulWidget. Solo guarda</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">la configuración: aquí no va el estado.</text></g><g transform="translate(16,112)"><rect width="328" height="72" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#A96C05" data-fit="300">createState()</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Flutter lo llama una vez y conecta</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">el widget con su objeto State.</text></g><g transform="translate(16,208)"><rect width="328" height="72" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#7439B8" data-fit="300">Los datos que cambian</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Campos normales del State, sin final.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">Por convención empiezan con _.</text></g><g transform="translate(16,304)"><rect width="328" height="72" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#3A8235" data-fit="300">build() vive en el State</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Lee los campos y dibuja la pantalla</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">con lo que valen en ese momento.</text></g>
  </g>
  <path class="ld-indigo" d="M393.8,167 H504"/>
  <path class="ar-indigo" d="M504,167 H514 V190 H568"/>
  <path class="ld-amber" d="M354.8,263 H504"/>
  <path class="ar-amber" d="M504,263 H514 V286 H568"/>
  <path class="ld-violet" d="M237.8,383 H504"/>
  <path class="ar-violet" d="M504,383 H514 V382 H568"/>
  <path class="ld-green" d="M370.4,455 H504"/>
  <path class="ar-green" d="M504,455 H514 V478 H568"/>
</svg>
```

```dart
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() =>
      _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool _isOn = false;

  @override
  Widget build(BuildContext context) {
    return Text(_isOn ? 'Sí' : 'No');
  }
}
```

Tres detalles que vale la pena notar:

- El nombre del State es el del widget con `_` delante y `State` al final. El `_` lo hace **privado**: solo se usa dentro de este archivo.
- `createState()` es lo único que hace el widget. Flutter lo llama una vez y conecta el widget con su State.
- Los campos del State **no** son `final`: están ahí justamente para cambiar.

No hace falta escribir las dos clases a mano. En VS Code escribe `stful` y pulsa Enter: el editor genera el esqueleto y tú solo pones el nombre.

## Por qué el estado vive en el State

Podría parecer más simple guardar el dato en el widget. El problema es que **Flutter crea widgets nuevos todo el tiempo**: cada vez que el padre se reconstruye, tu `HomeScreen` se descarta y se crea otro objeto. El State, en cambio, se conserva: Flutter se lo conecta al widget nuevo.

Pruébalo con el bombillo del ejemplo de esta lección. A la derecha está el árbol de widgets y, debajo, la sección **Estado**: ahí vive `_isOn`, dentro del objeto `_HomeScreenState`. Las líneas la unen con los tres widgets que la usan: el `Icon`, el `Text` y el `FilledButton`.

1. Pulsa *Encender* y sigue los pasos. Mira los números de objeto (`#n`): los widgets cambian de número en cada `build()`.
2. Ahora pulsa *Reconstruir App*. `HomeScreen` cambia de número, pero `_HomeScreenState` conserva el suyo, y `_isOn` sigue en `true`.

```interactive
state-tree bulb
```

Si `_isOn` fuera un campo del widget, se iría con el `HomeScreen` viejo cada vez que el padre se reconstruye, y el bombillo volvería a apagarse solo. Además, un `StatelessWidget` no tiene cómo pedir que lo vuelvan a dibujar. Por eso el estado vive en el State.

Activa *Paso a paso* si quieres avanzar tú, con *Siguiente paso*. Qué hace `setState` en cada paso se ve con calma en la siguiente lección.

## Cuándo usar cada uno

- **`StatelessWidget`** para lo que solo muestra lo que recibe: botones, tarjetas, filas. Es lo normal en `lib/components/`.
- **`StatefulWidget`** cuando algo de la pantalla cambia mientras está abierta. En esta sesión, las Screens.

Empieza siempre por `StatelessWidget` y cámbialo solo si aparece un dato que cambia.

## Ejemplo completo

Un bombillo que se enciende y se apaga. `_isOn` es el estado. La función `_toggle` lo cambia dentro de `setState`, que es el tema de la siguiente lección. En tu proyecto, `App` y `HomeScreen` van en archivos separados; aquí están juntos para que corra en DartPad.

```dart trycode=5c03ad650ab4dd52d7fbac0cee78ec9c
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
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      routes: {
        '/': (context) => const HomeScreen(),
      },
    );
  }
}

/// Screen with a light bulb that turns on and off.
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool _isOn = false;

  void _toggle() {
    setState(() {
      _isOn = !_isOn;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Bombillo')),
      body: SafeArea(
        child: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(
                _isOn ? Icons.lightbulb : Icons.lightbulb_outline,
                size: 96,
                color: _isOn ? Colors.amber : Colors.grey,
              ),
              const SizedBox(height: 16),
              Text(_isOn ? 'Encendido' : 'Apagado'),
              const SizedBox(height: 16),
              FilledButton(
                onPressed: () => _toggle(),
                child: Text(_isOn ? 'Apagar' : 'Encender'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```
