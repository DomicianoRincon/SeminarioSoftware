# El agente en consola

<!-- tags: OpenCode, Antigravity CLI, agente de IA en consola, permisos del agente, opencode.json, /permissions, modelo gratuito, modo plan y modo build, el agente cambió archivos sin preguntar, opencode no se reconoce como comando, /undo, instalar agy -->

Hasta hoy escribiste todo a mano. Desde esta sesión trabajas con un **agente en la consola**: un modelo de IA con herramientas para leer tus archivos, editarlos y ejecutar comandos dentro de tu proyecto.

```svg
<svg id="agAgente" xmlns="http://www.w3.org/2000/svg" viewBox="480 88 456 344" width="100%" style="max-width:560px;display:block;margin:0 auto" role="img" aria-labelledby="agAgente-ttl agAgente-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="agAgente-ttl">Agente en consola</title>
  <desc id="agAgente-dsc">Un modelo de IA conectado a un tool system con cuatro herramientas: leer archivos, buscar en el código, editar archivos y ejecutar comandos. Con ellas actúa directamente sobre tu proyecto.</desc>
  <defs>
    <style>
      #agAgente .title{fill:#161A26;font-size:22px;font-weight:700}
      #agAgente .sub{fill:#79809A;font-size:13.5px}
      #agAgente .h{font-size:13px;font-weight:700;letter-spacing:.08em}
      #agAgente .lbl{fill:#556074;font-size:12px;font-weight:600}
      #agAgente .tool{fill:#7439B8;font-size:12.5px;font-weight:600}
      #agAgente .cap{fill:#454C61;font-size:13.5px}
      #agAgente .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
    </style>
    <marker id="agAgente-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
    <marker id="agAgente-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#79809A"/></marker>
  </defs>
  <rect x="480" y="88" width="456" height="344" rx="16" fill="#FBFBFD"/>
  <rect x="504" y="112" width="408" height="296" rx="16" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="2"/>
  <text class="h" x="528" y="144" fill="#7439B8">AGENTE EN CONSOLA</text>
  <rect x="528" y="209" width="96" height="84" rx="12" fill="#7439B8"/>
  <text x="576" y="243" text-anchor="middle" fill="#FFFFFF" font-size="14" font-weight="700">Modelo</text>
  <text x="576" y="261" text-anchor="middle" fill="#FFFFFF" font-size="14" font-weight="700">de IA</text>
  <path d="M624,251 L652,188" fill="none" stroke="#C9A6EE" stroke-width="1.5"/>
  <rect x="656" y="172" width="140" height="32" rx="16" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tool" x="726" y="188" dy="0.35em" text-anchor="middle" data-fit="150">Leer archivos</text>
  <path d="M796,188 L812,251" fill="none" stroke="#7439B8" stroke-width="1.5" marker-end="url(#agAgente-a)"/>
  <path d="M624,251 L652,230" fill="none" stroke="#C9A6EE" stroke-width="1.5"/>
  <rect x="656" y="214" width="140" height="32" rx="16" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tool" x="726" y="230" dy="0.35em" text-anchor="middle" data-fit="150">Buscar en el código</text>
  <path d="M796,230 L812,251" fill="none" stroke="#7439B8" stroke-width="1.5" marker-end="url(#agAgente-a)"/>
  <path d="M624,251 L652,272" fill="none" stroke="#C9A6EE" stroke-width="1.5"/>
  <rect x="656" y="256" width="140" height="32" rx="16" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tool" x="726" y="272" dy="0.35em" text-anchor="middle" data-fit="150">Editar archivos</text>
  <path d="M796,272 L812,251" fill="none" stroke="#7439B8" stroke-width="1.5" marker-end="url(#agAgente-a)"/>
  <path d="M624,251 L652,314" fill="none" stroke="#C9A6EE" stroke-width="1.5"/>
  <rect x="656" y="298" width="140" height="32" rx="16" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tool" x="726" y="314" dy="0.35em" text-anchor="middle" data-fit="150">Ejecutar comandos</text>
  <path d="M796,314 L812,251" fill="none" stroke="#7439B8" stroke-width="1.5" marker-end="url(#agAgente-a)"/>
  <path d="M820,230 Q820,220 830,220 H846 L854,230 H882 Q892,230 892,240 V272 Q892,282 882,282 H830 Q820,282 820,272 Z" fill="#E3F6F3" stroke="#0F8478" stroke-width="1.75"/>
  <text x="856" y="304" text-anchor="middle" fill="#0F8478" font-size="12.5" font-weight="700">Tu</text>
  <text x="856" y="320" text-anchor="middle" fill="#0F8478" font-size="12.5" font-weight="700">proyecto</text>
  <rect x="652" y="160" width="148" height="182" rx="12" fill="none" stroke="#C9A6EE" stroke-width="1.25" stroke-dasharray="5 4"/>
  <text x="726" y="358" text-anchor="middle" fill="#7439B8" font-size="12" font-weight="700" letter-spacing=".06em">TOOL SYSTEM</text>
  <text class="cap" x="528" y="388" data-fit="370">La IA lee, edita y <tspan font-weight="700">ejecuta en tu proyecto.</tspan></text>
</svg>
```

