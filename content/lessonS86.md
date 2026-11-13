# Sesión persistente y cerrar sesión

<!-- tags: initialRoute, isLoggedIn, currentSession, sesión persistente, signOut, pushNamedAndRemoveUntil, (route) => false, if (!mounted) return, use_build_context_synchronously, la app vuelve al login -->

Cuando un usuario entra, Supabase guarda la sesión en el dispositivo. Si cierra la app y la vuelve a abrir, la sesión sigue ahí: no tiene sentido mandarlo otra vez al login. Y cuando cierra sesión, no debería poder volver a la lista con el botón atrás.

## La ruta inicial depende de la sesión

```svg
<svg id="auArranque" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 430" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="auArranque-ttl auArranque-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="auArranque-ttl">Al abrir la app, ¿a qué pantalla?</title>
  <desc id="auArranque-dsc">Un flujo de izquierda a derecha. main corre Supabase.initialize, que lee la sesión guardada en el dispositivo. Después, la pregunta isLoggedIn. Si hay sesión, la flecha va a /home, HomeScreen. Si no, va a /login, LoginScreen.</desc>
  <defs>
    <style>
      #auArranque .title{fill:#161A26;font-size:22px;font-weight:700}
      #auArranque .sub{fill:#79809A;font-size:13.5px}
      #auArranque .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #auArranque .nt{font-size:15px;font-weight:700;fill:#161A26}
      #auArranque .nb{fill:#454C61;font-size:13px}
      #auArranque .lbl{fill:#556074;font-size:12px;font-weight:600}
      #auArranque .foot{fill:#79809A;font-size:12px}
      #auArranque .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #auArranque .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#auArranque-arrow)}
    </style>
    <marker id="auArranque-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="430" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Al abrir la app, ¿a qué pantalla?</text>
  <text class="sub" x="48" y="80" data-fit="860">Supabase.initialize recupera la sesión guardada. initialRoute decide con ella.</text>
<g><rect x="48" y="168" width="220" height="132" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="64" y="200" font-size="14" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="196">main()</text><text x="64" y="226" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">await Supabase.initialize</text><text x="64" y="245" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">lee la sesión que quedó</text><text x="64" y="264" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">guardada la última vez.</text></g><path class="link" d="M270,234 H344"/><path d="M466,154 L582,234 L466,314 L350,234 Z" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="466" y="230" font-size="14" font-weight="700" fill="#A96C05" text-anchor="middle" class="mono" data-fit="124">isLoggedIn()</text><text x="466" y="250" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="middle" data-fit="108">¿hay sesión?</text><path class="link" d="M548,210 C600,170 620,150 680,150"/><path class="link" d="M548,258 C600,298 620,318 680,318"/><rect x="592.3" y="148" width="35.4" height="24" rx="12" fill="#3A8235" stroke="#3A8235" stroke-width="1.2"/><text x="610" y="164.5" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="37">sí</text><rect x="592.3" y="298" width="35.4" height="24" rx="12" fill="#C2354F" stroke="#C2354F" stroke-width="1.2"/><text x="610" y="314.5" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="37">no</text><g><rect x="682" y="112" width="230" height="84" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="698" y="144" font-size="14" font-weight="700" fill="#3A8235" text-anchor="start" class="mono" data-fit="206">'/home'</text><text x="698" y="170" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="206">HomeScreen: el usuario</text><text x="698" y="189" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="206">sigue adentro.</text></g><g><rect x="682" y="276" width="230" height="84" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="698" y="308" font-size="14" font-weight="700" fill="#C2354F" text-anchor="start" class="mono" data-fit="206">'/login'</text><text x="698" y="334" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="206">LoginScreen: primera vez,</text><text x="698" y="353" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="206">o cerró sesión.</text></g><text x="48" y="402" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">initialRoute: AuthService().isLoggedIn() ? '/home' : '/login'</text></svg>
```

`await Supabase.initialize(...)` en `main` ya recupera la sesión guardada. Cuando `MaterialApp` se construye, basta con preguntar si hay una:

```dart
initialRoute: AuthService().isLoggedIn() ? '/home' : '/login',
```

`isLoggedIn` mira `currentSession`, que lee lo guardado sin ir a internet. Por eso no es `async` y se puede usar dentro de `build`.

Es la única **guarda** que necesita esta app: decide a qué ruta se entra. Las demás se cuidan solas porque nadie llega a `'/home'` sin pasar por el login o el registro.

## Cerrar sesión

```svg
<svg id="auSalir" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="auSalir-ttl auSalir-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="auSalir-ttl">Cerrar sesión y rehacer la pila</title>
  <desc id="auSalir-dsc">A la izquierda, la pila antes: /home encima. Al centro, las dos líneas de _logout: await signOut y pushNamedAndRemoveUntil con route false. A la derecha, la pila después: solo /login. Debajo, la nota: con un pop, o con push sin quitar, el botón atrás volvería a la lista.</desc>
  <defs>
    <style>
      #auSalir .title{fill:#161A26;font-size:22px;font-weight:700}
      #auSalir .sub{fill:#79809A;font-size:13.5px}
      #auSalir .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #auSalir .nt{font-size:15px;font-weight:700;fill:#161A26}
      #auSalir .nb{fill:#454C61;font-size:13px}
      #auSalir .lbl{fill:#556074;font-size:12px;font-weight:600}
      #auSalir .foot{fill:#79809A;font-size:12px}
      #auSalir .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #auSalir .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#auSalir-arrow)}
    </style>
    <marker id="auSalir-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="420" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Cerrar sesión y rehacer la pila</text>
  <text class="sub" x="48" y="80" data-fit="860">signOut borra la sesión. pushNamedAndRemoveUntil deja solo el login.</text>
<text x="48" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="91">PILA ANTES</text><g><rect x="48" y="144" width="200" height="52" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="64" y="176" font-size="14" font-weight="700" fill="#3A8235" text-anchor="start" class="mono" data-fit="176">'/home'</text></g><text x="148" y="222" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="138">la única pantalla</text><g><rect x="300" y="128" width="360" height="132" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="316" y="160" font-size="14" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="336">_logout()</text><text x="316" y="186" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="336">await _authService.signOut();</text><text x="316" y="205" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="336">if (!mounted) return;</text><text x="316" y="224" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="336">pushNamedAndRemoveUntil('/login',</text><text x="316" y="243" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="336">    (route) =&gt; false);</text></g><path class="link" d="M250,170 H298"/><path class="link" d="M662,170 H710"/><text x="712" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="104">PILA DESPUÉS</text><g><rect x="712" y="144" width="200" height="52" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="728" y="176" font-size="14" font-weight="700" fill="#C2354F" text-anchor="start" class="mono" data-fit="176">'/login'</text></g><text x="812" y="222" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="151">atrás cierra la app</text><g><rect x="48" y="292" width="864" height="72" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="64" y="322" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="840">El orden importa: primero signOut y después navegar. Si solo navegas, la sesión sigue guardada</text><text x="64" y="341" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="840">y la próxima vez que abra la app, initialRoute lo vuelve a meter a /home.</text></g></svg>
```

```dart
Future<void> _logout() async {
  await _authService.signOut();
  if (!mounted) return;
  Navigator.pushNamedAndRemoveUntil(context, '/login', (route) => false);
}
```

`if (!mounted) return;` aparece cada vez que se navega **después** de un `await`: mientras se esperaba la respuesta, la pantalla pudo haberse cerrado, y entonces su `context` ya no sirve. Sin esa línea, `flutter analyze` avisa con `use_build_context_synchronously`.

## Pruébalo

```interactive
auth
```

Entra como `ana@correo.com` con `secreta1` y pulsa *Cerrar y abrir la app*: arranca en `/home`. Cierra sesión con el ícono de la barra y vuelve a cerrar y abrir: ahora arranca en `/login`.
