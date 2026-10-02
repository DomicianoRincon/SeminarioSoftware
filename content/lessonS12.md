# Image

<!-- tags: Image.network, Image.asset, Unable to load asset, pubspec.yaml assets, BoxFit.cover, imagen deformada o recortada, width y height de una imagen, la imagen no aparece, BoxFit.contain, sangría del pubspec -->

`Image` muestra una imagen. Lo primero que hay que decidir es **de dónde sale**: de internet o de un archivo que viaja dentro de la app. Cada origen tiene su constructor.

## Una imagen desde internet

`Image.network` recibe la dirección de la imagen y la descarga:

```svg
<svg id="imNetwork" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 444" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="imNetwork-ttl imNetwork-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="imNetwork-ttl">Una imagen desde internet</title>
  <desc id="imNetwork-dsc">Image.network con la dirección de la imagen, width 160 y height 160. A la derecha, la imagen dibujada con sus dos medidas señaladas.</desc>
  <defs>
    <style>
      #imNetwork .title{fill:#161A26;font-size:22px;font-weight:700}
      #imNetwork .sub{fill:#79809A;font-size:13.5px}
      #imNetwork .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #imNetwork .cl{font-size:13px;fill:#C9CFDA}
      #imNetwork .s{fill:#A8D8A0} #imNetwork .n{fill:#F2B880} #imNetwork .c{fill:#7FD1E8}
      #imNetwork .p{fill:#D5B8F5} #imNetwork .k{fill:#F08FB0}
      #imNetwork .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #imNetwork .ct{fill:#161A26;font-size:14px;font-weight:700}
      #imNetwork .cb{fill:#454C61;font-size:13px}
      #imNetwork .rt{fill:#161A26;font-size:14px} #imNetwork .rs{fill:#79809A;font-size:12px}
      #imNetwork .foot{fill:#79809A;font-size:12px}
      #imNetwork .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #imNetwork .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #imNetwork .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#imNetwork-ar-green)}
      #imNetwork .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #imNetwork .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #imNetwork .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#imNetwork-ar-indigo)}
      #imNetwork .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #imNetwork .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #imNetwork .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#imNetwork-ar-violet)}
    </style>
    <marker id="imNetwork-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="imNetwork-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="imNetwork-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="444" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Una imagen desde internet</text>
  <text class="sub" x="48" y="80" data-fit="860">La dirección dice de dónde se descarga. width y height reservan el espacio que ocupa.</text>
  <rect x="48" y="112" width="456" height="300" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/main.dart</text>
  <rect x="552" y="112" width="360" height="300" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="79.6" y="180" width="218.6" height="22" rx="5"/>
  <rect class="hl-green" x="79.6" y="204" width="86.0" height="22" rx="5"/>
  <rect class="hl-violet" x="79.6" y="228" width="93.8" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Image</tspan>.network(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="218.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">'https://picsum.photos/400'</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">width</tspan>: <tspan class="n">160</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="93.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">height</tspan>: <tspan class="n">160</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="268" textLength="140.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">fit</tspan>: <tspan class="c">BoxFit</tspan>.cover,</text>
  <text class="cl mono" font-size="13" x="68.0" y="292" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<clipPath id="imNetwork-clip"><rect x="140" y="72" width="144" height="144" rx="6"/></clipPath><g clip-path="url(#imNetwork-clip)"><rect x="140" y="72" width="144" height="144" fill="#CFE4FF"/><circle cx="243.68" cy="112.32000000000001" r="18.72" fill="#F7C948"/><path d="M140,216 L188.96,132.48 L220.64000000000001,178.56 L243.68,152.64000000000001 L284,201.6 V216 Z" fill="#5B8C5A"/><path d="M140,216 L188.96,132.48 L206.24,158.39999999999998 L168.8,216 Z" fill="#3E6B45"/></g><path d="M140,232 H284 M140,226 V238 M284,226 V238" stroke="#3A8235" stroke-width="1.75" fill="none"/><text x="212" y="252" text-anchor="middle" font-size="12.5" font-weight="700" fill="#3A8235">160</text><path d="M124,72 V216 M118,72 H130 M118,216 H130" stroke="#7439B8" stroke-width="1.75" fill="none"/><text x="110" y="144" dy="0.35em" text-anchor="end" font-size="12.5" font-weight="700" fill="#7439B8">160</text>
  </g>
  <path class="ld-indigo" d="M308.0,191 H504"/>
  <path class="ar-indigo" d="M504,191 H764 V214"/>
  <path class="ld-green" d="M175.4,215 H504"/>
  <path class="ar-green" d="M504,215 H514 V376 H612 V376 H688"/>
  <path class="ld-violet" d="M183.2,239 H504"/>
  <path class="ar-violet" d="M504,239 H532 V288 H636"/>
</svg>
```

