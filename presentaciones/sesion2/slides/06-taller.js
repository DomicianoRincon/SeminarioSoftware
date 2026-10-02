// Bloque 5 · Taller (slides 31 a 36). Fuente: lección S0018.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS, FIG = window.FIG;

  // 31 · Separador de la parte práctica
  window.SLIDES.push(icesi.titleSlideF(
    'Manos a la obra',
    'Taller &middot; Componentes'
  ));

  // 32 · Los seis componentes
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Seis componentes, ninguna pantalla',
    '<div style="margin-top:44px;">' + H.bigCards([
      H.bigCard(I.btnFill, 'PrimaryButton', 'La acción principal', true),
      H.bigCard(I.btnLine, 'SecondaryButton', 'La alternativa, con borde', true),
      H.bigCard(I.stats, 'StatsRow', 'Tres StatCard en una fila', true),
      H.bigCard(I.chat, 'ChatItem', 'Una conversación de la lista', true),
      H.bigCard(I.person, 'ProfileInfo', 'La foto y los datos del perfil', true),
      H.bigCard(I.person, 'ContactCard', 'Un contacto sugerido', true)
    ]) + '</div>'
  ), 'Solo componentes. En la próxima sesión se usan para armar una pantalla de perfil y una de inicio de sesión. ' +
    'Cada componente va en su propio archivo dentro de lib/components, todos con la misma forma: el import, una línea de descripción, la clase, los campos final, el constructor y build. ' +
    'Para verlo se monta en HomeScreen, dentro del Center, y se le pasan datos. Los diseños están en el proyecto de Figma enlazado en el visor.'));

  // 33 · Botones
  window.SLIDES.push(H.withNotes(icesi.slideStandard('PrimaryButton y SecondaryButton', FIG.tlBoton),
    'Por dentro son un ElevatedButton y un OutlinedButton. Los dos reciben label, un String, e icon, un IconData: un icono también es un dato. ' +
    'El child de un botón es un widget cualquiera, así que puede ser una Row con el icono y el texto. Los colores se cambian con style y styleFrom. ' +
    'En onPressed se deja una función con un print.'));

  // 34 · StatsRow
  window.SLIDES.push(H.withNotes(icesi.slideStandard('StatsRow', FIG.tlStats),
    'El primer componente compuesto: uno que está hecho con otro componente propio. Es la fila de indicadores de un perfil, armada con tres StatCard.'));

  // 35 · ContactCard
  window.SLIDES.push(H.withNotes(icesi.slideStandard('ContactCard', FIG.tlContacto),
    'Si se ponen tantas en una Row que no caben, aparece la franja amarilla y negra: es lo esperado. El deslizamiento horizontal es de la sesión 3, y el componente no cambia cuando llegue.'));

  // 36 · La prueba de un buen componente
  window.SLIDES.push(H.withNotes(icesi.sectionSlideEGreen(
    'La prueba de un buen componente<br><small style="font-size:0.5em;">Todo lo que cambia entre un uso y otro llega por el constructor.</small>'
  ), 'Si para reutilizarlo hay que abrir el archivo y editar un texto, un icono o una imagen, ese dato debería ser un parámetro. ' +
    'Probar con datos incómodos: un nombre muy largo, una descripción de cinco renglones, un número de seis cifras.'));
})();
