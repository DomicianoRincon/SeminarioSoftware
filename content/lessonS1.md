# Instalación básica

<!-- tags: flutter create --org, flutter devices, flutter run -d chrome, Add SDK to PATH, flutter no se reconoce como comando, extensión Flutter de VS Code, Download SDK, Could not find a Flutter SDK, id del dispositivo, hot reload con r, nombre de proyecto en minúsculas, terminal de VS Code -->

Hay dos formas de dejar Flutter listo en tu computador. En esta lección vas a hacer la **básica**: la extensión de Flutter de VS Code descarga Flutter y lo deja disponible en la consola. Desde ahí creas tu primer proyecto con `flutter create` y lo ejecutas en **Chrome**, que es todo lo que necesitas para las primeras sesiones.

Partimos de que ya tienes **Git** y **Visual Studio Code** instalados, y **Google Chrome** para ver tu app.

La otra forma, la **avanzada**, es la que usarás cuando quieras correr tus apps en un emulador de Android, en un celular o en un simulador de iOS. Está en la sección *Instalación avanzada* del temario. No hace falta hacerla hoy, y todo lo que instales aquí te sirve para ella.

```svg
<svg id="fiPiezas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fiPiezas-ttl fiPiezas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fiPiezas-ttl">Las piezas de la instalación básica</title>
  <desc id="fiPiezas-dsc">Ya tienes Git y Visual Studio Code. La extensión de Flutter descarga el Flutter SDK, que incluye Dart, y lo agrega al PATH. Con eso la app corre en Chrome; Android e iOS se configuran en la instalación avanzada.</desc>
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
  <text class="sub" x="48" y="80" data-fit="860">Ya tienes Git y VS Code. La extensión de Flutter se encarga del resto.</text>

  <text class="h" x="48" y="120">LO QUE YA TIENES</text>
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

## Instalar Flutter con la extensión

Los primeros seis pasos ocurren dentro de VS Code. Los botones y mensajes están en inglés: así los vas a ver en tu pantalla.

```svg
<svg id="fiPasos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 616" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fiPasos-ttl fiPasos-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fiPasos-ttl">Instalar Flutter con la extensión</title>
  <desc id="fiPasos-dsc">Uno, instalar la extensión Flutter. Dos, abrir la paleta de comandos y elegir Flutter: New Project. Tres, pulsar Download SDK. Cuatro, elegir la carpeta y pulsar Clone Flutter. Cinco, pulsar Add SDK to PATH. Seis, abrir una terminal desde el menú Terminal.</desc>
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

  <text class="title" x="48" y="56">Instalar Flutter con la extensión</text>
  <text class="sub" x="48" y="80" data-fit="860">Seis pasos dentro de VS Code. Los botones están en inglés: así los vas a ver en tu pantalla.</text>

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
    <text class="cap" x="16" y="180" data-fit="264">Si pregunta por una plantilla,</text>
    <text class="cap" x="16" y="198" data-fit="264">presiona Esc: no la necesitas.</text>
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
    <text class="st" x="48" y="32" dy="0.35em" data-fit="208">Abre una terminal</text>
    <rect class="scr" x="16" y="56" width="240" height="96" rx="8"/>
    <text class="dim" x="26" y="70" dy="0.35em" font-size="11" data-fit="60">View</text>
    <text class="dim" x="60" y="70" dy="0.35em" font-size="11" data-fit="30">Go</text>
    <text class="dim" x="84" y="70" dy="0.35em" font-size="11" data-fit="30">Run</text>
    <rect x="110" y="61" width="58" height="18" rx="3" fill="#04395E"/>
    <text x="139" y="70" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="11" data-fit="54">Terminal</text>
    <rect x="110" y="82" width="136" height="62" rx="4" fill="#252B38" stroke="#3A4254"/>
    <rect x="114" y="87" width="128" height="22" rx="3" fill="#04395E"/>
    <text x="122" y="98" dy="0.35em" fill="#FFFFFF" font-size="11.5" data-fit="116">New Terminal</text>
    <rect class="ring" x="111" y="84" width="134" height="28" rx="5"/>
    <text class="dim" x="122" y="126" dy="0.35em" font-size="11" data-fit="116">Split Terminal</text>
    <text class="cap" x="16" y="180" data-fit="264">Terminal → New Terminal.</text>
    <text class="cap" x="16" y="198" data-fit="264">Desde aquí sigue todo en consola.</text>
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

