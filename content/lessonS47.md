# Funciones como parámetro

<!-- tags: callback, Function(), Function(Song), onDelete, onAdd, widget.onAdd, el hijo avisa al padre, SongForm, formulario como componente, datos bajan eventos suben, The method 'onAdd' isn't defined -->

`SongList` recibe la lista y la muestra, pero no puede cambiarla. Ahora vienen dos cosas que sí la cambian: **quitar** una canción desde su tarjeta y **agregar** una desde el formulario. Las dos pasan en un componente, pero la lista vive en la Screen.

La salida es pasarle al componente **una función**. El componente no cambia nada: llama la función en el momento justo. Quien escribió la función, la Screen, decide qué pasa.

```svg
<svg id="fpFlechas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 548" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpFlechas-ttl fpFlechas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpFlechas-ttl">Los datos bajan, los eventos suben</title>
  <desc id="fpFlechas-dsc">Arriba, PlaylistScreen con su estado _songs. Abajo a la izquierda, SongForm, con su borrador. A la derecha, SongList y debajo SongCard. Flechas azules bajan de la Screen a SongList con songs y de SongList a SongCard con song. Flechas naranjas suben: de SongForm a la Screen con onAdd(song) y de SongCard a la Screen con onDelete(). La función de borrar la escribió la Screen, así que corre allá.</desc>
  <defs>
    <style>
      #fpFlechas .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpFlechas .sub{fill:#79809A;font-size:13.5px}
      #fpFlechas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #fpFlechas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #fpFlechas .nb{fill:#454C61;font-size:13px}
      #fpFlechas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fpFlechas .foot{fill:#79809A;font-size:12px}
      #fpFlechas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpFlechas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fpFlechas-arrow)}
    </style>
    <marker id="fpFlechas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="fpFlechas-down" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="fpFlechas-up" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="fpFlechas-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#9AA1B2"/></marker>
  </defs>
  <rect width="960" height="548" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Los datos bajan, los eventos suben</text>
  <text class="sub" x="48" y="80" data-fit="860">La Screen le pasa datos a sus hijos por el constructor. Los hijos le avisan llamando una función.</text>
  <rect x="300" y="112" width="360" height="104" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="314" y="138" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="332">PlaylistScreen</text><text x="648" y="138" font-size="12" font-weight="600" fill="#7439B8" text-anchor="end">StatefulWidget</text>
  <rect x="316" y="160" width="328" height="40" rx="8" fill="#FFFFFF" stroke="#C9A6EE"/>
  <text x="330" y="185" font-size="13" font-weight="700" fill="#1F4FA8" text-anchor="start" class="mono">List&lt;Song&gt; _songs</text>
  <text x="630" y="185" font-size="12" font-weight="400" fill="#556074" text-anchor="end" class="mono">_addSong · _deleteSong</text>
  <rect x="64" y="320" width="300" height="104" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="78" y="346" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="272">SongForm</text><text x="352" y="346" font-size="12" font-weight="600" fill="#7439B8" text-anchor="end">StatefulWidget</text>
  <rect x="80" y="368" width="268" height="40" rx="8" fill="#FFFFFF" stroke="#C9A6EE"/>
  <text x="94" y="393" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="244">Borrador: 3 controllers, _showError</text>
  <rect x="596" y="288" width="300" height="44" rx="10" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="610" y="314" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="272">SongList</text><text x="884" y="314" font-size="12" font-weight="600" fill="#556074" text-anchor="end">Stateless</text>
  <rect x="596" y="400" width="300" height="44" rx="10" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="610" y="426" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="272">SongCard</text><text x="884" y="426" font-size="12" font-weight="600" fill="#556074" text-anchor="end">Stateless</text>
  <path d="M620,216 V282" fill="none" stroke="#2F6FD6" stroke-width="2.25" marker-end="url(#fpFlechas-down)"/>
  <text x="630" y="254" font-size="13" font-weight="700" fill="#2F6FD6" text-anchor="start" class="mono">songs</text>
  <path d="M660,332 V394" fill="none" stroke="#2F6FD6" stroke-width="2.25" marker-end="url(#fpFlechas-down)"/>
  <text x="670" y="368" font-size="13" font-weight="700" fill="#2F6FD6" text-anchor="start" class="mono">song</text>
  <path d="M214,320 V164 H294" fill="none" stroke="#C27A0E" stroke-width="2.25" marker-end="url(#fpFlechas-up)"/>
  <text x="110" y="250" font-size="13" font-weight="700" fill="#C27A0E" text-anchor="start" class="mono">onAdd(song)</text>
  <path d="M896,422 H928 V164 H666" fill="none" stroke="#C27A0E" stroke-width="2.25" marker-end="url(#fpFlechas-up)"/>
  <text x="700" y="150" font-size="13" font-weight="700" fill="#C27A0E" text-anchor="start" class="mono">onDelete()</text>
  <text x="596" y="472" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">onDelete corre en la Screen: la tarjeta</text>
  <text x="596" y="490" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">solo la llama, no sabe qué hace.</text>
  <path d="M48,520 H80" stroke="#2F6FD6" stroke-width="3"/>
  <text x="88" y="524" font-size="13" font-weight="600" fill="#161A26" text-anchor="start">Datos: bajan por el constructor</text>
  <path d="M340,520 H372" stroke="#C27A0E" stroke-width="3"/>
  <text x="380" y="524" font-size="13" font-weight="600" fill="#161A26" text-anchor="start">Eventos: suben llamando una función</text>
</svg>
```

