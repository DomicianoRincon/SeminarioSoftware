# Creador de playlists: el componente SongCard

<!-- tags: SongCard, componente que recibe un modelo, pasar datos del estado a un componente, for en children, Image.network con bordes redondeados, clipBehavior, BoxShadow, TextOverflow.ellipsis, misma lista otra vista, lib/components -->

La playlist de la lección anterior funciona, pero una lista de `Text` no se parece a ninguna app de música. En el curso las piezas de una pantalla se hacen como **componentes**, y aquí hay uno claro: la tarjeta de cada canción. En esta lección te entregamos el código de `SongCard` y vemos cómo conectarlo con el estado.

Agrega unas canciones y cambia entre *Text* y *SongCard*:

```interactive
playlist cards
```

Fíjate en el panel del State: al cambiar de vista **no cambia nada en el estado**. Las canciones son las mismas; lo único que cambia es cómo las pinta `build()`.

## El componente

`SongCard` es un `StatelessWidget`, como los de la sesión 2. No sabe nada de listas ni de formularios: recibe **una** `Song` y la dibuja.

```svg
<svg id="sgCodigo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 1050" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="sgCodigo-ttl sgCodigo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="sgCodigo-ttl">El componente SongCard</title>
  <desc id="sgCodigo-dsc">Código resumido de SongCard: un Container blanco con bordes redondeados y sombra, una fila con la portada redondeada, el título y el artista. Flechas de colores van del borderRadius a la tarjeta, de Image.network a la portada y de song.title al título.</desc>
  <defs>
    <style>
      #sgCodigo .title{fill:#161A26;font-size:22px;font-weight:700}
      #sgCodigo .sub{fill:#79809A;font-size:13.5px}
      #sgCodigo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #sgCodigo .cl{font-size:13px;fill:#C9CFDA}
      #sgCodigo .s{fill:#A8D8A0} #sgCodigo .n{fill:#F2B880} #sgCodigo .c{fill:#7FD1E8}
      #sgCodigo .p{fill:#D5B8F5} #sgCodigo .k{fill:#F08FB0}
      #sgCodigo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #sgCodigo .ct{fill:#161A26;font-size:14px;font-weight:700}
      #sgCodigo .cb{fill:#454C61;font-size:13px}
      #sgCodigo .rt{fill:#161A26;font-size:14px} #sgCodigo .rs{fill:#79809A;font-size:12px}
      #sgCodigo .foot{fill:#79809A;font-size:12px}
      #sgCodigo .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #sgCodigo .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #sgCodigo .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#sgCodigo-ar-amber)}
      #sgCodigo .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #sgCodigo .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #sgCodigo .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#sgCodigo-ar-green)}
      #sgCodigo .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #sgCodigo .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #sgCodigo .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#sgCodigo-ar-violet)}
    </style>
    <marker id="sgCodigo-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="sgCodigo-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="sgCodigo-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="1050" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">El componente <tspan class="mono">SongCard</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Resumido: el código completo está debajo. Todo lo que muestra sale de la Song que recibe.</text>
  <rect x="48" y="112" width="456" height="780" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/components/song_card.dart</text>
  <rect x="552" y="112" width="360" height="780" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="95.2" y="252" width="101.6" height="22" rx="5"/>
  <rect class="hl-violet" x="181.0" y="540" width="109.4" height="22" rx="5"/>
  <rect class="hl-green" x="196.6" y="660" width="86.0" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="78.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Container</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="265.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">padding</tspan>: <tspan class="k">const</tspan> <tspan class="c">EdgeInsets</tspan>.all(<tspan class="n">12</tspan>),</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="202.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">decoration</tspan>: <tspan class="c">BoxDecoration</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="156.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">color</tspan>: <tspan class="c">Colors</tspan>.white,</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="312.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">borderRadius</tspan>: <tspan class="c">BorderRadius</tspan>.circular(<tspan class="n">16</tspan>),</text>
  <text class="cl mono" font-size="13" x="99.2" y="292" textLength="351.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">boxShadow</tspan>: <tspan class="k">const</tspan> [<tspan class="c">BoxShadow</tspan>(<tspan class="p">blurRadius</tspan>: <tspan class="n">12</tspan>)],</text>
  <text class="cl mono" font-size="13" x="83.6" y="316" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="83.6" y="340" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Row</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="364" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">children</tspan>: [</text>
  <text class="cl mono" font-size="13" x="114.8" y="388" textLength="78.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Container</tspan>(</text>
  <text class="cl mono" font-size="13" x="130.4" y="412" textLength="78.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">width</tspan>: <tspan class="n">64</tspan>,</text>
  <text class="cl mono" font-size="13" x="130.4" y="436" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">height</tspan>: <tspan class="n">64</tspan>,</text>
  <text class="cl mono" font-size="13" x="130.4" y="460" textLength="226.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">clipBehavior</tspan>: <tspan class="c">Clip</tspan>.antiAlias,</text>
  <text class="cl mono" font-size="13" x="130.4" y="484" textLength="202.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">decoration</tspan>: <tspan class="c">BoxDecoration</tspan>(</text>
  <text class="cl mono" font-size="13" x="146.0" y="508" textLength="312.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">borderRadius</tspan>: <tspan class="c">BorderRadius</tspan>.circular(<tspan class="n">12</tspan>),</text>
  <text class="cl mono" font-size="13" x="130.4" y="532" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="130.4" y="556" textLength="280.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Image</tspan>.network(song.imageUrl),</text>
  <text class="cl mono" font-size="13" x="114.8" y="580" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="114.8" y="604" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Expanded</tspan>(</text>
  <text class="cl mono" font-size="13" x="130.4" y="628" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Column</tspan>(</text>
  <text class="cl mono" font-size="13" x="146.0" y="652" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">children</tspan>: [</text>
  <text class="cl mono" font-size="13" x="161.6" y="676" textLength="132.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(song.title),</text>
  <text class="cl mono" font-size="13" x="161.6" y="700" textLength="140.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(song.artist),</text>
  <text class="cl mono" font-size="13" x="146.0" y="724" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="130.4" y="748" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="114.8" y="772" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="114.8" y="796" textLength="226.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">const</tspan> <tspan class="c">Icon</tspan>(<tspan class="c">Icons</tspan>.music_note),</text>
  <text class="cl mono" font-size="13" x="99.2" y="820" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="83.6" y="844" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="68.0" y="868" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<defs><linearGradient id="sgCodigo-cover" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B69DF8"/><stop offset="1" stop-color="#6750A4"/></linearGradient></defs><text x="24" y="380" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" class="mono" data-fit="312">Song('Levitating', 'Dua Lipa', …)</text><rect x="24" y="424" width="312" height="88" rx="16" fill="#6750A4" fill-opacity=".12"/><rect x="24" y="420" width="312" height="88" rx="16" fill="#FFFFFF" stroke="#E6E0F2" stroke-width="1"/><rect x="36" y="432" width="64" height="64" rx="12" fill="url(#sgCodigo-cover)"/><circle cx="79.5" cy="452.5" r="7.7" fill="#FFFFFF" fill-opacity=".7"/><path d="M36,484.5 L59.0,464.0 L75.7,478.1 L85.9,470.4 L100,483.2 V484 A12,12 0 0 1 88,496 H48 A12,12 0 0 1 36,484 Z" fill="#FFFFFF" fill-opacity=".35"/><text x="112" y="460" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="176">Levitating</text><text x="112" y="482" font-size="13" font-weight="400" fill="#625B71" text-anchor="start">Dua Lipa</text><path d="M306,454 V472 M306,454 L316,451 V457 L306,460" fill="none" stroke="#6750A4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="302" cy="473" r="4" fill="#6750A4"/>
  </g>
  <path class="ld-amber" d="M417.2,263 H504"/>
  <path class="ar-amber" d="M504,263 H852 V564"/>
  <path class="ld-violet" d="M417.2,551 H504"/>
  <path class="ar-violet" d="M504,551 H620 V576"/>
  <path class="ld-green" d="M300.2,671 H504"/>
  <path class="ar-green" d="M504,671 H742 V610"/>
  <g transform="translate(48.0,916)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#FFF3DC" stroke="#A96C05" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="219">Tarjeta</text>
    <text class="cb" x="16" y="60" data-fit="245">Container con color, borde</text>
    <text class="cb" x="16" y="79" data-fit="245">redondeado y sombra suave.</text>
  </g>
  <g transform="translate(341.3,916)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#F4EBFF" stroke="#7439B8" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="219">Portada</text>
    <text class="cb" x="16" y="60" data-fit="245">clipBehavior recorta la imagen</text>
    <text class="cb" x="16" y="79" data-fit="245">con el borde: sin ClipRRect.</text>
  </g>
  <g transform="translate(634.7,916)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#E8F6E3" stroke="#3A8235" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="219">Datos</text>
    <text class="cb" x="16" y="60" data-fit="245">song.title y song.artist salen</text>
    <text class="cb" x="16" y="79" data-fit="245">de la Song que recibe.</text>
  </g>
</svg>
```

