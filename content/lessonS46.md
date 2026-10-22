# El estado entra como parámetro

<!-- tags: elevar el estado, pasar datos por el constructor, quién guarda el estado, SongList, StatelessWidget que recibe una lista, Screen dueña del estado, lista vacía, if dentro de build, un archivo con todo, lifting state up -->

La playlist de la sesión 6 funciona, pero todo vive en un solo lugar: `_PlaylistScreenState` tiene la lista, los tres controllers, el formulario, el botón y el `for` que pinta las tarjetas. Mientras la app es pequeña no importa. Cuando crece, ese archivo se vuelve el único lugar donde se puede tocar algo, y cada cambio pasa por él.

Esta sesión parte del **Ejemplo completo de *El componente SongCard***. Si hiciste el taller de la sesión 6, puedes partir de tu proyecto: lo que cambia es lo mismo.

## Quién guarda y quién muestra

Antes de mover código, una pregunta: **¿quién guarda datos y quién solo los muestra?** `SongCard` ya da la respuesta. No guarda nada: recibe una `Song` por el constructor y la dibuja. No sabe si la canción viene de una lista, de internet o de un valor fijo.

```svg
<svg id="leQuien" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 584" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="leQuien-ttl leQuien-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="leQuien-ttl">¿Quién guarda datos y quién solo los muestra?</title>
  <desc id="leQuien-dsc">El árbol de la playlist. Arriba, PlaylistScreen, con su bloque de estado: la lista _songs y los tres controllers. Debajo cuelgan AppBar, los campos del formulario, SongList y, dentro de SongList, una SongCard por canción. Una flecha azul lleva songs del estado a SongList y otra lleva song de SongList a cada SongCard. A la derecha, la regla del curso: solo la Screen, la Page y el formulario guardan estado; todo lo demás es Stateless y recibe por constructor.</desc>
  <defs>
    <style>
      #leQuien .title{fill:#161A26;font-size:22px;font-weight:700}
      #leQuien .sub{fill:#79809A;font-size:13.5px}
      #leQuien .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #leQuien .nt{font-size:15px;font-weight:700;fill:#161A26}
      #leQuien .nb{fill:#454C61;font-size:13px}
      #leQuien .lbl{fill:#556074;font-size:12px;font-weight:600}
      #leQuien .foot{fill:#79809A;font-size:12px}
      #leQuien .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #leQuien .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#leQuien-arrow)}
    </style>
    <marker id="leQuien-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="leQuien-down" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="leQuien-up" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="leQuien-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#9AA1B2"/></marker>
  </defs>
  <rect width="960" height="584" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">¿Quién guarda datos y quién solo los muestra?</text>
  <text class="sub" x="48" y="80" data-fit="860">Después del primer corte: la Screen guarda la lista y SongList la recibe por el constructor.</text>
  <rect x="48" y="112" width="320" height="44" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="62" y="138" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="292">PlaylistScreen</text><text x="356" y="138" font-size="12" font-weight="600" fill="#7439B8" text-anchor="end">StatefulWidget</text>
  <rect x="72" y="164" width="296" height="104" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="88" y="186" font-size="12" font-weight="700" fill="#7439B8" text-anchor="start" class="h">ESTADO · _PlaylistScreenState</text>
  <rect x="88" y="198" width="264" height="26" rx="6" fill="#E6F0FF" stroke="#7FA6E8"/>
  <text x="100" y="215.5" font-size="13" font-weight="700" fill="#1F4FA8" text-anchor="start" class="mono">List&lt;Song&gt; _songs</text>
  <text x="100" y="250" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" class="mono">3 × TextEditingController</text>
  <path d="M72,156 V490 M72,322 H96 M72,378 H96 M72,434 H96 M120,456 V490 H144" fill="none" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="4 4"/>
  <rect x="96" y="300" width="260" height="44" rx="10" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="110" y="326" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="232">AppBar</text>
  <rect x="96" y="356" width="260" height="44" rx="10" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="110" y="382" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="232">TextField ×3 · FilledButton</text>
  <rect x="96" y="412" width="260" height="44" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="110" y="438" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="232">SongList</text><text x="344" y="438" font-size="12" font-weight="600" fill="#4453C9" text-anchor="end">nuevo</text>
  <rect x="144" y="468" width="212" height="44" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="158" y="494" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="184">SongCard ×n</text>
  <path d="M352,211 H424 V424 H362" fill="none" stroke="#2F6FD6" stroke-width="2.25" marker-end="url(#leQuien-down)"/>
  <text x="432" y="320" font-size="13" font-weight="700" fill="#2F6FD6" text-anchor="start" class="mono">songs: _songs</text>
  <path d="M356,442 H396 V490 H362" fill="none" stroke="#2F6FD6" stroke-width="2.25" marker-end="url(#leQuien-down)"/>
  <text x="404" y="478" font-size="13" font-weight="700" fill="#2F6FD6" text-anchor="start" class="mono">song</text>
  <rect x="560" y="112" width="352" height="232" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text x="580" y="140" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="h">LA REGLA DEL CURSO</text>
  <text x="580" y="172" font-size="14" font-weight="700" fill="#161A26" text-anchor="start">Solo tres guardan estado:</text>
  <rect x="580" y="186" width="78.4" height="28" rx="14" fill="#F4EBFF" stroke="#C9A6EE"/>
  <text x="619.2" y="205" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle">Screen</text>
  <rect x="666.4" y="186" width="61.6" height="28" rx="14" fill="#F4EBFF" stroke="#C9A6EE"/>
  <text x="697.1999999999999" y="205" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle">Page</text>
  <rect x="736.0" y="186" width="112.0" height="28" rx="14" fill="#F4EBFF" stroke="#C9A6EE"/>
  <text x="792.0" y="205" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle">Formulario</text>
  <text x="580" y="240" font-size="13" font-weight="400" fill="#454C61" text-anchor="start">Son StatefulWidget. Todo lo demás es</text>
  <text x="580" y="259" font-size="13" font-weight="400" fill="#454C61" text-anchor="start">StatelessWidget: recibe los datos por</text>
  <text x="580" y="278" font-size="13" font-weight="400" fill="#454C61" text-anchor="start">el constructor y no sabe de dónde vienen.</text>
  <text x="580" y="316" font-size="13" font-weight="600" fill="#7439B8" text-anchor="start">El formulario guarda solo el borrador.</text>
  <rect x="560" y="368" width="352" height="120" rx="12" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.5"/><text x="576" y="399" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="324">SongCard ya cumplía la regla</text><text x="576" y="426" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="320">Desde la sesión 6 recibe una Song y la dibuja.</text><text x="576" y="445" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="320">SongList hace lo mismo con la lista entera:</text><text x="576" y="464" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="320">si está vacía, muestra el aviso.</text>
  <text x="48" y="552" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="864">El dato vive arriba y baja por el constructor. Ningún componente toca _songs.</text>
</svg>
```

