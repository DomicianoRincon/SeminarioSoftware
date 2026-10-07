# Armar una pantalla

<!-- tags: armar una pantalla con componentes, import package, Target of URI doesn't exist, The method 'ProfileInfo' isn't defined, orden de los widgets de una pantalla, usar un componente en una Screen, The named parameter is required, composición, qué va primero Scaffold o SafeArea -->

Ya tienes las dos mitades: los componentes de la sesión anterior y los widgets que arman una pantalla. Falta juntarlas. Una pantalla bien hecha casi no dibuja nada por su cuenta: ordena componentes y les entrega sus datos.

## De afuera hacia adentro

```svg
<svg id="apCapas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 464" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="apCapas-ttl apCapas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="apCapas-ttl">Una pantalla, de afuera hacia adentro</title>
  <desc id="apCapas-dsc">Cajas anidadas. La de afuera es Scaffold, la pantalla. Adentro, SafeArea, que aleja el contenido de los bordes. Adentro, SingleChildScrollView, que lo deja deslizar. Adentro, Column, que apila. En el centro, tres componentes: ProfileInfo, StatsRow y ChatItem.</desc>
  <defs>
    <style>
      #apCapas .title{fill:#161A26;font-size:22px;font-weight:700}
      #apCapas .sub{fill:#79809A;font-size:13.5px}
      #apCapas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #apCapas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #apCapas .nb{fill:#454C61;font-size:13px}
      #apCapas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #apCapas .foot{fill:#79809A;font-size:12px}
      #apCapas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #apCapas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#apCapas-arrow)}
    </style>
    <marker id="apCapas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="464" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Una pantalla, de afuera hacia adentro</text>
  <text class="sub" x="48" y="80" data-fit="860">Cada widget envuelve al siguiente y resuelve una sola cosa. Tus componentes van en el centro.</text>
  <rect x="48" y="112" width="864" height="304" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="64" y="139" font-size="14.5" font-weight="700" fill="#4453C9" text-anchor="start" class="mono">Scaffold</text>
  <text x="896" y="139" font-size="13" font-weight="400" fill="#556074" text-anchor="end" data-fit="360">La pantalla: fondo y barra</text>
  <rect x="72" y="156" width="816" height="244" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
  <text x="88" y="183" font-size="14.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">SafeArea</text>
  <text x="872" y="183" font-size="13" font-weight="400" fill="#556074" text-anchor="end" data-fit="360">Lejos de la cámara y de los gestos</text>
  <rect x="96" y="200" width="768" height="184" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="112" y="227" font-size="14.5" font-weight="700" fill="#A96C05" text-anchor="start" class="mono">SingleChildScrollView</text>
  <text x="848" y="227" font-size="13" font-weight="400" fill="#556074" text-anchor="end" data-fit="360">Se desliza si no cabe</text>
  <rect x="120" y="244" width="720" height="124" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="136" y="271" font-size="14.5" font-weight="700" fill="#0F8478" text-anchor="start" class="mono">Column</text>
  <text x="824" y="271" font-size="13" font-weight="400" fill="#556074" text-anchor="end" data-fit="360">Apila uno debajo de otro</text>
  <rect x="136" y="288" width="224" height="64" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>
  <text dy="0.35em" x="248" y="320" font-size="14" font-weight="700" fill="#161A26" text-anchor="middle" class="mono">ProfileInfo</text>
  <rect x="368" y="288" width="224" height="64" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>
  <text dy="0.35em" x="480" y="320" font-size="14" font-weight="700" fill="#161A26" text-anchor="middle" class="mono">StatsRow</text>
  <rect x="600" y="288" width="224" height="64" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>
  <text dy="0.35em" x="712" y="320" font-size="14" font-weight="700" fill="#161A26" text-anchor="middle" class="mono">ChatItem</text>
  <text x="480" y="440" font-size="12.5" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="860">Se escribe en este orden y se lee igual: de afuera hacia adentro.</text>
</svg>
```

