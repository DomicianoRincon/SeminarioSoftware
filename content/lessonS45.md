# Taller · Playlist con estado elevado

<!-- tags: taller playlist, componentizar la playlist, PlaylistSummary, SongForm, SongList, callbacks, copyWith, filtrar favoritas, favorita y eliminar, print en build -->

En esta sesión la playlist deja de ser una sola pantalla con todo adentro y se arma con piezas. El taller es la meta: al final de la sesión, tu app debe verse así.

```svg
<svg id="taMeta" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 600" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="taMeta-ttl taMeta-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="taMeta-ttl">Lo que vas a agregar</title>
  <desc id="taMeta-dsc">Un celular con la playlist: arriba del formulario, una fila con el texto 3 canciones y un corazón para filtrar favoritas; debajo, el formulario de tres campos y tres tarjetas con el corazón y la papelera. Dos marcas numeradas señalan el contador y el filtro, cada una con su tarjeta a la derecha.</desc>
  <defs>
    <style>
      #taMeta .title{fill:#161A26;font-size:22px;font-weight:700}
      #taMeta .sub{fill:#79809A;font-size:13.5px}
      #taMeta .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #taMeta .nt{font-size:15px;font-weight:700;fill:#161A26}
      #taMeta .nb{fill:#454C61;font-size:13px}
      #taMeta .lbl{fill:#556074;font-size:12px;font-weight:600}
      #taMeta .foot{fill:#79809A;font-size:12px}
      #taMeta .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #taMeta .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#taMeta-arrow)}
    </style>
    <marker id="taMeta-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="taMeta-down" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="taMeta-up" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="taMeta-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#9AA1B2"/></marker>
  </defs>
  <rect width="960" height="600" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Lo que vas a agregar</text>
  <text class="sub" x="48" y="80" data-fit="860">La playlist de las lecciones, con dos mejoras más. Las dos salen de la Screen y vuelven a ella.</text>
  <clipPath id="taMeta-clip"><rect width="300" height="470" rx="20"/></clipPath><rect x="73" y="97" width="314" height="484" rx="27" fill="#1F2430"/><g transform="translate(80,104)"><g clip-path="url(#taMeta-clip)"><rect width="300" height="470" rx="20" fill="#FEF7FF"/><rect width="300" height="56" fill="#D0BCFF"/><text x="16" y="34" font-size="17" font-weight="500" fill="#161A26" text-anchor="start">Mi playlist</text><text x="16" y="86" font-size="13.5" font-weight="500" fill="#1C1B1F" text-anchor="start">3 canciones</text><path d="M274,88 l-7,-7 a4.2,4.2 0 0 1 7,-5 a4.2,4.2 0 0 1 7,5 Z" fill="none" stroke="#C2354F" stroke-width="1.8" stroke-linejoin="round"/><rect x="16" y="104" width="268" height="32" rx="4" fill="none" stroke="#79747E"/><text x="28" y="125" font-size="12.5" font-weight="400" fill="#79747E" text-anchor="start">Canción</text><rect x="16" y="144" width="268" height="32" rx="4" fill="none" stroke="#79747E"/><text x="28" y="165" font-size="12.5" font-weight="400" fill="#79747E" text-anchor="start">Artista</text><rect x="16" y="184" width="268" height="32" rx="4" fill="none" stroke="#79747E"/><text x="28" y="205" font-size="12.5" font-weight="400" fill="#79747E" text-anchor="start">URL de la imagen</text><rect x="16" y="226" width="268" height="32" rx="16" fill="#6750A4"/><text x="150.0" y="247" font-size="13" font-weight="600" fill="#FFFFFF" text-anchor="middle">Agregar</text><rect x="12" y="268" width="276" height="60" rx="14" fill="#FFFFFF" stroke="#E6E0F2"/><rect x="22" y="276" width="44" height="44" rx="10" fill="#9C7FE0"/><text x="80" y="295" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Imagine</text><text x="80" y="312" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">John Lennon</text><path d="M242,304 l-7,-7 a4.2,4.2 0 0 1 7,-5 a4.2,4.2 0 0 1 7,5 Z" fill="none" stroke="#C2354F" stroke-width="1.8" stroke-linejoin="round"/><path d="M266,292 H278 M268,292 L269,306 H275 L276,292" fill="none" stroke="#49454F" stroke-width="1.6" stroke-linejoin="round"/><rect x="12" y="334" width="276" height="60" rx="14" fill="#FFFFFF" stroke="#E6E0F2"/><rect x="22" y="342" width="44" height="44" rx="10" fill="#9C7FE0"/><text x="80" y="361" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Yellow</text><text x="80" y="378" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">Coldplay</text><path d="M242,370 l-7,-7 a4.2,4.2 0 0 1 7,-5 a4.2,4.2 0 0 1 7,5 Z" fill="#C2354F" stroke="#C2354F" stroke-width="1.8" stroke-linejoin="round"/><path d="M266,358 H278 M268,358 L269,372 H275 L276,358" fill="none" stroke="#49454F" stroke-width="1.6" stroke-linejoin="round"/><rect x="12" y="400" width="276" height="60" rx="14" fill="#FFFFFF" stroke="#E6E0F2"/><rect x="22" y="408" width="44" height="44" rx="10" fill="#9C7FE0"/><text x="80" y="427" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Levitating</text><text x="80" y="444" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">Dua Lipa</text><path d="M242,436 l-7,-7 a4.2,4.2 0 0 1 7,-5 a4.2,4.2 0 0 1 7,5 Z" fill="none" stroke="#C2354F" stroke-width="1.8" stroke-linejoin="round"/><path d="M266,424 H278 M268,424 L269,438 H275 L276,424" fill="none" stroke="#49454F" stroke-width="1.6" stroke-linejoin="round"/></g></g>
  <rect x="90" y="172" width="96" height="26" rx="8" fill="#A96C05" fill-opacity=".08" stroke="#A96C05" stroke-width="2"/>
  <rect x="338" y="172" width="32" height="26" rx="8" fill="#C2354F" fill-opacity=".08" stroke="#C2354F" stroke-width="2"/>
  <rect x="480" y="112" width="432" height="124" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><circle cx="508" cy="138" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="508" y="142.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">1</text><text x="530" y="143" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="370">El resumen</text><text x="496" y="170" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">PlaylistSummary, arriba del formulario: recibe</text><text x="496" y="189" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">count desde _songs.length y el corazón.</text>
  <rect x="480" y="260" width="432" height="124" rx="12" fill="#FFFFFF" stroke="#F3A3B2" stroke-width="1.5"/><circle cx="508" cy="286" r="13" fill="#FFFFFF" stroke="#C2354F" stroke-width="2"/><text x="508" y="290.5" font-size="13" font-weight="700" fill="#C2354F" text-anchor="middle">2</text><text x="530" y="291" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="370">Solo favoritas</text><text x="496" y="318" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">El corazón avisa a la Screen, que guarda el bool.</text><text x="496" y="337" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">SongList recibe la lista ya filtrada.</text>
  <circle cx="200" cy="185" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="200" y="189.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">1</text>
  <circle cx="322" cy="185" r="13" fill="#FFFFFF" stroke="#C2354F" stroke-width="2"/><text x="322" y="189.5" font-size="13" font-weight="700" fill="#C2354F" text-anchor="middle">2</text>
  <text x="480" y="424" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="432">Y una prueba: un print en cada build para ver quién se reconstruye.</text>
</svg>
```

