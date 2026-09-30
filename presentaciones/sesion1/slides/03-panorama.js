// Bloque 2 · Panorama del frontend (slides 8 a 11). Fuente: lección S0004.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS, FIG = window.FIG;

  // El color de cada tarjeta lo pone la plantilla por posición: azul, morado, naranja, verde.
  function fw(color, langs, list) {
    return '<p style="margin-top:12px;"><strong>Lenguajes:</strong> ' + langs + '</p>' +
      '<p style="margin-top:12px;font-weight:700;" class="text-' + color + '">' + list + '</p>';
  }

  // 8 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Panorama del frontend<br><small style="font-size:0.5em;">Según dónde corre la app, cambian las herramientas.</small>'
  ));

  // 9 · Las cuatro familias
  window.SLIDES.push(H.withNotes(icesi.slideFourCards(
    'Las cuatro familias del frontend',
    'Web', '<p>Corre en el navegador. Se abre con una URL, sin instalar nada.</p>' +
      fw('blue', 'HTML, CSS, JavaScript', 'React &middot; Angular &middot; Vue &middot; Svelte'),
    'Escritorio', '<p>Se instala en Windows, macOS o Linux.</p>' +
      fw('purple', 'C#, Swift, C++, JavaScript', 'WinUI &middot; SwiftUI &middot; Qt &middot; Electron &middot; Tauri'),
    'Móvil nativo', '<p>Una app por sistema, cada una en su lenguaje.</p>' +
      fw('orange', 'Kotlin (Android), Swift (iOS)', 'Jetpack Compose &middot; SwiftUI'),
    'Multiplataforma', '<p>Un solo código para varios destinos.</p>' +
      fw('green', 'Dart, JavaScript, Kotlin, C#', 'Flutter &middot; React Native &middot; Kotlin Multiplatform &middot; .NET MAUI') +
      '<p style="margin-top:12px;"><span style="background:#4CB979;color:#fff;font-size:13px;font-weight:700;padding:3px 10px;border-radius:999px;">Flutter: el de este curso</span></p>'
  ), 'Web: HTML, CSS y JavaScript o TypeScript. Escritorio: VS Code, el editor que usan, está hecho con Electron. ' +
    'Móvil nativo: Kotlin con Jetpack Compose en Android y Swift con SwiftUI en iOS. ' +
    'Multiplataforma: Flutter (Dart, Google), React Native (JavaScript, Meta), Kotlin Multiplatform (JetBrains), .NET MAUI (C#, Microsoft).'));

  // 10 · Nativo o multiplataforma
  window.SLIDES.push(H.withNotes(icesi.slideStandard('¿Nativo o multiplataforma?', FIG.pfNativo),
    'Es una de las primeras decisiones de ingeniería de un proyecto con app, y no tiene una respuesta única. ' +
    'Si la app depende mucho de lo propio de un sistema (hardware, integraciones específicas), lo nativo rinde más. ' +
    'Si hay que llegar a varias plataformas con un solo equipo, multiplataforma ahorra la mitad del trabajo.'));

  // 11 · Por qué Flutter
  window.SLIDES.push(H.withNotes(icesi.slideSidebarLeftBlue(
    '¿Por qué Flutter en este curso?',
    H.ul([
      [H.baseIcon('code'), 'Un solo lenguaje: <strong>Dart</strong>.'],
      [I.map, 'La misma app en Android, iOS, web y escritorio.'],
      [I.screen, 'Hoy probamos en <strong>Chrome</strong>, sin emuladores.'],
      [H.baseIcon('check'), 'Después la llevas al celular sin reescribirla.']
    ]),
    { type: 'icons', items: [
      { icon: I.androidW, label: 'Android' },
      { icon: I.iosW, label: 'iOS' },
      { icon: I.webW, label: 'Web' },
      { icon: I.deskW, label: 'Escritorio' }
    ] }
  ), 'El argumento práctico para hoy: como Flutter corre en Chrome, nadie necesita un emulador para empezar. El celular y los emuladores quedan para la Instalación avanzada.'));
})();
