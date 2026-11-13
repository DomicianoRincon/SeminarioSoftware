# La tabla profiles: el usuario en tu base de datos

<!-- tags: profiles, references auth.users, uuid, on delete cascade, createProfile, user_id, eq('user_id'), currentUser, violates foreign key constraint, permission denied for table profiles -->

Auth solo guarda correo y contraseña. El nombre del usuario, y cualquier otro dato que pida tu formulario de registro, va en una tabla propia: `profiles`. Su llave primaria **no** la genera la base de datos: es el `id` que Auth le dio a la cuenta.

## La migración

```svg
<svg id="auMigracion" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 538" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="auMigracion-ttl auMigracion-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="auMigracion-ttl">La migración de profiles</title>
  <desc id="auMigracion-dsc">En el proyecto del equipo, npx supabase migration new create_profiles crea el archivo 20261118140000_create_profiles.sql. Después de escribir el SQL, npx supabase db push <tspan letter-spacing="2">-</tspan>-remote lo aplica y termina con Finished supabase db push. Un recuadro señala el nombre de la migración y otro el archivo que se sube.</desc>
  <defs>
    <style>
      #auMigracion .title{fill:#161A26;font-size:22px;font-weight:700}
      #auMigracion .sub{fill:#79809A;font-size:13.5px}
      #auMigracion .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #auMigracion .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #auMigracion .pf{fill:#7F8AA3} #auMigracion .cmd{fill:#FFFFFF;font-weight:600}
      #auMigracion .dim{fill:#8A93A6} #auMigracion .okk{fill:#6BCB77;font-weight:600}
      #auMigracion .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #auMigracion .chipc{fill:#F2C069} #auMigracion .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #auMigracion .ct{fill:#161A26;font-size:14px;font-weight:700}
      #auMigracion .cb{fill:#454C61;font-size:13px}
      #auMigracion .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="538" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La migración de profiles</text>
  <text class="sub" x="48" y="80" data-fit="860">En el proyecto de tu equipo, como en Migraciones con el CLI de Supabase.</text>
  <rect x="48" y="112" width="864" height="268" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\mi_app</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">mi_app&gt; </tspan><tspan class="cmd">npx supabase migration new create_profiles</tspan></text>
  <text class="tl mono okk" font-size="13" x="72" y="200" data-fit="816">Created new migration at supabase/migrations/20261118140000_create_profiles.sql</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816"><tspan class="pf">mi_app&gt; </tspan><tspan class="cmd">npx supabase db push <tspan letter-spacing="2">-</tspan>-remote</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816">Do you want to push these migrations to the remote database?</text>
  <text class="tl mono" font-size="13" x="72" y="304" data-fit="816"> • 20261118140000_create_profiles.sql</text>
  <text class="tl mono" font-size="13" x="72" y="330" data-fit="816"> [Y/n] y</text>
  <text class="tl mono okk" font-size="13" x="72" y="356" data-fit="816">Finished supabase db push.</text>
  <rect class="ring" x="341.0" y="158" width="125.0" height="22" rx="5"/>
  <circle class="chipc" cx="466.0" cy="159" r="8"/>
  <text class="chipt" x="466.0" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="91.4" y="288" width="273.2" height="22" rx="5"/>
  <circle class="chipc" cx="364.6" cy="289" r="8"/>
  <text class="chipt" x="364.6" y="289" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <g transform="translate(48.0,404)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">El nombre</text>
    <text class="cb" x="16" y="60" data-fit="392">Qué cambia la migración:</text>
    <text class="cb" x="16" y="79" data-fit="392">crea la tabla profiles.</text>
  </g>
  <g transform="translate(488.0,404)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Lo que se sube</text>
    <text class="cb" x="16" y="60" data-fit="392">Solo la migración nueva. Las</text>
    <text class="cb" x="16" y="79" data-fit="392">anteriores ya estaban arriba.</text>
  </g>
</svg>
```

```shell
npx supabase migration new create_profiles
npx supabase db push --remote
```

Entre los dos comandos escribes el SQL en el archivo que creó el primero:

```sql
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  name text not null,
  email text not null
);

grant select, insert, update, delete on public.profiles
  to anon, authenticated;
```

- `references auth.users(id)`: no se puede guardar un perfil con un `id` que no sea de una cuenta.
- `on delete cascade`: si se borra la cuenta en Auth, su perfil se borra con ella.
- Sin `default gen_random_uuid()`: el `id` lo pone la app, con el que devolvió `signUp`.

