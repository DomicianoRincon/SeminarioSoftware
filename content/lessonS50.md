# Taller · Playlist navegable

<!-- tags: taller de navegación, cuatro pantallas, LoginScreen, SongDetailScreen, AddSongScreen, una Screen por archivo, saludo con el nombre, quitar desde el detalle, solo las Screens navegan -->

En esta sesión la playlist deja de ser una sola pantalla. Al final tendrá cuatro, y se podrá ir y volver entre ellas. El taller es la meta: al terminar la sesión, tu app debe moverse así.

```svg
<svg id="tnMeta" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 660" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tnMeta-ttl tnMeta-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tnMeta-ttl">Las cuatro pantallas de la playlist</title>
  <desc id="tnMeta-dsc">Cuatro celulares. A la izquierda LoginScreen con el botón Entrar; en el centro PlaylistScreen con tres canciones, el botón de cerrar sesión y el botón más; a la derecha, arriba, SongDetailScreen con la canción Yellow, y abajo AddSongScreen con el formulario. Entrar y Cerrar sesión, en rojo, usan pushNamedAndRemoveUntil. Tocar una canción y el botón más, en azul, usan pushNamed: el primero manda la canción en arguments y el segundo espera un resultado con await. Volver y Agregar, en naranja, usan pop; Agregar devuelve la canción nueva.</desc>
  <defs>
    <style>
      #tnMeta .title{fill:#161A26;font-size:22px;font-weight:700}
      #tnMeta .sub{fill:#79809A;font-size:13.5px}
      #tnMeta .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tnMeta .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tnMeta .nb{fill:#454C61;font-size:13px}
      #tnMeta .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tnMeta .foot{fill:#79809A;font-size:12px}
      #tnMeta .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tnMeta .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tnMeta-arrow)}
    </style>
    <marker id="tnMeta-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="tnMeta-push" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="tnMeta-pop" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="tnMeta-reset" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/></marker>
  </defs>
  <rect width="960" height="660" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las cuatro pantallas de la playlist</text>
  <text class="sub" x="48" y="80" data-fit="860">Cada flecha es una llamada al Navigator. El color dice cuál: abrir encima, volver o rehacer la pila.</text>
  <text x="134.0" y="186" font-size="13" font-weight="700" fill="#6750A4" text-anchor="middle" class="mono">'/'</text><text x="134.0" y="202" font-size="12" font-weight="500" fill="#556074" text-anchor="middle" class="mono">LoginScreen</text>
  <text x="402.0" y="186" font-size="13" font-weight="700" fill="#6750A4" text-anchor="middle" class="mono">'/playlist'</text><text x="402.0" y="202" font-size="12" font-weight="500" fill="#556074" text-anchor="middle" class="mono">PlaylistScreen</text>
  <text x="790.0" y="102" font-size="13" font-weight="700" fill="#6750A4" text-anchor="middle" class="mono">'/song'</text><text x="790.0" y="118" font-size="12" font-weight="500" fill="#556074" text-anchor="middle" class="mono">SongDetailScreen</text>
  <text x="790.0" y="378" font-size="13" font-weight="700" fill="#6750A4" text-anchor="middle" class="mono">'/add-song'</text><text x="790.0" y="394" font-size="12" font-weight="500" fill="#556074" text-anchor="middle" class="mono">AddSongScreen</text>
  <clipPath id="tnMeta-l"><rect width="156" height="290" rx="20"/></clipPath><rect x="49" y="205" width="170" height="304" rx="27" fill="#1F2430"/><g transform="translate(56,212)"><g clip-path="url(#tnMeta-l)"><rect width="156" height="290" rx="20" fill="#FEF7FF"/><circle cx="78.0" cy="104.39999999999999" r="22" fill="#EADDFF"/><text x="78.0" y="111.39999999999999" font-size="20" font-weight="700" fill="#6750A4" text-anchor="middle">♫</text><text x="78.0" y="154.39999999999998" font-size="14" font-weight="700" fill="#161A26" text-anchor="middle">Mi playlist</text><rect x="36.0" y="170.39999999999998" width="84" height="26.0" rx="13.0" fill="#6750A4"/><text x="78.0" y="187.39999999999998" font-size="11.5" font-weight="600" fill="#FFFFFF" text-anchor="middle">Entrar</text></g></g>
  <clipPath id="tnMeta-p"><rect width="156" height="290" rx="20"/></clipPath><rect x="317" y="205" width="170" height="304" rx="27" fill="#1F2430"/><g transform="translate(324,212)"><g clip-path="url(#tnMeta-p)"><rect width="156" height="290" rx="20" fill="#FEF7FF"/><rect width="156" height="40.0" fill="#D0BCFF"/><text x="12.0" y="26.0" font-size="13.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="114.0">Mi playlist</text><path d="M134.8,14.0 H130.0 V26.0 H134.8" fill="none" stroke="#161A26" stroke-width="1.6" stroke-linejoin="round"/><path d="M133.6,20.0 H142.6 M139.0,16.4 L142.6,20.0 L139.0,23.6" fill="none" stroke="#161A26" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><rect x="8" y="50" width="140" height="42.0" rx="10.0" fill="#FFFFFF" stroke="#E6E0F2"/><rect x="14.0" y="56.0" width="30.0" height="30.0" rx="7.0" fill="#9C7FE0"/><text x="52.0" y="69.0" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="88.0">Imagine</text><text x="52.0" y="83.0" font-size="10.0" font-weight="400" fill="#625B71" text-anchor="start" data-fit="88.0">John Lennon</text><rect x="8" y="98" width="140" height="42.0" rx="10.0" fill="#FFFFFF" stroke="#E6E0F2"/><rect x="14.0" y="104.0" width="30.0" height="30.0" rx="7.0" fill="#9C7FE0"/><text x="52.0" y="117.0" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="88.0">Yellow</text><text x="52.0" y="131.0" font-size="10.0" font-weight="400" fill="#625B71" text-anchor="start" data-fit="88.0">Coldplay</text><rect x="8" y="146" width="140" height="42.0" rx="10.0" fill="#FFFFFF" stroke="#E6E0F2"/><rect x="14.0" y="152.0" width="30.0" height="30.0" rx="7.0" fill="#9C7FE0"/><text x="52.0" y="165.0" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="88.0">Levitating</text><text x="52.0" y="179.0" font-size="10.0" font-weight="400" fill="#625B71" text-anchor="start" data-fit="88.0">Dua Lipa</text><rect x="112" y="244" width="34" height="34" rx="10" fill="#EADDFF"/><text x="129" y="267" font-size="18" font-weight="600" fill="#21005D" text-anchor="middle">+</text></g></g>
  <clipPath id="tnMeta-d"><rect width="140" height="210" rx="20"/></clipPath><rect x="713" y="121" width="154" height="224" rx="27" fill="#1F2430"/><g transform="translate(720,128)"><g clip-path="url(#tnMeta-d)"><rect width="140" height="210" rx="20" fill="#FEF7FF"/><rect width="140" height="40.0" fill="#D0BCFF"/><text x="12.0" y="26.0" font-size="15.0" font-weight="600" fill="#161A26" text-anchor="start">←</text><text x="32.0" y="26.0" font-size="13.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="100.0">Yellow</text><rect x="35.0" y="54" width="70" height="70" rx="14" fill="#9C7FE0"/><text x="70.0" y="142" font-size="13" font-weight="700" fill="#161A26" text-anchor="middle">Yellow</text><text x="70.0" y="158" font-size="11" font-weight="400" fill="#625B71" text-anchor="middle">Coldplay</text><rect x="15.0" y="170" width="110" height="26.0" rx="13.0" fill="#6750A4"/><text x="70.0" y="187.0" font-size="11.5" font-weight="600" fill="#FFFFFF" text-anchor="middle">Volver</text></g></g>
  <clipPath id="tnMeta-a"><rect width="140" height="210" rx="20"/></clipPath><rect x="713" y="397" width="154" height="224" rx="27" fill="#1F2430"/><g transform="translate(720,404)"><g clip-path="url(#tnMeta-a)"><rect width="140" height="210" rx="20" fill="#FEF7FF"/><rect width="140" height="40.0" fill="#D0BCFF"/><text x="12.0" y="26.0" font-size="15.0" font-weight="600" fill="#161A26" text-anchor="start">←</text><text x="32.0" y="26.0" font-size="13.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="100.0">Nueva canción</text><rect x="10" y="54" width="120" height="28" rx="4" fill="none" stroke="#79747E"/><text x="18" y="72" font-size="11" font-weight="400" fill="#79747E" text-anchor="start">Canción</text><rect x="10" y="90" width="120" height="28" rx="4" fill="none" stroke="#79747E"/><text x="18" y="108" font-size="11" font-weight="400" fill="#79747E" text-anchor="start">Artista</text><rect x="10.0" y="132" width="120" height="26.0" rx="13.0" fill="#6750A4"/><text x="70.0" y="149.0" font-size="11.5" font-weight="600" fill="#FFFFFF" text-anchor="middle">Agregar</text></g></g>
  <path d="M224,322 H312" fill="none" stroke="#C2354F" stroke-width="2.25" marker-end="url(#tnMeta-reset)"/>
  <rect x="237.0" y="288" width="62.0" height="24" rx="12" fill="#FFFFFF" stroke="#C2354F" stroke-width="1.5"/><text x="268.0" y="304.5" font-size="12" font-weight="600" fill="#C2354F" text-anchor="middle">Entrar</text>
  <path d="M312,402 H224" fill="none" stroke="#C2354F" stroke-width="2.25" marker-end="url(#tnMeta-reset)"/>
  <rect x="212.5" y="412" width="111.0" height="24" rx="12" fill="#FFFFFF" stroke="#C2354F" stroke-width="1.5"/><text x="268.0" y="428.5" font-size="12" font-weight="600" fill="#C2354F" text-anchor="middle">Cerrar sesión</text>
  <path d="M492,282 C592,282 598,198 708,198" fill="none" stroke="#2F6FD6" stroke-width="2.25" marker-end="url(#tnMeta-push)"/>
  <rect x="530.5" y="140" width="139.0" height="24" rx="12" fill="#FFFFFF" stroke="#2F6FD6" stroke-width="1.5"/><text x="600" y="156.5" font-size="12" font-weight="600" fill="#2F6FD6" text-anchor="middle">toque · arguments</text>
  <path d="M708,278 C618,278 582,324 492,324" fill="none" stroke="#C27A0E" stroke-width="2.25" marker-end="url(#tnMeta-pop)"/>
  <rect x="560.0" y="288" width="104.0" height="24" rx="12" fill="#FFFFFF" stroke="#C27A0E" stroke-width="1.5"/><text x="612" y="304.5" font-size="12" font-weight="600" fill="#C27A0E" text-anchor="middle">Volver · pop</text>
  <path d="M492,412 C582,412 608,474 708,474" fill="none" stroke="#2F6FD6" stroke-width="2.25" marker-end="url(#tnMeta-push)"/>
  <rect x="554.5" y="408" width="83.0" height="24" rx="12" fill="#FFFFFF" stroke="#2F6FD6" stroke-width="1.5"/><text x="596" y="424.5" font-size="12" font-weight="600" fill="#2F6FD6" text-anchor="middle">+ · await</text>
  <path d="M708,554 C598,554 592,462 492,462" fill="none" stroke="#C27A0E" stroke-width="2.25" marker-end="url(#tnMeta-pop)"/>
  <rect x="535.5" y="528" width="153.0" height="24" rx="12" fill="#FFFFFF" stroke="#C27A0E" stroke-width="1.5"/><text x="612" y="544.5" font-size="12" font-weight="600" fill="#C27A0E" text-anchor="middle">Agregar · pop(song)</text>
  <path d="M56,628 H84" stroke="#2F6FD6" stroke-width="2.5"/><text x="92" y="632.5" font-size="12.5" font-weight="500" fill="#454C61" text-anchor="start">pushNamed · abre encima</text><path d="M289,628 H317" stroke="#C27A0E" stroke-width="2.5"/><text x="325" y="632.5" font-size="12.5" font-weight="500" fill="#454C61" text-anchor="start">pop · vuelve a la de abajo</text><path d="M543,628 H571" stroke="#C2354F" stroke-width="2.5"/><text x="579" y="632.5" font-size="12.5" font-weight="500" fill="#454C61" text-anchor="start">pushNamedAndRemoveUntil · rehace la pila</text>
</svg>
```

