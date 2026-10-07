# SafeArea

<!-- tags: SafeArea, contenido tapado por la cámara, notch, barra de estado, barra de gestos, pantalla sin AppBar, zona segura, texto debajo de la hora, SafeArea no hace nada en Chrome, botón tapado abajo -->

Un `Scaffold` ocupa la pantalla entera, de borde a borde. El problema es que en un teléfono los bordes no son tuyos.

## La pantalla no es toda tuya

```svg
<svg id="saZonas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="saZonas-ttl saZonas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="saZonas-ttl">La pantalla no es toda tuya</title>
  <desc id="saZonas-dsc">Un celular con tres zonas marcadas. Arriba, la barra de estado con la hora, la batería y el recorte de la cámara. Abajo, la barra de gestos. En medio, la zona segura, donde todo se ve y se puede tocar.</desc>
  <defs>
    <style>
      #saZonas .title{fill:#161A26;font-size:22px;font-weight:700}
      #saZonas .sub{fill:#79809A;font-size:13.5px}
      #saZonas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #saZonas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #saZonas .nb{fill:#454C61;font-size:13px}
      #saZonas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #saZonas .foot{fill:#79809A;font-size:12px}
      #saZonas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #saZonas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#saZonas-arrow)}
    </style>
    <marker id="saZonas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="540" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La pantalla no es toda tuya</text>
  <text class="sub" x="48" y="80" data-fit="860">El sistema dibuja encima de la app en los bordes. Lo que pongas ahí queda tapado.</text>
  <clipPath id="saZonas-a"><rect width="220" height="344" rx="20"/></clipPath><rect x="129" y="125" width="234" height="358" rx="27" fill="#1F2430"/><g transform="translate(136,132)"><g clip-path="url(#saZonas-a)"><rect width="220" height="344" rx="20" fill="#FFFFFF"/><rect y="0" width="220" height="36" fill="#C2354F" fill-opacity=".13"/><rect y="36" width="220" height="284" fill="#3A8235" fill-opacity=".13"/><rect y="320" width="220" height="24" fill="#C2354F" fill-opacity=".13"/><path d="M0,36 H220 M0,320 H220" stroke="#FFFFFF" stroke-width="2"/><text x="110.0" y="177.0" font-size="15" font-weight="700" fill="#3A8235" text-anchor="middle">Zona segura</text><text x="16" y="22" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start">9:41</text><rect x="78.0" y="7" width="64" height="18" rx="9" fill="#1F2430"/><rect x="182" y="11" width="22" height="11" rx="3" fill="none" stroke="#161A26" stroke-width="1.5"/><rect x="184" y="13" width="13" height="7" rx="1.5" fill="#161A26"/><rect x="74.0" y="332" width="72" height="5" rx="2.5" fill="#1F2430"/></g></g>
  <path d="M366,150 H432" stroke="#C2354F" stroke-width="1.75"/><circle cx="366" cy="150" r="3.5" fill="#C2354F"/>
  <text x="448" y="146" font-size="15" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="440">Barra de estado y cámara</text>
  <text x="448" y="167" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="440">La hora, la batería y el recorte de la cámara.</text>
  <path d="M366,304 H432" stroke="#3A8235" stroke-width="1.75"/><circle cx="366" cy="304" r="3.5" fill="#3A8235"/>
  <text x="448" y="300" font-size="15" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="440">Zona segura</text>
  <text x="448" y="321" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="440">Aquí todo se ve completo y se puede tocar.</text>
  <path d="M366,464 H432" stroke="#C2354F" stroke-width="1.75"/><circle cx="366" cy="464" r="3.5" fill="#C2354F"/>
  <text x="448" y="460" font-size="15" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="440">Barra de gestos</text>
  <text x="448" y="481" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="440">La raya para volver al inicio del teléfono.</text>
  <text x="448" y="238" font-size="13" font-weight="400" fill="#79809A" text-anchor="start" data-fit="440">Las esquinas redondeadas también recortan.</text>
</svg>
```

El sistema dibuja encima de tu app la hora, la batería y la barra de gestos, y el propio teléfono recorta la pantalla con la cámara y las esquinas. Lo que tu app ponga en esas zonas se pinta igual, pero queda tapado.

Cada teléfono tiene zonas de distinto tamaño, así que no sirve dejar un espacio fijo arriba. `SafeArea` le pregunta al teléfono cuánto miden y aparta el contenido justo esa distancia.

## Cuándo hace falta

