// Bloque 2 · SafeArea (slides 8 a 12). Fuente: lección S0021.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  // 8 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'SafeArea<br><small style="font-size:0.5em;">En un teléfono, los bordes no son tuyos.</small>'
  ));

  // 9 · La pantalla no es toda tuya
  window.SLIDES.push(H.withNotes(icesi.slideStandard('La pantalla no es toda tuya', FIG.saZonas),
    'Un Scaffold ocupa la pantalla entera, de borde a borde. El sistema dibuja encima la hora, la batería y la barra de gestos, y el teléfono recorta la pantalla con la cámara y las esquinas. ' +
    'Lo que la app ponga en esas zonas se pinta igual, pero queda tapado. Cada teléfono tiene zonas de distinto tamaño, así que no sirve dejar un espacio fijo: SafeArea le pregunta al teléfono cuánto miden.'));

  // 10 · Cuándo hace falta
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Tres pantallas con el mismo contenido', FIG.saCasos),
    'Un AppBar ya sabe de la barra de estado: se estira hasta el borde y pone su título más abajo. Por eso en las pantallas con barra el problema de arriba no se nota. ' +
    'El de abajo sigue ahí, y en una pantalla sin barra aparecen los dos.'));

  // 11 · SafeArea envuelve el contenido
  window.SLIDES.push(H.withNotes(icesi.slideStandard('SafeArea envuelve el contenido', FIG.saCodigo),
    'SafeArea tiene un solo child: todo el contenido de la pantalla. Va dentro del Scaffold, en el body, no alrededor: por fuera, el fondo tampoco llega a los bordes y quedan dos franjas vacías. ' +
    'En Chrome no se nota, porque la ventana no tiene cámara ni barra de gestos. No se quita por eso: la app termina en un teléfono.'));

  // 12 · La regla del curso
  window.SLIDES.push(H.withNotes(icesi.sectionSlideEGreen(
    'La regla del curso<br><small style="font-size:0.5em;">El body de toda Screen empieza con un SafeArea.</small>'
  ), 'Si la pantalla tiene AppBar, SafeArea cuida el borde de abajo. Si no la tiene, cuida los dos. En ProfileScreen se envuelve ahora el Center del body.'));
})();
