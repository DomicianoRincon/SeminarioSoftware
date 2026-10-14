# Automatización con Playwright MCP

<!-- tags: Playwright MCP, @playwright/mcp, automatización con IA, árbol de accesibilidad, pruebas de interfaz, verificar pantalla en navegador, Flutter web, navegador Chromium -->

Una vez que Antigravity genera una pantalla de Flutter, el paso natural es abrirla y comprobar que los campos de texto respondan, que los botones estén en su lugar y que el diseño no se rompa. En lugar de hacer clics manuales repetitivos en cada iteración, puedes darle a Antigravity un navegador real mediante **Playwright MCP**.

## Qué es Playwright MCP

**Playwright** es la herramienta de automatización de navegadores web desarrollada por Microsoft. Su servidor oficial para el Model Context Protocol (`@playwright/mcp`) expone las capacidades del motor Chromium para que un asistente de inteligencia artificial pueda navegar por páginas web, hacer clic en botones, rellenar formularios e inspeccionar el contenido renderizado.

Se instala y ejecuta automáticamente con `npx -y @playwright/mcp@latest` a través del transporte `stdio`.

## Cómo ve el agente una página web

Cuando una persona mira una interfaz, procesa pixeles, sombras y tipografías. Si le pides a un modelo de IA que analice una página mediante capturas de pantalla continuas, se consumen miles de tokens por cada imagen y la detección de elementos resulta lenta y propensa a fallos.

Playwright MCP resuelve esto utilizando el **árbol de accesibilidad** (*accessibility tree*):

```svg
<svg id="pwFlujo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 420" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="pwFlujo-ttl pwFlujo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="pwFlujo-ttl">Cómo Playwright MCP interactúa con la aplicación</title>
  <desc id="pwFlujo-dsc">El agente envía instrucciones a Playwright MCP. Playwright lee el árbol de accesibilidad de la página y ejecuta acciones reales: rellenar campos, hacer clic y verificar la respuesta.</desc>
  <defs>
    <style>
      #pwFlujo .title{fill:#161A26;font-size:22px;font-weight:700}
      #pwFlujo .sub{fill:#79809A;font-size:13.5px}
      #pwFlujo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #pwFlujo .nt{font-size:15px;font-weight:700;fill:#161A26}
      #pwFlujo .nb{fill:#454C61;font-size:13px}
      #pwFlujo .lbl{fill:#556074;font-size:12px;font-weight:600}
      #pwFlujo .foot{fill:#79809A;font-size:12px}
      #pwFlujo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #pwFlujo .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#pwFlujo-arrow)}
    </style>
    <marker id="pwFlujo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="420" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Cómo Playwright MCP interactúa con la aplicación</text>
  <text class="sub" x="48" y="80" data-fit="860">Antigravity inspecciona la semántica del navegador mediante el árbol de accesibilidad.</text>
  <rect x="48" y="120" width="250" height="160" rx="12" fill="#EEF1FF" stroke="#4453C9" stroke-width="2.5"/>
  <text x="72" y="154" font-size="16" font-weight="700" fill="#4453C9" text-anchor="start">Antigravity</text>
  <text x="72" y="180" font-size="13" font-weight="400" fill="#161A26" text-anchor="start">1. Solicita navegar a URL</text>
  <text x="72" y="204" font-size="13" font-weight="400" fill="#161A26" text-anchor="start">2. Analiza el snapshot</text>
  <text x="72" y="228" font-size="13" font-weight="400" fill="#161A26" text-anchor="start">3. Ordena fill y click</text>
  <text x="72" y="252" font-size="13" font-weight="400" fill="#161A26" text-anchor="start">4. Verifica resultado</text>
  <rect x="348" y="120" width="240" height="160" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="372" y="154" font-size="16" font-weight="700" fill="#0F8478" text-anchor="start" class="mono">Playwright MCP</text>
  <text x="372" y="182" font-size="13" font-weight="600" fill="#556074" text-anchor="start" class="mono">• browser_navigate</text>
  <text x="372" y="206" font-size="13" font-weight="600" fill="#556074" text-anchor="start" class="mono">• accessibility_snapshot</text>
  <text x="372" y="230" font-size="13" font-weight="600" fill="#556074" text-anchor="start" class="mono">• fill / click</text>
  <text x="372" y="254" font-size="13" font-weight="600" fill="#556074" text-anchor="start" class="mono">• take_screenshot</text>
  <rect x="638" y="120" width="274" height="160" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="662" y="154" font-size="16" font-weight="700" fill="#A96C05" text-anchor="start">Navegador Chromium</text>
  <text x="662" y="182" font-size="13" font-weight="400" fill="#161A26" text-anchor="start">Campo: Correo electrónico</text>
  <text x="662" y="206" font-size="13" font-weight="400" fill="#161A26" text-anchor="start">Campo: Contraseña</text>
  <text x="662" y="230" font-size="13" font-weight="700" fill="#4453C9" text-anchor="start">Botón: [ Iniciar sesión ]</text>
  <text x="662" y="254" font-size="12.5" font-weight="600" fill="#0F8478" text-anchor="start">Estado: Interacción verificada</text>
  <path d="M298,185 H342" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#pwFlujo-arrow)"/>
  <path d="M342,215 H298" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#pwFlujo-arrow)"/>
  <path d="M588,185 H632" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#pwFlujo-arrow)"/>
  <path d="M632,215 H588" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#pwFlujo-arrow)"/>
  <rect x="48" y="306" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="332" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">Accesibilidad semántica:</tspan> Playwright MCP entrega a Antigravity la estructura de botones, etiquetas y campos de entrada en texto estructurado, ahorrando miles de tokens frente a procesar capturas de imagen.</text>
</svg>
```

