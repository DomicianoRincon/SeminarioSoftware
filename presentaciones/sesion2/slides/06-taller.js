// Bloque 5 · Taller (slides 30 a 35). Fuente: lección S0018.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS, FIG = window.FIG;

  // 30 · Separador de la parte práctica
  window.SLIDES.push(icesi.titleSlideF(
    'Manos a la obra',
    'Taller &middot; Componentes'
  ));

  // 31 · Los seis componentes
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Seis componentes, ninguna pantalla',
    '<div style="margin-top:30px;">' + FIG.tlTodos + '</div>'
  ), 'Solo componentes. En la próxima sesión se usan para armar una pantalla de perfil y una de inicio de sesión. ' +
    'Cada componente va en su propio archivo dentro de lib/components, todos con la misma forma: el import, una línea de descripción, la clase, los campos final, el constructor y build. ' +
    'Para verlo se monta en HomeScreen, dentro del Center, y se le pasan datos. Los diseños están en el proyecto de Figma enlazado en el visor.'));

  // 32 · Botones
  window.SLIDES.push(H.withNotes(icesi.slideStandard('PrimaryButton y SecondaryButton', FIG.tlBoton),
    'Por dentro son un ElevatedButton y un OutlinedButton. Los dos reciben label, un String, e icon, un IconData: un icono también es un dato. ' +
    'El child de un botón es un widget cualquiera, así que puede ser una Row con el icono y el texto. Los colores se cambian con style y styleFrom. ' +
    'En onPressed se deja una función con un print.'));

  // 33 · StatsRow
  window.SLIDES.push(H.withNotes(icesi.slideStandard('StatsRow', FIG.tlStats),
    'El primer componente compuesto: uno que está hecho con otro componente propio. Es la fila de indicadores de un perfil, armada con tres StatCard.'));

  // 34 · ContactCard
  window.SLIDES.push(H.withNotes(icesi.slideStandard('ContactCard', FIG.tlContacto),
    'Si se ponen tantas en una Row que no caben, aparece la franja amarilla y negra: es lo esperado. El deslizamiento horizontal es de la sesión 3, y el componente no cambia cuando llegue.'));

  // 35 · La prueba de un buen componente
  window.SLIDES.push(H.withNotes(icesi.sectionSlideEGreen(
    'La prueba de un buen componente<br><small style="font-size:0.5em;">Todo lo que cambia entre un uso y otro llega por el constructor.</small>'
  ), 'Si para reutilizarlo hay que abrir el archivo y editar un texto, un icono o una imagen, ese dato debería ser un parámetro. ' +
    'Probar con datos incómodos: un nombre muy largo, una descripción de cinco renglones, un número de seis cifras.'));
})();