```dart
Image.network(
  'https://picsum.photos/400',
  width: 160,
  height: 160,
  fit: BoxFit.cover,
)
```

- La **dirección** tiene que apuntar al archivo de la imagen, no a la página donde aparece.
- **`width`** y **`height`** son el espacio que ocupa en pantalla, en píxeles lógicos. Ponlos casi siempre: sin ellos la imagen sale a su tamaño real, y mientras se descarga no ocupa nada, así que todo lo que está debajo salta cuando termina de cargar.
- **`fit`** decide qué pasa cuando la imagen no tiene la forma del espacio. Tiene su propio apartado más abajo.

Úsala para lo que cambia y no conoces de antemano: la foto de un perfil, la portada de un producto.

## Una imagen que viaja con la app

Lo que es parte del diseño (el logo, una ilustración de bienvenida) se guarda dentro del proyecto y se muestra con `Image.asset`. Son tres pasos:

```svg
<svg id="imAsset" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 392" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="imAsset-ttl imAsset-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="imAsset-ttl">Una imagen que viaja con la app</title>
  <desc id="imAsset-dsc">Los tres pasos para mostrar una imagen local: guardar el archivo en la carpeta assets del proyecto, declarar la carpeta en pubspec.yaml y usar Image.asset con la ruta del archivo.</desc>
  <defs>
    <style>
      #imAsset .title{fill:#161A26;font-size:22px;font-weight:700}
      #imAsset .sub{fill:#79809A;font-size:13.5px}
      #imAsset .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #imAsset .nt{font-size:15px;font-weight:700;fill:#161A26}
      #imAsset .nb{fill:#454C61;font-size:13px}
      #imAsset .lbl{fill:#556074;font-size:12px;font-weight:600}
      #imAsset .foot{fill:#79809A;font-size:12px}
      #imAsset .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #imAsset .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#imAsset-arrow)}
      #imAsset .code{font-size:13px;fill:#C9CFDA}
      #imAsset .s{fill:#A8D8A0} #imAsset .c{fill:#7FD1E8} #imAsset .k{fill:#F08FB0}
    </style>
    <marker id="imAsset-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="392" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Una imagen que viaja con la app</text>
  <text class="sub" x="48" y="80" data-fit="860">Tres pasos, siempre los mismos. Si falta el segundo, la app no encuentra el archivo.</text>
  <g transform="translate(48,112)">
    <rect width="272" height="216" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="28" cy="28" r="12" fill="#F2C069"/>
    <text x="28" y="28" dy="0.35em" text-anchor="middle" font-size="13" font-weight="700" fill="#1F2430">1</text>
    <text class="nt" x="50" y="28" dy="0.35em" data-fit="206">Guarda el archivo</text>
    <rect x="16" y="52" width="240" height="124" rx="8" fill="#1F2430"/>
    <text class="mono" x="28" y="72" font-size="12" fill="#8A93A6" data-fit="216">miapp1/</text>
    <text class="code mono" x="28.0" y="96" data-fit="216"><tspan class="c">assets/</tspan></text>
    <text class="code mono" x="43.6" y="118" data-fit="200">logo.png</text>
    <text class="code mono" x="28.0" y="140" data-fit="216"><tspan class="c">lib/</tspan></text>
    <text class="code mono" x="28.0" y="162" data-fit="216">pubspec.yaml</text>
    <text x="16" y="198" font-size="12.5" fill="#454C61" data-fit="240">En assets/, al lado de lib/</text>
  </g>
  <path class="link" d="M322,220 H342"/>
  <g transform="translate(344,112)">
    <rect width="272" height="216" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="28" cy="28" r="12" fill="#F2C069"/>
    <text x="28" y="28" dy="0.35em" text-anchor="middle" font-size="13" font-weight="700" fill="#1F2430">2</text>
    <text class="nt" x="50" y="28" dy="0.35em" data-fit="206">Declara la carpeta</text>
    <rect x="16" y="52" width="240" height="124" rx="8" fill="#1F2430"/>
    <text class="mono" x="28" y="72" font-size="12" fill="#8A93A6" data-fit="216">pubspec.yaml</text>
    <text class="code mono" x="28.0" y="96" data-fit="216"><tspan class="k">flutter:</tspan></text>
    <text class="code mono" x="43.6" y="118" data-fit="200"><tspan class="k">assets:</tspan></text>
    <text class="code mono" x="59.2" y="140" data-fit="185">- assets/</text>
    <text x="16" y="198" font-size="12.5" fill="#454C61" data-fit="240">La sangría de dos espacios importa</text>
  </g>
  <path class="link" d="M618,220 H638"/>
  <g transform="translate(640,112)">
    <rect width="272" height="216" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="28" cy="28" r="12" fill="#F2C069"/>
    <text x="28" y="28" dy="0.35em" text-anchor="middle" font-size="13" font-weight="700" fill="#1F2430">3</text>
    <text class="nt" x="50" y="28" dy="0.35em" data-fit="206">Úsala en el código</text>
    <rect x="16" y="52" width="240" height="124" rx="8" fill="#1F2430"/>
    <text class="mono" x="28" y="72" font-size="12" fill="#8A93A6" data-fit="216">lib/main.dart</text>
    <text class="code mono" x="28.0" y="96" data-fit="216"><tspan class="c">Image</tspan>.asset(</text>
    <text class="code mono" x="43.6" y="118" data-fit="200"><tspan class="s">'assets/logo.png'</tspan>,</text>
    <text class="code mono" x="43.6" y="140" data-fit="200">width: 120,</text>
    <text class="code mono" x="28.0" y="162" data-fit="216">)</text>
    <text x="16" y="198" font-size="12.5" fill="#454C61" data-fit="240">La ruta completa desde la raíz</text>
  </g>
  <text class="foot" x="48" y="364" data-fit="860">Después de tocar pubspec.yaml hay que detener la app y volver a ejecutarla: el hot reload no carga assets nuevos.</text>
</svg>
```

