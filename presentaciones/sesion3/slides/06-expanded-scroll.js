// Bloque 5 · Expanded y scroll (slides 22 a 29). Fuente: lecciones S0023 y S0024.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS, FIG = window.FIG;

  // 22 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Expanded y scroll<br><small style="font-size:0.5em;">Las dos salidas de la franja amarilla y negra.</small>'
  ));

  // 23 · El problema
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Una fila con un texto largo', FIG.exSobra),
    'Una Row le pregunta a cada hijo cuánto ancho quiere, y se lo da. Un Text quiere todo el que necesita para escribirse en un solo renglón, aunque sea más que la pantalla. ' +
    'Expanded cambia el trato para un hijo: la Row primero mide a los demás y a él le entrega lo que sobra. Con un ancho definido, el texto ya sabe dónde cortarse.'));

  // 24 · Cómo se usa
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Expanded dentro de una Row', FIG.exCodigo),
    'Se envuelve al hijo que debe adaptarse, no a todos. Aquí es la Column de los textos: la foto y la hora conservan su tamaño. ' +
    'Expanded solo puede ser hijo directo de una Row o de una Column. En cualquier otro lugar la consola dice Incorrect use of ParentDataWidget.'));

  // 25 · flex
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Repartir el espacio con flex', FIG.exFlex),
    'Si dos hijos de la misma fila son Expanded, se reparten lo que sobra por partes iguales; flex cambia la proporción. El caso más común: dos botones que deben medir lo mismo. ' +
    'En una Column funciona igual, pero a lo alto. Spacer es un Expanded vacío: se queda con el espacio libre y empuja lo que viene después hasta el final.'));

  // 26 · La pantalla es una ventana
  window.SLIDES.push(H.withNotes(icesi.slideStandard('La pantalla es una ventana', FIG.scVentana),
    'Una Column no sabe deslizarse. Si sus hijos miden más que la pantalla, aparece la franja abajo y la consola dice A RenderFlex overflowed on the bottom. ' +
    'SingleChildScrollView deja que su hijo mida todo lo que necesite y muestra solo el pedazo que cabe. La persona mueve ese pedazo con el dedo.'));

  // 27 · Cómo se usa
  window.SLIDES.push(H.withNotes(icesi.slideStandard('SingleChildScrollView envuelve la Column', FIG.scCodigo),
    'Tiene un solo hijo, como dice su nombre: casi siempre la Column con el contenido de la pantalla. ' +
    'El scroll tiene su propio padding, y conviene usarlo en lugar de envolverlo en un Padding: así el aire se desliza con el contenido y no queda una franja fija arriba y abajo.'));

  // 28 · De lado
  window.SLIDES.push(H.withNotes(icesi.slideStandard('El mismo scroll, de lado', FIG.scHorizontal),
    'Se le dice con scrollDirection, y adentro va una Row. Es la fila de contactos sugeridos que quedó pendiente en el taller anterior. ' +
    'ContactCard no cambia: su ancho fijo hace que todas las tarjetas midan igual. Un scroll horizontal puede ir dentro de uno vertical, porque se mueven en direcciones distintas.'));

  // 29 · Lo que no va dentro de un scroll
  window.SLIDES.push(H.withNotes(icesi.slideSidebarLeftOrange(
    'Lo que no va dentro de un scroll',
    H.ul([
      [H.baseIcon('alert'), '<strong>Expanded</strong> y <strong>Spacer</strong> reparten el espacio que sobra.'],
      [I.map, 'Dentro de un scroll no sobra nada: el contenido mide lo que quiera.'],
      [I.screen, 'Si pones uno en la Column que se desliza, la pantalla queda en blanco.'],
      [H.baseIcon('check'), 'Se quita y se separa con <strong>SizedBox</strong>.']
    ]),
    { type: 'icons', items: [
      { icon: I.phoneW, label: 'El alto no tiene límite' },
      { icon: I.checkW, label: 'SizedBox para separar' }
    ] }
  ), 'La consola dice RenderFlex children have non-zero flex but incoming height constraints are unbounded. ' +
    'Dentro de las filas de esa columna sí se puede seguir usando Expanded: el ancho sigue teniendo límite.'));
})();
