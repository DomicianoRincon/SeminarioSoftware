# Estado: StatelessWidget frente a StatefulWidget

<!-- tags: StatefulWidget, estado de un widget, createState, clase State, StatelessWidget vs StatefulWidget, por qué el estado no va en el widget, campos final, _HomeScreenState, la pantalla no cambia, Stateful Widget -->

Hasta ahora tus pantallas muestran siempre lo mismo: el perfil de la sesión 3 se ve igual la primera vez que se abre y la décima. Una app de verdad cambia mientras la usas. Un contador sube, un campo muestra lo que escribes y una lista crece. A todo lo que puede cambiar mientras la pantalla está abierta se le llama **estado**.

## Qué es el estado

El estado son los **datos que cambian mientras la pantalla está abierta** y que la pantalla tiene que mostrar. Unos ejemplos:

- cuántas veces se pulsó un botón;
- si un bombillo está encendido o apagado;
- lo que alguien escribió en un campo;
- las canciones que lleva una playlist.

El título de la barra o el texto de un botón no son estado, porque no cambian. Una buena pregunta para distinguirlos es: *¿esto puede valer distinto dentro de un minuto, sin salir de la pantalla?* Si la respuesta es sí, es estado.

## Dos tipos de widget

Los componentes que hiciste en la sesión 2 eran `StatelessWidget`: reciben sus datos por el constructor, los guardan en campos `final` y los dibujan. No pueden cambiar por sí solos. Para algo que cambia, Flutter tiene el `StatefulWidget`, que se parte en dos clases:

```svg
<svg id="ewComparar" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 488" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ewComparar-ttl ewComparar-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ewComparar-ttl">Un widget sin estado y uno con estado</title>
  <desc id="ewComparar-dsc">A la izquierda, un StatelessWidget: una sola clase con campos final y un build que dibuja lo que recibe. A la derecha, un StatefulWidget: la clase del widget, que solo guarda la configuración, crea con createState un objeto State que guarda los datos que cambian, tiene el build y sobrevive cuando el widget se vuelve a crear.</desc>
  <defs>
    <style>
      #ewComparar .title{fill:#161A26;font-size:22px;font-weight:700}
      #ewComparar .sub{fill:#79809A;font-size:13.5px}
      #ewComparar .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ewComparar .nt{font-size:15px;font-weight:700;fill:#161A26}
      #ewComparar .nb{fill:#454C61;font-size:13px}
      #ewComparar .lbl{fill:#556074;font-size:12px;font-weight:600}
      #ewComparar .foot{fill:#79809A;font-size:12px}
      #ewComparar .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ewComparar .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#ewComparar-arrow)}
    </style>
    <marker id="ewComparar-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="488" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Un widget sin estado y uno con estado</text>
  <text class="sub" x="48" y="80" data-fit="860">El StatelessWidget es una sola clase. El StatefulWidget se parte en dos: el widget y su State.</text>
  <text x="48" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="h">STATELESSWIDGET</text>
  <rect x="48" y="144" width="408" height="156" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="72" y="176" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" class="mono">ProfileInfo</text>
  <text x="72" y="204" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="360">Recibe sus datos por el constructor,</text><text x="72" y="223" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="360">en campos final.</text><text x="72" y="242" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="360">build() los dibuja tal cual llegan.</text><text x="72" y="261" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="360">No puede cambiar por sí solo.</text>
  <rect x="48" y="324" width="408" height="76" rx="10" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.5"/><text x="64" y="346" font-size="13.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="376">Para piezas que solo muestran</text><text x="64" y="366" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="376">Los componentes de la sesión 2: botones,</text><text x="64" y="383" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="376">tarjetas, filas de estadísticas.</text>
  <text x="504" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="h">STATEFULWIDGET</text>
  <rect x="504" y="144" width="408" height="76" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="528" y="174" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" class="mono">HomeScreen</text>
  <text x="528" y="200" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="360">El widget: solo la configuración. Se puede recrear.</text>
  <path class="link" d="M708,220 V262"/>
  <text x="718" y="246" font-size="12.5" font-weight="600" fill="#556074" text-anchor="start" class="mono">createState()</text>
  <rect x="504" y="264" width="408" height="132" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="528" y="294" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" class="mono">_HomeScreenState</text>
  <text x="528" y="322" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="360">El State: guarda los datos que cambian.</text><text x="528" y="341" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="360">Aquí vive build().</text><text x="528" y="360" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="360">Sobrevive cuando el widget se recrea.</text>
  <rect x="504" y="412" width="408" height="48" rx="10" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="520" y="434" font-size="13.5" font-weight="700" fill="#7439B8" text-anchor="start" data-fit="376">Para pantallas que cambian</text><text x="520" y="454" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="376">Un contador, un formulario, una playlist.</text>
</svg>
```

