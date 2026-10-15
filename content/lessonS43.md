# Creador de playlists: la lista en texto

<!-- tags: lista en el estado, List en setState, formulario con TextField, modelo Song, _songs.add, agregar a una lista, for dentro de children, la lista no se actualiza, varios TextEditingController, limpiar el formulario -->

Ya tienes las piezas: un dato en el estado, `setState` para cambiarlo y un `TextEditingController` para leer un campo. Ahora se juntan en una app pequeña: **un creador de playlists**. Un formulario con el nombre de la canción, el artista y la URL de la portada; al pulsar *Agregar*, la canción entra a la lista. En esta lección la lista se muestra como texto simple. En la siguiente, con un componente.

Pruébala antes de leer el código. Agrega tres o cuatro canciones y mira cómo crece `_songs`:

```interactive
playlist
```

## El modelo: Song

Una canción tiene tres datos. En vez de guardar tres listas separadas, se agrupan en una clase, en `lib/models/song.dart`:

```dart
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
```

Es la misma forma de los componentes de la sesión 2: campos `final` y un constructor con parámetros con nombre. Una `Song` no cambia; lo que cambia es **la lista de canciones**.

## El estado de la pantalla

`PlaylistScreen` es un `StatefulWidget`. Su State guarda la lista y los tres controllers del formulario:

```dart
class _PlaylistScreenState extends State<PlaylistScreen> {
  final List<Song> _songs = [];
  late TextEditingController _titleController;
  late TextEditingController _artistController;
  late TextEditingController _imageUrlController;

  @override
  void initState() {
    super.initState();
    _titleController = TextEditingController();
    _artistController = TextEditingController();
    _imageUrlController = TextEditingController(
      text: 'https://picsum.photos/400',
    );
  }
```

`_songs` es `final` y aun así crece. `final` quiere decir que el campo siempre apunta a **la misma lista**, no que la lista no se pueda modificar. Lo que no se puede es escribir `_songs = otraLista`.

El campo de la imagen arranca con `https://picsum.photos/400` para no tener que escribir una URL cada vez. Y como hay tres controllers, `dispose` libera los tres (está en el ejemplo completo).

## Agregar una canción

El botón llama a `_addSong`, que lee los campos, crea la `Song` y la agrega **dentro de `setState`**:

```dart
void _addSong() {
  final title = _titleController.text;
  final artist = _artistController.text;
  if (title.isEmpty || artist.isEmpty) return;
  setState(() {
    _songs.add(Song(
      title: title,
      artist: artist,
      imageUrl: _imageUrlController.text,
    ));
  });
  _titleController.clear();
  _artistController.clear();
}
```

```dart
FilledButton(
  onPressed: () => _addSong(),
  child: const Text('Agregar'),
),
```

- Si falta el nombre o el artista, la función sale sin hacer nada.
- Los `clear()` van fuera del `setState`: el controller avisa solo a su campo, no hace falta reconstruir la pantalla para eso.
- La URL no se borra, para que la siguiente canción pueda usar la misma.

## Pintar la lista

En el `build`, dentro del `Column`, un `for` crea un `Text` por cada canción:

```dart
const SizedBox(height: 24),
for (final song in _songs)
  Text('${song.title} · ${song.artist}'),
```

Ese `for` se escribe dentro de la lista de `children`, sin llaves. Dart lo expande: con tres canciones es como si hubieras escrito tres `Text` seguidos. Con la lista vacía no escribe ninguno.

Así queda el recorrido completo de un toque:

