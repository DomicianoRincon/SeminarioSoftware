# Taller · Foto de perfil con el implementador

<!-- tags: bucket avatars, Public bucket, policy INSERT, policy SELECT, avatar_url, sdd-implementar, T-09, showModalBottomSheet, image_picker, camera_macos, new row violates row-level security policy, MissingPluginException -->

En este taller no escribes el código: lo escribe `sdd-implementar`, tarea por tarea. Lo tuyo es preparar Supabase a mano, pedir cada tarea, revisar lo que hizo y probarlo. Trabajas sobre el [repositorio de arranque](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0088).

```svg
<svg id="fpTareas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 536" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpTareas-ttl fpTareas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpTareas-ttl">Las cuatro tareas del taller</title>
  <desc id="fpTareas-dsc">A la izquierda, T-09 en una caja grande: modal inferior con Elegir de la galería, subir al bucket avatars y mostrar la foto en el perfil; necesita la columna, el bucket y la policy de INSERT. Tres flechas salen hacia la derecha: T-10, la foto en el botón de perfil de HomeScreen; T-11, Tomar una foto con camera y camera_macos; T-12, Mis fotos anteriores, que necesita la policy de SELECT.</desc>
  <defs>
    <style>
      #fpTareas .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpTareas .sub{fill:#79809A;font-size:13.5px}
      #fpTareas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #fpTareas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #fpTareas .nb{fill:#454C61;font-size:13px}
      #fpTareas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fpTareas .foot{fill:#79809A;font-size:12px}
      #fpTareas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpTareas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fpTareas-arrow)}
    </style>
    <marker id="fpTareas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="536" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las cuatro tareas del taller</text>
  <text class="sub" x="48" y="80" data-fit="860">T-09 es obligatoria. Después escoge una o dos de las otras: todas dependen solo de T-09.</text>
<g><rect x="48" y="128" width="300" height="300" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="64" y="160" font-size="14.5" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="276">T-09 · Galería</text><text x="64" y="186" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="276">Modal inferior con</text><text x="64" y="205" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="276">«Elegir de la galería».</text><text x="64" y="224" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="276">Sube a avatars y guarda</text><text x="64" y="243" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="276">la URL en avatar_url.</text><text x="64" y="262" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="276">La foto aparece en</text><text x="64" y="281" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="276">el perfil.</text><text x="64" y="300" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="276"></text><text x="64" y="319" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="276">Necesita: columna,</text><text x="64" y="338" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="276">bucket y policy INSERT.</text></g><rect x="150.0" y="440" width="95.9" height="24" rx="12" fill="#C2354F" stroke="#C2354F" stroke-width="1.2"/><text x="198" y="456.5" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="97">obligatoria</text><g><rect x="424" y="128" width="488" height="88" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="440" y="160" font-size="14.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="464">T-10 · Avatar en Home</text><text x="440" y="186" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="464">El botón de perfil de HomeScreen muestra la foto,</text><text x="440" y="205" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="464">o la inicial si no hay.</text></g><path class="link" d="M352,278 C388,278 388,172 420,172"/><g><rect x="424" y="232" width="488" height="88" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="440" y="264" font-size="14.5" font-weight="700" fill="#7439B8" text-anchor="start" data-fit="464">T-11 · Cámara</text><text x="440" y="290" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="464">Opción «Tomar una foto» y CameraScreen: camera en</text><text x="440" y="309" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="464">Android, iOS y web; camera_macos en macOS.</text></g><path class="link" d="M352,278 C388,278 388,276 420,276"/><g><rect x="424" y="336" width="488" height="88" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="440" y="368" font-size="14.5" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="464">T-12 · Mis fotos anteriores</text><text x="440" y="394" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="464">Opción en el modal y AvatarHistoryScreen con la</text><text x="440" y="413" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="464">cuadrícula. Necesita: policy SELECT.</text></g><path class="link" d="M352,278 C388,278 388,380 420,380"/><rect x="603.2" y="440" width="129.5" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="668" y="456.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="131">escoge una o dos</text><text x="48" y="508" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Cada tarea se pide por separado y se prueba antes de pedir la siguiente.</text></svg>
```

## 0. Antes de empezar

