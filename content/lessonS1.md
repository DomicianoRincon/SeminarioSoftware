# Instalación básica

<!-- tags: extensión Flutter de VS Code, Flutter: New Project, Download SDK, Add SDK to PATH, flutter doctor, Could not find a Flutter SDK, flutter no se reconoce como comando, Git para Windows, Chrome como dispositivo, hot reload, ruta con espacios, Developer Mode -->

Hay dos formas de dejar Flutter listo en tu computador. En esta lección vas a hacer la **básica**: instalas Visual Studio Code, le agregas la extensión de Flutter y es la extensión la que descarga Flutter, lo deja disponible en la terminal y crea tu primer proyecto. Al final vas a tener una app corriendo en **Chrome**, que es todo lo que necesitas para las primeras sesiones.

La otra forma, la **avanzada**, es la que usarás cuando quieras correr tus apps en un emulador de Android, en un celular o en un simulador de iOS. Está en la sección *Instalación avanzada* del temario. No hace falta hacerla hoy, y todo lo que instales aquí te sirve para ella.

```svg
<svg id="fiPiezas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fiPiezas-ttl fiPiezas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fiPiezas-ttl">Las piezas de la instalación básica</title>
  <desc id="fiPiezas-dsc">Tú instalas Git y Visual Studio Code. La extensión de Flutter descarga el Flutter SDK, que incluye Dart, y lo agrega al PATH. Con eso la app corre en Chrome; Android e iOS se configuran en la instalación avanzada.</desc>
  <defs>
    <style>
      #fiPiezas .card{stroke-width:1.5}
      #fiPiezas .hero{stroke-width:2.5;filter:url(#fiPiezas-lift)}
      #fiPiezas .n-indigo{fill:#EEF1FF;stroke:#A9B4F2} #fiPiezas .t-indigo{fill:#4453C9}
      #fiPiezas .n-violet{fill:#F4EBFF;stroke:#C9A6EE} #fiPiezas .t-violet{fill:#7439B8}
      #fiPiezas .n-amber{fill:#FFF3DC;stroke:#F0C572} #fiPiezas .t-amber{fill:#A96C05}
      #fiPiezas .n-green{fill:#E8F6E3;stroke:#9FD68D} #fiPiezas .t-green{fill:#3A8235}
      #fiPiezas .n-slate{fill:#EFF1F5;stroke:#C4CBD8} #fiPiezas .t-slate{fill:#556074}
      #fiPiezas .title{fill:#161A26;font-size:22px;font-weight:700}
      #fiPiezas .sub{fill:#79809A;font-size:13.5px}
      #fiPiezas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #fiPiezas .nt{font-size:16px;font-weight:600}
      #fiPiezas .nb{fill:#454C61;font-size:13px}
      #fiPiezas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fiPiezas .foot{fill:#79809A;font-size:12px}
      #fiPiezas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fiPiezas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fiPiezas-arrow)}
      #fiPiezas .soft{stroke:#A0A8B8;stroke-dasharray:6 5;marker-end:url(#fiPiezas-arrow-soft)}
    </style>
    <marker id="fiPiezas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="fiPiezas-arrow-soft" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A0A8B8"/>
    </marker>
    <filter id="fiPiezas-lift" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#0B1020" flood-opacity="0.14"/>
    </filter>
  </defs>

  <rect width="960" height="560" rx="16" fill="#FBFBFD"/>

  <text class="title" x="48" y="56">Las piezas de la instalación básica</text>
  <text class="sub" x="48" y="80" data-fit="860">Tú instalas dos programas; la extensión de Flutter se encarga del resto.</text>

  <text class="h" x="48" y="120">LO QUE INSTALAS TÚ</text>
  <text class="h" x="344" y="120">LO QUE HACE LA EXTENSIÓN</text>
  <text class="h" x="696" y="120">DÓNDE CORRE TU APP</text>

  <g transform="translate(48,136)">
    <rect class="card n-indigo" width="232" height="80" rx="12"/>
    <text class="nt t-indigo" x="16" y="32" data-fit="200">Visual Studio Code</text>
    <text class="nb" x="16" y="56" data-fit="200">el editor donde vas a trabajar</text>
  </g>
  <g transform="translate(48,248)">
    <rect class="card n-slate" width="232" height="80" rx="12"/>
    <text class="nt t-slate" x="16" y="32" data-fit="200">Git</text>
    <text class="nb" x="16" y="56" data-fit="200">con él se descarga Flutter</text>
  </g>

  <path class="link" d="M280,176 H336"/>
  <text class="lbl" x="308" y="166" text-anchor="middle" data-fit="56">instala</text>

  <g transform="translate(344,136)">
    <rect class="card n-violet" width="288" height="80" rx="12"/>
    <text class="nt t-violet" x="16" y="32" data-fit="256">Extensión Flutter</text>
    <text class="nb" x="16" y="56" data-fit="256">trae también la extensión de Dart</text>
  </g>

  <path class="link" d="M488,216 V256"/>
  <text class="lbl" x="500" y="240" data-fit="120">Download SDK</text>
  <path class="link" d="M280,300 H336"/>
  <text class="lbl" x="308" y="290" text-anchor="middle" data-fit="56">clona</text>

  <g transform="translate(344,264)">
    <rect class="card hero n-indigo" width="288" height="112" rx="12" stroke="#4453C9"/>
    <text class="nt t-indigo" x="16" y="32" data-fit="256">Flutter SDK</text>
    <text class="nb" x="16" y="56" data-fit="256">el comando <tspan class="mono">flutter</tspan> + el Dart SDK</text>
    <text class="nb mono" x="16" y="84" data-fit="256">C:\develop\flutter</text>
    <text class="nb mono" x="16" y="100" font-size="11.5" fill="#79809A" data-fit="256">~/develop/flutter  (Mac/Linux)</text>
  </g>

  <path class="link" d="M488,376 V416"/>
  <text class="lbl" x="500" y="400" data-fit="120">Add SDK to PATH</text>

  <g transform="translate(344,424)">
    <rect class="card n-amber" width="288" height="72" rx="12"/>
    <text class="nt t-amber" x="16" y="30" data-fit="256">PATH del sistema</text>
    <text class="nb" x="16" y="54" data-fit="256"><tspan class="mono">flutter</tspan> funciona en cualquier terminal</text>
  </g>

  <path class="link" d="M632,320 H664 V184 Q664,176 672,176 H688"/>
  <path class="link soft" d="M664,288 H688"/>
  <path class="link soft" d="M664,320 V392 Q664,400 672,400 H688"/>

  <g transform="translate(696,136)">
    <rect class="card n-green" width="216" height="80" rx="12" stroke-width="2"/>
    <text class="nt t-green" x="16" y="32" data-fit="184">Chrome (web)</text>
    <text class="nb" x="16" y="56" data-fit="184">sesión 1: con esto basta</text>
  </g>
  <g transform="translate(696,248)">
    <rect class="card n-slate" width="216" height="80" rx="12" stroke-dasharray="6 5"/>
    <text class="nt t-slate" x="16" y="32" data-fit="184">Android</text>
    <text class="nb" x="16" y="56" data-fit="184">→ Instalación avanzada</text>
  </g>
  <g transform="translate(696,360)">
    <rect class="card n-slate" width="216" height="80" rx="12" stroke-dasharray="6 5"/>
    <text class="nt t-slate" x="16" y="32" data-fit="184">iOS <tspan class="nb">(solo en Mac)</tspan></text>
    <text class="nb" x="16" y="56" data-fit="184">→ Instalación avanzada</text>
  </g>

  <line x1="48" y1="528" x2="80" y2="528" stroke="#A0A8B8" stroke-width="1.75" stroke-dasharray="6 5"/>
  <text class="foot" x="92" y="528" dy="0.35em" data-fit="700">Punteado: no hace falta para la sesión 1. Se configura en la sección Instalación avanzada.</text>
</svg>
```