- **El widget** (`HomeScreen`) solo guarda la configuración. Flutter lo puede tirar y crear otro en cualquier momento.
- **El State** (`_HomeScreenState`) guarda los datos que cambian y tiene el `build()`. Vive mientras la pantalla esté montada.

## Las dos clases en código

```svg
<svg id="ewAnatomia" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 588" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ewAnatomia-ttl ewAnatomia-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ewAnatomia-ttl">Las dos clases de un StatefulWidget</title>
  <desc id="ewAnatomia-dsc">El código de HomeScreen, que hereda de StatefulWidget y en createState devuelve un _HomeScreenState. El State tiene el campo _isOn y el método build. Cuatro tarjetas explican el widget, createState, los datos que cambian y build.</desc>
  <defs>
    <style>
      #ewAnatomia .title{fill:#161A26;font-size:22px;font-weight:700}
      #ewAnatomia .sub{fill:#79809A;font-size:13.5px}
      #ewAnatomia .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ewAnatomia .cl{font-size:13px;fill:#C9CFDA}
      #ewAnatomia .s{fill:#A8D8A0} #ewAnatomia .n{fill:#F2B880} #ewAnatomia .c{fill:#7FD1E8}
      #ewAnatomia .p{fill:#D5B8F5} #ewAnatomia .k{fill:#F08FB0}
      #ewAnatomia .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ewAnatomia .ct{fill:#161A26;font-size:14px;font-weight:700}
      #ewAnatomia .cb{fill:#454C61;font-size:13px}
      #ewAnatomia .rt{fill:#161A26;font-size:14px} #ewAnatomia .rs{fill:#79809A;font-size:12px}
      #ewAnatomia .foot{fill:#79809A;font-size:12px}
      #ewAnatomia .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #ewAnatomia .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #ewAnatomia .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#ewAnatomia-ar-amber)}
      #ewAnatomia .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #ewAnatomia .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #ewAnatomia .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#ewAnatomia-ar-green)}
      #ewAnatomia .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #ewAnatomia .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #ewAnatomia .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#ewAnatomia-ar-indigo)}
      #ewAnatomia .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #ewAnatomia .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #ewAnatomia .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#ewAnatomia-ar-violet)}
    </style>
    <marker id="ewAnatomia-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="ewAnatomia-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="ewAnatomia-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="ewAnatomia-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="588" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las dos clases de un <tspan class="mono">StatefulWidget</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">El widget se declara arriba y el State abajo. El estado y el build van en el State.</text>
  <rect x="48" y="112" width="456" height="444" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/home_screen.dart</text>
  <rect x="552" y="112" width="360" height="444" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">QUÉ HACE CADA PARTE</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="259.0" y="156" width="117.2" height="22" rx="5"/>
  <rect class="hl-amber" x="220.0" y="252" width="93.8" height="22" rx="5"/>
  <rect class="hl-violet" x="118.6" y="372" width="47.0" height="22" rx="5"/>
  <rect class="hl-green" x="134.2" y="444" width="47.0" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="319.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">class</tspan> <tspan class="c">HomeScreen</tspan> <tspan class="k">extends</tspan> <tspan class="c">StatefulWidget</tspan> {</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="234.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">const</tspan> <tspan class="c">HomeScreen</tspan>({<tspan class="k">super</tspan>.key});</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">@override</tspan></text>
  <text class="cl mono" font-size="13" x="83.6" y="268" textLength="265.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">State</tspan>&lt;<tspan class="c">HomeScreen</tspan>&gt; createState() =&gt;</text>
  <text class="cl mono" font-size="13" x="114.8" y="292" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432">_HomeScreenState();</text>
  <text class="cl mono" font-size="13" x="68.0" y="316" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="364" textLength="390.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">class</tspan> _HomeScreenState <tspan class="k">extends</tspan> <tspan class="c">State</tspan>&lt;<tspan class="c">HomeScreen</tspan>&gt; {</text>
  <text class="cl mono" font-size="13" x="83.6" y="388" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432">bool _isOn = <tspan class="k">false</tspan>;</text>
  <text class="cl mono" font-size="13" x="83.6" y="436" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">@override</tspan></text>
  <text class="cl mono" font-size="13" x="83.6" y="460" textLength="280.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Widget</tspan> build(<tspan class="c">BuildContext</tspan> context) {</text>
  <text class="cl mono" font-size="13" x="99.2" y="484" textLength="257.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="c">Text</tspan>(_isOn ? <tspan class="s">'Sí'</tspan> : <tspan class="s">'No'</tspan>);</text>
  <text class="cl mono" font-size="13" x="83.6" y="508" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="532" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <g transform="translate(552,144)">
<g transform="translate(16,16)"><rect width="328" height="72" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#4453C9" data-fit="300">El widget</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Hereda de StatefulWidget. Solo guarda</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">la configuración: aquí no va el estado.</text></g><g transform="translate(16,112)"><rect width="328" height="72" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#A96C05" data-fit="300">createState()</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Flutter lo llama una vez y conecta</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">el widget con su objeto State.</text></g><g transform="translate(16,208)"><rect width="328" height="72" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#7439B8" data-fit="300">Los datos que cambian</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Campos normales del State, sin final.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">Por convención empiezan con _.</text></g><g transform="translate(16,304)"><rect width="328" height="72" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#3A8235" data-fit="300">build() vive en el State</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Lee los campos y dibuja la pantalla</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">con lo que valen en ese momento.</text></g>
  </g>
  <path class="ld-indigo" d="M393.8,167 H504"/>
  <path class="ar-indigo" d="M504,167 H514 V190 H568"/>
  <path class="ld-amber" d="M354.8,263 H504"/>
  <path class="ar-amber" d="M504,263 H514 V286 H568"/>
  <path class="ld-violet" d="M237.8,383 H504"/>
  <path class="ar-violet" d="M504,383 H514 V382 H568"/>
  <path class="ld-green" d="M370.4,455 H504"/>
  <path class="ar-green" d="M504,455 H514 V478 H568"/>
</svg>
```

