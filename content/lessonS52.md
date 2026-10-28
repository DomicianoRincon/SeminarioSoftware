# Rutas nombradas: pushNamed y pop

<!-- tags: routes, initialRoute, Navigator.pushNamed, Navigator.pop, rutas nombradas, abrir otra pantalla, Could not find a generator for route, flecha atrás del AppBar, LoginScreen -->

Para abrir una pantalla, el `Navigator` necesita saber cuál. En este curso se le dice por su **nombre**: cada Screen se registra una vez en la tabla `routes:` de `MaterialApp`, y desde ahí cualquier botón la abre diciendo ese nombre.

## La tabla de rutas

```svg
<svg id="rnTabla" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 522" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="rnTabla-ttl rnTabla-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="rnTabla-ttl">La tabla routes: de MaterialApp</title>
  <desc id="rnTabla-dsc">El código de MaterialApp con initialRoute igual a barra y la tabla routes con dos entradas: barra construye LoginScreen y barra playlist construye PlaylistScreen. Una flecha de initialRoute a una tarjeta que explica que es la ruta con la que arranca la pila, y una flecha de cada nombre a la Screen que construye. Debajo, dos tarjetas: pushNamed busca el nombre en la tabla y pone esa Screen encima; pop quita la de arriba.</desc>
  <defs>
    <style>
      #rnTabla .title{fill:#161A26;font-size:22px;font-weight:700}
      #rnTabla .sub{fill:#79809A;font-size:13.5px}
      #rnTabla .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #rnTabla .cl{font-size:13px;fill:#C9CFDA}
      #rnTabla .s{fill:#A8D8A0} #rnTabla .n{fill:#F2B880} #rnTabla .c{fill:#7FD1E8}
      #rnTabla .p{fill:#D5B8F5} #rnTabla .k{fill:#F08FB0}
      #rnTabla .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #rnTabla .ct{fill:#161A26;font-size:14px;font-weight:700}
      #rnTabla .cb{fill:#454C61;font-size:13px}
      #rnTabla .rt{fill:#161A26;font-size:14px} #rnTabla .rs{fill:#79809A;font-size:12px}
      #rnTabla .foot{fill:#79809A;font-size:12px}
      #rnTabla .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #rnTabla .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #rnTabla .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#rnTabla-ar-amber)}
      #rnTabla .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #rnTabla .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #rnTabla .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#rnTabla-ar-indigo)}
      #rnTabla .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #rnTabla .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #rnTabla .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#rnTabla-ar-violet)}
    </style>
    <marker id="rnTabla-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="rnTabla-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="rnTabla-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="522" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La tabla <tspan class="mono">routes:</tspan> de <tspan class="mono">MaterialApp</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Cada nombre apunta a una función que construye su Screen. Navegar es decir un nombre.</text>
  <rect x="48" y="112" width="456" height="252" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/main.dart</text>
  <rect x="552" y="112" width="360" height="252" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">QUÉ CONSTRUYE CADA NOMBRE</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="188.8" y="180" width="31.4" height="22" rx="5"/>
  <rect class="hl-violet" x="95.2" y="228" width="31.4" height="22" rx="5"/>
  <rect class="hl-indigo" x="95.2" y="252" width="93.8" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="93.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">MaterialApp</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="140.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">initialRoute</tspan>: <tspan class="s">'/'</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">routes</tspan>: {</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="296.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">'/'</tspan>: (context) =&gt; <tspan class="k">const</tspan> <tspan class="c">LoginScreen</tspan>(),</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="195.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">'/playlist'</tspan>: (context) =&gt;</text>
  <text class="cl mono" font-size="13" x="130.4" y="292" textLength="179.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">const</tspan> <tspan class="c">PlaylistScreen</tspan>(),</text>
  <text class="cl mono" font-size="13" x="83.6" y="316" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">},</text>
  <text class="cl mono" font-size="13" x="68.0" y="340" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<g transform="translate(16,12)"><rect width="328" height="60" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#A96C05" data-fit="300">initialRoute</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">El nombre de la ruta con la que</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">arranca la pila.</text></g><g transform="translate(16,84)"><rect width="328" height="46" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#7439B8" data-fit="300">LoginScreen</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">'/' es la primera que se ve.</text></g><g transform="translate(16,150)"><rect width="328" height="46" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#4453C9" data-fit="300">PlaylistScreen</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">'/playlist' se abre al tocar Entrar.</text></g>
  </g>
  <path class="ld-amber" d="M230.0,191 H504"/>
  <path class="ar-amber" d="M504,191 H514 V190 H568"/>
  <path class="ld-violet" d="M401.6,239 H504"/>
  <path class="ar-violet" d="M504,239 H568"/>
  <path class="ld-indigo" d="M300.2,263 H504"/>
  <path class="ar-indigo" d="M504,263 H532 V317 H568"/>
  <g transform="translate(48.0,388)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#EEF1FF" stroke="#4453C9" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="366">pushNamed(context, '/playlist')</text>
    <text class="cb" x="16" y="60" data-fit="392">Busca el nombre en routes: y pone</text>
    <text class="cb" x="16" y="79" data-fit="392">esa Screen encima de la pila.</text>
  </g>
  <g transform="translate(488.0,388)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#FFF3DC" stroke="#A96C05" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="366">pop(context)</text>
    <text class="cb" x="16" y="60" data-fit="392">Quita la de arriba. La flecha del AppBar</text>
    <text class="cb" x="16" y="79" data-fit="392">y el atrás del sistema hacen lo mismo.</text>
  </g>
</svg>
```