```svg
<svg id="plFlujo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 424" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="plFlujo-ttl plFlujo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="plFlujo-ttl">Del formulario a la lista</title>
  <desc id="plFlujo-dsc">Cuatro etapas. El formulario con nombre, artista y URL de la imagen y el botón Agregar. La función _addSong, que lee los controllers y dentro de setState agrega una Song a _songs. El estado _songs con tres canciones. Y build, que pinta un Text por cada canción.</desc>
  <defs>
    <style>
      #plFlujo .title{fill:#161A26;font-size:22px;font-weight:700}
      #plFlujo .sub{fill:#79809A;font-size:13.5px}
      #plFlujo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #plFlujo .nt{font-size:15px;font-weight:700;fill:#161A26}
      #plFlujo .nb{fill:#454C61;font-size:13px}
      #plFlujo .lbl{fill:#556074;font-size:12px;font-weight:600}
      #plFlujo .foot{fill:#79809A;font-size:12px}
      #plFlujo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #plFlujo .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#plFlujo-arrow)}
    </style>
    <marker id="plFlujo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="424" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Del formulario a la lista</text>
  <text class="sub" x="48" y="80" data-fit="860">El botón no pinta nada en la lista: agrega al estado, y build() vuelve a pintar todo.</text>
  <rect x="48" y="120" width="196" height="232" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <circle cx="74" cy="148" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="74" y="152.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">1</text>
  <text x="96" y="153" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="136">Formulario</text>
  <path class="link" d="M246,236 H266"/>
  <rect x="268" y="120" width="196" height="232" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <circle cx="294" cy="148" r="13" fill="#FFFFFF" stroke="#7439B8" stroke-width="2"/><text x="294" y="152.5" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle">2</text>
  <text x="316" y="153" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="136">_addSong()</text>
  <path class="link" d="M466,236 H486"/>
  <rect x="488" y="120" width="196" height="232" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <circle cx="514" cy="148" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="514" y="152.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle">3</text>
  <text x="536" y="153" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="136">_songs</text>
  <path class="link" d="M686,236 H706"/>
  <rect x="708" y="120" width="196" height="232" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
  <circle cx="734" cy="148" r="13" fill="#FFFFFF" stroke="#3A8235" stroke-width="2"/><text x="734" y="152.5" font-size="13" font-weight="700" fill="#3A8235" text-anchor="middle">4</text>
  <text x="756" y="153" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="136">build()</text>
  <rect x="64" y="176" width="164" height="26" rx="5" fill="#FFFFFF" stroke="#8D93A5" stroke-width="1.2"/><text x="72" y="193" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" data-fit="148">Levitating</text>
  <rect x="64" y="210" width="164" height="26" rx="5" fill="#FFFFFF" stroke="#8D93A5" stroke-width="1.2"/><text x="72" y="227" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" data-fit="148">Dua Lipa</text>
  <rect x="64" y="244" width="164" height="26" rx="5" fill="#FFFFFF" stroke="#8D93A5" stroke-width="1.2"/><text x="72" y="261" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" data-fit="148">picsum.photos/400</text>
  <rect x="64" y="284" width="164" height="30" rx="15" fill="#6750A4"/>
  <text x="146" y="304" font-size="13" font-weight="600" fill="#FFFFFF" text-anchor="middle">Agregar</text>
  <text x="286.0" y="186" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="160">final title =</text><text x="300.4" y="203" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="160">_titleController.text;</text><text x="286.0" y="220" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="160">...</text><text x="286.0" y="237" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="160">setState(() {</text><text x="300.4" y="254" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="160">_songs.add(Song(</text><text x="314.8" y="271" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="160">title: title,</text><text x="314.8" y="288" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="160">...</text><text x="300.4" y="305" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="160">));</text><text x="286.0" y="322" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="160">});</text>
  <rect x="504" y="178" width="164" height="40" rx="8" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.2"/>
  <text x="514" y="195" font-size="12" font-weight="600" fill="#4453C9" text-anchor="start" class="mono">[0] Song(</text>
  <text x="524" y="211" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="140">'Imagine', …)</text>
  <rect x="504" y="228" width="164" height="40" rx="8" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.2"/>
  <text x="514" y="245" font-size="12" font-weight="600" fill="#4453C9" text-anchor="start" class="mono">[1] Song(</text>
  <text x="524" y="261" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="140">'Yellow', …)</text>
  <rect x="504" y="278" width="164" height="40" rx="8" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.2"/>
  <text x="514" y="295" font-size="12" font-weight="600" fill="#4453C9" text-anchor="start" class="mono">[2] Song(</text>
  <text x="524" y="311" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="140">'Levitating', …)</text>
  <text x="724" y="190" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="168">Imagine · John Lennon</text>
  <text x="724" y="216" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="168">Yellow · Coldplay</text>
  <text x="724" y="242" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="168">Levitating · Dua Lipa</text>
  <text x="724" y="288" font-size="12" font-weight="400" fill="#79809A" text-anchor="start">Un Text por cada</text><text x="724" y="305" font-size="12" font-weight="400" fill="#79809A" text-anchor="start">canción del estado.</text>
  <text x="48" y="388" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="864">Si setState no envuelve el add, la canción entra a _songs pero la lista de la pantalla no cambia.</text>
</svg>
```

