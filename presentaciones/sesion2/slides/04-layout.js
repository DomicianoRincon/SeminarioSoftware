// Bloque 3 · Column y Row (slides 19 a 23). Fuente: lecciones S0016 y S0017.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  // 19 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Column y Row<br><small style="font-size:0.5em;">De un widget en la pantalla a varios.</small>'
  ));

  // 20 · Column
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Column: los dos ejes', FIG.clAnatomia),
    'Column recibe varios widgets y los pone uno debajo del otro. Un botón tiene child, en singular; Column tiene children, en plural, y recibe una lista entre corchetes. ' +
    'El eje principal es la dirección en la que se apilan los hijos: en una Column, el vertical, y lo controla mainAxisAlignment. El eje cruzado es el otro, y lo controla crossAxisAlignment. ' +
    'Los nombres parecen rebuscados, pero Row usa las mismas dos propiedades con los ejes cambiados.'));

  // 21 · Alinear en Column
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Alinear los hijos de una Column', FIG.clAlineacion),
    'crossAxisAlignment start es el que más van a escribir: el texto de una tarjeta casi siempre va a la izquierda, y por defecto sale centrado. ' +
    'Si mainAxisAlignment no parece hacer nada, suele ser el tamaño de la columna: a lo alto ocupa todo lo que le den, a lo ancho mide lo que su hijo más ancho. ' +
    'Para separar los hijos se intercala un SizedBox. Pocos valores y repetidos: 8 entre cosas que van juntas, 16 o 24 entre bloques. ' +
    'Si no caben, aparece la franja amarilla y negra: RenderFlex overflowed. La solución es de la sesión 3.'));

  // 22 · Row
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Row: los mismos ejes, girados', FIG.rwAnatomia),
    'Row es una Column acostada: mismas propiedades, otra dirección. ' +
    'La regla para no confundirse: el eje principal es la dirección en la que el widget acomoda a sus hijos. Una Row los acomoda a lo ancho, así que mainAxisAlignment los mueve a lo ancho.'));

  // 23 · Alinear en Row
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Alinear los hijos de una Row', FIG.rwAlineacion),
    'spaceBetween es el típico de un encabezado: el título a la izquierda y un icono a la derecha. spaceEvenly reparte elementos iguales, como una fila de indicadores. ' +
    'Un hijo de una Column puede ser una Row, y al revés: se mira el boceto y se parte en filas y columnas, de afuera hacia adentro. ' +
    'Antes de escribir código, dibujar las cajas sobre el diseño. Una Row no parte sus hijos en dos renglones: si no caben, franja amarilla y negra a la derecha.'));
})();
