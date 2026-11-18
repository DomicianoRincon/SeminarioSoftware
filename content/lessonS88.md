# Repositorio de arranque

<!-- tags: 262SeminarioSesion14, git clone, flutter pub get, ProfileScreen, ProfileAvatar, impl_progress.md, standard_code.md, .agents/skills, .claude/skills, docs/tecnicas -->

El taller de esta sesión sigue sobre la app de tracks de la sesión 13, ya resuelta: cada persona tiene su cuenta y sus tracks. Esta versión trae además una pantalla de perfil y todo el proceso de Spec Driven Development ya corrido: las specs, las specs técnicas y la lista de tareas, con cuatro pendientes. Clónala aparte, fuera de la carpeta de tu proyecto.

```svg
<svg id="raClonar14" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 590" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="raClonar14-ttl raClonar14-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="raClonar14-ttl">Clonar el repositorio de la sesión 14</title>
  <desc id="raClonar14-dsc">Una terminal parada en la carpeta develop. Primero git clone con la dirección de 262SeminarioSesion14, que crea la carpeta 262SeminarioSesion14. Después cd 262SeminarioSesion14, flutter pub get, que termina con Got dependencies, y flutter run -d chrome, que abre la app en Chrome. Tres recuadros numerados señalan la dirección del repositorio, flutter pub get y flutter run, cada uno con su tarjeta debajo.</desc>
  <defs>
    <style>
      #raClonar14 .title{fill:#161A26;font-size:22px;font-weight:700}
      #raClonar14 .sub{fill:#79809A;font-size:13.5px}
      #raClonar14 .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #raClonar14 .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #raClonar14 .pf{fill:#7F8AA3} #raClonar14 .cmd{fill:#FFFFFF;font-weight:600}
      #raClonar14 .dim{fill:#8A93A6} #raClonar14 .okk{fill:#6BCB77;font-weight:600}
      #raClonar14 .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #raClonar14 .chipc{fill:#F2C069} #raClonar14 .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #raClonar14 .ct{fill:#161A26;font-size:14px;font-weight:700}
      #raClonar14 .cb{fill:#454C61;font-size:13px}
      #raClonar14 .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="590" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Clonar el repositorio de la sesión 14</text>
  <text class="sub" x="48" y="80" data-fit="860">Cuatro comandos, desde la carpeta donde guardas tus proyectos.</text>
  <rect x="48" y="112" width="864" height="320" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">git clone https://github.com/Domiciano/262SeminarioSesion14.git</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="200" data-fit="816">Cloning into '262SeminarioSesion14'...</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">cd 262SeminarioSesion14</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816"><tspan class="pf">262SeminarioSesion14&gt; </tspan><tspan class="cmd">flutter pub get</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="304" data-fit="816">Resolving dependencies...</text>
  <text class="tl mono okk" font-size="13" x="72" y="330" data-fit="816">Got dependencies!</text>
  <text class="tl mono" font-size="13" x="72" y="382" data-fit="816"><tspan class="pf">262SeminarioSesion14&gt; </tspan><tspan class="cmd">flutter run -d chrome</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="408" data-fit="816">Launching lib/main.dart on Chrome in debug mode...</text>
  <rect class="ring" x="216.2" y="158" width="421.4" height="22" rx="5"/>
  <circle class="chipc" cx="637.6" cy="159" r="8"/>
  <text class="chipt" x="637.6" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="239.6" y="262" width="125.0" height="22" rx="5"/>
  <circle class="chipc" cx="364.6" cy="263" r="8"/>
  <text class="chipt" x="364.6" y="263" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <rect class="ring" x="239.6" y="366" width="171.8" height="22" rx="5"/>
  <circle class="chipc" cx="411.4" cy="367" r="8"/>
  <text class="chipt" x="411.4" y="367" dy="0.35em" text-anchor="middle" font-size="10.5">3</text>
  <g transform="translate(48.0,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">La dirección</text>
    <text class="cb" x="16" y="60" data-fit="245">Copia el proyecto en una</text>
    <text class="cb" x="16" y="79" data-fit="245">carpeta nueva con su nombre.</text>
  </g>
  <g transform="translate(341.3,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">flutter pub get</text>
    <text class="cb" x="16" y="60" data-fit="245">Baja los paquetes. Sin él,</text>
    <text class="cb" x="16" y="79" data-fit="245">el editor marca errores.</text>
  </g>
  <g transform="translate(634.7,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">3</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">flutter run</text>
    <text class="cb" x="16" y="60" data-fit="245">Abre la app en Chrome. Si</text>
    <text class="cb" x="16" y="79" data-fit="245">la ves, ya puedes empezar.</text>
  </g>
</svg>
```

