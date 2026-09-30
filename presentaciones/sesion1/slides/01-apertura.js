// Apertura (slides 1 y 2)
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS;

  // 1 · Portada
  window.SLIDES.push(icesi.titleSlideA(
    'Frontend developing',
    'Entorno y primera aplicación<br>' +
    '<span class="slide-footer-tag">Seminario de Ingeniería de Software &middot; Universidad Icesi</span>'
  ));

  // 2 · El recorrido de hoy
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'El recorrido de hoy',
    '<div style="margin-top:70px;">' + H.bigPipeline([
      { icon: I.screen, label: 'Frontend', sub: 'qué es y por qué<br>es difícil' },
      { icon: I.map, label: 'Panorama', sub: 'dónde encaja<br>Flutter' },
      { icon: I.cloud, label: 'La nube', sub: 'servicios<br>a través del SDK' },
      { icon: I.ai, label: 'IA', sub: 'tú al mando' },
      { icon: I.install, label: 'Manos a la obra', sub: 'Flutter corriendo<br>en Chrome' }
    ]) + '</div>'
  ), 'Cuatro bloques de conceptos y uno práctico. Al final de la clase cada uno tiene Flutter instalado y una app corriendo en Chrome.'));
})();
