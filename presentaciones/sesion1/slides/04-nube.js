// Bloque 3 · Frontend y la nube (slides 12 a 14). Fuente: lección S0005.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  // 12 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Frontend y la nube<br><small style="font-size:0.5em;">No programas el backend: usas servicios que ya existen.</small>'
  ));

  // 13 · Tu app y los servicios de la nube
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Tu app y los servicios de la nube', FIG.fnServicios),
    'El SDK es una librería que se agrega a la app. Para usar un servicio no hay que saber cómo viaja la información por internet: ' +
    'se llama una función del SDK y él se encarga. Autenticación: quién es el usuario. Base de datos: información en tablas, como las que ya conocen. ' +
    'Storage: archivos, fotos, documentos. No mencionar HTTP ni REST: no lo han visto y no hace falta.'));

  // 14 · Ejemplo con los tres servicios
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Un ejemplo: cambiar la foto de perfil', FIG.fnEjemplo),
    'Casi todo lo que hace una app se arma así: una pantalla que combina, a través del SDK, lo que les pide a varios servicios. ' +
    'Cada servicio se ve a fondo más adelante en el curso.'));
})();
