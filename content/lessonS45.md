# Taller · Playlist, parte 1

<!-- tags: taller playlist, setState con listas, quitar de una lista, removeAt, _songs.length, mensaje de error en un formulario, lista vacía, if dentro de children, StatefulWidget con formulario, la lista no se actualiza -->

```svg
<svg id="ptMeta" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 668" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ptMeta-ttl ptMeta-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ptMeta-ttl">La playlist que vas a construir</title>
  <desc id="ptMeta-dsc">Maqueta de la app terminada: barra con el título Mi playlist y la cantidad de canciones, el formulario con un mensaje de error en rojo, y la lista de tarjetas, cada una con un ícono de quitar. Cuatro tarjetas numeradas explican las mejoras: contador en la barra, mensaje cuando faltan datos, quitar una canción y mensaje cuando la lista está vacía.</desc>
  <defs>
    <style>
      #ptMeta .title{fill:#161A26;font-size:22px;font-weight:700}
      #ptMeta .sub{fill:#79809A;font-size:13.5px}
      #ptMeta .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ptMeta .nt{font-size:15px;font-weight:700;fill:#161A26}
      #ptMeta .nb{fill:#454C61;font-size:13px}
      #ptMeta .lbl{fill:#556074;font-size:12px;font-weight:600}
      #ptMeta .foot{fill:#79809A;font-size:12px}
      #ptMeta .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ptMeta .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#ptMeta-arrow)}
    </style>
    <marker id="ptMeta-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <linearGradient id="ptMeta-cover" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B69DF8"/><stop offset="1" stop-color="#6750A4"/></linearGradient>
  </defs>
  <rect width="960" height="668" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La playlist que vas a construir</text>
  <text class="sub" x="48" y="80" data-fit="860">La app de las dos lecciones anteriores, con cuatro mejoras. Todo el estado sigue en PlaylistScreen.</text>
  <rect x="86" y="102" width="340" height="548" rx="36" fill="#1F2430"/>
  <rect x="96" y="112" width="320" height="528" rx="26" fill="#FEF7FF"/>
  <path d="M96,138 A26,26 0 0 1 122,112 H390 A26,26 0 0 1 416,138 V172 H96 Z" fill="#D0BCFF"/>
  <text x="114" y="156" font-size="17" font-weight="500" fill="#161A26" text-anchor="start">Mi playlist</text>
  <rect x="300" y="140" width="100" height="24" rx="12" fill="#FFFFFF" fill-opacity=".7"/>
  <text x="350" y="157" font-size="12" font-weight="600" fill="#4F378B" text-anchor="middle">3 canciones</text>
  <rect x="112" y="188" width="288" height="26" rx="5" fill="#FFFFFF" stroke="#8D93A5" stroke-width="1.2"/><text x="120" y="205" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="272">Nombre de la canción</text>
  <rect x="112" y="222" width="288" height="26" rx="5" fill="#FFFFFF" stroke="#8D93A5" stroke-width="1.2"/><text x="120" y="239" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="272">Artista</text>
  <rect x="112" y="256" width="288" height="26" rx="5" fill="#FFFFFF" stroke="#8D93A5" stroke-width="1.2"/><text x="120" y="273" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" data-fit="272">picsum.photos/400</text>
  <text x="114" y="302" font-size="12.5" font-weight="600" fill="#C2354F" text-anchor="start">Escribe el nombre y el artista</text>
  <rect x="112" y="314" width="288" height="34" rx="17" fill="#6750A4"/>
  <text x="256.0" y="336" font-size="13.5" font-weight="600" fill="#FFFFFF" text-anchor="middle">Agregar</text>
  <rect x="112" y="371" width="288" height="72" rx="14" fill="#6750A4" fill-opacity=".1"/>
  <rect x="112" y="368" width="288" height="72" rx="14" fill="#FFFFFF" stroke="#E6E0F2"/>
  <rect x="122" y="378" width="52" height="52" rx="10" fill="url(#ptMeta-cover)"/><circle cx="157.4" cy="394.6" r="6.2" fill="#FFFFFF" fill-opacity=".7"/><path d="M122,420.6 L140.7,404.0 L154.2,415.4 L162.6,409.2 L174,419.6 V420 A10,10 0 0 1 164,430 H132 A10,10 0 0 1 122,420 Z" fill="#FFFFFF" fill-opacity=".35"/>
  <text x="186" y="400" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="150">Imagine</text>
  <text x="186" y="420" font-size="12.5" font-weight="400" fill="#625B71" text-anchor="start">John Lennon</text>
  <path d="M367,398 H381 M371,398 V395 H377 V398 M369,398 L370,412 H378 L379,398" fill="none" stroke="#C2354F" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="112" y="455" width="288" height="72" rx="14" fill="#6750A4" fill-opacity=".1"/>
  <rect x="112" y="452" width="288" height="72" rx="14" fill="#FFFFFF" stroke="#E6E0F2"/>
  <rect x="122" y="462" width="52" height="52" rx="10" fill="url(#ptMeta-cover)"/><circle cx="157.4" cy="478.6" r="6.2" fill="#FFFFFF" fill-opacity=".7"/><path d="M122,504.6 L140.7,488.0 L154.2,499.4 L162.6,493.2 L174,503.6 V504 A10,10 0 0 1 164,514 H132 A10,10 0 0 1 122,504 Z" fill="#FFFFFF" fill-opacity=".35"/>
  <text x="186" y="484" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="150">Yellow</text>
  <text x="186" y="504" font-size="12.5" font-weight="400" fill="#625B71" text-anchor="start">Coldplay</text>
  <path d="M367,482 H381 M371,482 V479 H377 V482 M369,482 L370,496 H378 L379,482" fill="none" stroke="#C2354F" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="112" y="539" width="288" height="72" rx="14" fill="#6750A4" fill-opacity=".1"/>
  <rect x="112" y="536" width="288" height="72" rx="14" fill="#FFFFFF" stroke="#E6E0F2"/>
  <rect x="122" y="546" width="52" height="52" rx="10" fill="url(#ptMeta-cover)"/><circle cx="157.4" cy="562.6" r="6.2" fill="#FFFFFF" fill-opacity=".7"/><path d="M122,588.6 L140.7,572.0 L154.2,583.4 L162.6,577.2 L174,587.6 V588 A10,10 0 0 1 164,598 H132 A10,10 0 0 1 122,588 Z" fill="#FFFFFF" fill-opacity=".35"/>
  <text x="186" y="568" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="150">Levitating</text>
  <text x="186" y="588" font-size="12.5" font-weight="400" fill="#625B71" text-anchor="start">Dua Lipa</text>
  <path d="M367,566 H381 M371,566 V563 H377 V566 M369,566 L370,580 H378 L379,566" fill="none" stroke="#C2354F" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="294" y="134" width="112" height="36" rx="18" fill="#A96C05" fill-opacity=".08" stroke="#A96C05" stroke-width="2"/>
  <rect x="106" y="284" width="210" height="26" rx="8" fill="#C2354F" fill-opacity=".08" stroke="#C2354F" stroke-width="2"/>
  <rect x="356" y="382" width="36" height="40" rx="8" fill="#7439B8" fill-opacity=".08" stroke="#7439B8" stroke-width="2"/>
  <circle cx="294" cy="134" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="294" y="138.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">1</text>
  <circle cx="316" cy="284" r="13" fill="#FFFFFF" stroke="#C2354F" stroke-width="2"/><text x="316" y="288.5" font-size="13" font-weight="700" fill="#C2354F" text-anchor="middle">2</text>
  <circle cx="392" cy="382" r="13" fill="#FFFFFF" stroke="#7439B8" stroke-width="2"/><text x="392" y="386.5" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle">3</text>
  <rect x="480" y="112" width="432" height="112" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/>
  <circle cx="508" cy="142" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="508" y="146.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">1</text>
  <text x="532" y="147" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="360">Contador en la barra</text>
  <text x="504" y="180" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="392">El AppBar muestra cuántas canciones hay.</text><text x="504" y="200" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="392">Sale de _songs.length.</text>
  <rect x="480" y="244" width="432" height="112" rx="12" fill="#FFFFFF" stroke="#F3A3B2" stroke-width="1.5"/>
  <circle cx="508" cy="274" r="13" fill="#FFFFFF" stroke="#C2354F" stroke-width="2"/><text x="508" y="278.5" font-size="13" font-weight="700" fill="#C2354F" text-anchor="middle">2</text>
  <text x="532" y="279" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="360">Aviso cuando faltan datos</text>
  <text x="504" y="312" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="392">Si falta el nombre o el artista, no se agrega</text><text x="504" y="332" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="392">y aparece un mensaje en rojo.</text>
  <rect x="480" y="376" width="432" height="112" rx="12" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <circle cx="508" cy="406" r="13" fill="#FFFFFF" stroke="#7439B8" stroke-width="2"/><text x="508" y="410.5" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle">3</text>
  <text x="532" y="411" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="360">Quitar una canción</text>
  <text x="504" y="444" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="392">Cada tarjeta tiene un botón que la saca</text><text x="504" y="464" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="392">de _songs dentro de setState.</text>
  <rect x="480" y="508" width="432" height="112" rx="12" fill="#FFFFFF" stroke="#9FD68D" stroke-width="1.5"/>
  <circle cx="508" cy="538" r="13" fill="#FFFFFF" stroke="#3A8235" stroke-width="2"/><text x="508" y="542.5" font-size="13" font-weight="700" fill="#3A8235" text-anchor="middle">4</text>
  <text x="532" y="543" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="360">Lista vacía</text>
  <text x="504" y="576" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="392">Sin canciones, en lugar de la lista se ve</text><text x="504" y="596" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="392">Todavía no hay canciones.</text>
</svg>
```

