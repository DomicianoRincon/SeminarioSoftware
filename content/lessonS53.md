# pushNamedAndRemoveUntil: rehacer la pila

<!-- tags: pushNamedAndRemoveUntil, (route) => false, limpiar la pila, cerrar sesión, atrás vuelve al login, predicado, quitar la flecha atrás -->

Con `pushNamed`, entrar deja el login debajo de la playlist. Atrás vuelve a él, y la flecha del `AppBar` invita a hacerlo. Al entrar se quiere otra cosa: que la playlist **reemplace** todo lo que había.

```svg
<svg id="ruPila" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 476" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ruPila-ttl ruPila-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ruPila-ttl">Entrar sin dejar el login debajo</title>
  <desc id="ruPila-dsc">Tres columnas. La primera, con pushNamed: la pila tiene PlaylistScreen encima de LoginScreen, y atrás vuelve al login. La segunda, con pushNamedAndRemoveUntil: PlaylistScreen entra arriba y LoginScreen, abajo, aparece tachada porque el predicado route flecha false responde que no se queda. La tercera, la pila nueva: solo PlaylistScreen, y atrás cierra la app.</desc>
  <defs>
    <style>
      #ruPila .title{fill:#161A26;font-size:22px;font-weight:700}
      #ruPila .sub{fill:#79809A;font-size:13.5px}
      #ruPila .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ruPila .nt{font-size:15px;font-weight:700;fill:#161A26}
      #ruPila .nb{fill:#454C61;font-size:13px}
      #ruPila .lbl{fill:#556074;font-size:12px;font-weight:600}
      #ruPila .foot{fill:#79809A;font-size:12px}
      #ruPila .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ruPila .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#ruPila-arrow)}
    </style>
    <marker id="ruPila-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="ruPila-push" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="ruPila-pop" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="ruPila-reset" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/></marker>
  </defs>
  <rect width="960" height="476" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Entrar sin dejar el login debajo</text>
  <text class="sub" x="48" y="80" data-fit="860">Con pushNamed el login sigue en la pila. Con pushNamedAndRemoveUntil sale, y atrás ya no vuelve a él.</text>
  <text x="48" y="128" font-size="14" font-weight="700" fill="#2F6FD6" text-anchor="start" class="mono" data-fit="264">pushNamed</text>
  <text x="48" y="148" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="264">El login queda debajo</text>
  <text x="348" y="128" font-size="14" font-weight="700" fill="#C2354F" text-anchor="start" class="mono" data-fit="264">pushNamedAndRemoveUntil</text>
  <text x="348" y="148" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="264">Entra y pregunta por las de abajo</text>
  <text x="648" y="128" font-size="14" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="264">La pila nueva</text>
  <text x="648" y="148" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="264">Solo queda la playlist</text>
  <rect x="48" y="176" width="264" height="52" rx="10" fill="#FFFFFF" stroke="#6750A4" stroke-width="1.5"/><text x="64" y="198" font-size="13" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">'/playlist'</text><text x="64" y="217" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">PlaylistScreen</text><rect x="232.4" y="191" width="67.6" height="22" rx="11" fill="#E8F6E3"/><text x="266.2" y="206" font-size="11.5" font-weight="600" fill="#3A8235" text-anchor="middle">visible</text>
  <rect x="48" y="238" width="264" height="52" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="64" y="260" font-size="13" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">'/'</text><text x="64" y="279" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">LoginScreen</text><rect x="191.60000000000002" y="253" width="108.4" height="22" rx="11" fill="#EEF1FF"/><text x="245.8" y="268" font-size="11.5" font-weight="600" fill="#4453C9" text-anchor="middle">debajo · viva</text>
  <path d="M48,304 H312" stroke="#C4CBD8" stroke-width="3"/><text x="180.0" y="322" font-size="11.5" font-weight="500" fill="#79809A" text-anchor="middle">base de la pila</text>
  <rect x="348" y="176" width="264" height="52" rx="10" fill="#FFFFFF" stroke="#6750A4" stroke-width="1.5"/><text x="364" y="198" font-size="13" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">'/playlist'</text><text x="364" y="217" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">PlaylistScreen</text><rect x="546.0" y="191" width="54.0" height="22" rx="11" fill="#E8F6E3"/><text x="573.0" y="206" font-size="11.5" font-weight="600" fill="#3A8235" text-anchor="middle">entra</text>
  <rect x="348" y="238" width="264" height="52" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="364" y="260" font-size="13" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">'/'</text><text x="364" y="279" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">LoginScreen</text><path d="M362,275 H448.5" stroke="#C2354F" stroke-width="1.5"/><rect x="471.2" y="253" width="128.8" height="22" rx="11" fill="#FFEBEF"/><text x="535.6" y="268" font-size="11.5" font-weight="600" fill="#C2354F" text-anchor="middle">(route) => false</text>
  <path d="M348,304 H612" stroke="#C4CBD8" stroke-width="3"/><text x="480.0" y="322" font-size="11.5" font-weight="500" fill="#79809A" text-anchor="middle">base de la pila</text>
  <rect x="648" y="238" width="264" height="52" rx="10" fill="#FFFFFF" stroke="#6750A4" stroke-width="1.5"/><text x="664" y="260" font-size="13" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">'/playlist'</text><text x="664" y="279" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">PlaylistScreen</text><rect x="832.4" y="253" width="67.6" height="22" rx="11" fill="#E8F6E3"/><text x="866.2" y="268" font-size="11.5" font-weight="600" fill="#3A8235" text-anchor="middle">visible</text>
  <path d="M648,304 H912" stroke="#C4CBD8" stroke-width="3"/><text x="780.0" y="322" font-size="11.5" font-weight="500" fill="#79809A" text-anchor="middle">base de la pila</text>
  <path d="M320,258 H340" fill="none" stroke="#C2354F" stroke-width="2.25" marker-end="url(#ruPila-reset)"/>
  <path d="M620,258 H640" fill="none" stroke="#C2354F" stroke-width="2.25" marker-end="url(#ruPila-reset)"/>
  <rect x="48" y="348" width="264" height="84" rx="12" fill="#FFFFFF" stroke="#F3A3B2" stroke-width="1.5"/><text x="64" y="379" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="236">Atrás vuelve al login</text><text x="64" y="406" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="232">La persona ya entró y el botón</text><text x="64" y="425" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="232">atrás la saca otra vez.</text>
  <rect x="348" y="348" width="264" height="84" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><text x="364" y="379" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="236">El predicado decide</text><text x="364" y="406" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="232">Se llama con cada ruta de abajo.</text><text x="364" y="425" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="232">false = esa ruta sale.</text>
  <rect x="648" y="348" width="264" height="84" rx="12" fill="#FFFFFF" stroke="#9FD68D" stroke-width="1.5"/><text x="664" y="379" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="236">Atrás cierra la app</text><text x="664" y="406" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="232">No hay nada debajo. El AppBar</text><text x="664" y="425" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="232">tampoco pone la flecha.</text>
</svg>
```

