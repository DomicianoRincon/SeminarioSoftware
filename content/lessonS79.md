# Map<String, dynamic>: la fila como JSON

<!-- tags: Map<String, dynamic>, JSON, row['name'], llave y valor, List<Map<String, dynamic>>, fromMap, as String, dynamic, type 'Null' is not a subtype of type 'String', snake_case en las llaves -->

Supabase no devuelve objetos `Track`. Devuelve cada fila como **JSON**, y en Dart un JSON se guarda en un **`Map<String, dynamic>`**: un conjunto de pares *llave: valor*.

## Una fila, tres formas de verla

```svg
<svg id="mpFila" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 430" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="mpFila-ttl mpFila-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="mpFila-ttl">Una fila, tres formas de verla</title>
  <desc id="mpFila-dsc">Tres columnas unidas por flechas. A la izquierda, una fila de la tabla tracks con id, name, artist_name e image_url. En el centro, la misma fila como JSON, con cada columna como llave entre comillas. A la derecha, el Map en Dart y tres lecturas con corchetes: row de name da Yellow, row de artist_name da Coldplay y row de year da null porque esa llave no existe.</desc>
  <defs>
    <style>
      #mpFila .title{fill:#161A26;font-size:22px;font-weight:700}
      #mpFila .sub{fill:#79809A;font-size:13.5px}
      #mpFila .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #mpFila .nt{font-size:15px;font-weight:700;fill:#161A26}
      #mpFila .nb{fill:#454C61;font-size:13px}
      #mpFila .lbl{fill:#556074;font-size:12px;font-weight:600}
      #mpFila .foot{fill:#79809A;font-size:12px}
      #mpFila .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #mpFila .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#mpFila-arrow)}
    </style>
    <marker id="mpFila-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="430" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Una fila, tres formas de verla</text>
  <text class="sub" x="48" y="80" data-fit="860">La misma fila de tracks: en la tabla, como JSON y como Map en Dart.</text>
<text x="48" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="97">EN LA TABLA</text><text x="336" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="84">COMO JSON</text><text x="624" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">EN DART</text><rect x="48" y="144" width="240" height="196" rx="12" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><rect x="48" y="144" width="240" height="36" rx="12" fill="#F4EBFF"/><text x="64" y="168" font-size="13.5" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="72">tracks</text><text x="64" y="206" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="110">id</text><text x="170" y="206" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="120">'a1f…'</text><text x="64" y="240" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="110">name</text><text x="170" y="240" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="120">'Yellow'</text><text x="64" y="274" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="110">artist_name</text><text x="170" y="274" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="120">'Coldplay'</text><text x="64" y="308" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="110">image_url</text><text x="170" y="308" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" class="mono" data-fit="120">'picsum…'</text><path class="link" d="M288,242 H334"/><rect x="336" y="144" width="240" height="196" rx="12" fill="#1F2430"/><text x="352" y="176" font-size="12.5" font-weight="400" fill="#E6E9F0" text-anchor="start" class="mono" data-fit="216">{</text><text x="352" y="202" font-size="12.5" font-weight="400" fill="#E6E9F0" text-anchor="start" class="mono" data-fit="216">  "id": "a1f…",</text><text x="352" y="228" font-size="12.5" font-weight="400" fill="#E6E9F0" text-anchor="start" class="mono" data-fit="216">  "name": "Yellow",</text><text x="352" y="254" font-size="12.5" font-weight="400" fill="#E6E9F0" text-anchor="start" class="mono" data-fit="216">  "artist_name": "Coldplay",</text><text x="352" y="280" font-size="12.5" font-weight="400" fill="#E6E9F0" text-anchor="start" class="mono" data-fit="216">  "image_url": "picsum…"</text><text x="352" y="306" font-size="12.5" font-weight="400" fill="#E6E9F0" text-anchor="start" class="mono" data-fit="216">}</text><path class="link" d="M576,242 H622"/><g><rect x="624" y="144" width="288" height="196" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="640" y="176" font-size="13" font-weight="700" fill="#0F8478" text-anchor="start" class="mono" data-fit="264">Map&lt;String, dynamic&gt;</text></g><text x="640" y="214" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">row['name']</text><rect x="812.2" y="198" width="79.6" height="24" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="852" y="214.5" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle" class="mono" data-fit="81">'Yellow'</text><text x="640" y="252" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">row['artist_name']</text><rect x="805.0" y="236" width="94.0" height="24" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="852" y="252.5" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle" class="mono" data-fit="96">'Coldplay'</text><text x="640" y="290" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="150">row['year']</text><rect x="826.6" y="274" width="50.8" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="852" y="290.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" class="mono" data-fit="52">null</text><g><rect x="48" y="364" width="864" height="40" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/></g><text x="64" y="389" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="830">La llave es el nombre de la columna, tal cual: artist_name, no artistName. Una llave que no existe da null.</text></svg>
```