```svg
<svg id="saCasos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 556" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="saCasos-ttl saCasos-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="saCasos-ttl">Tres pantallas con el mismo contenido</title>
  <desc id="saCasos-dsc">Tres celulares con un título arriba y un botón abajo. En el primero, sin AppBar ni SafeArea, la cámara tapa el título y la barra de gestos queda encima del botón. En el segundo, con AppBar, el título ya se ve pero el botón sigue tapado. En el tercero, con SafeArea, todo queda dentro de la zona segura.</desc>
  <defs>
    <style>
      #saCasos .title{fill:#161A26;font-size:22px;font-weight:700}
      #saCasos .sub{fill:#79809A;font-size:13.5px}
      #saCasos .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #saCasos .nt{font-size:15px;font-weight:700;fill:#161A26}
      #saCasos .nb{fill:#454C61;font-size:13px}
      #saCasos .lbl{fill:#556074;font-size:12px;font-weight:600}
      #saCasos .foot{fill:#79809A;font-size:12px}
      #saCasos .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #saCasos .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#saCasos-arrow)}
    </style>
    <marker id="saCasos-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="556" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Tres pantallas con el mismo contenido</text>
  <text class="sub" x="48" y="80" data-fit="860">Un título arriba y un botón abajo. Lo que cambia es qué los protege de los bordes.</text>
  <clipPath id="saCasos-0"><rect width="200" height="300" rx="20"/></clipPath><rect x="73" y="125" width="214" height="314" rx="27" fill="#1F2430"/><g transform="translate(80,132)"><g clip-path="url(#saCasos-0)"><rect width="200" height="300" rx="20" fill="#FFFFFF"/><text x="100.0" y="26" font-size="20" font-weight="700" fill="#161A26" text-anchor="middle">Bienvenido</text><text x="100.0" y="48" font-size="12" font-weight="400" fill="#556074" text-anchor="middle">Inicia sesión para continuar</text><rect x="16" y="260" width="168" height="40" rx="20" fill="#2196F3"/><text x="100.0" y="285" font-size="14" font-weight="600" fill="#FFFFFF" text-anchor="middle">Entrar</text><text x="16" y="22" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start">9:41</text><rect x="68.0" y="7" width="64" height="18" rx="9" fill="#1F2430"/><rect x="162" y="11" width="22" height="11" rx="3" fill="none" stroke="#161A26" stroke-width="1.5"/><rect x="164" y="13" width="13" height="7" rx="1.5" fill="#161A26"/><rect x="64.0" y="288" width="72" height="5" rx="2.5" fill="#1F2430"/></g></g>
  <text x="180.0" y="476" font-size="15" font-weight="700" fill="#C2354F" text-anchor="middle" data-fit="280">Sin AppBar ni SafeArea</text>
  <text x="180.0" y="498" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">La cámara tapa el título</text>
  <text x="180.0" y="516" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">y los gestos, el botón.</text>
  <clipPath id="saCasos-1"><rect width="200" height="300" rx="20"/></clipPath><rect x="373" y="125" width="214" height="314" rx="27" fill="#1F2430"/><g transform="translate(380,132)"><g clip-path="url(#saCasos-1)"><rect width="200" height="300" rx="20" fill="#FFFFFF"/><rect width="200" height="80" fill="#F1ECF8"/><text x="16" y="64" font-size="15" font-weight="500" fill="#161A26" text-anchor="start">Inicio</text><text x="100.0" y="106" font-size="20" font-weight="700" fill="#161A26" text-anchor="middle">Bienvenido</text><text x="100.0" y="128" font-size="12" font-weight="400" fill="#556074" text-anchor="middle">Inicia sesión para continuar</text><rect x="16" y="260" width="168" height="40" rx="20" fill="#2196F3"/><text x="100.0" y="285" font-size="14" font-weight="600" fill="#FFFFFF" text-anchor="middle">Entrar</text><text x="16" y="22" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start">9:41</text><rect x="68.0" y="7" width="64" height="18" rx="9" fill="#1F2430"/><rect x="162" y="11" width="22" height="11" rx="3" fill="none" stroke="#161A26" stroke-width="1.5"/><rect x="164" y="13" width="13" height="7" rx="1.5" fill="#161A26"/><rect x="64.0" y="288" width="72" height="5" rx="2.5" fill="#1F2430"/></g></g>
  <text x="480.0" y="476" font-size="15" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="280">Con AppBar</text>
  <text x="480.0" y="498" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">Arriba ya está resuelto.</text>
  <text x="480.0" y="516" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">El botón sigue tapado.</text>
  <clipPath id="saCasos-2"><rect width="200" height="300" rx="20"/></clipPath><rect x="673" y="125" width="214" height="314" rx="27" fill="#1F2430"/><g transform="translate(680,132)"><g clip-path="url(#saCasos-2)"><rect width="200" height="300" rx="20" fill="#FFFFFF"/><text x="100.0" y="62" font-size="20" font-weight="700" fill="#161A26" text-anchor="middle">Bienvenido</text><text x="100.0" y="84" font-size="12" font-weight="400" fill="#556074" text-anchor="middle">Inicia sesión para continuar</text><rect x="16" y="236" width="168" height="40" rx="20" fill="#2196F3"/><text x="100.0" y="261" font-size="14" font-weight="600" fill="#FFFFFF" text-anchor="middle">Entrar</text><text x="16" y="22" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start">9:41</text><rect x="68.0" y="7" width="64" height="18" rx="9" fill="#1F2430"/><rect x="162" y="11" width="22" height="11" rx="3" fill="none" stroke="#161A26" stroke-width="1.5"/><rect x="164" y="13" width="13" height="7" rx="1.5" fill="#161A26"/><rect x="64.0" y="288" width="72" height="5" rx="2.5" fill="#1F2430"/></g></g>
  <text x="780.0" y="476" font-size="15" font-weight="700" fill="#3A8235" text-anchor="middle" data-fit="280">Con SafeArea</text>
  <text x="780.0" y="498" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">Todo queda dentro</text>
  <text x="780.0" y="516" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" data-fit="280">de la zona segura.</text>
</svg>
```

