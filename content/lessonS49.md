# Prop drilling

<!-- tags: prop drilling, pasar el estado por constructores, de la Screen a SongCard, el dato baja nivel por nivel, parámetro que no se usa, pasar datos por varios niveles, cuándo duele pasar datos, constructor muy largo, InheritedWidget, Provider -->

En la lección anterior `_songs` salió de la Screen hacia `SongList`, y la Screen quedó con una línea: `SongList(songs: _songs)`. Ahora sigue el dato completo. ¿Cómo llega una canción desde el estado de la Screen hasta el `Text` que muestra su título?

## El camino de un dato

La lista vive **solo** en el estado de la Screen. Desde ahí baja por los constructores, primero a `SongList` y luego a cada `SongCard`. En código, el camino tiene tres paradas:

```svg
<svg id="pdCamino" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 500" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="pdCamino-ttl pdCamino-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="pdCamino-ttl">El camino de una canción</title>
  <desc id="pdCamino-dsc">Tres bloques de código en fila. PlaylistScreen guarda _songs y crea SongList(songs: _songs). SongList declara final List de Song songs y en su for crea SongCard(song: song). SongCard declara final Song song y muestra Text(song.title). Flechas azules van de _songs al campo songs de SongList y de song al campo song de SongCard.</desc>
  <defs>
    <style>
      #pdCamino .title{fill:#161A26;font-size:22px;font-weight:700}
      #pdCamino .sub{fill:#79809A;font-size:13.5px}
      #pdCamino .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #pdCamino .nt{font-size:15px;font-weight:700;fill:#161A26}
      #pdCamino .nb{fill:#454C61;font-size:13px}
      #pdCamino .lbl{fill:#556074;font-size:12px;font-weight:600}
      #pdCamino .foot{fill:#79809A;font-size:12px}
      #pdCamino .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #pdCamino .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#pdCamino-arrow)}
    </style>
    <marker id="pdCamino-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="pdCamino-down" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="pdCamino-up" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="pdCamino-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#9AA1B2"/></marker>
  </defs>
  <rect width="960" height="500" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">El camino de una canción</text>
  <text class="sub" x="48" y="80" data-fit="860">De la Screen a la tarjeta, cada nivel recibe el dato por su constructor y se lo pasa al siguiente.</text>
  <rect x="48" y="112" width="256" height="178" rx="12" fill="#1F2430"/><path d="M48,124 A12,12 0 0 1 60,112 H292 A12,12 0 0 1 304,124 V148 H48 Z" fill="#F4EBFF"/><text x="62" y="136" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">PlaylistScreen</text><text x="292" y="136" font-size="12" font-weight="600" fill="#7439B8" text-anchor="end">guarda</text><text x="62.0" y="174" font-size="12.5" fill="#C9CFDA" class="mono" textLength="217.5" lengthAdjust="spacingAndGlyphs">final List&lt;Song&gt; _songs = [];</text><text x="62.0" y="196" font-size="12.5" fill="#C9CFDA" class="mono" textLength="0.0" lengthAdjust="spacingAndGlyphs"></text><text x="62.0" y="218" font-size="12.5" fill="#C9CFDA" class="mono" textLength="127.5" lengthAdjust="spacingAndGlyphs">Widget build(…) {</text><text x="77.0" y="240" font-size="12.5" fill="#C9CFDA" class="mono" textLength="7.5" lengthAdjust="spacingAndGlyphs">…</text><rect x="194.0" y="247" width="51.0" height="21" rx="5" fill="#2F6FD6" fill-opacity=".28" stroke="#7FA6E8"/><text x="77.0" y="262" font-size="12.5" fill="#C9CFDA" class="mono" textLength="180.0" lengthAdjust="spacingAndGlyphs">SongList(songs: _songs),</text>
  <rect x="352" y="112" width="256" height="178" rx="12" fill="#1F2430"/><path d="M352,124 A12,12 0 0 1 364,112 H596 A12,12 0 0 1 608,124 V148 H352 Z" fill="#EEF1FF"/><text x="366" y="136" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">SongList</text><text x="596" y="136" font-size="12" font-weight="600" fill="#4453C9" text-anchor="end">recibe y reparte</text><rect x="490.5" y="159" width="43.5" height="21" rx="5" fill="#2F6FD6" fill-opacity=".28" stroke="#7FA6E8"/><text x="366.0" y="174" font-size="12.5" fill="#C9CFDA" class="mono" textLength="172.5" lengthAdjust="spacingAndGlyphs">final List&lt;Song&gt; songs;</text><text x="366.0" y="196" font-size="12.5" fill="#C9CFDA" class="mono" textLength="0.0" lengthAdjust="spacingAndGlyphs"></text><text x="366.0" y="218" font-size="12.5" fill="#C9CFDA" class="mono" textLength="127.5" lengthAdjust="spacingAndGlyphs">Widget build(…) {</text><text x="381.0" y="240" font-size="12.5" fill="#C9CFDA" class="mono" textLength="187.5" lengthAdjust="spacingAndGlyphs">for (final song in songs)</text><rect x="505.5" y="247" width="43.5" height="21" rx="5" fill="#2F6FD6" fill-opacity=".28" stroke="#7FA6E8"/><text x="396.0" y="262" font-size="12.5" fill="#C9CFDA" class="mono" textLength="157.5" lengthAdjust="spacingAndGlyphs">SongCard(song: song),</text>
  <rect x="656" y="112" width="256" height="178" rx="12" fill="#1F2430"/><path d="M656,124 A12,12 0 0 1 668,112 H900 A12,12 0 0 1 912,124 V148 H656 Z" fill="#EEF1FF"/><text x="670" y="136" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">SongCard</text><text x="900" y="136" font-size="12" font-weight="600" fill="#4453C9" text-anchor="end">recibe y muestra</text><rect x="749.5" y="159" width="36.0" height="21" rx="5" fill="#2F6FD6" fill-opacity=".28" stroke="#7FA6E8"/><text x="670.0" y="174" font-size="12.5" fill="#C9CFDA" class="mono" textLength="120.0" lengthAdjust="spacingAndGlyphs">final Song song;</text><text x="670.0" y="196" font-size="12.5" fill="#C9CFDA" class="mono" textLength="0.0" lengthAdjust="spacingAndGlyphs"></text><text x="670.0" y="218" font-size="12.5" fill="#C9CFDA" class="mono" textLength="127.5" lengthAdjust="spacingAndGlyphs">Widget build(…) {</text><text x="685.0" y="240" font-size="12.5" fill="#C9CFDA" class="mono" textLength="7.5" lengthAdjust="spacingAndGlyphs">…</text><rect x="719.5" y="247" width="36.0" height="21" rx="5" fill="#2F6FD6" fill-opacity=".28" stroke="#7FA6E8"/><text x="685.0" y="262" font-size="12.5" fill="#C9CFDA" class="mono" textLength="127.5" lengthAdjust="spacingAndGlyphs">Text(song.title),</text>
  <path d="M245.0,257 H328 V169 H350" fill="none" stroke="#2F6FD6" stroke-width="2.25" marker-end="url(#pdCamino-down)"/>
  <path d="M549.0,257 H632 V169 H654" fill="none" stroke="#2F6FD6" stroke-width="2.25" marker-end="url(#pdCamino-down)"/>
  <rect x="48" y="336" width="256" height="104" rx="12" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="64" y="367" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="228">Guarda el dato</text><text x="64" y="394" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="224">Es su estado. Lo entrega</text><text x="64" y="413" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="224">al hijo por el constructor.</text>
  <rect x="352" y="336" width="256" height="104" rx="12" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.5"/><text x="368" y="367" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="228">Recibe y reparte</text><text x="368" y="394" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="224">Usa la lista para el for y</text><text x="368" y="413" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="224">a cada tarjeta le da una Song.</text>
  <rect x="656" y="336" width="256" height="104" rx="12" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.5"/><text x="672" y="367" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="228">Recibe y muestra</text><text x="672" y="394" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="224">No sabe de dónde vino:</text><text x="672" y="413" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="224">solo dibuja lo que le llegó.</text>
  <text x="48" y="476" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="864">Nadie toma el dato del aire: si un widget lo necesita, alguien de arriba se lo pasó.</text>
</svg>
```

