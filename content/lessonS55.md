# Devolver un resultado al cerrar

<!-- tags: Navigator.pop(context, result), await Navigator.pushNamed, Future, async, result is Song, devolver datos a la pantalla anterior, el resultado llega null, formulario en otra pantalla, FloatingActionButton -->

El formulario ocupa media playlist. Se va a mudar a su propia pantalla, `AddSongScreen`, que se abre con un botón *+* y se cierra al guardar. Pero la lista vive en `PlaylistScreen`, así que la canción nueva tiene que volver.

Toca *+*, escribe una canción y guárdala. Después prueba volver con atrás sin guardar:

```interactive
nav-result
```

## AddSongScreen hospeda el formulario

```dart
class AddSongScreen extends StatelessWidget {
  const AddSongScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Nueva canción')),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: SongForm(onAdd: (song) => Navigator.pop(context, song)),
        ),
      ),
    );
  }
}
```

`SongForm` no cambia: sigue armando la `Song` y avisando con `onAdd`. Lo que cambia es quién la recibe. Antes, la playlist la agregaba a la lista. Ahora, `AddSongScreen` se cierra con ella: `Navigator.pop` acepta un segundo parámetro, el resultado que se le entrega a quien abrió la pantalla.

## La playlist espera la respuesta

```svg
<svg id="reAwait" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 546" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="reAwait-ttl reAwait-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="reAwait-ttl">Abrir una pantalla y esperar su respuesta</title>
  <desc id="reAwait-dsc">El código de _openAddSong, una función async: final result igual a await Navigator.pushNamed con context y barra add-song; si result is Song, llama a _addSong con result. Tres tarjetas a la derecha: await deja la función en pausa hasta el pop; result es lo que mandó pop o null si se volvió con atrás; y _addSong es el setState de siempre. Debajo, dos tarjetas: Navigator.pop con context y song, que cierra y entrega la canción, y Navigator.pop solo con context, el del botón atrás, que entrega null.</desc>
  <defs>
    <style>
      #reAwait .title{fill:#161A26;font-size:22px;font-weight:700}
      #reAwait .sub{fill:#79809A;font-size:13.5px}
      #reAwait .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #reAwait .cl{font-size:13px;fill:#C9CFDA}
      #reAwait .s{fill:#A8D8A0} #reAwait .n{fill:#F2B880} #reAwait .c{fill:#7FD1E8}
      #reAwait .p{fill:#D5B8F5} #reAwait .k{fill:#F08FB0}
      #reAwait .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #reAwait .ct{fill:#161A26;font-size:14px;font-weight:700}
      #reAwait .cb{fill:#454C61;font-size:13px}
      #reAwait .rt{fill:#161A26;font-size:14px} #reAwait .rs{fill:#79809A;font-size:12px}
      #reAwait .foot{fill:#79809A;font-size:12px}
      #reAwait .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #reAwait .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #reAwait .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#reAwait-ar-green)}
      #reAwait .hl-rose{fill:#F3A3B2;fill-opacity:.16;stroke:#F3A3B2;stroke-width:1.5}
      #reAwait .ld-rose{fill:none;stroke:#F3A3B2;stroke-width:1.5;stroke-dasharray:3 4}
      #reAwait .ar-rose{fill:none;stroke:#C2354F;stroke-width:1.75;marker-end:url(#reAwait-ar-rose)}
      #reAwait .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #reAwait .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #reAwait .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#reAwait-ar-violet)}
    </style>
    <marker id="reAwait-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="reAwait-ar-rose" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/></marker>
    <marker id="reAwait-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="546" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Abrir una pantalla y esperar su respuesta</text>
  <text class="sub" x="48" y="80" data-fit="860">pushNamed devuelve un Future. Lo que se mande en el pop llega en result.</text>
  <rect x="48" y="112" width="456" height="276" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/playlist_screen.dart</text>
  <rect x="552" y="112" width="360" height="276" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">QUÉ PASA EN CADA LÍNEA</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-violet" x="196.6" y="180" width="47.0" height="22" rx="5"/>
  <rect class="hl-rose" x="110.8" y="276" width="117.2" height="22" rx="5"/>
  <rect class="hl-green" x="95.2" y="300" width="132.8" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="273.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Future</tspan>&lt;<tspan class="k">void</tspan>&gt; _openAddSong() async {</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="319.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">final</tspan> result = await <tspan class="c">Navigator</tspan>.pushNamed(</text>
  <text class="cl mono" font-size="13" x="99.2" y="220" textLength="62.4" lengthAdjust="spacingAndGlyphs" data-fit="432">context,</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="93.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">'/add-song'</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="268" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">);</text>
  <text class="cl mono" font-size="13" x="83.6" y="292" textLength="163.8" lengthAdjust="spacingAndGlyphs" data-fit="432">if (result is <tspan class="c">Song</tspan>) {</text>
  <text class="cl mono" font-size="13" x="99.2" y="316" textLength="132.6" lengthAdjust="spacingAndGlyphs" data-fit="432">_addSong(result);</text>
  <text class="cl mono" font-size="13" x="83.6" y="340" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="364" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <g transform="translate(552,144)">
<g transform="translate(16,16)"><rect width="328" height="64" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#7439B8" data-fit="300">await</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">_openAddSong queda en pausa aquí</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">hasta que AddSongScreen haga pop.</text></g><g transform="translate(16,92)"><rect width="328" height="64" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#C2354F" data-fit="300">result is Song</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">result es lo que mandó pop, o null</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">si se volvió con atrás sin guardar.</text></g><g transform="translate(16,168)"><rect width="328" height="64" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#3A8235" data-fit="300">_addSong(result)</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">El setState de siempre. Aquí ya se</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">sabe que result es una Song.</text></g>
  </g>
  <path class="ld-violet" d="M409.4,191 H504"/>
  <path class="ar-violet" d="M504,191 H568 V192"/>
  <path class="ld-rose" d="M253.4,287 H504"/>
  <path class="ar-rose" d="M504,287 H523 V268 H568"/>
  <path class="ld-green" d="M237.8,311 H504"/>
  <path class="ar-green" d="M504,311 H532 V344 H568"/>
  <g transform="translate(48.0,412)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#E8F6E3" stroke="#3A8235" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="366">Navigator.pop(context, song)</text>
    <text class="cb" x="16" y="60" data-fit="392">En AddSongScreen: cierra la pantalla</text>
    <text class="cb" x="16" y="79" data-fit="392">y entrega song como resultado.</text>
  </g>
  <g transform="translate(488.0,412)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#FFEBEF" stroke="#C2354F" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="366">Navigator.pop(context)</text>
    <text class="cb" x="16" y="60" data-fit="392">El atrás del sistema: cierra sin</text>
    <text class="cb" x="16" y="79" data-fit="392">resultado, y result llega null.</text>
  </g>
</svg>
```

