# Taller · Tracks en Supabase

<!-- tags: supabase_flutter, flutter pub add, Supabase.initialize, publishableKey, WidgetsFlutterBinding.ensureInitialized, from('tracks').select(), insert().select().single(), delete().eq, You must initialize the supabase instance, permission denied for table tracks, Invalid API key -->

La app del [repositorio de arranque](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0077) guarda los tracks en memoria. Al terminar, los guardará en la tabla `tracks` que creaste en [Migraciones con el CLI de Supabase](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0075).

```svg
<svg id="tlPiezas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 410" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tlPiezas-ttl tlPiezas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tlPiezas-ttl">Quién habla con quién</title>
  <desc id="tlPiezas-dsc">Arriba, main.dart llama a Supabase.initialize con la URL y la publishable key escritas ahí mismo. Abajo, tres cajas en fila: HomeScreen con _tracks y setState, TrackService con getTracks, createTrack y deleteTrack, y la tabla tracks en Supabase. Las flechas de ida llevan la llamada y las de vuelta un Future.</desc>
  <defs>
    <style>
      #tlPiezas .title{fill:#161A26;font-size:22px;font-weight:700}
      #tlPiezas .sub{fill:#79809A;font-size:13.5px}
      #tlPiezas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tlPiezas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tlPiezas .nb{fill:#454C61;font-size:13px}
      #tlPiezas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tlPiezas .foot{fill:#79809A;font-size:12px}
      #tlPiezas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tlPiezas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tlPiezas-arrow)}
    </style>
    <marker id="tlPiezas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="410" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Quién habla con quién</text>
  <text class="sub" x="48" y="80" data-fit="860">La pantalla pide, el servicio habla con Supabase, la tabla guarda.</text>
<g><rect x="48" y="116" width="864" height="72" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="64" y="148" font-size="13.5" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="840">main.dart</text><text x="64" y="174" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="840">Supabase.initialize con la Project URL y la publishable key, antes de runApp.</text></g><g><rect x="48" y="232" width="232" height="128" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="64" y="264" font-size="14" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="208">HomeScreen</text><text x="64" y="290" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">Dueña de _tracks.</text><text x="64" y="309" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">Llama al servicio con</text><text x="64" y="328" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">await y luego setState.</text></g><g><rect x="364" y="232" width="232" height="128" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="380" y="264" font-size="14" font-weight="700" fill="#0F8478" text-anchor="start" class="mono" data-fit="208">TrackService</text><text x="380" y="290" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">getTracks()</text><text x="380" y="309" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">createTrack(track)</text><text x="380" y="328" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">deleteTrack(id)</text></g><g><rect x="680" y="232" width="232" height="128" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="696" y="264" font-size="14" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="208">tabla tracks</text><text x="696" y="290" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">id · name</text><text x="696" y="309" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">artist_name</text><text x="696" y="328" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">image_url</text></g><path class="link" d="M280,276 H362"/><path class="link" d="M596,276 H678"/><path class="link" d="M678,320 H598" stroke-dasharray="5 5"/><path class="link" d="M362,320 H282" stroke-dasharray="5 5"/><rect x="290.8" y="286" width="62.3" height="24" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.2"/><text x="322" y="302.5" font-size="12" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="64">Future</text><rect x="606.8" y="286" width="62.3" height="24" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.2"/><text x="638" y="302.5" font-size="12" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="64">Future</text><text x="48" y="382" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Línea continua: la llamada. Punteada: la respuesta, que llega después.</text></svg>
```

## 1. Instalar supabase_flutter

```svg
<svg id="tlConsola" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 512" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tlConsola-ttl tlConsola-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tlConsola-ttl">Instalar supabase_flutter</title>
  <desc id="tlConsola-dsc">En la carpeta 262SeminarioSesion12, flutter pub add supabase_flutter termina con Changed dependencies. Después flutter run -d chrome lanza la app en Chrome. Un recuadro señala el paquete y otro el resultado.</desc>
  <defs>
    <style>
      #tlConsola .title{fill:#161A26;font-size:22px;font-weight:700}
      #tlConsola .sub{fill:#79809A;font-size:13.5px}
      #tlConsola .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tlConsola .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #tlConsola .pf{fill:#7F8AA3} #tlConsola .cmd{fill:#FFFFFF;font-weight:600}
      #tlConsola .dim{fill:#8A93A6} #tlConsola .okk{fill:#6BCB77;font-weight:600}
      #tlConsola .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #tlConsola .chipc{fill:#F2C069} #tlConsola .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #tlConsola .ct{fill:#161A26;font-size:14px;font-weight:700}
      #tlConsola .cb{fill:#454C61;font-size:13px}
      #tlConsola .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="512" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Instalar supabase_flutter</text>
  <text class="sub" x="48" y="80" data-fit="860">Se instala una sola vez, desde la carpeta del proyecto.</text>
  <rect x="48" y="112" width="864" height="242" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\262SeminarioSesion12</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">262SeminarioSesion12&gt; </tspan><tspan class="cmd">flutter pub add supabase_flutter</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="200" data-fit="816">Resolving dependencies...</text>
  <text class="tl mono" font-size="13" x="72" y="226" data-fit="816">+ supabase_flutter 2.x.x</text>
  <text class="tl mono okk" font-size="13" x="72" y="252" data-fit="816">Changed xx dependencies!</text>
  <text class="tl mono" font-size="13" x="72" y="304" data-fit="816"><tspan class="pf">262SeminarioSesion12&gt; </tspan><tspan class="cmd">flutter run -d chrome</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="330" data-fit="816">Launching lib/main.dart on Chrome in debug mode...</text>
  <rect class="ring" x="364.4" y="158" width="132.8" height="22" rx="5"/>
  <circle class="chipc" cx="497.2" cy="159" r="8"/>
  <text class="chipt" x="497.2" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="68.0" y="236" width="195.2" height="22" rx="5"/>
  <circle class="chipc" cx="263.2" cy="237" r="8"/>
  <text class="chipt" x="263.2" y="237" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <g transform="translate(48.0,378)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">supabase_flutter</text>
    <text class="cb" x="16" y="60" data-fit="392">El SDK de Supabase para Flutter.</text>
  </g>
  <g transform="translate(488.0,378)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Changed dependencies</text>
    <text class="cb" x="16" y="60" data-fit="392">Quedó en pubspec.yaml, en</text>
    <text class="cb" x="16" y="79" data-fit="392">dependencies.</text>
  </g>
</svg>
```

