# ¿Qué es MCP?

<!-- tags: MCP, Model Context Protocol, servidor MCP, herramientas externas, protocolo abierto, transporte stdio, host y cliente, JSON-RPC, AGENTS.md vs skill vs MCP -->

En la sesión anterior aprendiste a dirigir a Antigravity con dos herramientas: `AGENTS.md` para las reglas generales del proyecto y las **skills** para explicarle procedimientos paso a paso. Con eso el agente puede escribir código limpio y organizado, pero sigue encerrado en tu disco duro: no puede abrir un navegador, no puede ver un diseño en la nube y no puede consultar una base de datos externa.

Para romper esa barrera existe **MCP** (*Model Context Protocol*).

## De las instrucciones a las herramientas

Una regla en `AGENTS.md` o una skill le dicen al agente **cómo pensar**: qué convenciones usar, qué paleta de widgets respetar o cómo estructurar una pantalla. Sin embargo, el agente solo cuenta con cuatro capacidades nativas: leer archivos, buscar en el código, editar archivos y ejecutar comandos de terminal.

¿Qué ocurre cuando necesitas que el agente consulte un prototipo visual en la nube, inspeccione una base de datos remota o abra un navegador real para verificar si un botón funciona?

No puedes poner una base de datos o un navegador dentro de un archivo de texto. Necesitas darle al agente **herramientas vivas**.

El **Model Context Protocol** es un estándar abierto que permite conectar modelos de inteligencia artificial con herramientas y fuentes de datos externas mediante una interfaz universal y segura.

## La arquitectura de MCP

El protocolo funciona bajo una arquitectura cliente-servidor muy clara:

```svg
<svg id="mcpArquitectura" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 440" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="mcpArquitectura-ttl mcpArquitectura-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="mcpArquitectura-ttl">Arquitectura del Model Context Protocol (MCP)</title>
  <desc id="mcpArquitectura-dsc">Tres bloques horizontales. A la izquierda, Antigravity Host y Cliente. En el centro, dos Servidores MCP: Stitch y Playwright. A la derecha, los servicios externos: el lienzo de Stitch y el navegador Chromium.</desc>
  <defs>
    <style>
      #mcpArquitectura .title{fill:#161A26;font-size:22px;font-weight:700}
      #mcpArquitectura .sub{fill:#79809A;font-size:13.5px}
      #mcpArquitectura .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #mcpArquitectura .nt{font-size:15px;font-weight:700;fill:#161A26}
      #mcpArquitectura .nb{fill:#454C61;font-size:13px}
      #mcpArquitectura .lbl{fill:#556074;font-size:12px;font-weight:600}
      #mcpArquitectura .foot{fill:#79809A;font-size:12px}
      #mcpArquitectura .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #mcpArquitectura .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#mcpArquitectura-arrow)}
    </style>
    <marker id="mcpArquitectura-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="440" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Arquitectura del Model Context Protocol (MCP)</text>
  <text class="sub" x="48" y="80" data-fit="860">Antigravity actúa como Host y Cliente. Se comunica con servidores independientes mediante stdio (JSON-RPC).</text>
  <rect x="48" y="120" width="260" height="210" rx="12" fill="#EEF1FF" stroke="#4453C9" stroke-width="2.5"/>
  <text x="72" y="154" font-size="17" font-weight="700" fill="#4453C9" text-anchor="start">Google Antigravity</text>
  <text x="72" y="178" font-size="13" font-weight="600" fill="#556074" text-anchor="start">Host y Cliente MCP</text>
  <text x="72" y="212" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start">• Motor de razonamiento</text>
  <text x="72" y="236" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start">• Reglas de AGENTS.md</text>
  <text x="72" y="260" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start">• Skills activadas</text>
  <text x="72" y="284" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start">• Gestión de permisos</text>
  <rect x="356" y="120" width="250" height="96" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="376" y="150" font-size="15" font-weight="700" fill="#A96C05" text-anchor="start" class="mono">Stitch MCP Server</text>
  <text x="376" y="174" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Proceso local · stdio</text>
  <text x="376" y="194" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start">Herramientas de UI / tokens</text>
  <rect x="356" y="234" width="250" height="96" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="376" y="264" font-size="15" font-weight="700" fill="#0F8478" text-anchor="start" class="mono">Playwright MCP Server</text>
  <text x="376" y="288" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Proceso local · stdio</text>
  <text x="376" y="308" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start">Herramientas de navegador</text>
  <rect x="654" y="120" width="258" height="96" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5" stroke-dasharray="6 4"/>
  <text x="674" y="150" font-size="15" font-weight="700" fill="#A96C05" text-anchor="start">Google Stitch Web</text>
  <text x="674" y="174" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">stitch.withgoogle.com</text>
  <text x="674" y="194" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start">Lienzo de diseño con IA</text>
  <rect x="654" y="234" width="258" height="96" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5" stroke-dasharray="6 4"/>
  <text x="674" y="264" font-size="15" font-weight="700" fill="#0F8478" text-anchor="start">Navegador Chromium</text>
  <text x="674" y="288" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Local · Headless / Visible</text>
  <text x="674" y="308" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start">Árbol de accesibilidad y clics</text>
  <path d="M308,168 H350" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#mcpArquitectura-arrow)"/>
  <path d="M308,282 H350" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#mcpArquitectura-arrow)"/>
  <path d="M606,168 H648" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#mcpArquitectura-arrow)"/>
  <path d="M606,282 H648" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#mcpArquitectura-arrow)"/>
  <rect x="48" y="356" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="382" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">Protocolo abierto:</tspan> Antigravity no sabe qué hace cada servicio internamente; solo se comunica mediante el catálogo de herramientas que cada servidor MCP publica.</text>
</svg>
```

