# Taller · Servidores MCP

<!-- tags: taller de MCP, mcp_config.json en mi_app_1, login y registro en Flutter, probar con Playwright MCP, auditar pantallas con IA, Entrega 1, prototipo no funcional, widgets autorizados -->

En este taller vas a conectar Antigravity con **Google Stitch** y **Playwright**, para generar y verificar las pantallas de autenticación (**Login** y **Registro**) de `mi_app_1`. Al terminar, tendrás el prototipo de interfaz listo para la Entrega 1 del curso.

## Antes de empezar

Asegúrate de tener en tu proyecto:

- `mi_app_1` con la estructura de las sesiones 1 a 4.
- `AGENTS.md` en la raíz del proyecto.
- La skill `flutter-pantallas` en `.agents/skills/flutter-pantallas/`.
- Node.js instalado en tu equipo para que `npx` pueda ejecutar los servidores MCP.

## El proyecto al terminar

Al completar los cinco pasos del taller, tu repositorio tendrá esta estructura:

```svg
<svg id="tsCarpetasMcp" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 490" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tsCarpetasMcp-ttl tsCarpetasMcp-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tsCarpetasMcp-ttl">Tu proyecto con servidores MCP y autenticación</title>
  <desc id="tsCarpetasMcp-dsc">El árbol de carpetas de mi_app_1: dentro de .agents se agrega mcp_config.json. Dentro de lib/screens se agregan login_screen.dart y register_screen.dart.</desc>
  <defs>
    <style>
      #tsCarpetasMcp .title{fill:#161A26;font-size:22px;font-weight:700}
      #tsCarpetasMcp .sub{fill:#79809A;font-size:13.5px}
      #tsCarpetasMcp .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tsCarpetasMcp .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tsCarpetasMcp .nb{fill:#454C61;font-size:13px}
      #tsCarpetasMcp .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tsCarpetasMcp .foot{fill:#79809A;font-size:12px}
      #tsCarpetasMcp .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tsCarpetasMcp .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tsCarpetasMcp-arrow)}
    </style>
    <marker id="tsCarpetasMcp-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="490" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Tu proyecto con servidores MCP y autenticación</text>
  <text class="sub" x="48" y="80" data-fit="860">El archivo mcp_config.json conecta las herramientas; lib/screens/ recibe las pantallas de Login y Registro.</text>
  <path d="M64,124 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="98" y="137" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">mi_app_1/</text>
  <path d="M76,142 V157 H94" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M100,149 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="134" y="162" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">.agents/</text>
  <path d="M112,167 V182 H130" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M140,173 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="170" y="187" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">mcp_config.json</text>
  <rect x="470" y="172" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="498" y="187" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M112,167 V207 H130" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M136,199 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="170" y="212" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">skills/</text>
  <g opacity=".55"><path d="M148,217 V232 H166" fill="none" stroke="#C4CBD8" stroke-width="1.5"/><path d="M172,224 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/><text x="206" y="237" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">mer-svg/</text></g>
  <path d="M148,217 V257 H166" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M172,249 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="206" y="262" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">flutter-pantallas/</text>
  <path d="M76,142 V282 H94" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M100,274 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="134" y="287" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">lib/</text>
  <path d="M112,292 V307 H130" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M136,299 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="170" y="312" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">components/</text>
  <path d="M112,292 V332 H130" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M136,324 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="170" y="337" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">screens/</text>
  <path d="M148,342 V357 H166" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M176,348 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="206" y="362" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">messages_screen.dart</text>
  <path d="M148,342 V382 H166" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M176,373 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="206" y="387" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">login_screen.dart</text>
  <rect x="470" y="372" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="498" y="387" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M148,342 V407 H166" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M176,398 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="206" y="412" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">register_screen.dart</text>
  <rect x="470" y="397" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="498" y="412" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M112,292 V432 H130" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M140,423 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="170" y="437" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">main.dart</text>
  <rect x="552" y="150" width="360" height="80" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="570" y="178" font-size="13.5" font-weight="700" fill="#0F8478" text-anchor="start" class="mono">.agents/mcp_config.json</text>
  <text x="570" y="202" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start">Registra Stitch y Playwright para Antigravity.</text>
  <rect x="552" y="250" width="360" height="110" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
  <text x="570" y="278" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">login_screen y register_screen</text>
  <text x="570" y="302" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start">Pantallas generadas a partir del diseño</text>
  <text x="570" y="322" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start">de Stitch y auditadas con Playwright.</text>
  <text x="570" y="342" font-size="12" font-weight="700" fill="#3A8235" text-anchor="start">Insumo directo para la Entrega 1.</text>
  <rect x="48" y="410" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="436" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">Resultado del taller:</tspan> Dos pantallas nuevas listas en tu aplicación, diseñadas desde Stitch y verificadas con Playwright.</text>
</svg>
```