```dart
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() =>
      _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool _isOn = false;

  @override
  Widget build(BuildContext context) {
    return Text(_isOn ? 'Sí' : 'No');
  }
}
```

Tres detalles que vale la pena notar:

- El nombre del State es el del widget con `_` delante y `State` al final. El `_` lo hace **privado**: solo se usa dentro de este archivo.
- `createState()` es lo único que hace el widget. Flutter lo llama una vez y conecta el widget con su State.
- Los campos del State **no** son `final`: están ahí justamente para cambiar.

No hace falta escribir las dos clases a mano. En VS Code escribe `stful` y pulsa Enter: el editor genera el esqueleto y tú solo pones el nombre.

## Por qué el estado vive en el State

Podría parecer más simple guardar el dato en el widget. El problema es que **Flutter crea widgets nuevos todo el tiempo**: cada vez que el padre se reconstruye, tu `HomeScreen` se descarta y se crea otro objeto. El State, en cambio, se conserva: Flutter se lo conecta al widget nuevo.

Pruébalo. Pulsa `+` unas veces y luego *Reconstruir MyApp*: mira los números de objeto (`#n`) del widget y del State. Después activa *Guardar el contador en un StatelessWidget* y repite.

```interactive
state-tree
```

Con el contador en el State, el widget cambia de número pero el contador sobrevive. Con el contador en el widget pasan dos cosas malas: pulsar `+` no cambia la pantalla, porque un `StatelessWidget` no tiene cómo pedir que lo vuelvan a dibujar, y al reconstruir el padre el dato se pierde.

## Cuándo usar cada uno

- **`StatelessWidget`** para lo que solo muestra lo que recibe: botones, tarjetas, filas. Es lo normal en `lib/components/`.
- **`StatefulWidget`** cuando algo de la pantalla cambia mientras está abierta. En esta sesión, las Screens.

Empieza siempre por `StatelessWidget` y cámbialo solo si aparece un dato que cambia.

## Ejemplo completo

Un bombillo que se enciende y se apaga. `_isOn` es el estado. La función `_toggle` lo cambia dentro de `setState`, que es el tema de la siguiente lección. En tu proyecto, `App` y `HomeScreen` van en archivos separados; aquí están juntos para que corra en DartPad.

```dart trycode=5c03ad650ab4dd52d7fbac0cee78ec9c
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
      initialRoute: '/',
      routes: {
        '/': (context) => const HomeScreen(),
      },
    );
  }
}

/// Screen with a light bulb that turns on and off.
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool _isOn = false;

  void _toggle() {
    setState(() {
      _isOn = !_isOn;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Bombillo')),
      body: SafeArea(
        child: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(
                _isOn ? Icons.lightbulb : Icons.lightbulb_outline,
                size: 96,
                color: _isOn ? Colors.amber : Colors.grey,
              ),
              const SizedBox(height: 16),
              Text(_isOn ? 'Encendido' : 'Apagado'),
              const SizedBox(height: 16),
              FilledButton(
                onPressed: () => _toggle(),
                child: Text(_isOn ? 'Apagar' : 'Encender'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```