- **`String`**: las llaves son textos, los nombres de las columnas.
- **`dynamic`**: los valores pueden ser de cualquier tipo: texto, número, `bool`, `null`.

## Escribir un Map

```dart
final Map<String, dynamic> row = {
  'id': 'a1f3',
  'name': 'Yellow',
  'artist_name': 'Coldplay',
  'image_url': 'https://picsum.photos/400',
};
```

Entre llaves `{}`, cada par es `llave: valor`, separados por comas.

## Leer con []

Para sacar un valor se escribe la llave entre corchetes:

```dart
print(row['name']);
print(row['artist_name']);
print(row['year']);
```

```text
Yellow
Coldplay
null
```

- La llave se escribe **igual que la columna**: `row['artist_name']`, no `row['artistName']`.
- Una llave que no existe no falla: da `null`.

## Darle el tipo con as

`row['name']` es `dynamic`: Dart no sabe que es un texto. Para guardarlo en una variable `String` se dice con `as`:

```dart
final String name = row['name'] as String;
```

Si la llave no existe, el valor es `null` y el `as String` falla con `type 'Null' is not a subtype of type 'String'`. Casi siempre es una llave mal escrita.

## Una lista de filas

Un `select()` devuelve **todas** las filas: una `List<Map<String, dynamic>>`. Cada elemento es un Map como el de arriba:

```dart
final List<Map<String, dynamic>> rows = [
  {'id': 'a1f3', 'name': 'Yellow', 'artist_name': 'Coldplay'},
  {'id': 'b2c4', 'name': 'Clocks', 'artist_name': 'Coldplay'},
];

print(rows[1]['name']);
```

```text
Clocks
```

`rows[1]` es la segunda fila y `['name']` saca su nombre.

## De Map a Track

`fromMap` hace esas lecturas una sola vez y arma el objeto. Así el resto de la app usa `track.name` y no vuelve a escribir llaves:

```dart
factory Track.fromMap(Map<String, dynamic> map) {
  return Track(
    id: map['id'] as String,
    name: map['name'] as String,
    artistName: map['artist_name'] as String,
    imageUrl: map['image_url'] as String? ?? Track.defaultImageUrl,
  );
}
```

`image_url` puede venir `null`. `as String?` acepta el `null` y `??` pone la imagen por defecto en su lugar. Con `as String` a secas, una fila sin imagen fallaría con `type 'Null' is not a subtype of type 'String'`.

`toMap` hace lo contrario: arma el Map con las llaves de las columnas para mandarlo a Supabase. Los dos ya vienen en el repositorio de arranque.

## Ejemplo completo

Una lista de Maps, como la que devuelve Supabase, mostrada leyendo cada valor con `[]`. En el proyecto cada clase va en su archivo.

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

/// Screen that shows rows read from a list of maps.
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  final List<Map<String, dynamic>> rows = const [
    {'id': 'a1f3', 'name': 'Yellow', 'artist_name': 'Coldplay'},
    {'id': 'b2c4', 'name': 'Clocks', 'artist_name': 'Coldplay'},
    {'id': 'c3d5', 'name': 'Bohemian Rhapsody', 'artist_name': 'Queen'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Filas como Map')),
      body: ListView(
        children: rows
            .map(
              (row) => ListTile(
                title: Text(row['name'] as String),
                subtitle: Text(row['artist_name'] as String),
                trailing: Text('id: ${row['id']}'),
              ),
            )
            .toList(),
      ),
    );
  }
}
```
