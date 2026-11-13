# Repositorio de arranque

<!-- tags: 262SeminarioSesion13, git clone, flutter pub get, initialRoute, LoginScreen, SignupScreen, AuthService, ProfileService, Target of URI doesn't exist -->

El taller de esta sesión sigue sobre la app de tracks de la sesión 12, ya resuelta: guarda, lista y borra tracks en Supabase. Esta versión le agrega lo que falta para que cada persona tenga su cuenta. Clónala aparte, fuera de la carpeta de tu proyecto.

```svg
<svg id="raClonar13" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 590" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="raClonar13-ttl raClonar13-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="raClonar13-ttl">Clonar el repositorio de la sesión 13</title>
  <desc id="raClonar13-dsc">Una terminal parada en la carpeta develop. Primero git clone con la dirección de 262SeminarioSesion13, que crea la carpeta 262SeminarioSesion13. Después cd 262SeminarioSesion13, flutter pub get, que termina con Got dependencies, y flutter run -d chrome, que abre la app en Chrome. Tres recuadros numerados señalan la dirección del repositorio, flutter pub get y flutter run, cada uno con su tarjeta debajo.</desc>
  <defs>
    <style>
      #raClonar13 .title{fill:#161A26;font-size:22px;font-weight:700}
      #raClonar13 .sub{fill:#79809A;font-size:13.5px}
      #raClonar13 .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #raClonar13 .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #raClonar13 .pf{fill:#7F8AA3} #raClonar13 .cmd{fill:#FFFFFF;font-weight:600}
      #raClonar13 .dim{fill:#8A93A6} #raClonar13 .okk{fill:#6BCB77;font-weight:600}
      #raClonar13 .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #raClonar13 .chipc{fill:#F2C069} #raClonar13 .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #raClonar13 .ct{fill:#161A26;font-size:14px;font-weight:700}
      #raClonar13 .cb{fill:#454C61;font-size:13px}
      #raClonar13 .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="590" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Clonar el repositorio de la sesión 13</text>
  <text class="sub" x="48" y="80" data-fit="860">Cuatro comandos, desde la carpeta donde guardas tus proyectos.</text>
  <rect x="48" y="112" width="864" height="320" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">git clone https://github.com/Domiciano/262SeminarioSesion13.git</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="200" data-fit="816">Cloning into '262SeminarioSesion13'...</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">cd 262SeminarioSesion13</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816"><tspan class="pf">262SeminarioSesion13&gt; </tspan><tspan class="cmd">flutter pub get</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="304" data-fit="816">Resolving dependencies...</text>
  <text class="tl mono okk" font-size="13" x="72" y="330" data-fit="816">Got dependencies!</text>
  <text class="tl mono" font-size="13" x="72" y="382" data-fit="816"><tspan class="pf">262SeminarioSesion13&gt; </tspan><tspan class="cmd">flutter run -d chrome</tspan></text>
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
git clone https://github.com/Domiciano/262SeminarioSesion13.git
cd 262SeminarioSesion13
flutter pub get
flutter run -d chrome
```

Ábrelo en VS Code con *File › Open Folder* y elige la carpeta `262SeminarioSesion13`. Si el editor marca en rojo los `import` con `Target of URI doesn't exist`, falta el `flutter pub get`.

## Las pantallas

