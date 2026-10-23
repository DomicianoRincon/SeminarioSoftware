# Funciones como parámetro

<!-- tags: callback, pasar una función por el constructor, Function(), Function(Song), onDelete, onAdd, widget.onAdd, el hijo avisa al padre, SongForm, formulario como componente, datos bajan eventos suben, The method 'onAdd' isn't defined -->

Ahora cada tarjeta necesita una papelera para quitar su canción. Y aparece un problema: la lista vive en el State de la Screen, que es el único que puede cambiarla, pero la papelera vive en `SongCard`, dos niveles más abajo. ¿Quién borra?

La respuesta es **una función que baja**. Recórrelo con *Siguiente* y, al final, toca una papelera:

```interactive
callback
```

La función nace donde vive el estado, baja por los constructores como cualquier otro dato y llega al botón. Cuando alguien toca el botón, la llamada recorre el camino al revés y termina en el `setState` de la Screen.

## Nivel 1: la función nace junto al estado

Solo el State de la Screen puede cambiar `_songs`, así que ahí se escribe la función que borra:

```dart
void _deleteSong(Song song) {
  setState(() {
    _songs.remove(song);
  });
}
```

En este nivel no hay ningún botón que la llame, así que se entrega hacia abajo, junto con la lista:

```dart
SongList(
  songs: _songs,
  onDelete: (song) => _deleteSong(song),
),
```

`(song) => _deleteSong(song)` es una función: recibe una canción y llama a `_deleteSong` con ella.

## Nivel 2: SongList solo la pasa

`SongList` recibe la función por el constructor. No la usa: solo la reparte. Es el mismo prop drilling de la lista, ahora con una función.

```dart
final List<Song> songs;
final Function(Song) onDelete;
```

A cada tarjeta le da una versión que ya sabe cuál es su canción:

```dart
for (final song in songs)
  SongCard(song: song, onDelete: () => onDelete(song)),
```

## Nivel 3: SongCard la conecta al botón

`SongCard` recibe una función sin parámetros y la llama cuando se pulsa la papelera:

```dart
final Song song;
final Function() onDelete;

const SongCard({super.key, required this.song, required this.onDelete});
```

```dart
IconButton(
  onPressed: () => onDelete(),
  icon: const Icon(Icons.delete_outline),
),
```

Es lo mismo que ya haces con un `FilledButton`: `onPressed` recibe una función. La diferencia es que ahora **tu** componente también recibe una. `SongCard` no sabe qué hace `onDelete`: podría borrar, pedir confirmación o no hacer nada.

El tipo dice qué tiene que pasar quien la llama. `Function(Song)` recibe una canción y `Function()` no recibe nada, porque cada tarjeta ya sabe cuál es la suya.

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