## Registrar es signUp y después createProfile

```svg
<svg id="auRegistro" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 430" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="auRegistro-ttl auRegistro-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="auRegistro-ttl">Registrarse son dos pasos</title>
  <desc id="auRegistro-dsc">Cinco pasos en fila. Uno, SignupForm valida y llama a onSignup con nombre, correo y contraseña. Dos, AuthService.signUp crea la cuenta. Tres, signUp devuelve el id del usuario. Cuatro, ProfileService.createProfile guarda la fila con ese id, el nombre y el correo. Cinco, la pantalla navega a /home. Debajo, una nota: si el paso 2 falla, el 4 no corre.</desc>
  <defs>
    <style>
      #auRegistro .title{fill:#161A26;font-size:22px;font-weight:700}
      #auRegistro .sub{fill:#79809A;font-size:13.5px}
      #auRegistro .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #auRegistro .nt{font-size:15px;font-weight:700;fill:#161A26}
      #auRegistro .nb{fill:#454C61;font-size:13px}
      #auRegistro .lbl{fill:#556074;font-size:12px;font-weight:600}
      #auRegistro .foot{fill:#79809A;font-size:12px}
      #auRegistro .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #auRegistro .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#auRegistro-arrow)}
    </style>
    <marker id="auRegistro-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="430" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Registrarse son dos pasos</text>
  <text class="sub" x="48" y="80" data-fit="860">Primero la cuenta en Auth, después la fila en profiles con el id que devolvió Auth.</text>
<g><rect x="48" y="124" width="155" height="160" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><circle cx="76" cy="151" r="13" fill="#FFFFFF" stroke="#556074" stroke-width="2"/><text x="76" y="155.5" font-size="13" font-weight="700" fill="#556074" text-anchor="middle" data-fit="31">1</text><text x="98" y="156" font-size="13" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="97">SignupForm</text><text x="64" y="182" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">Valida y llama</text><text x="64" y="201" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">a onSignup con</text><text x="64" y="220" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">name, email y</text><text x="64" y="239" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">password.</text></g><path class="link" d="M205,204 H223"/><g><rect x="225" y="124" width="155" height="160" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><circle cx="253" cy="151" r="13" fill="#FFFFFF" stroke="#7439B8" stroke-width="2"/><text x="253" y="155.5" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle" data-fit="31">2</text><text x="275" y="156" font-size="13" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="97">signUp</text><text x="241" y="182" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">AuthService crea</text><text x="241" y="201" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">la cuenta en</text><text x="241" y="220" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">auth.users.</text></g><path class="link" d="M382,204 H400"/><g><rect x="402" y="124" width="155" height="160" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="430" cy="151" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="430" y="155.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="31">3</text><text x="452" y="156" font-size="13" font-weight="700" fill="#A96C05" text-anchor="start" class="mono" data-fit="97">el id</text><text x="418" y="182" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">signUp devuelve</text><text x="418" y="201" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">response.user!.id,</text><text x="418" y="220" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">un uuid.</text></g><path class="link" d="M560,204 H578"/><g><rect x="580" y="124" width="155" height="160" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="608" cy="151" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="608" y="155.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="31">4</text><text x="630" y="156" font-size="13" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="97">profile</text><text x="596" y="182" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">ProfileService.</text><text x="596" y="201" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">createProfile</text><text x="596" y="220" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">inserta la fila</text><text x="596" y="239" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">con ese id.</text></g><path class="link" d="M737,204 H755"/><g><rect x="757" y="124" width="155" height="160" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><circle cx="785" cy="151" r="13" fill="#FFFFFF" stroke="#3A8235" stroke-width="2"/><text x="785" y="155.5" font-size="13" font-weight="700" fill="#3A8235" text-anchor="middle" data-fit="31">5</text><text x="807" y="156" font-size="13" font-weight="700" fill="#3A8235" text-anchor="start" class="mono" data-fit="97">'/home'</text><text x="773" y="182" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">La pantalla</text><text x="773" y="201" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">navega y borra</text><text x="773" y="220" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="131">la pila.</text></g><g><rect x="48" y="312" width="864" height="64" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/></g><text x="68" y="341" font-size="13" font-weight="600" fill="#C2354F" text-anchor="start" data-fit="830">Van en ese orden y con await: createProfile necesita el id que devolvió signUp. Si signUp lanza</text><text x="68" y="361" font-size="13" font-weight="600" fill="#C2354F" text-anchor="start" data-fit="830">AuthException (correo repetido, contraseña corta), el paso 4 no corre y no queda un perfil suelto.</text></svg>
```