```svg
<svg id="auPantallas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 610" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="auPantallas-ttl auPantallas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="auPantallas-ttl">Tres pantallas y una ruta inicial</title>
  <desc id="auPantallas-dsc">Tres teléfonos en fila. LoginScreen, marcada como initialRoute /login, con correo, contraseña, el botón Entrar y el enlace Regístrate. SignupScreen con nombre, correo, contraseña, repetirla y Crear cuenta. HomeScreen con la lista de tracks y el ícono de cerrar sesión. Flechas: Regístrate abre el registro con pushNamed; Entrar y Crear cuenta llevan a la lista con pushNamedAndRemoveUntil; cerrar sesión vuelve al login de la misma forma.</desc>
  <defs>
    <style>
      #auPantallas .title{fill:#161A26;font-size:22px;font-weight:700}
      #auPantallas .sub{fill:#79809A;font-size:13.5px}
      #auPantallas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #auPantallas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #auPantallas .nb{fill:#454C61;font-size:13px}
      #auPantallas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #auPantallas .foot{fill:#79809A;font-size:12px}
      #auPantallas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #auPantallas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#auPantallas-arrow)}
    </style>
    <marker id="auPantallas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="610" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Tres pantallas y una ruta inicial</text>
  <text class="sub" x="48" y="80" data-fit="860">La app abre en el login. Del login se va al registro o a la lista.</text>
<rect x="56" y="132" width="216" height="316" rx="26" fill="#1F2430"/><rect x="64" y="140" width="200" height="300" rx="18" fill="#FEF7FF"/><text x="164" y="210" font-size="30" font-weight="700" fill="#6750A4" text-anchor="middle" data-fit="40">♪</text><text x="164" y="240" font-size="18" font-weight="700" fill="#161A26" text-anchor="middle" data-fit="84">Tracks</text><rect x="80" y="264" width="168" height="28" rx="4" fill="#FFFFFF" stroke="#79747E"/><text x="90" y="282" font-size="12" font-weight="400" fill="#79747E" text-anchor="start" data-fit="152">Correo</text><rect x="80" y="302" width="168" height="28" rx="4" fill="#FFFFFF" stroke="#79747E"/><text x="90" y="320" font-size="12" font-weight="400" fill="#79747E" text-anchor="start" data-fit="152">Contraseña</text><rect x="80" y="344" width="168" height="30" rx="15" fill="#6750A4"/><text x="164.0" y="363.5" font-size="12.5" font-weight="600" fill="#FFFFFF" text-anchor="middle" data-fit="158">Entrar</text><text x="164" y="402" font-size="12" font-weight="600" fill="#6750A4" text-anchor="middle" data-fit="180">¿No tienes cuenta? Regístrate</text><rect x="73.8" y="458" width="180.4" height="24" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.2"/><text x="164.0" y="474.5" font-size="12" font-weight="700" fill="#7439B8" text-anchor="middle" class="mono" data-fit="182">initialRoute: '/login'</text><text x="164" y="122" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="113">LoginScreen</text><rect x="372" y="132" width="216" height="316" rx="26" fill="#1F2430"/><rect x="380" y="140" width="200" height="300" rx="18" fill="#FEF7FF"/><path d="M380,158 A18,18 0 0 1 398,140 H562 A18,18 0 0 1 580,158 V184 H380 Z" fill="#D0BCFF"/><text x="394" y="169" font-size="13.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="150">← Crear cuenta</text><rect x="396" y="200" width="168" height="28" rx="4" fill="#FFFFFF" stroke="#79747E"/><text x="406" y="218" font-size="12" font-weight="400" fill="#79747E" text-anchor="start" data-fit="152">Nombre</text><rect x="396" y="238" width="168" height="28" rx="4" fill="#FFFFFF" stroke="#79747E"/><text x="406" y="256" font-size="12" font-weight="400" fill="#79747E" text-anchor="start" data-fit="152">Correo</text><rect x="396" y="276" width="168" height="28" rx="4" fill="#FFFFFF" stroke="#79747E"/><text x="406" y="294" font-size="12" font-weight="400" fill="#79747E" text-anchor="start" data-fit="152">Contraseña</text><rect x="396" y="314" width="168" height="28" rx="4" fill="#FFFFFF" stroke="#79747E"/><text x="406" y="332" font-size="12" font-weight="400" fill="#79747E" text-anchor="start" data-fit="152">Repite la contraseña</text><rect x="396" y="362" width="168" height="30" rx="15" fill="#6750A4"/><text x="480.0" y="381.5" font-size="12.5" font-weight="600" fill="#FFFFFF" text-anchor="middle" data-fit="158">Crear cuenta</text><rect x="436.6" y="458" width="86.8" height="24" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.2"/><text x="480.0" y="474.5" font-size="12" font-weight="700" fill="#7439B8" text-anchor="middle" class="mono" data-fit="88">'/signup'</text><text x="480" y="122" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="121">SignupScreen</text><rect x="688" y="132" width="216" height="316" rx="26" fill="#1F2430"/><rect x="696" y="140" width="200" height="300" rx="18" fill="#FEF7FF"/><path d="M696,158 A18,18 0 0 1 714,140 H878 A18,18 0 0 1 896,158 V184 H696 Z" fill="#D0BCFF"/><text x="710" y="169" font-size="13.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="150">Mis tracks</text><rect x="710" y="198" width="172" height="30" rx="15" fill="#6750A4"/><text x="796" y="217.5" font-size="12.5" font-weight="600" fill="#FFFFFF" text-anchor="middle" data-fit="115">+ Crear track</text><rect x="710" y="242" width="172" height="48" rx="10" fill="#FFFFFF" stroke="#E3E3EA"/><rect x="718" y="250" width="32" height="32" rx="7" fill="#B69DF8"/><text x="758" y="263" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="110">Yellow</text><text x="758" y="279" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="110">Coldplay</text><rect x="710" y="300" width="172" height="48" rx="10" fill="#FFFFFF" stroke="#E3E3EA"/><rect x="718" y="308" width="32" height="32" rx="7" fill="#B69DF8"/><text x="758" y="321" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="110">Clocks</text><text x="758" y="337" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="110">Coldplay</text><rect x="710" y="358" width="172" height="48" rx="10" fill="#FFFFFF" stroke="#E3E3EA"/><rect x="718" y="366" width="32" height="32" rx="7" fill="#B69DF8"/><text x="758" y="379" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="110">Bohemian…</text><text x="758" y="395" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="110">Queen</text><path d="M874,154 h-6 v16 h6 M878,158 l4,4 -4,4 M882,162 h-9" fill="none" stroke="#161A26" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><rect x="759.8" y="458" width="72.4" height="24" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.2"/><text x="796.0" y="474.5" font-size="12" font-weight="700" fill="#7439B8" text-anchor="middle" class="mono" data-fit="74">'/home'</text><text x="796" y="122" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="105">HomeScreen</text><path class="link" d="M260,402 C314,402 310,280 368,280"/><rect x="278.6" y="244" width="86.8" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="322" y="260.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono" data-fit="88">pushNamed</text><path class="link" d="M572,377 H684"/><g><rect x="48" y="512" width="864" height="44" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/></g><text x="480" y="539" font-size="12.5" font-weight="600" fill="#A96C05" text-anchor="middle" data-fit="840">Entrar, Crear cuenta y cerrar sesión navegan con pushNamedAndRemoveUntil: la pila queda con una sola pantalla.</text><text x="48" y="582" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Hoy los botones navegan sin preguntarle nada a Supabase: en el taller cada uno llama a su servicio.</text></svg>
```

