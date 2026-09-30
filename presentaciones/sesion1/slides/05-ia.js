// Bloque 4 · Desarrollar con IA (slides 15 a 19). Fuente: lección S0006.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  // 15 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Desarrollar con IA<br><small style="font-size:0.5em;">La IA escribe y ejecuta. Tú diriges.</small>'
  ));

  // 16 · A mano o con IA
  window.SLIDES.push(H.withNotes(icesi.slideStandard('A mano o potenciado con IA', FIG.iaManos),
    'Con IA se escribe menos código, pero hay que entender más. Si no saben qué es un estado o un componente, ' +
    'no pueden saber si lo que hizo la IA está bien. Esta es la razón por la que el curso insiste en los conceptos.'));

  // 17 · Chat vs agente
  window.SLIDES.push(H.withNotes(icesi.slideStandard('De un chat a un agente', FIG.iaTools),
    'Claude Code, OpenCode CLI y Antigravity CLI corren en la consola, dentro del proyecto. ' +
    'Su tool system es el conjunto de herramientas que el modelo puede usar: leer archivos, buscar en el código, editarlos y ejecutar comandos. ' +
    'Preguntar: ¿quién ha copiado y pegado código de un chat? Eso es lo que el agente ya no necesita.'));

  // 18 · Un agente en acción
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Un agente en acción', H.consoleSlide(FIG.iaAgente, [
    [1, 'Tú pides', 'En lenguaje natural: qué quieres, no cómo se escribe.'],
    [2, 'La IA usa herramientas', 'Lee y edita tus archivos. Cada acción queda a la vista.'],
    [3, 'Tú autorizas', 'Antes de ejecutar un comando pide permiso. Tú decides.']
  ])), 'Es una sesión de Claude Code, simplificada y en español. En OpenCode o Antigravity CLI el flujo es parecido. ' +
    'Se abre desde la carpeta del proyecto con el comando de cada herramienta (en Claude Code: claude).'));

  // 19 · Tú al mando
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Tú al mando', FIG.iaMando),
    'Human in the lead: la IA hace buena parte del trabajo, pero el objetivo, las reglas y la última palabra son de ustedes. ' +
    'Si la IA se equivoca y lo aceptaron, el error es de ustedes. En la unidad 3 del curso aprenden a configurar al agente para que trabaje como quieren.'));
})();