Así queda toda la sesión en una frase: **los datos bajan por el constructor y los eventos suben llamando una función**.

## Quitar: Function()

Cada `SongCard` lleva un botón con el ícono de la papelera. La tarjeta recibe una función sin parámetros y la llama cuando se pulsa:

```dart
final Song song;
final Function() onDelete;

const SongCard({super.key, required this.song, required this.onDelete});
```

Donde estaba el ícono de la nota, va el botón:

```dart
IconButton(
  onPressed: () => onDelete(),
  icon: const Icon(Icons.delete_outline),
),
```

Es lo mismo que ya haces con un `FilledButton`: `onPressed` recibe una función. La diferencia es que ahora **tu** componente también recibe una.

`SongCard` no sabe qué hace `onDelete`. Podría borrar, pedir confirmación o no hacer nada. Por eso sirve en cualquier pantalla.

## Quién escribe la función

`SongList` arma una tarjeta por canción y le entrega a cada una su `onDelete`. Lo que recibe de la Screen es una función que necesita **saber cuál canción** quitar, `Function(Song)`, y a cada tarjeta le pasa una versión sin parámetros que ya sabe cuál es:

```dart
final List<Song> songs;
final Function(Song) onDelete;
```

```dart
for (final song in songs)
  SongCard(song: song, onDelete: () => onDelete(song)),
```

La Screen escribe lo que de verdad pasa. Cambia el estado, así que va dentro de `setState`:

```dart
void _deleteSong(Song song) {
  setState(() {
    _songs.remove(song);
  });
}
```

```dart
SongList(
  songs: _songs,
  onDelete: (song) => _deleteSong(song),
),
```

`Function()` no recibe nada y `Function(Song)` recibe una canción. El tipo dice qué tiene que pasar quien la llama.

## Agregar: el formulario como componente

El formulario sale de la Screen a `lib/components/song_form.dart`. Es un componente de entrada: según la regla del curso, es un **`StatefulWidget` dueño de sus controllers**, con su `dispose()`. Lo que se está escribiendo es su **borrador**: no le interesa a nadie más hasta que se pulsa *Agregar*.

Cuando la canción está lista, `SongForm` la arma y se la entrega a quien lo use con `onAdd`:

```dart
/// Form that builds a song and hands it to whoever uses it.
class SongForm extends StatefulWidget {
  final Function(Song) onAdd;

  const SongForm({super.key, required this.onAdd});

  @override
  State<SongForm> createState() => _SongFormState();
}
```

```dart
void _submit() {
  if (_titleController.text.isEmpty || _artistController.text.isEmpty) {
    setState(() {
      _showError = true;
    });
    return;
  }
  widget.onAdd(Song(
    title: _titleController.text,
    artist: _artistController.text,
    imageUrl: _imageUrlController.text,
  ));
  _titleController.clear();
  _artistController.clear();
  setState(() {
    _showError = false;
  });
}
```