En el curso puedes usar uno de dos agentes, los dos gratuitos: **OpenCode** o **Antigravity CLI**. Elige uno y sigue su sección. Lo que armes en las lecciones siguientes (el archivo de contexto y las skills) sirve igual en los dos.

Como el agente puede tocar tus archivos y tu terminal, lo primero después de instalarlo es decirle **qué puede hacer sin preguntarte**:

```svg
<svg id="agReglas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 388" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="agReglas-ttl agReglas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="agReglas-ttl">Lo que cada agente hace sin preguntar</title>
  <desc id="agReglas-dsc">Dos tarjetas. OpenCode, tal como viene, edita archivos y ejecuta comandos sin preguntar. Antigravity CLI edita archivos dentro del proyecto sin preguntar, pero pregunta antes de ejecutar un comando. Con las reglas de la lección, los dos preguntan en ambos casos.</desc>
  <defs>
    <style>
      #agReglas .title{fill:#161A26;font-size:22px;font-weight:700}
      #agReglas .sub{fill:#79809A;font-size:13.5px}
      #agReglas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #agReglas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #agReglas .nb{fill:#454C61;font-size:13px}
      #agReglas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #agReglas .foot{fill:#79809A;font-size:12px}
      #agReglas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #agReglas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#agReglas-arrow)}
    </style>
    <marker id="agReglas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="388" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Lo que cada agente hace sin preguntar</text>
  <text class="sub" x="48" y="80" data-fit="860">Así vienen de fábrica. Las reglas de permiso lo cambian: desde que pregunten todo hasta que lo permitan todo.</text>
  <rect x="48" y="112" width="408" height="172" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="72" y="148" font-size="18" font-weight="700" fill="#7439B8" text-anchor="start">OpenCode</text>
  <text x="72" y="190" font-size="14" font-weight="400" fill="#161A26" text-anchor="start" data-fit="210">Editar un archivo</text>
  <rect x="312" y="172" width="120" height="28" rx="14" fill="#FFEBEF" stroke="#C2354F" stroke-width="1.5"/>
  <text x="372" y="190.5" font-size="12.5" font-weight="700" fill="#C2354F" text-anchor="middle">no pregunta</text>
  <text x="72" y="234" font-size="14" font-weight="400" fill="#161A26" text-anchor="start" data-fit="210">Ejecutar un comando</text>
  <rect x="312" y="216" width="120" height="28" rx="14" fill="#FFEBEF" stroke="#C2354F" stroke-width="1.5"/>
  <text x="372" y="234.5" font-size="12.5" font-weight="700" fill="#C2354F" text-anchor="middle">no pregunta</text>
  <rect x="504" y="112" width="408" height="172" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="528" y="148" font-size="18" font-weight="700" fill="#4453C9" text-anchor="start">Antigravity CLI</text>
  <text x="528" y="190" font-size="14" font-weight="400" fill="#161A26" text-anchor="start" data-fit="210">Editar un archivo</text>
  <rect x="768" y="172" width="120" height="28" rx="14" fill="#FFEBEF" stroke="#C2354F" stroke-width="1.5"/>
  <text x="828" y="190.5" font-size="12.5" font-weight="700" fill="#C2354F" text-anchor="middle">no pregunta</text>
  <text x="528" y="234" font-size="14" font-weight="400" fill="#161A26" text-anchor="start" data-fit="210">Ejecutar un comando</text>
  <rect x="768" y="216" width="120" height="28" rx="14" fill="#E8F6E3" stroke="#3A8235" stroke-width="1.5"/>
  <text x="828" y="234.5" font-size="12.5" font-weight="700" fill="#3A8235" text-anchor="middle">pregunta</text>
  <rect x="48" y="308" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="334" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">Tú diriges:</tspan> en el curso, el agente pregunta antes de editar y antes de ejecutar.</text>
</svg>
```

