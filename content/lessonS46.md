# El estado entra como parámetro

<!-- tags: elevar el estado, componentizar una pantalla, pasar datos por el constructor, quién guarda el estado, SongList, StatelessWidget que recibe una lista, Screen dueña del estado, lista vacía, if dentro de build, un archivo con todo, lifting state up -->

La playlist de la sesión 6 funciona, pero tiene un problema que todavía no se nota: **no está hecha de piezas**. `PlaylistScreen` es una sola clase que guarda todas las variables y arma todos los widgets: los tres campos, el botón y la lista. `SongCard` es la única pieza con nombre propio. Cada mejora que le hagas a la app pasa por ese mismo archivo, y cada variable nueva es una línea más desde el mismo bloque de estado.

Las apps de verdad se arman al revés: **pantallas compuestas de piezas**, cada una con un nombre y un trabajo. Compara las dos versiones de la misma app:

```interactive
compose
```

- **Sin componentes** es el *Ejemplo completo* de *El componente SongCard*, de donde parte esta sesión. A la derecha está el árbol de widgets y, debajo, el estado. Cada variable tiene una línea hasta el widget que la usa, y todas salen del mismo `_PlaylistScreenState`. Agrega canciones y mira cómo el árbol crece colgado de la Screen.
- **Con componentes** es la app a la que vas a llegar en el taller: un resumen con el número de canciones y un filtro de favoritas, el formulario, y tarjetas con favorita y papelera. El árbol ahora tiene piezas con nombre: `PlaylistSummary`, `SongForm`, `SongList` y `SongCard`. Fíjate en las líneas. El estado de la Screen ya no llega a cada tarjeta: solo a `PlaylistSummary` y `SongList`, que lo reciben por el constructor. Los controllers ya no están en la Screen, sino en `SongForm`, que tiene **su propio** estado.

Pasar de una versión a la otra es el trabajo de esta sesión. Esta lección da el primer paso.

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
