# Automatización con Playwright MCP

<!-- tags: Playwright MCP, @playwright/mcp, automatización con IA, árbol de accesibilidad, pruebas de interfaz, verificar pantalla en navegador, Flutter web, navegador Chromium, flujo de registro e2e -->

```svg
<svg id="pwCapacidades" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 636" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="pwCapacidades-ttl pwCapacidades-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="pwCapacidades-ttl">Lo que puedes hacer con Playwright MCP</title>
  <desc id="pwCapacidades-dsc">Cuatro tarjetas. 1: abrir la app en un navegador Chromium. 2: leer la página como árbol de accesibilidad, con el rol y el nombre de cada elemento. 3: escribir en los campos y hacer clic en los botones. 4: verificar el resultado, revisar la consola y tomar capturas.</desc>
  <defs>
    <style>
      #pwCapacidades .title{fill:#161A26;font-size:22px;font-weight:700}
      #pwCapacidades .sub{fill:#79809A;font-size:13.5px}
      #pwCapacidades .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #pwCapacidades .nt{font-size:15px;font-weight:700;fill:#161A26}
      #pwCapacidades .nb{fill:#454C61;font-size:13px}
      #pwCapacidades .lbl{fill:#556074;font-size:12px;font-weight:600}
      #pwCapacidades .foot{fill:#79809A;font-size:12px}
      #pwCapacidades .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #pwCapacidades .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#pwCapacidades-arrow)}
    </style>
    <marker id="pwCapacidades-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="636" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Lo que puedes hacer con Playwright MCP</text>
  <text class="sub" x="48" y="80" data-fit="860">Antigravity usa un navegador real para probar tu app como lo haría una persona.</text>
  <rect x="48" y="112" width="420" height="200" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><g transform="translate(64,128)"><rect x="0" y="8" width="176" height="152" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><path d="M0,34 H176" stroke="#C4CBD8" stroke-width="1.5"/><circle cx="12" cy="21" r="3.5" fill="#F3A3B2"/><circle cx="23" cy="21" r="3.5" fill="#F0C572"/><circle cx="34" cy="21" r="3.5" fill="#9FD68D"/><rect x="48" y="13" width="120" height="16" rx="8" fill="#EFF1F5"/><text x="56" y="25" font-size="12" font-weight="400" fill="#556074" text-anchor="start" class="mono">localhost:8080</text><rect x="40" y="52" width="96" height="16" rx="5" fill="none" stroke="#C4CBD8"/><rect x="40" y="76" width="96" height="16" rx="5" fill="none" stroke="#C4CBD8"/><rect x="40" y="100" width="96" height="18" rx="5" fill="#4453C9"/><text x="88" y="140" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">Chromium</text></g><circle cx="268" cy="152" r="11" fill="#4453C9"/><text x="268" y="156.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">1</text><text x="288" y="157" font-size="15" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="164">Abrir tu app</text><text x="256" y="192" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">Lanza un navegador real</text><text x="256" y="213" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">y entra a tu app Flutter</text><text x="256" y="234" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">web o a cualquier URL.</text>
  <rect x="492" y="112" width="420" height="200" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><g transform="translate(508,128)"><rect width="176" height="168" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><text x="12" y="24" font-size="12" font-weight="700" fill="#161A26" text-anchor="start" class="mono">- page</text><path d="M16,30 V48 H24" fill="none" stroke="#C4CBD8" stroke-width="1.5"/><text x="28" y="52" font-size="12" font-weight="600" fill="#7439B8" text-anchor="start" class="mono">heading</text><text x="96" y="52" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono">"Patitas"</text><path d="M16,58 V76 H24" fill="none" stroke="#C4CBD8" stroke-width="1.5"/><text x="28" y="80" font-size="12" font-weight="600" fill="#7439B8" text-anchor="start" class="mono">textbox</text><text x="96" y="80" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono">"Correo"</text><path d="M16,86 V104 H24" fill="none" stroke="#C4CBD8" stroke-width="1.5"/><text x="28" y="108" font-size="12" font-weight="600" fill="#7439B8" text-anchor="start" class="mono">textbox</text><text x="96" y="108" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono">"Clave"</text><path d="M16,114 V132 H24" fill="none" stroke="#C4CBD8" stroke-width="1.5"/><text x="28" y="136" font-size="12" font-weight="600" fill="#7439B8" text-anchor="start" class="mono">button</text><text x="96" y="136" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono">"Entrar"</text></g><circle cx="712" cy="152" r="11" fill="#7439B8"/><text x="712" y="156.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">2</text><text x="732" y="157" font-size="15" font-weight="700" fill="#7439B8" text-anchor="start" data-fit="164">Leer la página</text><text x="700" y="192" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">Ve la página como árbol</text><text x="700" y="213" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">de accesibilidad: el rol</text><text x="700" y="234" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">y nombre de cada cosa.</text>
  <rect x="48" y="336" width="420" height="200" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><g transform="translate(64,352)"><rect width="176" height="168" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><rect x="16" y="24" width="144" height="28" rx="6" fill="#FFFFFF" stroke="#0F8478" stroke-width="2"/><text x="26" y="43" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono">ana@mail.com</text><path d="M120,30 V46" stroke="#0F8478" stroke-width="1.5"/><rect x="16" y="64" width="144" height="28" rx="6" fill="none" stroke="#C4CBD8"/><rect x="16" y="104" width="144" height="30" rx="6" fill="#4453C9"/><text x="64" y="124" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">Entrar</text><circle cx="128" cy="119" r="13" fill="none" stroke="#F0C572" stroke-width="2"/><path d="M128,119 l0,24 l6,-6 l5,10 l4,-2 l-5,-10 l8,0 Z" fill="#161A26" stroke="#FFFFFF" stroke-width="1.25" stroke-linejoin="round"/></g><circle cx="268" cy="376" r="11" fill="#0F8478"/><text x="268" y="380.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">3</text><text x="288" y="381" font-size="15" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="164">Escribir y hacer clic</text><text x="256" y="416" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">Rellena campos, pulsa</text><text x="256" y="437" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">botones y navega como</text><text x="256" y="458" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">lo haría un usuario.</text>
  <rect x="492" y="336" width="420" height="200" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><g transform="translate(508,352)"><rect width="176" height="168" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><circle cx="26" cy="34" r="9" fill="#3A8235"/><path d="M22,34 l3,3 l5,-6" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="44" y="39" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start">Abrió /home</text><circle cx="26" cy="70" r="9" fill="#3A8235"/><path d="M22,70 l3,3 l5,-6" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="44" y="75" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start">Ve "Hola, Ana"</text><circle cx="26" cy="106" r="9" fill="#3A8235"/><path d="M22,106 l3,3 l5,-6" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="44" y="111" font-size="12.5" font-weight="600" fill="#161A26" text-anchor="start">0 errores</text><rect x="16" y="128" width="144" height="26" rx="6" fill="#EFF1F5"/><text x="88" y="145" font-size="12" font-weight="600" fill="#556074" text-anchor="middle" class="mono">captura.png</text></g><circle cx="712" cy="376" r="11" fill="#3A8235"/><text x="712" y="380.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">4</text><text x="732" y="381" font-size="15" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="164">Verificar</text><text x="700" y="416" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">Comprueba el resultado,</text><text x="700" y="437" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">revisa la consola y</text><text x="700" y="458" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">toma capturas.</text>
  <rect x="48" y="560" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="586" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">Pruebas sin clics manuales:</tspan> tú das la instrucción en español y Playwright la convierte en acciones reales en el navegador.</text>
</svg>
```

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

