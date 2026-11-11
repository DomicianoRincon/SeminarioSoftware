# Migraciones con el CLI de Supabase

<!-- tags: npx supabase init, supabase link, migration new, db push --remote, migración, esquema inicial, modelo de datos en AGENTS.md, Schema Visualizer, Access token not provided, unknown flag: --remote, Remote migration versions not found, permission denied for table -->

Las tablas de tu app no se crean a mano en el dashboard: se escriben en **migraciones**, archivos SQL que viven en el repositorio y que el CLI de Supabase corre en tu proyecto. Esta lección se hace **en el proyecto de tu equipo**.

## El recorrido

```svg
<svg id="mgFlujo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 388" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="mgFlujo-ttl mgFlujo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="mgFlujo-ttl">Del modelo de datos a las tablas</title>
  <desc id="mgFlujo-dsc">Cinco pasos en fila. Uno, el modelo de datos del equipo vive en docs. Dos, AGENTS.md dice dónde está. Tres, supabase migration new crea un archivo SQL vacío. Cuatro, el agente escribe el SQL a partir del modelo. Cinco, db push remote crea las tablas en Supabase. Debajo, una nota: tú revisas el SQL antes del push.</desc>
  <defs>
    <style>
      #mgFlujo .title{fill:#161A26;font-size:22px;font-weight:700}
      #mgFlujo .sub{fill:#79809A;font-size:13.5px}
      #mgFlujo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #mgFlujo .nt{font-size:15px;font-weight:700;fill:#161A26}
      #mgFlujo .nb{fill:#454C61;font-size:13px}
      #mgFlujo .lbl{fill:#556074;font-size:12px;font-weight:600}
      #mgFlujo .foot{fill:#79809A;font-size:12px}
      #mgFlujo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #mgFlujo .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#mgFlujo-arrow)}
    </style>
    <marker id="mgFlujo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="388" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Del modelo de datos a las tablas</text>
  <text class="sub" x="48" y="80" data-fit="860">Tú creas el archivo vacío; el agente lo llena leyendo tu modelo.</text>
<g><rect x="48" y="128" width="152" height="150" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><circle cx="76" cy="155" r="13" fill="#FFFFFF" stroke="#556074" stroke-width="2"/><text x="76" y="159.5" font-size="13" font-weight="700" fill="#556074" text-anchor="middle" data-fit="31">1</text><text x="98" y="160" font-size="13.5" font-weight="700" fill="#556074" text-anchor="start" data-fit="94">El modelo</text><text x="64" y="186" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">docs/modelo.pdf</text><text x="64" y="205" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">o el MER de la</text><text x="64" y="224" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">entrega 1.</text></g><path class="link" d="M202,203 H224"/><g><rect x="226" y="128" width="152" height="150" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="254" cy="155" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="254" y="159.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="31">2</text><text x="276" y="160" font-size="13.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="94">AGENTS.md</text><text x="242" y="186" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">Dice dónde está</text><text x="242" y="205" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">el modelo y cómo</text><text x="242" y="224" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">se escriben las</text><text x="242" y="243" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">migraciones.</text></g><path class="link" d="M380,203 H402"/><g><rect x="404" y="128" width="152" height="150" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="432" cy="155" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="432" y="159.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="31">3</text><text x="454" y="160" font-size="13.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="94">migration new</text><text x="420" y="186" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">Crea un .sql</text><text x="420" y="205" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">vacío en</text><text x="420" y="224" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">supabase/</text><text x="420" y="243" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">migrations/.</text></g><path class="link" d="M558,203 H580"/><g><rect x="582" y="128" width="152" height="150" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><circle cx="610" cy="155" r="13" fill="#FFFFFF" stroke="#7439B8" stroke-width="2"/><text x="610" y="159.5" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle" data-fit="31">4</text><text x="632" y="160" font-size="13.5" font-weight="700" fill="#7439B8" text-anchor="start" data-fit="94">El agente</text><text x="598" y="186" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">Lee el modelo y</text><text x="598" y="205" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">escribe el SQL</text><text x="598" y="224" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">en ese archivo.</text></g><path class="link" d="M736,203 H758"/><g><rect x="760" y="128" width="152" height="150" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><circle cx="788" cy="155" r="13" fill="#FFFFFF" stroke="#3A8235" stroke-width="2"/><text x="788" y="159.5" font-size="13" font-weight="700" fill="#3A8235" text-anchor="middle" data-fit="31">5</text><text x="810" y="160" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="94">db push</text><text x="776" y="186" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">Corre el SQL en</text><text x="776" y="205" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">tu proyecto: las</text><text x="776" y="224" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">tablas aparecen</text><text x="776" y="243" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="128">en Supabase.</text></g><g><rect x="48" y="300" width="864" height="48" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/></g><text x="68" y="329" font-size="13" font-weight="600" fill="#C2354F" text-anchor="start" data-fit="830">Entre el paso 4 y el 5 lees el SQL. Lo que se sube a la base de datos es responsabilidad tuya, no del agente.</text></svg>
```