## Paso 2 · Abrir la paleta de comandos

1. Abre la **paleta de comandos** con `Ctrl+Shift+P` (`Cmd+Shift+P` en Mac). Es la caja desde la que se le puede pedir cualquier cosa a VS Code.
2. Escribe `flutter`.
3. Elige **Flutter: New Project**.

No vas a crear el proyecto desde aquí: eso lo harás en la consola. Este comando sirve para que la extensión se dé cuenta de que Flutter todavía no está instalado y te ofrezca descargarlo.

## Paso 3 · Descargar el SDK de Flutter

Abajo a la derecha aparece el aviso **Could not find a Flutter SDK**, con dos botones:

- **Locate SDK** es para quien ya tiene Flutter descargado en alguna carpeta.
- **Download SDK** es el tuyo: pídele a VS Code que lo descargue.

Si VS Code te pregunta **Which Flutter template?**, presiona `Esc`. No necesitas plantilla porque el proyecto lo vas a crear en la consola.

## Paso 4 · Elegir dónde queda Flutter

Se abre el diálogo **Select Folder for Flutter SDK**. Elige o crea una carpeta y pulsa **Clone Flutter**. VS Code crea dentro una carpeta `flutter` y empieza a descargar; la descarga pesa bastante y puede tardar varios minutos.

| Sistema | Carpeta recomendada |
|---|---|
| Windows | `C:\develop` |
| macOS y Linux | `~/develop` |

Esa misma carpeta `develop` es la que vas a usar después para tus proyectos. Tiene que cumplir tres reglas, y romper cualquiera de ellas causa errores raros más adelante:

- **Sin espacios ni tildes** en ninguna parte de la ruta. `C:\Users\María José\...` da problemas.
- **Fuera de carpetas que pidan permisos de administrador**, como `C:\Program Files`.
- **Fuera de OneDrive.** En muchos Windows, *Documentos* y *Escritorio* están sincronizados con OneDrive, y la sincronización interfiere con los miles de archivos de Flutter.

## Paso 5 · Agregar Flutter al PATH

Cuando termina la descarga, VS Code pregunta **Do you want to add the Flutter SDK to PATH so it's accessible in external terminals?** Pulsa **Add SDK to PATH**. Si todo sale bien, verás **The Flutter SDK was added to your PATH**.

El `PATH` es la lista de carpetas donde el sistema busca los programas que escribes en una consola. Mientras la carpeta de Flutter no esté en esa lista, escribir `flutter` da error aunque Flutter esté descargado.

Ahora **cierra VS Code y todas las terminales, y vuelve a abrirlos**. Las terminales leen el `PATH` solo al abrirse: una que ya estaba abierta sigue usando la lista vieja.

## Paso 6 · Ir a la consola

Desde aquí todo se hace en la consola. Abre una terminal nueva en VS Code con **Terminal → New Terminal**. También sirve la terminal del sistema: PowerShell en Windows o Terminal en Mac.

Primero comprueba que la consola encuentra Flutter:

```svg
<svg id="tcVersion" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 460" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tcVersion-ttl tcVersion-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tcVersion-ttl">Comprobar que Flutter responde</title>
  <desc id="tcVersion-dsc">Terminal con el comando flutter <tspan letter-spacing="2">-</tspan>-version y su salida: la versión de Flutter, del framework, del engine y de Dart.</desc>
  <defs>
    <style>
      #tcVersion .title{fill:#161A26;font-size:22px;font-weight:700}
      #tcVersion .sub{fill:#79809A;font-size:13.5px}
      #tcVersion .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tcVersion .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #tcVersion .pf{fill:#7F8AA3} #tcVersion .cmd{fill:#FFFFFF;font-weight:600}
      #tcVersion .dim{fill:#8A93A6} #tcVersion .okk{fill:#6BCB77;font-weight:600}
      #tcVersion .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #tcVersion .chipc{fill:#F2C069} #tcVersion .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #tcVersion .ct{fill:#161A26;font-size:14px;font-weight:700}
      #tcVersion .cb{fill:#454C61;font-size:13px}
      #tcVersion .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="460" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Comprobar que Flutter responde</text>
  <text class="sub" x="48" y="80" data-fit="860">Lo que está antes de &gt; es la carpeta en la que estás. No se escribe.</text>
  <rect x="48" y="112" width="864" height="190" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">flutter <tspan letter-spacing="2">-</tspan>-version</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="200" data-fit="816">Flutter 3.x.x • channel stable • https://github.com/flutter/flutter.git</text>
  <text class="tl mono" font-size="13" x="72" y="226" data-fit="816">Framework • revision xxxxxxxxxx • 2026-xx-xx</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816">Engine • revision xxxxxxxxxx</text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816">Tools • Dart 3.x.x • DevTools 2.x.x</text>
  <rect class="ring" x="68.0" y="184" width="109.4" height="22" rx="5"/>
  <circle class="chipc" cx="177.4" cy="185" r="8"/>
  <text class="chipt" x="177.4" y="185" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="130.4" y="262" width="86.0" height="22" rx="5"/>
  <circle class="chipc" cx="216.4" cy="263" r="8"/>
  <text class="chipt" x="216.4" y="263" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <g transform="translate(48.0,326)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Flutter responde</text>
    <text class="cb" x="16" y="60" data-fit="392">La terminal encontró el comando: la carpeta</text>
    <text class="cb" x="16" y="79" data-fit="392">de Flutter quedó en el PATH.</text>
  </g>
  <g transform="translate(488.0,326)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Dart viene incluido</text>
    <text class="cb" x="16" y="60" data-fit="392">No hay que instalar Dart aparte: llega</text>
    <text class="cb" x="16" y="79" data-fit="392">junto con Flutter.</text>
  </g>
</svg>
```

```shell
flutter --version
```

En las figuras de consola, lo que aparece antes de `>` es la carpeta en la que estás parado. No se escribe: solo se escribe lo que va después.

## Crear el proyecto con flutter create

Ubícate en la carpeta `develop` y crea el proyecto:

```svg
<svg id="tcCreate" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 739" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tcCreate-ttl tcCreate-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tcCreate-ttl">Crear el proyecto con flutter create</title>
  <desc id="tcCreate-dsc">Terminal en la carpeta develop con el comando flutter create <tspan letter-spacing="2">-</tspan>-org icesi.edu.co miapp1, su salida terminada en All done!, y luego cd miapp1 para entrar a la carpeta del proyecto.</desc>
  <defs>
    <style>
      #tcCreate .title{fill:#161A26;font-size:22px;font-weight:700}
      #tcCreate .sub{fill:#79809A;font-size:13.5px}
      #tcCreate .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tcCreate .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #tcCreate .pf{fill:#7F8AA3} #tcCreate .cmd{fill:#FFFFFF;font-weight:600}
      #tcCreate .dim{fill:#8A93A6} #tcCreate .okk{fill:#6BCB77;font-weight:600}
      #tcCreate .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #tcCreate .chipc{fill:#F2C069} #tcCreate .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #tcCreate .ct{fill:#161A26;font-size:14px;font-weight:700}
      #tcCreate .cb{fill:#454C61;font-size:13px}
      #tcCreate .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="739" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Crear el proyecto con <tspan class="mono">flutter create</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Un solo comando crea el proyecto completo. Después entras a su carpeta.</text>
  <rect x="48" y="112" width="864" height="450" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">flutter create <tspan letter-spacing="2">-</tspan>-org icesi.edu.co miapp1</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="200" data-fit="816">Creating project miapp1...</text>
  <text class="tl mono" font-size="13" x="72" y="226" data-fit="816">Resolving dependencies in `miapp1`...</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816">Got dependencies in `miapp1`.</text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816">Wrote 130 files.</text>
  <text class="tl mono okk" font-size="13" x="72" y="330" data-fit="816">All done!</text>
  <text class="tl mono dim" font-size="13" x="72" y="356" data-fit="816">In order to run your application, type:</text>
  <text class="tl mono dim" font-size="13" x="72" y="408" data-fit="816">  $ cd miapp1</text>
  <text class="tl mono dim" font-size="13" x="72" y="434" data-fit="816">  $ flutter run</text>
  <text class="tl mono dim" font-size="13" x="72" y="486" data-fit="816">Your application code is in miapp1\lib\main.dart.</text>
  <text class="tl mono" font-size="13" x="72" y="512" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">cd miapp1</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="538" data-fit="816"><tspan class="pf">miapp1&gt; </tspan><tspan class="cmd"></tspan></text>
  <rect class="ring" x="255.2" y="158" width="148.4" height="22" rx="5"/>
  <circle class="chipc" cx="403.6" cy="159" r="8"/>
  <text class="chipt" x="403.6" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="403.4" y="158" width="54.8" height="22" rx="5"/>
  <circle class="chipc" cx="458.2" cy="159" r="8"/>
  <text class="chipt" x="458.2" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <rect class="ring" x="138.2" y="496" width="78.2" height="22" rx="5"/>
  <circle class="chipc" cx="216.4" cy="497" r="8"/>
  <text class="chipt" x="216.4" y="497" dy="0.35em" text-anchor="middle" font-size="10.5">3</text>
  <g transform="translate(48.0,586)">
    <rect width="277.3" height="121" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct mono" x="46" y="26" dy="0.35em" data-fit="215"><tspan letter-spacing="2">-</tspan>-org icesi.edu.co</text>
    <text class="cb" x="16" y="60" data-fit="245">Prefijo del identificador de la</text>
    <text class="cb" x="16" y="79" data-fit="245">app. Queda como</text>
    <text class="cb" x="16" y="98" data-fit="245"><tspan class="mono">icesi.edu.co.miapp1</tspan></text>
  </g>
  <g transform="translate(341.3,586)">
    <rect width="277.3" height="121" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct mono" x="46" y="26" dy="0.35em" data-fit="215">miapp1</text>
    <text class="cb" x="16" y="60" data-fit="245">Nombre del proyecto y de la</text>
    <text class="cb" x="16" y="79" data-fit="245">carpeta que se crea. Solo</text>
    <text class="cb" x="16" y="98" data-fit="245">minúsculas, números y _</text>
  </g>
  <g transform="translate(634.7,586)">
    <rect width="277.3" height="121" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">3</text>
    <text class="ct mono" x="46" y="26" dy="0.35em" data-fit="215">cd miapp1</text>
    <text class="cb" x="16" y="60" data-fit="245">Entra a la carpeta del proyecto.</text>
    <text class="cb" x="16" y="79" data-fit="245">Todo lo que sigue se ejecuta</text>
    <text class="cb" x="16" y="98" data-fit="245">desde ahí.</text>
  </g>
</svg>
```

En Windows:

```shell
cd C:\develop
flutter create --org icesi.edu.co miapp1
cd miapp1
```

En macOS o Linux:

```shell
cd ~/develop
flutter create --org icesi.edu.co miapp1
cd miapp1
```

El comando tiene dos partes que tú decides:

- `--org icesi.edu.co` es el prefijo del identificador de la app. Con él, la app queda identificada como `icesi.edu.co.miapp1`, que es el nombre con el que la reconocen Android e iOS.
- `miapp1` es el nombre del proyecto y de la carpeta que se crea. Flutter solo acepta **minúsculas, números y guion bajo**, y tiene que empezar con una letra: `miapp1` y `mi_app` sirven; `MiApp`, `mi-app` y `mi app` no.

Para ver el código, abre la carpeta del proyecto en VS Code con **File → Open Folder** y elige `miapp1`. La app empieza en `lib/main.dart`.

## Probar: ver los dispositivos con flutter devices

Antes de ejecutar, pregúntale a Flutter en qué dispositivos puede correr tu app:

```svg
<svg id="tcDevices" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 564" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tcDevices-ttl tcDevices-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tcDevices-ttl">Ver los dispositivos con flutter devices</title>
  <desc id="tcDevices-dsc">Terminal con flutter devices: aparecen Windows, Chrome y Edge. La segunda columna es el id de cada dispositivo; el de Chrome es chrome.</desc>
  <defs>
    <style>
      #tcDevices .title{fill:#161A26;font-size:22px;font-weight:700}
      #tcDevices .sub{fill:#79809A;font-size:13.5px}
      #tcDevices .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tcDevices .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #tcDevices .pf{fill:#7F8AA3} #tcDevices .cmd{fill:#FFFFFF;font-weight:600}
      #tcDevices .dim{fill:#8A93A6} #tcDevices .okk{fill:#6BCB77;font-weight:600}
      #tcDevices .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #tcDevices .chipc{fill:#F2C069} #tcDevices .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #tcDevices .ct{fill:#161A26;font-size:14px;font-weight:700}
      #tcDevices .cb{fill:#454C61;font-size:13px}
      #tcDevices .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="564" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Ver los dispositivos con <tspan class="mono">flutter devices</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Cada renglón es un lugar donde puede correr tu app: nombre • id • plataforma • detalles.</text>
  <rect x="48" y="112" width="864" height="294" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\miapp1</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">miapp1&gt; </tspan><tspan class="cmd">flutter devices</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="200" data-fit="816">Found 3 connected devices:</text>
  <text class="tl mono" font-size="13" x="72" y="226" data-fit="816">  Windows (desktop) • windows • windows-x64    • Microsoft Windows 11</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816">  Chrome (web)      • chrome  • web-javascript • Google Chrome 1xx</text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816">  Edge (web)        • edge    • web-javascript • Microsoft Edge 1xx</text>
  <text class="tl mono dim" font-size="13" x="72" y="330" data-fit="816">No wireless devices were found.</text>
  <text class="tl mono dim" font-size="13" x="72" y="382" data-fit="816">Run "flutter emulators" to list and start any available device emulators.</text>
  <rect class="ring" x="239.6" y="236" width="54.8" height="22" rx="5"/>
  <circle class="chipc" cx="294.4" cy="237" r="8"/>
  <text class="chipt" x="294.4" y="237" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <g transform="translate(48.0,430)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">chrome es el id</text>
    <text class="cb" x="16" y="60" data-fit="392">La segunda columna es el id del dispositivo:</text>
    <text class="cb" x="16" y="79" data-fit="392">es lo que va después de <tspan class="mono">-d</tspan> en <tspan class="mono">flutter run</tspan>.</text>
  </g>
  <g transform="translate(488.0,430)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="26" cy="26" r="10" fill="#4453C9"/>
    <text x="26" y="26" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="12" font-weight="700">i</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">La lista cambia según tu equipo</text>
    <text class="cb" x="16" y="60" data-fit="392">En Mac aparece macOS en vez de Windows.</text>
    <text class="cb" x="16" y="79" data-fit="392">Emuladores y celulares: Instalación avanzada.</text>
  </g>
</svg>
```