En este taller construyes la playlist de las dos lecciones anteriores en un proyecto nuevo y le agregas cuatro mejoras. **Todo el estado vive en una sola pantalla**, `PlaylistScreen`: la lista, los controllers y las funciones que los cambian. Es la parte 1 de un taller de dos sesiones; en la sesión 7 se parte en componentes y ahí se ve por qué.

## Antes de empezar

1. Crea el proyecto desde tu carpeta `develop`, como en la sesión 1:

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

2. Arma la estructura del curso: `lib/models/`, `lib/components/` y `lib/screens/`.
3. `main.dart` con `App` y su tabla de rutas, con `'/'` apuntando a `PlaylistScreen`. Sin `home:`.
4. `Song` en `lib/models/song.dart`, como en *La lista en texto*.
5. `SongCard` en `lib/components/song_card.dart`, como te lo entregamos en *El componente SongCard*.
6. `PlaylistScreen` en `lib/screens/playlist_screen.dart`, con el `SafeArea` en el `body`, el formulario, `_addSong` y la lista de `SongCard`.

Cuando agregues una canción y aparezca su tarjeta, empieza con las mejoras. Recuerda: todos los imports del proyecto con `package:playlist_app/...`.

## 1. Contador en la barra

El `AppBar` muestra cuántas canciones hay, a la derecha del título: `3 canciones`.

