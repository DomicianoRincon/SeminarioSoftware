# Repositorio de arranque

<!-- tags: 262SeminarioSesion11, git clone, flutter pub get, track_app, Track, TrackService, track_services.dart, Target of URI doesn't exist -->

El taller de esta sesión no se hace sobre el proyecto de tu equipo, sino sobre una app pequeña de tracks. Clónala aparte, fuera de la carpeta de tu proyecto.

```svg
<svg id="raClonar11" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 590" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="raClonar11-ttl raClonar11-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="raClonar11-ttl">Clonar el repositorio de la sesión 11</title>
  <desc id="raClonar11-dsc">Una terminal parada en la carpeta develop. Primero git clone con la dirección de 262SeminarioSesion11, que crea la carpeta 262SeminarioSesion11. Después cd 262SeminarioSesion11, flutter pub get, que termina con Got dependencies, y flutter run -d chrome, que abre la app en Chrome. Tres recuadros numerados señalan la dirección del repositorio, flutter pub get y flutter run, cada uno con su tarjeta debajo.</desc>
  <defs>
    <style>
      #raClonar11 .title{fill:#161A26;font-size:22px;font-weight:700}
      #raClonar11 .sub{fill:#79809A;font-size:13.5px}
      #raClonar11 .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #raClonar11 .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #raClonar11 .pf{fill:#7F8AA3} #raClonar11 .cmd{fill:#FFFFFF;font-weight:600}
      #raClonar11 .dim{fill:#8A93A6} #raClonar11 .okk{fill:#6BCB77;font-weight:600}
      #raClonar11 .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #raClonar11 .chipc{fill:#F2C069} #raClonar11 .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #raClonar11 .ct{fill:#161A26;font-size:14px;font-weight:700}
      #raClonar11 .cb{fill:#454C61;font-size:13px}
      #raClonar11 .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="590" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Clonar el repositorio de la sesión 11</text>
  <text class="sub" x="48" y="80" data-fit="860">Cuatro comandos, desde la carpeta donde guardas tus proyectos.</text>
  <rect x="48" y="112" width="864" height="320" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">git clone https://github.com/Domiciano/262SeminarioSesion11.git</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="200" data-fit="816">Cloning into '262SeminarioSesion11'...</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">cd 262SeminarioSesion11</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816"><tspan class="pf">262SeminarioSesion11&gt; </tspan><tspan class="cmd">flutter pub get</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="304" data-fit="816">Resolving dependencies...</text>
  <text class="tl mono okk" font-size="13" x="72" y="330" data-fit="816">Got dependencies!</text>
  <text class="tl mono" font-size="13" x="72" y="382" data-fit="816"><tspan class="pf">262SeminarioSesion11&gt; </tspan><tspan class="cmd">flutter run -d chrome</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="408" data-fit="816">Launching lib/main.dart on Chrome in debug mode...</text>
  <rect class="ring" x="216.2" y="158" width="421.4" height="22" rx="5"/>
  <circle class="chipc" cx="637.6" cy="159" r="8"/>
  <text class="chipt" x="637.6" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="239.6" y="262" width="125.0" height="22" rx="5"/>
  <circle class="chipc" cx="364.6" cy="263" r="8"/>
  <text class="chipt" x="364.6" y="263" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <rect class="ring" x="239.6" y="366" width="171.8" height="22" rx="5"/>
  <circle class="chipc" cx="411.4" cy="367" r="8"/>
  <text class="chipt" x="411.4" y="367" dy="0.35em" text-anchor="middle" font-size="10.5">3</text>
  <g transform="translate(48.0,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">La dirección</text>
    <text class="cb" x="16" y="60" data-fit="245">Copia el proyecto en una</text>
    <text class="cb" x="16" y="79" data-fit="245">carpeta nueva con su nombre.</text>
  </g>
  <g transform="translate(341.3,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">flutter pub get</text>
    <text class="cb" x="16" y="60" data-fit="245">Baja los paquetes. Sin él,</text>
    <text class="cb" x="16" y="79" data-fit="245">el editor marca errores.</text>
  </g>
  <g transform="translate(634.7,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">3</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">flutter run</text>
    <text class="cb" x="16" y="60" data-fit="245">Abre la app en Chrome. Si</text>
    <text class="cb" x="16" y="79" data-fit="245">la ves, ya puedes empezar.</text>
  </g>
</svg>
```