La app ya no abre en la lista: `initialRoute` es `'/login'`. Desde el login se llega al registro con *Regístrate*, y a la lista con *Entrar*. La lista tiene en la barra el botón de cerrar sesión.

## Qué trae

```svg
<svg id="auCarpetas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 534" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="auCarpetas-ttl auCarpetas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="auCarpetas-ttl">Lo que trae el repositorio</title>
  <desc id="auCarpetas-dsc">Árbol de lib: main.dart con las cinco rutas e initialRoute /login, models con track y profile, components con login_form, signup_form y los de tracks, screens con login, signup, home y las dos de tracks, y services con auth_service y profile_service vacíos y track_services completo.</desc>
  <defs>
    <style>
      #auCarpetas .title{fill:#161A26;font-size:22px;font-weight:700}
      #auCarpetas .sub{fill:#79809A;font-size:13.5px}
      #auCarpetas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #auCarpetas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #auCarpetas .nb{fill:#454C61;font-size:13px}
      #auCarpetas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #auCarpetas .foot{fill:#79809A;font-size:12px}
      #auCarpetas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #auCarpetas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#auCarpetas-arrow)}
    </style>
    <marker id="auCarpetas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="534" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Lo que trae el repositorio</text>
  <text class="sub" x="48" y="80" data-fit="860">Lo de la sesión 12, ya resuelto, más el login, el registro y dos servicios vacíos.</text>
<rect x="48" y="112" width="864" height="414" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><path d="M72,127 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="100" y="140" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="56">lib/</text><rect x="102" y="151" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="128" y="166" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="96">main.dart</text><rect x="600.0" y="150" width="169.8" height="24" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.2"/><text x="684.92" y="166.5" font-size="12" font-weight="700" fill="#7439B8" text-anchor="middle" data-fit="171">initialRoute: '/login'</text><path d="M100,179 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="192" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="80">models/</text><rect x="130" y="203" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="218" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="105">track.dart</text><rect x="600.0" y="202" width="122.8" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="661.4" y="218.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="124">de la sesión 12</text><rect x="130" y="229" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="244" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="121">profile.dart</text><rect x="600.0" y="228" width="183.3" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="691.64" y="244.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="185">Profile: id, name, email</text><path d="M100,257 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="270" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="113">components/</text><rect x="130" y="281" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="296" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="299">login_form.dart · signup_form.dart</text><rect x="600.0" y="280" width="183.3" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="691.64" y="296.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="185">el borrador y sus avisos</text><rect x="130" y="307" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="322" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="315">track_card · track_list · track_form</text><rect x="600.0" y="306" width="122.8" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="661.4" y="322.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="124">de la sesión 12</text><path d="M100,335 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="348" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="88">screens/</text><rect x="130" y="359" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="374" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="331">login_screen.dart · signup_screen.dart</text><rect x="600.0" y="358" width="163.1" height="24" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.2"/><text x="681.56" y="374.5" font-size="12" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="165">navegan sin preguntar</text><rect x="130" y="385" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="400" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="153">home_screen.dart</text><rect x="600.0" y="384" width="216.9" height="24" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.2"/><text x="708.44" y="400.5" font-size="12" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="218">con el botón de cerrar sesión</text><path d="M100,413 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="426" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="96">services/</text><rect x="130" y="437" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="452" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="161">auth_service.dart</text><rect x="600.0" y="436" width="149.7" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="674.84" y="452.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" data-fit="151">vacío: lo completas</text><rect x="130" y="463" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="478" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="186">profile_service.dart</text><rect x="600.0" y="462" width="149.7" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="674.84" y="478.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" data-fit="151">vacío: lo completas</text><rect x="130" y="489" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="504" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="177">track_services.dart</text><rect x="600.0" y="488" width="190.0" height="24" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="695.0" y="504.5" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle" data-fit="192">completo, de la sesión 12</text></svg>
```

- **`LoginForm` y `SignupForm`**: los formularios. Guardan el borrador y avisan si falta un campo, si la contraseña tiene menos de 6 caracteres o si las dos contraseñas no coinciden. Al enviar, suben los datos con `onLogin` y `onSignup`.
- **`LoginScreen` y `SignupScreen`**: reciben esos datos en `_login` y `_signup`, y por ahora solo navegan a `'/home'`.
- **`Profile`**: `id`, `name` y `email`, con `fromMap`, `toMap` y `copyWith`, como `Track`.
- **`TrackService`**: completo, como quedó al final de la sesión 12.

## Lo que falta

*Entrar* deja pasar a cualquiera, aunque los campos tengan cualquier cosa, y *Crear cuenta* no crea nada. `lib/services/auth_service.dart` y `lib/services/profile_service.dart` traen sus métodos, pero vacíos. En el taller los completas y los invocas desde las pantallas.

Antes de correr el taller, pega en `lib/main.dart` la Project URL y la publishable key de tu proyecto, como en la sesión 12.
