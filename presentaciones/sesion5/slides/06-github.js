// Bloque 5 · GitHub MCP (slides 28 a 32). Fuente: lección S0039.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS, FIG = window.FIG;

  // 28 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'GitHub MCP<br><small style="font-size:0.5em;">El agente como colaborador del repositorio.</small>'
  ));

  // 29 · Lo que puedes hacer con GitHub MCP
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Lo que puedes hacer con GitHub MCP', FIG.ghCapacidades),
    'Leer issues con sus criterios de aceptación, reportar un fallo con los pasos para reproducirlo, abrir un pull request desde una rama y leer archivos de otros repositorios sin clonarlos. ' +
    'Lo delicado queda en ask: fusionar un PR, subir archivos directo y borrarlos piden confirmación.'));

  // 30 · El software se construye en equipo
  window.SLIDES.push(H.withNotes(icesi.slideStandard('El software se construye en equipo', FIG.ghFlujo),
    'En el Seminario se trabaja en equipo y el proyecto vive en GitHub: las tareas en issues, los cambios en pull requests y las revisiones entre compañeros. ' +
    'Sin MCP, hay que copiar a mano el issue, programar, probar y redactar el PR. Con GitHub MCP el agente lee el issue de origen, implementa y redacta el PR con un resumen técnico.'));

  // 31 · Herramientas de GitHub
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Herramientas de GitHub',
    '<div style="margin-top:28px;">' + H.bigCards([
      H.bigCard(I.issue, 'list_issues', 'Lista las tareas del equipo y lee una completa.', true),
      H.bigCard(H.baseIcon('alert'), 'create_issue', 'Reporta un fallo con etiquetas y pasos.', true),
      H.bigCard(I.branch, 'create_pull_request', 'Abre un PR hacia main con su descripción.', true),
      H.bigCard(I.file, 'get_file_contents', 'Lee archivos o ramas sin clonar.', true)
    ], 2) + '</div>'
  ), 'Para las reglas de permisos: mcp(github/*) en allow, y en ask las tres que se saltan la revisión entre compañeros: merge_pull_request, push_files y delete_file. ' +
    'La regla de ask es más específica que el comodín de allow, así que gana.'));

  // 32 · Paso a paso
  window.SLIDES.push(H.withNotes(icesi.slideSidebarLeftOrange(
    'Paso a paso: Experimenta con GitHub MCP',
    H.ul([
      [I.key, 'Crea un token de acceso personal con alcance <strong>repo</strong>.'],
      [I.json, 'Registra <strong>github</strong> en .agents/mcp_config.json.'],
      [I.issue, 'Pide la lista de issues abiertos del sprint.'],
      [I.file, 'Pide un resumen de los requisitos del issue #3.'],
      [H.baseIcon('alert'), 'Pide que cree un issue de seguimiento.']
    ]),
    { type: 'icons', items: [
      { icon: I.keyW, label: 'Token personal' },
      { icon: I.branchW, label: 'Repositorio del equipo' },
      { icon: I.checkW, label: 'Issues desde el chat' }
    ] }
  ), 'El token se crea en Settings, Developer settings, Personal access tokens, Tokens (classic). Va en env, como GITHUB_PERSONAL_ACCESS_TOKEN. ' +
    'Regla estricta: nunca se hace commit del token. Si el repositorio es público o compartido, se define como variable de entorno del sistema o en la configuración global de Antigravity.'));
})();
