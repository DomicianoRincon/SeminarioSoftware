// Cierre (slides 33 y 34).
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS;

  // 33 · Lo que te llevas para la Entrega 1
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Lo que te llevas para la Entrega 1',
    '<div style="margin-top:40px;">' + H.bigCards([
      H.bigCard(I.palette, 'Prototipo en Stitch', 'Las pantallas de tu app, con colores coherentes.'),
      H.bigCard(I.json, 'Servidores configurados', 'Stitch, Playwright y GitHub en .agents/mcp_config.json.'),
      H.bigCard(I.browser, 'Pantallas verificadas', 'El agente recorre tus formularios en el navegador.'),
      H.bigCard(I.branch, 'Trabajo trazable', 'Issues y pull requests del equipo en GitHub.')
    ], 2) + '</div>'
  ), 'Es la evidencia de la Entrega 1: las herramientas configuradas y probadas en el repositorio de cada equipo. Lo que no alcancen en clase se termina por fuera con el paso a paso de cada lección.'));

  // 34 · Para la próxima sesión
  window.SLIDES.push(H.withNotes(icesi.slideSidebarLeftOrange(
    'Para la próxima sesión',
    H.ul([
      [I.json, 'Deja los tres servidores funcionando en tu proyecto.'],
      [I.palette, 'Completa el prototipo de tu app en Stitch.'],
      [I.edit, 'Próximo tema: <strong>StatefulWidget</strong> y <strong>setState</strong>.'],
      [I.screen, 'Los formularios empiezan a responder.']
    ]) +
    '<p style="margin-top:18px;font-size:17px;color:#5454E9;font-weight:700;">domicianorincon.github.io/SeminarioSoftware</p>',
    { type: 'icons', items: [
      { icon: I.plugW, label: 'Tres servidores' },
      { icon: I.paletteW, label: 'Prototipo' },
      { icon: I.phoneW, label: 'Formularios vivos' }
    ] }
  ), 'Hasta ahora las pantallas son estáticas. En la próxima sesión los formularios guardan lo que escribe el usuario y cambian con setState.'));
})();
