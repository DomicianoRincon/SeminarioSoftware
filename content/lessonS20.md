# Scaffold

<!-- tags: Scaffold, appBar y body, pantalla negra con texto rojo, AppBar con actions, floatingActionButton, backgroundColor del Scaffold, Screen y Page, lib/screens, registrar una pantalla en routes, No Material widget found, Could not find a generator for route -->

En la sesión anterior hiciste siete componentes y los probaste dentro de un `Center`. Hoy los vas a encajar en pantallas de verdad, y toda pantalla empieza por el mismo widget: `Scaffold`.

## Lo que le falta a un widget suelto

¿Recuerdas la palabra *Pantalla* en rojo, con subrayado amarillo, sobre fondo negro? Así se ve cualquier widget que se muestra sin nada alrededor.

```svg
<svg id="sfSinScaffold" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="sfSinScaffold-ttl sfSinScaffold-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="sfSinScaffold-ttl">El mismo Text, sin y con Scaffold</title>
  <desc id="sfSinScaffold-dsc">Dos celulares. En el de la izquierda, un Text suelto: letras rojas con subrayado amarillo sobre fondo negro. En el de la derecha, el mismo texto dentro de un Scaffold: fondo claro, una barra con el título Inicio y el texto en el centro.</desc>
  <defs>
    <style>
      #sfSinScaffold .title{fill:#161A26;font-size:22px;font-weight:700}
      #sfSinScaffold .sub{fill:#79809A;font-size:13.5px}
      #sfSinScaffold .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #sfSinScaffold .nt{font-size:15px;font-weight:700;fill:#161A26}
      #sfSinScaffold .nb{fill:#454C61;font-size:13px}
      #sfSinScaffold .lbl{fill:#556074;font-size:12px;font-weight:600}
      #sfSinScaffold .foot{fill:#79809A;font-size:12px}
      #sfSinScaffold .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #sfSinScaffold .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#sfSinScaffold-arrow)}
    </style>
    <marker id="sfSinScaffold-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="560" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">El mismo <tspan class="mono">Text</tspan>, sin y con <tspan class="mono">Scaffold</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Un texto suelto no es una pantalla. Scaffold le pone el fondo, el estilo y un lugar a cada parte.</text>
  <clipPath id="sfSinScaffold-a"><rect width="220" height="330" rx="20"/></clipPath><rect x="143" y="125" width="234" height="344" rx="27" fill="#1F2430"/><g transform="translate(150,132)"><g clip-path="url(#sfSinScaffold-a)"><rect width="220" height="330" rx="20" fill="#000000"/><text x="14" y="40" font-size="26" font-weight="400" fill="#E53935">Pantalla</text><path d="M14,46 H112 M14,50 H112" stroke="#FFEB3B" stroke-width="1.5"/></g></g>
  <clipPath id="sfSinScaffold-b"><rect width="220" height="330" rx="20"/></clipPath><rect x="583" y="125" width="234" height="344" rx="27" fill="#1F2430"/><g transform="translate(590,132)"><g clip-path="url(#sfSinScaffold-b)"><rect width="220" height="330" rx="20" fill="#FFFFFF"/><rect width="220" height="52" fill="#F1ECF8"/><text x="18" y="31" font-size="17" font-weight="500" fill="#161A26" text-anchor="start">Inicio</text><text x="110" y="196" font-size="14" font-weight="400" fill="#161A26" text-anchor="middle">Pantalla</text></g></g>
  <path class="link" d="M400,297 H560"/>
  <text x="480" y="285" font-size="12.5" font-weight="600" fill="#556074" text-anchor="middle" data-fit="150">dentro de un Scaffold</text>
  <text x="260" y="502" font-size="15" font-weight="700" fill="#161A26" text-anchor="middle">Un Text suelto</text>
  <text x="260" y="524" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="330">Sin fondo, sin estilo de letra, sin barra.</text>
  <text x="700" y="502" font-size="15" font-weight="700" fill="#161A26" text-anchor="middle" data-fit="380">El mismo Text en el body de un Scaffold</text>
  <text x="700" y="524" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="330">Fondo, letra del tema y barra con título.</text>
</svg>
```

