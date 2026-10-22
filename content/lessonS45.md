# Taller · Playlist con estado elevado

<!-- tags: taller playlist, elevar el estado, SongForm, SongList, callbacks, copyWith, contador en el AppBar, filtrar favoritas, where y toList, print en build, prop drilling -->

En este taller armas la playlist de la sesión en un proyecto con la estructura del curso, y le agregas tres mejoras. Cada una pone a prueba una idea de las lecciones: **el estado vive en la Screen, los datos bajan por el constructor, los eventos suben con funciones y las canciones se cambian con `copyWith`**.

```svg
<svg id="taMeta" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 600" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="taMeta-ttl taMeta-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="taMeta-ttl">Lo que vas a agregar</title>
  <desc id="taMeta-dsc">Un celular con la playlist: arriba del formulario, una fila con el texto 3 canciones y un corazón para filtrar favoritas; debajo, el formulario de tres campos y tres tarjetas con cinco estrellas, el corazón y la papelera. Tres marcas numeradas señalan el contador, el filtro y las estrellas, cada una con su tarjeta a la derecha.</desc>
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
  <text class="sub" x="48" y="80" data-fit="860">La playlist de las lecciones, con tres mejoras más. Cada una sale de la Screen o vuelve a ella.</text>
  <clipPath id="taMeta-clip"><rect width="300" height="470" rx="20"/></clipPath><rect x="73" y="97" width="314" height="484" rx="27" fill="#1F2430"/><g transform="translate(80,104)"><g clip-path="url(#taMeta-clip)"><rect width="300" height="470" rx="20" fill="#FEF7FF"/><rect width="300" height="56" fill="#D0BCFF"/><text x="16" y="34" font-size="17" font-weight="500" fill="#161A26" text-anchor="start">Mi playlist</text><text x="16" y="86" font-size="13.5" font-weight="500" fill="#1C1B1F" text-anchor="start">3 canciones</text><path d="M274,88 l-7,-7 a4.2,4.2 0 0 1 7,-5 a4.2,4.2 0 0 1 7,5 Z" fill="none" stroke="#C2354F" stroke-width="1.8" stroke-linejoin="round"/><rect x="16" y="104" width="268" height="32" rx="4" fill="none" stroke="#79747E"/><text x="28" y="125" font-size="12.5" font-weight="400" fill="#79747E" text-anchor="start">Canción</text><rect x="16" y="144" width="268" height="32" rx="4" fill="none" stroke="#79747E"/><text x="28" y="165" font-size="12.5" font-weight="400" fill="#79747E" text-anchor="start">Artista</text><rect x="16" y="184" width="268" height="32" rx="4" fill="none" stroke="#79747E"/><text x="28" y="205" font-size="12.5" font-weight="400" fill="#79747E" text-anchor="start">URL de la imagen</text><rect x="16" y="226" width="268" height="32" rx="16" fill="#6750A4"/><text x="150.0" y="247" font-size="13" font-weight="600" fill="#FFFFFF" text-anchor="middle">Agregar</text><rect x="12" y="268" width="276" height="60" rx="14" fill="#FFFFFF" stroke="#E6E0F2"/><rect x="22" y="276" width="44" height="44" rx="10" fill="#9C7FE0"/><text x="80" y="291" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Imagine</text><text x="80" y="306" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">John Lennon</text><polygon points="86.0,312.5 87.5,316.0 91.2,316.3 88.4,318.8 89.2,322.4 86.0,320.5 82.8,322.4 83.6,318.8 80.8,316.3 84.5,316.0" fill="#F2B300" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="101.0,312.5 102.5,316.0 106.2,316.3 103.4,318.8 104.2,322.4 101.0,320.5 97.8,322.4 98.6,318.8 95.8,316.3 99.5,316.0" fill="#F2B300" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="116.0,312.5 117.5,316.0 121.2,316.3 118.4,318.8 119.2,322.4 116.0,320.5 112.8,322.4 113.6,318.8 110.8,316.3 114.5,316.0" fill="#F2B300" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="131.0,312.5 132.5,316.0 136.2,316.3 133.4,318.8 134.2,322.4 131.0,320.5 127.8,322.4 128.6,318.8 125.8,316.3 129.5,316.0" fill="none" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="146.0,312.5 147.5,316.0 151.2,316.3 148.4,318.8 149.2,322.4 146.0,320.5 142.8,322.4 143.6,318.8 140.8,316.3 144.5,316.0" fill="none" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><path d="M242,304 l-7,-7 a4.2,4.2 0 0 1 7,-5 a4.2,4.2 0 0 1 7,5 Z" fill="none" stroke="#C2354F" stroke-width="1.8" stroke-linejoin="round"/><path d="M266,292 H278 M268,292 L269,306 H275 L276,292" fill="none" stroke="#49454F" stroke-width="1.6" stroke-linejoin="round"/><rect x="12" y="334" width="276" height="60" rx="14" fill="#FFFFFF" stroke="#E6E0F2"/><rect x="22" y="342" width="44" height="44" rx="10" fill="#9C7FE0"/><text x="80" y="357" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Yellow</text><text x="80" y="372" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">Coldplay</text><polygon points="86.0,378.5 87.5,382.0 91.2,382.3 88.4,384.8 89.2,388.4 86.0,386.5 82.8,388.4 83.6,384.8 80.8,382.3 84.5,382.0" fill="#F2B300" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="101.0,378.5 102.5,382.0 106.2,382.3 103.4,384.8 104.2,388.4 101.0,386.5 97.8,388.4 98.6,384.8 95.8,382.3 99.5,382.0" fill="#F2B300" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="116.0,378.5 117.5,382.0 121.2,382.3 118.4,384.8 119.2,388.4 116.0,386.5 112.8,388.4 113.6,384.8 110.8,382.3 114.5,382.0" fill="#F2B300" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="131.0,378.5 132.5,382.0 136.2,382.3 133.4,384.8 134.2,388.4 131.0,386.5 127.8,388.4 128.6,384.8 125.8,382.3 129.5,382.0" fill="#F2B300" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="146.0,378.5 147.5,382.0 151.2,382.3 148.4,384.8 149.2,388.4 146.0,386.5 142.8,388.4 143.6,384.8 140.8,382.3 144.5,382.0" fill="#F2B300" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><path d="M242,370 l-7,-7 a4.2,4.2 0 0 1 7,-5 a4.2,4.2 0 0 1 7,5 Z" fill="#C2354F" stroke="#C2354F" stroke-width="1.8" stroke-linejoin="round"/><path d="M266,358 H278 M268,358 L269,372 H275 L276,358" fill="none" stroke="#49454F" stroke-width="1.6" stroke-linejoin="round"/><rect x="12" y="400" width="276" height="60" rx="14" fill="#FFFFFF" stroke="#E6E0F2"/><rect x="22" y="408" width="44" height="44" rx="10" fill="#9C7FE0"/><text x="80" y="423" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Levitating</text><text x="80" y="438" font-size="12" font-weight="400" fill="#625B71" text-anchor="start">Dua Lipa</text><polygon points="86.0,444.5 87.5,448.0 91.2,448.3 88.4,450.8 89.2,454.4 86.0,452.5 82.8,454.4 83.6,450.8 80.8,448.3 84.5,448.0" fill="none" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="101.0,444.5 102.5,448.0 106.2,448.3 103.4,450.8 104.2,454.4 101.0,452.5 97.8,454.4 98.6,450.8 95.8,448.3 99.5,448.0" fill="none" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="116.0,444.5 117.5,448.0 121.2,448.3 118.4,450.8 119.2,454.4 116.0,452.5 112.8,454.4 113.6,450.8 110.8,448.3 114.5,448.0" fill="none" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="131.0,444.5 132.5,448.0 136.2,448.3 133.4,450.8 134.2,454.4 131.0,452.5 127.8,454.4 128.6,450.8 125.8,448.3 129.5,448.0" fill="none" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><polygon points="146.0,444.5 147.5,448.0 151.2,448.3 148.4,450.8 149.2,454.4 146.0,452.5 142.8,454.4 143.6,450.8 140.8,448.3 144.5,448.0" fill="none" stroke="#D99A00" stroke-width="1.2" stroke-linejoin="round"/><path d="M242,436 l-7,-7 a4.2,4.2 0 0 1 7,-5 a4.2,4.2 0 0 1 7,5 Z" fill="none" stroke="#C2354F" stroke-width="1.8" stroke-linejoin="round"/><path d="M266,424 H278 M268,424 L269,438 H275 L276,424" fill="none" stroke="#49454F" stroke-width="1.6" stroke-linejoin="round"/></g></g>
  <rect x="90" y="172" width="96" height="26" rx="8" fill="#A96C05" fill-opacity=".08" stroke="#A96C05" stroke-width="2"/>
  <rect x="338" y="172" width="32" height="26" rx="8" fill="#C2354F" fill-opacity=".08" stroke="#C2354F" stroke-width="2"/>
  <rect x="154" y="413" width="84" height="19" rx="6" fill="#7439B8" fill-opacity=".08" stroke="#7439B8" stroke-width="2"/>
  <rect x="480" y="112" width="432" height="124" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><circle cx="508" cy="138" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="508" y="142.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">1</text><text x="530" y="143" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="370">El resumen</text><text x="496" y="170" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">PlaylistSummary, arriba del formulario: recibe</text><text x="496" y="189" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">count desde _songs.length y el corazón.</text>
  <rect x="480" y="260" width="432" height="124" rx="12" fill="#FFFFFF" stroke="#F3A3B2" stroke-width="1.5"/><circle cx="508" cy="286" r="13" fill="#FFFFFF" stroke="#C2354F" stroke-width="2"/><text x="508" y="290.5" font-size="13" font-weight="700" fill="#C2354F" text-anchor="middle">2</text><text x="530" y="291" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="370">Solo favoritas</text><text x="496" y="318" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">El corazón avisa a la Screen, que guarda el bool.</text><text x="496" y="337" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">SongList recibe la lista ya filtrada.</text>
  <rect x="480" y="408" width="432" height="124" rx="12" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><circle cx="508" cy="434" r="13" fill="#FFFFFF" stroke="#7439B8" stroke-width="2"/><text x="508" y="438.5" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle">3</text><text x="530" y="439" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="370">Calificación</text><text x="496" y="466" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">Cinco estrellas: la tocada sube con onRate(n)</text><text x="496" y="485" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">y la Screen hace copyWith(rating: n).</text>
  <circle cx="200" cy="185" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="200" y="189.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">1</text>
  <circle cx="322" cy="185" r="13" fill="#FFFFFF" stroke="#C2354F" stroke-width="2"/><text x="322" y="189.5" font-size="13" font-weight="700" fill="#C2354F" text-anchor="middle">2</text>
  <circle cx="254" cy="422" r="13" fill="#FFFFFF" stroke="#7439B8" stroke-width="2"/><text x="254" y="426.5" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle">3</text>
  <text x="480" y="572" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="432">Y una prueba: un print en cada build para ver quién se reconstruye.</text>
</svg>
```