- El número sale de `_songs.length`. No hace falta un campo nuevo en el estado: si la lista ya lo sabe, se le pregunta a la lista.
- Ponlo en `actions` del `AppBar`, dentro de un `Padding` para que no quede pegado al borde.
- Con una sola canción debe decir `1 canción`, no `1 canciones`.

## 2. Aviso cuando faltan datos

Hoy `_addSong` agrega lo que haya, aunque los campos estén vacíos, y no los borra después. Arregla las dos cosas:

- Si falta el nombre o el artista, no se agrega nada y aparece un mensaje en rojo debajo del formulario: `Escribe el nombre y el artista`.
- Cuando la canción sí se agrega, se borran el nombre y el artista con `clear()`, para escribir la siguiente.

- Necesitas un dato nuevo en el estado. Piensa de qué tipo: el mensaje aparece o no aparece.
- Se activa cuando falta algo y se apaga cuando la canción sí se agrega. Las dos cosas pasan dentro de `_addSong`, y las dos dentro de un `setState`.
- Para mostrarlo solo a veces, dentro de `children` se puede escribir un `if` igual que el `for`:

  ```dart
  if (_showError)
    const Text('Escribe el nombre y el artista'),
  ```

## 3. Quitar una canción

Cada tarjeta tiene un botón con el ícono `Icons.delete_outline` que saca esa canción de la lista.

- El botón va en la `SongCard`, pero la lista vive en `PlaylistScreen`. La tarjeta no puede tocar `_songs`.
- La salida es que `SongCard` reciba **una función**: un parámetro `final Function() onDelete;` que la tarjeta llama cuando se pulsa su botón (`onPressed: () => onDelete()`).
- La pantalla decide qué hace esa función al crear cada tarjeta. Quitar la canción es cambiar el estado, así que va dentro de `setState`.

Esta es la primera vez que un componente le avisa algo a la pantalla. En la sesión 7 se vuelve la forma normal de trabajar.

## 4. Lista vacía

Cuando no hay canciones, en lugar de la lista se ve el texto `Todavía no hay canciones`, centrado y en gris. Debe aparecer al abrir la app y otra vez si se quitan todas las canciones.

- Pregúntale a la lista: `_songs.isEmpty`.
- Puedes usar `if` dentro de `children`, igual que en la mejora 2.

## Qué debes tener al terminar

- El proyecto `playlist_app` con `main.dart`, `models/song.dart`, `components/song_card.dart` y `screens/playlist_screen.dart`.
- Todo el estado en `_PlaylistScreenState`: la lista, los tres controllers y el aviso de la mejora 2. Los tres controllers liberados en `dispose`.
- Las cuatro mejoras funcionando: agrega cinco canciones, intenta agregar una sin artista, quita dos y luego quita las que quedan.
- El proyecto sin errores en el editor.

Pon un `print` en el `build` de `PlaylistScreen` y otro en el de `SongCard`. Cada vez que agregas o quitas una canción, mira en la consola cuántas veces corre cada uno. Es una buena pista de lo que viene en la parte 2.

Guarda el proyecto: la sesión 7 empieza desde aquí.