- El repositorio de arranque corriendo, con la Project URL y la publishable key de tu equipo en `lib/main.dart`.
- Una cuenta creada en la app: entra y abre tu perfil. Debes ver tu inicial.
- Lee `docs/specs/F-04-foto-de-perfil.md` y `docs/tecnicas/TS-04-foto-de-perfil.md`. Vas a revisar el trabajo del agente contra ellas.

## 1. La columna avatar_url

En el proyecto de tu equipo, como en la sesión 13:

```svg
<svg id="fpMigracion" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 538" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpMigracion-ttl fpMigracion-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpMigracion-ttl">La columna avatar_url</title>
  <desc id="fpMigracion-dsc">En el proyecto del equipo, npx supabase migration new add_avatar_url crea el archivo 20261125140000_add_avatar_url.sql. Después de escribir el alter table, npx supabase db push <tspan letter-spacing="2">-</tspan>-remote lo aplica y termina con Finished supabase db push. Un recuadro señala el nombre de la migración y otro el archivo que se sube.</desc>
  <defs>
    <style>
      #fpMigracion .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpMigracion .sub{fill:#79809A;font-size:13.5px}
      #fpMigracion .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpMigracion .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #fpMigracion .pf{fill:#7F8AA3} #fpMigracion .cmd{fill:#FFFFFF;font-weight:600}
      #fpMigracion .dim{fill:#8A93A6} #fpMigracion .okk{fill:#6BCB77;font-weight:600}
      #fpMigracion .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #fpMigracion .chipc{fill:#F2C069} #fpMigracion .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #fpMigracion .ct{fill:#161A26;font-size:14px;font-weight:700}
      #fpMigracion .cb{fill:#454C61;font-size:13px}
      #fpMigracion .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="538" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La columna avatar_url</text>
  <text class="sub" x="48" y="80" data-fit="860">En el proyecto de tu equipo, como en la sesión 13.</text>
  <rect x="48" y="112" width="864" height="268" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\mi_app</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">mi_app&gt; </tspan><tspan class="cmd">npx supabase migration new add_avatar_url</tspan></text>
  <text class="tl mono okk" font-size="13" x="72" y="200" data-fit="816">Created new migration at supabase/migrations/20261125140000_add_avatar_url.sql</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816"><tspan class="pf">mi_app&gt; </tspan><tspan class="cmd">npx supabase db push <tspan letter-spacing="2">-</tspan>-remote</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816">Do you want to push these migrations to the remote database?</text>
  <text class="tl mono" font-size="13" x="72" y="304" data-fit="816"> • 20261125140000_add_avatar_url.sql</text>
  <text class="tl mono" font-size="13" x="72" y="330" data-fit="816"> [Y/n] y</text>
  <text class="tl mono okk" font-size="13" x="72" y="356" data-fit="816">Finished supabase db push.</text>
  <rect class="ring" x="341.0" y="158" width="117.2" height="22" rx="5"/>
  <circle class="chipc" cx="458.2" cy="159" r="8"/>
  <text class="chipt" x="458.2" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="91.4" y="288" width="265.4" height="22" rx="5"/>
  <circle class="chipc" cx="356.8" cy="289" r="8"/>
  <text class="chipt" x="356.8" y="289" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <g transform="translate(48.0,404)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">El nombre</text>
    <text class="cb" x="16" y="60" data-fit="392">Qué cambia: le agrega</text>
    <text class="cb" x="16" y="79" data-fit="392">una columna a profiles.</text>
  </g>
  <g transform="translate(488.0,404)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Lo que se sube</text>
    <text class="cb" x="16" y="60" data-fit="392">Solo la migración nueva.</text>
    <text class="cb" x="16" y="79" data-fit="392">profiles ya tenía su grant.</text>
  </g>
</svg>
```

```shell
npx supabase migration new add_avatar_url
npx supabase db push --remote
```

Y en el archivo de la migración:

```sql
alter table public.profiles add column avatar_url text;
```

## 2. El bucket avatars