En cada nivel se repite lo mismo. El widget **declara un campo** (`final List<Song> songs;`, `final Song song;`), su constructor lo recibe, y su `build()` lo usa o se lo pasa al siguiente. Ningún widget toma el dato "del aire": si `SongCard` puede mostrar un título, es porque alguien de arriba le entregó la canción.

Cuando la lista cambia, la Screen corre `build()` y crea un `SongList` nuevo con la lista nueva, y ese `SongList` crea sus tarjetas. Nada se actualiza solo: todo sale de volver a construir con el dato nuevo.

## Eso es prop drilling

Pasar un dato **de nivel en nivel por los constructores**, hasta el widget que lo usa, se llama **prop drilling**. *Prop* viene de *property*: los parámetros de un componente. *Drilling* es perforar: el dato atraviesa los niveles del medio.

En la playlist cada nivel **usa** lo que recibe. La Screen lo guarda, `SongList` recorre la lista y `SongCard` la dibuja. Ese drilling es sano, y es justo lo que el curso quiere: el dato vive arriba y baja por el constructor.

El problema aparece cuando la app crece y entre la Screen y la tarjeta hay widgets que **no usan** el dato y lo reciben solo para pasarlo:

```svg
<svg id="pdNiveles" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 640" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="pdNiveles-ttl pdNiveles-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="pdNiveles-ttl">Prop drilling: pasar algo que no se usa</title>
  <desc id="pdNiveles-dsc">Dos columnas. A la izquierda, la playlist: PlaylistScreen, SongList con songs y SongCard con song, todos en azul porque cada uno usa lo que recibe. A la derecha, una app más grande: la Screen, una Page y una sección reciben songs en gris sin usarlo, solo para pasarlo, hasta SongList y SongCard. Debajo, tres señales de que el drilling empieza a doler.</desc>
  <defs>
    <style>
      #pdNiveles .title{fill:#161A26;font-size:22px;font-weight:700}
      #pdNiveles .sub{fill:#79809A;font-size:13.5px}
      #pdNiveles .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #pdNiveles .nt{font-size:15px;font-weight:700;fill:#161A26}
      #pdNiveles .nb{fill:#454C61;font-size:13px}
      #pdNiveles .lbl{fill:#556074;font-size:12px;font-weight:600}
      #pdNiveles .foot{fill:#79809A;font-size:12px}
      #pdNiveles .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #pdNiveles .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#pdNiveles-arrow)}
    </style>
    <marker id="pdNiveles-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="pdNiveles-down" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="pdNiveles-up" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="pdNiveles-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#9AA1B2"/></marker>
  </defs>
  <rect width="960" height="640" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Prop drilling: pasar algo que no se usa</text>
  <text class="sub" x="48" y="80" data-fit="860">Un widget recibe un parámetro solo para entregárselo a su hijo. Un nivel se tolera; varios duelen.</text>
  <rect x="48" y="112" width="420" height="344" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><path d="M48,126 A14,14 0 0 1 62,112 H454 A14,14 0 0 1 468,126 V152 H48 Z" fill="#E8F6E3"/><text x="66" y="138" font-size="14" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="384">La playlist: cada nivel usa lo que recibe</text><rect x="66" y="172" width="384" height="44" rx="10" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="80" y="199" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">PlaylistScreen</text><path d="M88,216 V261" stroke="#C4CBD8" stroke-width="1.5"/><rect x="66" y="261" width="384" height="44" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><text x="80" y="288" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">SongList</text><rect x="224" y="272" width="55" height="22" rx="11" fill="#E6F0FF" stroke="#7FA6E8"/><text x="251.5" y="287.5" font-size="12" font-weight="600" fill="#1F4FA8" text-anchor="middle" class="mono">songs</text><path d="M88,305 V350" stroke="#C4CBD8" stroke-width="1.5"/><rect x="66" y="350" width="384" height="44" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><text x="80" y="377" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">SongCard</text><rect x="224" y="361" width="48" height="22" rx="11" fill="#E6F0FF" stroke="#7FA6E8"/><text x="248.0" y="376.5" font-size="12" font-weight="600" fill="#1F4FA8" text-anchor="middle" class="mono">song</text>
  <rect x="492" y="112" width="420" height="344" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><path d="M492,126 A14,14 0 0 1 506,112 H898 A14,14 0 0 1 912,126 V152 H492 Z" fill="#FFEBEF"/><text x="510" y="138" font-size="14" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="384">Una app más grande: cuatro niveles</text><rect x="510" y="172" width="384" height="44" rx="10" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="524" y="199" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">HomeScreen</text><path d="M532,216 V225" stroke="#C4CBD8" stroke-width="1.5"/><rect x="510" y="225" width="384" height="44" rx="10" fill="#F6F7F9" stroke="#D9DEE8" stroke-width="1.5"/><text x="524" y="252" font-size="13.5" font-weight="700" fill="#79809A" text-anchor="start" class="mono" data-fit="150">LibraryPage</text><rect x="668" y="236" width="55" height="22" rx="11" fill="#F1F2F5" stroke="#B8BDC9" stroke-dasharray="4 3"/><text x="695.5" y="251.5" font-size="12" font-weight="600" fill="#79809A" text-anchor="middle" class="mono">songs</text><path d="M532,269 V278" stroke="#C4CBD8" stroke-width="1.5"/><rect x="510" y="278" width="384" height="44" rx="10" fill="#F6F7F9" stroke="#D9DEE8" stroke-width="1.5"/><text x="524" y="305" font-size="13.5" font-weight="700" fill="#79809A" text-anchor="start" class="mono" data-fit="150">RecentSection</text><rect x="668" y="289" width="55" height="22" rx="11" fill="#F1F2F5" stroke="#B8BDC9" stroke-dasharray="4 3"/><text x="695.5" y="304.5" font-size="12" font-weight="600" fill="#79809A" text-anchor="middle" class="mono">songs</text><path d="M532,322 V331" stroke="#C4CBD8" stroke-width="1.5"/><rect x="510" y="331" width="384" height="44" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><text x="524" y="358" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">SongList</text><rect x="668" y="342" width="55" height="22" rx="11" fill="#E6F0FF" stroke="#7FA6E8"/><text x="695.5" y="357.5" font-size="12" font-weight="600" fill="#1F4FA8" text-anchor="middle" class="mono">songs</text><path d="M532,375 V384" stroke="#C4CBD8" stroke-width="1.5"/><rect x="510" y="384" width="384" height="44" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><text x="524" y="411" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">SongCard</text><rect x="668" y="395" width="48" height="22" rx="11" fill="#E6F0FF" stroke="#7FA6E8"/><text x="692.0" y="410.5" font-size="12" font-weight="600" fill="#1F4FA8" text-anchor="middle" class="mono">song</text>
  <rect x="48" y="480" width="272" height="104" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><circle cx="76" cy="506" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="76" y="510.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">1</text><text x="98" y="511" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="210">Recibe lo que no usa</text><text x="64" y="538" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Un widget tiene en su</text><text x="64" y="557" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">constructor algo que solo pasa.</text>
  <rect x="344" y="480" width="272" height="104" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><circle cx="372" cy="506" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="372" y="510.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">2</text><text x="394" y="511" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="210">Un cambio, tres archivos</text><text x="360" y="538" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Agregar un dato obliga a</text><text x="360" y="557" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">tocar tres archivos o más.</text>
  <rect x="640" y="480" width="272" height="104" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><circle cx="668" cy="506" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="668" y="510.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">3</text><text x="690" y="511" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="210">Cinco parámetros o más</text><text x="656" y="538" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">El constructor ya no se lee</text><text x="656" y="557" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">de un vistazo.</text>
  <text x="48" y="616" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="864">En este curso el drilling corto es lo correcto: es explícito y se sigue con los ojos.</text>
</svg>
```