Cada capa responde una pregunta, y en ese orden se escribe:

- **¿Es una pantalla?** Entonces empieza por `Scaffold`, con su `appBar` si lleva barra.
- **¿Qué va en el `body`?** Siempre un `SafeArea`.
- **¿El contenido puede no caber?** Entonces un `SingleChildScrollView`, con su `padding`.
- **¿Cómo se acomoda?** Casi siempre en una `Column`, con `SizedBox` entre los bloques.

Lo que queda adentro son componentes.

## Traer los componentes

Cada componente vive en su archivo, así que la pantalla tiene que importarlos. Se importan igual que la pantalla en `main.dart`: con `package:`, el nombre del proyecto y la ruta desde `lib/`.

```dart
import 'package:flutter/material.dart';
import 'package:miapp1/components/profile_info.dart';
import 'package:miapp1/components/stats_row.dart';
```

Si usas un componente sin importarlo, el editor lo subraya y dice `The method 'ProfileInfo' isn't defined`. Si el `import` está pero la ruta tiene un error, dice `Target of URI doesn't exist`. En los dos casos el arreglo está en las primeras líneas del archivo.

## Los componentes, en su lugar

```svg
<svg id="apPerfil" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 684" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="apPerfil-ttl apPerfil-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="apPerfil-ttl">Tus componentes, dentro de la pantalla</title>
  <desc id="apPerfil-dsc">El body de ProfileScreen: SafeArea, SingleChildScrollView y una Column con ProfileInfo, un SizedBox y StatsRow. En el resultado, el bloque de información del perfil arriba y la fila de estadísticas debajo.</desc>
  <defs>
    <style>
      #apPerfil .title{fill:#161A26;font-size:22px;font-weight:700}
      #apPerfil .sub{fill:#79809A;font-size:13.5px}
      #apPerfil .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #apPerfil .cl{font-size:13px;fill:#C9CFDA}
      #apPerfil .s{fill:#A8D8A0} #apPerfil .n{fill:#F2B880} #apPerfil .c{fill:#7FD1E8}
      #apPerfil .p{fill:#D5B8F5} #apPerfil .k{fill:#F08FB0}
      #apPerfil .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #apPerfil .ct{fill:#161A26;font-size:14px;font-weight:700}
      #apPerfil .cb{fill:#454C61;font-size:13px}
      #apPerfil .rt{fill:#161A26;font-size:14px} #apPerfil .rs{fill:#79809A;font-size:12px}
      #apPerfil .foot{fill:#79809A;font-size:12px}
      #apPerfil .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #apPerfil .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #apPerfil .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#apPerfil-ar-indigo)}
      #apPerfil .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #apPerfil .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #apPerfil .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#apPerfil-ar-violet)}
    </style>
    <marker id="apPerfil-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="apPerfil-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="684" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Tus componentes, dentro de la pantalla</text>
  <text class="sub" x="48" y="80" data-fit="860">La pantalla no dibuja nada por su cuenta: ordena componentes y les entrega sus datos.</text>
  <rect x="48" y="112" width="456" height="540" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/profile_screen.dart</text>
  <rect x="552" y="112" width="360" height="540" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-violet" x="126.4" y="276" width="93.8" height="22" rx="5"/>
  <rect class="hl-indigo" x="126.4" y="420" width="70.4" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="117.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">body</tspan>: <tspan class="c">SafeArea</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="226.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">SingleChildScrollView</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="220" textLength="218.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">padding</tspan>: <tspan class="c">EdgeInsets</tspan>.all(<tspan class="n">16</tspan>),</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Column</tspan>(</text>
  <text class="cl mono" font-size="13" x="114.8" y="268" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">children</tspan>: [</text>
  <text class="cl mono" font-size="13" x="130.4" y="292" textLength="93.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">ProfileInfo</tspan>(</text>
  <text class="cl mono" font-size="13" x="146.0" y="316" textLength="210.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">name</tspan>: <tspan class="s">'Mariana Valenzuela'</tspan>,</text>
  <text class="cl mono" font-size="13" x="146.0" y="340" textLength="171.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">username</tspan>: <tspan class="s">'@marianav'</tspan>,</text>
  <text class="cl mono" font-size="13" x="146.0" y="364" textLength="23.4" lengthAdjust="spacingAndGlyphs" data-fit="432">...</text>
  <text class="cl mono" font-size="13" x="130.4" y="388" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="130.4" y="412" textLength="163.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">SizedBox</tspan>(<tspan class="p">height</tspan>: <tspan class="n">24</tspan>),</text>
  <text class="cl mono" font-size="13" x="130.4" y="436" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">StatsRow</tspan>(</text>
  <text class="cl mono" font-size="13" x="146.0" y="460" textLength="101.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">posts</tspan>: <tspan class="s">'128'</tspan>,</text>
  <text class="cl mono" font-size="13" x="146.0" y="484" textLength="140.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">followers</tspan>: <tspan class="s">'2.4k'</tspan>,</text>
  <text class="cl mono" font-size="13" x="146.0" y="508" textLength="132.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">following</tspan>: <tspan class="s">'310'</tspan>,</text>
  <text class="cl mono" font-size="13" x="130.4" y="532" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="114.8" y="556" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="99.2" y="580" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="83.6" y="604" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="68.0" y="628" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <g transform="translate(552,144)">
<rect x="40" y="20" width="280" height="420" rx="26" fill="#FFFFFF" stroke="#2A3040" stroke-width="3"/><rect x="42" y="22" width="276" height="44" rx="24" fill="#F1ECF8"/><rect x="42" y="44" width="276" height="22" fill="#F1ECF8"/><text x="60" y="50" font-size="15" font-weight="500" fill="#161A26" text-anchor="start">Perfil</text><circle cx="180" cy="116" r="30" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><circle cx="180" cy="110.0" r="9.9" fill="#C9A6EE"/><path d="M161.4,138.2 a18.6,16.8 0 0 1 37.2,0 Z" fill="#C9A6EE"/><text x="180" y="170" font-size="15.5" font-weight="700" fill="#161A26" text-anchor="middle">Mariana Valenzuela</text><text x="180" y="190" font-size="12" font-weight="400" fill="#556074" text-anchor="middle" data-fit="250">@marianav • Diseñadora de Producto</text><text x="180" y="210" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="250">m.val@estudio.com · Madrid, ES</text><rect x="52" y="252" width="82" height="60" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="93" y="278" font-size="17" font-weight="700" fill="#161A26" text-anchor="middle">128</text><text x="93" y="298" font-size="12" font-weight="400" fill="#556074" text-anchor="middle" data-fit="80">Publicaciones</text><rect x="139" y="252" width="82" height="60" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="180" y="278" font-size="17" font-weight="700" fill="#161A26" text-anchor="middle">2.4k</text><text x="180" y="298" font-size="12" font-weight="400" fill="#556074" text-anchor="middle" data-fit="80">Seguidores</text><rect x="226" y="252" width="82" height="60" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="267" y="278" font-size="17" font-weight="700" fill="#161A26" text-anchor="middle">310</text><text x="267" y="298" font-size="12" font-weight="400" fill="#556074" text-anchor="middle" data-fit="80">Seguidos</text><rect x="46" y="76" width="268" height="148" rx="12" fill="#7439B8" fill-opacity=".08" stroke="#7439B8" stroke-width="2"/><rect x="46" y="244" width="268" height="76" rx="12" fill="#4453C9" fill-opacity=".08" stroke="#4453C9" stroke-width="2"/>
  </g>
  <path class="ld-violet" d="M230.0,287 H504"/>
  <path class="ar-violet" d="M504,287 H598"/>
  <path class="ld-indigo" d="M206.6,431 H504"/>
  <path class="ar-indigo" d="M504,431 H598"/>
</svg>
```