## Dónde se trabaja

En el mismo proyecto de las sesiones 6 y 7, `playlist_app`, o en el repositorio de arranque de esta sesión. No se crea un proyecto nuevo: cada lección agrega una pantalla o una llamada al `Navigator`, y el taller suma dos mejoras al final. `PlaylistScreen` sigue siendo la dueña de la lista. Al terminar, el proyecto queda así:

```svg
<svg id="tnCarpetas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 539" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tnCarpetas-ttl tnCarpetas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tnCarpetas-ttl">Los archivos de playlist_app al terminar</title>
  <desc id="tnCarpetas-dsc">La carpeta lib con main.dart, que tiene la tabla de las cuatro rutas, y tres carpetas: models con song.dart; components con song_card.dart, song_form.dart y song_list.dart; y screens con login_screen.dart, playlist_screen.dart, song_detail_screen.dart y add_song_screen.dart. Las tres pantallas nuevas están marcadas como nuevas, y cada archivo dice si guarda estado.</desc>
  <defs>
    <style>
      #tnCarpetas .title{fill:#161A26;font-size:22px;font-weight:700}
      #tnCarpetas .sub{fill:#79809A;font-size:13.5px}
      #tnCarpetas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tnCarpetas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tnCarpetas .nb{fill:#454C61;font-size:13px}
      #tnCarpetas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tnCarpetas .foot{fill:#79809A;font-size:12px}
      #tnCarpetas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tnCarpetas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tnCarpetas-arrow)}
    </style>
    <marker id="tnCarpetas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="tnCarpetas-push" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="tnCarpetas-pop" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="tnCarpetas-reset" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/></marker>
  </defs>
  <rect width="960" height="539" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Los archivos de <tspan class="mono">playlist_app</tspan> al terminar</text>
  <text class="sub" x="48" y="80" data-fit="860">Tres pantallas nuevas en screens/. Los componentes no cambian de carpeta ni saben que hay navegación.</text>
  <rect x="48" y="104" width="864" height="403" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <path d="M72,127 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="100" y="140" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">lib/</text>
  <rect x="102" y="154" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="128" y="169" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">main.dart</text><rect x="420" y="154" width="264.8" height="22" rx="11" fill="#EEF1FF" stroke="#A9B4F2"/><text x="552.4" y="169" font-size="12" font-weight="600" fill="#4453C9" text-anchor="middle">App y la tabla de las cuatro rutas</text>
  <path d="M100,185 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="198" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">models/</text>
  <rect x="130" y="212" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="227" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">song.dart</text><rect x="420" y="212" width="142.4" height="22" rx="11" fill="#EFF1F5" stroke="#C4CBD8"/><text x="491.2" y="227" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Song con copyWith</text>
  <path d="M100,243 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="256" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">components/</text>
  <rect x="130" y="270" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="285" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">song_card.dart</text><rect x="420" y="270" width="214.4" height="22" rx="11" fill="#EFF1F5" stroke="#C4CBD8"/><text x="527.2" y="285" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Stateless · ahora con onTap</text>
  <rect x="130" y="299" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="314" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">song_form.dart</text><rect x="420" y="299" width="272.0" height="22" rx="11" fill="#F4EBFF" stroke="#C9A6EE"/><text x="556.0" y="314" font-size="12" font-weight="600" fill="#7439B8" text-anchor="middle">StatefulWidget · guarda el borrador</text>
  <rect x="130" y="328" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="343" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">song_list.dart</text><rect x="420" y="328" width="221.6" height="22" rx="11" fill="#EFF1F5" stroke="#C4CBD8"/><text x="530.8" y="343" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Stateless · ahora con onOpen</text>
  <path d="M100,359 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="372" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">screens/</text>
  <rect x="130" y="386" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="401" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">login_screen.dart</text><rect x="420" y="386" width="207.20000000000002" height="22" rx="11" fill="#F4EBFF" stroke="#C9A6EE"/><text x="523.6" y="401" font-size="12" font-weight="600" fill="#7439B8" text-anchor="middle">StatefulWidget · el nombre</text>
  <rect x="812" y="386" width="72" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D"/><text x="848" y="401" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nueva</text>
  <rect x="130" y="415" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="430" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">playlist_screen.dart</text><rect x="420" y="415" width="236.0" height="22" rx="11" fill="#F4EBFF" stroke="#C9A6EE"/><text x="538.0" y="430" font-size="12" font-weight="600" fill="#7439B8" text-anchor="middle">StatefulWidget · guarda _songs</text>
  <rect x="130" y="444" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="459" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">song_detail_screen.dart</text><rect x="420" y="444" width="200.0" height="22" rx="11" fill="#EFF1F5" stroke="#C4CBD8"/><text x="520.0" y="459" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Stateless · lee arguments</text>
  <rect x="812" y="444" width="72" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D"/><text x="848" y="459" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nueva</text>
  <rect x="130" y="473" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="488" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">add_song_screen.dart</text><rect x="420" y="473" width="257.6" height="22" rx="11" fill="#EFF1F5" stroke="#C4CBD8"/><text x="548.8" y="488" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Stateless · hospeda el formulario</text>
  <rect x="812" y="473" width="72" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D"/><text x="848" y="488" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nueva</text>
</svg>
```