```shell
git clone https://github.com/Domiciano/262SeminarioSesion11.git
cd 262SeminarioSesion11
flutter pub get
flutter run -d chrome
```

Ábrelo en VS Code con *File › Open Folder* y elige la carpeta `262SeminarioSesion11`. Si el editor marca en rojo los `import` con `Target of URI doesn't exist`, falta el `flutter pub get`.

## Qué trae

```svg
<svg id="acCarpetas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 474" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="acCarpetas-ttl acCarpetas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="acCarpetas-ttl">Lo que trae el repositorio</title>
  <desc id="acCarpetas-dsc">Árbol de lib: main.dart con las tres rutas, models con track.dart, components con track_card, track_list y track_form, screens con home_screen, add_track_screen y track_detail_screen, y services con track_services.dart vacío, señalado como lo que se llena en el taller.</desc>
  <defs>
    <style>
      #acCarpetas .title{fill:#161A26;font-size:22px;font-weight:700}
      #acCarpetas .sub{fill:#79809A;font-size:13.5px}
      #acCarpetas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #acCarpetas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #acCarpetas .nb{fill:#454C61;font-size:13px}
      #acCarpetas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #acCarpetas .foot{fill:#79809A;font-size:12px}
      #acCarpetas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #acCarpetas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#acCarpetas-arrow)}
    </style>
    <marker id="acCarpetas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="474" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Lo que trae el repositorio</text>
  <text class="sub" x="48" y="80" data-fit="860">La app ya funciona en memoria. Lo que falta está en services/.</text>
<rect x="48" y="112" width="864" height="336" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><path d="M72,127 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="100" y="140" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="56">lib/</text><rect x="102" y="151" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="128" y="166" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="96">main.dart</text><rect x="620.0" y="150" width="250.5" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="745.24" y="166.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="252">rutas '/', '/add-track' y '/track'</text><path d="M100,179 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="192" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="80">models/</text><rect x="130" y="203" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="218" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="105">track.dart</text><rect x="620.0" y="202" width="250.5" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="745.24" y="218.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="252">Track con fromMap, toMap, copyWith</text><path d="M100,231 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="244" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="113">components/</text><rect x="130" y="255" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="270" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="291">track_card.dart · track_list.dart</text><rect x="620.0" y="254" width="75.8" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="657.88" y="270.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="77">la lista</text><rect x="130" y="281" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="296" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="145">track_form.dart</text><rect x="620.0" y="280" width="163.1" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="701.56" y="296.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="165">el borrador del track</text><path d="M100,309 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="322" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="88">screens/</text><rect x="130" y="333" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="348" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="153">home_screen.dart</text><rect x="620.0" y="332" width="129.5" height="24" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.2"/><text x="684.76" y="348.5" font-size="12" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="131">dueña de _tracks</text><rect x="130" y="359" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="374" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="412">add_track_screen.dart · track_detail_screen.dart</text><path d="M100,387 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="400" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="96">services/</text><rect x="130" y="411" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="426" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="177">track_services.dart</text><rect x="620.0" y="410" width="149.7" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="694.84" y="426.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" data-fit="151">vacío: lo llenas tú</text></svg>
```

- **`HomeScreen`**: la lista de tracks y el botón *Crear track*. Es la dueña de `_tracks`.
- **`AddTrackScreen`**: el formulario. La URL de la imagen ya trae `https://picsum.photos/400`. Al guardar, devuelve el borrador con `pop`.
- **`TrackDetailScreen`**: la portada, el nombre, el artista, el `id` y el botón *Eliminar*, que devuelve `true` con `pop`.
- **`Track`**: `id`, `name`, `artistName` e `imageUrl`. `fromMap` y `toMap` ya traducen entre los nombres de Dart y las columnas de la tabla (`artist_name`, `image_url`).
- **`AGENTS.md`**: la estructura, la tabla `tracks` y las reglas, para que el agente escriba el servicio en el estilo del curso.

## Lo que falta

La app ya crea, muestra y elimina tracks, pero **solo en memoria**: recarga la página y la lista vuelve a quedar vacía. El `id` que ves en el detalle es inventado con la hora.

`lib/services/track_services.dart` trae solo la clase `TrackService`, vacía. En el taller la llenas para que los tracks se guarden en la tabla `tracks` de Supabase.

El paquete se llama `track_app`, así que los `import` del proyecto empiezan con `package:track_app/`.