**1.** Crea la carpeta `assets` en la raíz del proyecto, al lado de `lib`, y copia ahí la imagen.

**2.** Abre `pubspec.yaml`, busca la sección `flutter:` que está casi al final y declara la carpeta:

```yaml
flutter:
  uses-material-design: true
  assets:
    - assets/
```

**3.** Úsala en el código con la ruta completa:

```dart
Image.asset(
  'assets/logo.png',
  width: 120,
)
```

Si pones solo `width`, el alto se calcula solo y la imagen conserva su proporción.

Cuando algo falla, la consola muestra `Unable to load asset: "assets/logo.png"`. Casi siempre es una de estas tres cosas:

| Causa | Cómo se arregla |
|---|---|
| La sangría de `pubspec.yaml` está mal | `assets:` va con dos espacios y `- assets/` con cuatro. Sin tabuladores |
| El nombre no coincide | `Logo.png` y `logo.png` son archivos distintos |
| La app sigue corriendo con la configuración vieja | Detenla y vuelve a ejecutarla. El hot reload no carga assets nuevos |

## fit: cuando la forma no coincide

Una foto rara vez tiene la misma proporción que el espacio donde va. `fit` dice cómo resolverlo:

```svg
<svg id="imFit" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 468" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="imFit-ttl imFit-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="imFit-ttl">Qué hace fit cuando la imagen no tiene la forma de la caja</title>
  <desc id="imFit-dsc">La misma imagen dentro de una caja alargada con tres valores de fit: cover llena la caja y recorta lo que sobra, contain muestra la imagen entera y deja espacio vacío, fill la estira hasta deformarla.</desc>
  <defs>
    <style>
      #imFit .title{fill:#161A26;font-size:22px;font-weight:700}
      #imFit .sub{fill:#79809A;font-size:13.5px}
      #imFit .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #imFit .nt{font-size:15px;font-weight:700;fill:#161A26}
      #imFit .nb{fill:#454C61;font-size:13px}
      #imFit .lbl{fill:#556074;font-size:12px;font-weight:600}
      #imFit .foot{fill:#79809A;font-size:12px}
      #imFit .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #imFit .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#imFit-arrow)}
    </style>
    <marker id="imFit-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="468" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Qué hace <tspan class="mono">fit</tspan> cuando la imagen no tiene la forma de la caja</text>
  <text class="sub" x="48" y="80" data-fit="860">La misma imagen, casi cuadrada, en la misma caja alargada. Solo cambia fit.</text>
  <defs><g id="imFit-pic"><rect width="120" height="90" fill="#CFE4FF"/><circle cx="88" cy="24" r="12" fill="#F7C948"/><path d="M0,90 L40,38 L66,66 L86,50 L120,82 V90 Z" fill="#5B8C5A"/><path d="M0,90 L40,38 L55,54 L24,90 Z" fill="#3E6B45"/></g></defs>
  <text class="h" x="48" y="124">LA IMAGEN ORIGINAL</text>
  <g transform="translate(48,136)"><use href="#imFit-pic"/></g>
  <text class="nb" x="184" y="176" data-fit="300">Mide 4 de ancho por 3 de alto.</text>
  <text class="nb" x="184" y="196" data-fit="300">La caja donde va es mucho más ancha que alta.</text>
  <clipPath id="imFit-c0"><rect width="240" height="120" rx="8"/></clipPath>
  <g transform="translate(48,288)">
    <text class="mono" x="0" y="-12" font-size="14" font-weight="700" fill="#3A8235" data-fit="240">BoxFit.cover</text>
    <rect width="240" height="120" rx="8" fill="#EFF1F5"/>
    <g clip-path="url(#imFit-c0)"><use href="#imFit-pic" transform="translate(0,-30) scale(2)"/></g>
    <rect width="240" height="120" rx="8" fill="none" stroke="#9FD68D" stroke-width="2"/>
    <text class="nb" x="0" y="144" data-fit="240" font-weight="600">Llena la caja y recorta lo que sobra.</text>
    <text class="nb" x="0" y="163" data-fit="250">La más usada: no deforma ni deja huecos.</text>
  </g>
  <clipPath id="imFit-c1"><rect width="240" height="120" rx="8"/></clipPath>
  <g transform="translate(360,288)">
    <text class="mono" x="0" y="-12" font-size="14" font-weight="700" fill="#4453C9" data-fit="240">BoxFit.contain</text>
    <rect width="240" height="120" rx="8" fill="#EFF1F5"/>
    <g clip-path="url(#imFit-c1)"><use href="#imFit-pic" transform="translate(40,0) scale(1.3333)"/></g>
    <rect width="240" height="120" rx="8" fill="none" stroke="#A9B4F2" stroke-width="2"/>
    <text class="nb" x="0" y="144" data-fit="240" font-weight="600">Muestra la imagen entera.</text>
    <text class="nb" x="0" y="163" data-fit="250">Deja espacio vacío a los lados.</text>
  </g>
  <clipPath id="imFit-c2"><rect width="240" height="120" rx="8"/></clipPath>
  <g transform="translate(672,288)">
    <text class="mono" x="0" y="-12" font-size="14" font-weight="700" fill="#C2354F" data-fit="240">BoxFit.fill</text>
    <rect width="240" height="120" rx="8" fill="#EFF1F5"/>
    <g clip-path="url(#imFit-c2)"><use href="#imFit-pic" transform="scale(2,1.3333)"/></g>
    <rect width="240" height="120" rx="8" fill="none" stroke="#F3A3B2" stroke-width="2"/>
    <text class="nb" x="0" y="144" data-fit="240" font-weight="600">Estira la imagen hasta llenar.</text>
    <text class="nb" x="0" y="163" data-fit="250">Se deforma: casi nunca es lo que quieres.</text>
  </g>
</svg>
```

