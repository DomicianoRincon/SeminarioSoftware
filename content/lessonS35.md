# Configurar MCP en Antigravity

<!-- tags: mcp_config.json, mcpServers, configurar MCP, permisos MCP, /permissions, transporte stdio, npx mcp, herramientas externas en Antigravity, .agents/mcp_config.json -->

Para que Antigravity pueda utilizar un servidor MCP, solo necesitas decírselo en un archivo JSON. No tienes que compilar servidores ni modificar el código de la aplicación.

## Dónde vive la configuración

Tienes dos lugares para registrar servidores MCP:

- **En el proyecto (`.agents/mcp_config.json`):** Queda guardado en la carpeta del repositorio y se comparte con todo el equipo cuando hacen commit. Es la opción recomendada en el curso porque garantiza que todos los integrantes tengan exactamente las mismas herramientas.
- **En tu equipo (`~/.gemini/config/mcp_config.json`):** Aplica para todas las sesiones de Antigravity en tu computador personal, sin importar en qué carpeta lo abras.

Si un servidor está configurado en ambos lugares, la configuración dentro del proyecto tiene prioridad.

## La estructura de mcp_config.json

El archivo contiene un objeto principal llamado `mcpServers`. Dentro de él, cada servidor tiene un identificador y sus parámetros de ejecución:

```svg
<svg id="mcpConfiguracion" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 666" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="mcpConfiguracion-ttl mcpConfiguracion-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="mcpConfiguracion-ttl">Configuración en .agents/mcp_config.json</title>
  <desc id="mcpConfiguracion-dsc">El archivo mcp_config.json define los servidores en la clave mcpServers. Soporta servidores remotos (serverUrl y headers) y locales (command y args).</desc>
  <defs>
    <style>
      #mcpConfiguracion .title{fill:#161A26;font-size:22px;font-weight:700}
      #mcpConfiguracion .sub{fill:#79809A;font-size:13.5px}
      #mcpConfiguracion .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #mcpConfiguracion .cl{font-size:13px;fill:#C9CFDA}
      #mcpConfiguracion .s{fill:#A8D8A0} #mcpConfiguracion .n{fill:#F2B880} #mcpConfiguracion .c{fill:#7FD1E8}
      #mcpConfiguracion .p{fill:#D5B8F5} #mcpConfiguracion .k{fill:#F08FB0}
      #mcpConfiguracion .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #mcpConfiguracion .ct{fill:#161A26;font-size:14px;font-weight:700}
      #mcpConfiguracion .cb{fill:#454C61;font-size:13px}
      #mcpConfiguracion .rt{fill:#161A26;font-size:14px} #mcpConfiguracion .rs{fill:#79809A;font-size:12px}
      #mcpConfiguracion .foot{fill:#79809A;font-size:12px}
      #mcpConfiguracion .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #mcpConfiguracion .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #mcpConfiguracion .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#mcpConfiguracion-ar-amber)}
      #mcpConfiguracion .hl-teal{fill:#86D3CA;fill-opacity:.16;stroke:#86D3CA;stroke-width:1.5}
      #mcpConfiguracion .ld-teal{fill:none;stroke:#86D3CA;stroke-width:1.5;stroke-dasharray:3 4}
      #mcpConfiguracion .ar-teal{fill:none;stroke:#0F8478;stroke-width:1.75;marker-end:url(#mcpConfiguracion-ar-teal)}
    </style>
    <marker id="mcpConfiguracion-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="mcpConfiguracion-ar-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#0F8478"/></marker>
  </defs>
  <rect width="960" height="666" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Configuración en <tspan class="mono">.agents/mcp_config.json</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Antigravity conecta o levanta cada servidor al arrancar la sesión.</text>
  <rect x="48" y="112" width="456" height="396" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">.agents/mcp_config.json</text>
  <rect x="552" y="112" width="360" height="396" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">QUÉ HACE CADA SERVIDOR</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="95.2" y="204" width="78.2" height="22" rx="5"/>
  <rect class="hl-teal" x="95.2" y="348" width="109.4" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">{</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="117.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">"mcpServers"</tspan>: {</text>
  <text class="cl mono" font-size="13" x="99.2" y="220" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">"stitch"</tspan>: {</text>
  <text class="cl mono" font-size="13" x="114.8" y="244" textLength="382.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">"serverUrl"</tspan>: <tspan class="s">"https://stitch.googleapis.com/mcp"</tspan>,</text>
  <text class="cl mono" font-size="13" x="114.8" y="268" textLength="93.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">"headers"</tspan>: {</text>
  <text class="cl mono" font-size="13" x="130.4" y="292" textLength="179.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">"X-Goog-Api-Key"</tspan>: <tspan class="s">"key"</tspan></text>
  <text class="cl mono" font-size="13" x="114.8" y="316" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="99.2" y="340" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">},</text>
  <text class="cl mono" font-size="13" x="99.2" y="364" textLength="117.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">"playwright"</tspan>: {</text>
  <text class="cl mono" font-size="13" x="114.8" y="388" textLength="132.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">"command"</tspan>: <tspan class="s">"npx"</tspan>,</text>
  <text class="cl mono" font-size="13" x="114.8" y="412" textLength="312.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="s">"args"</tspan>: [<tspan class="s">"-y"</tspan>, <tspan class="s">"@playwright/mcp@latest"</tspan>]</text>
  <text class="cl mono" font-size="13" x="99.2" y="436" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="83.6" y="460" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="484" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <g transform="translate(552,144)">

<g transform="translate(16,26)">
  <rect width="328" height="90" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="16" y="32" font-size="14" font-weight="700" fill="#A96C05" class="mono">stitch</text>
  <text x="16" y="54" font-size="12.5" fill="#454C61">Servidor remoto en la nube.</text>
  <text x="16" y="74" font-size="12.5" fill="#454C61">Extrae tokens visuales, colores y pantallas.</text>
</g>
<g transform="translate(16,194)">
  <rect width="328" height="90" rx="10" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="16" y="32" font-size="14" font-weight="700" fill="#0F8478" class="mono">playwright</text>
  <text x="16" y="54" font-size="12.5" fill="#454C61">Controla Chromium en vivo.</text>
  <text x="16" y="74" font-size="12.5" fill="#454C61">Lee el árbol de accesibilidad y simula clics.</text>
</g>

  </g>
  <path class="ld-amber" d="M191.0,215 H504"/>
  <path class="ar-amber" d="M504,215 H568"/>
  <path class="ld-teal" d="M222.2,359 H504"/>
  <path class="ar-teal" d="M504,359 H514 V383 H568"/>
  <g transform="translate(48.0,532)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#FFF3DC" stroke="#A96C05" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="366">Stitch MCP</text>
    <text class="cb" x="16" y="60" data-fit="392">Prototipado rápido de interfaces</text>
    <text class="cb" x="16" y="79" data-fit="392">y extracción de diseño.</text>
  </g>
  <g transform="translate(488.0,532)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle cx="24" cy="26" r="7" fill="#E3F6F3" stroke="#0F8478" stroke-width="2"/>
    <text class="ct mono" x="42" y="26" dy="0.35em" data-fit="366">Playwright MCP</text>
    <text class="cb" x="16" y="60" data-fit="392">Automatización y verificación</text>
    <text class="cb" x="16" y="79" data-fit="392">de la app en el navegador.</text>
  </g>
</svg>
```

```json
{
  "mcpServers": {
    "stitch": {
      "serverUrl": "https://stitch.googleapis.com/mcp",
      "headers": {
        "X-Goog-Api-Key": "key"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

Cada tipo de servidor declara su mecanismo de conexión:

- **Servidores remotos por HTTP (`serverUrl` y `headers`):** Como Google Stitch. Antigravity se comunica directamente con el endpoint en la nube sin necesidad de iniciar procesos locales en tu computador.
  - **`serverUrl`:** La dirección HTTPS del servidor MCP (`https://stitch.googleapis.com/mcp`).
  - **`headers`:** Encabezados HTTP enviados en cada llamada, utilizados para autenticación mediante claves de API (como `X-Goog-Api-Key`).
