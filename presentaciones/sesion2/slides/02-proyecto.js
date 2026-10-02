// Bloque 1 · El proyecto por dentro (slides 3 a 7). Fuente: lección S0010.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  // 3 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'El proyecto por dentro<br><small style="font-size:0.5em;">Dónde está cada cosa antes de escribir el primer widget.</small>'
  ));

  // 4 · Las carpetas
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Las carpetas del proyecto', FIG.ppCarpetas),
    'flutter create deja muchas carpetas, pero casi todo el trabajo ocurre en lib. Dentro de lib Flutter solo crea main.dart: las demás las crean ellos. ' +
    'Hoy se crean components y screens. Tener un lugar fijo para cada cosa sirve cuando el proyecto crece y cuando un agente de IA trabaje con ellos. ' +
    'Los nombres de carpetas y archivos van en minúscula y con guion bajo: home_screen.dart, stat_card.dart.'));

  // 5 · main.dart: el arranque
  window.SLIDES.push(H.withNotes(icesi.slideStandard('main.dart: el arranque', FIG.ppMainA),
    'Borrar todo el contenido de lib/main.dart: el ejemplo que trae Flutter es largo y mezcla temas que no se han visto. ' +
    'main es donde arranca todo programa en Dart; en Flutter casi siempre tiene una sola línea. ' +
    'runApp recibe un widget y lo pone en pantalla: es la raíz y todos los demás cuelgan de él. ' +
    'App es un widget que escriben ellos, con la misma forma de los componentes del final de la sesión.'));

  // 6 · main.dart: MaterialApp
  window.SLIDES.push(H.withNotes(icesi.slideStandard('main.dart: MaterialApp', FIG.ppMainB),
    'MaterialApp configura la aplicación completa. El tema saca los colores de un solo color y por ahora se queda como está. ' +
    'En routes cada pantalla tiene un nombre que empieza por barra, e initialRoute dice cuál se muestra primero. Por ahora hay una sola. ' +
    'Al ejecutar aparece la palabra Pantalla en rojo, con subrayado amarillo, sobre fondo negro. No es un error: la ruta entrega un Text suelto.'));

  // 7 · Las partes de un Scaffold
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Las partes de un Scaffold', FIG.ppScaffold),
    'En lugar del Text, la ruta entrega una pantalla completa: lib/screens/home_screen.dart. En main.dart se importa el archivo y en routes se cambia el Text por HomeScreen. ' +
    'Scaffold es la pantalla completa y le da un lugar a cada parte. appBar es la barra de arriba. body es el contenido y ocupa lo que deja libre la barra. Center deja el Text en el medio. ' +
    'Este es el banco de pruebas de toda la sesión: cada widget nuevo se prueba reemplazando el Text que está dentro de Center. ' +
    'El programa entero está en el visor, en el apartado Ejemplo completo y en la lección Playground.'));

})();