## Empujar y quitar lo de abajo

```dart
Navigator.pushNamedAndRemoveUntil(
  context,
  '/playlist',
  (route) => false,
);
```

Hace dos cosas. Primero empuja la ruta nueva, igual que `pushNamed`. Luego recorre las de abajo, de arriba hacia abajo, y a cada una le pregunta a la función del tercer parámetro si se queda.

Esa función se llama **predicado**: recibe una ruta y devuelve un `bool`. `(route) => false` responde que no a todas, así que la pila queda solo con la nueva. Con otros predicados se pueden hacer cosas más finas, pero en este curso se usa siempre `(route) => false`: rehacer la pila desde cero.

## Entrar y cerrar sesión

Los dos botones lo usan. *Entrar*, en `LoginScreen`:

```dart
FilledButton(
  onPressed: () => Navigator.pushNamedAndRemoveUntil(
    context,
    '/playlist',
    (route) => false,
  ),
  child: const Text('Entrar'),
),
```

Y *Cerrar sesión*, en la barra de `PlaylistScreen`:

```dart
IconButton(
  onPressed: () => Navigator.pushNamedAndRemoveUntil(
    context,
    '/',
    (route) => false,
  ),
  icon: const Icon(Icons.logout),
),
```

Cerrar sesión ya no puede ser un pop: debajo de la playlist no queda nada. Un pop la sacaría y la app se cerraría.

Pruébalo. Entra, cierra sesión y luego toca atrás en cada pantalla:

```interactive
nav-stack reset
```

## Ejemplo completo

Entrar y cerrar sesión rehacen la pila. La flecha `←` ya no aparece en la playlist.

```dart trycode=a1932b17a95580ccbf924329e770adef tab=run
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
        '/': (context) => const LoginScreen(),
        '/playlist': (context) => const PlaylistScreen(),
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

/// Screen where the user signs in, with simulated data.
class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Icon(Icons.queue_music, size: 72, color: Colors.deepPurple),
              const SizedBox(height: 16),
              const Text(
                'Mi playlist',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 24),
              FilledButton(
                onPressed: () => Navigator.pushNamedAndRemoveUntil(
                  context,
                  '/playlist',
                  (route) => false,
                ),
                child: const Text('Entrar'),
              ),
            ],
          ),
        ),
      ),
    );
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
      appBar: AppBar(
        title: const Text('Mi playlist'),
        actions: [
          IconButton(
            onPressed: () => Navigator.pushNamedAndRemoveUntil(
              context,
              '/',
              (route) => false,
            ),
            icon: const Icon(Icons.logout),
          ),
        ],
      ),
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
