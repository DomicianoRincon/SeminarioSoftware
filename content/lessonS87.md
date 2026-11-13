# Taller · Login y registro con Supabase

<!-- tags: AuthService, ProfileService, signUp, signInWithPassword, signOut, AuthException, initialRoute, user_id, Invalid login credentials, User already registered, Email not confirmed, violates foreign key constraint -->

La app del [repositorio de arranque](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0083) deja entrar a cualquiera. Al terminar, cada persona tendrá su cuenta, su perfil y sus propios tracks.

```svg
<svg id="tlAuthPiezas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 450" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tlAuthPiezas-ttl tlAuthPiezas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tlAuthPiezas-ttl">Quién llama a quién</title>
  <desc id="tlAuthPiezas-dsc">Tres columnas. Pantallas: LoginScreen, SignupScreen y HomeScreen. Servicios: AuthService, ProfileService y TrackService. Supabase: Auth, la tabla profiles y la tabla tracks. Flechas: Login a AuthService, Signup a AuthService y a ProfileService, Home a AuthService y a TrackService; cada servicio a su parte de Supabase. Los dos servicios vacíos están marcados.</desc>
  <defs>
    <style>
      #tlAuthPiezas .title{fill:#161A26;font-size:22px;font-weight:700}
      #tlAuthPiezas .sub{fill:#79809A;font-size:13.5px}
      #tlAuthPiezas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tlAuthPiezas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tlAuthPiezas .nb{fill:#454C61;font-size:13px}
      #tlAuthPiezas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tlAuthPiezas .foot{fill:#79809A;font-size:12px}
      #tlAuthPiezas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tlAuthPiezas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tlAuthPiezas-arrow)}
    </style>
    <marker id="tlAuthPiezas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="450" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Quién llama a quién</text>
  <text class="sub" x="48" y="80" data-fit="860">Las pantallas llaman a los servicios. Solo los servicios hablan con Supabase.</text>
<text x="48" y="124" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="84">PANTALLAS</text><g><rect x="48" y="140" width="232" height="60" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/></g><text x="164" y="175" font-size="14" font-weight="700" fill="#556074" text-anchor="middle" class="mono" data-fit="116">LoginScreen</text><g><rect x="48" y="230" width="232" height="60" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/></g><text x="164" y="265" font-size="14" font-weight="700" fill="#556074" text-anchor="middle" class="mono" data-fit="124">SignupScreen</text><g><rect x="48" y="320" width="232" height="60" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/></g><text x="164" y="355" font-size="14" font-weight="700" fill="#556074" text-anchor="middle" class="mono" data-fit="108">HomeScreen</text><text x="364" y="124" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="84">SERVICIOS</text><g><rect x="364" y="140" width="232" height="60" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/></g><text x="480" y="175" font-size="14" font-weight="700" fill="#C2354F" text-anchor="middle" class="mono" data-fit="116">AuthService</text><g><rect x="364" y="230" width="232" height="60" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/></g><text x="480" y="265" font-size="14" font-weight="700" fill="#C2354F" text-anchor="middle" class="mono" data-fit="141">ProfileService</text><g><rect x="364" y="320" width="232" height="60" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/></g><text x="480" y="355" font-size="14" font-weight="700" fill="#3A8235" text-anchor="middle" class="mono" data-fit="124">TrackService</text><text x="680" y="124" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="77">SUPABASE</text><g><rect x="680" y="140" width="232" height="60" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/></g><text x="796" y="175" font-size="14" font-weight="700" fill="#7439B8" text-anchor="middle" class="mono" data-fit="166">Auth · auth.users</text><g><rect x="680" y="230" width="232" height="60" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/></g><text x="796" y="265" font-size="14" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono" data-fit="141">tabla profiles</text><g><rect x="680" y="320" width="232" height="60" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/></g><text x="796" y="355" font-size="14" font-weight="700" fill="#0F8478" text-anchor="middle" class="mono" data-fit="124">tabla tracks</text><path class="link" d="M282,170 C320,170 326,170 362,170"/><path class="link" d="M282,260 C320,260 326,170 362,170"/><path class="link" d="M282,260 C320,260 326,260 362,260"/><path class="link" d="M282,350 C320,350 326,170 362,170"/><path class="link" d="M282,350 C320,350 326,350 362,350"/><path class="link" d="M598,170 H678"/><path class="link" d="M598,260 H678"/><path class="link" d="M598,350 H678"/><rect x="488.7" y="108" width="102.6" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="540" y="124.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" data-fit="104">rojo: vacíos</text><text x="48" y="422" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">TrackService viene completo de la sesión 12. Al final del taller le agregas el dueño de cada track.</text></svg>
```

## 0. Antes de empezar

En el proyecto de Supabase de tu equipo:

- La confirmación de correo, apagada ([Supabase Auth: cuentas y sesiones](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0084)).
- Las dos migraciones de [La tabla profiles](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0085), subidas: `create_profiles` y la columna `user_id` de `tracks`.
- La Project URL y la publishable key, pegadas en `lib/main.dart` de este repositorio.

## 1. Completar AuthService

Abre `lib/services/auth_service.dart`. Trae los cuatro métodos, vacíos:

```dart
class AuthService {
  Future<String> signUp(String email, String password) async {
    return '';
  }

  Future<void> signIn(String email, String password) async {}

  Future<void> signOut() async {}

  bool isLoggedIn() {
    return false;
  }
}
```