## Hasta dónde se tolera

Uno o dos niveles de paso se toleran, y en este curso es lo correcto. Tiene una ventaja que no se ve hasta que falta: es **explícito**. Si quieres saber de dónde sale la `song` de una tarjeta, subes por los constructores y llegas a la Screen. No hay nada escondido.

En las próximas lecciones el mismo camino va a llevar también **funciones**: para quitar una canción, `onDelete` baja de la Screen a la tarjeta pasando por `SongList`. Ahí aparece el primer parámetro que `SongList` recibe solo para entregarlo.

## Las señales de que empieza a doler

1. **Un widget recibe lo que no usa.** Si en el constructor hay parámetros que el `build()` solo reenvía, es drilling de paso. Uno se tolera. Si la mayoría del constructor es eso, el widget es un tubo.
2. **Un cambio, tres archivos.** Agregar un dato nuevo obliga a tocar la Screen, cada intermediario y el componente final. Si sumar algo te hace editar tres archivos o más, el drilling ya cuesta.
3. **Cinco parámetros o más.** Un constructor así ya no se lee de un vistazo, y es fácil pasar uno en el lugar de otro.

## Las salidas, para después

Cuando el drilling duele de verdad, Flutter tiene formas de que un widget lea algo de un ancestro **sin** que los del medio lo pasen: `InheritedWidget`, que viene en Flutter, y paquetes como `Provider` o Bloc que se apoyan en él. Funcionan, pero esconden de dónde sale cada dato, y ese precio solo vale la pena con apps grandes. En este curso el estado se maneja con `setState` y se pasa por el constructor. Lo importante es que sepas reconocer el momento en que esto deja de alcanzar.