- **Servidores locales por stdio (`command`, `args`, `env`):** Como Playwright. Antigravity arranca el servidor como un proceso hijo en tu máquina:
  - **`command`:** El ejecutable que inicia el servidor. Al usar `npx`, Node descarga y ejecuta el paquete automáticamente sin necesidad de instalarlo de forma global en tu máquina.
  - **`args`:** La lista de argumentos para el comando. El modificador `-y` le indica a `npx` que acepte la descarga de dependencias sin detenerse a preguntar en la consola.
  - **`env`:** Variables de entorno necesarias para el proceso, como credenciales o configuraciones del sistema.

## El ciclo de descubrimiento de herramientas

Cuando abres Antigravity en la carpeta de tu proyecto, el sistema realiza tres pasos de forma transparente:

1. **Lectura del archivo:** Busca `.agents/mcp_config.json` en la raíz del espacio de trabajo.
2. **Conexión con los servidores:** Conecta vía HTTP con los servicios remotos y arranca en segundo plano los procesos locales mediante `stdio`.
3. **Descubrimiento de herramientas:** Le pregunta a cada servidor qué herramientas tiene disponibles y agrega sus firmas y descripciones al contexto de trabajo del modelo.

A partir de ese instante, cuando le pides al agente una tarea que requiere interactuar con el diseño o con el navegador, Antigravity sabrá qué herramienta invocar.

## Permisos y seguridad

En la sesión 4 configuraste las reglas de permiso para que Antigravity no edite archivos ni ejecute comandos sin tu autorización. Con los servidores MCP aplica el mismo principio de control:

- **Lecturas seguras:** Operaciones como consultar la estructura de un diseño o inspeccionar el contenido de una página suelen ejecutarse fluidamente.
- **Acciones externas:** Si una herramienta realiza acciones que modifican recursos remotos, envían peticiones a servicios de terceros o ejecutan scripts externos, Antigravity te mostrará el nombre de la herramienta y sus parámetros para que confirmes antes de proceder.

### Ejecutar herramientas MCP libremente con /permissions

Cuando interactúas con servidores como Playwright o Stitch, confirmar manualmente cada clic, campo de texto o captura de accesibilidad puede volverse repetitivo e interrumpir la fluidez del agente. Para permitir que Antigravity ejecute las herramientas de un servidor MCP sin pedir confirmación en cada llamada, puedes agregarlas a la lista de permitidos (**allowlist**) mediante el comando `/permissions` (o `/permission`).

**Paso a paso para autorizar un servidor MCP:**

1. En la consola interactiva de Antigravity, escribe:
   ```text
   /permissions
   ```
2. Desplázate con la tecla **Tab** hasta situarte en la sección **allowlist**.
3. Presiona la tecla **A** (*Add*) para registrar una nueva regla.
4. Escribe el patrón de permiso según el nivel de libertad que desees otorgar:
   - **Para un servidor específico:** autoriza todas las herramientas de ese servidor. Por ejemplo:
     - `mcp(playwright/*)` para permitir que Playwright navegue, haga clics y rellene formularios sin pausas.
     - `mcp(stitch/*)` para permitir consultas e inspección en Google Stitch.
   - **Para una herramienta puntual:** si solo deseas liberar una acción concreta:
     - `mcp(playwright/browser_navigate)`
   - **Para todos los servidores MCP:** si estás en un entorno de pruebas controlado y quieres habilitar cualquier herramienta de cualquier MCP:
     - `mcp(*)`
5. Presiona **Enter** y selecciona el alcance (**Scope**):
   - Elige **Project** para que la autorización aplique únicamente a este repositorio.
   - Elige **User** si deseas que la regla aplique a todos tus proyectos en tu equipo.

También puedes definir estas reglas de forma permanente en tu archivo global de configuración (`~/.gemini/antigravity-cli/settings.json`), dentro del arreglo `"allow"`:

```json
{
  "permissions": {
    "allow": [
      "mcp(playwright/*)",
      "mcp(stitch/*)"
    ],
    "ask": [
      "write_file(*)",
      "command(*)"
    ],
    "deny": []
  }
}
```

Con esta configuración, el agente conserva la protección sobre tus archivos locales y comandos de terminal, mientras ejecuta con total libertad y rapidez las herramientas especializadas de tus servidores MCP.

En la siguiente lección conectaremos el primer servidor: Google Stitch MCP.