Tres piezas componen este sistema:

- **Host y Cliente (Antigravity):** Es el entorno donde trabajas. Antigravity actúa como host del modelo y como cliente MCP. Se encarga de descubrir los servidores configurados, consultar qué herramientas ofrecen y decidir cuándo invocarlas según lo que le pidas.
- **Servidores MCP (Procesos locales):** Son programas independientes que implementan el protocolo. Cada servidor se especializa en una tarea: uno sabe hablar con Google Stitch, otro sabe controlar un navegador Chromium mediante Playwright y otro sabe conectarse a Postgres.
- **Recursos y Servicios externos:** Es el mundo real con el que interactúa cada servidor: la plataforma web de Stitch, un navegador en ejecución, APIs en la nube o archivos remotos.

El agente nunca necesita conocer los detalles internos de cómo funciona Playwright o cómo se comunica la API de Stitch. El servidor MCP expone un catálogo de herramientas con nombres, descripciones y parámetros en formato JSON-RPC. Antigravity lee ese catálogo y sabe exactamente cuándo y cómo llamar a cada herramienta.

## La tríada del desarrollo asistido

Con MCP se completa el sistema de trabajo para guiar a Antigravity en proyectos reales:

```svg
<svg id="mcpTriada" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 390" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="mcpTriada-ttl mcpTriada-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="mcpTriada-ttl">La tríada del desarrollo con Antigravity</title>
  <desc id="mcpTriada-dsc">Tres tarjetas comparativas. AGENTS.md representa las reglas fijas en cada pedido. Las Skills representan metodologías bajo demanda en Markdown. Los Servidores MCP representan herramientas y conexiones vivas ejecutables.</desc>
  <defs>
    <style>
      #mcpTriada .title{fill:#161A26;font-size:22px;font-weight:700}
      #mcpTriada .sub{fill:#79809A;font-size:13.5px}
      #mcpTriada .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #mcpTriada .nt{font-size:15px;font-weight:700;fill:#161A26}
      #mcpTriada .nb{fill:#454C61;font-size:13px}
      #mcpTriada .lbl{fill:#556074;font-size:12px;font-weight:600}
      #mcpTriada .foot{fill:#79809A;font-size:12px}
      #mcpTriada .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #mcpTriada .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#mcpTriada-arrow)}
    </style>
    <marker id="mcpTriada-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="390" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La tríada del desarrollo con Antigravity</text>
  <text class="sub" x="48" y="80" data-fit="860">Reglas fijas, metodologías bajo demanda y herramientas externas vivas.</text>
  <rect x="48" y="120" width="264" height="180" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <circle cx="76" cy="146" r="11" fill="#7439B8"/><text x="76" y="150.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">1</text>
  <text x="98" y="151" font-size="15" font-weight="700" fill="#7439B8" text-anchor="start" class="mono">AGENTS.md</text>
  <text x="68" y="184" font-size="14" font-weight="700" fill="#161A26" text-anchor="start">Reglas fijas</text>
  <text x="68" y="208" font-size="13" font-weight="400" fill="#556074" text-anchor="start">Viaja en cada pedido.</text>
  <text x="68" y="228" font-size="13" font-weight="400" fill="#556074" text-anchor="start">Convenciones del equipo,</text>
  <text x="68" y="248" font-size="13" font-weight="400" fill="#556074" text-anchor="start">imports y estilo de código.</text>
  <text x="68" y="276" font-size="12" font-weight="700" fill="#7439B8" text-anchor="start">Alcance: Todo el repo</text>
  <rect x="348" y="120" width="264" height="180" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <circle cx="376" cy="146" r="11" fill="#4453C9"/><text x="376" y="150.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">2</text>
  <text x="398" y="151" font-size="15" font-weight="700" fill="#4453C9" text-anchor="start" class="mono">Skills</text>
  <text x="368" y="184" font-size="14" font-weight="700" fill="#161A26" text-anchor="start">Metodología</text>
  <text x="368" y="208" font-size="13" font-weight="400" fill="#556074" text-anchor="start">Se carga solo si coincide.</text>
  <text x="368" y="228" font-size="13" font-weight="400" fill="#556074" text-anchor="start">Paleta de widgets, pasos</text>
  <text x="368" y="248" font-size="13" font-weight="400" fill="#556074" text-anchor="start">y plantillas de código.</text>
  <text x="368" y="276" font-size="12" font-weight="700" fill="#4453C9" text-anchor="start">Alcance: Tareas específicas</text>
  <rect x="648" y="120" width="264" height="180" rx="12" fill="#E3F6F3" stroke="#0F8478" stroke-width="2.5"/>
  <circle cx="676" cy="146" r="11" fill="#0F8478"/><text x="676" y="150.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">3</text>
  <text x="698" y="151" font-size="15" font-weight="700" fill="#0F8478" text-anchor="start" class="mono">Servidores MCP</text>
  <text x="668" y="184" font-size="14" font-weight="700" fill="#161A26" text-anchor="start">Herramientas vivas</text>
  <text x="668" y="208" font-size="13" font-weight="400" fill="#556074" text-anchor="start">Conexión con el exterior.</text>
  <text x="668" y="228" font-size="13" font-weight="400" fill="#556074" text-anchor="start">Consultar Stitch, abrir</text>
  <text x="668" y="248" font-size="13" font-weight="400" fill="#556074" text-anchor="start">el navegador, bases de datos.</text>
  <text x="668" y="276" font-size="12" font-weight="700" fill="#0F8478" text-anchor="start">Alcance: El mundo exterior</text>
  <rect x="48" y="316" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="342" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">Diferencia clave:</tspan> Una skill le enseña al agente cómo pensar; un servidor MCP le da manos y ojos para interactuar con sistemas reales.</text>
</svg>
```

