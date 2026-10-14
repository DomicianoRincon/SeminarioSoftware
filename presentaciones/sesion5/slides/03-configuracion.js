// Bloque 2 · Configuración de MCP en Antigravity (slides 10 a 14). Fuente: lección S0035.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS, FIG = window.FIG;

  // 10 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Configuración de MCP en Antigravity<br><small style="font-size:0.5em;">Un archivo JSON y nada más.</small>'
  ));

  // 11 · El archivo .agents/mcp_config.json
  window.SLIDES.push(H.withNotes(icesi.slideStandard('El archivo .agents/mcp_config.json', FIG.mcpConfiguracion),
    'Todo cuelga de la clave mcpServers, y cada servidor tiene un nombre y sus parámetros. ' +
    'En el proyecto, el archivo se comparte con el equipo al hacer commit; también puede ir en ~/.gemini/config/mcp_config.json para todas las sesiones del computador. ' +
    'Si un servidor está en los dos lugares, gana el del proyecto. Las claves reales no se suben a un repositorio público.'));

  // 12 · Transporte local y remoto
  window.SLIDES.push(H.withNotes(icesi.slideTwoCols(
    'Transporte local y remoto',
    '<h3>Local &middot; stdio</h3>' + H.bigUl([
      [H.baseIcon('terminal'), 'Antigravity arranca el servidor como un proceso en tu equipo.'],
      [I.json, 'Se declara con <strong>command</strong>, <strong>args</strong> y <strong>env</strong>.'],
      [I.browser, 'Playwright y GitHub, con <strong>npx</strong>.']
    ]),
    '<h3>Remoto &middot; HTTP</h3>' + H.bigUl([
      [I.cloud, 'El servidor vive en la nube y no instalas nada.'],
      [I.json, 'Se declara con <strong>serverUrl</strong> y <strong>headers</strong>.'],
      [I.palette, 'Google Stitch, con tu clave de API.']
    ])
  ), 'Con npx, Node descarga y ejecuta el paquete sin instalarlo de forma global, y el -y acepta la descarga sin preguntar. ' +
    'En el remoto, los headers viajan en cada llamada y llevan la autenticación, como X-Goog-Api-Key en Stitch.'));

  // 13 · Ciclo de descubrimiento
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Ciclo de descubrimiento',
    '<div style="margin-top:70px;">' + H.bigPipeline([
      { icon: I.file, label: 'Lee el archivo', sub: '.agents/mcp_config.json<br>al abrir la sesión' },
      { icon: I.plug, label: 'Conecta', sub: 'HTTP a los remotos,<br>stdio a los locales' },
      { icon: I.ai, label: 'Descubre', sub: 'pide el catálogo y lo<br>agrega al contexto' }
    ]) + '</div>'
  ), 'Esto pasa solo, cada vez que se abre Antigravity en la carpeta del proyecto. Desde ese momento, cuando se le pide algo que necesita el diseño o el navegador, ya sabe qué herramienta llamar. ' +
    'Si se cambia el archivo, hay que reiniciar la sesión para que lo vuelva a leer.'));

  // 14 · Permisos
  window.SLIDES.push(H.withNotes(icesi.slideSidebarLeftOrange(
    'Permisos: tú mantienes el control',
    H.ul([
      [H.baseIcon('check'), 'Las <strong>lecturas</strong> corren sin pausas.'],
      [I.shield, 'Las <strong>acciones externas</strong> piden confirmación con sus parámetros.'],
      [I.key, '<strong>/permissions</strong> agrega reglas a la allowlist.'],
      [I.json, '<strong>mcp(playwright/*)</strong> libera un servidor completo.'],
      [H.baseIcon('alert'), '<strong>ask</strong> deja una herramienta con confirmación.']
    ]),
    { type: 'icons', items: [
      { icon: I.checkW, label: 'allow' },
      { icon: I.keyW, label: 'ask' },
      { icon: I.terminalW, label: '/permissions' }
    ] }
  ), 'Es el mismo principio de la sesión 4. En /permissions se baja con Tab hasta allowlist, se pulsa A, se escribe el patrón y se elige el alcance: Project o User. ' +
    'Patrones: mcp(playwright/*) para todo un servidor, mcp(playwright/browser_navigate) para una sola herramienta, mcp(*) para todos, solo en un entorno de pruebas. ' +
    'Las reglas también se escriben en ~/.gemini/antigravity-cli/settings.json, en allow, ask y deny.'));
})();
