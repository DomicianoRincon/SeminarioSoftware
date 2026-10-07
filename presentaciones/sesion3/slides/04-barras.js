// Bloque 3 · Las dos barras (slides 13 a 16). Fuente: lecciones S0028 y S0027.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  // 13 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Las dos barras<br><small style="font-size:0.5em;">AppBar arriba y BottomNavigationBar abajo.</small>'
  ));

  // 14 · Las partes de un AppBar
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Las partes de un AppBar', FIG.abPartes),
    'title es el nombre de la pantalla y es el único que se pone siempre. actions es una lista: sus widgets se dibujan a la derecha en el orden en que se escriben; con más de tres, el título se queda sin espacio. ' +
    'leading recibe un solo widget y lo pone a la izquierda. Casi nunca se escribe: al llegar a una pantalla desde otra, Flutter pone ahí la flecha de volver por su cuenta. Eso es la sesión 8.'));

  // 15 · Centrar y colorear
  window.SLIDES.push(H.withNotes(icesi.slideStandard('La misma barra, con tres ajustes', FIG.abVariantes),
    'centerTitle en true lleva el título al centro. backgroundColor es el fondo de la barra y foregroundColor el color de lo que va encima: el título y los iconos. Van en pareja. ' +
    'El error típico: oscurecer el fondo sin cambiar foregroundColor, y el título queda oscuro sobre oscuro. ' +
    'En ProfileScreen centran el título y agregan en actions un IconButton con los tres puntos, como en el diseño del taller.'));

  // 16 · Tres botones abajo
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Tres botones en bottomNavigationBar', FIG.bnCodigo),
    'Es el lugar del Scaffold que faltaba. items es la lista de botones, de izquierda a derecha, y la barra pide al menos dos. Cada uno es un BottomNavigationBarItem con icon y label. ' +
    'currentIndex dice cuál aparece resaltado y se cuenta desde 0. Al tocar otro botón no pasa nada: currentIndex tiene un número fijo. ' +
    'Hacer que responda, y que cada botón muestre un contenido distinto, es la sesión 9. La pantalla del taller no lleva esta barra.'));
})();