`Scaffold` es el andamio de la pantalla. Pone el fondo, hace que los textos tomen la letra y el color del tema, y reserva un lugar para cada parte: la barra, el contenido, los botones flotantes. Por eso es siempre el widget que devuelve el `build` de una pantalla.

## Los lugares de un Scaffold

```svg
<svg id="sfPartes" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 616" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="sfPartes-ttl sfPartes-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="sfPartes-ttl">Los lugares de un Scaffold</title>
  <desc id="sfPartes-dsc">Un Scaffold con backgroundColor, appBar, body y floatingActionButton, junto a la pantalla que produce: el color de fondo cubre toda la pantalla, la barra queda arriba, el contenido ocupa el resto y el botón flotante queda abajo a la derecha.</desc>
  <defs>
    <style>
      #sfPartes .title{fill:#161A26;font-size:22px;font-weight:700}
      #sfPartes .sub{fill:#79809A;font-size:13.5px}
      #sfPartes .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #sfPartes .cl{font-size:13px;fill:#C9CFDA}
      #sfPartes .s{fill:#A8D8A0} #sfPartes .n{fill:#F2B880} #sfPartes .c{fill:#7FD1E8}
      #sfPartes .p{fill:#D5B8F5} #sfPartes .k{fill:#F08FB0}
      #sfPartes .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #sfPartes .ct{fill:#161A26;font-size:14px;font-weight:700}
      #sfPartes .cb{fill:#454C61;font-size:13px}
      #sfPartes .rt{fill:#161A26;font-size:14px} #sfPartes .rs{fill:#79809A;font-size:12px}
      #sfPartes .foot{fill:#79809A;font-size:12px}
      #sfPartes .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #sfPartes .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #sfPartes .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#sfPartes-ar-amber)}
      #sfPartes .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #sfPartes .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #sfPartes .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#sfPartes-ar-green)}
      #sfPartes .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #sfPartes .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #sfPartes .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#sfPartes-ar-indigo)}
      #sfPartes .hl-rose{fill:#F3A3B2;fill-opacity:.16;stroke:#F3A3B2;stroke-width:1.5}
      #sfPartes .ld-rose{fill:none;stroke:#F3A3B2;stroke-width:1.5;stroke-dasharray:3 4}
      #sfPartes .ar-rose{fill:none;stroke:#C2354F;stroke-width:1.75;marker-end:url(#sfPartes-ar-rose)}
    </style>
    <marker id="sfPartes-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="sfPartes-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="sfPartes-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="sfPartes-ar-rose" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/></marker>
  </defs>
  <rect width="960" height="616" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Los lugares de un <tspan class="mono">Scaffold</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Cada propiedad es un lugar fijo de la pantalla. Tú decides qué widget va en cada uno.</text>
  <rect x="48" y="112" width="456" height="472" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/profile_screen.dart</text>
  <rect x="552" y="112" width="360" height="472" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="79.6" y="180" width="125.0" height="22" rx="5"/>
  <rect class="hl-amber" x="79.6" y="204" width="54.8" height="22" rx="5"/>
  <rect class="hl-green" x="79.6" y="228" width="39.2" height="22" rx="5"/>
  <rect class="hl-rose" x="79.6" y="300" width="164.0" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="c">Scaffold</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="296.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">backgroundColor</tspan>: <tspan class="c">Colors</tspan>.grey.shade100,</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="343.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">appBar</tspan>: <tspan class="c">AppBar</tspan>(<tspan class="p">title</tspan>: <tspan class="k">const</tspan> <tspan class="c">Text</tspan>(<tspan class="s">'Perfil'</tspan>)),</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">body</tspan>: <tspan class="k">const</tspan> <tspan class="c">Center</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="195.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Text</tspan>(<tspan class="s">'Contenido'</tspan>),</text>
  <text class="cl mono" font-size="13" x="83.6" y="292" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="83.6" y="316" textLength="335.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">floatingActionButton</tspan>: <tspan class="c">FloatingActionButton</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="340" textLength="117.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">onPressed</tspan>: () {</text>
  <text class="cl mono" font-size="13" x="114.8" y="364" textLength="117.0" lengthAdjust="spacingAndGlyphs" data-fit="432">print(<tspan class="s">'Nuevo'</tspan>);</text>
  <text class="cl mono" font-size="13" x="99.2" y="388" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">},</text>
  <text class="cl mono" font-size="13" x="99.2" y="412" textLength="226.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="k">const</tspan> <tspan class="c">Icon</tspan>(<tspan class="c">Icons</tspan>.add),</text>
  <text class="cl mono" font-size="13" x="83.6" y="436" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="68.0" y="460" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">);</text>
  <g transform="translate(552,144)">
<rect x="78" y="22" width="204" height="396" rx="26" fill="#F0F1F4" stroke="#2A3040" stroke-width="3"/><rect x="84" y="28" width="192" height="384" rx="20" fill="#4453C9" fill-opacity=".08" stroke="#4453C9" stroke-width="2"/><rect x="92" y="44" width="176" height="54" rx="12" fill="#A96C05" fill-opacity=".08" stroke="#A96C05" stroke-width="2"/><text dy="0.35em" x="108" y="71" font-size="17" font-weight="500" fill="#161A26" text-anchor="start">Perfil</text><rect x="92" y="106" width="176" height="298" rx="12" fill="#3A8235" fill-opacity=".08" stroke="#3A8235" stroke-width="2"/><text x="180" y="220" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="middle">Contenido</text><rect x="212" y="346" width="48" height="48" rx="14" fill="#FFEBEF" stroke="#C2354F" stroke-width="2"/><path d="M236,360 V380 M226,370 H246" stroke="#C2354F" stroke-width="2.5" stroke-linecap="round"/>
  </g>
  <path class="ld-indigo" d="M386.0,191 H504"/>
  <path class="ar-indigo" d="M504,191 H636"/>
  <path class="ld-amber" d="M432.8,215 H504"/>
  <path class="ar-amber" d="M504,215 H644"/>
  <path class="ld-green" d="M237.8,239 H504"/>
  <path class="ar-green" d="M504,239 H532 V394 H644"/>
  <path class="ld-rose" d="M425.0,311 H504"/>
  <path class="ar-rose" d="M504,311 H514 V514 H764"/>
</svg>
```