Tú creas el archivo vacío, el agente lo llena a partir del modelo de datos de la entrega 1, tú lo revisas y lo subes.

## 1. Conectar con tu proyecto

Necesitas el Project ID y la contraseña de la base de datos del proyecto de tu equipo, los de [Primeros pasos con Supabase](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0080).

Necesitas también Node.js (`node --version`): todos los comandos empiezan por `npx supabase`, sin instalar nada más. La primera vez, `npx` pregunta si puede descargar el paquete: responde `y`.

```svg
<svg id="mgInit" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 590" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="mgInit-ttl mgInit-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="mgInit-ttl">Conectar el proyecto con Supabase</title>
  <desc id="mgInit-dsc">Una terminal en la carpeta del proyecto del equipo, mi_app. npx supabase init termina con Finished supabase init. npx supabase login abre el navegador y termina con You are now logged in. npx supabase link con el project ref termina con Finished supabase link. Tres recuadros señalan init, login y el project ref.</desc>
  <defs>
    <style>
      #mgInit .title{fill:#161A26;font-size:22px;font-weight:700}
      #mgInit .sub{fill:#79809A;font-size:13.5px}
      #mgInit .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #mgInit .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #mgInit .pf{fill:#7F8AA3} #mgInit .cmd{fill:#FFFFFF;font-weight:600}
      #mgInit .dim{fill:#8A93A6} #mgInit .okk{fill:#6BCB77;font-weight:600}
      #mgInit .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #mgInit .chipc{fill:#F2C069} #mgInit .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #mgInit .ct{fill:#161A26;font-size:14px;font-weight:700}
      #mgInit .cb{fill:#454C61;font-size:13px}
      #mgInit .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="590" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Conectar el proyecto con Supabase</text>
  <text class="sub" x="48" y="80" data-fit="860">Tres comandos, una sola vez por proyecto. Siempre desde la carpeta raíz de tu app.</text>
  <rect x="48" y="112" width="864" height="320" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\mi_app</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">mi_app&gt; </tspan><tspan class="cmd">npx supabase init</tspan></text>
  <text class="tl mono okk" font-size="13" x="72" y="200" data-fit="816">Finished supabase init.</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816"><tspan class="pf">mi_app&gt; </tspan><tspan class="cmd">npx supabase login</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="278" data-fit="816">Hit enter to open browser and login automatically.</text>
  <text class="tl mono okk" font-size="13" x="72" y="304" data-fit="816">You are now logged in. Happy coding!</text>
  <text class="tl mono" font-size="13" x="72" y="356" data-fit="816"><tspan class="pf">mi_app&gt; </tspan><tspan class="cmd">npx supabase link <tspan letter-spacing="2">-</tspan>-project-ref abcdefghijklmnopqrst</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="382" data-fit="816">Enter your database password:</text>
  <text class="tl mono okk" font-size="13" x="72" y="408" data-fit="816">Finished supabase link.</text>
  <rect class="ring" x="231.8" y="158" width="39.2" height="22" rx="5"/>
  <circle class="chipc" cx="271.0" cy="159" r="8"/>
  <text class="chipt" x="271.0" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="231.8" y="236" width="47.0" height="22" rx="5"/>
  <circle class="chipc" cx="278.8" cy="237" r="8"/>
  <text class="chipt" x="278.8" y="237" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <rect class="ring" x="380.0" y="340" width="164.0" height="22" rx="5"/>
  <circle class="chipc" cx="544.0" cy="341" r="8"/>
  <text class="chipt" x="544.0" y="341" dy="0.35em" text-anchor="middle" font-size="10.5">3</text>
  <g transform="translate(48.0,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">init</text>
    <text class="cb" x="16" y="60" data-fit="245">Crea la carpeta supabase/</text>
    <text class="cb" x="16" y="79" data-fit="245">con config.toml y migrations/.</text>
  </g>
  <g transform="translate(341.3,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">login</text>
    <text class="cb" x="16" y="60" data-fit="245">Autoriza la consola con tu</text>
    <text class="cb" x="16" y="79" data-fit="245">cuenta. Abre el navegador.</text>
  </g>
  <g transform="translate(634.7,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">3</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">El project ref</text>
    <text class="cb" x="16" y="60" data-fit="245">Las 20 letras de tu Project</text>
    <text class="cb" x="16" y="79" data-fit="245">URL. Pide la clave de la BD.</text>
  </g>
</svg>
```