## Antes de empezar

Si hiciste el taller de la sesión 6, abre tu `playlist_app` y salta al paso 3. Si no, créalo desde tu carpeta `develop`:

```svg
<svg id="ptCrear" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 590" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ptCrear-ttl ptCrear-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ptCrear-ttl">Crear el proyecto playlist_app</title>
  <desc id="ptCrear-dsc">Terminal en la carpeta develop. Se ejecuta flutter create con la organización icesi.edu.co y el nombre playlist_app, la salida termina en All done, y luego cd playlist_app.</desc>
  <defs>
    <style>
      #ptCrear .title{fill:#161A26;font-size:22px;font-weight:700}
      #ptCrear .sub{fill:#79809A;font-size:13.5px}
      #ptCrear .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ptCrear .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #ptCrear .pf{fill:#7F8AA3} #ptCrear .cmd{fill:#FFFFFF;font-weight:600}
      #ptCrear .dim{fill:#8A93A6} #ptCrear .okk{fill:#6BCB77;font-weight:600}
      #ptCrear .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #ptCrear .chipc{fill:#F2C069} #ptCrear .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #ptCrear .ct{fill:#161A26;font-size:14px;font-weight:700}
      #ptCrear .cb{fill:#454C61;font-size:13px}
      #ptCrear .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="590" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Crear el proyecto <tspan class="mono">playlist_app</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">El mismo comando de la sesión 1, con otro nombre. El nombre va en minúsculas y con guion bajo.</text>
  <rect x="48" y="112" width="864" height="320" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">flutter create <tspan letter-spacing="2">-</tspan>-org icesi.edu.co playlist_app</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="200" data-fit="816">Creating project playlist_app...</text>
  <text class="tl mono dim" font-size="13" x="72" y="226" data-fit="816">Resolving dependencies in `playlist_app`...</text>
  <text class="tl mono dim" font-size="13" x="72" y="252" data-fit="816">Got dependencies in `playlist_app`.</text>
  <text class="tl mono dim" font-size="13" x="72" y="278" data-fit="816">Wrote 130 files.</text>
  <text class="tl mono okk" font-size="13" x="72" y="330" data-fit="816">All done!</text>
  <text class="tl mono" font-size="13" x="72" y="382" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">cd playlist_app</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="408" data-fit="816"><tspan class="pf">playlist_app&gt; </tspan><tspan class="cmd"></tspan></text>
  <rect class="ring" x="403.4" y="158" width="101.6" height="22" rx="5"/>
  <circle class="chipc" cx="505.0" cy="159" r="8"/>
  <text class="chipt" x="505.0" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="138.2" y="366" width="125.0" height="22" rx="5"/>
  <circle class="chipc" cx="263.2" cy="367" r="8"/>
  <text class="chipt" x="263.2" y="367" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <g transform="translate(48.0,456)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">El nombre del proyecto</text>
    <text class="cb" x="16" y="60" data-fit="392">Es también el nombre del paquete:</text>
    <text class="cb" x="16" y="79" data-fit="392">package:playlist_app/...</text>
  </g>
  <g transform="translate(488.0,456)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Entrar a la carpeta</text>
    <text class="cb" x="16" y="60" data-fit="392">Abre esta carpeta en VS Code</text>
    <text class="cb" x="16" y="79" data-fit="392">antes de crear los archivos.</text>
  </g>
</svg>
```