```svg
<svg id="fpNuevoBucket" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpNuevoBucket-ttl fpNuevoBucket-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpNuevoBucket-ttl">Crear el bucket avatars</title>
  <desc id="fpNuevoBucket-dsc">Maqueta del panel de Supabase: menú Storage con Files seleccionado y, encima, la ventana Create a file bucket. Name of bucket con avatars, señalado con el 1. Public bucket encendido, señalado con el 2. Restrict file size apagado. El botón Create, señalado con el 3. A la derecha, una tarjeta para cada uno.</desc>
  <defs>
    <style>
      #fpNuevoBucket .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpNuevoBucket .sub{fill:#79809A;font-size:13.5px}
      #fpNuevoBucket .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #fpNuevoBucket .nt{font-size:15px;font-weight:700;fill:#161A26}
      #fpNuevoBucket .nb{fill:#454C61;font-size:13px}
      #fpNuevoBucket .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fpNuevoBucket .foot{fill:#79809A;font-size:12px}
      #fpNuevoBucket .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpNuevoBucket .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fpNuevoBucket-arrow)}
    </style>
    <marker id="fpNuevoBucket-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="540" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Crear el bucket avatars</text>
  <text class="sub" x="48" y="80" data-fit="860">Storage › Files › New bucket. Se hace una sola vez, en el proyecto de tu equipo.</text>
<rect x="48" y="112" width="600" height="384" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><path d="M48,124 A12,12 0 0 1 60,112 H636 A12,12 0 0 1 648,124 V148 H48 Z" fill="#EFF1F5"/><circle cx="66" cy="130" r="5" fill="#F14C4C"/><circle cx="82" cy="130" r="5" fill="#E5C07B"/><circle cx="98" cy="130" r="5" fill="#6BCB77"/><rect x="118" y="120" width="514" height="20" rx="10" fill="#FFFFFF" stroke="#C4CBD8"/><text x="132" y="134" font-size="11.5" font-weight="400" fill="#556074" text-anchor="start" class="mono" data-fit="490">supabase.com/dashboard/project/abcdefghijklmnopqrst/storage/files</text><rect x="49" y="148" width="150" height="347" fill="#F7F8FA"/><line x1="199" y1="148" x2="199" y2="496" stroke="#C4CBD8"/><text x="64" y="176" font-size="11" font-weight="700" fill="#79809A" text-anchor="start" data-fit="130">STORAGE</text><rect x="56" y="188" width="136" height="24" rx="6" fill="#E8F6E3"/><text x="66" y="204" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="124">Files</text><text x="66" y="234" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="124">Policies</text><text x="66" y="264" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="124">Settings</text><rect x="200" y="149" width="447" height="346" fill="#161A26" opacity=".12"/><rect x="216" y="164" width="416" height="316" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><text x="232" y="196" font-size="16" font-weight="700" fill="#161A26" text-anchor="start" data-fit="300">Create a file bucket</text><text x="232" y="228" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="122">Name of bucket</text><rect x="232" y="238" width="384" height="32" rx="6" fill="#FFFFFF" stroke="#C4CBD8"/><text x="244" y="259" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="78">avatars</text><rect x="228" y="234" width="392" height="40" rx="8" fill="none" stroke="#F2A93B" stroke-width="2.5"/><circle cx="620" cy="234" r="10" fill="#F2A93B"/><text x="620" y="238" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">1</text><text x="232" y="302" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="115">Public bucket</text><rect x="574" y="288" width="34" height="20" rx="10" fill="#3ECF8E"/><circle cx="598" cy="298" r="7" fill="#FFFFFF"/><text x="232" y="320" font-size="11.5" font-weight="400" fill="#79809A" text-anchor="start" data-fit="330">Anyone can read any object without any authorization.</text><rect x="224" y="280" width="400" height="52" rx="8" fill="none" stroke="#F2A93B" stroke-width="2.5"/><circle cx="624" cy="280" r="10" fill="#F2A93B"/><text x="624" y="284" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">2</text><text x="232" y="360" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="150">Restrict file size</text><rect x="574" y="346" width="34" height="20" rx="10" fill="#D5D9E0"/><circle cx="584" cy="356" r="7" fill="#FFFFFF"/><text x="232" y="392" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="157">Restrict MIME types</text><rect x="574" y="378" width="34" height="20" rx="10" fill="#D5D9E0"/><circle cx="584" cy="388" r="7" fill="#FFFFFF"/><rect x="428" y="430" width="90" height="32" rx="6" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.2"/><text x="473.0" y="450.5" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="middle" data-fit="82">Cancel</text><rect x="528" y="430" width="88" height="32" rx="6" fill="#3ECF8E" stroke="#3ECF8E" stroke-width="1.2"/><text x="572.0" y="450.5" font-size="12.5" font-weight="600" fill="#1C1C1C" text-anchor="middle" data-fit="80">Create</text><rect x="524" y="426" width="96" height="40" rx="8" fill="none" stroke="#F2A93B" stroke-width="2.5"/><circle cx="620" cy="426" r="10" fill="#F2A93B"/><text x="620" y="430" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">3</text><rect x="680" y="112" width="232" height="80" rx="12" fill="#FFFFFF" stroke="#F2A93B" stroke-width="1.5"/><circle cx="704" cy="134" r="10" fill="#F2A93B"/><text x="704" y="138" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">1</text><text x="722" y="139" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="182">El nombre</text><text x="696" y="162" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">avatars, en minúscula.</text><text x="696" y="180" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">El código lo busca así.</text><rect x="680" y="204" width="232" height="98" rx="12" fill="#FFFFFF" stroke="#F2A93B" stroke-width="1.5"/><circle cx="704" cy="226" r="10" fill="#F2A93B"/><text x="704" y="230" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">2</text><text x="722" y="231" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="182">Public bucket</text><text x="696" y="254" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">Encendido: la foto se</text><text x="696" y="272" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">ve con su URL, sin</text><text x="696" y="290" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">sesión ni token.</text><rect x="680" y="314" width="232" height="80" rx="12" fill="#FFFFFF" stroke="#F2A93B" stroke-width="1.5"/><circle cx="704" cy="336" r="10" fill="#F2A93B"/><text x="704" y="340" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">3</text><text x="722" y="341" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="182">Create</text><text x="696" y="364" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">El bucket aparece en</text><text x="696" y="382" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">la lista, vacío.</text><text x="48" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Maqueta de la interfaz de noviembre de 2026. Si tu panel se ve distinto, busca los mismos tres campos.</text></svg>
```

