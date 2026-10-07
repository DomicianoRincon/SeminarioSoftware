// Cierre (slide 42). Fuente: lección S0026 y sesión 20 del planeador.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS;

  window.SLIDES.push(H.withNotes(icesi.slideSidebarLeftOrange(
    'Para la próxima sesión',
    H.ul([
      [I.screen, 'Termina la <strong>pantalla de perfil</strong>, con sus cuatro bloques.'],
      [I.brick, 'Saca cada bloque a su <strong>sección</strong>, en su propio archivo.'],
      [H.baseIcon('check'), 'Pruébala en una ventana angosta y en una baja, sin franjas.'],
      [I.ai, 'La sesión 4 trabaja con un agente de IA en la consola.']
    ]) +
    '<p style="margin-top:18px;font-size:17px;color:#5454E9;font-weight:700;">domicianorincon.github.io/SeminarioSoftware</p>',
    { type: 'icons', items: [
      { icon: I.phoneW, label: 'Pantalla de perfil' },
      { icon: I.brickW, label: 'Cuatro secciones' },
      { icon: I.bookW, label: 'Material en el visor' }
    ] }
  ), 'Lo que no alcancen en clase se termina por fuera. Esta pantalla es la base del prototipo de cada equipo.'));
})();