```shell
flutter create --org icesi.edu.co playlist_app
cd playlist_app
```

1. Arma la estructura del curso: `lib/models/`, `lib/components/` y `lib/screens/`.
2. `main.dart` con `App` y su tabla de rutas, con `'/'` apuntando a `PlaylistScreen`. Sin `home:`.
3. Lleva el código de *Modelos con copyWith* a los archivos de la figura, uno por clase. Todos los imports del proyecto van con `package:playlist_app/...`.

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

Antes de seguir, comprueba que agregar, quitar y marcar favoritas funciona igual que en el ejemplo.

## 1. El resumen

Arriba del formulario va una fila nueva: a la izquierda, cuántas canciones hay (`3 canciones`); a la derecha, un botón con un corazón.

- Es una pieza nueva, `PlaylistSummary`, en `lib/components/playlist_summary.dart`. No guarda nada, así que es `StatelessWidget`.
- Recibe el número por el constructor: `final int count;`. La Screen le pasa `_songs.length`. El dato ya existe, así que no hace falta un campo nuevo en el estado.
- Con una sola canción debe decir `1 canción`, no `1 canciones`.
- El corazón también va en `PlaylistSummary`, pero lo que hace se decide en la mejora 2. Por ahora, que reciba `final bool onlyFavorites;` para pintarse lleno o vacío y `final Function() onToggleFavorites;` para avisar que lo tocaron.

