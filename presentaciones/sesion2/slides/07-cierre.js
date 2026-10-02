// Cierre (slide 36). Fuente: actividad fuera de clase de la sesión 18 del planeador.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS;

  window.SLIDES.push(H.withNotes(icesi.slideSidebarLeftOrange(
    'Para la próxima sesión',
    H.ul([
      [I.brick, 'Termina los <strong>seis componentes</strong> del taller, cada uno en su archivo.'],
      [H.baseIcon('check'), 'Prueba cada uno con dos juegos de datos distintos.'],
      [I.screen, 'La sesión 3 arma pantallas con esas piezas.'],
      [I.map, '¿Una idea rápida? Pruébala en el <strong>Playground</strong> del visor.']
    ]) +
    '<p style="margin-top:18px;font-size:17px;color:#5454E9;font-weight:700;">domicianorincon.github.io/SeminarioSoftware</p>',
    { type: 'icons', items: [
      { icon: I.brickW, label: 'Seis componentes' },
      { icon: I.checkW, label: 'Probados' },
      { icon: I.bookW, label: 'Material en el visor' }
    ] }
  ), 'Al terminar deben tener siete archivos en lib/components: los seis del taller y stat_card.dart, y el proyecto sin errores en el editor. ' +
    'Lo que no alcancen en clase se termina por fuera: son el insumo del taller de la próxima sesión.'));
})();
