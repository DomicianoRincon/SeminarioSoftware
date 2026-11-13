# Supabase Auth: cuentas y sesiones

<!-- tags: Supabase Auth, signUp, signInWithPassword, signOut, currentSession, AuthException, auth.users, Invalid login credentials, User already registered, Email not confirmed, Confirm email -->

Hasta ahora cualquiera que abre la app ve los mismos tracks. Para que cada persona tenga los suyos, la app necesita saber **quién** la está usando. Eso lo resuelve *Auth*, el servicio de cuentas de Supabase.

## Dos lugares para un usuario

```svg
<svg id="auDosLugares" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="auDosLugares-ttl auDosLugares-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="auDosLugares-ttl">Un usuario vive en dos lugares</title>
  <desc id="auDosLugares-dsc">A la izquierda, Supabase Auth con la tabla auth.users: id, email y la contraseña cifrada; la crea y la maneja Supabase. A la derecha, en Postgres, la tabla profiles con id, name y email, y la tabla tracks con su columna user_id. Una línea une el id de auth.users con el id de profiles, y otra el id de profiles con el user_id de tracks. Abajo, el teléfono guarda la sesión.</desc>
  <defs>
    <style>
      #auDosLugares .title{fill:#161A26;font-size:22px;font-weight:700}
      #auDosLugares .sub{fill:#79809A;font-size:13.5px}
      #auDosLugares .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #auDosLugares .nt{font-size:15px;font-weight:700;fill:#161A26}
      #auDosLugares .nb{fill:#454C61;font-size:13px}
      #auDosLugares .lbl{fill:#556074;font-size:12px;font-weight:600}
      #auDosLugares .foot{fill:#79809A;font-size:12px}
      #auDosLugares .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #auDosLugares .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#auDosLugares-arrow)}
    </style>
    <marker id="auDosLugares-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="520" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Un usuario vive en dos lugares</text>
  <text class="sub" x="48" y="80" data-fit="860">Auth guarda la cuenta. Tus tablas guardan todo lo demás, con el mismo id.</text>
<text x="48" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="111">SUPABASE AUTH</text><rect x="48" y="140" width="380" height="108" rx="12" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><path d="M48,152 A12,12 0 0 1 60,140 H416 A12,12 0 0 1 428,152 V176 H48 Z" fill="#F4EBFF"/><text x="62" y="164" font-size="13.5" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="360">auth.users</text><text x="416" y="164" font-size="12" font-weight="400" fill="#556074" text-anchor="end" data-fit="190.0">la crea Supabase</text><text x="62" y="202" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="112">id</text><text x="182" y="202" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="142">email</text><text x="332" y="202" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="102">password</text><line x1="58" y1="211" x2="418" y2="211" stroke="#C4CBD8"/><text x="62" y="230" font-size="12" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="112">3f9a1c27-…</text><text x="182" y="230" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="142">ana@correo.com</text><text x="332" y="230" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="102">$2a$10$…</text><g><rect x="48" y="288" width="380" height="84" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="64" y="318" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="356">No la creas ni la editas tú. Se llena con</text><text x="64" y="337" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="356">signUp y se consulta con signInWithPassword.</text></g><text x="532" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="165">POSTGRES · TUS TABLAS</text><rect x="532" y="140" width="380" height="108" rx="12" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.5"/><path d="M532,152 A12,12 0 0 1 544,140 H900 A12,12 0 0 1 912,152 V176 H532 Z" fill="#EEF1FF"/><text x="546" y="164" font-size="13.5" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="360">profiles</text><text x="900" y="164" font-size="12" font-weight="400" fill="#556074" text-anchor="end" data-fit="190.0">la creas tú</text><text x="546" y="202" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="112">id</text><text x="666" y="202" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="102">name</text><text x="776" y="202" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="142">email</text><line x1="542" y1="211" x2="902" y2="211" stroke="#C4CBD8"/><text x="546" y="230" font-size="12" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="112">3f9a1c27-…</text><text x="666" y="230" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="102">Ana</text><text x="776" y="230" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="142">ana@correo.com</text><rect x="532" y="288" width="380" height="108" rx="12" fill="#FFFFFF" stroke="#86D3CA" stroke-width="1.5"/><path d="M532,300 A12,12 0 0 1 544,288 H900 A12,12 0 0 1 912,300 V324 H532 Z" fill="#E3F6F3"/><text x="546" y="312" font-size="13.5" font-weight="700" fill="#0F8478" text-anchor="start" class="mono" data-fit="360">tracks</text><text x="900" y="312" font-size="12" font-weight="400" fill="#556074" text-anchor="end" data-fit="190.0">sesión 12 + user_id</text><text x="546" y="350" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="92">id</text><text x="646" y="350" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="102">name</text><text x="756" y="350" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="162">user_id</text><line x1="542" y1="359" x2="902" y2="359" stroke="#C4CBD8"/><text x="546" y="378" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="92">a1f3c9e2</text><text x="646" y="378" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="102">Yellow</text><text x="756" y="378" font-size="12" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="162">3f9a1c27-…</text><path class="link" d="M96,234 V268 H500 V226 H536"/><rect x="252.0" y="256" width="95.9" height="24" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.2"/><text x="300" y="272.5" font-size="12" font-weight="700" fill="#7439B8" text-anchor="middle" data-fit="97">el mismo id</text><path class="link" d="M590,234 V266 H880 V284"/><g><rect x="48" y="400" width="864" height="72" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="64" y="432" font-size="13.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="840">En el teléfono: la sesión</text><text x="64" y="458" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="840">Al entrar, Supabase guarda la sesión en el dispositivo. Mientras exista, la app sabe quién es el usuario sin volver a preguntar.</text></g></svg>
```

