# Modelos con copyWith

<!-- tags: copyWith, modelo inmutable, campos final, cambiar un campo de un objeto, can't be used as a setter because it's final, favorita, isFavorite, reemplazar en la lista, _songs[index], parámetros opcionales con ?? -->

La playlist va a marcar canciones como **favoritas**: un corazón en cada tarjeta que se llena al pulsarlo. Es un dato más de la canción, y el modelo lo guarda: `Song` gana un campo.

```dart
final bool isFavorite;
```

```dart
const Song({
  required this.title,
  required this.artist,
  required this.imageUrl,
  this.isFavorite = false,
});
```

No es `required`: por defecto una canción no es favorita, así que `SongForm` sigue creando canciones igual que antes.

## El intento que no compila

Lo primero que se le ocurre a cualquiera es cambiar el campo:

```dart
song.isFavorite = true;
```

El editor lo marca de inmediato: `'isFavorite' can't be used as a setter because it's final.` Los campos de `Song` son `final` a propósito. Una `Song` no cambia nunca: si algo de la canción es distinto, **es otra `Song`**.

Suena a capricho, pero tiene una razón práctica. Si cualquiera que tenga la canción pudiera cambiarla, `SongCard` podría tocar la favorita por su cuenta sin pasar por `setState`. Sería el error de "la lista no cambia", ahora escondido dentro de un objeto. Con campos `final`, el único camino es entregarle a la Screen una canción nueva.

## copyWith

Crear "la misma canción, pero favorita" a mano es repetir los cuatro campos cada vez. Para eso el modelo trae un método, `copyWith`, que copia todo y cambia solo lo que se le pase:

```dart
Song copyWith({
  String? title,
  String? artist,
  String? imageUrl,
  bool? isFavorite,
}) {
  return Song(
    title: title ?? this.title,
    artist: artist ?? this.artist,
    imageUrl: imageUrl ?? this.imageUrl,
    isFavorite: isFavorite ?? this.isFavorite,
  );
}
```

- Cada parámetro es opcional y puede ser nulo (`String?`, `bool?`). Si no lo pasas, llega `null`.
- `??` significa "si lo de la izquierda es nulo, usa lo de la derecha". `title ?? this.title` es "el título nuevo, o si no hay, el que ya tenía".
- `this.title` es el campo del objeto. `title`, sin `this`, es el parámetro.

`song.copyWith(isFavorite: true)` devuelve una `Song` nueva con los mismos tres datos y el corazón lleno. La original no se tocó.

