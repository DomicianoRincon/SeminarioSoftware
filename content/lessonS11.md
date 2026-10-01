# Text

<!-- tags: Text, TextStyle, fontSize y fontWeight, color del texto, maxLines y overflow, texto que se sale de la pantalla, TextOverflow.ellipsis, textAlign, RenderFlex overflowed, negrita -->

`Text` muestra una cadena en pantalla. Es el widget más simple de Flutter y el que más vas a escribir: títulos, etiquetas, el texto de un botón, todo es un `Text`.

## Uso básico

Lo único obligatorio es la cadena:

```dart
Text('Hola, Icesi')
```

Sin nada más, el texto sale con el tamaño y el color que define el tema de la app. Pruébalo en tu `HomeScreen`, dentro del `Center`.

## Cambiar cómo se ve: style

`Text` no tiene una propiedad `color` ni una `fontSize`. Todo lo que cambia el aspecto se agrupa en un objeto `TextStyle`, que se entrega en `style`:

```svg
<svg id="txAnatomia" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 396" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="txAnatomia-ttl txAnatomia-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="txAnatomia-ttl">Las partes de un Text</title>
  <desc id="txAnatomia-dsc">Un widget Text con la cadena Hola, Icesi y un TextStyle con fontSize 32, fontWeight bold y color indigo. A la derecha, el texto resultante y el efecto de cada propiedad por separado.</desc>
  <defs>
    <style>
      #txAnatomia .title{fill:#161A26;font-size:22px;font-weight:700}
      #txAnatomia .sub{fill:#79809A;font-size:13.5px}
      #txAnatomia .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #txAnatomia .cl{font-size:13px;fill:#C9CFDA}
      #txAnatomia .s{fill:#A8D8A0} #txAnatomia .n{fill:#F2B880} #txAnatomia .c{fill:#7FD1E8}
      #txAnatomia .p{fill:#D5B8F5} #txAnatomia .k{fill:#F08FB0}
      #txAnatomia .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #txAnatomia .ct{fill:#161A26;font-size:14px;font-weight:700}
      #txAnatomia .cb{fill:#454C61;font-size:13px}
      #txAnatomia .rt{fill:#161A26;font-size:14px} #txAnatomia .rs{fill:#79809A;font-size:12px}
      #txAnatomia .foot{fill:#79809A;font-size:12px}
      #txAnatomia .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #txAnatomia .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #txAnatomia .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#txAnatomia-ar-amber)}
      #txAnatomia .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #txAnatomia .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #txAnatomia .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#txAnatomia-ar-green)}
      #txAnatomia .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #txAnatomia .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #txAnatomia .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#txAnatomia-ar-indigo)}
      #txAnatomia .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #txAnatomia .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #txAnatomia .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#txAnatomia-ar-violet)}
    </style>
    <marker id="txAnatomia-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="txAnatomia-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="txAnatomia-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="txAnatomia-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="396" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las partes de un <tspan class="mono">Text</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">El primer dato es lo que se escribe. Todo lo que cambia cómo se ve va dentro de style.</text>
  <rect x="48" y="112" width="456" height="252" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/main.dart</text>
  <rect x="552" y="112" width="360" height="252" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="79.6" y="180" width="109.4" height="22" rx="5"/>
  <rect class="hl-amber" x="95.2" y="228" width="101.6" height="22" rx="5"/>
  <rect class="hl-green" x="95.2" y="252" width="218.6" height="22" rx="5"/>
  <rect class="hl-violet" x="95.2" y="276" width="164.0" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="39.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">'Hola, Icesi'</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="132.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">style</tspan>: <tspan class="c">TextStyle</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="101.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">fontSize</tspan>: <tspan class="n">32</tspan>,</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="218.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">fontWeight</tspan>: <tspan class="c">FontWeight</tspan>.bold,</text>
  <text class="cl mono" font-size="13" x="99.2" y="292" textLength="163.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">color</tspan>: <tspan class="c">Colors</tspan>.indigo,</text>
  <text class="cl mono" font-size="13" x="83.6" y="316" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="68.0" y="340" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<text x="188" y="47" dy="0.35em" text-anchor="middle" font-size="32" font-weight="700" fill="#3F51B5" data-fit="250">Hola, Icesi</text><g transform="translate(20,88)"><rect width="320" height="36" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="16" y="18" dy="0.35em" font-size="11" font-weight="400" fill="#161A26">Aa</text><text x="62" y="18" dy="0.35em" font-size="14" fill="#79809A">→</text><text x="86" y="18" dy="0.35em" font-size="20" font-weight="400" fill="#161A26">Aa</text><text x="140" y="18" dy="0.35em" font-size="13" fill="#454C61" data-fit="170">tamaño de la letra</text></g><g transform="translate(20,132)"><rect width="320" height="36" rx="8" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="16" y="18" dy="0.35em" font-size="14" font-weight="400" fill="#161A26">Aa</text><text x="62" y="18" dy="0.35em" font-size="14" fill="#79809A">→</text><text x="86" y="18" dy="0.35em" font-size="14" font-weight="800" fill="#161A26">Aa</text><text x="140" y="18" dy="0.35em" font-size="13" fill="#454C61" data-fit="170">grosor: negrita</text></g><g transform="translate(20,176)"><rect width="320" height="36" rx="8" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="16" y="18" dy="0.35em" font-size="14" font-weight="400" fill="#161A26">Aa</text><text x="62" y="18" dy="0.35em" font-size="14" fill="#79809A">→</text><text x="86" y="18" dy="0.35em" font-size="14" font-weight="400" fill="#3F51B5">Aa</text><text x="140" y="18" dy="0.35em" font-size="13" fill="#454C61" data-fit="170">color de la letra</text></g>
  </g>
  <path class="ld-indigo" d="M198.8,191 H504"/>
  <path class="ar-indigo" d="M504,191 H636"/>
  <path class="ld-amber" d="M206.6,239 H504"/>
  <path class="ar-amber" d="M504,239 H532 V250 H572"/>
  <path class="ld-green" d="M323.6,263 H504"/>
  <path class="ar-green" d="M504,263 H523 V294 H572"/>
  <path class="ld-violet" d="M269.0,287 H504"/>
  <path class="ar-violet" d="M504,287 H514 V338 H572"/>
</svg>
```

