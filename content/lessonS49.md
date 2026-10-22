# Prop drilling

<!-- tags: prop drilling, pasar parámetros por varios niveles, callback que atraviesa widgets, parámetro que no se usa, demasiados callbacks, constructor muy largo, SongList solo pasa onDelete, cuándo duele pasar datos, InheritedWidget, Provider -->

Mira el constructor de `SongList` después de la favorita:

```dart
final List<Song> songs;
final Function(Song) onDelete;
final Function(Song) onToggleFavorite;
```

`songs` lo usa: con eso decide si muestra tarjetas o el aviso. Pero `onDelete` y `onToggleFavorite` **no los usa para nada**. Los recibe de la Screen solo para entregárselos a cada `SongCard`. Pasar algo por un widget que no lo necesita, solo porque un hijo suyo sí, se llama **prop drilling**: el dato "perfora" los niveles del medio.

```svg
<svg id="pdNiveles" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 640" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="pdNiveles-ttl pdNiveles-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="pdNiveles-ttl">Prop drilling: pasar algo que no se usa</title>
  <desc id="pdNiveles-dsc">Dos columnas. A la izquierda, la playlist: PlaylistScreen, SongList con songs en azul y onDelete en gris porque solo lo pasa, y SongCard, que sí usa onDelete. A la derecha, una app más grande: la Screen, una Page, una sección y una lista que reciben onDelete en gris sin usarlo, hasta la tarjeta que lo usa. Debajo, tres señales de que el drilling empieza a doler.</desc>
  <defs>
    <style>
      #pdNiveles .title{fill:#161A26;font-size:22px;font-weight:700}
      #pdNiveles .sub{fill:#79809A;font-size:13.5px}
      #pdNiveles .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #pdNiveles .nt{font-size:15px;font-weight:700;fill:#161A26}
      #pdNiveles .nb{fill:#454C61;font-size:13px}
      #pdNiveles .lbl{fill:#556074;font-size:12px;font-weight:600}
      #pdNiveles .foot{fill:#79809A;font-size:12px}
      #pdNiveles .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #pdNiveles .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#pdNiveles-arrow)}
    </style>
    <marker id="pdNiveles-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="pdNiveles-down" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="pdNiveles-up" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="pdNiveles-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#9AA1B2"/></marker>
  </defs>
  <rect width="960" height="640" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Prop drilling: pasar algo que no se usa</text>
  <text class="sub" x="48" y="80" data-fit="860">Un widget recibe un parámetro solo para entregárselo a su hijo. Un nivel se tolera; varios duelen.</text>
  <rect x="48" y="112" width="420" height="344" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><path d="M48,126 A14,14 0 0 1 62,112 H454 A14,14 0 0 1 468,126 V152 H48 Z" fill="#E8F6E3"/><text x="66" y="138" font-size="14" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="384">La playlist: un nivel, se tolera</text><rect x="66" y="172" width="384" height="44" rx="10" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="80" y="199" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">PlaylistScreen</text><path d="M88,216 V261" stroke="#C4CBD8" stroke-width="1.5"/><rect x="66" y="261" width="384" height="44" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><text x="80" y="288" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">SongList</text><rect x="224" y="272" width="55" height="22" rx="11" fill="#E6F0FF" stroke="#7FA6E8"/><text x="251.5" y="287.5" font-size="12" font-weight="600" fill="#1F4FA8" text-anchor="middle" class="mono">songs</text><rect x="285" y="272" width="77" height="22" rx="11" fill="#F1F2F5" stroke="#B8BDC9" stroke-dasharray="4 3"/><text x="323.5" y="287.5" font-size="12" font-weight="600" fill="#79809A" text-anchor="middle" class="mono">onDelete</text><path d="M88,305 V350" stroke="#C4CBD8" stroke-width="1.5"/><rect x="66" y="350" width="384" height="44" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><text x="80" y="377" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">SongCard</text><rect x="224" y="361" width="48" height="22" rx="11" fill="#E6F0FF" stroke="#7FA6E8"/><text x="248.0" y="376.5" font-size="12" font-weight="600" fill="#1F4FA8" text-anchor="middle" class="mono">song</text><rect x="278" y="361" width="77" height="22" rx="11" fill="#FFF3DC" stroke="#E2B25C"/><text x="316.5" y="376.5" font-size="12" font-weight="600" fill="#8A5600" text-anchor="middle" class="mono">onDelete</text>
  <rect x="492" y="112" width="420" height="344" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><path d="M492,126 A14,14 0 0 1 506,112 H898 A14,14 0 0 1 912,126 V152 H492 Z" fill="#FFEBEF"/><text x="510" y="138" font-size="14" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="384">Una app más grande: cuatro niveles</text><rect x="510" y="172" width="384" height="44" rx="10" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="524" y="199" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">HomeScreen</text><path d="M532,216 V225" stroke="#C4CBD8" stroke-width="1.5"/><rect x="510" y="225" width="384" height="44" rx="10" fill="#F6F7F9" stroke="#D9DEE8" stroke-width="1.5"/><text x="524" y="252" font-size="13.5" font-weight="700" fill="#79809A" text-anchor="start" class="mono" data-fit="150">LibraryPage</text><rect x="668" y="236" width="77" height="22" rx="11" fill="#F1F2F5" stroke="#B8BDC9" stroke-dasharray="4 3"/><text x="706.5" y="251.5" font-size="12" font-weight="600" fill="#79809A" text-anchor="middle" class="mono">onDelete</text><path d="M532,269 V278" stroke="#C4CBD8" stroke-width="1.5"/><rect x="510" y="278" width="384" height="44" rx="10" fill="#F6F7F9" stroke="#D9DEE8" stroke-width="1.5"/><text x="524" y="305" font-size="13.5" font-weight="700" fill="#79809A" text-anchor="start" class="mono" data-fit="150">RecentSection</text><rect x="668" y="289" width="77" height="22" rx="11" fill="#F1F2F5" stroke="#B8BDC9" stroke-dasharray="4 3"/><text x="706.5" y="304.5" font-size="12" font-weight="600" fill="#79809A" text-anchor="middle" class="mono">onDelete</text><path d="M532,322 V331" stroke="#C4CBD8" stroke-width="1.5"/><rect x="510" y="331" width="384" height="44" rx="10" fill="#F6F7F9" stroke="#D9DEE8" stroke-width="1.5"/><text x="524" y="358" font-size="13.5" font-weight="700" fill="#79809A" text-anchor="start" class="mono" data-fit="150">SongList</text><rect x="668" y="342" width="77" height="22" rx="11" fill="#F1F2F5" stroke="#B8BDC9" stroke-dasharray="4 3"/><text x="706.5" y="357.5" font-size="12" font-weight="600" fill="#79809A" text-anchor="middle" class="mono">onDelete</text><path d="M532,375 V384" stroke="#C4CBD8" stroke-width="1.5"/><rect x="510" y="384" width="384" height="44" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><text x="524" y="411" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">SongCard</text><rect x="668" y="395" width="77" height="22" rx="11" fill="#FFF3DC" stroke="#E2B25C"/><text x="706.5" y="410.5" font-size="12" font-weight="600" fill="#8A5600" text-anchor="middle" class="mono">onDelete</text>
  <rect x="48" y="480" width="272" height="104" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><circle cx="76" cy="506" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="76" y="510.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">1</text><text x="98" y="511" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="210">Recibe lo que no usa</text><text x="64" y="538" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Un widget tiene en su</text><text x="64" y="557" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">constructor algo que solo pasa.</text>
  <rect x="344" y="480" width="272" height="104" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><circle cx="372" cy="506" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="372" y="510.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">2</text><text x="394" y="511" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="210">Un cambio, tres archivos</text><text x="360" y="538" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Agregar un evento obliga a</text><text x="360" y="557" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">tocar tres archivos o más.</text>
  <rect x="640" y="480" width="272" height="104" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><circle cx="668" cy="506" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="668" y="510.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">3</text><text x="690" y="511" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="210">Cinco callbacks o más</text><text x="656" y="538" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">El constructor ya no se lee</text><text x="656" y="557" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">de un vistazo.</text>
  <text x="48" y="616" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="864">En este curso el drilling corto es lo correcto: es explícito y se sigue con los ojos.</text>
</svg>
```