```svg
<svg id="cwCopia" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="cwCopia-ttl cwCopia-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="cwCopia-ttl">copyWith: una copia con un campo cambiado</title>
  <desc id="cwCopia-dsc">A la izquierda, Song número 1 con título Yellow, artista Coldplay, la URL de la imagen e isFavorite en false. Una flecha con song.copyWith(isFavorite: true) lleva a Song número 2, con los tres primeros campos copiados e isFavorite en true. Debajo, el intento song.isFavorite = true marcado como error porque el campo es final, y la lista _songs, cuya posición 1 ahora apunta a la Song nueva.</desc>
  <defs>
    <style>
      #cwCopia .title{fill:#161A26;font-size:22px;font-weight:700}
      #cwCopia .sub{fill:#79809A;font-size:13.5px}
      #cwCopia .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #cwCopia .nt{font-size:15px;font-weight:700;fill:#161A26}
      #cwCopia .nb{fill:#454C61;font-size:13px}
      #cwCopia .lbl{fill:#556074;font-size:12px;font-weight:600}
      #cwCopia .foot{fill:#79809A;font-size:12px}
      #cwCopia .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #cwCopia .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#cwCopia-arrow)}
    </style>
    <marker id="cwCopia-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="cwCopia-down" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="cwCopia-up" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="cwCopia-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#9AA1B2"/></marker>
  </defs>
  <rect width="960" height="520" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56"><tspan class="mono">copyWith</tspan>: una copia con un campo cambiado</text>
  <text class="sub" x="48" y="80" data-fit="860">Song tiene sus campos final: no se puede cambiar. Se crea otra Song igual, salvo lo que cambia.</text>
  <rect x="48" y="112" width="300" height="196" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><path d="M48,124 A12,12 0 0 1 60,112 H336 A12,12 0 0 1 348,124 V152 H48 Z" fill="#EFF1F5"/><text x="64" y="138" font-size="14" font-weight="700" fill="#556074" text-anchor="start" class="mono">Song #1</text><text x="66" y="183" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" class="mono">title</text><text x="168" y="183" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="118">'Yellow'</text><text x="66" y="217" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" class="mono">artist</text><text x="168" y="217" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="118">'Coldplay'</text><text x="66" y="251" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" class="mono">imageUrl</text><text x="168" y="251" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="118">'…/400'</text><rect x="56" y="266" width="284" height="28" rx="6" fill="#FFEBEF" stroke="#F3A3B2"/><text x="66" y="285" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" class="mono">isFavorite</text><text x="168" y="285" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="118">false</text>
  <rect x="612" y="112" width="300" height="196" rx="12" fill="#FFFFFF" stroke="#9FD68D" stroke-width="1.5"/><path d="M612,124 A12,12 0 0 1 624,112 H900 A12,12 0 0 1 912,124 V152 H612 Z" fill="#E8F6E3"/><text x="628" y="138" font-size="14" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">Song #2</text><text x="630" y="183" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" class="mono">title</text><text x="732" y="183" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="118">'Yellow'</text><text x="898" y="183" font-size="11.5" font-weight="600" fill="#79809A" text-anchor="end">copiado</text><text x="630" y="217" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" class="mono">artist</text><text x="732" y="217" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="118">'Coldplay'</text><text x="898" y="217" font-size="11.5" font-weight="600" fill="#79809A" text-anchor="end">copiado</text><text x="630" y="251" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" class="mono">imageUrl</text><text x="732" y="251" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="118">'…/400'</text><text x="898" y="251" font-size="11.5" font-weight="600" fill="#79809A" text-anchor="end">copiado</text><rect x="620" y="266" width="284" height="28" rx="6" fill="#E8F6E3" stroke="#9FD68D"/><text x="630" y="285" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" class="mono">isFavorite</text><text x="732" y="285" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="118">true</text><text x="898" y="285" font-size="11.5" font-weight="600" fill="#3A8235" text-anchor="end">cambia</text>
  <path d="M356,210 H604" fill="none" stroke="#2F6FD6" stroke-width="2.25" marker-end="url(#cwCopia-down)"/>
  <rect x="364" y="166" width="232" height="30" rx="8" fill="#1F2430"/>
  <text x="480" y="186" font-size="13" font-weight="400" fill="#C9CFDA" text-anchor="middle" class="mono">song.copyWith(</text>
  <rect x="364" y="218" width="232" height="28" rx="8" fill="#1F2430"/>
  <text x="480" y="237" font-size="13" font-weight="400" fill="#A8D8A0" text-anchor="middle" class="mono">isFavorite: true)</text>
  <rect x="48" y="332" width="300" height="56" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/>
  <text x="64" y="356" font-size="13" font-weight="700" fill="#C2354F" text-anchor="start" class="mono">song.isFavorite = true;</text>
  <text x="64" y="376" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start">No compila: isFavorite es final.</text>
  <text x="48" y="428" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="h">LA LISTA DE LA SCREEN</text>
  <rect x="48" y="440" width="272" height="36" rx="8" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="62" y="463" font-size="13" font-weight="700" fill="#556074" text-anchor="start" class="mono">[0]</text>
  <text x="96" y="463" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="212">Song #3 · Imagine</text>
  <rect x="336" y="440" width="272" height="36" rx="8" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
  <text x="350" y="463" font-size="13" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">[1]</text>
  <text x="384" y="463" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="212">Song #2 · Yellow ♥</text>
  <rect x="624" y="440" width="272" height="36" rx="8" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="638" y="463" font-size="13" font-weight="700" fill="#556074" text-anchor="start" class="mono">[2]</text>
  <text x="672" y="463" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="212">Song #4 · Levitating</text>
  <path d="M700,308 V372 H472 V434" fill="none" stroke="#2F6FD6" stroke-width="2.25" stroke-dasharray="6 5" marker-end="url(#cwCopia-down)"/>
  <text x="712" y="352" font-size="12.5" font-weight="600" fill="#2F6FD6" text-anchor="start" class="mono">_songs[1] = la copia</text>
  <text x="48" y="504" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="864">Song #1 no se tocó: ya nadie la usa y Dart la recoge. La Screen cambió su lista dentro de setState.</text>
</svg>
```