```dart
return Scaffold(
  backgroundColor: Colors.grey.shade100,
  appBar: AppBar(title: const Text('Perfil')),
  body: const Center(
    child: Text('Contenido'),
  ),
  floatingActionButton: FloatingActionButton(
    onPressed: () {
      print('Nuevo');
    },
    child: const Icon(Icons.add),
  ),
);
```

Todos los lugares son opcionales. El único que usas siempre es `body`, que ocupa lo que dejan libre los demás. Si quitas `appBar`, el contenido sube hasta el borde de arriba; si quitas `floatingActionButton`, simplemente no hay botón.

Hay un lugar más, `bottomNavigationBar`, para la barra de secciones de abajo. Cómo se ve está en la lección *BottomNavigationBar*; hacerla funcionar es la sesión 9.

## La barra de arriba

En `appBar` casi siempre va un `AppBar`. Su `title` es el nombre de la pantalla, y en `actions` caben los botones de la derecha:

```dart
AppBar(
  title: const Text('Perfil'),
  actions: [
    IconButton(
      onPressed: () {
        print('Ajustes');
      },
      icon: const Icon(Icons.settings),
    ),
  ],
)
```

Lo demás que cabe en la barra está en la lección *AppBar*.

No toda pantalla lleva barra. Una de inicio de sesión, por ejemplo, no la tiene, y eso trae un problema que resuelve la lección siguiente.

