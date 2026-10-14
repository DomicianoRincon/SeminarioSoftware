# Plan · Servidores MCP: conectando al agente con el mundo

**Curso:** Seminario de Ingeniería de Software · Universidad Icesi  
**Sesión:** 5 del bloque de Domiciano, semana 11 · *Servidores MCP (Model Context Protocol)*  
**Duración:** 2 horas en clase  
**Público:** estudiantes de Ingeniería de Sistemas, con `mi_app_1` tal como quedó en la sesión 4 (con `AGENTS.md` y `flutter-pantallas`) y la Entrega 1 en curso.  
**Proyecto de referencia:** `mi_app_1`, la red social profesional del curso.  
**Herramienta de desarrollo:** **Google Antigravity** exclusivamente.  
**Fuente:** las cinco lecciones de la sección *Sesión 5 · Servidores MCP* del visor (`S0034`, `S0035`, `S0036`, `S0037`, `S0039`). El plan sigue su orden y su contenido.

**Estado:** plan redactado siguiendo los lineamientos pedagógicos del curso y el planeador institucional.

## Qué tiene que lograr

1. Que entiendan la diferencia conceptual entre una **Skill** (instrucciones y metodología) y un **Servidor MCP** (herramientas y conexiones externas vivas).
2. Que conozcan la arquitectura de MCP: Host/Cliente (Antigravity), Servidores locales (`stdio`) y remotos (HTTP), y Servicios externos.
3. Que configuren `.agents/mcp_config.json` con los servidores de **Google Stitch**, **Playwright** y **GitHub**.
4. Que comprendan el modelo de permisos y supervisión al invocar herramientas externas.
5. Que experimenten el paso a paso de cada MCP directamente en su lección:
   - **Stitch MCP:** formular prompts de interfaz para veterinaria y consultar tokens con `stitch_get_screen`.
   - **Playwright MCP:** navegar por Chromium y auditar formularios mediante el árbol de accesibilidad.
   - **GitHub MCP:** consultar issues de equipo, reportar hallazgos y abrir Pull Requests automáticos.
6. Que dejen las herramientas configuradas y probadas en su repositorio como evidencia de la Entrega 1.

## Tiempos

| Bloque | Slides | Minutos |
|---|---|---|
| Apertura y contexto | 1 a 3 | 10 |
| De las instrucciones a las herramientas (MCP) | 4 a 9 | 15 |
| Configuración de MCP en Antigravity | 10 a 14 | 15 |
| Google Stitch MCP: Prototipado y práctica | 15 a 21 | 25 |
| Playwright MCP: Verificación web y práctica | 22 a 25 | 20 |
| GitHub MCP: Colaboración y práctica | 26 a 29 | 25 |
| Cierre y Entrega 1 | 30 y 31 | 10 |

Total: 120 minutos (2 horas).

## Cómo se reutilizan las ilustraciones

Siguiendo el estándar de las presentaciones institucionales de Icesi:
- Poco texto en las diapositivas; las explicaciones extensas van en las **notas de orador** (tecla `S`).
- Las figuras vectoriales SVG de las lecciones ocupan el espacio principal.
- El fondo `#FBFBFD` de las lecciones pasa a blanco en las diapositivas con marco institucional.
- Se omiten títulos redundantes dentro de las figuras para evitar duplicación con el título de la slide.

## Slides