## 2. Solo favoritas

El corazón de `PlaylistSummary` alterna entre ver todas las canciones y ver solo las favoritas.

- **Dónde vive.** Ver o no las favoritas es estado de la pantalla: un `bool _onlyFavorites` en `_PlaylistScreenState`. `PlaylistSummary` lo recibe para pintar el corazón y avisa con `onToggleFavorites`. La Screen lo cambia dentro de `setState`.
- **Qué recibe `SongList`.** No le pases el `bool`: pásale **la lista ya filtrada**. `SongList` no tiene por qué saber que existe un filtro, y así no cambia su forma de trabajar. En el `build` de la Screen:

  ```dart
  final visible = _onlyFavorites
      ? _songs.where((song) => song.isFavorite).toList()
      : _songs;
  ```

- **El aviso.** Con el filtro activo y ninguna favorita, `Todavía no hay canciones` es mentira. Haz que `SongList` reciba también el texto del aviso por el constructor (`emptyMessage`), y que la Screen le pase `No tienes favoritas` cuando el filtro está activo.
- Quitar o marcar una canción con el filtro activo debe seguir funcionando. `_toggleFavorite` busca la canción en `_songs` con `indexOf`, no en la lista filtrada: piensa por qué igual la encuentra.

## 3. Calificación

Debajo del artista, cada tarjeta muestra cinco estrellas. Tocar la tercera deja la canción con tres estrellas llenas, y tocar otra la cambia.