Cada nivel resuelve un problema diferente:

- **AGENTS.md (Reglas globales):** Aplica a todo el repositorio en cada mensaje. Es corto y define la identidad del proyecto, las librerías permitidas y las restricciones generales.
- **Skills (Metodología bajo demanda):** Se cargan únicamente cuando la tarea coincide con su descripción. Guardan listas largas, paletas de diseño, plantillas de código y guías de paso a paso.
- **Servidores MCP (Capacidades externas):** Le dan al agente ojos y manos fuera del editor. Le permiten consultar servicios web, ejecutar pruebas en navegadores y traer información viva al contexto de trabajo.

## Cómo se comunica: el transporte stdio

Existen dos formas de conectar un servidor MCP con Antigravity:

- **Transporte local (`stdio`):** Antigravity arranca el servidor MCP como un proceso hijo en tu propio computador y se comunica con él a través de la entrada y salida estándar (*standard input / output*). Es el mecanismo más rápido, seguro y común para desarrollo, y no requiere configurar puertos de red ni certificados SSL.
- **Transporte remoto (`Streamable HTTP`):** El servidor MCP se ejecuta en un servidor remoto y Antigravity se conecta a él mediante peticiones HTTP. Se utiliza para servicios compartidos en equipos corporativos.

En este curso utilizaremos el transporte local (`stdio`) ejecutando paquetes mediante `npx`. En la siguiente lección aprenderás a registrar tus primeros servidores en `mcp_config.json`.
