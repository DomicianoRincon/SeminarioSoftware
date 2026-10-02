// Apertura (slides 1 y 2)
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS;

  // 1 · Portada
  window.SLIDES.push(icesi.titleSlideA(
    'Componentes',
    'Widgets básicos y tu primer componente<br>' +
    '<span class="slide-footer-tag">Seminario de Ingeniería de Software &middot; Universidad Icesi</span>'
  ));

  // 2 · El recorrido de hoy
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'El recorrido de hoy',
    '<div style="margin-top:70px;">' + H.bigPipeline([
      { icon: I.folder, label: 'El proyecto', sub: 'carpetas, main.dart<br>y la primera pantalla' },
      { icon: I.map, label: 'Widgets básicos', sub: 'Text, Image, Button<br>y TextField' },
      { icon: I.layout, label: 'Column y Row', sub: 'acomodar<br>varios widgets' },
      { icon: I.brick, label: 'Componentes', sub: 'tus propios<br>widgets' },
      { icon: I.tool, label: 'Taller', sub: 'seis componentes' }
    ]) + '</div>'
  ), 'Cuatro bloques cortos y un taller. Todo se prueba sobre el proyecto miapp1 de la sesión anterior. Al final de la clase cada uno tiene el taller empezado.'));
})();