```shell
git clone https://github.com/Domiciano/262SeminarioSesion14.git
cd 262SeminarioSesion14
flutter pub get
flutter run -d chrome
```

Ábrelo en VS Code con *File › Open Folder* y elige la carpeta `262SeminarioSesion14`. Antes de correrlo, pega en `lib/main.dart` la Project URL y la publishable key del proyecto de Supabase de tu equipo, como en la sesión 13.

## Las pantallas

```svg
<svg id="fpPantallas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpPantallas-ttl fpPantallas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpPantallas-ttl">De dónde sale y a dónde va la foto</title>
  <desc id="fpPantallas-dsc">Tres teléfonos en fila. HomeScreen con la lista de tracks y, arriba a la derecha, el botón de perfil con la inicial A. ProfileScreen con un círculo grande con la A, el nombre Ana Gómez, el correo y un botón punteado Cambiar foto. El tercero es el mismo perfil oscurecido con un panel que sube desde abajo: Cambiar foto de perfil, con Elegir de la galería (T-09), Tomar una foto (T-11) y Mis fotos anteriores (T-12). Flechas: el botón de perfil abre ProfileScreen con pushNamed y Cambiar foto abre el panel.</desc>
  <defs>
    <style>
      #fpPantallas .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpPantallas .sub{fill:#79809A;font-size:13.5px}
      #fpPantallas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #fpPantallas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #fpPantallas .nb{fill:#454C61;font-size:13px}
      #fpPantallas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fpPantallas .foot{fill:#79809A;font-size:12px}
      #fpPantallas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpPantallas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fpPantallas-arrow)}
    </style>
    <marker id="fpPantallas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="620" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">De dónde sale y a dónde va la foto</text>
  <text class="sub" x="48" y="80" data-fit="860">La lista y el perfil ya vienen. Lo punteado es lo que hace el implementador en el taller.</text>
<rect x="56" y="132" width="216" height="316" rx="26" fill="#1F2430"/><rect x="64" y="140" width="200" height="300" rx="18" fill="#FEF7FF"/><path d="M64,158 A18,18 0 0 1 82,140 H246 A18,18 0 0 1 264,158 V184 H64 Z" fill="#D0BCFF"/><text x="78" y="169" font-size="13.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="150">Mis tracks</text><rect x="78" y="198" width="172" height="30" rx="15" fill="#6750A4"/><text x="164" y="217.5" font-size="12.5" font-weight="600" fill="#FFFFFF" text-anchor="middle" data-fit="115">+ Crear track</text><rect x="78" y="242" width="172" height="48" rx="10" fill="#FFFFFF" stroke="#E3E3EA"/><rect x="86" y="250" width="32" height="32" rx="7" fill="#B69DF8"/><text x="126" y="263" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="110">Yellow</text><text x="126" y="279" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="110">Coldplay</text><rect x="78" y="300" width="172" height="48" rx="10" fill="#FFFFFF" stroke="#E3E3EA"/><rect x="86" y="308" width="32" height="32" rx="7" fill="#B69DF8"/><text x="126" y="321" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="110">Clocks</text><text x="126" y="337" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="110">Coldplay</text><rect x="78" y="358" width="172" height="48" rx="10" fill="#FFFFFF" stroke="#E3E3EA"/><rect x="86" y="366" width="32" height="32" rx="7" fill="#B69DF8"/><text x="126" y="379" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="110">Bohemian…</text><text x="126" y="395" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="110">Queen</text><circle cx="214" cy="162" r="12" fill="#E8DEF8"/><text x="214" y="166.08" font-size="10.8" font-weight="700" fill="#6750A4" text-anchor="middle" data-fit="30">A</text><path d="M244,154 h-6 v16 h6 M248,158 l4,4 -4,4 M252,162 h-9" fill="none" stroke="#161A26" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><rect x="127.8" y="458" width="72.4" height="24" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.2"/><text x="164.0" y="474.5" font-size="12" font-weight="700" fill="#7439B8" text-anchor="middle" class="mono" data-fit="74">'/home'</text><text x="164" y="122" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="105">HomeScreen</text><rect x="198" y="146" width="32" height="32" rx="8" fill="none" stroke="#C2354F" stroke-width="2" stroke-dasharray="4 3"/><rect x="224.6" y="110" width="50.8" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="250" y="126.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" class="mono" data-fit="52">T-10</text><rect x="372" y="132" width="216" height="316" rx="26" fill="#1F2430"/><rect x="380" y="140" width="200" height="300" rx="18" fill="#FEF7FF"/><path d="M380,158 A18,18 0 0 1 398,140 H562 A18,18 0 0 1 580,158 V184 H380 Z" fill="#D0BCFF"/><text x="394" y="169" font-size="13.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="150">← Mi perfil</text><circle cx="480" cy="244" r="40" fill="#E8DEF8"/><text x="480" y="257.6" font-size="36.0" font-weight="700" fill="#6750A4" text-anchor="middle" data-fit="44">A</text><text x="480" y="312" font-size="15" font-weight="700" fill="#161A26" text-anchor="middle" data-fit="99">Ana Gómez</text><text x="480" y="332" font-size="12" font-weight="400" fill="#556074" text-anchor="middle" data-fit="118">ana@correo.com</text><rect x="428" y="350" width="104" height="28" rx="14" fill="#FFFFFF" stroke="#6750A4" stroke-width="1.5" stroke-dasharray="5 4"/><text x="480" y="368.5" font-size="12" font-weight="600" fill="#6750A4" text-anchor="middle" data-fit="104">Cambiar foto</text><rect x="433.0" y="458" width="94.0" height="24" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.2"/><text x="480.0" y="474.5" font-size="12" font-weight="700" fill="#7439B8" text-anchor="middle" class="mono" data-fit="96">'/profile'</text><text x="480" y="122" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="129">ProfileScreen</text><rect x="688" y="132" width="216" height="316" rx="26" fill="#1F2430"/><rect x="696" y="140" width="200" height="300" rx="18" fill="#FEF7FF"/><path d="M696,158 A18,18 0 0 1 714,140 H878 A18,18 0 0 1 896,158 V184 H696 Z" fill="#D0BCFF"/><text x="710" y="169" font-size="13.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="150">← Mi perfil</text><circle cx="796" cy="244" r="40" fill="#E8DEF8"/><text x="796" y="257.6" font-size="36.0" font-weight="700" fill="#6750A4" text-anchor="middle" data-fit="44">A</text><text x="796" y="312" font-size="15" font-weight="700" fill="#161A26" text-anchor="middle" data-fit="99">Ana Gómez</text><text x="796" y="332" font-size="12" font-weight="400" fill="#556074" text-anchor="middle" data-fit="118">ana@correo.com</text><rect x="744" y="350" width="104" height="28" rx="14" fill="#FFFFFF" stroke="#6750A4" stroke-width="1.5" stroke-dasharray="5 4"/><text x="796" y="368.5" font-size="12" font-weight="600" fill="#6750A4" text-anchor="middle" data-fit="104">Cambiar foto</text><rect x="696" y="140" width="200" height="300" rx="18" fill="#161A26" opacity=".45"/><path d="M696,288 A16,16 0 0 1 712,272 H880 A16,16 0 0 1 896,288 V422 A18,18 0 0 1 878,440 H714 A18,18 0 0 1 696,422 Z" fill="#FFFFFF"/><rect x="780" y="280" width="32" height="4" rx="2" fill="#C4CBD8"/><text x="712" y="308" font-size="13" font-weight="700" fill="#161A26" text-anchor="start" data-fit="170">Cambiar foto de perfil</text><rect x="710" y="328" width="18" height="16" rx="3" fill="none" stroke="#161A26" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><path d="M712,341 l5,-6 4,4 2,-2 3,4" fill="none" stroke="#161A26" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><text x="736" y="341" font-size="11.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="112">Elegir de la galería</text><rect x="846.6" y="324" width="50.8" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="872" y="340.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" class="mono" data-fit="52">T-09</text><path d="M710,368 h4 l2,-3 h6 l2,3 h4 v12 h-18 Z" fill="none" stroke="#161A26" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="719" cy="374" r="3.5" fill="none" stroke="#161A26" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><text x="736" y="377" font-size="11.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="112">Tomar una foto</text><rect x="846.6" y="360" width="50.8" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="872" y="376.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" class="mono" data-fit="52">T-11</text><circle cx="719" cy="409" r="8" fill="none" stroke="#161A26" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><path d="M719,404 v5 l3,2" fill="none" stroke="#161A26" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><text x="736" y="413" font-size="11.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="112">Mis fotos anteriores</text><rect x="846.6" y="396" width="50.8" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="872" y="412.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" class="mono" data-fit="52">T-12</text><rect x="713.0" y="458" width="166.0" height="24" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.2"/><text x="796.0" y="474.5" font-size="12" font-weight="700" fill="#7439B8" text-anchor="middle" class="mono" data-fit="168">showModalBottomSheet</text><text x="796" y="122" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="middle" data-fit="152">el panel de abajo</text><path class="link" d="M226,176 C314,200 320,244 368,244"/><rect x="278.6" y="208" width="86.8" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="322" y="224.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono" data-fit="88">pushNamed</text><path class="link" d="M536,364 H684"/><g><rect x="48" y="520" width="864" height="44" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/></g><text x="480" y="547" font-size="12.5" font-weight="600" fill="#454C61" text-anchor="middle" data-fit="840">Ya viene: el botón de perfil con la inicial y ProfileScreen. En rojo, la tarea del implementador que lo completa.</text><text x="48" y="592" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">La inicial sale del nombre del perfil. Cuando haya foto, ProfileAvatar muestra la foto en su lugar.</text></svg>
```

