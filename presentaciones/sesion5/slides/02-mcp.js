// Bloque 1 · Qué es MCP (slides 4 a 9). Fuente: lección S0034.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, I = H.ICONS, FIG = window.FIG;

  // 4 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'De las instrucciones a las herramientas<br><small style="font-size:0.5em;">Qué es el Model Context Protocol.</small>'
  ));

  // 5 · El límite de una caja cerrada
  window.SLIDES.push(H.withNotes(icesi.slideTwoCols(
    'El límite de una caja cerrada',
    '<h3>Lo que el agente ya sabe hacer</h3>' + H.bigUl([
      [I.file, 'Leer los archivos del proyecto.'],
      [H.baseIcon('code'), 'Buscar en el código.'],
      [I.edit, 'Editar archivos.'],
      [H.baseIcon('terminal'), 'Ejecutar comandos en la terminal.']
    ]),
    '<h3>Lo que no puede hacer</h3>' + H.bigUl([
      [I.palette, 'Ver un diseño que vive en la nube.'],
      [I.browser, 'Abrir un navegador y hacer clic.'],
      [H.baseIcon('database'), 'Consultar una base de datos remota.'],
      [I.branch, 'Leer los issues del equipo.']
    ])
  ), 'AGENTS.md y las skills le dicen al agente cómo pensar: convenciones, paleta de widgets, cómo se arma una pantalla. Pero sigue encerrado en el disco: solo tiene cuatro capacidades nativas. ' +
    'No se puede meter un navegador o una base de datos dentro de un archivo de texto. Hace falta darle herramientas vivas, y para eso existe MCP.'));

  // 6 · Qué es el Model Context Protocol
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Qué es el Model Context Protocol', FIG.mcpArquitectura),
    'MCP es un estándar abierto para conectar modelos de IA con herramientas y fuentes de datos externas por una interfaz única. ' +
    'Antigravity es el host y el cliente; cada servidor MCP expone un catálogo de herramientas con nombre, descripción y parámetros en JSON-RPC; y detrás de cada servidor está el servicio real: Stitch, un navegador, GitHub.'));

  // 7 · Host, Cliente y Servidor
  window.SLIDES.push(H.withNotes(icesi.slideStandard(
    'Host, Cliente y Servidor',
    '<div style="margin-top:40px;">' + H.bigCards([
      H.bigCard(I.ai, 'Host y cliente', 'Antigravity descubre los servidores, lee sus herramientas y decide cuándo usarlas.'),
      H.bigCard(I.plug, 'Servidor MCP', 'Un programa que expone herramientas: local por stdio o remoto por HTTP.'),
      H.bigCard(I.cloud, 'Servicio externo', 'El mundo real: Stitch, un navegador, una API o un repositorio.')
    ], 3) + '</div>' +
    '<p style="margin-top:48px;text-align:center;font-size:24px;">El agente no necesita saber cómo funciona Playwright por dentro &middot; le basta el catálogo</p>'
  ), 'La separación es lo que hace útil al protocolo: el servidor esconde los detalles del servicio y el agente solo ve herramientas con nombre y parámetros. ' +
    'Por eso el mismo Antigravity puede usar Stitch, Playwright y GitHub sin que nadie lo programe para cada uno.'));

  // 8 · La tríada de Antigravity
  window.SLIDES.push(H.withNotes(icesi.slideStandard('La tríada de Antigravity', FIG.mcpTriada),
    'AGENTS.md aplica a todo el repositorio en cada mensaje: es corto y define identidad, librerías y restricciones. ' +
    'Las skills se cargan solo cuando la tarea coincide con su descripción: guardan las guías largas. ' +
    'Los servidores MCP le dan al agente ojos y manos fuera del editor. Cada nivel resuelve un problema distinto.'));

  // 9 · La idea de la sesión
  window.SLIDES.push(icesi.sectionSlideEGreen(
    'Una skill le enseña al agente cómo pensar<br><small style="font-size:0.5em;">Un servidor MCP le da manos y ojos para trabajar con sistemas reales.</small>'
  ));
})();
