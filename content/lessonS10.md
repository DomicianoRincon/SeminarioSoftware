# El proyecto por dentro

<!-- tags: main.dart, runApp, MaterialApp, estructura de carpetas, declarativo frente a imperativo, rutas nombradas, lib/components, initialRoute, interfaz como función del estado, Could not find a generator for route, Scaffold, texto rojo con subrayado amarillo -->

**Presentación de la sesión:** [Componentes](https://domicianorincon.github.io/SeminarioSoftware/presentaciones/2/)

En la sesión anterior creaste `miapp1` y la viste correr. Antes de escribir tu primer widget conviene saber dónde está cada cosa: qué carpetas hay, qué hace `main.dart` y por qué en Flutter la interfaz se **describe** en lugar de irse modificando.

## Las carpetas

`flutter create` deja muchas carpetas, pero casi todo tu trabajo ocurre en una sola: `lib/`.

```svg
<svg id="ppCarpetas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 636" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ppCarpetas-ttl ppCarpetas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ppCarpetas-ttl">Las carpetas del proyecto</title>
  <desc id="ppCarpetas-dsc">Árbol de carpetas de un proyecto Flutter: lib con main.dart, theme, models, components, screens y pages; assets; pubspec.yaml; y las carpetas de plataforma. Se destaca components, que es donde se trabaja en esta sesión.</desc>
  <defs>
    <style>
      #ppCarpetas .title{fill:#161A26;font-size:22px;font-weight:700}
      #ppCarpetas .sub{fill:#79809A;font-size:13.5px}
      #ppCarpetas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ppCarpetas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #ppCarpetas .nb{fill:#454C61;font-size:13px}
      #ppCarpetas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #ppCarpetas .foot{fill:#79809A;font-size:12px}
      #ppCarpetas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ppCarpetas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#ppCarpetas-arrow)}
    </style>
    <marker id="ppCarpetas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="636" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las carpetas del proyecto</text>
  <text class="sub" x="48" y="80" data-fit="860">Flutter crea las de afuera. Las que están dentro de lib/ las creas tú, y cada una guarda una sola cosa.</text>
  <rect x="48" y="104" width="312" height="464" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect x="68" y="122" width="79" height="28" rx="8" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text class="mono" x="80" y="136" dy="0.35em" font-size="13" font-weight="600" fill="#556074" data-fit="63">miapp1/</text>
  <path d="M155,136 H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>
  <text x="396" y="136" dy="0.35em" font-size="14" font-weight="400" fill="#454C61" data-fit="516">La carpeta del proyecto</text>
  <path d="M80,152.0 V176 H92" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <rect x="96" y="162" width="55" height="28" rx="8" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text class="mono" x="108" y="176" dy="0.35em" font-size="13" font-weight="600" fill="#4453C9" data-fit="39">lib/</text>
  <path d="M159,176 H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>
  <text x="396" y="176" dy="0.35em" font-size="14" font-weight="400" fill="#454C61" data-fit="516">Tu código Dart. Aquí pasas casi todo el tiempo</text>
  <path d="M108,192.0 V216 H120" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <rect x="124" y="202" width="94" height="28" rx="4" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text class="mono" x="136" y="216" dy="0.35em" font-size="13" font-weight="600" fill="#4453C9" data-fit="78">main.dart</text>
  <path d="M226,216 H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>
  <text x="396" y="216" dy="0.35em" font-size="14" font-weight="400" fill="#454C61" data-fit="516">Punto de entrada: arranca la app y declara las rutas</text>
  <path d="M108,232.0 V256 H120" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <rect x="124" y="242" width="71" height="28" rx="8" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text class="mono" x="136" y="256" dy="0.35em" font-size="13" font-weight="600" fill="#7439B8" data-fit="55">theme/</text>
  <path d="M203,256 H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>
  <text x="396" y="256" dy="0.35em" font-size="14" font-weight="400" fill="#454C61" data-fit="516">Colores y tema de la app, en app_theme.dart</text>
  <path d="M108,272.0 V296 H120" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <rect x="124" y="282" width="79" height="28" rx="8" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text class="mono" x="136" y="296" dy="0.35em" font-size="13" font-weight="600" fill="#7439B8" data-fit="63">models/</text>
  <path d="M211,296 H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>
  <text x="396" y="296" dy="0.35em" font-size="14" font-weight="400" fill="#454C61" data-fit="516">Los datos que maneja la app</text>
  <path d="M108,312.0 V336 H120" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <rect x="124" y="322" width="110" height="28" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="2.5"/>
  <text class="mono" x="136" y="336" dy="0.35em" font-size="13" font-weight="600" fill="#A96C05" data-fit="94">components/</text>
  <path d="M242,336 H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>
  <text x="396" y="336" dy="0.35em" font-size="14" font-weight="700" fill="#161A26" data-fit="516">Widgets reutilizables. Es lo que haces en esta sesión</text>
  <path d="M108,352.0 V376 H120" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <rect x="124" y="362" width="86" height="28" rx="8" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text class="mono" x="136" y="376" dy="0.35em" font-size="13" font-weight="600" fill="#7439B8" data-fit="70">screens/</text>
  <path d="M218,376 H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>
  <text x="396" y="376" dy="0.35em" font-size="14" font-weight="400" fill="#454C61" data-fit="516">Pantallas completas, con Scaffold (sesión 3)</text>
  <path d="M108,392.0 V416 H120" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <rect x="124" y="402" width="71" height="28" rx="8" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text class="mono" x="136" y="416" dy="0.35em" font-size="13" font-weight="600" fill="#7439B8" data-fit="55">pages/</text>
  <path d="M203,416 H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>
  <text x="396" y="416" dy="0.35em" font-size="14" font-weight="400" fill="#454C61" data-fit="516">Secciones que una pantalla hospeda (sesión 9)</text>
  <path d="M80,432.0 V456 H92" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <rect x="96" y="442" width="79" height="28" rx="8" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
  <text class="mono" x="108" y="456" dy="0.35em" font-size="13" font-weight="600" fill="#3A8235" data-fit="63">assets/</text>
  <path d="M183,456 H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>
  <text x="396" y="456" dy="0.35em" font-size="14" font-weight="400" fill="#454C61" data-fit="516">Imágenes y otros archivos que viajan con la app</text>
  <path d="M80,472.0 V496 H92" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <rect x="96" y="482" width="118" height="28" rx="4" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
  <text class="mono" x="108" y="496" dy="0.35em" font-size="13" font-weight="600" fill="#3A8235" data-fit="102">pubspec.yaml</text>
  <path d="M222,496 H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>
  <text x="396" y="496" dy="0.35em" font-size="14" font-weight="400" fill="#454C61" data-fit="516">Nombre, dependencias y assets declarados</text>
  <path d="M80,512.0 V536 H92" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <rect x="96" y="522" width="180" height="28" rx="8" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text class="mono" x="108" y="536" dy="0.35em" font-size="13" font-weight="600" fill="#556074" data-fit="164">android/  ios/  web/</text>
  <path d="M284,536 H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>
  <text x="396" y="536" dy="0.35em" font-size="14" font-weight="400" fill="#454C61" data-fit="516">Un proyecto por plataforma. Casi nunca se tocan</text>
  <text class="foot" x="48" y="608" data-fit="860">Los nombres de carpetas y archivos van en minúscula y con guion bajo: home_screen.dart, stat_card.dart.</text>
</svg>
```

Dentro de `lib/` Flutter solo crea `main.dart`. Las demás carpetas las creas tú, y en este curso usamos siempre las mismas:

| Carpeta | Qué guarda | Cuándo la usas |
|---|---|---|
| `theme/` | `app_theme.dart`, con los colores y el tema | Más adelante |
| `components/` | Widgets reutilizables: una tarjeta, un botón propio, una fila de lista | **Esta sesión** |
| `screens/` | Pantallas completas | Sesión 3 |
| `pages/` | Secciones que una pantalla hospeda | Sesión 9 |
| `models/` | Las clases de datos de la app | Sesión 7 |

Tener un lugar fijo para cada cosa no es un capricho: cuando el proyecto crezca, y cuando un agente de IA trabaje contigo, los dos van a saber dónde buscar.

Crea las carpetas `components` y `screens` dentro de `lib/` antes de seguir.

## main.dart, parte por parte

Borra todo el contenido de `lib/main.dart`. El ejemplo que trae Flutter es largo y mezcla temas que todavía no hemos visto. Este es el que vamos a usar:

```svg
<svg id="ppMain" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 804" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ppMain-ttl ppMain-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ppMain-ttl">main.dart, parte por parte</title>
  <desc id="ppMain-dsc">El archivo main.dart anotado: el import, la función main que llama a runApp, la clase App que es un StatelessWidget, y MaterialApp con su tema, su tabla de rutas y su ruta inicial.</desc>
  <defs>
    <style>
      #ppMain .title{fill:#161A26;font-size:22px;font-weight:700}
      #ppMain .sub{fill:#79809A;font-size:13.5px}
      #ppMain .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ppMain .cl{font-size:13px;fill:#C9CFDA}
      #ppMain .s{fill:#A8D8A0} #ppMain .n{fill:#F2B880} #ppMain .c{fill:#7FD1E8}
      #ppMain .p{fill:#D5B8F5} #ppMain .k{fill:#F08FB0}
      #ppMain .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ppMain .ct{fill:#161A26;font-size:14px;font-weight:700}
      #ppMain .cb{fill:#454C61;font-size:13px}
      #ppMain .rt{fill:#161A26;font-size:14px} #ppMain .rs{fill:#79809A;font-size:12px}
      #ppMain .foot{fill:#79809A;font-size:12px}
      #ppMain .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #ppMain .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #ppMain .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#ppMain-ar-amber)}
      #ppMain .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #ppMain .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #ppMain .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#ppMain-ar-green)}
      #ppMain .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #ppMain .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #ppMain .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#ppMain-ar-indigo)}
      #ppMain .hl-rose{fill:#F3A3B2;fill-opacity:.16;stroke:#F3A3B2;stroke-width:1.5}
      #ppMain .ld-rose{fill:none;stroke:#F3A3B2;stroke-width:1.5;stroke-dasharray:3 4}
      #ppMain .ar-rose{fill:none;stroke:#C2354F;stroke-width:1.75;marker-end:url(#ppMain-ar-rose)}
      #ppMain .hl-teal{fill:#86D3CA;fill-opacity:.16;stroke:#86D3CA;stroke-width:1.5}
      #ppMain .ld-teal{fill:none;stroke:#86D3CA;stroke-width:1.5;stroke-dasharray:3 4}
      #ppMain .ar-teal{fill:none;stroke:#0F8478;stroke-width:1.75;marker-end:url(#ppMain-ar-teal)}
      #ppMain .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #ppMain .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #ppMain .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#ppMain-ar-violet)}
    </style>
    <marker id="ppMain-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="ppMain-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="ppMain-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="ppMain-ar-rose" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/></marker>
    <marker id="ppMain-ar-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#0F8478"/></marker>
    <marker id="ppMain-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="804" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56"><tspan class="mono">main.dart</tspan>, parte por parte</text>
  <text class="sub" x="48" y="80" data-fit="860">Todo proyecto Flutter arranca aquí. Es corto, y cada bloque tiene un solo trabajo.</text>
  <rect x="48" y="112" width="456" height="660" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/main.dart</text>
  <rect x="552" y="112" width="360" height="660" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">QUÉ HACE CADA PARTE</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-teal" x="64.0" y="156" width="54.8" height="22" rx="5"/>
  <rect class="hl-amber" x="103.0" y="204" width="54.8" height="22" rx="5"/>
  <rect class="hl-green" x="79.6" y="228" width="156.2" height="22" rx="5"/>
  <rect class="hl-indigo" x="110.8" y="300" width="31.4" height="22" rx="5"/>
  <rect class="hl-violet" x="149.8" y="420" width="93.8" height="22" rx="5"/>
  <rect class="hl-rose" x="110.8" y="612" width="54.8" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="304.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">import</tspan> <tspan class="s">'package:flutter/material.dart'</tspan>;</text>
  <text class="cl mono" font-size="13" x="68.0" y="220" textLength="101.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">void</tspan> main() {</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="156.0" lengthAdjust="spacingAndGlyphs" data-fit="432">runApp(<tspan class="k">const</tspan> <tspan class="c">App</tspan>());</text>
  <text class="cl mono" font-size="13" x="68.0" y="268" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="316" textLength="273.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">class</tspan> <tspan class="c">App</tspan> <tspan class="k">extends</tspan> <tspan class="c">StatelessWidget</tspan> {</text>
  <text class="cl mono" font-size="13" x="83.6" y="340" textLength="179.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">const</tspan> <tspan class="c">App</tspan>({<tspan class="k">super</tspan>.key});</text>
  <text class="cl mono" font-size="13" x="83.6" y="388" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">@override</tspan></text>
  <text class="cl mono" font-size="13" x="83.6" y="412" textLength="280.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Widget</tspan> build(<tspan class="c">BuildContext</tspan> context) {</text>
  <text class="cl mono" font-size="13" x="99.2" y="436" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="c">MaterialApp</tspan>(</text>
  <text class="cl mono" font-size="13" x="114.8" y="460" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">title</tspan>: <tspan class="s">'Mi app'</tspan>,</text>
  <text class="cl mono" font-size="13" x="114.8" y="484" textLength="132.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">theme</tspan>: <tspan class="c">ThemeData</tspan>(</text>
  <text class="cl mono" font-size="13" x="130.4" y="508" textLength="265.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">colorScheme</tspan>: <tspan class="c">ColorScheme</tspan>.fromSeed(</text>
  <text class="cl mono" font-size="13" x="146.0" y="532" textLength="226.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">seedColor</tspan>: <tspan class="c">Colors</tspan>.deepPurple,</text>
  <text class="cl mono" font-size="13" x="130.4" y="556" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="114.8" y="580" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="114.8" y="604" textLength="171.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">initialRoute</tspan>: <tspan class="s">'/home'</tspan>,</text>
  <text class="cl mono" font-size="13" x="114.8" y="628" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">routes</tspan>: {</text>
  <text class="cl mono" font-size="13" x="130.4" y="652" textLength="351.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">'/home'</tspan>: (context) =&gt; <tspan class="k">const</tspan> <tspan class="c">Text</tspan>(<tspan class="s">"Pantalla"</tspan>),</text>
  <text class="cl mono" font-size="13" x="114.8" y="676" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">},</text>
  <text class="cl mono" font-size="13" x="99.2" y="700" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">);</text>
  <text class="cl mono" font-size="13" x="83.6" y="724" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="748" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <g transform="translate(552,144)">
<g transform="translate(16,16)"><rect width="328" height="68" rx="10" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#556074" data-fit="300">import</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Trae código de otros archivos. Este trae</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">los widgets de Flutter.</text></g><g transform="translate(16,96)"><rect width="328" height="68" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#A96C05" data-fit="300">main()</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">La primera función que se ejecuta.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">Es la puerta de entrada de la app.</text></g><g transform="translate(16,176)"><rect width="328" height="68" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#3A8235" data-fit="300">runApp(...)</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Recibe el widget raíz y lo pone en pantalla.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">Todo lo demás cuelga de él.</text></g><g transform="translate(16,256)"><rect width="328" height="68" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#4453C9" data-fit="300">App</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">El widget raíz. Lo escribes tú, como</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">cualquier otro componente.</text></g><g transform="translate(16,336)"><rect width="328" height="68" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#7439B8" data-fit="300">MaterialApp</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Configura toda la app: título, tema</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">y pantallas.</text></g><g transform="translate(16,445)"><rect width="328" height="68" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#C2354F" data-fit="300">routes e initialRoute</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">La tabla de pantallas, cada una con su</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">nombre, y por cuál se empieza.</text></g>
  </g>
  <path class="ld-teal" d="M378.2,167 H504"/>
  <path class="ar-teal" d="M504,167 H514 V194 H568"/>
  <path class="ld-amber" d="M175.4,215 H504"/>
  <path class="ar-amber" d="M504,215 H541 V274 H568"/>
  <path class="ld-green" d="M245.6,239 H504"/>
  <path class="ar-green" d="M504,239 H532 V354 H568"/>
  <path class="ld-indigo" d="M347.0,311 H504"/>
  <path class="ar-indigo" d="M504,311 H523 V420 H568"/>
  <path class="ld-violet" d="M253.4,431 H504"/>
  <path class="ar-violet" d="M504,431 H514 V514 H568"/>
  <path class="ld-rose" d="M191.0,623 H504"/>
  <path class="ar-rose" d="M504,623 H568"/>
</svg>
```

```dart
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
      routes: {'/home': (context) => const Text("Pantalla")},
    );
  }
}
```

Lo que conviene retener:

- **`main()`** es donde arranca todo programa en Dart. En Flutter casi siempre tiene una sola línea.
- **`runApp`** recibe un widget y lo pone en pantalla. Ese widget es la raíz: todos los demás cuelgan de él.
- **`App`** es un widget que escribes tú. Su forma (una clase con un método `build`) es la misma de los componentes que vas a hacer al final de esta sesión.
- **`MaterialApp`** configura la aplicación completa. `theme` saca los colores de toda la app de un solo color, y por ahora se queda como está. En `routes` cada pantalla tiene un nombre que empieza por `/`, e `initialRoute` dice cuál se muestra primero. Por ahora hay una sola. La tabla crece cuando veamos navegación.

Ejecuta la app. Aparece la palabra *Pantalla* en rojo, con un subrayado amarillo, sobre un fondo negro. No es un error: la ruta `/home` entrega un `Text` suelto, y a un texto suelto le falta todo lo que hace que algo se vea como una pantalla.

## La primera pantalla

En lugar de ese `Text`, la ruta puede entregar una pantalla completa. Crea el archivo `lib/screens/home_screen.dart`:

```dart
import 'package:flutter/material.dart';

/// First screen of the app.
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Inicio')),
      body: const Center(
        child: Text('Hola, Icesi'),
      ),
    );
  }
}
```

```svg
<svg id="ppScaffold" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 769" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ppScaffold-ttl ppScaffold-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ppScaffold-ttl">Las partes de un Scaffold</title>
  <desc id="ppScaffold-dsc">El archivo home_screen.dart anotado junto a la pantalla que produce: Scaffold abarca toda la pantalla, appBar es la barra de arriba con el título Inicio, body es el resto de la pantalla y dentro de él un Center deja el texto Hola, Icesi en el medio.</desc>
  <defs>
    <style>
      #ppScaffold .title{fill:#161A26;font-size:22px;font-weight:700}
      #ppScaffold .sub{fill:#79809A;font-size:13.5px}
      #ppScaffold .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ppScaffold .cl{font-size:13px;fill:#C9CFDA}
      #ppScaffold .s{fill:#A8D8A0} #ppScaffold .n{fill:#F2B880} #ppScaffold .c{fill:#7FD1E8}
      #ppScaffold .p{fill:#D5B8F5} #ppScaffold .k{fill:#F08FB0}
      #ppScaffold .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ppScaffold .ct{fill:#161A26;font-size:14px;font-weight:700}
      #ppScaffold .cb{fill:#454C61;font-size:13px}
      #ppScaffold .rt{fill:#161A26;font-size:14px} #ppScaffold .rs{fill:#79809A;font-size:12px}
      #ppScaffold .foot{fill:#79809A;font-size:12px}
      #ppScaffold .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #ppScaffold .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #ppScaffold .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#ppScaffold-ar-amber)}
      #ppScaffold .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #ppScaffold .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #ppScaffold .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#ppScaffold-ar-green)}
      #ppScaffold .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #ppScaffold .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #ppScaffold .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#ppScaffold-ar-indigo)}
      #ppScaffold .hl-rose{fill:#F3A3B2;fill-opacity:.16;stroke:#F3A3B2;stroke-width:1.5}
      #ppScaffold .ld-rose{fill:none;stroke:#F3A3B2;stroke-width:1.5;stroke-dasharray:3 4}
      #ppScaffold .ar-rose{fill:none;stroke:#C2354F;stroke-width:1.75;marker-end:url(#ppScaffold-ar-rose)}
    </style>
    <marker id="ppScaffold-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="ppScaffold-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="ppScaffold-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="ppScaffold-ar-rose" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/></marker>
  </defs>
  <rect width="960" height="769" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las partes de un <tspan class="mono">Scaffold</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Scaffold arma la pantalla: tiene un lugar para la barra de arriba y otro para el contenido.</text>
  <rect x="48" y="112" width="456" height="480" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/home_screen.dart</text>
  <rect x="552" y="112" width="360" height="480" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="149.8" y="324" width="70.4" height="22" rx="5"/>
  <rect class="hl-amber" x="110.8" y="348" width="54.8" height="22" rx="5"/>
  <rect class="hl-green" x="110.8" y="372" width="39.2" height="22" rx="5"/>
  <rect class="hl-rose" x="181.0" y="396" width="156.2" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="304.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">import</tspan> <tspan class="s">'package:flutter/material.dart'</tspan>;</text>
  <text class="cl mono" font-size="13" x="68.0" y="220" textLength="327.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">class</tspan> <tspan class="c">HomeScreen</tspan> <tspan class="k">extends</tspan> <tspan class="c">StatelessWidget</tspan> {</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="234.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">const</tspan> <tspan class="c">HomeScreen</tspan>({<tspan class="k">super</tspan>.key});</text>
  <text class="cl mono" font-size="13" x="83.6" y="292" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">@override</tspan></text>
  <text class="cl mono" font-size="13" x="83.6" y="316" textLength="280.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Widget</tspan> build(<tspan class="c">BuildContext</tspan> context) {</text>
  <text class="cl mono" font-size="13" x="99.2" y="340" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="c">Scaffold</tspan>(</text>
  <text class="cl mono" font-size="13" x="114.8" y="364" textLength="343.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">appBar</tspan>: <tspan class="c">AppBar</tspan>(<tspan class="p">title</tspan>: <tspan class="k">const</tspan> <tspan class="c">Text</tspan>(<tspan class="s">'Inicio'</tspan>)),</text>
  <text class="cl mono" font-size="13" x="114.8" y="388" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">body</tspan>: <tspan class="k">const</tspan> <tspan class="c">Center</tspan>(</text>
  <text class="cl mono" font-size="13" x="130.4" y="412" textLength="210.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Text</tspan>(<tspan class="s">'Hola, Icesi'</tspan>),</text>
  <text class="cl mono" font-size="13" x="114.8" y="436" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="99.2" y="460" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">);</text>
  <text class="cl mono" font-size="13" x="83.6" y="484" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="508" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <g transform="translate(552,144)">
<rect x="78" y="30" width="204" height="402" rx="26" fill="#FFFFFF" stroke="#2A3040" stroke-width="3"/><rect x="84" y="36" width="192" height="390" rx="20" fill="#4453C9" fill-opacity=".08" stroke="#4453C9" stroke-width="2"/><rect x="92" y="44" width="176" height="56" rx="12" fill="#A96C05" fill-opacity=".08" stroke="#A96C05" stroke-width="2"/><text x="108" y="72" dy="0.35em" font-size="17" font-weight="500" fill="#161A26">Inicio</text><rect x="92" y="108" width="176" height="310" rx="12" fill="#3A8235" fill-opacity=".08" stroke="#3A8235" stroke-width="2"/><rect x="134" y="249" width="92" height="28" rx="8" fill="#C2354F" fill-opacity=".08" stroke="#C2354F" stroke-width="2"/><text x="180" y="263" dy="0.35em" text-anchor="middle" font-size="13.5" fill="#161A26">Hola, Icesi</text>
  </g>
  <path class="ld-indigo" d="M230.0,335 H504"/>
  <path class="ar-indigo" d="M504,335 H514 V156 H868 V248 H828"/>
  <path class="ld-amber" d="M464.0,359 H504"/>
  <path class="ar-amber" d="M504,359 H523 V216 H644"/>
  <path class="ld-green" d="M269.0,383 H504"/>
  <path class="ar-green" d="M504,383 H532 V312 H644"/>
  <path class="ld-rose" d="M347.0,407 H504"/>
  <path class="ar-rose" d="M504,407 H686"/>
  <g transform="translate(48.0,616)">
    <rect width="204.0" height="121" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#EEF1FF" stroke="#4453C9" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="146">Scaffold</text>
    <text class="cb" x="16" y="60" data-fit="172">La pantalla completa.</text>
    <text class="cb" x="16" y="79" data-fit="172">Le da un lugar a</text>
    <text class="cb" x="16" y="98" data-fit="172">cada parte.</text>
  </g>
  <g transform="translate(268.0,616)">
    <rect width="204.0" height="121" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#FFF3DC" stroke="#A96C05" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="146">appBar</text>
    <text class="cb" x="16" y="60" data-fit="172">La barra de arriba.</text>
    <text class="cb" x="16" y="79" data-fit="172">Aquí es un AppBar</text>
    <text class="cb" x="16" y="98" data-fit="172">con un título.</text>
  </g>
  <g transform="translate(488.0,616)">
    <rect width="204.0" height="121" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#E8F6E3" stroke="#3A8235" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="146">body</text>
    <text class="cb" x="16" y="60" data-fit="172">El contenido. Ocupa</text>
    <text class="cb" x="16" y="79" data-fit="172">lo que deja libre</text>
    <text class="cb" x="16" y="98" data-fit="172">la barra.</text>
  </g>
  <g transform="translate(708.0,616)">
    <rect width="204.0" height="121" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#FFEBEF" stroke="#C2354F" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="146">Text</text>
    <text class="cb" x="16" y="60" data-fit="172">Center lo deja en el</text>
    <text class="cb" x="16" y="79" data-fit="172">medio. Es lo que vas</text>
    <text class="cb" x="16" y="98" data-fit="172">a cambiar hoy.</text>
  </g>
</svg>
```

Falta conectarla. En `lib/main.dart` importa el archivo nuevo, debajo del `import` que ya está:

```dart
import 'screens/home_screen.dart';
```

Y en `routes` cambia el `Text` por la pantalla:

```dart
routes: {'/home': (context) => const HomeScreen()},
```

Ejecuta la app. Debes ver una barra con el título *Inicio* y el texto *Hola, Icesi* en el centro.

**Este es tu banco de pruebas para toda la sesión.** En las lecciones que siguen, cada widget nuevo lo pruebas reemplazando el `Text('Hola, Icesi')` que está dentro de `Center`. `Scaffold` y `Center` se ven a fondo en la sesión 3; hoy basta con saber que uno arma la pantalla y el otro centra lo que tenga adentro.

Fíjate en algo de `main.dart`: en ninguna parte dice *crea una ventana*, *ahora ponle un título*, *ahora agrégale una pantalla*. Dice **qué hay**: una `MaterialApp` con este título, este tema y estas rutas. Esa es la diferencia entre programar de forma imperativa y de forma declarativa.

```svg
<svg id="ppDeclarativo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 500" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ppDeclarativo-ttl ppDeclarativo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ppDeclarativo-ttl">Dar órdenes o describir</title>
  <desc id="ppDeclarativo-dsc">Comparación entre el paradigma imperativo, donde el código modifica cada elemento de la pantalla paso a paso, y el declarativo, donde el código describe la interfaz a partir del estado y el framework la redibuja.</desc>
  <defs>
    <style>
      #ppDeclarativo .title{fill:#161A26;font-size:22px;font-weight:700}
      #ppDeclarativo .sub{fill:#79809A;font-size:13.5px}
      #ppDeclarativo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ppDeclarativo .nt{font-size:15px;font-weight:700;fill:#161A26}
      #ppDeclarativo .nb{fill:#454C61;font-size:13px}
      #ppDeclarativo .lbl{fill:#556074;font-size:12px;font-weight:600}
      #ppDeclarativo .foot{fill:#79809A;font-size:12px}
      #ppDeclarativo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ppDeclarativo .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#ppDeclarativo-arrow)}
      #ppDeclarativo .code{font-size:13px;fill:#C9CFDA}
      #ppDeclarativo .k{fill:#F08FB0} #ppDeclarativo .s{fill:#A8D8A0} #ppDeclarativo .c{fill:#7FD1E8}
    </style>
    <marker id="ppDeclarativo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="500" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Dar órdenes o describir</text>
  <text class="sub" x="48" y="80" data-fit="860">Las dos formas de programar una interfaz. Flutter usa la segunda.</text>
  <text class="h" x="48" y="124">IMPERATIVO · DAR ÓRDENES</text>
  <rect x="48" y="140" width="408" height="176" rx="12" fill="#1F2430"/>
  <text class="code mono" x="68" y="174" data-fit="372">counter = counter + 1;</text>
  <text class="code mono" x="68" y="202" data-fit="372">label.<tspan class="c">setText</tspan>(<tspan class="s">'3'</tspan>);</text>
  <text class="code mono" x="68" y="230" data-fit="372">label.<tspan class="c">setColor</tspan>(red);</text>
  <text class="code mono" x="68" y="258" data-fit="372">button.<tspan class="c">setEnabled</tspan>(<tspan class="k">false</tspan>);</text>
  <text class="code mono" x="68" y="286" data-fit="372">warning.<tspan class="c">show</tspan>();</text>
  <g transform="translate(48,332)">
    <rect width="408" height="100" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/>
    <text class="nt" x="16" y="30" fill="#C2354F" data-fit="376">Tú cambias cada pieza, una por una</text>
    <text class="nb" x="16" y="56" data-fit="376">Si olvidas una línea, la pantalla queda mostrando</text>
    <text class="nb" x="16" y="76" data-fit="376">algo que ya no es cierto.</text>
  </g>

  <text class="h" x="504" y="124">DECLARATIVO · DESCRIBIR</text>
  <g transform="translate(504,140)">
    <rect width="112" height="72" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
    <text x="56" y="28" text-anchor="middle" font-size="12" font-weight="700" fill="#A96C05" data-fit="96">ESTADO</text>
    <text class="mono" x="56" y="52" text-anchor="middle" font-size="14" font-weight="600" fill="#161A26" data-fit="96">counter = 3</text>
  </g>
  <path class="link" d="M616,176 H648"/>
  <g transform="translate(656,140)">
    <rect width="96" height="72" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="2.5"/>
    <text x="48" y="28" text-anchor="middle" font-size="12" font-weight="700" fill="#4453C9" data-fit="80">TU CÓDIGO</text>
    <text class="mono" x="48" y="52" text-anchor="middle" font-size="14" font-weight="600" fill="#161A26" data-fit="80">build()</text>
  </g>
  <path class="link" d="M752,176 H784"/>
  <g transform="translate(792,140)">
    <rect width="120" height="72" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
    <text x="60" y="28" text-anchor="middle" font-size="12" font-weight="700" fill="#3A8235" data-fit="104">INTERFAZ</text>
    <text x="60" y="52" text-anchor="middle" font-size="14" font-weight="600" fill="#161A26" data-fit="104">lo que se ve</text>
  </g>
  <rect x="504" y="228" width="408" height="88" rx="12" fill="#1F2430"/>
  <text class="code mono" x="524" y="262" data-fit="372"><tspan class="c">Text</tspan>(<tspan class="s">'$counter'</tspan>),</text>
  <text class="code mono" x="524" y="290" data-fit="372"><tspan class="k">if</tspan> (counter &gt;= 3) <tspan class="c">Text</tspan>(<tspan class="s">'Límite'</tspan>),</text>
  <g transform="translate(504,332)">
    <rect width="408" height="100" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
    <text class="nt" x="16" y="30" fill="#3A8235" data-fit="376">Tú describes cómo se ve para cada estado</text>
    <text class="nb" x="16" y="56" data-fit="376">Cuando el estado cambia, Flutter vuelve a llamar a</text>
    <text class="nb" x="16" y="76" data-fit="376">build() y redibuja. No hay pieza que se te olvide.</text>
  </g>
  <text class="foot" x="48" y="472" data-fit="860">interfaz = f(estado): la pantalla es el resultado de una función, no una lista de cambios.</text>
</svg>
```

En el estilo **imperativo** el código es una lista de órdenes sobre lo que ya está en pantalla: cambia este texto, pinta aquel de rojo, apaga ese botón. Funciona, pero cada cambio de datos obliga a recordar todas las piezas que dependen de él. La que se olvida queda mostrando un valor viejo, y ese es uno de los errores más comunes en una interfaz.

En el estilo **declarativo**, que es el de Flutter, escribes una sola cosa: cómo se ve la pantalla **para un estado dado**. Cuando el estado cambia, Flutter vuelve a ejecutar `build` y redibuja lo que haga falta.

> **interfaz = f(estado)**

Es la idea con la que cerró la lección *¿Qué es el frontend?*, y ahora tiene nombre en el código: esa función `f` es el método `build`.

Por eso los widgets de las próximas lecciones no tienen métodos como `setText` o `setColor`. Un `Text` no se modifica: se describe otra vez con el dato nuevo. En esta sesión el estado todavía no cambia, así que la descripción es fija. Qué pasa cuando cambia es el tema de la sesión 6.

## Ejemplo completo

Este es el programa entero, listo para ejecutar. Aquí `App` y `HomeScreen` están en un solo archivo porque el editor en línea solo tiene uno. En tu proyecto van separados, como los dejaste: `App` en `lib/main.dart` y `HomeScreen` en `lib/screens/home_screen.dart`.

Pasa a la pestaña *Fire it up!* para verlo correr, y cambia el título de la barra o el texto del centro para ver qué pasa.

```dart trycode=c7ed2d4963223915971ae8ebda848400
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
      appBar: AppBar(title: const Text('Inicio')),
      body: const Center(
        child: Text('Hola, Icesi'),
      ),
    );
  }
}
```