```shell
npx supabase init
npx supabase login
npx supabase link --project-ref TU_PROJECT_REF
```

Lo que va antes de `>` es la carpeta en la que estás parado: no se escribe. El *project ref* son las veinte letras de tu `Project URL` (`https://abcdefghijklmnopqrst.supabase.co`). `link` pide la contraseña de la base de datos, la que pusiste al crear el proyecto.

## 2. El modelo, en el archivo de contexto

Copia el modelo de datos del equipo a `docs/` (el PDF de la entrega 1, el `docs/mer.svg` o un `docs/modelo.md`). Después agrega esta sección a `AGENTS.md` (en Claude Code el archivo se llama `CLAUDE.md`), con el nombre real de tu archivo:

```markdown
## Base de datos

- El modelo de datos está en docs/modelo.pdf. Es la fuente
  de verdad de las tablas, las columnas y las relaciones.
- Las tablas se crean con migraciones del CLI de Supabase,
  en supabase/migrations/. Nunca se editan a mano en el
  dashboard.
- Una migración que ya se subió no se edita: se crea otra.
- Tablas en plural; tablas y columnas en inglés y snake_case.
- Toda llave primaria es id uuid default gen_random_uuid().
- Cada tabla nueva lleva su permiso, después del create table:
  grant select, insert, update, delete on <tabla>
  to anon, authenticated;
```

Sin esta sección, el agente inventa las tablas a partir del nombre de tu proyecto. Con ella, lee el modelo que el equipo ya acordó.

## 3. La migración vacía

```svg
<svg id="mgNueva" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 434" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="mgNueva-ttl mgNueva-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="mgNueva-ttl">Crear la migración vacía</title>
  <desc id="mgNueva-dsc">npx supabase migration new initial_schema responde con la ruta del archivo creado, supabase/migrations/20261111140000_initial_schema.sql, y el mensaje Migration created. Un recuadro señala el nombre de la migración y otro la marca de tiempo del archivo.</desc>
  <defs>
    <style>
      #mgNueva .title{fill:#161A26;font-size:22px;font-weight:700}
      #mgNueva .sub{fill:#79809A;font-size:13.5px}
      #mgNueva .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #mgNueva .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #mgNueva .pf{fill:#7F8AA3} #mgNueva .cmd{fill:#FFFFFF;font-weight:600}
      #mgNueva .dim{fill:#8A93A6} #mgNueva .okk{fill:#6BCB77;font-weight:600}
      #mgNueva .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #mgNueva .chipc{fill:#F2C069} #mgNueva .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #mgNueva .ct{fill:#161A26;font-size:14px;font-weight:700}
      #mgNueva .cb{fill:#454C61;font-size:13px}
      #mgNueva .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="434" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Crear la migración vacía</text>
  <text class="sub" x="48" y="80" data-fit="860">El nombre lo eliges tú. La fecha y la hora delante del nombre las pone el comando.</text>
  <rect x="48" y="112" width="864" height="164" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\mi_app</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">mi_app&gt; </tspan><tspan class="cmd">npx supabase migration new initial_schema</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="200" data-fit="816">{"path":"…/supabase/migrations/</text>
  <text class="tl mono" font-size="13" x="72" y="226" data-fit="816">  20261111140000_initial_schema.sql",</text>
  <text class="tl mono okk" font-size="13" x="72" y="252" data-fit="816"> "message":"Migration created"}</text>
  <rect class="ring" x="341.0" y="158" width="117.2" height="22" rx="5"/>
  <circle class="chipc" cx="458.2" cy="159" r="8"/>
  <text class="chipt" x="458.2" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="83.6" y="210" width="117.2" height="22" rx="5"/>
  <circle class="chipc" cx="200.8" cy="211" r="8"/>
  <text class="chipt" x="200.8" y="211" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <g transform="translate(48.0,300)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">El nombre</text>
    <text class="cb" x="16" y="60" data-fit="392">Corto, en inglés y con guion bajo:</text>
    <text class="cb" x="16" y="79" data-fit="392">qué cambia esta migración.</text>
  </g>
  <g transform="translate(488.0,300)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">La marca de tiempo</text>
    <text class="cb" x="16" y="60" data-fit="392">Ordena las migraciones. Se corren</text>
    <text class="cb" x="16" y="79" data-fit="392">de la más vieja a la más nueva.</text>
  </g>
</svg>
```

