// Bloque 7 · Taller (slides 33 a 41). Fuente: lección S0026.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  function block(n, title, body) {
    return '<div style="display:flex;gap:16px;align-items:center;margin-bottom:20px;">' +
      '<span style="flex-shrink:0;width:40px;height:40px;border-radius:50%;background:#4453C9;color:#fff;font-weight:800;font-size:20px;' +
      'display:flex;align-items:center;justify-content:center;">' + n + '</span>' +
      '<div><div style="font-size:23px;font-weight:700;color:#393939;line-height:28px;">' + title + '</div>' +
      '<div style="font-size:17px;color:#5B5C60;line-height:23px;font-family:ui-monospace,Menlo,Consolas,monospace;">' + body + '</div></div></div>';
  }
  function section(name, soft, border, strong) {
    return '<div style="padding:13px 18px;border-radius:12px;background:' + soft + ';border:2px solid ' + border + ';' +
      'font-family:ui-monospace,Menlo,Consolas,monospace;font-size:20px;font-weight:700;color:' + strong + ';">' + name + '</div>';
  }

  // 33 · Separador de la parte práctica
  window.SLIDES.push(icesi.titleSlideF(
    'Manos a la obra',
    'Taller &middot; Pantallas'
  ));

  // 34 · La pantalla en cuatro bloques
  window.SLIDES.push(H.withNotes(icesi.slideGraphicRight(
    'Cuatro bloques',
    block(1, 'La información del perfil', 'ProfileInfo &middot; StatsRow') +
    block(2, 'Los botones', 'PrimaryButton &middot; SecondaryButton') +
    block(3, 'Contactos sugeridos', 'SectionHeader &middot; ContactCard') +
    block(4, 'Últimas conversaciones', 'SectionHeader &middot; ChatItem'),
    FIG.tpPantallas
  ), 'El taller va en dos tiempos: primero se arma la pantalla completa dentro de ProfileScreen, bloque por bloque, y después cada bloque se saca a su propio archivo. ' +
    'ProfileScreen ya existe y ya está anotada en main.dart. Los botones siguen con su print: pasar de una pantalla a otra es la sesión 8. ' +
    'SectionHeader es un componente que se les entrega hecho, con su código en el visor: recibe title y actionLabel, y se lee antes de usarlo.'));

  // 35 · El esqueleto
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Primero, el esqueleto del body', FIG.apCapas),
    'Antes del primer bloque se arma el body de afuera hacia adentro: SafeArea, SingleChildScrollView con padding de 16 y una Column. Los cuatro bloques son hijos de esa Column. ' +
    'Entre un bloque y el siguiente va un SizedBox de 24; entre las cosas de un mismo bloque, 8 o 12. Se ejecuta después de cada bloque.'));

  // 36 · Bloque 1
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Bloque 1 · La información del perfil', FIG.tpBloque1),
    'ProfileInfo y, debajo, StatsRow. Cada componente vive en su archivo, así que la pantalla tiene que importarlo; sin el import, el editor dice The method ProfileInfo isn\'t defined. ' +
    'Se prueba en una ventana angosta: si aparece la franja en StatsRow, el arreglo va en el componente, envolviendo cada StatCard en un Expanded. ' +
    'En el diseño de Figma este bloque va dentro de una tarjeta blanca con esquinas redondeadas: es opcional, con un Container.'));

  // 37 · Bloque 2
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Bloque 2 · Los botones', FIG.tpBloque2),
    'Los dos van de borde a borde. Para que cada hijo ocupe todo el ancho, la Column de la pantalla lleva crossAxisAlignment en stretch. ProfileInfo sigue viéndose centrado, porque centra su contenido por dentro.'));

  // 38 · Bloque 3
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Bloque 3 · Contactos sugeridos', FIG.tpBloque3),
    'Seis tarjetas no caben a lo ancho, así que la fila se desliza de lado: un SingleChildScrollView horizontal con una Row adentro y un SizedBox de 12 entre tarjetas. Va como un hijo más de la Column. ' +
    'Si la última tarjeta visible queda cortada, está bien: así sabe la persona que hay más.'));

  // 39 · Bloque 4
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Bloque 4 · Últimas conversaciones', FIG.tpBloque4),
    'Los ChatItem van uno debajo del otro, directamente en la Column de la pantalla. No necesitan un scroll propio: ya se desliza la pantalla entera. ' +
    'Con este bloque la pantalla ya no cabe en la ventana: se desliza hasta el final para revisar que el último se vea completo.'));

  // 40 · Sepáralo en secciones
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Después, cada bloque a su archivo',
    '<div style="display:flex;align-items:center;justify-content:center;gap:56px;margin-top:-6px;">' +
    '<div style="display:flex;flex-direction:column;gap:16px;width:420px;">' +
    section('ProfileSummarySection', '#F4EBFF', '#C9A6EE', '#7439B8') +
    section('ProfileActionsSection', '#EEF1FF', '#A9B4F2', '#4453C9') +
    section('SuggestedContactsSection', '#E3F6F3', '#86D3CA', '#0F8478') +
    section('RecentChatsSection', '#FFEBEF', '#F3A3B2', '#C2354F') +
    '</div>' +
    '<pre style="margin:0;padding:22px 26px;border-radius:14px;background:#1F2430;color:#C9CFDA;font-size:17px;line-height:24px;' +
    'font-family:ui-monospace,Menlo,Consolas,monospace;width:auto;box-shadow:none;">' +
    'child: Column(\n' +
    '  crossAxisAlignment: CrossAxisAlignment.stretch,\n' +
    '  children: [\n' +
    '    ProfileSummarySection(),\n' +
    '    SizedBox(height: 24),\n' +
    '    ProfileActionsSection(),\n' +
    '    SizedBox(height: 24),\n' +
    '    SuggestedContactsSection(),\n' +
    '    SizedBox(height: 24),\n' +
    '    RecentChatsSection(),\n' +
    '  ],\n' +
    '),</pre>' +
    '</div>' +
    '<p style="margin-top:20px;text-align:center;font-size:21px;">Una sección agrupa componentes &middot; va en <strong>lib/components/</strong> &middot; su clase termina en <strong>Section</strong></p>'
  ), 'La pantalla funciona, pero su build ya pasa de cien líneas. Cada bloque tiene nombre y límites claros, así que puede ser un widget. ' +
    'No se escribe nada nuevo: se corta el bloque de la pantalla y se pega en el build de la sección, dentro de una Column propia; los import se mudan con él. ' +
    'La primera, ProfileSummarySection, está resuelta en el visor como ejemplo; las otras tres las hacen ellos, una a la vez y ejecutando después de cada una. ' +
    'Por ahora cada sección lleva sus datos escritos adentro; en la sesión 7 los recibe por el constructor.'));

  // 41 · Tu proyecto al terminar
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Tu proyecto al terminar', FIG.tpCarpetas),
    'Cinco archivos nuevos en lib/components: section_header.dart y las cuatro secciones. profile_screen.dart solo importa las cuatro secciones. ' +
    'Todos los import de archivos propios empiezan por package y el nombre del proyecto. La pantalla aguanta una ventana angosta y una baja, sin franjas.'));
})();
