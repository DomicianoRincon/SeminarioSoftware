# Pasar datos a la pantalla nueva

<!-- tags: arguments, ModalRoute.of(context), settings.arguments, as Song, pasar datos entre pantallas, pantalla de detalle, type 'Null' is not a subtype of type, GestureDetector, onTap en una tarjeta -->

Tocar una canción debe abrir su detalle. La pantalla es una sola, `SongDetailScreen`, pero cada vez muestra una canción distinta: la que se tocó. Esa canción tiene que viajar con la ruta.

Toca una canción y sigue el paquete azul:

```interactive
nav-result args
```

## La tarjeta avisa, la Screen navega

`SongCard` no abre nada por su cuenta. Igual que con la papelera, avisa con una función:

```dart
final Function() onTap;
```

Para que toda la tarjeta se pueda tocar, el `Container` que ya tenía pasa a ser el `child` de un `GestureDetector`, que detecta el toque:

```dart
return GestureDetector(
  onTap: () => onTap(),
  child: Container(
```

`SongList` le da a cada tarjeta un `onTap` que ya sabe cuál es su canción, y sube la llamada con `onOpen`, igual que `onDelete`:

```dart
SongCard(
  song: song,
  onDelete: () => onDelete(song),
  onToggleFavorite: () => onToggleFavorite(song),
  onTap: () => onOpen(song),
),
```

Solo la Screen llama al `Navigator`. Los componentes no saben que existen otras pantallas, y por eso sirven en cualquier parte.

## arguments: la canción viaja con la ruta

```svg
<svg id="paArgs" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 527" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="paArgs-ttl paArgs-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="paArgs-ttl">La canción viaja en arguments</title>
  <desc id="paArgs-dsc">Arriba, en PlaylistScreen, Navigator.pushNamed con context, el nombre barra song y arguments igual a song. Abajo, en SongDetailScreen, final song igual a ModalRoute.of context, settings.arguments as Song. A la derecha, la ruta nueva con su settings: name barra song y arguments con la canción Yellow. Una flecha va del nombre al name, otra de arguments a arguments, y otra de settings.arguments a la misma caja. La última va de as Song a una tarjeta que explica que arguments llega como Object con signo de pregunta. Debajo, el error que sale si se olvida arguments.</desc>
  <defs>
    <style>
      #paArgs .title{fill:#161A26;font-size:22px;font-weight:700}
      #paArgs .sub{fill:#79809A;font-size:13.5px}
      #paArgs .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #paArgs .cl{font-size:13px;fill:#C9CFDA}
      #paArgs .s{fill:#A8D8A0} #paArgs .n{fill:#F2B880} #paArgs .c{fill:#7FD1E8}
      #paArgs .p{fill:#D5B8F5} #paArgs .k{fill:#F08FB0}
      #paArgs .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #paArgs .ct{fill:#161A26;font-size:14px;font-weight:700}
      #paArgs .cb{fill:#454C61;font-size:13px}
      #paArgs .rt{fill:#161A26;font-size:14px} #paArgs .rs{fill:#79809A;font-size:12px}
      #paArgs .foot{fill:#79809A;font-size:12px}
      #paArgs .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #paArgs .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #paArgs .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#paArgs-ar-amber)}
      #paArgs .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #paArgs .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #paArgs .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#paArgs-ar-indigo)}
      #paArgs .hl-teal{fill:#86D3CA;fill-opacity:.16;stroke:#86D3CA;stroke-width:1.5}
      #paArgs .ld-teal{fill:none;stroke:#86D3CA;stroke-width:1.5;stroke-dasharray:3 4}
      #paArgs .ar-teal{fill:none;stroke:#0F8478;stroke-width:1.75;marker-end:url(#paArgs-ar-teal)}
    </style>
    <marker id="paArgs-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="paArgs-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="paArgs-ar-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#0F8478"/></marker>
  </defs>
  <rect width="960" height="527" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La canción viaja en <tspan class="mono">arguments</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">pushNamed mete la canción en la ruta nueva. La pantalla que llega la saca de ahí en su build.</text>
  <rect x="48" y="112" width="456" height="276" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/</text>
  <rect x="552" y="112" width="360" height="276" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">LO QUE LLEVA LA RUTA</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="79.6" y="204" width="62.6" height="22" rx="5"/>
  <rect class="hl-teal" x="79.6" y="228" width="78.2" height="22" rx="5"/>
  <rect class="hl-amber" x="251.2" y="324" width="62.6" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="156.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Navigator</tspan>.pushNamed(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="62.4" lengthAdjust="spacingAndGlyphs" data-fit="432">context,</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="62.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">'/song'</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">arguments</tspan>: song,</text>
  <text class="cl mono" font-size="13" x="68.0" y="268" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">);</text>
  <text class="cl mono" font-size="13" x="68.0" y="316" textLength="280.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">final</tspan> song = <tspan class="c">ModalRoute</tspan>.of(context)!</text>
  <text class="cl mono" font-size="13" x="99.2" y="340" textLength="218.4" lengthAdjust="spacingAndGlyphs" data-fit="432">.settings.arguments as <tspan class="c">Song</tspan>;</text>
  <g transform="translate(552,144)">
<rect x="16" y="16" width="328" height="124" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="32" y="42" font-size="12" font-weight="700" fill="#4453C9" text-anchor="start" class="h">La ruta nueva · settings</text><rect x="28" y="56" width="304" height="30" rx="7" fill="#FFFFFF" stroke="#D9DEE8"/><text x="40" y="76" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" class="mono">name: '/song'</text><rect x="28" y="96" width="304" height="30" rx="7" fill="#E6F0FF" stroke="#7FA6E8"/><text x="40" y="116" font-size="13" font-weight="600" fill="#1F4FA8" text-anchor="start" class="mono">arguments: Song('Yellow')</text><g transform="translate(16,160)"><rect width="328" height="62" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#A96C05" data-fit="300">as Song</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">arguments llega como Object?.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">as Song le dice a Dart qué es.</text></g>
  </g>
  <path class="ld-indigo" d="M152.0,215 H504"/>
  <path class="ar-indigo" d="M504,215 H580"/>
  <path class="ld-teal" d="M214.4,239 H504"/>
  <path class="ar-teal" d="M504,239 H523 V252 H580"/>
  <path class="ld-amber" d="M323.6,335 H504"/>
  <path class="ar-amber" d="M504,335 H514 V334 H568"/>
  <g transform="translate(48.0,412)">
    <rect width="864.0" height="83" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#FFEBEF" stroke="#C2354F" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="806">type 'Null' is not a subtype of type 'Song' in type cast</text>
    <text class="cb" x="16" y="60" data-fit="832">Se olvidó arguments en el pushNamed: la ruta llegó vacía, settings.arguments vale null y el as Song falla.</text>
  </g>
</svg>
```