Supabase ya trae una tabla de cuentas, `auth.users`, con el correo y la contraseña cifrada. No la creas tú ni la llenas con `insert`: la llenan las llamadas de `supabase.auth`. Todo lo demás del usuario (su nombre, su foto, sus tracks) va en **tus** tablas, unido a la cuenta por el mismo `id`.

## Las cuatro llamadas

```svg
<svg id="auMetodos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 380" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="auMetodos-ttl auMetodos-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="auMetodos-ttl">Cuatro llamadas de supabase.auth</title>
  <desc id="auMetodos-dsc">Cuatro tarjetas en fila. signUp crea la cuenta y deja la sesión iniciada. signInWithPassword revisa correo y contraseña y guarda la sesión. signOut borra la sesión del dispositivo. currentSession lee la sesión guardada, sin ir a internet. Debajo de cada una, cómo queda la sesión: iniciada, iniciada, null y la misma.</desc>
  <defs>
    <style>
      #auMetodos .title{fill:#161A26;font-size:22px;font-weight:700}
      #auMetodos .sub{fill:#79809A;font-size:13.5px}
      #auMetodos .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #auMetodos .nt{font-size:15px;font-weight:700;fill:#161A26}
      #auMetodos .nb{fill:#454C61;font-size:13px}
      #auMetodos .lbl{fill:#556074;font-size:12px;font-weight:600}
      #auMetodos .foot{fill:#79809A;font-size:12px}
      #auMetodos .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #auMetodos .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#auMetodos-arrow)}
    </style>
    <marker id="auMetodos-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="380" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Cuatro llamadas de supabase.auth</text>
  <text class="sub" x="48" y="80" data-fit="860">Tres van a Supabase y cambian la sesión. La cuarta solo mira la que hay.</text>
<g><rect x="48" y="120" width="198" height="146" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="64" y="152" font-size="13.5" font-weight="700" fill="#0F8478" text-anchor="start" class="mono" data-fit="174">signUp</text><text x="64" y="178" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">Crea la cuenta en</text><text x="64" y="197" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">auth.users.</text><text x="64" y="216" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">Devuelve el user</text><text x="64" y="235" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">con su id.</text></g><path class="link" d="M147.0,268 V290"/><rect x="85.6" y="296" width="122.8" height="24" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="147.0" y="312.5" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle" data-fit="124">sesión iniciada</text><g><rect x="270" y="120" width="198" height="146" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="286" y="152" font-size="13.5" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="174">signInWithPassword</text><text x="286" y="178" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">Busca la cuenta y</text><text x="286" y="197" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">revisa la contraseña.</text><text x="286" y="216" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">No crea nada.</text></g><path class="link" d="M369.0,268 V290"/><rect x="307.6" y="296" width="122.8" height="24" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="369.0" y="312.5" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle" data-fit="124">sesión iniciada</text><g><rect x="492" y="120" width="198" height="146" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="508" y="152" font-size="13.5" font-weight="700" fill="#C2354F" text-anchor="start" class="mono" data-fit="174">signOut</text><text x="508" y="178" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">Borra la sesión</text><text x="508" y="197" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">del dispositivo. La</text><text x="508" y="216" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">cuenta sigue en</text><text x="508" y="235" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">Supabase.</text></g><path class="link" d="M591.0,268 V290"/><rect x="539.7" y="296" width="102.6" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="591.0" y="312.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" data-fit="104">sesión: null</text><g><rect x="714" y="120" width="198" height="146" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="730" y="152" font-size="13.5" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="174">currentSession</text><text x="730" y="178" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">Lee la sesión</text><text x="730" y="197" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">guardada. No va a</text><text x="730" y="216" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">internet: no lleva</text><text x="730" y="235" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="174">await.</text></g><path class="link" d="M813.0,268 V290"/><rect x="761.7" y="296" width="102.6" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="813.0" y="312.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="104">no la cambia</text><text x="48" y="352" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Las tres primeras devuelven un Future y van con await. Si algo sale mal lanzan AuthException.</text></svg>
```

