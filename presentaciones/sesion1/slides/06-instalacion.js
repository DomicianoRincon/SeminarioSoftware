// Bloque 5 · Manos a la obra: instalación básica (slides 20 a 27). Fuente: lección S0001.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS, FIG = window.FIG;

  // 20 · Separador de la parte práctica
  window.SLIDES.push(icesi.titleSlideF(
    'Manos a la obra',
    'Instalación básica: Flutter corriendo en Chrome'
  ));

  // 21 · Las piezas
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Las piezas de la instalación básica', FIG.fiPiezas),
    'Partimos de que ya tienen Git y VS Code, y Google Chrome para ver la app. ' +
    'La extensión descarga Flutter usando Git: si Git no está, Download SDK no descarga nada. ' +
    'Android e iOS van por la Instalación avanzada, que está en el visor.'));

  // 22 · Los seis pasos
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Instalar Flutter con la extensión', FIG.fiPasos),
    'Todo ocurre dentro de VS Code; los botones están en inglés, así los van a ver. El recuadro amarillo marca dónde hacer clic. ' +
    'Paso 2: no creamos el proyecto desde VS Code; Flutter: New Project solo sirve para que la extensión note que falta Flutter. ' +
    'Paso 4: carpeta sin espacios ni tildes, fuera de Program Files y fuera de OneDrive (en muchos Windows, Documentos y Escritorio están en OneDrive). ' +
    'Paso 5: después de Add SDK to PATH hay que cerrar y abrir VS Code y todas las terminales.'));

  // 23 · flutter --version
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Comprobar que Flutter responde', H.consoleSlide(FIG.tcVersion, [
    [1, 'Flutter responde', 'La terminal encontró el comando: Flutter quedó en el PATH.'],
    [2, 'Dart viene incluido', 'No hay que instalarlo aparte.'],
    ['i', 'El prompt', 'Lo que va antes de <strong>&gt;</strong> es la carpeta en la que estás. No se escribe.']
  ])), 'Terminal nueva: Terminal, New Terminal en VS Code, o PowerShell. Si dice que flutter no se reconoce, la terminal se abrió antes de agregar Flutter al PATH: cerrarla y abrir otra.'));

  // 24 · flutter create
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Crear el proyecto', H.consoleSlide(FIG.tcCreate, [
    [1, '--org icesi.edu.co', 'Prefijo del identificador: la app queda como icesi.edu.co.miapp1.'],
    [2, 'miapp1', 'Nombre del proyecto y de su carpeta: minúsculas, números y guion bajo.'],
    [3, 'cd miapp1', 'Entra a la carpeta del proyecto. Todo lo que sigue se ejecuta desde ahí.']
  ])), 'Antes: cd C:\\develop en Windows, o cd ~/develop en Mac y Linux. Nombres que no sirven: MiApp, mi-app, mi app. ' +
    'Para ver el código: File, Open Folder, miapp1. La app empieza en lib/main.dart.'));

  // 25 · flutter devices
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Ver los dispositivos', H.consoleSlide(FIG.tcDevices, [
    [1, 'chrome es el id', 'La segunda columna es el id: va después de <strong>-d</strong> en flutter run.'],
    ['i', 'La lista cambia', 'En Mac aparece macOS. Emuladores y celulares llegan con la Instalación avanzada.']
  ])), 'Cada renglón es un dispositivo: nombre, id, plataforma y detalles. Con la instalación básica deben ver al menos Chrome.'));

  // 26 · flutter run -d chrome
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Ejecutar en el navegador', H.consoleSlide(FIG.tcRun, [
    [1, '-d chrome', 'Ejecuta en el navegador. La primera vez tarda porque compila todo.'],
    [2, 'r y R', '<strong>r</strong> aplica tus cambios sin cerrar la app. <strong>R</strong> la reinicia desde cero.'],
    [3, 'q', 'Detiene la app y te devuelve la consola.']
  ])), 'Mientras la app corre, la terminal espera teclas, no comandos. Cerrar Chrome no basta: hay que presionar q.'));

  // 27 · Pruébalo
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Pruébalo: cambia el título',
    '<div style="margin-top:48px;">' + H.bigPipeline([
      { icon: I.file, label: 'Abre', sub: 'lib/main.dart' },
      { icon: I.edit, label: 'Cambia', sub: '\'Flutter Demo Home Page\'<br>por \'Hola mundo\'' },
      { icon: I.save, label: 'Guarda', sub: 'Ctrl+S o Cmd+S' },
      { icon: I.key, label: 'Presiona r', sub: 'en la terminal<br>donde corre la app' }
    ]) + '</div>' +
    '<p style="margin-top:48px;text-align:center;">El título cambia en Chrome sin volver a compilar todo. Para terminar, presiona <strong>q</strong>.</p>'
  ), 'Recorrer los puestos: el objetivo de la clase es que todos lleguen hasta aquí.'));
})();