En `PlaylistScreen`, la función que abre el detalle manda la canción en `arguments`:

```dart
void _openSong(Song song) {
  Navigator.pushNamed(context, '/song', arguments: song);
}
```

`arguments` acepta cualquier objeto. Se guarda dentro de la ruta nueva, en `settings.arguments`, y se registra en la tabla como cualquier otra: `'/song': (context) => const SongDetailScreen()`.

## SongDetailScreen la lee en build

```dart
final song = ModalRoute.of(context)!.settings.arguments as Song;
```

`ModalRoute.of(context)` es la ruta en la que vive esta pantalla, y sus `settings` traen el nombre y los argumentos. `arguments` es de tipo `Object?`: puede ser cualquier cosa, o nada. Por eso `as Song` le dice a Dart qué es.

`SongDetailScreen` es un `StatelessWidget`: todo lo que muestra sale de esa línea. Su botón *Volver a la lista* es un `Navigator.pop(context)`.

Si alguien abre `'/song'` sin argumentos, `arguments` vale `null` y el `as Song` falla:

```text
type 'Null' is not a subtype of type 'Song' in type cast
```

Pruébalo en el interactivo con *Olvidar arguments*.

## Ejemplo completo

La playlist con la pantalla de detalle. Para probarlo, agrega una canción y tócala.

```dart
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
        '/song': (context) => const SongDetailScreen(),
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
  final Function() onTap;

  const SongCard({
    super.key,
    required this.song,
    required this.onDelete,
    required this.onToggleFavorite,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => onTap(),
      child: Container(
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
      ),
    );
  }
}

/// List of songs, or a message when there are none.
class SongList extends StatelessWidget {
  final List<Song> songs;
  final Function(Song) onDelete;
  final Function(Song) onToggleFavorite;
  final Function(Song) onOpen;

  const SongList({
    super.key,
    required this.songs,
    required this.onDelete,
    required this.onToggleFavorite,
    required this.onOpen,
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
            onTap: () => onOpen(song),
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

  void _openSong(Song song) {
    Navigator.pushNamed(context, '/song', arguments: song);
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
                onOpen: (song) => _openSong(song),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

/// Screen with the details of the song it receives.
class SongDetailScreen extends StatelessWidget {
  const SongDetailScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final song = ModalRoute.of(context)!.settings.arguments as Song;
    return Scaffold(
      appBar: AppBar(title: Text(song.title)),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            children: [
              Container(
                width: 220,
                height: 220,
                clipBehavior: Clip.antiAlias,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(24),
                ),
                child: Image.network(song.imageUrl, fit: BoxFit.cover),
              ),
              const SizedBox(height: 24),
              Text(
                song.title,
                style: const TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                song.artist,
                style: const TextStyle(fontSize: 16, color: Colors.black54),
              ),
              const SizedBox(height: 8),
              if (song.isFavorite)
                const Text(
                  'Está en tus favoritas',
                  style: TextStyle(color: Colors.pink),
                ),
              const SizedBox(height: 24),
              FilledButton(
                onPressed: () => Navigator.pop(context),
                child: const Text('Volver a la lista'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```