```dart
final auth = Supabase.instance.client.auth;

final response = await auth.signUp(email: email, password: password);
final id = response.user!.id;

await auth.signInWithPassword(email: email, password: password);

await auth.signOut();

final loggedIn = auth.currentSession != null;
```

Cuando algo sale mal, las tres primeras lanzan `AuthException`, y su `message` dice qué pasó. Los dos que vas a ver más:

- `User already registered`: `signUp` con un correo que ya tiene cuenta.
- `Invalid login credentials`: `signInWithPassword` con un correo o una contraseña que no coinciden.

## Pruébalo

```interactive
auth
```

Regístrate con un correo nuevo y mira las tres tarjetas de la derecha: aparece la cuenta en `auth.users`, su fila en `profiles` y la sesión en el dispositivo. Después:

- **Cierra sesión** con el ícono de la barra. La sesión desaparece; la cuenta no.
- **Entra** como `ana@correo.com` con `secreta1`. Nada se crea: solo vuelve la sesión.
- **Cierra y abre la app** con y sin sesión, y mira la ruta en la que arranca.
- **Activa *Olvidar createProfile*** y regístrate otra vez. La cuenta queda en rojo: existe en Auth, pero no tiene fila en `profiles`.

## Apagar la confirmación de correo

```svg
<svg id="auConfirm" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="auConfirm-ttl auConfirm-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="auConfirm-ttl">Apagar la confirmación de correo</title>
  <desc id="auConfirm-dsc">Maqueta del panel de Supabase: menú de Authentication con Sign In / Providers seleccionado. En el panel, User Signups con Allow new users to sign up encendido y Confirm email apagado, señalado con el número 1, y el botón Save changes con el número 2. A la derecha, una tarjeta para cada uno.</desc>
  <defs>
    <style>
      #auConfirm .title{fill:#161A26;font-size:22px;font-weight:700}
      #auConfirm .sub{fill:#79809A;font-size:13.5px}
      #auConfirm .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #auConfirm .nt{font-size:15px;font-weight:700;fill:#161A26}
      #auConfirm .nb{fill:#454C61;font-size:13px}
      #auConfirm .lbl{fill:#556074;font-size:12px;font-weight:600}
      #auConfirm .foot{fill:#79809A;font-size:12px}
      #auConfirm .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #auConfirm .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#auConfirm-arrow)}
    </style>
    <marker id="auConfirm-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="540" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Apagar la confirmación de correo</text>
  <text class="sub" x="48" y="80" data-fit="860">Authentication › Sign In / Providers. Para clase, el usuario entra apenas se registra.</text>
<rect x="48" y="112" width="600" height="384" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><path d="M48,124 A12,12 0 0 1 60,112 H636 A12,12 0 0 1 648,124 V148 H48 Z" fill="#EFF1F5"/><circle cx="66" cy="130" r="5" fill="#F14C4C"/><circle cx="82" cy="130" r="5" fill="#E5C07B"/><circle cx="98" cy="130" r="5" fill="#6BCB77"/><rect x="118" y="120" width="514" height="20" rx="10" fill="#FFFFFF" stroke="#C4CBD8"/><text x="132" y="134" font-size="11.5" font-weight="400" fill="#556074" text-anchor="start" class="mono" data-fit="490">supabase.com/dashboard/project/abcdefghijklmnopqrst/auth/providers</text><rect x="49" y="148" width="150" height="347" fill="#F7F8FA"/><line x1="199" y1="148" x2="199" y2="496" stroke="#C4CBD8"/><text x="64" y="176" font-size="11" font-weight="700" fill="#79809A" text-anchor="start" data-fit="130">AUTHENTICATION</text><text x="66" y="204" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="124">Users</text><rect x="56" y="218" width="136" height="24" rx="6" fill="#E8F6E3"/><text x="66" y="234" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="124">Sign In / Providers</text><text x="66" y="264" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="124">Emails</text><text x="66" y="294" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="124">URL Configuration</text><text x="66" y="324" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="124">Policies</text><text x="224" y="182" font-size="18" font-weight="700" fill="#161A26" text-anchor="start" data-fit="260">Sign In / Providers</text><text x="224" y="216" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="200">User Signups</text><rect x="224" y="228" width="400" height="150" rx="10" fill="#FFFFFF" stroke="#C4CBD8"/><text x="240" y="256" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="280">Allow new users to sign up</text><rect x="574" y="243" width="34" height="20" rx="10" fill="#3ECF8E"/><circle cx="598" cy="253" r="7" fill="#FFFFFF"/><line x1="224" y1="278" x2="624" y2="278" stroke="#C4CBD8"/><text x="240" y="306" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="280">Confirm email</text><rect x="574" y="293" width="34" height="20" rx="10" fill="#D5D9E0"/><circle cx="584" cy="303" r="7" fill="#FFFFFF"/><text x="240" y="324" font-size="11.5" font-weight="400" fill="#79809A" text-anchor="start" data-fit="320">Users need to confirm their email before signing in.</text><rect x="228" y="282" width="392" height="54" rx="8" fill="none" stroke="#F2A93B" stroke-width="2.5"/><circle cx="620" cy="282" r="10" fill="#F2A93B"/><text x="620" y="286" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">1</text><text x="240" y="362" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="370">Minimum password length: 6</text><rect x="494" y="402" width="130" height="32" rx="6" fill="#3ECF8E" stroke="#3ECF8E" stroke-width="1.2"/><text x="559.0" y="422.5" font-size="12.5" font-weight="600" fill="#1C1C1C" text-anchor="middle" data-fit="122">Save changes</text><rect x="490" y="398" width="138" height="40" rx="8" fill="none" stroke="#F2A93B" stroke-width="2.5"/><circle cx="628" cy="398" r="10" fill="#F2A93B"/><text x="628" y="402" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">2</text><rect x="680" y="112" width="232" height="116" rx="12" fill="#FFFFFF" stroke="#F2A93B" stroke-width="1.5"/><circle cx="704" cy="134" r="10" fill="#F2A93B"/><text x="704" y="138" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">1</text><text x="722" y="139" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="182">Confirm email</text><text x="696" y="162" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">Apagado: signUp deja la</text><text x="696" y="180" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">sesión iniciada de una.</text><text x="696" y="198" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">Encendido: hay que abrir</text><text x="696" y="216" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">el correo primero.</text><rect x="680" y="240" width="232" height="80" rx="12" fill="#FFFFFF" stroke="#F2A93B" stroke-width="1.5"/><circle cx="704" cy="262" r="10" fill="#F2A93B"/><text x="704" y="266" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="30">2</text><text x="722" y="267" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="182">Save changes</text><text x="696" y="290" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">Sin guardar no cambia</text><text x="696" y="308" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="208">nada.</text><text x="48" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Maqueta de la interfaz de noviembre de 2026. En una app publicada la confirmación se deja encendida.</text></svg>
```

Por defecto, Supabase le manda un correo al usuario nuevo y no lo deja entrar hasta que lo confirma: `signUp` crea la cuenta pero no devuelve sesión, y `signInWithPassword` responde `Email not confirmed`. Para la clase, apágala en el proyecto de tu equipo.