| # | Título | Layout | Contenido | Gráfico |
|---|---|---|---|---|
| 1 | Servidores MCP: conectando al agente con el mundo | `titleSlideA` | Subtítulo: *Model Context Protocol, Google Stitch, Playwright y GitHub en Antigravity* | · |
| 2 | El recorrido de hoy | `slideStandard` | Del código local a MCP → Configuración → Stitch → Playwright → GitHub → Cierre | `H.bigPipeline` |
| 3 | Lo que te llevas hoy | `slideStandard` | `.agents/mcp_config.json`, prototipos en Stitch, verificación web con Playwright y sincronización con GitHub | Resumen de entregables |
| 4 | De las instrucciones a las herramientas | `sectionSlideEBlue` | Divisor de bloque | · |
| 5 | El límite de una caja cerrada | `slideStandard` | `AGENTS.md` y Skills dan metodología; no pueden interactuar con servicios web ni navegadores | Texto comparativo |
| 6 | Qué es el Model Context Protocol | `slideStandard` | Un estándar abierto de conexión para agentes de IA | SVG `mcpArquitectura` |
| 7 | Host, Cliente y Servidor | `slideStandard` | Antigravity como host/cliente; servidores locales por `stdio` | Diagrama de cajas |
| 8 | La tríada de Antigravity | `slideStandard` | Reglas fijas (`AGENTS.md`) + Metodología (`Skills`) + Herramientas vivas (`MCP`) | SVG `mcpTriada` |
| 9 | La idea de la sesión | `sectionSlideEGreen` | *Una skill le enseña al agente cómo pensar; un servidor MCP le da manos y ojos para interactuar con sistemas reales.* | · |
| 10 | Configuración de MCP en Antigravity | `sectionSlideEBlue` | Divisor de bloque | · |
| 11 | El archivo .agents/mcp_config.json | `slideStandard` | La clave `mcpServers`: remotos (`serverUrl` y `headers`) y locales (`npx`, `stdio`) | SVG `mcpConfiguracion` |
| 12 | Transporte local y remoto | `slideStandard` | `stdio` para herramientas locales y `Streamable HTTP` para servicios cloud como Stitch | Esquema de procesos |
| 13 | Ciclo de descubrimiento | `slideStandard` | Inicio de sesión → lectura de catálogo de herramientas → inyección en contexto | Diagrama de pasos |
| 14 | Permisos: tú mantienes el control | `slideSidebarLeftOrange` | Lecturas automáticas vs. confirmación explícita para acciones con efectos externos | Panel lateral con íconos |
| 15 | Google Stitch MCP | `sectionSlideEBlue` | Divisor de bloque | · |
| 16 | Google Stitch en la Entrega 1 | `slideStandard` | El lienzo de diseño asistido por IA (`stitch.withgoogle.com`) | Tarjeta de Entrega 1 |
| 17 | Flujo de prototipado con Stitch MCP | `slideStandard` | De los prompts en lenguaje natural a los mockups consultados por Antigravity | SVG `stFlujo` |
| 18 | Prompts para prototipado en Stitch | `slideStandard` | Anatomía de un buen prompt: contexto, jerarquía, inputs y restricciones mobile | Tarjeta con desglose |
| 19 | Caso de uso: Clínica Veterinaria | `slideStandard` | Prompts estructurados para `SigninScreen`, `LoginScreen` y `HomeScreen` | Desglose de 3 pantallas |
| 20 | Consulta e inspección con Stitch MCP | `slideStandard` | Herramientas `stitch_list_projects` y `stitch_get_screen` en acción desde Antigravity | Simulación de consola |
| 21 | Paso a paso: Experimenta con Stitch MCP | `slideSidebarLeftOrange` | Configurar `.agents/mcp_config.json`, generar en Stitch y extraer tokens desde Antigravity | Checklist guiado |
| 22 | Playwright MCP | `sectionSlideEBlue` | Divisor de bloque | · |
| 23 | Ojos y manos en el navegador | `slideStandard` | `@playwright/mcp`: control de Chromium en vivo desde Antigravity | Descripción de herramientas |
| 24 | El árbol de accesibilidad | `slideStandard` | Por qué la semántica en texto estructurado supera a las capturas de imagen | SVG `pwFlujo` |
| 25 | Paso a paso: Experimenta con Playwright MCP | `slideSidebarLeftOrange` | Levantar Flutter web, navegar e interactuar con formularios desde Antigravity | Checklist guiado |
| 26 | GitHub MCP | `sectionSlideEBlue` | Divisor de bloque | · |
| 27 | El software se construye en equipo | `slideStandard` | Conectar Antigravity con los Issues, Pull Requests y ramas del proyecto | SVG `ghFlujo` |
| 28 | Herramientas de GitHub | `slideStandard` | `list_issues`, `create_issue`, `create_pull_request`, `get_file_contents` | Descripción de herramientas |
| 29 | Paso a paso: Experimenta con GitHub MCP | `slideSidebarLeftOrange` | Configurar PAT, consultar requerimientos de sprint y reportar issues | Checklist guiado |
| 30 | Lo que te llevas para la Entrega 1 | `slideStandard` | Prototipo en Stitch, servidores MCP configurados y automatizaciones probadas | Lista de entregables |
| 31 | Para la próxima sesión | `slideSidebarLeftOrange` | Próximo tema: `StatefulWidget` y `setState` (dar vida a los formularios) | Panel lateral con íconos |

**31 slides.** Cada slide de contenido cuenta con sus notas de orador (tecla `S`) correspondientes a las lecciones `S0034` a `S0039`.