## OpenCode

Es de código abierto y trae modelos gratuitos que no piden cuenta ni tarjeta.

### Instalar

Necesitas **Node.js** instalado (se descarga de `nodejs.org`).

```svg
<svg id="agInstalar" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 460" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="agInstalar-ttl agInstalar-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="agInstalar-ttl">Instalar OpenCode</title>
  <desc id="agInstalar-dsc">En la consola, el comando npm install -g opencode-ai instala OpenCode. Después, el comando de versión de opencode responde con su número.</desc>
  <defs>
    <style>
      #agInstalar .title{fill:#161A26;font-size:22px;font-weight:700}
      #agInstalar .sub{fill:#79809A;font-size:13.5px}
      #agInstalar .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #agInstalar .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #agInstalar .pf{fill:#7F8AA3} #agInstalar .cmd{fill:#FFFFFF;font-weight:600}
      #agInstalar .dim{fill:#8A93A6} #agInstalar .okk{fill:#6BCB77;font-weight:600}
      #agInstalar .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #agInstalar .chipc{fill:#F2C069} #agInstalar .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #agInstalar .ct{fill:#161A26;font-size:14px;font-weight:700}
      #agInstalar .cb{fill:#454C61;font-size:13px}
      #agInstalar .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="460" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Instalar OpenCode</text>
  <text class="sub" x="48" y="80" data-fit="860">Se instala una sola vez y queda disponible en todas tus carpetas.</text>
  <rect x="48" y="112" width="864" height="190" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">npm install -g opencode-ai</tspan></text>
  <text class="tl mono dim" font-size="13" x="72" y="200" data-fit="816">added 1 package in 12s</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">opencode <tspan letter-spacing="2">-</tspan>-version</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816">2.x.x</text>
  <rect class="ring" x="138.2" y="158" width="210.8" height="22" rx="5"/>
  <circle class="chipc" cx="349.0" cy="159" r="8"/>
  <text class="chipt" x="349.0" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="68.0" y="262" width="47.0" height="22" rx="5"/>
  <circle class="chipc" cx="115.0" cy="263" r="8"/>
  <text class="chipt" x="115.0" y="263" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <g transform="translate(48.0,326)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Instalar</text>
    <text class="cb" x="16" y="60" data-fit="392">El <tspan font-weight="700">-g</tspan> lo deja disponible</text>
    <text class="cb" x="16" y="79" data-fit="392">en todo el equipo.</text>
  </g>
  <g transform="translate(488.0,326)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Comprobar</text>
    <text class="cb" x="16" y="60" data-fit="392">Si responde con un número</text>
    <text class="cb" x="16" y="79" data-fit="392">de versión, quedó instalado.</text>
  </g>
</svg>
```

```shell
npm install -g opencode-ai
opencode --version
```

Lo que va antes de `>` es la carpeta en la que estás: no se escribe. En macOS y Linux también se puede instalar con `curl -fsSL https://opencode.ai/install | bash`.

Si la consola responde que `opencode` no se reconoce como comando, ciérrala y ábrela de nuevo.

### Abrirlo en el proyecto

El agente trabaja sobre **la carpeta en la que lo abres**. Primero entras al proyecto y después lo ejecutas.

```shell
cd C:\develop\mi_app_1
opencode
```

En macOS y Linux la primera línea es `cd ~/develop/mi_app_1`.

Ya adentro, escribe `/models` y elige un modelo **gratuito**: los que dicen *Free* en el nombre, o *Big Pickle*. La lista cambia con el tiempo; si uno desaparece, se elige otro.

### Las reglas de permiso

Las reglas van en el archivo `opencode.json`, en la raíz del proyecto, junto a `pubspec.yaml`. Cada permiso puede valer `ask` (pregunta), `allow` (lo hace) o `deny` (nunca lo hace). Después de cambiar el archivo, cierra OpenCode y ábrelo de nuevo.

**Que lo permita todo.** Es como viene OpenCode si no hay archivo. Escrito, se ve así:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": "allow"
}
```

El agente edita y ejecuta sin detenerse. Es rápido, y solo es buena idea en un proyecto de prueba que puedas perder.

**Que pregunte todo.** El `*` significa "cualquier herramienta":

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "*": "ask"
  }
}
```