```shell
flutter devices
```

Cada renglón es un dispositivo, y la **segunda columna es su id**. Con la instalación básica deberías ver al menos **Chrome**, con el id `chrome`. Es el que usarás en el paso siguiente.

## Ejecutar en el navegador con flutter run -d chrome

Desde la carpeta `miapp1`:

```svg
<svg id="tcRun" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 802" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tcRun-ttl tcRun-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tcRun-ttl">Ejecutar en el navegador con flutter run -d chrome</title>
  <desc id="tcRun-dsc">Terminal con flutter run -d chrome: compila, abre Chrome con la app de ejemplo (un contador) y muestra las teclas r para recargar, R para reiniciar y q para salir.</desc>
  <defs>
    <style>
      #tcRun .title{fill:#161A26;font-size:22px;font-weight:700}
      #tcRun .sub{fill:#79809A;font-size:13.5px}
      #tcRun .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tcRun .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #tcRun .pf{fill:#7F8AA3} #tcRun .cmd{fill:#FFFFFF;font-weight:600}
      #tcRun .dim{fill:#8A93A6} #tcRun .okk{fill:#6BCB77;font-weight:600}
      #tcRun .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #tcRun .chipc{fill:#F2C069} #tcRun .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #tcRun .ct{fill:#161A26;font-size:14px;font-weight:700}
      #tcRun .cb{fill:#454C61;font-size:13px}
      #tcRun .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="802" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Ejecutar en el navegador con <tspan class="mono">flutter run -d chrome</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">La primera vez tarda porque compila todo. Mientras la app corre, la terminal queda esperando teclas.</text>
  <rect x="48" y="112" width="864" height="398" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\miapp1</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">miapp1&gt; </tspan><tspan class="cmd">flutter run -d chrome</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="200" data-fit="816">Launching lib\main.dart on Chrome in debug mode...</text>
  <text class="tl mono" font-size="13" x="72" y="226" data-fit="816">Waiting for connection from debug service on Chrome...      14.8s</text>
  <text class="tl mono dim" font-size="13" x="72" y="252" data-fit="816">This app is linked to the debug service: ws://127.0.0.1:53712/xYz/ws</text>
  <text class="tl mono dim" font-size="13" x="72" y="278" data-fit="816">Debug service listening on ws://127.0.0.1:53712/xYz/ws</text>
  <text class="tl mono" font-size="13" x="72" y="330" data-fit="816">Flutter run key commands.</text>
  <text class="tl mono" font-size="13" x="72" y="356" data-fit="816">r Hot reload.</text>
  <text class="tl mono" font-size="13" x="72" y="382" data-fit="816">R Hot restart.</text>
  <text class="tl mono" font-size="13" x="72" y="408" data-fit="816">h List all available interactive commands.</text>
  <text class="tl mono" font-size="13" x="72" y="434" data-fit="816">d Detach (terminate "flutter run" but leave application running).</text>
  <text class="tl mono" font-size="13" x="72" y="460" data-fit="816">c Clear the screen</text>
  <text class="tl mono" font-size="13" x="72" y="486" data-fit="816">q Quit (terminate the application on the device).</text>
  <rect class="ring" x="224.0" y="158" width="78.2" height="22" rx="5"/>
  <circle class="chipc" cx="302.2" cy="159" r="8"/>
  <text class="chipt" x="302.2" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="68.0" y="340" width="109.4" height="22" rx="5"/>
  <circle class="chipc" cx="177.4" cy="341" r="8"/>
  <text class="chipt" x="177.4" y="341" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <rect class="ring" x="68.0" y="470" width="54.8" height="22" rx="5"/>
  <circle class="chipc" cx="122.8" cy="471" r="8"/>
  <text class="chipt" x="122.8" y="471" dy="0.35em" text-anchor="middle" font-size="10.5">3</text>
  <g transform="translate(48.0,534)">
    <rect width="277.3" height="236" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">Se abre Chrome con tu app</text>
    <rect x="16" y="52" width="245" height="168" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.25"/>
    <path d="M16,60 A8,8 0 0 1 24,52 H253 A8,8 0 0 1 261,60 V74 H16 Z" fill="#E8EAEF"/>
    <rect x="26" y="57" width="225" height="12" rx="6" fill="#FFFFFF"/>
    <text x="34" y="63" dy="0.35em" fill="#79809A" font-size="10" class="mono">localhost:53712</text>
    <rect x="17" y="74" width="243" height="26" fill="#EADDFF"/>
    <text x="28" y="87" dy="0.35em" fill="#1D1B20" font-size="11.5" data-fit="221">Flutter Demo Home Page</text>
    <text x="139" y="124" text-anchor="middle" fill="#454C61" font-size="10.5" data-fit="229">You have pushed the button this many times:</text>
    <text x="139" y="150" text-anchor="middle" fill="#1D1B20" font-size="20" font-weight="600">0</text>
    <rect x="217" y="176" width="32" height="32" rx="9" fill="#EADDFF"/>
    <text x="233" y="192" dy="0.35em" text-anchor="middle" fill="#1D1B20" font-size="18">+</text>
  </g>
  <g transform="translate(341.3,534)">
    <rect width="277.3" height="236" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">r y R: ver tus cambios</text>
    <text class="cb" x="16" y="60" data-fit="245"><tspan class="mono">r</tspan> aplica lo que cambiaste en el</text>
    <text class="cb" x="16" y="79" data-fit="245">código sin cerrar la app.</text>
    <text class="cb" x="16" y="98" data-fit="245"><tspan class="mono">R</tspan> la reinicia desde cero: el</text>
    <text class="cb" x="16" y="117" data-fit="245">contador vuelve a 0.</text>
  </g>
  <g transform="translate(634.7,534)">
    <rect width="277.3" height="236" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">3</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">q: terminar</text>
    <text class="cb" x="16" y="60" data-fit="245">Detiene la app y te devuelve la</text>
    <text class="cb" x="16" y="79" data-fit="245">terminal. Cerrar Chrome no</text>
    <text class="cb" x="16" y="98" data-fit="245">basta: la terminal sigue</text>
    <text class="cb" x="16" y="117" data-fit="245">esperando.</text>
  </g>
</svg>
```