## Antes de empezar: Git, VS Code y Chrome

La extensión descarga Flutter usando **Git**, así que Git tiene que estar instalado antes. Si no lo está, el botón *Download SDK* no descarga nada y te manda a la página de Flutter.

| Sistema | Qué instalar |
|---|---|
| Windows | [Git para Windows](https://git-scm.com/download/win). Deja las opciones por defecto del instalador |
| macOS | Abre la Terminal y ejecuta `xcode-select --install`. Eso instala Git junto con otras herramientas de Apple |
| Linux | `sudo apt-get install -y git curl unzip xz-utils zip libglu1-mesa` (en Ubuntu o Debian) |

Luego instala:

- [Visual Studio Code](https://code.visualstudio.com/), el editor.
- [Google Chrome](https://www.google.com/chrome/), porque va a ser el "dispositivo" donde corre tu app.

Para comprobar que Git quedó bien, abre una terminal **nueva** y ejecuta:

```shell
git --version
```

Si responde algo como `git version 2.x.x`, puedes seguir.

## Los seis pasos de un vistazo

Todo lo que sigue ocurre dentro de VS Code. Los botones y mensajes están en inglés: así los vas a ver en tu pantalla.

```svg
<svg id="fiPasos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 616" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fiPasos-ttl fiPasos-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fiPasos-ttl">La instalación básica en seis pasos</title>
  <desc id="fiPasos-dsc">Uno, instalar la extensión Flutter. Dos, abrir la paleta de comandos y elegir Flutter: New Project. Tres, pulsar Download SDK. Cuatro, elegir la carpeta y pulsar Clone Flutter. Cinco, pulsar Add SDK to PATH. Seis, elegir Chrome como dispositivo y pulsar F5.</desc>
  <defs>
    <style>
      #fiPasos .card{fill:#FFFFFF;stroke:#D9DEE8;stroke-width:1.5}
      #fiPasos .title{fill:#161A26;font-size:22px;font-weight:700}
      #fiPasos .sub{fill:#79809A;font-size:13.5px}
      #fiPasos .st{fill:#161A26;font-size:15px;font-weight:600}
      #fiPasos .cap{fill:#454C61;font-size:13px}
      #fiPasos .chip{fill:#FFFFFF;font-size:12px;font-weight:700}
      #fiPasos .scr{fill:#1F2430}
      #fiPasos .ui{fill:#D4D8E3;font-size:12px}
      #fiPasos .dim{fill:#9AA3B5;font-size:11.5px}
      #fiPasos .btn{fill:#0E639C}
      #fiPasos .btn2{fill:#3A4254}
      #fiPasos .bt{fill:#FFFFFF;font-size:11.5px;font-weight:600}
      #fiPasos .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fiPasos .ring{fill:none;stroke:#F2C069;stroke-width:2}
    </style>
  </defs>

  <rect width="960" height="616" rx="16" fill="#FBFBFD"/>

  <text class="title" x="48" y="56">La instalación básica en seis pasos</text>
  <text class="sub" x="48" y="80" data-fit="860">Todo ocurre dentro de VS Code. Los botones están en inglés: así los vas a ver en tu pantalla.</text>

  <g transform="translate(48,112)">
    <rect class="card" width="272" height="216" rx="12"/>
    <circle cx="28" cy="32" r="12" fill="#4453C9"/><text class="chip" x="28" y="32" dy="0.35em" text-anchor="middle">1</text>
    <text class="st" x="48" y="32" dy="0.35em" data-fit="208">Instala la extensión</text>
    <rect class="scr" x="16" y="56" width="240" height="96" rx="8"/>
    <rect x="28" y="66" width="216" height="22" rx="4" fill="#2A3040"/>
    <text class="ui mono" x="36" y="77" dy="0.35em" data-fit="200">flutter</text>
    <rect x="28" y="100" width="36" height="36" rx="6" fill="#1E88E5"/>
    <text x="46" y="118" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="18" font-weight="700">F</text>
    <text x="74" y="113" fill="#FFFFFF" font-size="13" font-weight="700" data-fit="100">Flutter</text>
    <text class="dim" x="74" y="130" data-fit="100">Dart Code</text>
    <rect class="btn" x="180" y="108" width="60" height="22" rx="4"/>
    <text class="bt" x="210" y="119" dy="0.35em" text-anchor="middle" data-fit="56">Install</text>
    <rect class="ring" x="177" y="105" width="66" height="28" rx="6"/>
    <text class="cap" x="16" y="180" data-fit="264">Ctrl+Shift+X, busca «Flutter» e</text>
    <text class="cap" x="16" y="198" data-fit="264">instala la que publica Dart Code.</text>
  </g>

  <g transform="translate(344,112)">
    <rect class="card" width="272" height="216" rx="12"/>
    <circle cx="28" cy="32" r="12" fill="#4453C9"/><text class="chip" x="28" y="32" dy="0.35em" text-anchor="middle">2</text>
    <text class="st" x="48" y="32" dy="0.35em" data-fit="208">Abre la paleta de comandos</text>
    <rect class="scr" x="16" y="56" width="240" height="96" rx="8"/>
    <rect x="28" y="66" width="216" height="24" rx="4" fill="#2A3040" stroke="#0E639C" stroke-width="1.5"/>
    <text class="ui mono" x="36" y="78" dy="0.35em" data-fit="200">&gt; flutter: new</text>
    <rect x="28" y="96" width="216" height="24" fill="#04395E"/>
    <text x="36" y="108" dy="0.35em" fill="#FFFFFF" font-size="12" data-fit="200">Flutter: New Project</text>
    <rect class="ring" x="25" y="93" width="222" height="30" rx="4"/>
    <text class="dim" x="36" y="136" dy="0.35em" data-fit="200">Flutter: Run Flutter Doctor</text>
    <text class="cap" x="16" y="180" data-fit="264">Ctrl+Shift+P (Cmd+Shift+P en Mac)</text>
    <text class="cap" x="16" y="198" data-fit="264">y elige Flutter: New Project.</text>
  </g>

  <g transform="translate(640,112)">
    <rect class="card" width="272" height="216" rx="12"/>
    <circle cx="28" cy="32" r="12" fill="#4453C9"/><text class="chip" x="28" y="32" dy="0.35em" text-anchor="middle">3</text>
    <text class="st" x="48" y="32" dy="0.35em" data-fit="208">Descarga el SDK</text>
    <rect class="scr" x="16" y="56" width="240" height="96" rx="8"/>
    <rect x="28" y="66" width="216" height="76" rx="6" fill="#252B38" stroke="#3A4254"/>
    <circle cx="44" cy="84" r="7" fill="#3794FF"/>
    <text x="44" y="84" dy="0.35em" text-anchor="middle" fill="#1F2430" font-size="10" font-weight="700">i</text>
    <text x="58" y="84" dy="0.35em" fill="#E6E9F0" font-size="11.5" data-fit="180">Could not find a Flutter SDK.</text>
    <rect class="btn" x="40" y="106" width="104" height="24" rx="4"/>
    <text class="bt" x="92" y="118" dy="0.35em" text-anchor="middle" data-fit="112">Download SDK</text>
    <rect class="ring" x="37" y="103" width="110" height="30" rx="6"/>
    <rect class="btn2" x="154" y="106" width="80" height="24" rx="4"/>
    <text x="194" y="118" dy="0.35em" text-anchor="middle" fill="#D4D8E3" font-size="11.5" data-fit="76">Locate SDK</text>
    <text class="cap" x="16" y="180" data-fit="264">Si luego pregunta por una plantilla,</text>
    <text class="cap" x="16" y="198" data-fit="264">presiona Esc por ahora.</text>
  </g>

  <g transform="translate(48,352)">
    <rect class="card" width="272" height="216" rx="12"/>
    <circle cx="28" cy="32" r="12" fill="#4453C9"/><text class="chip" x="28" y="32" dy="0.35em" text-anchor="middle">4</text>
    <text class="st" x="48" y="32" dy="0.35em" data-fit="208">Elige la carpeta</text>
    <rect class="scr" x="16" y="56" width="240" height="96" rx="8"/>
    <text class="dim" x="28" y="76" dy="0.35em" data-fit="216">Select Folder for Flutter SDK</text>
    <rect x="28" y="90" width="216" height="22" rx="4" fill="#2A3040"/>
    <text class="ui mono" x="36" y="101" dy="0.35em" data-fit="200">C:\develop</text>
    <rect class="btn" x="148" y="120" width="96" height="24" rx="4"/>
    <text class="bt" x="196" y="132" dy="0.35em" text-anchor="middle" data-fit="100">Clone Flutter</text>
    <rect class="ring" x="145" y="117" width="102" height="30" rx="6"/>
    <text class="cap" x="16" y="180" data-fit="264">Ruta sin espacios, sin tildes y</text>
    <text class="cap" x="16" y="198" data-fit="264">fuera de OneDrive.</text>
  </g>

  <g transform="translate(344,352)">
    <rect class="card" width="272" height="216" rx="12"/>
    <circle cx="28" cy="32" r="12" fill="#4453C9"/><text class="chip" x="28" y="32" dy="0.35em" text-anchor="middle">5</text>
    <text class="st" x="48" y="32" dy="0.35em" data-fit="208">Agrégalo al PATH</text>
    <rect class="scr" x="16" y="56" width="240" height="96" rx="8"/>
    <rect x="28" y="66" width="216" height="76" rx="6" fill="#252B38" stroke="#3A4254"/>
    <text x="40" y="82" dy="0.35em" fill="#E6E9F0" font-size="11.5" data-fit="196">Do you want to add the Flutter</text>
    <text x="40" y="97" dy="0.35em" fill="#E6E9F0" font-size="11.5" data-fit="196">SDK to PATH...?</text>
    <rect class="btn" x="40" y="110" width="124" height="24" rx="4"/>
    <text class="bt" x="102" y="122" dy="0.35em" text-anchor="middle" data-fit="130">Add SDK to PATH</text>
    <rect class="ring" x="37" y="107" width="130" height="30" rx="6"/>
    <text class="cap" x="16" y="180" data-fit="264">Luego cierra y vuelve a abrir</text>
    <text class="cap" x="16" y="198" data-fit="264">VS Code y las terminales.</text>
  </g>

  <g transform="translate(640,352)">
    <rect class="card" width="272" height="216" rx="12"/>
    <circle cx="28" cy="32" r="12" fill="#3A8235"/><text class="chip" x="28" y="32" dy="0.35em" text-anchor="middle">6</text>
    <text class="st" x="48" y="32" dy="0.35em" data-fit="208">Crea y ejecuta</text>
    <rect class="scr" x="16" y="56" width="240" height="96" rx="8"/>
    <rect x="16" y="56" width="84" height="22" rx="0" fill="#2A3040"/>
    <text class="dim mono" x="26" y="67" dy="0.35em" font-size="11" data-fit="72">main.dart</text>
    <text class="mono" x="28" y="94" font-size="11" fill="#569CD6" data-fit="216">void <tspan fill="#DCDCAA">main</tspan><tspan fill="#D4D8E3">() {</tspan></text>
    <text class="mono" x="44" y="110" font-size="11" fill="#DCDCAA" data-fit="200">runApp<tspan fill="#D4D8E3">(</tspan><tspan fill="#569CD6">const</tspan><tspan fill="#4EC9B0"> MyApp</tspan><tspan fill="#D4D8E3">());</tspan></text>
    <text class="mono" x="28" y="126" font-size="11" fill="#D4D8E3" data-fit="216">}</text>
    <path d="M16,130 H256 V144 A8,8 0 0 1 248,152 H24 A8,8 0 0 1 16,144 Z" fill="#007ACC"/>
    <text x="248" y="141" dy="0.35em" text-anchor="end" fill="#FFFFFF" font-size="11" data-fit="160">Chrome (web-javascript)</text>
    <rect class="ring" x="112" y="131" width="142" height="20" rx="4"/>
    <text class="cap" x="16" y="180" data-fit="264">Elige Chrome abajo a la derecha</text>
    <text class="cap" x="16" y="198" data-fit="264">y presiona F5.</text>
  </g>

  <rect x="48" y="584" width="14" height="14" rx="3" fill="none" stroke="#F2C069" stroke-width="2"/>
  <text class="cap" x="72" y="591" dy="0.35em" fill="#79809A" style="fill:#79809A;font-size:12px" data-fit="700">El recuadro amarillo marca dónde hacer clic en cada paso.</text>
</svg>
```

## Paso 1 · Instalar la extensión de Flutter

1. Abre VS Code.
2. Abre la vista de extensiones con `Ctrl+Shift+X` (`Cmd+Shift+X` en Mac).
3. Busca **Flutter** y elige la que publica **Dart Code**, que es la oficial.
4. Pulsa **Install**.

La extensión de Flutter instala sola la extensión de **Dart**, que es el lenguaje en el que se escribe Flutter. No hace falta instalarla aparte.

## Paso 2 · Pedirle a VS Code un proyecto nuevo

1. Abre la **paleta de comandos** con `Ctrl+Shift+P` (`Cmd+Shift+P` en Mac). Es la caja desde la que se le puede pedir cualquier cosa a VS Code.
2. Escribe `flutter`.
3. Elige **Flutter: New Project**.

Todavía no tienes Flutter, así que VS Code no puede crear el proyecto. Te lo va a decir en el paso siguiente.

## Paso 3 · Descargar el SDK de Flutter

Abajo a la derecha aparece el aviso **Could not find a Flutter SDK**, con dos botones:

- **Locate SDK** es para quien ya tiene Flutter descargado en alguna carpeta.
- **Download SDK** es el tuyo: pídele a VS Code que lo descargue.

Si en este momento VS Code te pregunta **Which Flutter template?**, presiona `Esc`. Vas a crear el proyecto al final, cuando Flutter ya esté instalado.

## Paso 4 · Elegir dónde queda Flutter

Se abre el diálogo **Select Folder for Flutter SDK**. Elige o crea una carpeta y pulsa **Clone Flutter**. VS Code crea dentro una carpeta `flutter` y empieza a descargar; la descarga pesa bastante y puede tardar varios minutos.

| Sistema | Carpeta recomendada |
|---|---|
| Windows | `C:\develop` |
| macOS y Linux | `~/develop` |

La carpeta que elijas tiene que cumplir tres reglas, y romper cualquiera de ellas causa errores raros más adelante:

- **Sin espacios ni tildes** en ninguna parte de la ruta. `C:\Users\María José\...` da problemas.
- **Fuera de carpetas que pidan permisos de administrador**, como `C:\Program Files`.
- **Fuera de OneDrive.** En muchos Windows, *Documentos* y *Escritorio* están sincronizados con OneDrive, y la sincronización interfiere con los miles de archivos de Flutter.

## Paso 5 · Agregar Flutter al PATH

Cuando termina la descarga, VS Code pregunta **Do you want to add the Flutter SDK to PATH so it's accessible in external terminals?** Pulsa **Add SDK to PATH**. Si todo sale bien, verás **The Flutter SDK was added to your PATH**.

El `PATH` es la lista de carpetas donde el sistema busca los programas que escribes en una terminal. Mientras la carpeta de Flutter no esté en esa lista, escribir `flutter` en una terminal da error aunque Flutter esté descargado.

Ahora **cierra VS Code y todas las terminales, y vuelve a abrirlos**. Las terminales leen el `PATH` solo al abrirse: una terminal que ya estaba abierta sigue usando la lista vieja.

Para comprobarlo, abre una terminal nueva (en VS Code: *Terminal → New Terminal*) y ejecuta:

```shell
flutter --version
```

Si ves la versión de Flutter y la de Dart, quedó instalado.

## Revisar la instalación con flutter doctor

`flutter doctor` revisa todo lo que Flutter necesita para cada plataforma y lo resume en una lista.

```shell
flutter doctor
```

La primera vez es normal que salgan varias ✗. **No significan que la instalación esté mala**, sino que falta algo para programar en *esa* plataforma. Para la sesión 1 solo importan las líneas marcadas en verde:

```svg
<svg id="fiDoctor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 568" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fiDoctor-ttl fiDoctor-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fiDoctor-ttl">Cómo leer flutter doctor</title>
  <desc id="fiDoctor-dsc">Salida típica de flutter doctor en Windows después de la instalación básica. Flutter, Chrome, VS Code y Connected device en verde bastan para la sesión 1. Android toolchain y Android Studio se resuelven en la instalación avanzada. Visual Studio solo hace falta para apps de escritorio de Windows.</desc>
  <defs>
    <style>
      #fiDoctor .title{fill:#161A26;font-size:22px;font-weight:700}
      #fiDoctor .sub{fill:#79809A;font-size:13.5px}
      #fiDoctor .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fiDoctor .tl{fill:#D4D8E3;font-size:12.5px}
      #fiDoctor .ok{fill:#6BCB77} #fiDoctor .ko{fill:#F14C4C} #fiDoctor .wa{fill:#E5C07B}
      #fiDoctor .ct{font-size:15px;font-weight:700}
      #fiDoctor .cb{fill:#454C61;font-size:13px}
      #fiDoctor .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>

  <rect width="960" height="568" rx="16" fill="#FBFBFD"/>

  <text class="title" x="48" y="56">Cómo leer <tspan class="mono">flutter doctor</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Una ✗ no siempre es un problema: depende de para qué plataforma vas a programar.</text>

  <rect x="48" y="112" width="560" height="392" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H596 A12,12 0 0 1 608,124 V140 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="126" r="5" fill="#F14C4C"/><circle cx="84" cy="126" r="5" fill="#E5C07B"/><circle cx="100" cy="126" r="5" fill="#6BCB77"/>
  <text x="328" y="126" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="11.5">Terminal</text>

  <g class="mono">
    <text class="tl mono" font-size="12.5" x="72" y="170"><tspan fill="#9AA3B5">$</tspan> flutter doctor</text>
    <text class="tl mono" font-size="12.5" x="72" y="196" fill="#9AA3B5" style="fill:#9AA3B5" data-fit="536">Doctor summary (to see all details, run flutter doctor -v):</text>

    <rect x="56" y="208" width="4" height="20" rx="2" fill="#3A8235"/>
    <text class="tl mono" font-size="12.5" x="72" y="222" data-fit="520">[<tspan class="ok">✓</tspan>] Flutter (Channel stable, 3.x.x)</text>
    <text class="tl mono" font-size="12.5" x="72" y="248" data-fit="520">[<tspan class="ok">✓</tspan>] Windows Version (11 Pro 64-bit)</text>
    <rect x="56" y="260" width="4" height="20" rx="2" fill="#A96C05"/>
    <text class="tl mono" font-size="12.5" x="72" y="274" data-fit="520">[<tspan class="ko">✗</tspan>] Android toolchain - develop for Android devices</text>
    <rect x="56" y="286" width="4" height="20" rx="2" fill="#3A8235"/>
    <text class="tl mono" font-size="12.5" x="72" y="300" data-fit="520">[<tspan class="ok">✓</tspan>] Chrome - develop for the web</text>
    <rect x="56" y="312" width="4" height="20" rx="2" fill="#79809A"/>
    <text class="tl mono" font-size="12.5" x="72" y="326" data-fit="520">[<tspan class="ko">✗</tspan>] Visual Studio - develop Windows apps</text>
    <rect x="56" y="338" width="4" height="20" rx="2" fill="#A96C05"/>
    <text class="tl mono" font-size="12.5" x="72" y="352" data-fit="520">[<tspan class="wa">!</tspan>] Android Studio (not installed)</text>
    <rect x="56" y="364" width="4" height="20" rx="2" fill="#3A8235"/>
    <text class="tl mono" font-size="12.5" x="72" y="378" data-fit="520">[<tspan class="ok">✓</tspan>] VS Code (version 1.x)</text>
    <rect x="56" y="390" width="4" height="20" rx="2" fill="#3A8235"/>
    <text class="tl mono" font-size="12.5" x="72" y="404" data-fit="520">[<tspan class="ok">✓</tspan>] Connected device (3 available)</text>
    <text class="tl mono" font-size="12.5" x="72" y="430" data-fit="520">[<tspan class="ok">✓</tspan>] Network resources</text>

    <text class="tl mono" font-size="12.5" x="72" y="470" data-fit="520"><tspan class="wa">!</tspan> Doctor found issues in 3 categories.</text>
  </g>

  <g transform="translate(640,160)">
    <rect width="272" height="112" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
    <rect width="6" height="112" rx="3" fill="#3A8235"/>
    <text class="ct" x="22" y="30" fill="#3A8235" data-fit="236">Lo que necesitas hoy</text>
    <text class="cb" x="22" y="54" data-fit="236">Flutter, Chrome, VS Code y</text>
    <text class="cb" x="22" y="73" data-fit="236">Connected device en ✓.</text>
    <text class="cb" x="22" y="92" data-fit="236">Con eso corre la sesión 1.</text>
  </g>

  <g transform="translate(640,288)">
    <rect width="272" height="112" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
    <rect width="6" height="112" rx="3" fill="#A96C05"/>
    <text class="ct" x="22" y="30" fill="#A96C05" data-fit="236">Puede quedar pendiente</text>
    <text class="cb" x="22" y="54" data-fit="236">Android toolchain y Android</text>
    <text class="cb" x="22" y="73" data-fit="236">Studio se resuelven en la</text>
    <text class="cb" x="22" y="92" data-fit="236">sección Instalación avanzada.</text>
  </g>

  <g transform="translate(640,416)">
    <rect width="272" height="88" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
    <rect width="6" height="88" rx="3" fill="#79809A"/>
    <text class="ct" x="22" y="30" fill="#556074" data-fit="236">No hace falta en el curso</text>
    <text class="cb" x="22" y="54" data-fit="236">Visual Studio solo sirve para</text>
    <text class="cb" x="22" y="73" data-fit="236">apps de escritorio de Windows.</text>
  </g>

  <text class="foot" x="48" y="536" data-fit="860">Ejemplo en Windows. En Mac aparece Xcode en lugar de Visual Studio: es para iOS y también va en Instalación avanzada.</text>
</svg>
```

| Línea | Qué hacer por ahora |
|---|---|
| `Flutter`, `Chrome`, `VS Code`, `Connected device` en ✓ | Nada: con eso ya puedes trabajar |
| `Android toolchain` en ✗, `Android Studio` en ! | Nada todavía. Se resuelve en la sección *Instalación avanzada* |
| `Visual Studio` en ✗ (Windows) | Nada. Solo hace falta para apps de escritorio de Windows |
| `Xcode` en ✗ (Mac) | Nada todavía. Es para iOS y va en *Instalación avanzada* |
| `Chrome` en ✗ | Instala Google Chrome, cierra y abre la terminal, y repite `flutter doctor` |

## Crear y ejecutar tu primera app

Ahora sí, con Flutter instalado:

1. Abre la paleta de comandos (`Ctrl+Shift+P`) y elige otra vez **Flutter: New Project**.
2. Elige la plantilla **Application**.
3. Elige la carpeta donde vas a guardar tus proyectos. Aplican las mismas reglas: sin espacios, sin tildes, fuera de OneDrive.
4. Escribe el nombre del proyecto en minúsculas y con guion bajo, por ejemplo `hola_mundo`. Flutter no acepta mayúsculas, espacios ni guiones en el nombre.

VS Code crea el proyecto y abre `lib/main.dart`, el archivo donde empieza la app.

Para ejecutarla:

1. Mira la **barra azul de abajo**, a la derecha. Ahí aparece el dispositivo donde correrá la app. Haz clic y elige **Chrome (web-javascript)**.
2. Presiona `F5` (o *Run → Start Debugging*).

La primera ejecución tarda un poco porque compila todo. Después se abre Chrome con la app de ejemplo: un contador con un botón **+**.

Si prefieres la terminal, lo mismo se hace con:

```shell
flutter run -d chrome
```

### Pruébalo: hot reload

Con la app corriendo, abre `lib/main.dart`, busca el texto `'Flutter Demo Home Page'`, cámbialo por `'Hola mundo'` y guarda con `Ctrl+S`. El título cambia en Chrome sin reiniciar la app y sin perder el número del contador. Eso es el **hot reload**, y es lo que vas a usar todo el tiempo mientras programas.

## Si algo falla

| Lo que ves | Por qué pasa | Qué hacer |
|---|---|---|
| `flutter: command not found` o `"flutter" no se reconoce como un comando interno o externo` | La terminal se abrió antes de agregar Flutter al PATH, o el Paso 5 no se completó | Cierra todas las terminales y VS Code, y ábrelos otra vez. Si sigue, repite el Paso 5 desde la paleta: **Flutter: Add SDK to PATH** |
| *Download SDK* abre una página web en vez de descargar | Git no está instalado | Instala Git (ver *Antes de empezar*), reinicia VS Code y repite el Paso 2 |
| Vuelve a salir **Could not find a Flutter SDK** | VS Code no sabe en qué carpeta quedó Flutter | Pulsa **Locate SDK** y elige la carpeta `flutter` que se creó en el Paso 4 |
| En la barra de abajo no aparece Chrome | Chrome no está instalado, o VS Code no lo ha detectado todavía | Instala Chrome y reinicia VS Code |
| Errores raros de rutas al compilar | La ruta de Flutter o del proyecto tiene espacios, tildes o está en OneDrive | Mueve el proyecto (o reinstala Flutter) a una carpeta como `C:\develop` |
| `Building with plugins requires symlink support` (Windows) | Windows no deja crear accesos directos simbólicos, que Flutter usa cuando el proyecto tiene paquetes | Activa el **Modo de desarrollador**: ejecuta `start ms-settings:developers` y enciende la opción |

## ¿Y Android o iOS?

Con esta instalación ya puedes seguir todo lo que viene en las primeras sesiones. Cuando quieras ver tu app en un emulador de Android, en tu celular o en un simulador de iOS (este último solo en Mac), sigue la sección **Instalación avanzada**, donde se instalan Android Studio, Xcode y los dispositivos virtuales.