Con esta regla pregunta hasta para leer un archivo. Sirve para ver, una vez, todo lo que el agente hace por dentro; para trabajar es demasiado lento.

**La del curso.** Leer y buscar, libre. Editar archivos (`edit`) y ejecutar comandos (`bash`), con tu permiso:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "bash": "ask",
    "edit": "ask"
  }
}
```

Así se ve cuando el agente espera tu respuesta:

```svg
<svg id="agPermiso" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 486" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="agPermiso-ttl agPermiso-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="agPermiso-ttl">El agente pide permiso</title>
  <desc id="agPermiso-dsc">Se le pide al agente crear una pantalla de ajustes. Antes de escribir el archivo, el agente muestra qué va a editar y ofrece tres opciones: una vez, siempre o rechazar.</desc>
  <defs>
    <style>
      #agPermiso .title{fill:#161A26;font-size:22px;font-weight:700}
      #agPermiso .sub{fill:#79809A;font-size:13.5px}
      #agPermiso .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #agPermiso .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #agPermiso .pf{fill:#7F8AA3} #agPermiso .cmd{fill:#FFFFFF;font-weight:600}
      #agPermiso .dim{fill:#8A93A6} #agPermiso .okk{fill:#6BCB77;font-weight:600}
      #agPermiso .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #agPermiso .chipc{fill:#F2C069} #agPermiso .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #agPermiso .ct{fill:#161A26;font-size:14px;font-weight:700}
      #agPermiso .cb{fill:#454C61;font-size:13px}
      #agPermiso .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="486" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">El agente pide permiso</text>
  <text class="sub" x="48" y="80" data-fit="860">Con opencode.json en el proyecto, cada edición y cada comando esperan tu respuesta. Simplificado y en español.</text>
  <rect x="48" y="112" width="864" height="216" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\mi_app_1</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816">&gt; Crea una pantalla de ajustes</text>
  <text class="tl mono" font-size="13" x="72" y="226" data-fit="816">→ Read lib/main.dart</text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816">? Permiso para editar lib/screens/settings_screen.dart</text>
  <text class="tl mono" font-size="13" x="72" y="304" data-fit="816">  Una vez    Siempre    Rechazar</text>
  <rect class="ring" x="83.6" y="262" width="413.6" height="22" rx="5"/>
  <circle class="chipc" cx="497.2" cy="263" r="8"/>
  <text class="chipt" x="497.2" y="263" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="83.6" y="288" width="249.8" height="22" rx="5"/>
  <circle class="chipc" cx="333.4" cy="289" r="8"/>
  <text class="chipt" x="333.4" y="289" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <g transform="translate(48.0,352)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Qué va a tocar</text>
    <text class="cb" x="16" y="60" data-fit="392">Lee el nombre del archivo</text>
    <text class="cb" x="16" y="79" data-fit="392">o el comando completo.</text>
  </g>
  <g transform="translate(488.0,352)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Tú decides</text>
    <text class="cb" x="16" y="60" data-fit="392"><tspan font-weight="700">Siempre</tspan> vale para lo que</text>
    <text class="cb" x="16" y="79" data-fit="392">queda de la sesión.</text>
  </g>