En el dashboard de Supabase: *Storage › Files › New bucket*. Nombre `avatars` y *Public bucket* encendido.

## 3. Las policies

```svg
<svg id="fpPolicy" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpPolicy-ttl fpPolicy-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpPolicy-ttl">Las policies del bucket</title>
  <desc id="fpPolicy-dsc">Maqueta del editor de policies de Supabase: Policy name con subir fotos; Allowed operation con INSERT marcado, señalado con el 1; Target roles con authenticated, señalado con el 2; Policy definition con bucket_id = 'avatars', señalado con el 3; y el botón Save policy. A la derecha, una tarjeta para cada uno y una cuarta que dice que se repite con SELECT para el historial.</desc>
  <defs>
    <style>
      #fpPolicy .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpPolicy .sub{fill:#79809A;font-size:13.5px}
      #fpPolicy .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #fpPolicy .nt{font-size:15px;font-weight:700;fill:#161A26}
      #fpPolicy .nb{fill:#454C61;font-size:13px}
      #fpPolicy .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fpPolicy .foot{fill:#79809A;font-size:12px}
      #fpPolicy .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpPolicy .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fpPolicy-arrow)}
    </style>
    <marker id="fpPolicy-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="540" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las policies del bucket</text>
  <text class="sub" x="48" y="80" data-fit="860">Storage › Policies › New policy en avatars. Público deja leer, no subir.</text>
<rect x="48" y="112" width="600" height="384" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><path d="M48,124 A12,12 0 0 1 60,112 H636 A12,12 0 0 1 648,124 V148 H48 Z" fill="#EFF1F5"/><circle cx="66" cy="130" r="5" fill="#F14C4C"/><circle cx="82" cy="130" r="5" fill="#E5C07B"/><circle cx="98" cy="130" r="5" fill="#6BCB77"/><rect x="118" y="120" width="514" height="20" rx="10" fill="#FFFFFF" stroke="#C4CBD8"/><text x="132" y="134" font-size="11.5" font-weight="400" fill="#556074" text-anchor="start" class="mono" data-fit="490">supabase.com/dashboard/project/abcdefghijklmnopqrst/storage/policies</text><rect x="49" y="148" width="150" height="347" fill="#F7F8FA"/><line x1="199" y1="148" x2="199" y2="496" stroke="#C4CBD8"/><text x="64" y="176" font-size="11" font-weight="700" fill="#79809A" text-anchor="start" data-fit="130">STORAGE</text><text x="66" y="204" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="124">Files</text><rect x="56" y="218" width="136" height="24" rx="6" fill="#E8F6E3"/><text x="66" y="234" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="124">Policies</text><text x="66" y="264" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="124">Settings</text><text x="224" y="178" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" data-fit="400">Adding new policy to avatars</text><text x="224" y="208" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="101">Policy name</text><rect x="224" y="216" width="400" height="28" rx="6" fill="#FFFFFF" stroke="#C4CBD8"/><text x="234" y="234" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="101">subir fotos</text><text x="224" y="268" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="143">Allowed operation</text><rect x="224" y="283" width="14" height="14" rx="3" fill="#FFFFFF" stroke="#556074" stroke-width="1.4"/><text x="244" y="294" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" class="mono" data-fit="67">SELECT</text><rect x="320" y="283" width="14" height="14" rx="3" fill="#3A8235"/><path d="M323,290 l3,3 5,-6" fill="none" stroke="#FFFFFF" stroke-width="1.8"/><text x="340" y="294" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" class="mono" data-fit="67">INSERT</text><rect x="416" y="283" width="14" height="14" rx="3" fill="#FFFFFF" stroke="#556074" stroke-width="1.4"/><text x="436" y="294" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" class="mono" data-fit="67">UPDATE</text><rect x="512" y="283" width="14" height="14" rx="3" fill="#FFFFFF" stroke="#556074" stroke-width="1.4"/><text x="532" y="294" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" class="mono" data-fit="67">DELETE</text><rect x="312" y="274" width="90" height="30" rx="8" fill="none" stroke="#F2A93B" stroke-width="2.5"/><circle cx="402" cy="274" r="10" fill="#F2A93B"/><text x="402" y="278" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">1</text><text x="224" y="326" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="108">Target roles</text><rect x="224" y="334" width="400" height="28" rx="6" fill="#FFFFFF" stroke="#C4CBD8"/><rect x="222.2" y="336" width="115.6" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="280" y="352.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" class="mono" data-fit="117">authenticated</text><rect x="220" y="330" width="408" height="36" rx="8" fill="none" stroke="#F2A93B" stroke-width="2.5"/><circle cx="628" cy="330" r="10" fill="#F2A93B"/><text x="628" y="334" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">2</text><text x="224" y="386" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="143">Policy definition</text><rect x="224" y="394" width="400" height="40" rx="6" fill="#1F2430"/><text x="236" y="419" font-size="12.5" font-weight="400" fill="#E5C07B" text-anchor="start" class="mono" data-fit="181">bucket_id = 'avatars'</text><rect x="220" y="390" width="408" height="48" rx="8" fill="none" stroke="#F2A93B" stroke-width="2.5"/><circle cx="628" cy="390" r="10" fill="#F2A93B"/><text x="628" y="394" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">3</text><rect x="514" y="448" width="110" height="32" rx="6" fill="#3ECF8E" stroke="#3ECF8E" stroke-width="1.2"/><text x="569.0" y="468.5" font-size="12.5" font-weight="600" fill="#1C1C1C" text-anchor="middle" data-fit="102">Save policy</text><rect x="680" y="112" width="232" height="80" rx="12" fill="#FFFFFF" stroke="#F2A93B" stroke-width="1.5"/><circle cx="704" cy="134" r="10" fill="#F2A93B"/><text x="704" y="138" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">1</text><text x="722" y="139" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="182">INSERT</text><text x="696" y="162" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">Deja subir archivos</text><text x="696" y="180" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">nuevos. Lo pide T-09.</text><rect x="680" y="204" width="232" height="62" rx="12" fill="#FFFFFF" stroke="#F2A93B" stroke-width="1.5"/><circle cx="704" cy="226" r="10" fill="#F2A93B"/><text x="704" y="230" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">2</text><text x="722" y="231" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="182">authenticated</text><text x="696" y="254" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">Solo quien inició sesión.</text><rect x="680" y="278" width="232" height="80" rx="12" fill="#FFFFFF" stroke="#F2A93B" stroke-width="1.5"/><circle cx="704" cy="300" r="10" fill="#F2A93B"/><text x="704" y="304" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">3</text><text x="722" y="305" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="182">La definición</text><text x="696" y="328" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">Solo en este bucket. Ya</text><text x="696" y="346" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">viene escrita así.</text><rect x="680" y="370" width="232" height="80" rx="12" fill="#FFFFFF" stroke="#86D3CA" stroke-width="1.5"/><circle cx="704" cy="392" r="10" fill="#0F8478"/><text x="704" y="396" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">4</text><text x="722" y="397" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="182">Otra vez, con SELECT</text><text x="696" y="420" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">Una segunda policy para</text><text x="696" y="438" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">listar las fotos (T-12).</text><text x="48" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Maqueta de la interfaz de noviembre de 2026. Sin la de INSERT: new row violates row-level security policy.</text></svg>
```