El navegador traduce la pantalla visual a una jerarquía semántica en texto estructurado:

- Sabe qué elementos son campos de texto editables (`textbox`) y cuáles son sus etiquetas (`"Correo electrónico"`, `"Contraseña"`).
- Identifica qué elementos son interactivos (`button "Iniciar sesión"`, `link "¿Olvidaste tu contraseña?"`).
- Reconoce si un elemento está deshabilitado, enfocado o contiene texto de ayuda.

Gracias a este árbol de accesibilidad, Antigravity puede "leer" la interfaz en milisegundos y con precisión matemática, decidiendo exactamente sobre qué campo debe escribir o qué botón debe presionar.

## Las herramientas que gana Antigravity

Al conectar `@playwright/mcp`, Antigravity incorpora herramientas clave para interactuar con la web:

- **`browser_navigate`:** Abre una URL específica en una instancia de Chromium (por ejemplo, el servidor local de Flutter Web).
- **`browser_fill`:** Escribe un texto en un campo determinado, seleccionándolo por su nombre de accesibilidad o su etiqueta.
- **`browser_click`:** Simula el clic del ratón sobre un botón, pestaña o enlace.
- **`browser_snapshot`:** Captura el estado actual del árbol de accesibilidad para que el agente verifique el resultado de una acción.
- **`browser_take_screenshot`:** Toma una captura visual únicamente cuando se requiere una comprobación estética puntual.

## Caso práctico: verificar el flujo de autenticación

Para probar la pantalla de login con Antigravity y Playwright:

1. **Inicias la aplicación en modo web:**
   Ejecutas en la terminal `flutter run -d web-server --web-port 8080`.
2. **Le das la instrucción a Antigravity:**
   ```text
   > Abre http://localhost:8080 con Playwright, entra a la pantalla de login, escribe "domiciano@icesi.edu.co" en el correo y "clave123" en la contraseña, y verifica que los botones y enlaces del formulario sean detectados correctamente.
   ```
3. **Antigravity ejecuta la verificación:**
   Llama a `browser_navigate`, lee el árbol de accesibilidad, invoca `browser_fill` en los campos indicados y te entrega un reporte detallando qué elementos encontró y si hubo algún problema de visualización.

Este ciclo automatizado ahorra minutos valiosos en cada sesión de desarrollo y sienta las bases para probar la aplicación de forma continua a lo largo del semestre. En la siguiente lección integraremos todo en el taller práctico.
