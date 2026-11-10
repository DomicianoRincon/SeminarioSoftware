# Future: pedir y esperar

<!-- tags: Future, await, async, Future<void>, try catch, The await expression can only be used in an async function, A value of type 'Future' can't be assigned, capa de servicio, Future.delayed -->

Cuando la app le pide algo a Supabase, la respuesta tarda: viaja por internet, la base de datos busca y vuelve. Dart no se queda congelado esperando. La llamada devuelve de inmediato un **`Future`**: la promesa de un valor que todavía no llega.

## Pedir y esperar

```interactive
future
```

Pulsa *Reproducir* y cambia las pestañas:

- **Con await**: la función queda en pausa en el `await` y sigue cuando llega el valor. La respuesta llega **una sola vez**.
- **Con error**: el `Future` se completa con un error y el `await` lo lanza como excepción. Lo atrapa el `catch`.

El tipo va entre `<>`: `Future<int>` promete un número, `Future<List<Track>>` una lista de tracks.

## Las tres piezas

```dart
Future<List<Track>> getTracks() async {
  final rows = await _client.from('tracks').select();
  return rows.map(Track.fromMap).toList();
}
```

- **`Future<List<Track>>`**: lo que devuelve la función. Quien la llame recibe la promesa.
- **`async`**: permite usar `await` adentro. Sin él, Dart responde `The await expression can only be used in an async function`.
- **`await`**: espera el valor. Sin él, `rows` sería un `Future` y no la lista. Asignarlo a una lista falla con `A value of type 'Future<…>' can't be assigned to a variable of type '…'`.

## Por las capas: pantalla, servicio y Supabase

En la app, la pantalla no habla con Supabase: le pide al servicio, y el servicio a Supabase. Por eso hay **dos esperas**, una dentro de la otra.

```interactive
future service
```

- **Listar**: `initState` llama a `_loadTracks`. La pantalla espera a `getTracks()`, que espera al `select()`. Cuando todo vuelve, `setState` guarda la lista.
- **Crear**: el borrador sale con `id` vacío y vuelve con el `id` que generó la base de datos. Por eso se agrega a la lista lo que devolvió el servicio.
- **Borrar**: `deleteTrack` devuelve `Future<void>`: no trae ningún valor, solo avisa que ya terminó. Hasta entonces no se quita el track de la lista.

En los tres, `setState` va **después** del `await`. Antes, el dato todavía no existe.

## Ejemplo completo

La app pide los tracks a un servicio de mentira: `Future.delayed` simula los dos segundos que tardaría Supabase. Pulsa *Volver a cargar* y mira el aviso mientras espera. En el proyecto cada clase va en su archivo.

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
      routes: {'/': (context) => const HomeScreen()},
    );
  }
}

/// A track with its name and artist.
class Track {
  final String id;
  final String name;
  final String artistName;

  const Track({
    required this.id,
    required this.name,
    required this.artistName,
  });
}

/// Fake service that takes two seconds to answer, like a database.
class TrackService {
  Future<List<Track>> getTracks() async {
    await Future.delayed(const Duration(seconds: 2));
    return const [
      Track(id: 'a1', name: 'Yellow', artistName: 'Coldplay'),
      Track(id: 'b2', name: 'Clocks', artistName: 'Coldplay'),
    ];
  }
}

/// Screen that loads the tracks when it starts.
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final TrackService _trackService = TrackService();
  List<Track> _tracks = [];
  String _status = '';

  @override
  void initState() {
    super.initState();
    _loadTracks();
  }

  Future<void> _loadTracks() async {
    setState(() {
      _tracks = [];
      _status = 'Esperando al servicio...';
    });
    final tracks = await _trackService.getTracks();
    setState(() {
      _tracks = tracks;
      _status = 'Llegaron ${tracks.length} tracks';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Mis tracks')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(_status),
            const SizedBox(height: 8),
            FilledButton(
              onPressed: () => _loadTracks(),
              child: const Text('Volver a cargar'),
            ),
            Expanded(
              child: ListView(
                children: _tracks
                    .map(
                      (track) => ListTile(
                        title: Text(track.name),
                        subtitle: Text(track.artistName),
                      ),
                    )
                    .toList(),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```