- **`widget.onAdd`.** `onAdd` es un campo del widget, `SongForm`, pero `_submit` está en el State. Desde el State, los campos del widget se leen con `widget.`. Si escribes solo `onAdd(...)`, el editor marca `The method 'onAdd' isn't defined for the type '_SongFormState'`.
- **La validación se queda aquí.** `_showError` y el `clear()` son parte del borrador, así que su `setState` es el del formulario. Si falta un dato, solo se reconstruye `SongForm`. La Screen ni se entera.
- `SongForm` nunca nombra a `PlaylistScreen` ni a `_songs`. Lo podrías usar en otra pantalla sin cambiarle una línea.

En la Screen, el formulario entero queda en una línea, y `_addSong` recibe la canción ya armada:

```dart
void _addSong(Song song) {
  setState(() {
    _songs.add(song);
  });
}
```

```dart
SongForm(onAdd: (song) => _addSong(song)),
```

Los tres controllers y su `dispose()` salieron de la Screen. Ahora su State solo tiene `_songs`.

## Pruébalo

Ahora hay dos dueños de estado. El de la Screen guarda `_songs` y el de `SongForm` guarda el borrador. Escribe y mira cuál cambia. Pulsa *Agregar* con un campo vacío y después agrega canciones y quita una. El paquete naranja es el evento que sube, y el azul, el dato que baja.

```interactive
lift events
```

Cuando quitas una canción, `onDelete()` va de la tarjeta **directo** a la Screen: la función la escribió la Screen, así que corre allá. `SongList` solo se la había entregado a la tarjeta. Esa entrega tiene nombre y es el tema de dos lecciones más adelante.

## Ejemplo completo

`App`, `Song`, `SongCard`, `SongList`, `SongForm` y `PlaylistScreen` en un archivo. En tu proyecto, `SongForm` va en `lib/components/song_form.dart`.

```dart trycode=49fb5d3becca6dfe7639a8e2a19731b1
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
  final Function() onDelete;

  const SongCard({super.key, required this.song, required this.onDelete});

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
          IconButton(
            onPressed: () => onDelete(),
            icon: const Icon(Icons.delete_outline),
          ),
        ],
      ),
    );
  }
}

/// List of songs, or a message when there are none.
class SongList extends StatelessWidget {
  final List<Song> songs;
  final Function(Song) onDelete;

  const SongList({super.key, required this.songs, required this.onDelete});

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
        for (final song in songs)
          SongCard(song: song, onDelete: () => onDelete(song)),
      ],
    );
  }
}

/// Form that builds a song and hands it to whoever uses it.
class SongForm extends StatefulWidget {
  final Function(Song) onAdd;

  const SongForm({super.key, required this.onAdd});

  @override
  State<SongForm> createState() => _SongFormState();
}

class _SongFormState extends State<SongForm> {
  final _titleController = TextEditingController();
  final _artistController = TextEditingController();
  final _imageUrlController = TextEditingController();
  bool _showError = false;

  void _submit() {
    if (_titleController.text.isEmpty || _artistController.text.isEmpty) {
      setState(() {
        _showError = true;
      });
      return;
    }
    widget.onAdd(Song(
      title: _titleController.text,
      artist: _artistController.text,
      imageUrl: _imageUrlController.text,
    ));
    _titleController.clear();
    _artistController.clear();
    setState(() {
      _showError = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
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
        if (_showError)
          const Text(
            'Escribe el nombre y el artista',
            style: TextStyle(color: Colors.red),
          ),
        FilledButton(
          onPressed: () => _submit(),
          child: const Text('Agregar'),
        ),
      ],
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

/// Screen that owns the playlist.
class PlaylistScreen extends StatefulWidget {
  const PlaylistScreen({super.key});

  @override
  State<PlaylistScreen> createState() => _PlaylistScreenState();
}

class _PlaylistScreenState extends State<PlaylistScreen> {
  final List<Song> _songs = [];

  void _addSong(Song song) {
    setState(() {
      _songs.add(song);
    });
  }

  void _deleteSong(Song song) {
    setState(() {
      _songs.remove(song);
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
              SongForm(onAdd: (song) => _addSong(song)),
              SongList(
                songs: _songs,
                onDelete: (song) => _deleteSong(song),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```