El botón nunca toca la lista de la pantalla. Solo agrega un dato al estado. La pantalla se vuelve a pintar entera desde `_songs` cada vez que corre `build()`. Esa es la idea más importante de la sesión: **la interfaz es lo que sale de pintar el estado**.

## Si la lista no cambia

Si escribes `_songs.add(...)` fuera del `setState`, la canción sí entra a la lista, pero la pantalla no se entera: es el mismo error del contador. Lo confuso es que la canción aparece después, cuando cualquier otro `setState` reconstruye la pantalla, porque `build()` pinta todo lo que haya en `_songs`. Parece que la app va "un paso atrasada". Revisa siempre que el cambio esté **dentro** del `setState`.

Cuando la lista crezca, el `Column` se sale de la pantalla y aparece `A RenderFlex overflowed by … pixels on the bottom`. Por eso el cuerpo va dentro de un `SingleChildScrollView`, como en la sesión 3.

## Ejemplo completo

Todo en un archivo: `App`, el modelo `Song` y `PlaylistScreen`. En tu proyecto, `Song` va en `lib/models/song.dart` y la pantalla en `lib/screens/playlist_screen.dart`.

```dart trycode=b0295ce283b4ce1551b4cf1809a4b773
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
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
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

/// Screen that builds a playlist from a form.
class PlaylistScreen extends StatefulWidget {
  const PlaylistScreen({super.key});

  @override
  State<PlaylistScreen> createState() => _PlaylistScreenState();
}

class _PlaylistScreenState extends State<PlaylistScreen> {
  final List<Song> _songs = [];
  late TextEditingController _titleController;
  late TextEditingController _artistController;
  late TextEditingController _imageUrlController;

  @override
  void initState() {
    super.initState();
    _titleController = TextEditingController();
    _artistController = TextEditingController();
    _imageUrlController = TextEditingController(
      text: 'https://picsum.photos/400',
    );
  }

  void _addSong() {
    final title = _titleController.text;
    final artist = _artistController.text;
    if (title.isEmpty || artist.isEmpty) return;
    setState(() {
      _songs.add(Song(
        title: title,
        artist: artist,
        imageUrl: _imageUrlController.text,
      ));
    });
    _titleController.clear();
    _artistController.clear();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Mi playlist'),
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextField(
                controller: _titleController,
                decoration: const InputDecoration(
                  labelText: 'Nombre de la canción',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 12),
              TextField(
                controller: _artistController,
                decoration: const InputDecoration(
                  labelText: 'Artista',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 12),
              TextField(
                controller: _imageUrlController,
                decoration: const InputDecoration(
                  labelText: 'URL de la imagen',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 12),
              FilledButton(
                onPressed: () => _addSong(),
                child: const Text('Agregar'),
              ),
              const SizedBox(height: 24),
              for (final song in _songs)
                Text('${song.title} · ${song.artist}'),
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
