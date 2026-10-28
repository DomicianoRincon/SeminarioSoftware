# Repositorio de arranque

<!-- tags: git clone, repositorio de arranque, punto de partida de la sesión, 262SeminarioSesion3, flutter pub get, flutter run -d chrome, Target of URI doesn't exist -->

La sesión 3 arranca donde terminó la sesión 2. Si tu proyecto llegó hasta ahí, sigue en él. Si no alcanzaste a terminar, o prefieres empezar limpio, clona este repositorio: trae exactamente ese punto de partida.

```svg
<svg id="raClonar3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 590" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="raClonar3-ttl raClonar3-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="raClonar3-ttl">Clonar el repositorio de la sesión 3</title>
  <desc id="raClonar3-dsc">Una terminal parada en la carpeta develop. Primero git clone con la dirección de 262SeminarioSesion3, que crea la carpeta 262SeminarioSesion3. Después cd 262SeminarioSesion3, flutter pub get, que termina con Got dependencies, y flutter run -d chrome, que abre la app en Chrome. Tres recuadros numerados señalan la dirección del repositorio, flutter pub get y flutter run, cada uno con su tarjeta debajo.</desc>
  <defs>
    <style>
      #raClonar3 .title{fill:#161A26;font-size:22px;font-weight:700}
      #raClonar3 .sub{fill:#79809A;font-size:13.5px}
      #raClonar3 .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #raClonar3 .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #raClonar3 .pf{fill:#7F8AA3} #raClonar3 .cmd{fill:#FFFFFF;font-weight:600}
      #raClonar3 .dim{fill:#8A93A6} #raClonar3 .okk{fill:#6BCB77;font-weight:600}
      #raClonar3 .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #raClonar3 .chipc{fill:#F2C069} #raClonar3 .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #raClonar3 .ct{fill:#161A26;font-size:14px;font-weight:700}
      #raClonar3 .cb{fill:#454C61;font-size:13px}
      #raClonar3 .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="590" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Clonar el repositorio de la sesión 3</text>
  <text class="sub" x="48" y="80" data-fit="860">Cuatro comandos, desde la carpeta donde guardas tus proyectos.</text>
  <rect x="48" y="112" width="864" height="320" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">git clone https://github.com/Domiciano/262SeminarioSesion3.git</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="200" data-fit="816">Cloning into '262SeminarioSesion3'...</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">cd 262SeminarioSesion3</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816"><tspan class="pf">262SeminarioSesion3&gt; </tspan><tspan class="cmd">flutter pub get</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="304" data-fit="816">Resolving dependencies...</text>
  <text class="tl mono okk" font-size="13" x="72" y="330" data-fit="816">Got dependencies!</text>
  <text class="tl mono" font-size="13" x="72" y="382" data-fit="816"><tspan class="pf">262SeminarioSesion3&gt; </tspan><tspan class="cmd">flutter run -d chrome</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="408" data-fit="816">Launching lib/main.dart on Chrome in debug mode...</text>
  <rect class="ring" x="216.2" y="158" width="413.6" height="22" rx="5"/>
  <circle class="chipc" cx="629.8" cy="159" r="8"/>
  <text class="chipt" x="629.8" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="231.8" y="262" width="125.0" height="22" rx="5"/>
  <circle class="chipc" cx="356.8" cy="263" r="8"/>
  <text class="chipt" x="356.8" y="263" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <rect class="ring" x="231.8" y="366" width="171.8" height="22" rx="5"/>
  <circle class="chipc" cx="403.6" cy="367" r="8"/>
  <text class="chipt" x="403.6" y="367" dy="0.35em" text-anchor="middle" font-size="10.5">3</text>
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
git clone https://github.com/Domiciano/262SeminarioSesion3.git
cd 262SeminarioSesion3
flutter pub get
flutter run -d chrome
```

Ábrelo en VS Code con *File › Open Folder* y elige la carpeta `262SeminarioSesion3`. Si el editor marca en rojo los `import` con `Target of URI doesn't exist`, falta el `flutter pub get`.

## Qué trae

- En `lib/components/`, los componentes del taller: `PrimaryButton`, `SecondaryButton`, `StatCard`, `StatsRow`, `ProfileInfo`, `ChatItem` y `ContactCard`.
- En `lib/main.dart`, `App` con la tabla de rutas y una `HomeScreen` de prueba en `'/home'`.
- La foto de perfil en `assets/images/avatar.png`, ya declarada en `pubspec.yaml`.

El paquete se llama `mi_app_1`, así que los `import` del proyecto empiezan con `package:mi_app_1/`.
