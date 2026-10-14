# Colaboración con GitHub MCP

<!-- tags: GitHub MCP, server-github, gestión de issues, pull requests con IA, GITHUB_PERSONAL_ACCESS_TOKEN, automatización de repositorios, trabajo en equipo, trazabilidad del reto -->

Hasta ahora has conectado a Antigravity con dos herramientas externas: **Stitch** para el diseño visual y **Playwright** para la verificación en el navegador. Sin embargo, el software no se construye de forma aislada: en el Seminario trabajas en equipo y todo el ciclo de vida del proyecto vive en **GitHub**.

Con el servidor oficial de **GitHub MCP**, puedes permitir que Antigravity consulte tareas pendientes, reporte problemas encontrados en pruebas y abra Pull Requests directamente desde la conversación.

## Por qué conectar el agente a GitHub

En un equipo de desarrollo, las decisiones y los requerimientos no viajan por mensajes sueltos:

- Las tareas y especificaciones se documentan en **GitHub Issues**.
- Los cambios de código se proponen y auditan mediante **Pull Requests**.
- Las revisiones entre compañeros garantizan que nadie suba código roto a la rama principal.

Si el agente solo trabaja con archivos locales, tienes que copiar a mano los requerimientos del issue, pedirle que programe, probar y luego redactar el Pull Request manualmente. Al conectar el servidor MCP de GitHub, Antigravity puede leer el issue de origen, implementar la pantalla y redactar la solicitud de cambios con un resumen técnico detallado.

## La arquitectura de trabajo con GitHub MCP

El agente actúa como un colaborador activo del repositorio:

```svg
<svg id="ghFlujo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="ghFlujo-ttl ghFlujo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="ghFlujo-ttl">Gestión colaborativa con GitHub MCP</title>
  <desc id="ghFlujo-dsc">Tres bloques. A la izquierda, Antigravity gestionando el flujo de trabajo. En el centro, GitHub MCP Server con herramientas de issues y PRs. A la derecha, la plataforma de GitHub con el repositorio del equipo.</desc>
  <defs>
    <style>
      #ghFlujo .title{fill:#161A26;font-size:22px;font-weight:700}
      #ghFlujo .sub{fill:#79809A;font-size:13.5px}
      #ghFlujo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #ghFlujo .nt{font-size:15px;font-weight:700;fill:#161A26}
      #ghFlujo .nb{fill:#454C61;font-size:13px}
      #ghFlujo .lbl{fill:#556074;font-size:12px;font-weight:600}
      #ghFlujo .foot{fill:#79809A;font-size:12px}
      #ghFlujo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #ghFlujo .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#ghFlujo-arrow)}
    </style>
    <marker id="ghFlujo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="420" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Gestión colaborativa con GitHub MCP</text>
  <text class="sub" x="48" y="80" data-fit="860">Antigravity interactúa con el repositorio remoto para consultar issues, reportar hallazgos y abrir pull requests.</text>
  <rect x="48" y="120" width="250" height="160" rx="12" fill="#EEF1FF" stroke="#4453C9" stroke-width="2.5"/>
  <text x="72" y="154" font-size="16" font-weight="700" fill="#4453C9" text-anchor="start">Antigravity</text>
  <text x="72" y="180" font-size="13" font-weight="400" fill="#161A26" text-anchor="start">1. Lee requerimientos</text>
  <text x="72" y="204" font-size="13" font-weight="400" fill="#161A26" text-anchor="start">2. Implementa y audita</text>
  <text x="72" y="228" font-size="13" font-weight="400" fill="#161A26" text-anchor="start">3. Documenta hallazgos</text>
  <text x="72" y="252" font-size="13" font-weight="400" fill="#161A26" text-anchor="start">4. Abre Pull Request</text>
  <rect x="348" y="120" width="240" height="160" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="372" y="154" font-size="16" font-weight="700" fill="#7439B8" text-anchor="start" class="mono">GitHub MCP Server</text>
  <text x="372" y="182" font-size="13" font-weight="600" fill="#556074" text-anchor="start" class="mono">• list_issues / get</text>
  <text x="372" y="206" font-size="13" font-weight="600" fill="#556074" text-anchor="start" class="mono">• create_issue</text>
  <text x="372" y="230" font-size="13" font-weight="600" fill="#556074" text-anchor="start" class="mono">• create_pull_request</text>
  <text x="372" y="254" font-size="13" font-weight="600" fill="#556074" text-anchor="start" class="mono">• get_file_contents</text>
  <rect x="638" y="120" width="274" height="160" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
  <text x="662" y="154" font-size="16" font-weight="700" fill="#3A8235" text-anchor="start">GitHub del Equipo</text>
  <text x="662" y="182" font-size="13" font-weight="400" fill="#161A26" text-anchor="start">Issue #3: Pantalla de Login</text>
  <text x="662" y="206" font-size="13" font-weight="600" fill="#4453C9" text-anchor="start">PR #12: feat/auth-screens</text>
  <text x="662" y="230" font-size="13" font-weight="400" fill="#556074" text-anchor="start">Revisión por compañeros</text>
  <text x="662" y="254" font-size="12.5" font-weight="700" fill="#3A8235" text-anchor="start">Trazabilidad del reto</text>
  <path d="M298,185 H342" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#ghFlujo-arrow)"/>
  <path d="M342,215 H298" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#ghFlujo-arrow)"/>
  <path d="M588,185 H632" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#ghFlujo-arrow)"/>
  <path d="M632,215 H588" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#ghFlujo-arrow)"/>
  <rect x="48" y="306" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="332" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">Trazabilidad en equipo:</tspan> Antigravity conecta el trabajo local con el tablero de GitHub, documentando avances y abriendo revisiones de código automáticamente.</text>
</svg>
```