```dart
Future<void> _openAddSong() async {
  final result = await Navigator.pushNamed(context, '/add-song');
  if (result is Song) {
    _addSong(result);
  }
}
```

`pushNamed` devuelve un **`Future`**: un valor que todavía no existe y que llegará después. Con `await`, la función se queda en pausa en esa línea mientras la persona llena el formulario, y sigue cuando `AddSongScreen` hace pop. `result` vale lo que se mandó en ese pop. Por usar `await`, la función se marca `async` y devuelve `Future<void>`.

## Si vuelve sin guardar

La flecha del `AppBar` y el atrás del sistema hacen `Navigator.pop(context)`, sin resultado. Entonces `result` llega `null`.

`if (result is Song)` deja pasar solo una canción de verdad. Además le dice a Dart que, dentro del `if`, `result` es una `Song`, y por eso `_addSong(result)` compila.

## El botón +

El formulario sale de la playlist, que ahora solo muestra la lista. El botón va en el `Scaffold`:

```dart
floatingActionButton: FloatingActionButton(
  onPressed: () => _openAddSong(),
  child: const Icon(Icons.add),
),
```

Y la tabla suma la cuarta ruta, `'/add-song': (context) => const AddSongScreen()`.

## Ejemplo completo

La playlist navegable completa: entrar, ver el detalle, agregar desde otra pantalla y cerrar sesión. En el proyecto, cada Screen va en su archivo de `screens/`.

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
        '/add-song': (context) => const AddSongScreen(),
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

  Future<void> _openAddSong() async {
    final result = await Navigator.pushNamed(context, '/add-song');
    if (result is Song) {
      _addSong(result);
    }
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
          child: SongList(
            songs: _songs,
            onDelete: (song) => _deleteSong(song),
            onToggleFavorite: (song) => _toggleFavorite(song),
            onOpen: (song) => _openSong(song),
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => _openAddSong(),
        child: const Icon(Icons.add),
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

/// Screen that hosts the form and returns the new song.
class AddSongScreen extends StatelessWidget {
  const AddSongScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Nueva canción')),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: SongForm(onAdd: (song) => Navigator.pop(context, song)),
        ),
      ),
    );
  }
}
```
