// Bloque 1 · ¿Qué es el frontend? (slides 3 a 7). Fuente: lección S0003.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  // 3 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    '¿Qué es el frontend?<br><small style="font-size:0.5em;">La parte del software que responde a personas.</small>'
  ));

  // 4 · Dos lados de una misma app
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Dos lados de una misma app', FIG.feLados),
    'Hasta ahora han construido software que usan otros programas: funciones, clases, servicios. ' +
    'El backend vive en servidores, guarda los datos y aplica las reglas del negocio. ' +
    'El frontend vive en el dispositivo del usuario: muestra, reacciona y recuerda qué pasa en la pantalla. ' +
    'En este curso el backend ya existe (Supabase): ellos construyen el lado izquierdo.'));

  // 5 · Una pantalla, cuatro estados
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Una pantalla, cuatro estados', FIG.feEstados),
    'Al backend lo usan otros programas, que siempre piden las cosas de la misma forma. Al frontend lo usan personas: ' +
    'tocan dos veces, se quedan sin señal, abren la app sin datos. Cada situación es un estado, y el usuario ve todos. ' +
    'Error típico: diseñar solo el estado Lista, el camino feliz. Preguntar: ¿qué app que usan se queda en blanco sin conexión?'));

  // 6 · Una base de código, muchas pantallas
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Una base de código, muchas pantallas', FIG.feLugares),
    'Con Flutter se escribe la app una vez y corre en celular, tablet y navegador. ' +
    'Pero una pantalla chica no se usa igual que una ventana de escritorio: cada una pide su propia distribución.'));

  // 7 · La idea que guía el curso
  window.SLIDES.push(H.withNotes(icesi.sectionSlideEGreen(
    'interfaz = f(estado)<br><small style="font-size:0.5em;">Cuando cambia el estado, la pantalla se vuelve a dibujar sola.</small>'
  ), 'En el frontend moderno la pantalla no se modifica a mano: se describe a partir del estado. ' +
    'Sobre esta idea están construidas las próximas sesiones: componentes, pantallas, estado y navegación.'));
})();