```shell
npx supabase migration new initial_schema
```

```svg
<svg id="mgCarpetas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 446" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="mgCarpetas-ttl mgCarpetas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="mgCarpetas-ttl">Dónde queda cada cosa</title>
  <desc id="mgCarpetas-dsc">Árbol del proyecto mi_app: AGENTS.md, la carpeta docs con modelo.pdf, la carpeta lib y la carpeta supabase con config.toml y migrations, que tiene initial_schema.sql y create_tracks.sql.</desc>
  <defs>
    <style>
      #mgCarpetas .title{fill:#161A26;font-size:22px;font-weight:700}
      #mgCarpetas .sub{fill:#79809A;font-size:13.5px}
      #mgCarpetas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #mgCarpetas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #mgCarpetas .nb{fill:#454C61;font-size:13px}
      #mgCarpetas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #mgCarpetas .foot{fill:#79809A;font-size:12px}
      #mgCarpetas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #mgCarpetas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#mgCarpetas-arrow)}
    </style>
    <marker id="mgCarpetas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="446" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Dónde queda cada cosa</text>
  <text class="sub" x="48" y="80" data-fit="860">El modelo y las migraciones viven en el repositorio, junto al código.</text>
<rect x="48" y="112" width="864" height="304" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><path d="M72,127 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="100" y="140" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="80">mi_app/</text><rect x="102" y="153" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="128" y="168" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="96">AGENTS.md</text><rect x="600.0" y="152" width="169.8" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="684.92" y="168.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="171">nombra docs/modelo.pdf</text><path d="M100,183 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="196" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="64">docs/</text><rect x="130" y="209" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="224" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="105">modelo.pdf</text><rect x="600.0" y="208" width="216.9" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="708.44" y="224.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="218">el modelo de datos del equipo</text><path d="M100,239 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="252" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="56">lib/</text><rect x="600.0" y="236" width="203.4" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="701.72" y="252.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="205">tu app Flutter, sin cambios</text><path d="M100,267 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="280" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="96">supabase/</text><rect x="600.0" y="264" width="190.0" height="24" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.2"/><text x="695.0" y="280.5" font-size="12" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="192">la crea npx supabase init</text><rect x="130" y="293" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="308" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="113">config.toml</text><path d="M128,323 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="156" y="336" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="113">migrations/</text><rect x="158" y="349" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="184" y="364" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="291">20261111140000_initial_schema.sql</text><rect x="600.0" y="348" width="156.4" height="24" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.2"/><text x="678.2" y="364.5" font-size="12" font-weight="700" fill="#7439B8" text-anchor="middle" data-fit="158">lo escribe el agente</text><rect x="158" y="377" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="184" y="392" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="283">20261111143000_create_tracks.sql</text><rect x="600.0" y="376" width="156.4" height="24" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.2"/><text x="678.2" y="392.5" font-size="12" font-weight="700" fill="#0F8478" text-anchor="middle" data-fit="158">la tabla de práctica</text></svg>
```

El archivo queda vacío. El nombre empieza por la fecha y la hora, así que el tuyo tendrá otros números.

## 4. Pedirle el esquema al agente

```text
Llena la migración supabase/migrations/<archivo>_initial_schema.sql
con el esquema inicial de la base de datos, a partir del
modelo de datos de docs/modelo.pdf.
Sigue la sección Base de datos de AGENTS.md.
```

Antes de subirla, lee el SQL contra tu modelo:

- Hay una tabla por entidad, y ninguna que el modelo no tenga.
- Cada relación es una llave foránea (`references`).
- Cada tabla tiene su `grant`.

## 5. Subirla y verla en Supabase