## Las dos mejoras

1. **El saludo.** `LoginScreen` pide el nombre en un `TextField` y lo manda en `arguments` al entrar. La barra de la playlist dice `Hola, Ana`.
2. **Quitar desde el detalle.** `SongDetailScreen` tiene un botón *Quitar de la playlist* que la cierra devolviendo `true`. La playlist espera ese resultado y, si llega, borra la canción con la misma función de la papelera.

## Metas

Para terminar el laboratorio, cumple estas metas en orden. Cada una dice qué lección leer para hacerla.

1. Registra las cuatro rutas en `routes:` de `MaterialApp`, con cada Screen en su archivo de `screens/`. Lee: [Rutas nombradas: pushNamed y pop](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0052).
2. Haz que *Entrar* en `LoginScreen` abra la playlist y que la playlist pueda volver. Lee: [La pila de pantallas](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0051) · [Rutas nombradas: pushNamed y pop](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0052).
3. Haz que entrar y cerrar sesión rehagan la pila con `pushNamedAndRemoveUntil` y `(route) => false`. Lee: [pushNamedAndRemoveUntil: rehacer la pila](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0053).
4. Abre `SongDetailScreen` al tocar una tarjeta, con la canción en `arguments`. Lee: [Pasar datos a la pantalla nueva](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0054).
5. Muda el formulario a `AddSongScreen` y recibe la canción nueva con `await` y `pop`. Lee: [Devolver un resultado al cerrar](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0055).
6. Muestra `Hola, <nombre>` en la barra de la playlist con el nombre que se escribió en el login. Lee: [Pasar datos a la pantalla nueva](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0054).
7. Quita una canción desde su detalle cerrándolo con `pop(context, true)`. Lee: [Devolver un resultado al cerrar](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0055).

Al final, el proyecto no debe tener errores en el editor, y solo las Screens llaman al `Navigator`: `SongCard` y `SongList` avisan con una función, como la papelera.