Estos son los bloques que faltan, **en desorden**. Cópialos y decide dónde va cada uno. Lo que un método tenía antes se reemplaza.

```dart
return _client.auth.currentSession != null;
```

```dart
import 'package:supabase_flutter/supabase_flutter.dart';
```

```dart
await _client.auth.signInWithPassword(email: email, password: password);
```

```dart
final response = await _client.auth.signUp(
  email: email,
  password: password,
);
return response.user!.id;
```

```dart
final SupabaseClient _client = Supabase.instance.client;
```

```dart
await _client.auth.signOut();
```

## 2. Completar ProfileService

`lib/services/profile_service.dart` tiene un solo método, `createProfile`. Escríbelo tú: inserta en la tabla `profiles` el `Map` que devuelve `profile.toMap()`. Es el mismo `insert` de `createTrack`, sin `.select().single()`, porque no hace falta que devuelva nada.

## 3. Invocar los servicios

Cada pantalla ya tiene su método, que hoy solo navega. Ahora:

- **`LoginScreen._login`**: inicia sesión con `signIn` y, si sale bien, navega a `'/home'`.
- **`SignupScreen._signup`**: crea la cuenta con `signUp` y, con el `id` que devuelve, el perfil con `createProfile`. Después navega a `'/home'`.
- **`HomeScreen._logout`**: cierra la sesión con `signOut` antes de volver a `'/login'`.

Cada pantalla crea su servicio como un campo del `State`, igual que `HomeScreen` crea `TrackService`. Y después de un `await`, antes de navegar, va `if (!mounted) return;` ([Sesión persistente y cerrar sesión](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0086)).

Cuando Supabase rechaza el correo o la contraseña, el `await` lanza `AuthException`. Para mostrarle el mensaje al usuario, la pantalla de login y la de registro necesitan un estado más, una forma de llenarlo y un lugar donde se vea. Estos son los tres bloques; tú decides dónde va cada uno en cada pantalla:

```dart
String _error = '';
```

```dart
try {

} on AuthException catch (error) {
  setState(() {
    _error = error.message;
  });
}
```

```dart
Text(
  _error,
  textAlign: TextAlign.center,
  style: const TextStyle(color: Colors.red),
),
```

`AuthException` viene de `supabase_flutter`: la pantalla necesita ese `import`.

## 4. Sesión persistente

Cambia el `initialRoute` de `lib/main.dart` para que la app arranque en `'/home'` si ya hay sesión, y en `'/login'` si no. `AuthService` ya tiene el método que lo responde.

## 5. Los tracks de cada usuario

`TrackService` hoy lista todos los tracks de la tabla y crea tracks sin dueño. Estas son las líneas que lo cambian; decide en qué método va cada una:

```dart
final userId = _client.auth.currentUser!.id;
```

```dart
final rows = await _client.from('tracks').select().eq('user_id', userId);
```

```dart
final data = track.toMap();
data['user_id'] = _client.auth.currentUser!.id;
```

Una de ellas reemplaza una línea que ya existe. Y si armas `data`, el `insert` tiene que recibir `data`, no `track.toMap()`.

## 6. Comprobar

- La app abre en el login. *Entrar* con un correo inventado muestra `Invalid login credentials` en rojo.
- Regístrate. La app pasa a la lista, vacía. En Supabase, el usuario aparece en `Authentication > Users` y su fila en `Table Editor > profiles`, con el mismo `id`.
- Registra otra vez el mismo correo: `User already registered`.
- Crea un track. En `Table Editor > tracks`, su `user_id` es tu `id`.
- Recarga la página: sigues adentro, en la lista.
- Cierra sesión, crea otra cuenta y entra con ella: no ves los tracks de la primera.

## Metas

- [ ] `AuthService` con sus cuatro métodos
- [ ] `ProfileService.createProfile` inserta en `profiles`
- [ ] El login entra con una cuenta real y muestra el error de Supabase
- [ ] El registro crea la cuenta y su perfil con el mismo `id`
- [ ] Cerrar sesión borra la sesión y vuelve al login
- [ ] La app recuerda la sesión al recargar
- [ ] Cada usuario ve solo sus tracks

## Si te sobra tiempo

- **Hola, nombre**: un `getProfile(String id)` en `ProfileService` con `.select().eq('id', id).single()` y `Profile.fromMap`, y el nombre en la barra de `HomeScreen`.
- **Cargando**: un `bool _isLoading` en `LoginScreen` que deshabilite *Entrar* mientras espera `signIn`.
- **Mensajes en español**: traduce los dos o tres `error.message` que más aparecen antes de ponerlos en `_error`.

## Si algo falla

- `Email not confirmed`: la confirmación de correo sigue encendida. Apágala, o borra el usuario en `Authentication > Users` y regístralo otra vez.
- `Null check operator used on a null value` al llegar a la lista después de registrarte: `signUp` creó la cuenta pero no dejó sesión, porque la confirmación de correo sigue encendida, y `currentUser!` es `null`.
- `permission denied for table profiles`: a la migración le falta el `grant`.
- `insert or update on table "profiles" violates foreign key constraint`: el `id` del perfil no es el que devolvió `signUp`.
- `Could not find the 'user_id' column of 'tracks'`: falta subir la migración que agrega `user_id`.
- La lista sale vacía después de crear tracks: el `insert` no está mandando `data` y los tracks quedaron con `user_id` en `null`.
- `Password should be at least 6 characters`: no debería llegar, el formulario ya lo revisa. Si llega, revisa `SignupForm`.