En *Storage › Policies*, sobre `avatars`, *New policy* › *For full customization*. Crea dos, las dos para `authenticated` y con la definición `bucket_id = 'avatars'`:

- **subir fotos**, con `INSERT`.
- **ver fotos**, con `SELECT`.

Si el panel se ve distinto, el mismo resultado sale en el *SQL Editor*:

```sql
create policy "subir fotos" on storage.objects
  for insert to authenticated
  with check (bucket_id = 'avatars');

create policy "ver fotos" on storage.objects
  for select to authenticated
  using (bucket_id = 'avatars');
```

## 4. T-09: la galería

Abre el agente en la carpeta del repositorio (Antigravity CLI o Claude Code) y pide:

```text
Usa la skill sdd-implementar para hacer la tarea T-09.
Ya hice la preparación en Supabase.
```

Cuando termine, revisa antes de probar:

- `docs/impl_progress.md`: `T-09` con `[x]`, la fecha y los archivos.
- `PhotoSourceSheet` es `StatelessWidget` y solo tiene *Elegir de la galería*.
- Las llamadas a Supabase están en `lib/services/`, no en la pantalla.

Detén la app y vuelve a correrla: `image_picker` trae código nativo. En tu perfil, *Cambiar foto* debe subir el panel desde abajo. Elige una foto: aparece en el círculo, y en *Storage › avatars* hay una carpeta con tu id y un `.jpg` adentro.