## Cambiar la lista en la Screen

El corazón está en la tarjeta, así que el evento sube como el de borrar: `SongCard` recibe `onToggleFavorite` y lo llama, y `SongList` se lo entrega con la canción. La Screen hace el cambio:

```dart
void _toggleFavorite(Song song) {
  setState(() {
    final index = _songs.indexOf(song);
    _songs[index] = song.copyWith(isFavorite: !song.isFavorite);
  });
}
```

`indexOf` busca en qué posición está la canción, y en esa posición se pone la copia. `!song.isFavorite` es "lo contrario de lo que tenía": si era favorita deja de serlo. Como todo cambio de estado, va dentro de `setState`.

En la tarjeta, el corazón lleno o vacío sale del dato:

```dart
IconButton(
  onPressed: () => onToggleFavorite(),
  icon: Icon(
    song.isFavorite ? Icons.favorite : Icons.favorite_border,
    color: Colors.pink,
  ),
),
```

## Pruébalo

Agrega canciones y marca una como favorita. Mira el número de la `Song` en el estado antes y después: `copyWith` no cambia la canción, pone **otra** en su lugar.

```interactive
lift fav
```

## Lo mismo con la lista

`_songs.add(...)` y `_songs[index] = ...` modifican la lista que ya existe, y en esta app está bien: solo la Screen la toca, y siempre dentro de `setState`. Hay quien aplica a la lista la misma idea que a `Song` y la reemplaza entera, `_songs = [..._songs, song]`. Es el mismo principio. En el curso basta con que los **modelos** no se cambien por dentro. El estado completo con `copyWith` se ve cuando la app crezca.

## Ejemplo completo

La playlist con favoritas: `Song` con `isFavorite` y `copyWith`, y el corazón en `SongCard`.

```dart trycode=5e8418ee4a6895534ee4c017bf101a84
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
  final bool isFavorite;

  const Song({
    required this.title,
    required this.artist,
    required this.imageUrl,
    this.isFavorite = false,
  });

  Song copyWith({
    String? title,
    String? artist,
    String? imageUrl,
    bool? isFavorite,
  }) {
    return Song(
      title: title ?? this.title,
      artist: artist ?? this.artist,
      imageUrl: imageUrl ?? this.imageUrl,
      isFavorite: isFavorite ?? this.isFavorite,
    );
  }
}

/// Card for a song: cover, title and artist.
class SongCard extends StatelessWidget {
  final Song song;
  final Function() onDelete;
  final Function() onToggleFavorite;

  const SongCard({
    super.key,
    required this.song,
    required this.onDelete,
    required this.onToggleFavorite,
  });

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
            onPressed: () => onToggleFavorite(),
            icon: Icon(
              song.isFavorite ? Icons.favorite : Icons.favorite_border,
              color: Colors.pink,
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
  final Function(Song) onToggleFavorite;

  const SongList({
    super.key,
    required this.songs,
    required this.onDelete,
    required this.onToggleFavorite,
  });

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
          SongCard(
            song: song,
            onDelete: () => onDelete(song),
            onToggleFavorite: () => onToggleFavorite(song),
          ),
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

  void _toggleFavorite(Song song) {
    setState(() {
      final index = _songs.indexOf(song);
      _songs[index] = song.copyWith(isFavorite: !song.isFavorite);
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
                onToggleFavorite: (song) => _toggleFavorite(song),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```
