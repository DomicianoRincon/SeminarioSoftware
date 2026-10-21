# Ciclo de vida: initState, dispose y TextEditingController

<!-- tags: initState, dispose, TextEditingController, leer el texto de un TextField, ciclo de vida de un State, controller.text, liberar el controller, setState() called after dispose(), mounted, late -->

En la lección de `TextField` los campos se dejaban escribir, pero la app no podía leer lo escrito. Para leerlo hace falta un `TextEditingController`, y ese controller tiene que nacer y morir junto con la pantalla. Para eso el State tiene dos métodos: `initState` y `dispose`.

## La vida de un State

Un objeto State nace una vez, se dibuja muchas veces y muere una vez. Sigue los pasos: a la izquierda la pantalla, a la derecha la fase en la que va.

```svg
<svg id="lcVida" data-steps="6" data-step-seconds="4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 580" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="lcVida-ttl lcVida-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="lcVida-ttl">La vida de un objeto State</title>
  <desc id="lcVida-dsc">Animación en seis pasos. A la izquierda, un celular; a la derecha, las cinco fases del ciclo de vida de _GreetingScreenState. Uno: al pulsar Abrir saludo, Flutter llama a createState. Dos: initState crea el TextEditingController, todavía sin dibujar nada. Tres: build dibuja el campo vacío y el saludo Hola. Cuatro: se escribe Ana, se pulsa Saludar y setState pide otro build. Cinco: build corre otra vez y el saludo dice Hola, Ana. Seis: se vuelve a Inicio, dispose corre una vez y libera el controller.</desc>
  <defs>
    <style>
      #lcVida .title{fill:#161A26;font-size:22px;font-weight:700}
      #lcVida .sub{fill:#79809A;font-size:13.5px}
      #lcVida .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #lcVida .nt{font-size:15px;font-weight:700;fill:#161A26}
      #lcVida .nb{fill:#454C61;font-size:13px}
      #lcVida .lbl{fill:#556074;font-size:12px;font-weight:600}
      #lcVida .foot{fill:#79809A;font-size:12px}
      #lcVida .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #lcVida .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#lcVida-arrow)}
      #lcVida .an{opacity:0;animation-duration:24s;animation-iteration-count:infinite;animation-timing-function:linear}
      #lcVida .ph{animation-name:lcVida-ph}
      @keyframes lcVida-ph{0%{opacity:1} 1.0%{opacity:1} 15.67%{opacity:1} 16.67%{opacity:0} 83.33%{opacity:0} 84.33%{opacity:1} 99.0%{opacity:1} 100%{opacity:1}}
      #lcVida .t1{animation-name:lcVida-t1}
      @keyframes lcVida-t1{0%{opacity:1} 1.0%{opacity:1} 15.67%{opacity:1} 16.67%{opacity:0} 100%{opacity:0}}
      #lcVida .pb{animation-name:lcVida-pb}
      @keyframes lcVida-pb{0%{opacity:0} 16.67%{opacity:0} 17.67%{opacity:1} 32.33%{opacity:1} 33.33%{opacity:0} 100%{opacity:0}}
      #lcVida .pc{animation-name:lcVida-pc}
      @keyframes lcVida-pc{0%{opacity:0} 33.33%{opacity:0} 34.33%{opacity:1} 49.0%{opacity:1} 50.0%{opacity:0} 100%{opacity:0}}
      #lcVida .pd{animation-name:lcVida-pd}
      @keyframes lcVida-pd{0%{opacity:0} 50.0%{opacity:0} 51.0%{opacity:1} 65.67%{opacity:1} 66.67%{opacity:0} 100%{opacity:0}}
      #lcVida .pe{animation-name:lcVida-pe}
      @keyframes lcVida-pe{0%{opacity:0} 66.67%{opacity:0} 67.67%{opacity:1} 82.33%{opacity:1} 83.33%{opacity:0} 100%{opacity:0}}
      #lcVida .r0{animation-name:lcVida-r0}
      @keyframes lcVida-r0{0%{opacity:1} 1.0%{opacity:1} 15.67%{opacity:1} 16.67%{opacity:0} 100%{opacity:0}}
      #lcVida .r1{animation-name:lcVida-r1}
      @keyframes lcVida-r1{0%{opacity:0} 16.67%{opacity:0} 17.67%{opacity:1} 32.33%{opacity:1} 33.33%{opacity:0} 100%{opacity:0}}
      #lcVida .r2{animation-name:lcVida-r2}
      @keyframes lcVida-r2{0%{opacity:0} 33.33%{opacity:0} 34.33%{opacity:1} 49.0%{opacity:1} 50.0%{opacity:0} 66.67%{opacity:0} 67.67%{opacity:1} 82.33%{opacity:1} 83.33%{opacity:0} 100%{opacity:0}}
      #lcVida .r3{animation-name:lcVida-r3}
      @keyframes lcVida-r3{0%{opacity:0} 50.0%{opacity:0} 51.0%{opacity:1} 65.67%{opacity:1} 66.67%{opacity:0} 100%{opacity:0}}
      #lcVida .r4{animation-name:lcVida-r4}
      @keyframes lcVida-r4{0%{opacity:0} 83.33%{opacity:0} 84.33%{opacity:1} 99.0%{opacity:1} 100%{opacity:1}}
      #lcVida .b1{animation-name:lcVida-b1}
      @keyframes lcVida-b1{0%{opacity:0} 33.33%{opacity:0} 34.33%{opacity:1} 49.0%{opacity:1} 50.0%{opacity:0} 51.0%{opacity:1} 65.67%{opacity:1} 66.67%{opacity:0} 100%{opacity:0}}
      #lcVida .b2{animation-name:lcVida-b2}
      @keyframes lcVida-b2{0%{opacity:0} 66.67%{opacity:0} 67.67%{opacity:1} 82.33%{opacity:1} 83.33%{opacity:0} 84.33%{opacity:1} 99.0%{opacity:1} 100%{opacity:1}}
      #lcVida .x1{animation-name:lcVida-x1}
      @keyframes lcVida-x1{0%{opacity:1} 1.0%{opacity:1} 15.67%{opacity:1} 16.67%{opacity:0} 100%{opacity:0}}
      #lcVida .x2{animation-name:lcVida-x2}
      @keyframes lcVida-x2{0%{opacity:0} 16.67%{opacity:0} 17.67%{opacity:1} 32.33%{opacity:1} 33.33%{opacity:0} 100%{opacity:0}}
      #lcVida .x3{animation-name:lcVida-x3}
      @keyframes lcVida-x3{0%{opacity:0} 33.33%{opacity:0} 34.33%{opacity:1} 49.0%{opacity:1} 50.0%{opacity:0} 100%{opacity:0}}
      #lcVida .x4{animation-name:lcVida-x4}
      @keyframes lcVida-x4{0%{opacity:0} 50.0%{opacity:0} 51.0%{opacity:1} 65.67%{opacity:1} 66.67%{opacity:0} 100%{opacity:0}}
      #lcVida .x5{animation-name:lcVida-x5}
      @keyframes lcVida-x5{0%{opacity:0} 66.67%{opacity:0} 67.67%{opacity:1} 82.33%{opacity:1} 83.33%{opacity:0} 100%{opacity:0}}
      #lcVida .x6{animation-name:lcVida-x6}
      @keyframes lcVida-x6{0%{opacity:0} 83.33%{opacity:0} 84.33%{opacity:1} 99.0%{opacity:1} 100%{opacity:1}}
      #lcVida .c0{animation-name:lcVida-c0}
      @keyframes lcVida-c0{0%{opacity:1} 1.0%{opacity:1} 15.67%{opacity:1} 16.67%{opacity:0} 100%{opacity:0}}
      #lcVida .c1{animation-name:lcVida-c1}
      @keyframes lcVida-c1{0%{opacity:0} 16.67%{opacity:0} 17.67%{opacity:1} 32.33%{opacity:1} 33.33%{opacity:0} 34.33%{opacity:1} 49.0%{opacity:1} 50.0%{opacity:0} 51.0%{opacity:1} 65.67%{opacity:1} 66.67%{opacity:0} 67.67%{opacity:1} 82.33%{opacity:1} 83.33%{opacity:0} 100%{opacity:0}}
      #lcVida .c2{animation-name:lcVida-c2}
      @keyframes lcVida-c2{0%{opacity:0} 83.33%{opacity:0} 84.33%{opacity:1} 99.0%{opacity:1} 100%{opacity:1}}
      @media (prefers-reduced-motion: reduce){#lcVida .an{animation:none}}
    </style>
    <marker id="lcVida-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="580" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La vida de un objeto <tspan class="mono">State</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Nace una vez, se dibuja muchas veces y muere una vez. El controller vive lo mismo que el State.</text>
  <rect x="64" y="112" width="208" height="444" rx="30" fill="#1F2430"/>
  <rect x="74" y="122" width="188" height="424" rx="22" fill="#FEF7FF"/>
  <text x="92" y="142" font-size="11" font-weight="600" fill="#161A26" text-anchor="start">9:41</text><text x="244" y="142" font-size="11" font-weight="600" fill="#161A26" text-anchor="end">5G</text>
  <rect x="74" y="150" width="188" height="46" fill="#D0BCFF"/>
  <g class="an ph"><text x="90" y="179" font-size="17" font-weight="600" fill="#1C1B1F" text-anchor="start">Inicio</text><text x="168" y="300" font-size="13" font-weight="400" fill="#49454F" text-anchor="middle">Pantalla de inicio</text><rect x="108" y="318" width="120" height="38" rx="19" fill="#6750A4"/><text x="168" y="342" font-size="13" font-weight="600" fill="#FFFFFF" text-anchor="middle">Abrir saludo</text></g>
  <g class="an t1"><circle cx="220" cy="352" r="12" fill="#F2C069" fill-opacity=".45" stroke="#A96C05" stroke-width="2"/><circle cx="220" cy="352" r="3.5" fill="#A96C05"/></g>
  <g class="an pb"><path d="M98,173 H86 M91,168 L86,173 L91,178" fill="none" stroke="#1C1B1F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="106" y="179" font-size="17" font-weight="600" fill="#1C1B1F" text-anchor="start">Saludo</text><text x="168" y="300" font-size="12" font-weight="400" fill="#9E9AA7" text-anchor="middle">build() todavía no corre:</text><text x="168" y="318" font-size="12" font-weight="400" fill="#9E9AA7" text-anchor="middle">no hay nada que mostrar</text></g>
  <g class="an pc"><path d="M98,173 H86 M91,168 L86,173 L91,178" fill="none" stroke="#1C1B1F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="106" y="179" font-size="17" font-weight="600" fill="#1C1B1F" text-anchor="start">Saludo</text><text x="90" y="224" font-size="11" font-weight="400" fill="#49454F" text-anchor="start">Nombre</text><rect x="88" y="230" width="160" height="38" rx="4" fill="none" stroke="#79747E" stroke-width="1.2"/><text x="98" y="254" font-size="13" font-weight="400" fill="#9E9AA7" text-anchor="start">Escribe tu nombre</text><text x="90" y="308" font-size="22" font-weight="400" fill="#1C1B1F" text-anchor="start">Hola</text><rect x="88" y="326" width="104" height="38" rx="19" fill="#6750A4"/><text x="140" y="350" font-size="13" font-weight="600" fill="#FFFFFF" text-anchor="middle">Saludar</text></g>
  <g class="an pd"><path d="M98,173 H86 M91,168 L86,173 L91,178" fill="none" stroke="#1C1B1F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="106" y="179" font-size="17" font-weight="600" fill="#1C1B1F" text-anchor="start">Saludo</text><text x="90" y="224" font-size="11" font-weight="400" fill="#49454F" text-anchor="start">Nombre</text><rect x="88" y="230" width="160" height="38" rx="4" fill="none" stroke="#79747E" stroke-width="1.2"/><text x="98" y="254" font-size="14" font-weight="400" fill="#1C1B1F" text-anchor="start">Ana</text><text x="90" y="308" font-size="22" font-weight="400" fill="#1C1B1F" text-anchor="start">Hola</text><rect x="88" y="326" width="104" height="38" rx="19" fill="#6750A4"/><text x="140" y="350" font-size="13" font-weight="600" fill="#FFFFFF" text-anchor="middle">Saludar</text><circle cx="186" cy="360" r="12" fill="#F2C069" fill-opacity=".45" stroke="#A96C05" stroke-width="2"/><circle cx="186" cy="360" r="3.5" fill="#A96C05"/></g>
  <g class="an pe"><path d="M98,173 H86 M91,168 L86,173 L91,178" fill="none" stroke="#1C1B1F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="106" y="179" font-size="17" font-weight="600" fill="#1C1B1F" text-anchor="start">Saludo</text><text x="90" y="224" font-size="11" font-weight="400" fill="#49454F" text-anchor="start">Nombre</text><rect x="88" y="230" width="160" height="38" rx="4" fill="none" stroke="#79747E" stroke-width="1.2"/><text x="98" y="254" font-size="14" font-weight="400" fill="#1C1B1F" text-anchor="start">Ana</text><text x="90" y="308" font-size="22" font-weight="400" fill="#1C1B1F" text-anchor="start">Hola, Ana</text><rect x="88" y="326" width="104" height="38" rx="19" fill="#6750A4"/><text x="140" y="350" font-size="13" font-weight="600" fill="#FFFFFF" text-anchor="middle">Saludar</text></g>
  <text class="h" x="320" y="124">CICLO DE VIDA DE _GreetingScreenState</text>
  <rect x="320" y="140" width="592" height="56" rx="12" fill="#FFFFFF" stroke="#E3E6EE" stroke-width="1.5"/>
  <g class="an r0"><rect x="320" y="140" width="592" height="56" rx="12" fill="#FFF3DC" stroke="#A96C05" stroke-width="2.5"/></g>
  <circle cx="346" cy="168" r="10" fill="#FFF3DC" stroke="#A96C05" stroke-width="2.5"/>
  <text x="368" y="164" font-size="15" font-weight="700" fill="#A96C05" text-anchor="start" class="mono">createState</text>
  <text x="368" y="184" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">Flutter crea el objeto State</text>
  <text x="896" y="173" font-size="12" font-weight="600" fill="#79809A" text-anchor="end">una vez</text>
  <rect x="320" y="206" width="592" height="56" rx="12" fill="#FFFFFF" stroke="#E3E6EE" stroke-width="1.5"/>
  <g class="an r1"><rect x="320" y="206" width="592" height="56" rx="12" fill="#E8F6E3" stroke="#3A8235" stroke-width="2.5"/></g>
  <circle cx="346" cy="234" r="10" fill="#E8F6E3" stroke="#3A8235" stroke-width="2.5"/>
  <text x="368" y="230" font-size="15" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">initState</text>
  <text x="368" y="250" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">Prepara lo que el State necesita</text>
  <text x="896" y="239" font-size="12" font-weight="600" fill="#79809A" text-anchor="end">una vez</text>
  <rect x="320" y="272" width="592" height="56" rx="12" fill="#FFFFFF" stroke="#E3E6EE" stroke-width="1.5"/>
  <g class="an r2"><rect x="320" y="272" width="592" height="56" rx="12" fill="#EEF1FF" stroke="#4453C9" stroke-width="2.5"/></g>
  <circle cx="346" cy="300" r="10" fill="#EEF1FF" stroke="#4453C9" stroke-width="2.5"/>
  <text x="368" y="296" font-size="15" font-weight="700" fill="#4453C9" text-anchor="start" class="mono">build</text>
  <text x="368" y="316" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">Dibuja con los datos actuales</text>
  <text x="896" y="305" font-size="12" font-weight="600" fill="#79809A" text-anchor="end">muchas veces</text>
  <rect x="320" y="338" width="592" height="56" rx="12" fill="#FFFFFF" stroke="#E3E6EE" stroke-width="1.5"/>
  <g class="an r3"><rect x="320" y="338" width="592" height="56" rx="12" fill="#F4EBFF" stroke="#7439B8" stroke-width="2.5"/></g>
  <circle cx="346" cy="366" r="10" fill="#F4EBFF" stroke="#7439B8" stroke-width="2.5"/>
  <text x="368" y="362" font-size="15" font-weight="700" fill="#7439B8" text-anchor="start" class="mono">setState</text>
  <text x="368" y="382" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">Cambia un dato y pide otro build</text>
  <text x="896" y="371" font-size="12" font-weight="600" fill="#79809A" text-anchor="end">muchas veces</text>
  <rect x="320" y="404" width="592" height="56" rx="12" fill="#FFFFFF" stroke="#E3E6EE" stroke-width="1.5"/>
  <g class="an r4"><rect x="320" y="404" width="592" height="56" rx="12" fill="#FFEBEF" stroke="#C2354F" stroke-width="2.5"/></g>
  <circle cx="346" cy="432" r="10" fill="#FFEBEF" stroke="#C2354F" stroke-width="2.5"/>
  <text x="368" y="428" font-size="15" font-weight="700" fill="#C2354F" text-anchor="start" class="mono">dispose</text>
  <text x="368" y="448" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">Libera lo creado en initState</text>
  <text x="896" y="437" font-size="12" font-weight="600" fill="#79809A" text-anchor="end">una vez</text>
  <path class="link" d="M318,366 C292,366 292,300 316,300"/>
  <g class="an b1"><text x="790" y="305" font-size="12" font-weight="700" fill="#4453C9" text-anchor="end" class="mono">build #1</text></g>
  <g class="an b2"><text x="790" y="305" font-size="12" font-weight="700" fill="#4453C9" text-anchor="end" class="mono">build #2</text></g>
  <rect x="320" y="482" width="592" height="74" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <g class="an x1"><circle cx="348" cy="508" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="348" y="512.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle">1</text><text x="372" y="513" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">Pulsas Abrir saludo: Navigator crea GreetingScreen</text><text x="372" y="533" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">y Flutter llama a createState(). Nace el State #1.</text></g>
  <g class="an x2"><circle cx="348" cy="508" r="13" fill="#FFFFFF" stroke="#3A8235" stroke-width="2"/><text x="348" y="512.5" font-size="13" font-weight="700" fill="#3A8235" text-anchor="middle">2</text><text x="372" y="513" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">initState() corre una sola vez, antes de dibujar nada.</text><text x="372" y="533" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">Aquí se crea _nameController.</text></g>
  <g class="an x3"><circle cx="348" cy="508" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="348" y="512.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle">3</text><text x="372" y="513" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">build() dibuja la pantalla con los datos actuales:</text><text x="372" y="533" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">el campo vacío y el saludo Hola.</text></g>
  <g class="an x4"><circle cx="348" cy="508" r="13" fill="#FFFFFF" stroke="#7439B8" stroke-width="2"/><text x="348" y="512.5" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle">4</text><text x="372" y="513" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">Escribes Ana y pulsas Saludar: _greet() cambia</text><text x="372" y="533" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">_greeting dentro de setState y pide otro build().</text></g>
  <g class="an x5"><circle cx="348" cy="508" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="348" y="512.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle">5</text><text x="372" y="513" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">build() corre otra vez, con el mismo State #1:</text><text x="372" y="533" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">ahora el Text muestra Hola, Ana.</text></g>
  <g class="an x6"><circle cx="348" cy="508" r="13" fill="#FFFFFF" stroke="#C2354F" stroke-width="2"/><text x="348" y="512.5" font-size="13" font-weight="700" fill="#C2354F" text-anchor="middle">6</text><text x="372" y="513" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">Vuelves a Inicio y la pantalla se va para siempre:</text><text x="372" y="533" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="400">dispose() corre una vez y libera _nameController.</text></g>
  <text x="896" y="508" font-size="12" font-weight="700" fill="#161A26" text-anchor="end" class="mono">_nameController</text>
  <g class="an c0"><text x="896" y="532" font-size="12.5" font-weight="600" fill="#79809A" text-anchor="end">no existe</text></g>
  <g class="an c1"><text x="896" y="532" font-size="12.5" font-weight="700" fill="#3A8235" text-anchor="end">vivo</text></g>
  <g class="an c2"><text x="896" y="532" font-size="12.5" font-weight="700" fill="#C2354F" text-anchor="end">liberado</text></g>
</svg>
```