La lista tiene un botón nuevo en la barra, con la inicial de tu nombre. Abre `ProfileScreen`, que muestra tu nombre, tu correo y la misma inicial en grande. Cambiar la foto todavía no existe: es el taller.

## Qué trae

```svg
<svg id="fpCarpetas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 564" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpCarpetas-ttl fpCarpetas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpCarpetas-ttl">Lo que trae el repositorio</title>
  <desc id="fpCarpetas-dsc">Árbol del repositorio: .agents/skills y .claude/skills con las mismas once skills, AGENTS.md y CLAUDE.md, docs con el PRD, los requisitos, la spine, specs F-01 a F-04, tecnicas TS-01 a TS-04, impl_progress.md con 8 de 12 tareas hechas y standard_code.md, y en lib el componente profile_avatar y la pantalla profile_screen.</desc>
  <defs>
    <style>
      #fpCarpetas .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpCarpetas .sub{fill:#79809A;font-size:13.5px}
      #fpCarpetas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #fpCarpetas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #fpCarpetas .nb{fill:#454C61;font-size:13px}
      #fpCarpetas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fpCarpetas .foot{fill:#79809A;font-size:12px}
      #fpCarpetas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpCarpetas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fpCarpetas-arrow)}
    </style>
    <marker id="fpCarpetas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="564" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Lo que trae el repositorio</text>
  <text class="sub" x="48" y="80" data-fit="860">La app de la sesión 13 resuelta, el perfil, las specs y las skills para Antigravity y para Claude.</text>
<rect x="48" y="112" width="864" height="388" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><path d="M72,127 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="100" y="140" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="194">262SeminarioSesion14/</text><path d="M100,153 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="166" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="145">.agents/skills/</text><rect x="600.0" y="150" width="203.4" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="701.72" y="166.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="205">Antigravity CLI · 11 skills</text><path d="M100,179 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="192" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="145">.claude/skills/</text><rect x="600.0" y="176" width="203.4" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="701.72" y="192.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="205">Claude Code · las mismas 11</text><rect x="102" y="203" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="128" y="218" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="194">AGENTS.md · CLAUDE.md</text><rect x="600.0" y="202" width="237.0" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="718.52" y="218.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="239">CLAUDE.md solo importa AGENTS.md</text><path d="M100,231 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="244" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="64">docs/</text><rect x="130" y="255" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="270" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="267">prd.md · requisitos.md · spine</text><rect x="600.0" y="254" width="176.6" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="688.28" y="270.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="178">de las sesiones 10 y 11</text><path d="M128,283 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="156" y="296" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="72">specs/</text><rect x="600.0" y="280" width="203.4" height="24" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.2"/><text x="701.72" y="296.5" font-size="12" font-weight="700" fill="#7439B8" text-anchor="middle" data-fit="205">F-01 a F-04, sin tecnología</text><path d="M128,309 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="156" y="322" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="96">tecnicas/</text><rect x="600.0" y="306" width="216.9" height="24" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.2"/><text x="708.44" y="322.5" font-size="12" font-weight="700" fill="#0F8478" text-anchor="middle" data-fit="218">TS-01 a TS-04, con sus tareas</text><rect x="130" y="333" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="348" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="153">impl_progress.md</text><rect x="600.0" y="332" width="163.1" height="24" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="681.56" y="348.5" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle" data-fit="165">8 de 12 tareas hechas</text><rect x="130" y="359" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="374" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="153">standard_code.md</text><rect x="600.0" y="358" width="163.1" height="24" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.2"/><text x="681.56" y="374.5" font-size="12" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="165">las reglas del código</text><path d="M100,387 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="400" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="56">lib/</text><rect x="130" y="411" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="426" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="267">components/profile_avatar.dart</text><rect x="600.0" y="410" width="156.4" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="678.2" y="426.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="158">la foto o la inicial</text><rect x="130" y="437" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="452" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="242">screens/profile_screen.dart</text><rect x="600.0" y="436" width="176.6" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="688.28" y="452.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="178">nombre, correo y avatar</text><rect x="130" y="463" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="478" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="267">services/ · models/ · screens/</text><rect x="600.0" y="462" width="203.4" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="701.72" y="478.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="205">la solución de la sesión 13</text></svg>
```

- **Las skills, dos veces.** `.agents/skills/` es la carpeta que lee Antigravity CLI y `.claude/skills/` la que lee Claude Code. Tienen las mismas once: las del curso, las cinco de Spec Driven Development y dos nuevas, `sdd-tecnicas` y `sdd-implementar`.
- **`AGENTS.md` y `CLAUDE.md`.** `CLAUDE.md` tiene una sola línea, `@AGENTS.md`: así los dos agentes leen el mismo contexto.
- **`docs/`.** El PRD, los requisitos y la spine, las specs funcionales `F-01` a `F-04`, las técnicas `TS-01` a `TS-04`, `impl_progress.md` y `standard_code.md`.
- **`ProfileAvatar`.** Un componente que pinta la foto si hay URL y la inicial si no.

## Lo que falta

Abre `docs/impl_progress.md`: 8 de las 12 tareas están marcadas `[x]`. Las cuatro que faltan, `T-09` a `T-12`, son la foto de perfil de `F-04`. En el taller no las escribes tú: se las pides al implementador.