Un `AppBar` ya sabe de la barra de estado: se estira hasta el borde y pone su título más abajo. Por eso en las pantallas con barra el problema de arriba no se nota. El de abajo sigue ahí, y en una pantalla sin barra aparecen los dos.

La regla del curso es corta: **el `body` de toda Screen empieza con un `SafeArea`**. Si la pantalla tiene `AppBar`, cuida el borde de abajo. Si no la tiene, cuida los dos.

## Cómo se usa

`SafeArea` tiene un solo `child`: todo el contenido de la pantalla.

```svg
<svg id="saCodigo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 600" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="saCodigo-ttl saCodigo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="saCodigo-ttl">SafeArea envuelve el contenido</title>
  <desc id="saCodigo-dsc">Un Scaffold sin appBar cuyo body es un SafeArea con una Column adentro. En el resultado, el contenido empieza debajo de la barra de estado y termina antes de la barra de gestos.</desc>
  <defs>
    <style>
      #saCodigo .title{fill:#161A26;font-size:22px;font-weight:700}
      #saCodigo .sub{fill:#79809A;font-size:13.5px}
      #saCodigo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #saCodigo .cl{font-size:13px;fill:#C9CFDA}
      #saCodigo .s{fill:#A8D8A0} #saCodigo .n{fill:#F2B880} #saCodigo .c{fill:#7FD1E8}
      #saCodigo .p{fill:#D5B8F5} #saCodigo .k{fill:#F08FB0}
      #saCodigo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #saCodigo .ct{fill:#161A26;font-size:14px;font-weight:700}
      #saCodigo .cb{fill:#454C61;font-size:13px}
      #saCodigo .rt{fill:#161A26;font-size:14px} #saCodigo .rs{fill:#79809A;font-size:12px}
      #saCodigo .foot{fill:#79809A;font-size:12px}
      #saCodigo .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #saCodigo .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #saCodigo .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#saCodigo-ar-green)}
    </style>
    <marker id="saCodigo-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
  </defs>
  <rect width="960" height="600" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56"><tspan class="mono">SafeArea</tspan> envuelve el contenido</text>
  <text class="sub" x="48" y="80" data-fit="860">Va en el body, alrededor de todo lo demás. Deja libres los bordes que ocupa el sistema.</text>
  <rect x="48" y="112" width="456" height="456" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/login_screen.dart</text>
  <rect x="552" y="112" width="360" height="456" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-green" x="126.4" y="180" width="70.4" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="171.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="k">const</tspan> <tspan class="c">Scaffold</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="117.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">body</tspan>: <tspan class="c">SafeArea</tspan>(</text>
  <text class="cl mono" font-size="13" x="99.2" y="220" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">child</tspan>: <tspan class="c">Column</tspan>(</text>
  <text class="cl mono" font-size="13" x="114.8" y="244" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">children</tspan>: [</text>
  <text class="cl mono" font-size="13" x="130.4" y="268" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(<tspan class="s">'Bienvenido'</tspan>),</text>
  <text class="cl mono" font-size="13" x="130.4" y="292" textLength="288.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(<tspan class="s">'Inicia sesión para continuar'</tspan>),</text>
  <text class="cl mono" font-size="13" x="114.8" y="316" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="99.2" y="340" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="83.6" y="364" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">),</text>
  <text class="cl mono" font-size="13" x="68.0" y="388" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">);</text>
  <g transform="translate(552,144)">
<rect x="78" y="22" width="204" height="380" rx="26" fill="#FFFFFF" stroke="#2A3040" stroke-width="3"/><clipPath id="saCodigo-scr"><rect width="204" height="380" rx="26"/></clipPath><g transform="translate(78,22)" clip-path="url(#saCodigo-scr)"><rect y="0" width="204" height="36" fill="#C2354F" fill-opacity=".13"/><rect y="356" width="204" height="24" fill="#C2354F" fill-opacity=".13"/><text x="102.0" y="82" font-size="20" font-weight="700" fill="#161A26" text-anchor="middle">Bienvenido</text><text x="102.0" y="106" font-size="12" font-weight="400" fill="#556074" text-anchor="middle">Inicia sesión para continuar</text><text x="16" y="22" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start">9:41</text><rect x="70.0" y="7" width="64" height="18" rx="9" fill="#1F2430"/><rect x="166" y="11" width="22" height="11" rx="3" fill="none" stroke="#161A26" stroke-width="1.5"/><rect x="168" y="13" width="13" height="7" rx="1.5" fill="#161A26"/><rect x="66.0" y="368" width="72" height="5" rx="2.5" fill="#1F2430"/></g><rect x="78" y="22" width="204" height="380" rx="26" fill="none" stroke="#2A3040" stroke-width="3"/><rect x="84" y="62" width="192" height="312" rx="12" fill="#3A8235" fill-opacity=".08" stroke="#3A8235" stroke-width="2"/>
  </g>
  <path class="ld-green" d="M206.6,191 H504"/>
  <path class="ar-green" d="M504,191 H523 V384 H636"/>
</svg>
```