```dart
Text(
  'Hola, Icesi',
  style: TextStyle(
    fontSize: 32,
    fontWeight: FontWeight.bold,
    color: Colors.indigo,
  ),
)
```

Las propiedades de `TextStyle` que más se usan:

| Propiedad | Qué cambia | Valores típicos |
|---|---|---|
| `fontSize` | El tamaño de la letra | `12` para una nota, `16` para texto normal, `24` o más para un título |
| `fontWeight` | El grosor | `FontWeight.normal`, `FontWeight.w500`, `FontWeight.bold` |
| `color` | El color | `Colors.indigo`, `Colors.grey`, o uno propio como `AppColors.primary` |
| `fontStyle` | Cursiva | `FontStyle.italic` |
| `letterSpacing` | El espacio entre letras | `1.5` |

Solo escribes las que quieras cambiar. Las demás conservan el valor del tema.

`fontSize` no se mide en píxeles sino en **píxeles lógicos**: Flutter los convierte según la pantalla, así que un `16` se lee igual de grande en un celular y en un monitor.

## Cuando el texto no cabe

Un `Text` ocupa todos los renglones que necesite. En un título de tarjeta o en una fila de lista eso descuadra el diseño, y se controla con dos propiedades que van **en el `Text`**, no en el `TextStyle`:

```svg
<svg id="txLargo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 444" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="txLargo-ttl txLargo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="txLargo-ttl">Cuando el texto no cabe</title>
  <desc id="txLargo-dsc">Un Text con maxLines 1 y overflow TextOverflow.ellipsis. A la derecha, el mismo texto sin límite ocupa tres renglones, y con el límite ocupa uno solo terminado en puntos suspensivos.</desc>
  <defs>
    <style>
      #txLargo .title{fill:#161A26;font-size:22px;font-weight:700}
      #txLargo .sub{fill:#79809A;font-size:13.5px}
      #txLargo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #txLargo .cl{font-size:13px;fill:#C9CFDA}
      #txLargo .s{fill:#A8D8A0} #txLargo .n{fill:#F2B880} #txLargo .c{fill:#7FD1E8}
      #txLargo .p{fill:#D5B8F5} #txLargo .k{fill:#F08FB0}
      #txLargo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #txLargo .ct{fill:#161A26;font-size:14px;font-weight:700}
      #txLargo .cb{fill:#454C61;font-size:13px}
      #txLargo .rt{fill:#161A26;font-size:14px} #txLargo .rs{fill:#79809A;font-size:12px}
      #txLargo .foot{fill:#79809A;font-size:12px}
      #txLargo .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #txLargo .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #txLargo .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#txLargo-ar-amber)}
      #txLargo .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #txLargo .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #txLargo .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#txLargo-ar-green)}
    </style>
    <marker id="txLargo-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="txLargo-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
  </defs>
  <rect width="960" height="444" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Cuando el texto no cabe</text>
  <text class="sub" x="48" y="80" data-fit="860">Un texto largo ocupa los renglones que necesite. Con dos propiedades lo dejas en uno solo.</text>
  <rect x="48" y="112" width="456" height="300" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/main.dart</text>
  <rect x="552" y="112" width="360" height="300" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-green" x="79.6" y="204" width="93.8" height="22" rx="5"/>
  <rect class="hl-amber" x="79.6" y="228" width="249.8" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="39.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="366.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">'Seminario de Ingeniería de Software, grupo 1'</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="93.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">maxLines</tspan>: <tspan class="n">1</tspan>,</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="249.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">overflow</tspan>: <tspan class="c">TextOverflow</tspan>.ellipsis,</text>
  <text class="cl mono" font-size="13" x="68.0" y="268" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<text x="24" y="28" font-size="12" font-weight="700" fill="#79809A" letter-spacing=".06em">SIN LÍMITE</text><rect x="24" y="40" width="176" height="84" rx="8" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="36" y="64" font-size="15" fill="#161A26" data-fit="156">Seminario de</text><text x="36" y="86" font-size="15" fill="#161A26" data-fit="156">Ingeniería de</text><text x="36" y="108" font-size="15" fill="#161A26" data-fit="156">Software, grupo 1</text><text x="24" y="164" font-size="12" font-weight="700" fill="#79809A" letter-spacing=".06em">CON maxLines Y overflow</text><rect x="24" y="176" width="176" height="40" rx="8" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="36" y="196" dy="0.35em" font-size="15" fill="#161A26" data-fit="156">Seminario de Ingeni…</text><text x="216" y="190" font-size="12.5" fill="#454C61" data-fit="130">un solo renglón</text><text x="216" y="208" font-size="12.5" fill="#454C61" data-fit="130">y tres puntos al final</text>
  </g>
  <path class="ld-green" d="M183.2,215 H504"/>
  <path class="ar-green" d="M504,215 H523 V340 H576"/>
  <path class="ld-amber" d="M339.2,239 H504"/>
  <path class="ar-amber" d="M504,239 H514 V384 H734 V362 H734"/>
</svg>
```

```dart
Text(
  'Seminario de Ingeniería de Software, grupo 1',
  maxLines: 1,
  overflow: TextOverflow.ellipsis,
)
```

- `maxLines` es el máximo de renglones.
- `overflow` dice qué hacer con lo que sobra. `TextOverflow.ellipsis` pone los tres puntos.

Con `textAlign` se alinea el texto cuando ocupa varios renglones: `TextAlign.center`, `TextAlign.left` o `TextAlign.right`.

```dart
Text(
  'Bienvenido al seminario. Aquí vas a construir tu primera aplicación.',
  textAlign: TextAlign.center,
)
```

## Ejemplo completo

Varios `Text` con estilos distintos, uno debajo del otro:

```dart trycode=407020861ee8301495bb36973b9edc74
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Ejemplo Text Widget',
      home: Scaffold(
        appBar: AppBar(title: const Text('Widget Text')),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: const [
              Text(
                'Texto por defecto',
              ),
              SizedBox(height: 20),
              Text(
                'Texto de color verde',
                style: TextStyle(color: Colors.green),
              ),
              SizedBox(height: 20),
              Text(
                'Texto con tamaño 30',
                style: TextStyle(fontSize: 30.0),
              ),
              SizedBox(height: 20),
              Text(
                'Texto en negrita',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 20),
              Text(
                'Texto morado, grande y en negrita',
                style: TextStyle(
                  color: Colors.purple,
                  fontSize: 25.0,
                  fontWeight: FontWeight.w700,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

Este ejemplo viene de Aplicaciones Móviles y arranca con `home:` en lugar de la tabla de rutas. Sirve para experimentar en el navegador; en tu proyecto sigue usando el `main.dart` de la lección anterior.