- **`initState`** corre una sola vez, antes del primer `build`. Ahí se crea lo que el State necesita.
- **`build`** corre cada vez que algo pide reconstruir, como `setState`.
- **`dispose`** corre una sola vez, cuando la pantalla se va. Ahí se libera lo que se creó en `initState`.

## El TextEditingController

El controller es el objeto que guarda el texto de un campo. Se crea en `initState`, se conecta al `TextField` y se libera en `dispose`:

```dart
class _GreetingScreenState extends State<GreetingScreen> {
  late TextEditingController _nameController;

  @override
  void initState() {
    super.initState();
    _nameController = TextEditingController();
  }

  @override
  Widget build(BuildContext context) {
    return TextField(controller: _nameController);
  }

  @override
  void dispose() {
    _nameController.dispose();
    super.dispose();
  }
}
```

- `late` le dice a Dart que el campo tendrá valor antes de usarse, aunque no se le dé en la declaración. Se lo damos en `initState`.
- En `initState`, `super.initState()` va **primero**. En `dispose`, `super.dispose()` va **al final**.
- Para leer lo escrito: `_nameController.text`. Para borrarlo: `_nameController.clear()`.

Si no se llama `_nameController.dispose()`, el controller queda ocupando memoria aunque la pantalla ya no exista. Por eso la regla del curso es: **todo componente con un campo de texto es un `StatefulWidget` dueño de su controller, con su `dispose`**.