Este es `lib/screens/profile_screen.dart` completo, con la mitad de arriba del perfil:

```dart
import 'package:flutter/material.dart';
import 'package:miapp1/components/profile_info.dart';
import 'package:miapp1/components/stats_row.dart';

/// Profile of a person.
class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Perfil')),
      body: const SafeArea(
        child: SingleChildScrollView(
          padding: EdgeInsets.all(16),
          child: Column(
            children: [
              ProfileInfo(
                imageUrl: 'https://picsum.photos/400',
                name: 'Mariana Valenzuela',
                username: '@marianav',
                role: 'Diseñadora de Producto',
                bio: 'Creando experiencias digitales enfocadas en el usuario.',
                email: 'm.val@estudio.com',
                location: 'Madrid, ES',
              ),
              SizedBox(height: 24),
              StatsRow(posts: '128', followers: '2.4k', following: '310'),
            ],
          ),
        ),
      ),
    );
  }
}
```

Compara este archivo con lo que sería la misma pantalla sin componentes: más de cien líneas de `Row`, `Column` y `Text` mezcladas. Aquí se lee de un vistazo qué hay en la pantalla y en qué orden.

## Ejemplo completo

La pantalla de arriba, con versiones cortas de `ProfileInfo`, `StatsRow` y `StatCard` en el mismo archivo. Agrega un segundo `StatsRow` debajo del primero, con otros números.

