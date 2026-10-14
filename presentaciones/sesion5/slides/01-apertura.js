// Apertura (slides 1 a 3)
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS;

  // 1 · Portada
  window.SLIDES.push(icesi.titleSlideA(
    'Servidores MCP',
    'Conectando al agente con el mundo<br>' +
    '<span class="slide-footer-tag">Seminario de Ingeniería de Software &middot; Universidad Icesi</span>'
  ));

  // 2 · El recorrido de hoy
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'El recorrido de hoy',
    '<div style="margin-top:70px;">' + H.bigPipeline([
      { icon: I.plug, label: 'Qué es MCP', sub: 'de las instrucciones<br>a las herramientas' },
      { icon: I.json, label: 'Configuración', sub: 'mcp_config.json<br>y permisos' },
      { icon: I.palette, label: 'Stitch', sub: 'prototipos<br>con prompts' },
      { icon: I.browser, label: 'Playwright', sub: 'pruebas en<br>el navegador' },
      { icon: I.branch, label: 'GitHub', sub: 'issues y<br>pull requests' }
    ]) + '</div>'
  ), 'Un bloque de concepto, uno de configuración y tres servidores, cada uno con su práctica. Todo se hace en Antigravity, sobre el proyecto que traen de la sesión 4 con su AGENTS.md y la skill flutter-pantallas.'));

  // 3 · Lo que te llevas hoy
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Lo que te llevas hoy',
    '<div style="margin-top:40px;">' + H.bigCards([
      H.bigCard(I.json, '.agents/mcp_config.json', 'Los tres servidores registrados en tu proyecto.', true),
      H.bigCard(I.palette, 'Prototipo en Stitch', 'Las pantallas de tu app, generadas con prompts.'),
      H.bigCard(I.browser, 'Pruebas con Playwright', 'Tu app web recorrida por el agente.'),
      H.bigCard(I.branch, 'Equipo en GitHub', 'Issues y pull requests desde la conversación.')
    ], 2) + '</div>'
  ), 'Son cuatro evidencias concretas y todas sirven para la Entrega 1: el archivo de configuración queda en el repositorio y el prototipo de Stitch es parte de lo que se entrega.'));
})();
