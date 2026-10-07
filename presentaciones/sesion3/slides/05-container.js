// Bloque 4 · Container y Padding (slides 17 a 21). Fuente: lección S0022.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  // 17 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Container y Padding<br><small style="font-size:0.5em;">Uno separa y el otro, además, dibuja una caja.</small>'
  ));

  // 18 · Padding
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Padding: aire alrededor de un widget', FIG.cpPadding),
    'Con los componentes directamente en el body, quedan pegados al borde de la pantalla y unos a otros. Padding envuelve a un widget y le deja espacio alrededor; no dibuja nada. ' +
    'La diferencia con SizedBox es de lugar: SizedBox va entre dos widgets y Padding va alrededor de uno. Para separar todo el contenido del borde, un solo Padding envuelve la Column completa.'));

  // 19 · EdgeInsets
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Tres formas de decir cuánto aire', FIG.cpInsets),
    'El espacio se describe con EdgeInsets. En only se nombran left, top, right y bottom, los que se necesiten. ' +
    'Igual que con SizedBox, pocos valores y repetidos: 8, 16 y 24 alcanzan para casi todo.'));

  // 20 · Container
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Container: una caja que se ve', FIG.cpContainer),
    'En el taller anterior usaron un Container para darle fondo y borde a StatCard. Todo lo que se pinta va dentro de decoration, en un BoxDecoration. ' +
    'Container también acepta color por fuera, como atajo, pero no los dos a la vez: si se deja en los dos lugares, la app falla con Cannot provide both a color and a decoration. ' +
    'borderRadius redondea el fondo y el borde, pero no al hijo: para recortar una imagen con la misma forma se agrega clipBehavior.'));

  // 21 · padding y margin
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Las capas de un Container', FIG.cpCaja),
    'padding y margin reciben lo mismo, un EdgeInsets, y se confunden fácil. La referencia es el borde: padding es el aire de adentro y margin el de afuera. ' +
    'Con un fondo de color se nota enseguida, porque el fondo cubre el padding y no cubre el margin. Un Container mide lo que mide su child más el padding; para fijarle un tamaño tiene width y height.'));
})();
