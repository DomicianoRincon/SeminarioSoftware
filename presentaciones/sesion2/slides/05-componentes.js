// Bloque 4 · Tu primer componente (slides 24 a 30). Fuente: lección S0015.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS, FIG = window.FIG;

  // Tarjeta con el nombre de un componente, del color de su marca en el celular.
  function piece(name, soft, border, strong, count) {
    return '<div style="display:flex;align-items:center;justify-content:space-between;gap:12px;width:300px;' +
      'padding:14px 18px;border-radius:12px;background:' + soft + ';border:2px solid ' + border + ';">' +
      '<span style="font-family:ui-monospace,Menlo,Consolas,monospace;font-size:21px;font-weight:700;color:' + strong + ';">' + name + '</span>' +
      (count ? '<span style="flex-shrink:0;min-width:38px;height:30px;border-radius:15px;background:' + strong +
        ';color:#fff;font-size:16px;font-weight:700;display:flex;align-items:center;justify-content:center;">&times;' + count + '</span>' : '') +
      '</div>';
  }
  function column(items) {
    return '<div style="display:flex;flex-direction:column;gap:18px;">' + items.join('') + '</div>';
  }

  // 24 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Tu primer componente<br><small style="font-size:0.5em;">Una pantalla está hecha de piezas.</small>'
  ));

  // 25 · La pantalla, como la ve quien la usa
  window.SLIDES.push(H.withNotes(icesi.slideGraphicRight(
    'Una pantalla de perfil',
    '<p style="font-size:26px;line-height:36px;">Así la ve quien usa la app: parece una sola cosa.</p>' +
    '<p style="font-size:26px;line-height:36px;margin-top:22px;" class="text-blue"><strong>¿Cuántos bloques se parecen entre sí?</strong></p>',
    FIG.swPantalla
  ), 'Con los widgets básicos y Column y Row se puede armar una pantalla entera, pero el código se vuelve largo y repetido muy rápido. ' +
    'Dejar que cuenten antes de pasar a la siguiente slide.'));

  // 26 · La pantalla, como la ve quien la programa
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'La pantalla, como la ve quien la programa',
    '<div style="display:flex;align-items:center;justify-content:center;gap:44px;">' +
    column([
      piece('ProfileInfo', '#EEF1FF', '#A9B4F2', '#4453C9'),
      piece('StatsRow', '#F4EBFF', '#C9A6EE', '#7439B8'),
      piece('StatCard', '#FFF3DC', '#F0C572', '#A96C05', 3),
      piece('PrimaryButton', '#E3F6F3', '#86D3CA', '#0F8478')
    ]) +
    '<div style="flex-shrink:0;">' + FIG.swPiezas + '</div>' +
    column([
      piece('SecondaryButton', '#E8F6E3', '#9FD68D', '#3A8235'),
      piece('ContactCard', '#FFEBEF', '#F3A3B2', '#C2354F', 4),
      piece('ChatItem', '#EFF1F5', '#C4CBD8', '#556074', 2)
    ]) +
    '</div>'
  ), 'Siete piezas distintas, usadas trece veces, aunque la pantalla tenga más de treinta textos, iconos y fotos. ' +
    'Las piezas se repiten: cuatro ContactCard, tres StatCard, dos ChatItem; la misma pieza con datos distintos. ' +
    'Las piezas encajan: StatsRow está armada con tres StatCard. Funciona como un juego de Lego. ' +
    'Tres ventajas: se construye por separado, se prueba sola y se cambia en un solo lugar. ' +
    'Lo que no está marcado, como la barra y los títulos, son widgets de Flutter usados directamente.'));

  // 27 · De copiar y pegar a un componente
  window.SLIDES.push(H.withNotes(icesi.slideStandard('De copiar y pegar a un componente', FIG.swRepetido),
    'La fila de indicadores de un perfil: tres bloques idénticos en los que solo cambian dos datos. Copiar el bloque tres veces funciona hoy. ' +
    'El problema llega cuando cambia el diseño: hay que editar tres lugares, y con uno que se olvide la pantalla queda inconsistente. ' +
    'La señal para crear un componente: estás copiando un bloque y solo le cambias los datos.'));

  // 28 · Anatomía de un componente
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Anatomía de un componente', FIG.swAnatomia),
    'Un componente es una clase que extiende StatelessWidget. Stateless es sin estado: recibe datos y los muestra. ' +
    'Los campos final son los datos, lo que cambia en cada uso. El constructor los recibe por nombre, y required obliga a entregarlos; super.key se copia siempre igual. ' +
    'build describe cómo se ve a partir de sus campos: aquí devuelve una Column con un Text debajo del otro. El editor escribe casi todo: teclear stless y aceptar la sugerencia.'));

  // 29 · Usarlo en una pantalla
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Usarlo en una pantalla', FIG.swUso),
    'Se usa igual que un Text o un ElevatedButton: se escribe su nombre y se le entregan sus datos. Hay que importarlo en el archivo de la pantalla. ' +
    'Dentro de una Row las tres tarjetas se comportan como cualquier otro hijo.'));

  // 30 · Dónde vive y cómo se llama
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Dónde vive y cómo se llama',
    '<div style="margin-top:44px;">' + H.bigCards([
      H.bigCard(I.folder, 'Carpeta', 'Todos en <strong>lib/components/</strong>'),
      H.bigCard(I.file, 'Archivo', '<strong>stat_card.dart</strong><br>Minúsculas y guion bajo'),
      H.bigCard(I.brick, 'Clase', '<strong>StatCard</strong><br>Mayúscula inicial en cada palabra')
    ]) + '</div>' +
    '<p style="margin-top:48px;text-align:center;font-size:22px;">Un componente por archivo &middot; el código en inglés &middot; los textos de la pantalla, en español</p>'
  ), 'Dos ideas para el taller. Un componente puede usar otros componentes: las pantallas se arman de lo pequeño a lo grande. ' +
    'Todavía no hay interacción: un StatelessWidget solo muestra. Si lleva un botón, se le deja un onPressed con un print.'));
})();