## Una pantalla es una Screen

En este curso, lo que tiene `Scaffold` se llama **Screen**. Es una pantalla entera, vive en `lib/screens/`, su clase termina en `Screen` y se abre por su nombre en `routes`.

```svg
<svg id="sfScreen" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 500" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="sfScreen-ttl sfScreen-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="sfScreen-ttl">Screen y Page</title>
  <desc id="sfScreen-dsc">Dos celulares. El de la izquierda es una Screen: un Scaffold completo, con su barra y su contenido, en lib/screens. El de la derecha muestra una Page: solo la zona de contenido, sin Scaffold, dentro de una Screen que tiene una barra de navegación abajo; vive en lib/pages y se ve en la sesión 9.</desc>
  <defs>
    <style>
      #sfScreen .title{fill:#161A26;font-size:22px;font-weight:700}
      #sfScreen .sub{fill:#79809A;font-size:13.5px}
      #sfScreen .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #sfScreen .nt{font-size:15px;font-weight:700;fill:#161A26}
      #sfScreen .nb{fill:#454C61;font-size:13px}
      #sfScreen .lbl{fill:#556074;font-size:12px;font-weight:600}
      #sfScreen .foot{fill:#79809A;font-size:12px}
      #sfScreen .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #sfScreen .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#sfScreen-arrow)}
    </style>
    <marker id="sfScreen-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="500" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Screen y Page</text>
  <text class="sub" x="48" y="80" data-fit="860">Si tiene Scaffold, es una Screen. Una Page es un pedazo de pantalla que una Screen hospeda.</text>
  <clipPath id="sfScreen-a"><rect width="180" height="300" rx="20"/></clipPath><rect x="81" y="129" width="194" height="314" rx="27" fill="#1F2430"/><g transform="translate(88,136)"><g clip-path="url(#sfScreen-a)"><rect width="180" height="300" rx="20" fill="#FFFFFF"/><rect width="180" height="44" fill="#F1ECF8"/><text x="16" y="27" font-size="15" font-weight="500" fill="#161A26" text-anchor="start">Perfil</text><rect x="20" y="70" width="140" height="10" rx="5" fill="#D9DEE8"/><rect x="20" y="92" width="110" height="10" rx="5" fill="#D9DEE8"/><rect x="20" y="114" width="126" height="10" rx="5" fill="#D9DEE8"/><rect x="20" y="160" width="140" height="10" rx="5" fill="#D9DEE8"/><rect x="20" y="182" width="90" height="10" rx="5" fill="#D9DEE8"/><rect x="3" y="3" width="174" height="294" rx="18" fill="#4453C9" fill-opacity=".08" stroke="#4453C9" stroke-width="2"/></g></g>
  <clipPath id="sfScreen-b"><rect width="180" height="300" rx="20"/></clipPath><rect x="529" y="129" width="194" height="314" rx="27" fill="#1F2430"/><g transform="translate(536,136)"><g clip-path="url(#sfScreen-b)"><rect width="180" height="300" rx="20" fill="#FFFFFF"/><rect width="180" height="44" fill="#F1ECF8"/><text x="16" y="27" font-size="15" font-weight="500" fill="#161A26" text-anchor="start">Inicio</text><rect y="252" width="180" height="48" fill="#F1ECF8"/><circle cx="36" cy="276" r="7" fill="#7439B8"/><circle cx="90" cy="276" r="7" fill="#C4CBD8"/><circle cx="144" cy="276" r="7" fill="#C4CBD8"/><rect x="20" y="70" width="140" height="10" rx="5" fill="#D9DEE8"/><rect x="20" y="92" width="110" height="10" rx="5" fill="#D9DEE8"/><rect x="20" y="114" width="126" height="10" rx="5" fill="#D9DEE8"/><rect x="20" y="160" width="140" height="10" rx="5" fill="#D9DEE8"/><rect x="20" y="182" width="90" height="10" rx="5" fill="#D9DEE8"/><rect x="6" y="50" width="168" height="196" rx="10" fill="#0F8478" fill-opacity=".08" stroke="#0F8478" stroke-width="2" stroke-dasharray="6 4"/></g></g>
  <text x="300" y="152" font-size="17" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="180">ProfileScreen</text>
  <text x="300" y="176" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" class="mono" data-fit="180">lib/screens/</text>
  <text x="300" y="222" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="180">Tiene Scaffold</text>
  <text x="300" y="242" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="180">Es la pantalla entera.</text>
  <text x="300" y="284" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="180">Se abre por su ruta</text>
  <text x="300" y="304" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="180">Está en routes.</text>
  <text x="300" y="346" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="180">Desde hoy</text>
  <text x="300" y="366" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="180">Todas tus pantallas.</text>
  <text x="748" y="152" font-size="17" font-weight="700" fill="#0F8478" text-anchor="start" class="mono" data-fit="180">FeedPage</text>
  <text x="748" y="176" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" class="mono" data-fit="180">lib/pages/</text>
  <text x="748" y="222" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="180">No tiene Scaffold</text>
  <text x="748" y="242" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="180">Solo el contenido.</text>
  <text x="748" y="284" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="180">La hospeda una Screen</text>
  <text x="748" y="304" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="180">No tiene ruta propia.</text>
  <text x="748" y="346" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="180">Sesión 9</text>
  <text x="748" y="366" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="180">Con la barra de abajo.</text>
  <path d="M480,128 V444" stroke="#D9DEE8" stroke-width="1.5" stroke-dasharray="4 5"/>
</svg>
```