```shell
flutter pub add supabase_flutter
```

El comando agrega el paquete a `pubspec.yaml` y lo descarga.

## 2. Inicializar Supabase en main

Copia la `Project URL` y la **publishable key** (`sb_publishable_...`) de tu proyecto, como en [Primeros pasos con Supabase](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0080), y pégalas en `lib/main.dart`. `main` pasa a ser `async` e inicializa Supabase antes de `runApp`:

```dart
import 'package:supabase_flutter/supabase_flutter.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Supabase.initialize(
    url: 'https://abcdefghijklmnopqrst.supabase.co',
    publishableKey: 'sb_publishable_...',
  );
  runApp(const App());
}
```

- `WidgetsFlutterBinding.ensureInitialized()` prepara Flutter para poder esperar algo antes de `runApp`.
- `await Supabase.initialize(...)` conecta la app con tu proyecto. Desde ahí, `Supabase.instance.client` sirve en cualquier parte.
- La publishable key puede ir en el código. La secret key (`sb_secret_...`) **nunca**.

Corre la app con `flutter run -d chrome`: debe abrir igual que antes.

## 3. Completar TrackService

Abre `lib/services/track_services.dart`. Ya trae los tres métodos del CRUD, pero vacíos: no hablan con Supabase.

```dart
class TrackService {
  Future<List<Track>> getTracks() async {
    return [];
  }

  Future<Track> createTrack(Track track) async {
    return track;
  }

  Future<void> deleteTrack(String id) async {}
}
```

Estos son los bloques que faltan, **en desorden**. Cópialos y decide dónde va cada uno: arriba del archivo, dentro de la clase o dentro de cuál método. Lo que un método tenía antes se reemplaza.

```dart
await _client.from('tracks').delete().eq('id', id);
```

```dart
final SupabaseClient _client = Supabase.instance.client;
```

```dart
final rows = await _client.from('tracks').select();
return rows.map(Track.fromMap).toList();
```

```dart
import 'package:supabase_flutter/supabase_flutter.dart';
```

```dart
final row = await _client
    .from('tracks')
    .insert(track.toMap())
    .select()
    .single();
return Track.fromMap(row);
```

Pistas: lee qué devuelve cada bloque y compáralo con el tipo de cada método. Y mira qué variables usa: `id` y `track` solo existen dentro del método que las recibe.

## 4. Invocar el servicio

La app ya muestra y elimina tracks, pero en memoria. Crear todavía no hace nada: el track del formulario llega a la pantalla y no se agrega a la lista. Este es el bloque que lo agrega:

```dart
setState(() {
  _tracks = [..._tracks, track];
});
```

Ahora la app debe trabajar con `TrackService`:

- Al abrir la app, la lista sale de la tabla `tracks`.
- Al crear un track, se guarda en la tabla y la lista muestra el que devolvió el servicio, con su `id` real.
- Al eliminar un track, se borra de la tabla y desaparece de la lista.

No te decimos dónde va cada llamada: lee el código de `lib/screens/` y encuentra dónde la app maneja hoy la lista, dónde agrega y dónde quita. Recuerda lo de [Future: pedir y esperar](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0076): los métodos devuelven un `Future`, así que se esperan con `await`, y el resultado va al estado con `setState`.

## 5. Comprobar

- Los dos tracks que agregaste en el `Table Editor` aparecen al abrir la app.
- Crea un track, recarga la página y sigue ahí. En el detalle, su `id` es un `uuid`.
- La fila nueva aparece en `Table Editor > tracks` (pulsa *Refresh*).
- Elimina un track desde el detalle: desaparece de la app y de la tabla.

## Metas

- [ ] `supabase_flutter` instalado
- [ ] `Supabase.initialize` en `main.dart` con la URL y la publishable key
- [ ] Cada bloque en su lugar dentro de `TrackService`
- [ ] Al abrir la app, la lista sale de Supabase
- [ ] Crear guarda la fila y la muestra con su `id` real
- [ ] Eliminar borra la fila de la tabla

## Si te sobra tiempo

- **Cargando**: un `bool _isLoading` que muestre un `CircularProgressIndicator` mientras espera `getTracks()`.
- **Error**: envuelve el `await` en `try` / `catch` y muestra el mensaje con un `SnackBar`. Para probarlo, apaga el wifi.
- **Editar**: un método `updateTrack(Track track)` con `update(track.toMap()).eq('id', track.id)`.

## Si algo falla

- `You must initialize the supabase instance before calling Supabase.instance`: falta el `await Supabase.initialize(...)` en `main`, o va después de `runApp`.
- `Invalid API key`: la llave de `main.dart` no es la publishable key de este proyecto, o se copió incompleta.
- `permission denied for table tracks`: a la migración le falta el `grant`.
- `Could not find the table 'public.tracks'`: la migración `create_tracks` no se subió. Corre `npx supabase db push --remote` en el proyecto de tu equipo.
