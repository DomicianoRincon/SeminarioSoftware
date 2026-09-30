// Cierre (slide 28). Fuente: actividad fuera de clase de la sesión 17 del planeador.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS;

  window.SLIDES.push(H.withNotes(icesi.slideSidebarLeftOrange(
    'Para la próxima sesión',
    H.ul([
      [H.baseIcon('check'), 'Deja tu entorno listo: la app de ejemplo corriendo en Chrome.'],
      [I.screen, '¿Quieres verla en tu celular o en un emulador? Sigue la <strong>Instalación avanzada</strong> del visor.'],
      [I.map, 'Todo el material de hoy está en el visor del curso.']
    ]) +
    '<p style="margin-top:18px;font-size:17px;color:#5454E9;font-weight:700;">domicianorincon.github.io/SeminarioSoftware</p>',
    { type: 'icons', items: [
      { icon: I.checkW, label: 'Entorno listo' },
      { icon: I.phoneW, label: 'App corriendo' },
      { icon: I.bookW, label: 'Material en el visor' }
    ] }
  ), 'La próxima sesión arranca con componentes: necesitan tener el entorno funcionando desde el primer minuto.'));
})();