```dart trycode=PENDIENTE_S25
import 'package:flutter/material.dart';

void main() {
  runApp(const App());
}

/// Root widget of the app.
class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mi app',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      initialRoute: '/profile',
      routes: {'/profile': (context) => const ProfileScreen()},
    );
  }
}

/// Profile of a person.
class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Perfil')),
      body: const SafeArea(
        child: SingleChildScrollView(
          padding: EdgeInsets.all(16),
          child: Column(
            children: [
              ProfileInfo(
                imageUrl: 'https://picsum.photos/400',
                name: 'Mariana Valenzuela',
                username: '@marianav',
                role: 'Diseñadora de Producto',
              ),
              SizedBox(height: 24),
              StatsRow(posts: '128', followers: '2.4k', following: '310'),
            ],
          ),
        ),
      ),
    );
  }
}

/// Header of a profile: photo, name, username and role.
class ProfileInfo extends StatelessWidget {
  final String imageUrl;
  final String name;
  final String username;
  final String role;

  const ProfileInfo({
    super.key,
    required this.imageUrl,
    required this.name,
    required this.username,
    required this.role,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        CircleAvatar(radius: 48, backgroundImage: NetworkImage(imageUrl)),
        const SizedBox(height: 12),
        Text(
          name,
          style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
        ),
        Text('$username • $role', style: const TextStyle(color: Colors.grey)),
      ],
    );
  }
}

/// Row with the three numbers of a profile.
class StatsRow extends StatelessWidget {
  final String posts;
  final String followers;
  final String following;

  const StatsRow({
    super.key,
    required this.posts,
    required this.followers,
    required this.following,
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: [
        StatCard(number: posts, label: 'Publicaciones'),
        StatCard(number: followers, label: 'Seguidores'),
        StatCard(number: following, label: 'Seguidos'),
      ],
    );
  }
}

/// Shows a number with its label.
class StatCard extends StatelessWidget {
  final String number;
  final String label;

  const StatCard({super.key, required this.number, required this.label});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(
        color: Colors.indigo.shade50,
        border: Border.all(color: Colors.indigo.shade200, width: 2),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        children: [
          Text(
            number,
            style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
          ),
          Text(label, style: const TextStyle(fontSize: 12, color: Colors.grey)),
        ],
      ),
    );
  }
}
```

Aquí todo va en un solo archivo porque el editor en línea solo tiene uno. En tu proyecto cada componente está en `lib/components/` y la pantalla los importa.