```svg
<svg id="mgPush" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 512" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="mgPush-ttl mgPush-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="mgPush-ttl">Subir las migraciones</title>
  <desc id="mgPush-dsc">npx supabase db push <tspan letter-spacing="2">-</tspan>-remote lista la migración 20261111140000_initial_schema.sql, pregunta si se sube y, tras responder y, la aplica y termina con Finished supabase db push. Un recuadro señala <tspan letter-spacing="2">-</tspan>-remote y otro la lista de migraciones pendientes.</desc>
  <defs>
    <style>
      #mgPush .title{fill:#161A26;font-size:22px;font-weight:700}
      #mgPush .sub{fill:#79809A;font-size:13.5px}
      #mgPush .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #mgPush .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #mgPush .pf{fill:#7F8AA3} #mgPush .cmd{fill:#FFFFFF;font-weight:600}
      #mgPush .dim{fill:#8A93A6} #mgPush .okk{fill:#6BCB77;font-weight:600}
      #mgPush .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #mgPush .chipc{fill:#F2C069} #mgPush .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #mgPush .ct{fill:#161A26;font-size:14px;font-weight:700}
      #mgPush .cb{fill:#454C61;font-size:13px}
      #mgPush .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="512" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Subir las migraciones</text>
  <text class="sub" x="48" y="80" data-fit="860">Solo sube lo que la base de datos todavía no tiene. Una migración ya subida no se vuelve a correr.</text>
  <rect x="48" y="112" width="864" height="242" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\mi_app</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">mi_app&gt; </tspan><tspan class="cmd">npx supabase db push <tspan letter-spacing="2">-</tspan>-remote</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="200" data-fit="816">Do you want to push these migrations to the remote database?</text>
  <text class="tl mono" font-size="13" x="72" y="226" data-fit="816"> • 20261111140000_initial_schema.sql</text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816"> [Y/n] y</text>
  <text class="tl mono dim" font-size="13" x="72" y="304" data-fit="816">Applying migration 20261111140000_initial_schema.sql...</text>
  <text class="tl mono okk" font-size="13" x="72" y="330" data-fit="816">Finished supabase db push.</text>
  <rect class="ring" x="294.2" y="158" width="70.4" height="22" rx="5"/>
  <circle class="chipc" cx="364.6" cy="159" r="8"/>
  <text class="chipt" x="364.6" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="91.4" y="210" width="265.4" height="22" rx="5"/>
  <circle class="chipc" cx="356.8" cy="211" r="8"/>
  <text class="chipt" x="356.8" y="211" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <g transform="translate(48.0,378)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362"><tspan letter-spacing="2">-</tspan>-remote</text>
    <text class="cb" x="16" y="60" data-fit="392">Sin él, el CLI busca una base de</text>
    <text class="cb" x="16" y="79" data-fit="392">datos local que no estás usando.</text>
  </g>
  <g transform="translate(488.0,378)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Lo pendiente</text>
    <text class="cb" x="16" y="60" data-fit="392">Si la lista sale vacía, ya estaba</text>
    <text class="cb" x="16" y="79" data-fit="392">arriba: crea otra migración.</text>
  </g>
</svg>
```

```shell
npx supabase db push --remote
```

En el dashboard, `Table Editor` muestra cada tabla vacía, y `Database > Schema Visualizer` dibuja el modelo con sus relaciones: compáralo con el de la entrega 1.

Para cambiar una tabla más adelante no edites este archivo: crea otra migración con el cambio y vuelve a hacer `db push --remote`.

## 6. Una migración común: la tabla tracks

La siguiente migración es de práctica: la tabla que usa la app del taller. Esta la escribes tú, sin el agente.

```shell
npx supabase migration new create_tracks
```

```sql
create table public.tracks (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  artist_name text not null,
  image_url text not null default 'https://picsum.photos/400'
);

grant select, insert, update, delete on public.tracks to anon, authenticated;
```

La última línea es el permiso. Desde 2026, Supabase ya no deja que la app use una tabla nueva hasta que se le da permiso: sin el `grant`, la app recibe `permission denied for table tracks`.

```shell
npx supabase db push --remote
```

El push solo sube `create_tracks`: la del esquema inicial ya estaba. En `Table Editor > tracks`, usa `Insert > Insert row` para agregar dos tracks con nombre y artista. El `id` y la imagen los pone la base de datos.

## Si algo falla

- `Access token not provided`: falta `npx supabase login`.
- `unknown flag: --remote`: tu CLI es viejo. Corre `npx supabase@latest db push --remote`.
- `Remote migration versions not found in local migrations directory`: alguien del equipo subió una migración que tú no tienes. Haz `git pull` antes del push. Que una sola persona suba las migraciones evita el problema.
- `relation "…" already exists`: la tabla ya existía porque se creó a mano en el dashboard. Si está vacía, bórrala desde el `Table Editor` y vuelve a hacer el push; si tiene datos, pídele ayuda al profesor antes de borrar.
- Desde la app, `permission denied for table tracks`: falta el `grant` de la tabla. Agrégalo en una migración nueva.