## Leer el texto con un botón

Lo más común es leer el campo cuando se pulsa un botón. El valor se copia a un campo del State dentro de `setState`, para que la pantalla lo muestre:

```dart
String _greeting = 'Hola';

void _greet() {
  setState(() {
    _greeting = 'Hola, ${_nameController.text}';
  });
}
```

```dart
FilledButton(
  onPressed: () => _greet(),
  child: const Text('Saludar'),
),
Text(_greeting),
```

## setState() called after dispose()

Si algo tarda (una espera, una descarga, una consulta) y el usuario se va de la pantalla antes de que termine, el `setState` del final llega a un State que ya pasó por `dispose`. La consola muestra:

```text
setState() called after dispose(): _GreetingScreenState#…
```

La salida es preguntar antes si el State sigue montado:

```dart
if (!mounted) return;
setState(() {
  _saved = true;
});
```

Con los servicios de las sesiones 11 a 14 lo vas a ver seguido.

## Ejemplo completo

Una pantalla que pide un nombre y saluda al pulsar el botón, con el controller creado en `initState` y liberado en `dispose`.

```dart trycode=03a91a720d6158b2fc3f377b71a7c2ca
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
        '/': (context) => const GreetingScreen(),
      },
    );
  }
}

/// Screen that greets the name typed in the field.
class GreetingScreen extends StatefulWidget {
  const GreetingScreen({super.key});

  @override
  State<GreetingScreen> createState() => _GreetingScreenState();
}

class _GreetingScreenState extends State<GreetingScreen> {
  late TextEditingController _nameController;
  String _greeting = 'Hola';

  @override
  void initState() {
    super.initState();
    _nameController = TextEditingController();
  }

  void _greet() {
    setState(() {
      _greeting = 'Hola, ${_nameController.text}';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Saludo')),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextField(
                controller: _nameController,
                decoration: const InputDecoration(
                  labelText: 'Nombre',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 12),
              FilledButton(
                onPressed: () => _greet(),
                child: const Text('Saludar'),
              ),
              const SizedBox(height: 24),
              Text(_greeting, style: const TextStyle(fontSize: 24)),
            ],
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _nameController.dispose();
    super.dispose();
  }
}
```
