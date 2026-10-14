// Bloque 4 · Playwright MCP (slides 23 a 27). Fuente: lección S0037.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS, FIG = window.FIG;

  // 23 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Playwright MCP<br><small style="font-size:0.5em;">Tu app probada en un navegador real.</small>'
  ));

  // 24 · Lo que puedes hacer con Playwright MCP
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Lo que puedes hacer con Playwright MCP', FIG.pwCapacidades),
    'Abrir la app en Chromium, leer la página como árbol de accesibilidad, escribir en los campos y hacer clic, y verificar el resultado: la ruta a la que llegó, el texto visible, los errores de consola y una captura si hace falta. ' +
    'Todo eso a partir de una instrucción en español.'));

  // 25 · Ojos y manos en el navegador
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Ojos y manos en el navegador',
    '<div style="margin-top:28px;">' + H.bigCards([
      H.bigCard(I.browser, 'browser_navigate', 'Abre una URL, como el servidor local de Flutter web.', true),
      H.bigCard(I.edit, 'browser_fill', 'Escribe en un campo, ubicado por su etiqueta.', true),
      H.bigCard(H.baseIcon('pointer'), 'browser_click', 'Hace clic en un botón, una pestaña o un enlace.', true),
      H.bigCard(I.map, 'browser_snapshot', 'Lee el árbol de accesibilidad para verificar.', true)
    ], 2) + '</div>'
  ), 'Playwright es la herramienta de automatización de navegadores de Microsoft, y @playwright/mcp es su servidor oficial. Corre local por stdio con npx -y @playwright/mcp@latest. ' +
    'Hay una quinta herramienta, browser_take_screenshot, que se usa solo cuando hace falta una comprobación visual puntual.'));

  // 26 · El árbol de accesibilidad
  window.SLIDES.push(H.withNotes(icesi.slideStandard('El árbol de accesibilidad', FIG.pwFlujo),
    'Una persona ve pixeles; un modelo que analiza capturas gasta miles de tokens por imagen y detecta mal los elementos. ' +
    'El árbol de accesibilidad es la página traducida a texto: qué es un campo, cuál es su etiqueta, qué es un botón y si está deshabilitado. Con eso el agente sabe dónde escribir y qué pulsar, en milisegundos.'));

  // 27 · Paso a paso
  window.SLIDES.push(H.withNotes(icesi.slideSidebarLeftOrange(
    'Paso a paso: Experimenta con Playwright MCP',
    H.ul([
      [I.json, 'Registra <strong>playwright</strong> en .agents/mcp_config.json.'],
      [H.baseIcon('terminal'), 'Levanta la app: <strong>flutter run -d web-server --web-port=8080</strong>.'],
      [I.map, 'Pide el árbol de accesibilidad de localhost:8080.'],
      [I.edit, 'Pide que llene el login y pulse el botón.'],
      [H.baseIcon('check'), 'Pide que recorra el registro completo.']
    ]),
    { type: 'icons', items: [
      { icon: I.terminalW, label: 'App en el puerto 8080' },
      { icon: I.browserW, label: 'Navegador del agente' },
      { icon: I.checkW, label: 'Flujo verificado' }
    ] }
  ), 'Hay que esperar a que la consola diga que la app se sirve en http://localhost:8080 antes de pedirle nada al agente. ' +
    'En el tercer paso se ve que devuelve botones, campos y encabezados sin cargar una sola imagen. En el último encadena browser_snapshot, browser_fill y browser_click y al final entrega un resumen de cada paso.'));
})();