## Hasta dónde se tolera

En la playlist hay **un** intermediario, `SongList`, y además usa parte de lo que recibe. Eso está bien, y en este curso es lo correcto. Tiene una ventaja que no se ve hasta que falta: es **explícito**. Si quieres saber de dónde sale el `onDelete` de una tarjeta, subes por los constructores y llegas a la Screen. No hay nada escondido.

El problema aparece cuando la app crece. Imagina que la lista ya no está en la Screen, sino dentro de una Page, dentro de una sección. Ahora `onDelete` atraviesa tres widgets que no lo usan, y cada uno tiene que declararlo, recibirlo y pasarlo.

## Las señales de que empieza a doler

1. **Un widget recibe lo que no usa.** Si en el constructor hay parámetros que el `build()` solo reenvía, es drilling. Uno se tolera. Si la mayoría del constructor es eso, el widget es un tubo.
2. **Un cambio, tres archivos.** Agregar un evento nuevo obliga a tocar la Screen, cada intermediario y el componente final. Si sumar un botón te hace editar tres archivos o más, el drilling ya cuesta.
3. **Cinco callbacks o más.** Un constructor con cinco funciones ya no se lee de un vistazo, y es fácil pasarlas cruzadas: `onDelete` donde iba `onToggleFavorite`. El tipo no te salva, porque las dos son `Function(Song)`.

## Haz la cuenta

Cuenta los archivos que tocaste para la favorita de la lección anterior: el modelo (`song.dart`), la tarjeta (`song_card.dart`), la lista (`song_list.dart`) y la Screen (`playlist_screen.dart`). Cuatro archivos para un corazón. En `SongList` el cambio fue **solo** de paso: un campo, un parámetro del constructor y una línea en el `for`.

No es grave. Pero ya cumple la señal 2, y el taller va a sumar otro evento por el mismo camino.

## Las salidas, para después

Cuando el drilling duele de verdad, Flutter tiene formas de que un widget lea algo de un ancestro **sin** que los del medio lo pasen: `InheritedWidget`, que viene en Flutter, y paquetes como `Provider` o Bloc que se apoyan en él. Funcionan, pero esconden de dónde sale cada dato, y ese precio solo vale la pena con apps grandes. En este curso el estado se maneja solo con `setState` y se pasa por el constructor. Lo importante es que sepas reconocer el momento en que esto deja de alcanzar.

## Ejemplo completo

Es el mismo programa de *Modelos con copyWith*. Cuenta en él los parámetros que `SongList` recibe y solo reenvía.

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