| Valor | Qué hace | Cuándo usarlo |
|---|---|---|
| `BoxFit.cover` | Llena el espacio y recorta lo que sobra | Fotos, portadas, fondos. Es el más usado |
| `BoxFit.contain` | Muestra la imagen entera y deja espacio vacío | Logos, y todo lo que no se puede recortar |
| `BoxFit.fill` | Estira hasta llenar | Casi nunca: deforma la imagen |

`fit` solo tiene efecto cuando la imagen tiene `width` **y** `height`. Si le falta alguno, no hay un espacio fijo que llenar.

## Ejemplo completo

Una imagen de internet y una local, con su texto:

```dart trycode=ed4927e5a9a466f6d925e1af3a174320
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
      initialRoute: '/home',
      routes: {'/home': (context) => const HomeScreen()},
    );
  }
}

/// First screen of the app.
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Imágenes')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Desde internet'),
            Image.network(
              'https://picsum.photos/400',
              width: 160,
              height: 160,
              fit: BoxFit.cover,
            ),
            const SizedBox(height: 24),
            const Text('Desde assets'),
            // Image.asset(
            //   'assets/logo.png',
            //   width: 120,
            // ),
          ],
        ),
      ),
    );
  }
}
```

El editor en línea no tiene carpeta `assets`, así que el `Image.asset` va comentado: ahí solo corre la imagen de internet. En tu proyecto, con el archivo guardado y la carpeta declarada en `pubspec.yaml`, quítale las `//` para verla.

`Column` pone un widget debajo de otro y `SizedBox` deja un espacio entre ellos. Los dos tienen su propia lección más adelante en esta sesión: *Column*.