En el curso, la regla es corta: **solo tres tipos de widget guardan estado, la Screen, la Page y el formulario**. Son los `StatefulWidget`. Todo lo demás es `StatelessWidget`: recibe lo que muestra por el constructor y no sabe de dónde viene. A eso se le llama **elevar el estado**: el dato sube a la Screen, y los componentes lo reciben desde arriba.

Las Pages llegan en la sesión 9, y el formulario como componente, en la próxima lección. Aquí basta con la Screen.

## El primer corte: SongList

El `for` que pinta las tarjetas sale de la Screen y se va a un componente propio, `SongList`, en `lib/components/song_list.dart`. Recibe **la lista entera** por el constructor:

```dart
import 'package:flutter/material.dart';
import 'package:playlist_app/components/song_card.dart';
import 'package:playlist_app/models/song.dart';

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
```

- El campo se llama `songs`, sin guion bajo: es un parámetro público del componente, no estado privado.
- `SongList` **decide con lo que recibe**. Si la lista está vacía, muestra un aviso en lugar de las tarjetas. Ese `if` antes del `return` es Dart normal: `build()` es una función y puede devolver widgets distintos según los datos.
- No hay `setState` ni `State`. `SongList` no puede cambiar la lista, y no le hace falta.

En la Screen, donde estaba el `for`, queda una línea:

```dart
SongList(songs: _songs),
```

## Pruébalo

Agrega dos o tres canciones y sigue el paquete azul. La lista cambia **solo** en el bloque de estado de la Screen. Después baja por el constructor, primero a `SongList` y luego a cada `SongCard`. Cada paso es un salto entre dos widgets.

```interactive
lift
```

Fíjate en los contadores `build ×n`: cuando la Screen corre `build()`, crea un `SongList` nuevo con la lista nueva, y ese `SongList` crea sus tarjetas. Nada se actualiza "solo": todo sale de volver a construir con el dato nuevo.

El formulario todavía es parte de la Screen y sus tres controllers siguen en el mismo State. Ese es el siguiente corte, y para hacerlo falta algo nuevo: que un componente pueda **avisarle algo a la Screen**.

## Ejemplo completo

El programa entero en un archivo: `App`, `Song`, `SongCard`, `SongList` y `PlaylistScreen`. En tu proyecto, `SongList` va en `lib/components/song_list.dart`.

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