Los servidores MCP viven en `.agents/mcp_config.json` y las pantallas nuevas se incorporan en `lib/screens/`.

## Paso 1 · Crear mcp_config.json

Dentro de la carpeta `.agents/` de tu proyecto `mi_app_1`, crea el archivo `mcp_config.json` con la configuración de los dos servidores:

```json
{
  "mcpServers": {
    "stitch": {
      "command": "npx",
      "args": ["-y", "stitch-mcp"],
      "env": {
        "STITCH_API_KEY": "tu_clave_de_google_stitch_aqui"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

Si vas a realizar la prueba en modo local o sin clave de Stitch, puedes usar el archivo de recursos `SeminarioSoftware/recursos/sesion5/prompt_stitch_auth.md` como insumo directo para el agente.

## Paso 2 · Iniciar Antigravity y verificar las herramientas

Abre Antigravity en la consola dentro de la carpeta de `mi_app_1`:

```bash
cd mi_app_1
agy
```

Antigravity leerá `.agents/mcp_config.json` y levantará los procesos en segundo plano. Puedes comprobar que los servidores están activos preguntándole al agente:

```text
> ¿Qué herramientas tienes disponibles para interactuar con Stitch y con el navegador?
```

El agente te confirmará que cuenta con las herramientas de extracción de diseño de Stitch y los comandos de navegación de Playwright.

## Paso 3 · Generar LoginScreen y RegisterScreen

Con las herramientas activas, pídele a Antigravity que construya las dos pantallas:

```text
> Genera las pantallas LoginScreen en lib/screens/login_screen.dart y RegisterScreen en lib/screens/register_screen.dart para la red profesional. Respeta estrictamente la skill flutter-pantallas: usa solo StatelessWidget, la paleta de widgets.md y componentes reutilizables.
```

Antigravity ejecutará el siguiente procedimiento:

1. Consultará la estructura visual requerida.
2. Cargará la skill `flutter-pantallas` y su paleta `widgets.md`.
3. Escribirá `login_screen.dart` y `register_screen.dart`.
4. Registrará las dos rutas (`/login` y `/register`) en `lib/main.dart`.
5. Ejecutará `flutter analyze` para asegurar que no haya errores de compilación.

## Paso 4 · Verificar en el navegador con Playwright

En una terminal independiente, levanta el servidor web de Flutter:

```bash
flutter run -d web-server --web-port 8080
```

Cuando la aplicación esté corriendo, dile a Antigravity que realice la prueba:

```text
> Abre http://localhost:8080 con Playwright. Navega a la ruta de login, escribe un correo en el campo correspondiente y verifica que los botones y enlaces del formulario sean accesibles y se vean en pantalla.
```

Antigravity abrirá el navegador, procesará el árbol de accesibilidad, simulará la interacción con los campos de entrada y te informará el resultado de la prueba.

## Paso 5 · Auditar el resultado

Antes de hacer commit, audita lo que hizo el agente revisando tres puntos:

- **Sin paquetes no autorizados:** Confirma que el agente no haya agregado dependencias externas en `pubspec.yaml`.
- **Paleta de widgets:** Revisa que los campos sean `TextField` estándar con `InputDecoration`, sin controladores ni estados complejos.
- **Scroll seguro:** Comprueba que ambas pantallas tengan `SingleChildScrollView` dentro del `SafeArea` para evitar errores de desbordamiento en pantallas pequeñas.

## Lo que te llevas para la Entrega 1

Con el trabajo de esta sesión tienes listos los elementos clave de la Entrega 1:

- El modelo de datos documentado en `docs/mer.svg` (de la sesión 4).
- Las pantallas no funcionales en Stitch y su implementación en Flutter (`login_screen.dart`, `register_screen.dart`, `messages_screen.dart`).
- La configuración de herramientas de IA (`AGENTS.md`, skills y `.agents/mcp_config.json`).

En la siguiente sesión entraremos a la **Unidad 4**: aprenderás qué es el estado dinámico en Flutter, cómo funciona `StatefulWidget` y cómo usar `setState` para que estos formularios guarden y procesen datos reales.