</svg>
```

## Antigravity CLI

Es de Google y se usa con tu cuenta de Google. La cuota gratuita es **semanal**: si se agota, el agente se detiene hasta la semana siguiente.

### Instalar

No necesita Node.js.

```svg
<svg id="agAntigravity" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 460" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="agAntigravity-ttl agAntigravity-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="agAntigravity-ttl">Instalar Antigravity CLI</title>
  <desc id="agAntigravity-dsc">En el Símbolo del sistema de Windows, un comando descarga el instalador de Antigravity CLI, lo ejecuta y lo borra. Después, el comando de versión de agy responde con su número.</desc>
  <defs>
    <style>
      #agAntigravity .title{fill:#161A26;font-size:22px;font-weight:700}
      #agAntigravity .sub{fill:#79809A;font-size:13.5px}
      #agAntigravity .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #agAntigravity .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #agAntigravity .pf{fill:#7F8AA3} #agAntigravity .cmd{fill:#FFFFFF;font-weight:600}
      #agAntigravity .dim{fill:#8A93A6} #agAntigravity .okk{fill:#6BCB77;font-weight:600}
      #agAntigravity .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #agAntigravity .chipc{fill:#F2C069} #agAntigravity .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #agAntigravity .ct{fill:#161A26;font-size:14px;font-weight:700}
      #agAntigravity .cb{fill:#454C61;font-size:13px}
      #agAntigravity .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="460" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Instalar Antigravity CLI</text>
  <text class="sub" x="48" y="80" data-fit="860">En Windows se instala desde el Símbolo del sistema (cmd). No necesita Node.js.</text>
  <rect x="48" y="112" width="864" height="190" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Símbolo del sistema · C:\develop</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd</tspan></text>
  <text class="tl mono cmd" font-size="13" x="72" y="200" data-fit="816">         &amp;&amp; install.cmd &amp;&amp; del install.cmd</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816"><tspan class="pf">develop&gt; </tspan><tspan class="cmd">agy <tspan letter-spacing="2">-</tspan>-version</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816">1.x.x</text>
  <rect class="ring" x="138.2" y="158" width="538.4" height="22" rx="5"/>
  <circle class="chipc" cx="676.6" cy="159" r="8"/>
  <text class="chipt" x="676.6" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="68.0" y="262" width="47.0" height="22" rx="5"/>
  <circle class="chipc" cx="115.0" cy="263" r="8"/>
  <text class="chipt" x="115.0" y="263" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <g transform="translate(48.0,326)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Instalar</text>
    <text class="cb" x="16" y="60" data-fit="392">Es una sola línea: descarga el</text>
    <text class="cb" x="16" y="79" data-fit="392">instalador, lo ejecuta y lo borra.</text>
  </g>
  <g transform="translate(488.0,326)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Comprobar</text>
    <text class="cb" x="16" y="60" data-fit="392">Abre una consola nueva</text>
    <text class="cb" x="16" y="79" data-fit="392">antes de probarlo.</text>
  </g>