```shell
flutter run -d chrome
```

`-d` le dice a Flutter en qué dispositivo ejecutar, usando el id que viste con `flutter devices`. La primera vez tarda un poco porque compila todo. Después se abre una ventana de Chrome con la app de ejemplo: un contador con un botón **+**.

Mientras la app corre, la terminal queda **esperando teclas**, no comandos:

| Tecla | Qué hace |
|---|---|
| `r` | Aplica los cambios que hiciste en el código sin cerrar la app |
| `R` | Reinicia la app desde cero |
| `q` | Detiene la app y te devuelve la consola |

### Pruébalo: cambia el título

1. Con la app corriendo, abre `lib/main.dart` en VS Code.
2. Busca el texto `'Flutter Demo Home Page'` y cámbialo por `'Hola mundo'`.
3. Guarda con `Ctrl+S` (`Cmd+S` en Mac).
4. Vuelve a la terminal donde corre la app y presiona `r`.

El título cambia en Chrome sin volver a compilar todo. Cuando termines, presiona `q`.

## ¿Y Android o iOS?

Con esta instalación ya puedes seguir todo lo que viene en las primeras sesiones. Cuando quieras ver tu app en un emulador de Android, en tu celular o en un simulador de iOS (este último solo en Mac), sigue la sección **Instalación avanzada**, donde se instalan Android Studio, Xcode y los dispositivos virtuales. Cuando estén listos, van a aparecer en `flutter devices` con su propio id, y se ejecutan igual: `flutter run -d <id>`.