Va en `lib/components/song_card.dart`. Cópialo tal cual; si tu proyecto no se llama `playlist_app`, cambia el nombre en el `import`:

```dart
import 'package:flutter/material.dart';
import 'package:playlist_app/models/song.dart';

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
```

Lo que vale la pena mirar:

- **La imagen sale de la URL que se escribe.** Si el campo queda vacío, `Image.network` no tiene qué cargar y la tarjeta muestra un error en la portada. Usa `https://picsum.photos/400`.

- **Recibe un modelo, no tres textos.** `SongCard(song: song)` en vez de `SongCard(title: …, artist: …, imageUrl: …)`. Si mañana `Song` tiene duración, la tarjeta la puede mostrar sin cambiar a quien la usa.
- **La portada redondeada** es un `Container` con `borderRadius` y `clipBehavior: Clip.antiAlias`, que recorta la imagen con la forma del borde. No hace falta `ClipRRect`.
- **`maxLines: 1` con `TextOverflow.ellipsis`** corta un título largo con `…` en vez de partirlo en dos renglones o desbordar la fila.
- **`Expanded`** deja que el texto ocupe todo el espacio entre la portada y el ícono, como en la sesión 3.

## Del estado a las tarjetas

En `PlaylistScreen` solo cambia una línea del `build`. Donde estaba el `Text`, ahora va la tarjeta:

```dart
for (final song in _songs) SongCard(song: song),
```

Y arriba del archivo, el import del componente:

```dart
import 'package:playlist_app/components/song_card.dart';
```

```svg
<svg id="sgDatos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 424" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="sgDatos-ttl sgDatos-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="sgDatos-ttl">Del estado a las tarjetas</title>
  <desc id="sgDatos-dsc">A la izquierda, el estado _songs de la pantalla con tres canciones. En el centro, el código for final song in _songs, SongCard song: song. A la derecha, tres tarjetas, cada una conectada con su canción.</desc>
  <defs>
    <style>
      #sgDatos .title{fill:#161A26;font-size:22px;font-weight:700}
      #sgDatos .sub{fill:#79809A;font-size:13.5px}
      #sgDatos .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #sgDatos .nt{font-size:15px;font-weight:700;fill:#161A26}
      #sgDatos .nb{fill:#454C61;font-size:13px}
      #sgDatos .lbl{fill:#556074;font-size:12px;font-weight:600}
      #sgDatos .foot{fill:#79809A;font-size:12px}
      #sgDatos .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #sgDatos .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#sgDatos-arrow)}
    </style>
    <marker id="sgDatos-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <linearGradient id="sgDatos-cover" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B69DF8"/><stop offset="1" stop-color="#6750A4"/></linearGradient>
  </defs>
  <rect width="960" height="424" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Del estado a las tarjetas</text>
  <text class="sub" x="48" y="80" data-fit="860">La Screen tiene la lista. Por cada Song crea una SongCard y se la pasa por el constructor.</text>
  <text x="48" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="h">_PLAYLISTSCREENSTATE</text>
  <rect x="48" y="140" width="268" height="236" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="68" y="170" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">List&lt;Song&gt; _songs</text>
  <rect x="68" y="188" width="228" height="44" rx="8" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.2"/>
  <text x="80" y="207" font-size="12" font-weight="600" fill="#4453C9" text-anchor="start" class="mono">[0] Song(</text>
  <text x="92" y="224" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="196">'Imagine', 'John Lennon')</text>
  <path class="link" d="M298,210 H592"/>
  <rect x="68" y="248" width="228" height="44" rx="8" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.2"/>
  <text x="80" y="267" font-size="12" font-weight="600" fill="#4453C9" text-anchor="start" class="mono">[1] Song(</text>
  <text x="92" y="284" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="196">'Yellow', 'Coldplay')</text>
  <path class="link" d="M298,270 H592"/>
  <rect x="68" y="308" width="228" height="44" rx="8" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.2"/>
  <text x="80" y="327" font-size="12" font-weight="600" fill="#4453C9" text-anchor="start" class="mono">[2] Song(</text>
  <text x="92" y="344" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="196">'Levitating', 'Dua Lipa')</text>
  <path class="link" d="M298,330 H592"/>
  <rect x="340" y="116" width="236" height="58" rx="10" fill="#1F2430"/>
  <text x="354" y="140" font-size="12.5" font-weight="400" fill="#C9CFDA" text-anchor="start" class="mono" data-fit="208">for (final song in _songs)</text>
  <text x="369" y="160" font-size="12.5" font-weight="400" fill="#A8D8A0" text-anchor="start" class="mono" data-fit="208">SongCard(song: song)</text>
  <text x="456" y="196" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">una por canción</text>
  <text x="600" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="h">LO QUE SE VE</text>
  <rect x="600" y="184" width="312" height="52" rx="12" fill="#FFFFFF" stroke="#E6E0F2" stroke-width="1.2"/>
  <rect x="608" y="190" width="40" height="40" rx="8" fill="url(#sgDatos-cover)"/><circle cx="635.2" cy="202.8" r="4.8" fill="#FFFFFF" fill-opacity=".7"/><path d="M608,222.8 L622.4,210.0 L632.8,218.8 L639.2,214.0 L648,222.0 V222 A8,8 0 0 1 640,230 H616 A8,8 0 0 1 608,222 Z" fill="#FFFFFF" fill-opacity=".35"/>
  <text x="660" y="206" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="200">Imagine</text>
  <text x="660" y="224" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">John Lennon</text>
  <rect x="600" y="244" width="312" height="52" rx="12" fill="#FFFFFF" stroke="#E6E0F2" stroke-width="1.2"/>
  <rect x="608" y="250" width="40" height="40" rx="8" fill="url(#sgDatos-cover)"/><circle cx="635.2" cy="262.8" r="4.8" fill="#FFFFFF" fill-opacity=".7"/><path d="M608,282.8 L622.4,270.0 L632.8,278.8 L639.2,274.0 L648,282.0 V282 A8,8 0 0 1 640,290 H616 A8,8 0 0 1 608,282 Z" fill="#FFFFFF" fill-opacity=".35"/>
  <text x="660" y="266" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="200">Yellow</text>
  <text x="660" y="284" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">Coldplay</text>
  <rect x="600" y="304" width="312" height="52" rx="12" fill="#FFFFFF" stroke="#E6E0F2" stroke-width="1.2"/>
  <rect x="608" y="310" width="40" height="40" rx="8" fill="url(#sgDatos-cover)"/><circle cx="635.2" cy="322.8" r="4.8" fill="#FFFFFF" fill-opacity=".7"/><path d="M608,342.8 L622.4,330.0 L632.8,338.8 L639.2,334.0 L648,342.0 V342 A8,8 0 0 1 640,350 H616 A8,8 0 0 1 608,342 Z" fill="#FFFFFF" fill-opacity=".35"/>
  <text x="660" y="326" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="200">Levitating</text>
  <text x="660" y="344" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">Dua Lipa</text>
  <text x="48" y="404" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="864">SongCard no sabe que existe una lista: solo recibe una Song y la dibuja.</text>
</svg>
```

La Screen sigue siendo la dueña del estado: tiene `_songs`, los controllers y `_addSong`. Por cada canción crea una `SongCard` y le pasa esa canción por el constructor. La tarjeta solo la muestra. Cuando `setState` agrega una canción, `build()` corre otra vez y crea todas las tarjetas de nuevo, ahora con una más.

Esto ya lo hiciste en la sesión 3 con datos fijos, como en `ProfileInfo(name: 'Mariana Valenzuela', …)`. La diferencia es que ahora los datos salen del estado, y por eso la pantalla cambia sola cuando el estado cambia.

## Ejemplo completo

La playlist con `SongCard`: `App`, `Song`, `SongCard` y `PlaylistScreen` en un solo archivo. En tu proyecto van en `main.dart`, `models/song.dart`, `components/song_card.dart` y `screens/playlist_screen.dart`.

```dart trycode=f8b264b3dbc1ac97066fbe54e8670f5a
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
              for (final song in _songs) SongCard(song: song),
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