## Dónde se trabaja

En el mismo repositorio de la sesión 6, `playlist_app`. No se crea un proyecto nuevo: cada lección de la sesión agrega una pieza sobre lo que ya tienes, y el taller suma dos mejoras al final. Al terminar, el proyecto queda así:

```svg
<svg id="taCarpetas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 481" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="taCarpetas-ttl taCarpetas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="taCarpetas-ttl">Los archivos de playlist_app</title>
  <desc id="taCarpetas-dsc">La carpeta lib con main.dart y tres carpetas: models con song.dart, components con song_card.dart, song_form.dart y song_list.dart, y screens con playlist_screen.dart. Al lado de cada archivo, una etiqueta: playlist_screen y song_form son StatefulWidget y guardan estado; los demás son Stateless.</desc>
  <defs>
    <style>
      #taCarpetas .title{fill:#161A26;font-size:22px;font-weight:700}
      #taCarpetas .sub{fill:#79809A;font-size:13.5px}
      #taCarpetas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #taCarpetas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #taCarpetas .nb{fill:#454C61;font-size:13px}
      #taCarpetas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #taCarpetas .foot{fill:#79809A;font-size:12px}
      #taCarpetas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #taCarpetas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#taCarpetas-arrow)}
    </style>
    <marker id="taCarpetas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="taCarpetas-down" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="taCarpetas-up" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="taCarpetas-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#9AA1B2"/></marker>
  </defs>
  <rect width="960" height="481" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Los archivos de <tspan class="mono">playlist_app</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Un archivo por clase. Solo dos guardan estado: la Screen y el formulario.</text>
  <rect x="48" y="104" width="864" height="345" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <path d="M72,127 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="100" y="140" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">lib/</text>
  <rect x="102" y="154" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="128" y="169" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">main.dart</text><rect x="420" y="154" width="185.6" height="22" rx="11" fill="#EFF1F5" stroke="#C4CBD8"/><text x="512.8" y="169" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">App y la tabla de rutas</text>
  <path d="M100,185 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="198" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">models/</text>
  <rect x="130" y="212" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="227" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">song.dart</text><rect x="420" y="212" width="142.4" height="22" rx="11" fill="#EFF1F5" stroke="#C4CBD8"/><text x="491.2" y="227" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Song con copyWith</text>
  <path d="M100,243 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="256" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">components/</text>
  <rect x="130" y="270" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="285" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">playlist_summary.dart</text><rect x="420" y="270" width="84.8" height="22" rx="11" fill="#EFF1F5" stroke="#C4CBD8"/><text x="462.4" y="285" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Stateless</text>
  <rect x="130" y="299" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="314" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">song_card.dart</text><rect x="420" y="299" width="84.8" height="22" rx="11" fill="#EFF1F5" stroke="#C4CBD8"/><text x="462.4" y="314" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Stateless</text>
  <rect x="130" y="328" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="343" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">song_form.dart</text><rect x="420" y="328" width="272.0" height="22" rx="11" fill="#F4EBFF" stroke="#C9A6EE"/><text x="556.0" y="343" font-size="12" font-weight="600" fill="#7439B8" text-anchor="middle">StatefulWidget · guarda el borrador</text>
  <rect x="130" y="357" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="372" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">song_list.dart</text><rect x="420" y="357" width="84.8" height="22" rx="11" fill="#EFF1F5" stroke="#C4CBD8"/><text x="462.4" y="372" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Stateless</text>
  <path d="M100,388 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="401" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">screens/</text>
  <rect x="130" y="415" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="430" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">playlist_screen.dart</text><rect x="420" y="415" width="236.0" height="22" rx="11" fill="#F4EBFF" stroke="#C9A6EE"/><text x="538.0" y="430" font-size="12" font-weight="600" fill="#7439B8" text-anchor="middle">StatefulWidget · guarda _songs</text>
</svg>
```

## Las dos mejoras

1. **El resumen.** Arriba del formulario, `PlaylistSummary` muestra cuántas canciones hay (`3 canciones`) y un corazón. Recibe el número por el constructor, sacado de `_songs.length`.
2. **Solo favoritas.** El corazón alterna entre ver todas las canciones o solo las favoritas. El `bool` vive en la Screen, y `SongList` recibe la lista ya filtrada, con el aviso `No tienes favoritas` cuando no hay ninguna.
Y una prueba: pon un `print` en el `build` de cada pieza y mira quién se reconstruye cuando escribes, cuando falta un dato y cuando marcas una favorita.

## Qué debes tener al terminar

- Un archivo por clase, como en la figura. Solo dos `StatefulWidget`: `PlaylistScreen`, con `_songs` y `_onlyFavorites`, y `SongForm`, con su borrador.
- Ningún componente toca `_songs`: todo cambio pasa por una función de la Screen, dentro de `setState`.
- Las dos mejoras funcionando y el proyecto sin errores en el editor. Los avisos de los `print` no cuentan.