## 5. Una o dos más

Escoge en `impl_progress.md` una o dos de las otras y pídelas **de a una**, probando cada una antes de la siguiente:

```text
Usa la skill sdd-implementar para hacer la tarea T-10
```

- **T-10**: vuelve a la lista. El botón de perfil muestra tu foto.
- **T-11**: *Tomar una foto* en el panel abre la cámara. Pruébala en la plataforma que uses: Chrome, macOS, Android o iOS.
- **T-12**: sube dos o tres fotos y abre *Mis fotos anteriores*. Al tocar una, vuelve a ser tu foto de perfil.

## Metas

- [ ] El bucket `avatars` público, con sus dos policies, y la columna `avatar_url`.
- [ ] T-09 hecha y probada: la foto sale de la galería por el panel de abajo y sigue ahí al cerrar y abrir la app.
- [ ] Una o dos de T-10, T-11 y T-12, hechas y probadas.
- [ ] `impl_progress.md` con cada tarea marcada, y nada marcado que no hayas probado.

## Si te sobra tiempo

- Haz las tareas que no escogiste.
- Pídele a `sdd-tecnicas` la spec técnica de una funcionalidad de tu proyecto y mira qué tareas propone.

## Si algo falla

- **`new row violates row-level security policy`** al subir: falta la policy de `INSERT` en `avatars`, o se creó para otro bucket.
- **El historial sale vacío** aunque subiste fotos: falta la policy de `SELECT`.
- **`MissingPluginException`**: agregaste un paquete con la app corriendo. Detenla y córrela de nuevo.
- **`Could not find the 'avatar_url' column`**: falta subir la migración del paso 1.
- **La cámara no abre en Chrome**: el navegador pide permiso la primera vez y solo deja usarla en `localhost` o `https`.
- **La cámara no abre en macOS**: faltan `NSCameraUsageDescription` en `macos/Runner/Info.plist` o la entitlement `com.apple.security.device.camera`. Pídele al agente que revise la sección *Paquetes y plataformas* de `TS-04`.
- **«Camera not available» en el simulador de iOS**: el simulador no tiene cámara. Prueba la cámara en un teléfono.
- **El agente hizo otra cosa** (un `StatefulWidget` de más, Supabase en la pantalla): díselo citando la regla de `docs/standard_code.md` y pídele que lo corrija.
