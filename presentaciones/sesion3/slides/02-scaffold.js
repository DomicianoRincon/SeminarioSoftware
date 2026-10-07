// Bloque 1 · Scaffold (slides 4 a 7). Fuente: lección S0020.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  // 4 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Scaffold<br><small style="font-size:0.5em;">Toda pantalla empieza por el mismo widget.</small>'
  ));

  // 5 · Lo que le falta a un widget suelto
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Lo que le falta a un widget suelto', FIG.sfSinScaffold),
    'La palabra Pantalla en rojo, con subrayado amarillo, sobre fondo negro: así se ve cualquier widget que se muestra sin nada alrededor. ' +
    'Scaffold es el andamio de la pantalla. Pone el fondo, hace que los textos tomen la letra y el color del tema, y reserva un lugar para cada parte.'));

  // 6 · Los lugares de un Scaffold
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Los lugares de un Scaffold', FIG.sfPartes),
    'Cada propiedad es un lugar fijo de la pantalla, y ellos deciden qué widget va en cada uno. Todos son opcionales. El único que se usa siempre es body, que ocupa lo que dejan libre los demás. ' +
    'Si se quita appBar, el contenido sube hasta el borde de arriba; si se quita floatingActionButton, simplemente no hay botón. ' +
    'Hay un lugar más, bottomNavigationBar, que se ve en el tercer bloque de hoy.'));

  // 7 · Una pantalla es una Screen
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Una pantalla es una Screen', FIG.sfScreen),
    'En este curso, lo que tiene Scaffold se llama Screen: es una pantalla entera, vive en lib/screens, su clase termina en Screen y se abre por su nombre en routes. ' +
    'Una Page es otra cosa: un pedazo de contenido sin Scaffold que una Screen muestra en su body. Aparece cuando una pantalla tiene secciones, en la sesión 9. Hasta entonces todo es una Screen. ' +
    'Aquí crean la segunda pantalla, ProfileScreen, que es el banco de pruebas de hoy: en cada bloque se le agrega algo y en el taller se termina.'));
})();
