// Bloque 6 · Armar una pantalla (slides 30 a 32). Fuente: lección S0025.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  // 30 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Armar una pantalla<br><small style="font-size:0.5em;">Dos pasos: escribirla y anotarla en main.dart.</small>'
  ));

  // 31 · La estructura
  window.SLIDES.push(H.withNotes(icesi.slideStandard('La estructura de una pantalla', FIG.apEstructura),
    'Es un StatelessWidget como los componentes. Lo que la hace pantalla son tres cosas: el archivo va en lib/screens, uno por pantalla; la clase termina en Screen; y su build devuelve un Scaffold, sin nada que lo envuelva. ' +
    'Dentro del Scaffold van la barra, en appBar, y el contenido, en body. El body empieza con un SafeArea.'));

  // 32 · Anotarla en main.dart
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Anotar la pantalla en main.dart', FIG.apRutas),
    'Tres líneas. El import empieza con package, el nombre del proyecto y la ruta desde lib; si la ruta tiene un error, el editor dice Target of URI doesn\'t exist. ' +
    'La entrada de routes le pone nombre a la pantalla: empieza con barra y se elige uno que se parezca al de la clase. ' +
    'initialRoute dice con cuál pantalla abre la app y tiene que ser uno de los nombres de routes, escrito igual. Si no coincide, la app falla al arrancar con Could not find a generator for route.'));
})();
