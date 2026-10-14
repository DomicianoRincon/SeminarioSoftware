# Plan · Servidores MCP: conectando al agente con el mundo

**Curso:** Seminario de Ingeniería de Software · Universidad Icesi  
**Sesión:** 5 del bloque de Domiciano, semana 11 · *Servidores MCP (Model Context Protocol)*  
**Duración:** 2 horas en clase  
**Público:** estudiantes de Ingeniería de Sistemas, con `mi_app_1` tal como quedó en la sesión 4 (con `AGENTS.md` y `flutter-pantallas`) y la Entrega 1 en curso.  
**Proyecto de referencia:** `mi_app_1`, la red social profesional del curso.  
**Herramienta de desarrollo:** **Google Antigravity** exclusivamente.  
**Fuente:** las seis lecciones de la sección *Sesión 5 · Servidores MCP* del visor (`S0034`, `S0035`, `S0036`, `S0037`, `S0039`, `S0038`). El plan sigue su orden y su contenido.

**Estado:** plan redactado siguiendo los lineamientos pedagógicos del curso y el planeador institucional.

## Qué tiene que lograr

1. Que entiendan la diferencia conceptual entre una **Skill** (instrucciones y metodología) y un **Servidor MCP** (herramientas y conexiones externas vivas).
2. Que conozcan la arquitectura de MCP: Host/Cliente (Antigravity), Servidor local (proceso `stdio`) y Servicios externos.
3. Que configuren `.agents/mcp_config.json` con los servidores de **Google Stitch**, **Playwright** y **GitHub**.
4. Que comprendan el modelo de permisos y supervisión al invocar herramientas externas.
5. Que usen Stitch MCP para extraer el diseño de autenticación y generen `LoginScreen` y `RegisterScreen` en Flutter bajo las reglas de `flutter-pantallas`.
6. Que usen Playwright MCP para que Antigravity navegue en Chromium, lea el árbol de accesibilidad y verifique los campos del formulario.
7. Que usen GitHub MCP para consultar issues del equipo, documentar hallazgos y abrir Pull Requests.
8. Que dejen las pantallas y la configuración integradas en su repositorio como evidencia de la Entrega 1.

## Tiempos