</svg>
```

En Windows, desde el **Símbolo del sistema** (`cmd`), en una sola línea:

```shell
curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd
agy --version
```

En PowerShell esa línea no funciona: abre el Símbolo del sistema para instalarlo.

En macOS y Linux:

```shell
curl -fsSL https://antigravity.google/cli/install.sh | bash
agy --version
```

Si la consola no reconoce `agy`, ciérrala y ábrela de nuevo.

### Abrirlo en el proyecto

```shell
cd C:\develop\mi_app_1
agy
```

La primera vez abre el navegador para que inicies sesión con tu cuenta de Google. Ya adentro, `/model` deja elegir el modelo.

### Las reglas de permiso

Las reglas se manejan desde adentro, con `/permissions`. Hay tres listas: **allowlist** (lo hace), **asklist** (pregunta) y **denylist** (nunca lo hace). Una regla se escribe `acción(sobre qué)`, y el `*` significa "cualquiera":

- `read_file(*)`: leer cualquier archivo.
- `write_file(*)`: escribir cualquier archivo.
- `command(*)`: ejecutar cualquier comando.

Para agregar una regla:

1. Escribe `/permissions`.
2. Pasa a la lista que quieres con la tecla Tab.
3. Pulsa `A`, escribe la regla y pulsa Enter.
4. Cuando pregunte dónde guardarla, elige **Project**: así aplica solo a este proyecto.

Para quitar una, se resalta y se pulsa `D`. Si una acción está en dos listas, gana la más estricta: una regla en la *asklist* le gana a la misma regla en la *allowlist*.

**Que lo permita todo.** Las tres reglas en la **allowlist**, y ninguna en la *asklist*. El agente lee, edita y ejecuta sin detenerse. Solo es buena idea en un proyecto de prueba que puedas perder.

**Que pregunte todo.** Las tres reglas en la **asklist**. Pregunta hasta para leer un archivo: sirve para ver, una vez, todo lo que el agente hace por dentro.

**La del curso.** `write_file(*)` y `command(*)` en la **asklist**. Leer queda libre; editar y ejecutar, con tu permiso. Tal como viene, Antigravity CLI ya pregunta antes de ejecutar un comando, pero edita los archivos del proyecto sin preguntar.

Las mismas reglas se pueden escribir en el archivo de configuración de Antigravity CLI (`.gemini/antigravity-cli/settings.json`, en la carpeta de tu usuario), donde aplican a todos tus proyectos. Que lo permita todo:

```json
{
  "permissions": {
    "allow": ["read_file(*)", "write_file(*)", "command(*)"],
    "ask": [],
    "deny": []
  }
}
```

Que pregunte todo:

```json
{
  "permissions": {
    "allow": [],
    "ask": ["read_file(*)", "write_file(*)", "command(*)"],
    "deny": []
  }
}
```

## Los datos que no van en el agente

Los modelos gratuitos pueden usar lo que escribes para entrenarse. **No pegues contraseñas, claves ni datos personales** en ninguno de los dos.

## La primera pregunta

Empieza por algo que no cambie nada: pídele que te explique lo que hay.

```svg
<svg id="agSesion" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 564" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="agSesion-ttl agSesion-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="agSesion-ttl">La primera pregunta</title>
  <desc id="agSesion-dsc">Dentro de la carpeta del proyecto se ejecuta opencode. Se le pide que explique el proyecto; el agente busca y lee archivos de lib y responde con un resumen.</desc>
  <defs>
    <style>
      #agSesion .title{fill:#161A26;font-size:22px;font-weight:700}
      #agSesion .sub{fill:#79809A;font-size:13.5px}
      #agSesion .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #agSesion .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #agSesion .pf{fill:#7F8AA3} #agSesion .cmd{fill:#FFFFFF;font-weight:600}
      #agSesion .dim{fill:#8A93A6} #agSesion .okk{fill:#6BCB77;font-weight:600}
      #agSesion .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #agSesion .chipc{fill:#F2C069} #agSesion .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #agSesion .ct{fill:#161A26;font-size:14px;font-weight:700}
      #agSesion .cb{fill:#454C61;font-size:13px}
      #agSesion .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="564" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La primera pregunta</text>
  <text class="sub" x="48" y="80" data-fit="860">Una sesión de OpenCode, simplificada. El agente se abre dentro de la carpeta del proyecto.</text>
  <rect x="48" y="112" width="864" height="294" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\mi_app_1</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">mi_app_1&gt; </tspan><tspan class="cmd">opencode</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="226" data-fit="816">&gt; Explícame este proyecto</text>
  <text class="tl mono dim" font-size="13" x="72" y="278" data-fit="816">✱ Glob "lib/**"</text>
  <text class="tl mono" font-size="13" x="72" y="304" data-fit="816">→ Read lib/main.dart</text>
  <text class="tl mono" font-size="13" x="72" y="330" data-fit="816">→ Read lib/screens/profile_screen.dart</text>
  <text class="tl mono okk" font-size="13" x="72" y="382" data-fit="816">Es una app Flutter con una pantalla, ProfileScreen, y siete componentes.</text>
  <rect class="ring" x="68.0" y="210" width="210.8" height="22" rx="5"/>
  <circle class="chipc" cx="278.8" cy="211" r="8"/>
  <text class="chipt" x="278.8" y="211" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="68.0" y="288" width="171.8" height="22" rx="5"/>
  <circle class="chipc" cx="239.8" cy="289" r="8"/>
  <text class="chipt" x="239.8" y="289" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <rect class="ring" x="68.0" y="366" width="569.6" height="22" rx="5"/>
  <circle class="chipc" cx="637.6" cy="367" r="8"/>
  <text class="chipt" x="637.6" y="367" dy="0.35em" text-anchor="middle" font-size="10.5">3</text>
  <g transform="translate(48.0,430)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">Tú preguntas</text>
    <text class="cb" x="16" y="60" data-fit="245">En lenguaje natural,</text>
    <text class="cb" x="16" y="79" data-fit="245">como en un chat.</text>
  </g>
  <g transform="translate(341.3,430)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">El agente lee</text>
    <text class="cb" x="16" y="60" data-fit="245">Cada archivo que abre</text>
    <text class="cb" x="16" y="79" data-fit="245">queda a la vista.</text>
  </g>
  <g transform="translate(634.7,430)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">3</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">Responde</text>
    <text class="cb" x="16" y="60" data-fit="245">Con lo que encontró.</text>
    <text class="cb" x="16" y="79" data-fit="245">No cambió nada.</text>
  </g>