`routes:` es un mapa. La llave es el nombre, un `String` que empieza con `/`. El valor es una función que recibe el `context` y construye la Screen. `initialRoute` dice con qué nombre arranca la pila.

La playlist ya tenía esta tabla desde la sesión 6, con una sola entrada. Ahora llega una pantalla de entrada, `LoginScreen`, y la tabla crece:

```dart
MaterialApp(
  initialRoute: '/',
  routes: {
    '/': (context) => const LoginScreen(),
    '/playlist': (context) => const PlaylistScreen(),
  },
)
```

`'/'` pasa a ser `LoginScreen`, porque es lo primero que se ve, y la playlist se muda a `'/playlist'`. En este curso no se usa `home:`: toda pantalla entra por la tabla, incluida la primera.

## pushNamed abre

`LoginScreen` es una Screen sencilla y sin estado: un ícono, el nombre de la app y un botón. El botón abre la playlist diciendo su nombre:

```dart
FilledButton(
  onPressed: () => Navigator.pushNamed(context, '/playlist'),
  child: const Text('Entrar'),
),
```

`Navigator.pushNamed` recibe el `context`, que le sirve para encontrar el `Navigator` de la app, y el nombre. Busca el nombre en la tabla, construye esa Screen y la pone encima de la pila.

El nombre es un `String`, así que el editor no lo revisa. Si tiene un error de dedo, como `'/playlis'`, la app compila sin quejarse y falla al tocar el botón:

```text
Could not find a generator for route RouteSettings("/playlis", null)
```

Cuando aparezca ese mensaje, compara el nombre del `pushNamed` con el de la tabla.

## pop vuelve

Por ahora, cerrar sesión es solo volver. El botón va en la barra de la playlist, en `actions`:

```dart
appBar: AppBar(
  title: const Text('Mi playlist'),
  actions: [
    IconButton(
      onPressed: () => Navigator.pop(context),
      icon: const Icon(Icons.logout),
    ),
  ],
),
```

`Navigator.pop` quita la ruta de arriba, la playlist, y debajo aparece el login.

Al probarlo, fíjate en la barra de la playlist: apareció sola una flecha `←` a la izquierda. El `AppBar` la pone porque hay algo debajo, y tocarla también vuelve al login. En una app con inicio de sesión eso está mal, porque la persona ya entró. La próxima lección lo arregla.

## Ejemplo completo

La playlist con su pantalla de entrada. En el proyecto, `LoginScreen` va en `screens/login_screen.dart`; aquí todo está en un archivo para que corra en DartPad.

```dart trycode=84cee12d9d3ae54aa3808df07ee55488 tab=run
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
                onPressed: () => Navigator.pushNamed(context, '/playlist'),
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
            onPressed: () => Navigator.pop(context),
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