El ciclo se compone de cuatro pasos:

1. **Lectura de requerimientos:** Antigravity consulta los issues abiertos para comprender los criterios de aceptación y los campos obligatorios de la pantalla.
2. **Implementación y auditoría local:** Programa el código en Flutter apoyándose en Stitch y la skill `flutter-pantallas`.
3. **Documentación:** Si durante la verificación con Playwright encuentra un fallo visual o un error de validación, puede abrir un issue técnico con los pasos para reproducirlo.
4. **Propuesta de cambios:** Abre una rama y crea un Pull Request documentando los archivos modificados para que tus compañeros de equipo lo revisen.

## Configuración en mcp_config.json

Para registrar el servidor de GitHub en `.agents/mcp_config.json`, se añade el paquete `@modelcontextprotocol/server-github`:

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
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_tu_token_aqui"
      }
    }
  }
}
```

Para generar tu token de acceso personal (PAT):

- Ve a tu perfil en GitHub → *Settings* → *Developer settings* → *Personal access tokens*.
- Genera un token con permisos de lectura y escritura en repositorios (`repo`).
- **Regla estricta de seguridad:** Nunca hagas commit de tu token en ningún archivo público. Si compartes el repositorio, puedes configurar el token como variable de entorno en tu sistema (`$GITHUB_PERSONAL_ACCESS_TOKEN`) o en la configuración global de Antigravity en `~/.gemini/config/mcp_config.json`.

## Herramientas principales que incorpora el servidor

Al iniciar, GitHub MCP inyecta un conjunto de herramientas especializadas en la sesión de Antigravity:

- **`list_issues` y `get_issue`:** Permiten listar los requerimientos asignados a tu equipo y leer la descripción completa de una tarea.
- **`create_issue`:** Permite que el agente reporte automáticamente un bug con título, etiquetas y pasos de reproducción cuando una prueba de Playwright falla.
- **`create_pull_request`:** Abre un Pull Request desde una rama de trabajo hacia `main`, incluyendo una descripción estructurada de las pantallas agregadas.
- **`get_file_contents`:** Consulta archivos o ramas de otros repositorios sin necesidad de clonarlos localmente.

## Paso a paso: Configurar y experimentar con GitHub MCP

Sigue estos pasos para conectar Antigravity con los repositorios de tu equipo y experimentar la trazabilidad colaborativa:

- **Paso 1: Generar tu Personal Access Token (PAT):**
  En tu cuenta de GitHub (github.com), dirígete a *Settings* → *Developer settings* → *Personal access tokens* → *Tokens (classic)*. Genera un token nuevo con alcance `repo` (lectura y escritura de repositorios).

- **Paso 2: Registrar el servidor en tu entorno:**
  En el archivo `.agents/mcp_config.json` de tu proyecto, añade el bloque de GitHub dentro de `mcpServers`:
  ```json
  {
    "mcpServers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_tu_token_aqui"
        }
      }
    }
  }
  ```
  *Nota de seguridad:* Si tu repositorio es público o compartido, es preferible definir la variable en tu entorno del sistema o configurar el bloque en `~/.gemini/config/mcp_config.json` para no dejar expuesto el token en el historial de Git.

- **Paso 3: Experimentar la consulta de Issues del equipo:**
  Abre Antigravity en la carpeta del repositorio y pídele al agente:
  ```text
  > Consulta nuestro repositorio de GitHub
    y lista los issues abiertos para
    el sprint actual.
  ```
  Antigravity invocará `list_issues` y te entregará el listado estructurado con número de issue, título, autor y etiquetas.

- **Paso 4: Experimentar la lectura de especificaciones y reporte de tareas:**
  Pídele al agente que examine los criterios de aceptación de una tarea específica:
  ```text
  > Lee el Issue #3 de nuestro repositorio
    y resume los requisitos que debe
    cumplir la pantalla.
  ```
  También puedes probar la creación de un nuevo issue de seguimiento:
  ```text
  > Crea un issue titulado "Revisión de accesibilidad
    en formularios" con etiqueta "triage"
    y descripción breve del hallazgo.
  ```

- **Paso 5: Qué descubres con este ejercicio:**
  GitHub MCP convierte a Antigravity en un miembro activo del equipo: lee especificaciones directamente de los issues, documenta hallazgos y mantiene la trazabilidad del proyecto sin necesidad de copiar y pegar manualmente entre pestañas del navegador.