## Ejemplo completo

Es el mismo programa de *El estado entra como parámetro*. Recorre en él el camino de una canción: de `_songs` a `SongList`, del `for` a `SongCard` y de ahí al `Text`.

```dart trycode=f4a535c105c13abb18d1d3516c58997d
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
      routes: {
        '/': (context) => const PlaylistScreen(),
      },
    );
  }
}

/// A song in the playlist.
class Song {
  final String title;
  final String artist;
  final String imageUrl;

  const Song({
    required this.title,
    required this.artist,
    required this.imageUrl,
  });
}

/// Card for a song: cover, title and artist.
class SongCard extends StatelessWidget {
  final Song song;

  const SongCard({super.key, required this.song});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: const [
          BoxShadow(
            color: Color(0x296750A4),
            blurRadius: 12,
            offset: Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          Container(
            width: 64,
            height: 64,
            clipBehavior: Clip.antiAlias,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(12),
            ),
            child: Image.network(song.imageUrl, fit: BoxFit.cover),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  song.title,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  song.artist,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: const TextStyle(color: Colors.black54),
                ),
              ],
            ),
          ),
          const Icon(Icons.music_note, color: Colors.deepPurple),
        ],
      ),
    );
  }
}

/// List of songs, or a message when there are none.
class SongList extends StatelessWidget {
  final List<Song> songs;

  const SongList({super.key, required this.songs});

  @override
  Widget build(BuildContext context) {
    if (songs.isEmpty) {
      return const Padding(
        padding: EdgeInsets.all(24),
        child: Text(
          'Todavía no hay canciones',
          style: TextStyle(color: Colors.grey),
        ),
      );
    }
    return Column(
      children: [
        for (final song in songs) SongCard(song: song),
      ],
    );
  }
}

/// Screen that builds a playlist from a form.
class PlaylistScreen extends StatefulWidget {
  const PlaylistScreen({super.key});

  @override
  State<PlaylistScreen> createState() => _PlaylistScreenState();
}

class _PlaylistScreenState extends State<PlaylistScreen> {
  final List<Song> _songs = [];
  final _titleController = TextEditingController();
  final _artistController = TextEditingController();
  final _imageUrlController = TextEditingController();

  void _addSong() {
    setState(() {
      _songs.add(Song(
        title: _titleController.text,
        artist: _artistController.text,
        imageUrl: _imageUrlController.text,
      ));
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Mi playlist')),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              TextField(
                controller: _titleController,
                decoration: const InputDecoration(labelText: 'Canción'),
              ),
              TextField(
                controller: _artistController,
                decoration: const InputDecoration(labelText: 'Artista'),
              ),
              TextField(
                controller: _imageUrlController,
                decoration: const InputDecoration(labelText: 'URL de la imagen'),
              ),
              FilledButton(
                onPressed: () => _addSong(),
                child: const Text('Agregar'),
              ),
              SongList(songs: _songs),
            ],
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _titleController.dispose();
    _artistController.dispose();
    _imageUrlController.dispose();
    super.dispose();
  }
}
```