| Bloque | Slides | Minutos |
|---|---|---|
| Apertura y contexto | 1 a 3 | 10 |
| De las instrucciones a las herramientas (MCP) | 4 a 9 | 15 |
| Configuración de MCP en Antigravity | 10 a 14 | 15 |
| Google Stitch MCP: Login y Registro | 15 a 20 | 25 |
| Playwright MCP: Verificación en navegador | 21 a 24 | 15 |
| GitHub MCP: Colaboración y repositorios | 25 a 28 | 15 |
| Taller práctico en clase | 29 a 32 | 15 |
| Cierre y Entrega 1 | 33 y 34 | 10 |

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
| 1 | Servidores MCP: conectando al agente con el mundo | `titleSlideA` | Subtítulo: *Model Context Protocol, Google Stitch y Playwright en Antigravity* | · |
| 2 | El recorrido de hoy | `slideStandard` | Del código local a MCP → Configuración → Stitch (Diseño) → Playwright (Pruebas) → Taller | `H.bigPipeline` |
| 3 | Lo que te llevas hoy | `slideStandard` | `.agents/mcp_config.json`, pantallas de Login/Registro y verificación web automatizada | SVG `tsCarpetasMcp` |
| 4 | De las instrucciones a las herramientas | `sectionSlideEBlue` | Divisor de bloque | · |
| 5 | El límite de una caja cerrada | `slideStandard` | `AGENTS.md` y Skills dan metodología; no pueden interactuar con servicios web ni navegadores | Texto comparativo |
| 6 | Qué es el Model Context Protocol | `slideStandard` | Un estándar abierto de conexión para agentes de IA | SVG `mcpArquitectura` |
| 7 | Host, Cliente y Servidor | `slideStandard` | Antigravity como host/cliente; servidores locales por `stdio` | Diagrama de cajas |
| 8 | La tríada de Antigravity | `slideStandard` | Reglas fijas (`AGENTS.md`) + Metodología (`Skills`) + Herramientas vivas (`MCP`) | SVG `mcpTriada` |
| 9 | La idea de la sesión | `sectionSlideEGreen` | *Una skill le enseña al agente cómo pensar; un servidor MCP le da manos y ojos para interactuar con sistemas reales.* | · |
| 10 | Configuración de MCP en Antigravity | `sectionSlideEBlue` | Divisor de bloque | · |
| 11 | El archivo .agents/mcp_config.json | `slideStandard` | La clave `mcpServers`, comando `npx`, argumentos y variables de entorno | SVG `mcpConfiguracion` |
| 12 | Transporte local con stdio | `slideStandard` | Procesos hijos en segundo plano sin exponer puertos de red | Esquema de procesos |
| 13 | Ciclo de descubrimiento | `slideStandard` | Inicio de sesión → lectura de catálogo de herramientas → inyección en contexto | Diagrama de pasos |
| 14 | Permisos: tú mantienes el control | `slideSidebarLeftOrange` | Lecturas automáticas vs. confirmación explícita para acciones con efectos externos | Panel lateral con íconos |
| 15 | Google Stitch MCP | `sectionSlideEBlue` | Divisor de bloque | · |
| 16 | Google Stitch en la Entrega 1 | `slideStandard` | El lienzo de diseño asistido por IA (`stitch.withgoogle.com`) | Tarjeta de Entrega 1 |
| 17 | Flujo de prototipado con Stitch MCP | `slideStandard` | De los prompts en lenguaje natural a los mockups consultados por Antigravity | SVG `stFlujo` |
| 18 | Prompts para prototipado en Stitch | `slideStandard` | Anatomía de un buen prompt: contexto, jerarquía, inputs y restricciones mobile | Tarjeta con desglose |
| 19 | Caso de uso: Clínica Veterinaria | `slideStandard` | Prompts estructurados para `SigninScreen`, `LoginScreen` y `HomeScreen` | Desglose de 3 pantallas |
| 20 | Consulta e inspección con Stitch MCP | `slideStandard` | Herramientas `stitch_list_projects` y `stitch_get_screen` en acción desde Antigravity | Simulación de consola |
| 21 | Prototipado sin fricción | `slideSidebarLeftOrange` | Validación de tokens, contraste y componentes visuales para la Entrega 1 | Panel lateral con íconos |
| 22 | Playwright MCP | `sectionSlideEBlue` | Divisor de bloque | · |
| 23 | Ojos y manos en el navegador | `slideStandard` | `@playwright/mcp`: control de Chromium en vivo desde Antigravity | Descripción de herramientas |
| 24 | El árbol de accesibilidad | `slideStandard` | Por qué la semántica en texto estructurado supera a las capturas de imagen | SVG `pwFlujo` |
| 25 | GitHub MCP | `sectionSlideEBlue` | Divisor de bloque | · |
| 26 | El software se construye en equipo | `slideStandard` | Conectar Antigravity con los Issues, Pull Requests y ramas del proyecto | SVG `ghFlujo` |
| 27 | Herramientas de GitHub | `slideStandard` | `list_issues`, `create_issue`, `create_pull_request`, `get_file_contents` | Descripción de herramientas |
| 28 | Cero fricción en el equipo | `sectionSlideEGreen` | *Antigravity lee el issue del sprint, programa la pantalla y abre el Pull Request automáticamente.* | · |
| 29 | Manos a la obra | `titleSlideF` | Separador: *Taller · Servidores MCP en tu proyecto* | · |
| 30 | Paso 1 y 2: Configurar y verificar | `slideStandard` | Crear `.agents/mcp_config.json` con Stitch, Playwright y GitHub | Pasos guiados |
| 31 | Paso 3: Generar Login y Registro | `slideStandard` | Pedir las pantallas respetando la paleta de widgets | Bloque de instrucciones |
| 32 | Paso 4 y 5: Probar y auditar | `slideStandard` | Levantar Flutter web, ejecutar verificación con Playwright y auditar código | Checklist de auditoría |
| 33 | Lo que te llevas para la Entrega 1 | `slideStandard` | `mer.svg`, prototipo en Stitch, pantallas en Flutter y herramientas configuradas | Lista de entregables |
| 34 | Para la próxima sesión | `slideSidebarLeftOrange` | Próximo tema: `StatefulWidget` y `setState` (dar vida a los formularios) | Panel lateral con íconos |

**34 slides.** Cada slide de contenido cuenta con sus notas de orador (tecla `S`) correspondientes a las lecciones `S0034` a `S0039`.