Una **Page** es otra cosa: un pedazo de contenido sin `Scaffold`, que una Screen muestra dentro de su `body`. Aparece cuando una pantalla tiene secciones, en la sesión 9. Hasta entonces todo lo que hagas es una Screen.

Crea tu segunda pantalla, `lib/screens/profile_screen.dart`:

```dart
import 'package:flutter/material.dart';

/// Profile of a person.
class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey.shade100,
      appBar: AppBar(title: const Text('Perfil')),
      body: const Center(
        child: Text('Contenido'),
      ),
    );
  }
}
```

Regístrala en `lib/main.dart` y dile a la app que arranque en ella:

```dart
import 'package:flutter/material.dart';
import 'package:miapp1/screens/home_screen.dart';
import 'package:miapp1/screens/profile_screen.dart';
```

```dart
initialRoute: '/profile',
routes: {
  '/home': (context) => const HomeScreen(),
  '/profile': (context) => const ProfileScreen(),
},
```

Los `import` siguen la regla de siempre: `package:miapp1/`, el nombre de tu proyecto, y la ruta del archivo desde `lib/`. La dirección es la misma sin importar desde qué carpeta escribas.

Todavía no hay forma de pasar de una pantalla a otra tocando un botón: eso es la sesión 8. Por ahora, para ver otra pantalla cambias `initialRoute` y reinicias la app.

`ProfileScreen` es tu banco de pruebas de hoy. En cada lección le agregas algo, y en el taller la terminas.

## Ejemplo completo

Una pantalla con los cuatro lugares ocupados. Quita `appBar` o `floatingActionButton` y mira cómo `body` toma el espacio que queda libre.

```dart trycode=PENDIENTE_S20
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
      appBar: AppBar(
        title: const Text('Perfil'),
        actions: [
          IconButton(
            onPressed: () {
              print('Ajustes');
            },
            icon: const Icon(Icons.settings),
          ),
        ],
      ),
      body: const Center(
        child: Text('Contenido'),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          print('Nuevo');
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}
```

Aquí `App` y `ProfileScreen` van en un solo archivo porque el editor en línea solo tiene uno; en tu proyecto siguen separados.