```dart
final id = await _authService.signUp(email, password);
await _profileService.createProfile(
  Profile(id: id, name: name, email: email),
);
```

El orden no es negociable: `createProfile` necesita el `id` y el `id` solo existe cuando `signUp` terminó. Por eso los dos llevan `await`.

## Los tracks de cada usuario

```svg
<svg id="auDueno" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 470" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="auDueno-ttl auDueno-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="auDueno-ttl">Cada track tiene dueño</title>
  <desc id="auDueno-dsc">Arriba, la tabla tracks con la columna nueva user_id: dos filas de Ana y una de otro usuario. Abajo, dos tarjetas: createTrack agrega user_id con el id de currentUser antes del insert, y getTracks filtra con eq user_id, así que Ana solo ve sus dos filas.</desc>
  <defs>
    <style>
      #auDueno .title{fill:#161A26;font-size:22px;font-weight:700}
      #auDueno .sub{fill:#79809A;font-size:13.5px}
      #auDueno .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #auDueno .nt{font-size:15px;font-weight:700;fill:#161A26}
      #auDueno .nb{fill:#454C61;font-size:13px}
      #auDueno .lbl{fill:#556074;font-size:12px;font-weight:600}
      #auDueno .foot{fill:#79809A;font-size:12px}
      #auDueno .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #auDueno .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#auDueno-arrow)}
    </style>
    <marker id="auDueno-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="470" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Cada track tiene dueño</text>
  <text class="sub" x="48" y="80" data-fit="860">Al crear, el servicio pone el id del usuario. Al listar, filtra por él.</text>
<rect x="48" y="116" width="864" height="164" rx="12" fill="#FFFFFF" stroke="#86D3CA" stroke-width="1.5"/><path d="M48,128 A12,12 0 0 1 60,116 H900 A12,12 0 0 1 912,128 V152 H48 Z" fill="#E3F6F3"/><text x="62" y="140" font-size="13.5" font-weight="700" fill="#0F8478" text-anchor="start" class="mono" data-fit="844">tracks</text><text x="62" y="178" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="142">id</text><text x="212" y="178" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="232">name</text><text x="452" y="178" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="192">artist_name</text><text x="652" y="178" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="266">user_id</text><line x1="58" y1="187" x2="902" y2="187" stroke="#C4CBD8"/><text x="62" y="206" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="142">a1f3c9e2</text><text x="212" y="206" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="232">Yellow</text><text x="452" y="206" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="192">Coldplay</text><text x="652" y="206" font-size="12" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="266">3f9a1c27-…</text><text x="62" y="234" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="142">b2c4d1f7</text><text x="212" y="234" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="232">Clocks</text><text x="452" y="234" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="192">Coldplay</text><text x="652" y="234" font-size="12" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="266">3f9a1c27-…</text><text x="62" y="262" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="142">c3d5e8a0</text><text x="212" y="262" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="232">Bohemian Rhapsody</text><text x="452" y="262" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="192">Queen</text><text x="652" y="262" font-size="12" font-weight="700" fill="#79809A" text-anchor="start" class="mono" data-fit="266">8b2e6d40-…</text><g><rect x="48" y="300" width="420" height="120" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="64" y="332" font-size="13.5" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="396">createTrack</text><text x="64" y="358" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">data['user_id'] = currentUser!.id</text><text x="64" y="377" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">El formulario no lo pide: lo pone</text><text x="64" y="396" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">el servicio, que sabe quién entró.</text></g><g><rect x="492" y="300" width="420" height="120" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="508" y="332" font-size="13.5" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="396">getTracks</text><text x="508" y="358" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">.select().eq('user_id', userId)</text><text x="508" y="377" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">Ana ve Yellow y Clocks. La fila</text><text x="508" y="396" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">de otro usuario no le llega.</text></g><text x="48" y="442" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">user_id referencia a profiles(id): no puede apuntar a un usuario que no existe.</text></svg>
```

Para que cada usuario vea solo sus tracks, la tabla `tracks` necesita saber de quién es cada fila. Es otra migración:

```sql
alter table public.tracks
  add column user_id uuid references public.profiles(id)
  on delete cascade;
```

La columna queda sin `not null`, porque los tracks que ya tenías no tienen dueño. El servicio llena `user_id` con el `id` del usuario que entró (`currentUser!.id`) al crear, y filtra por él al listar.