```dart
return const Scaffold(
  body: SafeArea(
    child: Column(
      children: [
        Text('Bienvenido'),
        Text('Inicia sesión para continuar'),
      ],
    ),
  ),
);
```

Así empieza una pantalla de inicio de sesión. En `ProfileScreen` haz lo mismo ahora: envuelve el `Center` del `body`.

```dart
body: const SafeArea(
  child: Center(
    child: Text('Contenido'),
  ),
),
```

`SafeArea` va **dentro** del `Scaffold`, no alrededor. Si lo pones por fuera, el fondo de la pantalla tampoco llega a los bordes y quedan dos franjas vacías.

## En Chrome no se nota

La ventana de Chrome no tiene cámara ni barra de gestos, así que ahí `SafeArea` no aparta nada y la pantalla se ve igual con él o sin él. No lo quites por eso: el efecto aparece el día que la app corre en un teléfono. Para verlo desde ya, ejecuta la app en un emulador o en tu propio dispositivo, como explica la sección *Instalación avanzada*.

## Ejemplo completo

Una pantalla sin `AppBar`, con el título arriba y el botón abajo. Como el editor en línea tampoco tiene cámara, el bloque `builder` de `App` finge un teléfono con 48 píxeles ocupados arriba y 32 abajo. Ese bloque es solo para esta demostración: en tu proyecto no va.

Quita el `SafeArea` y deja el `Center` como `body`: el título y el botón se pegan a los bordes.

```dart trycode=PENDIENTE_S21
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
      builder: (context, child) {
        return MediaQuery(
          data: MediaQuery.of(context).copyWith(
            padding: const EdgeInsets.only(top: 48, bottom: 32),
          ),
          child: child!,
        );
      },
      initialRoute: '/welcome',
      routes: {'/welcome': (context) => const WelcomeScreen()},
    );
  }
}

/// Welcome screen, without an app bar.
class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text(
                'Bienvenido',
                style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
              ),
              ElevatedButton(
                onPressed: () {
                  print('Entrar');
                },
                child: const Text('Entrar'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

Aquí `App` y `WelcomeScreen` van en un solo archivo porque el editor en línea solo tiene uno; en tu proyecto van separados.
