// Bloque 3 · Google Stitch MCP (slides 15 a 22). Fuente: lección S0036.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS, FIG = window.FIG;

  function prompt(title, text) {
    return '<h3 style="margin-bottom:10px;">' + title + '</h3>' + H.codeBox(text, 15);
  }

  // 15 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Google Stitch MCP<br><small style="font-size:0.5em;">Prototipos de interfaz a partir de prompts.</small>'
  ));

  // 16 · Lo que puedes hacer con Stitch MCP
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Lo que puedes hacer con Stitch MCP', FIG.stCapacidades),
    'Cuatro cosas. Generar una pantalla describiéndola en español. Corregirla pidiendo solo el cambio, sin reescribir el prompt. Explorar variantes con otros colores o distribución. ' +
    'Y la que conecta con el código: Antigravity lee colores y componentes del diseño con stitch_get_screen, así nadie copia valores hexadecimales a mano.'));

  // 17 · Google Stitch en la Entrega 1
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Google Stitch en la Entrega 1',
    '<div style="margin-top:40px;">' + H.bigCards([
      H.bigCard(I.palette, 'stitch.withgoogle.com', 'Un lienzo de diseño de Google Labs que genera pantallas desde lenguaje natural.', true),
      H.bigCard(I.layout, 'Componentes, no imágenes', 'Reconoce botones, campos, barras de navegación, tipografías y colores.'),
      H.bigCard(I.ai, 'Inspeccionable', 'Antigravity lee la estructura de cada pantalla por MCP.'),
      H.bigCard(I.screen, 'El prototipo de tu app', 'Lo que presentas en la Entrega 1 sale de aquí.')
    ], 2) + '</div>'
  ), 'Prototipar solía exigir dominar herramientas de dibujo vectorial y transcribir medidas y colores a mano. ' +
    'Stitch no es un generador de imágenes: genera árboles de componentes con semántica de interfaz, y eso es lo que permite que el agente los lea después.'));

  // 18 · Flujo de prototipado
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Flujo de prototipado con Stitch MCP', FIG.stFlujo),
    'Primero los prompts en el lienzo de Stitch. Después Antigravity extrae la jerarquía y los colores con stitch_get_screen. ' +
    'Con eso audita accesibilidad, contraste y distribución, y las tres pantallas quedan listas como base de la Entrega 1.'));

  // 19 · Prompts para prototipado en Stitch
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Prompts para prototipado en Stitch',
    '<div style="margin-top:28px;">' + H.bigCards([
      H.bigCard(I.screen, '1 &middot; Qué pantalla', 'Login, registro o home, y el nombre de la app.'),
      H.bigCard(I.palette, '2 &middot; Qué colores', 'Uno o dos, con su código: verde #0F8478.'),
      H.bigCard(I.layout, '3 &middot; Qué lleva', 'Una viñeta por elemento, de arriba hacia abajo.')
    ], 3) + '</div>' +
    '<div style="margin-top:36px;display:flex;gap:28px;align-items:center;justify-content:center;">' +
    H.codeBox('Agrega un botón "Ingresar con Google"\ndebajo de "Iniciar sesión".', 17) +
    '<p style="font-size:22px;max-width:420px;margin:0;">Lo que falte se corrige con un prompt corto, sin reescribir todo.</p></div>'
  ), 'Un prompt vago como hazme una pantalla de veterinaria da resultados impredecibles, pero tampoco hace falta un prompt largo: basta con responder tres preguntas. ' +
    'Iconos, espaciado y tipografía los decide Stitch. Si algo no gusta, se pide solo ese cambio sobre la pantalla ya generada.'));

  // 20 · Caso de uso: Clínica Veterinaria
  window.SLIDES.push(H.withNotes(icesi.slideThreeCols(
    'Caso de uso: Clínica Veterinaria',
    prompt('LoginScreen', 'Pantalla móvil de inicio\nde sesión para la veterinaria\n"Peludos &amp; Co.".\nColores: verde (#0F8478)\ny fondo claro (#FDFCFB).\n\n- Logo y nombre.\n- Campo de correo.\n- Campo de contraseña.\n- Botón "Iniciar sesión".'),
    prompt('SigninScreen', 'Pantalla móvil de registro\npara la veterinaria\n"Peludos &amp; Co.".\nColores: verde (#0F8478)\ny fondo claro (#FDFCFB).\n\n- Regreso y "Crear cuenta".\n- Nombre, teléfono,\n  correo y contraseña.\n- Botón "Registrarme".'),
    prompt('HomeScreen', 'Pantalla principal (Home)\npara la veterinaria\n"Peludos &amp; Co.".\nColores: verde (#0F8478)\ny ámbar (#F0C572).\n\n- Saludo "Hola, Mariana".\n- Tarjeta de "Milo".\n- Aviso de la próxima cita.\n- Cuatro accesos rápidos.')
  ), 'Son los prompts de la lección, un poco recortados para que quepan en pantalla; los completos están en el visor para copiarlos. ' +
    'Los tres repiten los mismos colores, así las pantallas se ven como una sola app. El teléfono del registro es un dato propio del dominio: sirve para avisar en una emergencia. ' +
    'En el Home, el ámbar destaca el aviso de la cita sin alarmar.'));

  // 21 · Consulta e inspección con Stitch MCP
  window.SLIDES.push(H.withNotes(icesi.slideTwoCols(
    'Consulta e inspección con Stitch MCP',
    '<h3>Le pides en español</h3>' + H.codeBox('&gt; Extrae los tokens visuales\n  de la pantalla HomeScreen\n  en Stitch: colores primarios,\n  fondo de tarjetas y\n  componentes detectados.', 17) +
    '<p style="margin-top:18px;font-size:20px;">Usa <strong>stitch_list_projects</strong> y <strong>stitch_get_screen</strong>.</p>',
    '<h3>Recibe la estructura</h3>' + H.codeBox('{\n  "name": "HomeScreen Peludos",\n  "themeTokens": {\n    "primary": "#0F8478",\n    "cardHero": "#E3F6F3",\n    "alertWarning": "#F0C572"\n  },\n  "sections": [\n    "AppBar", "HeroCard",\n    "AppointmentBanner", "BottomBar"\n  ]\n}', 16)
  ), 'stitch_list_projects enumera los proyectos asociados a la clave de API; stitch_get_screen trae la descripción estructurada de una pantalla. ' +
    'El JSON está resumido: el real trae más secciones y detalle. Lo importante es que el agente recibe colores exactos y la jerarquía de componentes, no una imagen.'));

  // 22 · Paso a paso
  window.SLIDES.push(H.withNotes(icesi.slideSidebarLeftOrange(
    'Paso a paso: Experimenta con Stitch MCP',
    H.ul([
      [I.key, 'Crea tu clave en <strong>aistudio.google.com/apikey</strong>.'],
      [I.json, 'Registra <strong>stitch</strong> en .agents/mcp_config.json.'],
      [I.palette, 'Genera las tres pantallas con los prompts del visor.'],
      [I.ai, 'Pide a Antigravity que liste tus proyectos de Stitch.'],
      [H.baseIcon('check'), 'Extrae los tokens de HomeScreen.']
    ]),
    { type: 'icons', items: [
      { icon: I.keyW, label: 'Clave de API' },
      { icon: I.paletteW, label: 'Tres pantallas' },
      { icon: I.checkW, label: 'Tokens extraídos' }
    ] }
  ), 'La clave va en headers, en X-Goog-Api-Key. Nunca se hace commit de la clave real en un repositorio público: si el repositorio es compartido, el bloque con la clave va en la configuración global, ~/.gemini/config/mcp_config.json. ' +
    'Como el archivo se lee al arrancar, después de editarlo hay que abrir Antigravity de nuevo.'));
})();