</svg>
```

La figura es de OpenCode; en Antigravity CLI se ve parecido. Cada línea con una flecha es una **herramienta** que el agente usó: leer un archivo, buscar archivos por nombre, escribir o ejecutar un comando. Leer esas líneas es la forma de saber qué hizo.

Prueba también con una pregunta más concreta:

- *¿Qué componentes hay en `lib/components` y qué recibe cada uno?*
- *¿Qué pantallas están registradas en las rutas?*

## Planear antes de hacer

```svg
<svg id="agModos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 404" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="agModos-ttl agModos-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="agModos-ttl">Dos modos: plan y build</title>
  <desc id="agModos-dsc">Dos tarjetas. Plan: el agente lee los archivos y propone qué haría, y pide permiso para editar o ejecutar. Build: crea y edita archivos y ejecuta comandos. En OpenCode se cambia de modo con la tecla Tab y en Antigravity CLI con Shift más Tab.</desc>
  <defs>
    <style>
      #agModos .title{fill:#161A26;font-size:22px;font-weight:700}
      #agModos .sub{fill:#79809A;font-size:13.5px}
      #agModos .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #agModos .nt{font-size:15px;font-weight:700;fill:#161A26}
      #agModos .nb{fill:#454C61;font-size:13px}
      #agModos .lbl{fill:#556074;font-size:12px;font-weight:600}
      #agModos .foot{fill:#79809A;font-size:12px}
      #agModos .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #agModos .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#agModos-arrow)}
    </style>
    <marker id="agModos-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="404" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Dos modos: <tspan class="mono">plan</tspan> y <tspan class="mono">build</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">El agente arranca en build. Una tecla lo pasa a plan y lo devuelve. Mira siempre en cuál estás.</text>
  <rect x="48" y="112" width="408" height="208" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="72" y="148" font-size="20" font-weight="700" fill="#0F8478" text-anchor="start" class="mono">plan</text>
  <text x="72" y="172" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="360">Lee y propone.</text>
  <circle cx="78" cy="204" r="3.5" fill="#0F8478"/>
  <text x="94" y="208" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="340">Lee tus archivos.</text>
  <circle cx="78" cy="232" r="3.5" fill="#0F8478"/>
  <text x="94" y="236" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="340">Te dice qué haría y en qué orden.</text>
  <circle cx="78" cy="260" r="3.5" fill="#0F8478"/>
  <text x="94" y="264" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="340">Para editar o ejecutar, pide permiso.</text>
  <text x="72" y="300" font-size="13" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="360">Antes de un cambio grande.</text>
  <rect x="504" y="112" width="408" height="208" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="528" y="148" font-size="20" font-weight="700" fill="#7439B8" text-anchor="start" class="mono">build</text>
  <text x="528" y="172" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="360">Hace los cambios.</text>
  <circle cx="534" cy="204" r="3.5" fill="#7439B8"/>
  <text x="550" y="208" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="340">Crea y edita archivos.</text>
  <circle cx="534" cy="232" r="3.5" fill="#7439B8"/>
  <text x="550" y="236" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="340">Ejecuta comandos.</text>
  <circle cx="534" cy="260" r="3.5" fill="#7439B8"/>
  <text x="550" y="264" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="340">Es el modo en que arranca.</text>
  <text x="528" y="300" font-size="13" font-weight="700" fill="#7439B8" text-anchor="start" data-fit="360">Cuando ya sabes qué quieres.</text>
  <rect x="48" y="344" width="64" height="32" rx="8" fill="#FFFFFF" stroke="#556074" stroke-width="1.75"/>
  <text x="80.0" y="365" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="middle" class="mono">Tab</text>
  <text x="126" y="365" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="220">en OpenCode</text>
  <rect x="504" y="344" width="120" height="32" rx="8" fill="#FFFFFF" stroke="#556074" stroke-width="1.75"/>
  <text x="564.0" y="365" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="middle" class="mono">Shift + Tab</text>
  <text x="638" y="365" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="220">en Antigravity CLI</text>
</svg>
```

En `plan` el agente te cuenta qué haría antes de hacerlo. Úsalo cuando el cambio toque varios archivos: lees el plan, lo corriges y solo entonces lo dejas hacer.

Se cambia de modo sin salir del agente: en OpenCode con la tecla `Tab` y en Antigravity CLI con `Shift + Tab`.

## Deshacer

Si el agente hizo algo que no querías, escribe `/undo`. En OpenCode revierte los cambios de su última respuesta y te devuelve tu mensaje para que lo corrijas. En Antigravity CLI devuelve la conversación a un punto anterior.

Antes de aceptar un permiso, lee qué archivo o qué comando es. Si no entiendes para qué lo necesita, recházalo y pregúntale.