- `Song` gana un campo `final int rating`, con valor por defecto `0`, y `copyWith` un parámetro más.
- Las estrellas son cinco `IconButton` en una `Row`, hechos con un `for` dentro de `children`. Cada una está llena si su número es menor o igual que `song.rating` (`Icons.star` o `Icons.star_border`). Para que quepan, dales `padding: EdgeInsets.zero`, `constraints: const BoxConstraints()` e `iconSize: 20`.
- Esta vez el evento **lleva un dato**: cuántas estrellas. `SongCard` recibe `Function(int) onRate` y llama `onRate(star)`. `SongList` recibe `Function(Song, int)` y le agrega la canción. La Screen hace `song.copyWith(rating: rating)` dentro de `setState`.
- Cuando termines, cuenta los parámetros de `SongList` que solo reenvía y los archivos que tocaste. Compáralo con las señales de *Prop drilling*.

## 4. Quién se reconstruye

Pon un `print` al principio del `build` de `PlaylistScreen`, `PlaylistSummary`, `SongForm`, `SongList` y `SongCard`:

```dart
print('build SongList');
```

El editor subraya el `print` con un aviso azul (`avoid_print`). Es solo una sugerencia y aquí lo usamos a propósito. Con la consola de depuración abierta:

- Escribe en el formulario. ¿Se imprime algo?
- Pulsa *Agregar* con el nombre vacío. ¿Cuál `build` corre?
- Agrega una canción y después califica una. ¿Cuáles corren?

Anota lo que ves. La respuesta al segundo punto es la razón de que el formulario sea un componente con su propio estado.

## Qué debes tener al terminar

- `playlist_app` con un archivo por clase: `main.dart`, `models/song.dart`, `components/playlist_summary.dart`, `components/song_card.dart`, `components/song_form.dart`, `components/song_list.dart` y `screens/playlist_screen.dart`.
- Solo dos `StatefulWidget`: `PlaylistScreen`, con `_songs` y `_onlyFavorites`, y `SongForm`, con su borrador. Los demás, `StatelessWidget`.
- Ningún componente toca `_songs`: todo cambio pasa por una función de la Screen, dentro de `setState`.
- Las tres mejoras funcionando. Agrega cinco canciones, marca dos, califica tres, filtra y quita las que no sean favoritas.
- El proyecto sin errores en el editor. Los avisos de los `print` no cuentan.

Guarda el proyecto: la sesión 8 le agrega una segunda pantalla.