## Paso a paso: Configurar y experimentar con Playwright MCP

Sigue estos pasos para configurar Playwright MCP y experimentar cómo Antigravity interactúa de forma autónoma con tu aplicación web:

- **Paso 1: Configurar el servidor en tu proyecto:**
  En `.agents/mcp_config.json`, añade el bloque de Playwright dentro del objeto `mcpServers`:
  ```json
  {
    "mcpServers": {
      "playwright": {
        "command": "npx",
        "args": ["-y", "@playwright/mcp@latest"]
      }
    }
  }
  ```

- **Paso 2: Iniciar la aplicación web en segundo plano:**
  Abre una terminal en tu proyecto y levanta el servidor web de Flutter en un puerto fijo:
  ```bash
  flutter run -d web-server --web-port=8080
  ```
  Espera hasta que la consola indique que el servidor web está sirviendo en `http://localhost:8080`.

- **Paso 3: Experimentar la navegación y lectura de accesibilidad:**
  En tu sesión de Antigravity, pídele al agente que examine la página inicial:
  ```text
  > Conéctate a http://localhost:8080
    mediante Playwright y extrae el árbol
    de accesibilidad de la pantalla activa.
  ```
  Antigravity invocará `browser_navigate` y `browser_snapshot`. Observa cómo devuelve la lista estructurada de botones, campos de texto y encabezados sin haber cargado una sola imagen gráfica.

- **Paso 4: Experimentar la interacción con formularios:**
  Prueba la capacidad del agente para rellenar campos y accionar botones:
  ```text
  > En la pantalla de login, escribe
    "estudiante@icesi.edu.co" en el correo,
    ingresa una contraseña de prueba y
    presiona el botón "Iniciar sesión".
    Verifica si los elementos respondieron.
  ```
  Antigravity ejecutará `browser_fill` sobre los selectores semánticos y simulará el clic con `browser_click`, reportando el resultado de la interacción.

- **Paso 5: Fluir por toda la aplicación de registro paso a paso:**
  Lleva la automatización un paso más allá solicitándole a Antigravity que recorra el flujo completo de registro de la aplicación, transitando de manera autónoma por cada una de sus pantallas y pasos:
  ```text
  > Navega a http://localhost:8080 y completa el flujo integral
    de registro recorriendo todos los pasos de la aplicación:
    1. Desde la pantalla de bienvenida o login, localiza y pulsa
       el botón o enlace para registrarse ("Regístrate aquí" / "Crear cuenta").
    2. Inspecciona el árbol de accesibilidad de la pantalla de registro
       y localiza todos los campos del formulario.
    3. Diligencia los datos requeridos en cada paso: nombre completo,
       teléfono de contacto, correo electrónico y contraseña segura.
    4. Si el asistente de registro incluye pasos adicionales (como datos de
       perfil, mascota o preferencias), avanza secuencialmente completando
       cada sección.
    5. Acepta los términos de servicio y políticas de privacidad activando
       la casilla correspondiente.
    6. Presiona el botón final de confirmación ("Registrarme").
    7. Valida que la navegación concluya con éxito en el tablero principal
       (Home) o pantalla de confirmación, y reporta si hubo errores de validación.
  ```
  Antigravity coordinará de forma encadenada llamadas a `browser_snapshot`, `browser_fill` y `browser_click`. Al terminar, te presentará un resumen detallado de cada paso completado, los selectores identificados y el estado final de la interfaz.

- **Paso 6: Qué descubres con este ejercicio:**
  Playwright MCP dota a tu agente de capacidad sensorial y motora en el navegador. Las comprobaciones de interfaz dejan de ser una tarea manual y repetitiva, permitiéndote auditar la funcionalidad de tus pantallas de manera continua.
