# Prototipado con Stitch MCP

<!-- tags: Stitch MCP, Google Stitch, prototipado visual, prompts de interfaz, mockup veterinaria, mobile UI prompt, Antigravity Stitch, diseño de interfaces -->

En la Entrega 1 del curso debes presentar el prototipo de interfaz para tu aplicación móvil. Tradicionalmente, prototipar requiere dominar herramientas complejas de dibujo vectorial y transcribir a mano cada medida, color y elemento gráfico. Con **Google Stitch** y su integración a través del protocolo **MCP en Antigravity**, el prototipado visual se convierte en un proceso guiado por **prompts estructurados en lenguaje natural**.

En esta lección exploramos cómo formular prompts efectivos para generar pantallas móviles de alta fidelidad, tomando como caso práctico el diseño de tres pantallas clave para una **Clínica Veterinaria**: inicio de sesión (`LoginScreen`), registro de nuevo propietario (`SigninScreen`) y el tablero de control de la mascota (`HomeScreen`).

## Qué es Google Stitch y por qué prototipar con prompts

**Google Stitch** (`stitch.withgoogle.com`) es un entorno experimental de diseño de interfaces desarrollado por Google Labs. Permite conceptualizar, iterar y refinar pantallas completas a partir de instrucciones descriptivas en lenguaje natural.

A diferencia de un generador genérico de imágenes, Stitch genera **árboles de componentes interactivos con semántica de interfaz de usuario**: reconoce botones, campos de entrada, barras de navegación, tipografías y paletas de color con tokens formales.

Al integrar Stitch con Antigravity mediante un servidor MCP:
- **No necesitas dibujar píxel por píxel:** describes la intención funcional y estética en un prompt estructurado.
- **El diseño es inspeccionable:** Antigravity puede leer directamente la estructura jerárquica de la pantalla en Stitch a través de llamadas MCP.
- **Coherencia visual garantizada:** puedes reutilizar tokens cromáticos y componentes entre pantallas del mismo flujo.

## Anatomía de un prompt de interfaz para Stitch

Un prompt vago como *"hazme una pantalla de veterinaria"* produce resultados impredecibles. Para obtener prototipos nítidos y coherentes para una aplicación móvil, cada prompt debe especificar cuatro dimensiones fundamentales:

- **1. Contexto, identidad y atmósfera:**
  Indica el nombre de la marca, el público objetivo y la paleta cromática dominante. En entornos clínicos o de salud animal, los tonos cálidos, blancos suaves (#FDFCFB) y verdes esmeralda (#0F8478) transmiten confianza, higiene y cercanía.

- **2. Jerarquía visual y organización espacial:**
  Define el orden vertical de lectura de la pantalla móvil: cabecera con identidad, contenido principal en tarjetas o formularios, y elementos anclados como barras de acciones o navegación inferior.

- **3. Campos de entrada y micro-componentes:**
  Especifica el tipo de cada campo (correo, contraseña, selector de fecha), su icono distintivo a la izquierda y el texto de ayuda o placeholder. Menciona botones primarios de ancho completo y botones secundarios contorneados.

- **4. Restricciones móviles y accesibilidad:**
  Asegura áreas táctiles amplias (mínimo 48 píxeles de alto), textos con alto contraste sobre el fondo y agrupación lógica para no saturar al usuario en pantallas pequeñas.

## El flujo de prototipado con Stitch MCP

El prototipado asistido por IA conecta la redacción del diseño en Stitch con la capacidad de análisis de Antigravity:

```svg
<svg id="stFlujo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 440" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="stFlujo-ttl stFlujo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="stFlujo-ttl">Flujo de prototipado de UI con Stitch MCP</title>
  <desc id="stFlujo-dsc">Cuatro pasos enlazados. 1: Prompts estructurados en Stitch (Clínica Veterinaria). 2: Stitch MCP extrae jerarquía y tokens. 3: Antigravity inspecciona pantallas y elementos. 4: Mockups validados listos para SigninScreen, LoginScreen y HomeScreen.</desc>
  <defs>
    <style>
      #stFlujo .title{fill:#161A26;font-size:22px;font-weight:700}
      #stFlujo .sub{fill:#79809A;font-size:13.5px}
      #stFlujo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #stFlujo .nt{font-size:15px;font-weight:700;fill:#161A26}
      #stFlujo .nb{fill:#454C61;font-size:13px}
      #stFlujo .lbl{fill:#556074;font-size:12px;font-weight:600}
      #stFlujo .foot{fill:#79809A;font-size:12px}
      #stFlujo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #stFlujo .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#stFlujo-arrow)}
    </style>
    <marker id="stFlujo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="440" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Flujo de prototipado de UI con Stitch MCP</text>
  <text class="sub" x="48" y="80" data-fit="860">De los prompts en lenguaje natural a los mockups consultados por Antigravity.</text>
  <rect x="48" y="120" width="196" height="170" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <circle cx="72" cy="146" r="11" fill="#A96C05"/><text x="72" y="150.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">1</text>
  <text x="96" y="151" font-size="14" font-weight="700" fill="#A96C05" text-anchor="start">Lienzo Stitch</text>
  <text x="64" y="184" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Prompts UI</text>
  <text x="64" y="206" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Veterinaria Patitas</text>
  <text x="64" y="226" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Signin, Login y Home</text>
  <text x="64" y="250" font-size="11.5" font-weight="600" fill="#A96C05" text-anchor="start" class="mono">stitch.withgoogle</text>
  <rect x="270" y="120" width="196" height="170" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <circle cx="294" cy="146" r="11" fill="#7439B8"/><text x="294" y="150.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">2</text>
  <text x="318" y="151" font-size="14" font-weight="700" fill="#7439B8" text-anchor="start">Stitch MCP</text>
  <text x="286" y="184" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Extracción</text>
  <text x="286" y="206" font-size="12" font-weight="600" fill="#7439B8" text-anchor="start" class="mono">stitch_get_screen</text>
  <text x="286" y="226" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Lee campos, botones,</text>
  <text x="286" y="246" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">colores y jerarquía.</text>
  <rect x="492" y="120" width="196" height="170" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <circle cx="516" cy="146" r="11" fill="#4453C9"/><text x="516" y="150.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">3</text>
  <text x="540" y="151" font-size="14" font-weight="700" fill="#4453C9" text-anchor="start">Antigravity</text>
  <text x="508" y="184" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Auditoría Visual</text>
  <text x="508" y="206" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Verifica accesibilidad,</text>
  <text x="508" y="226" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">contraste de colores y</text>
  <text x="508" y="246" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">distribución mobile.</text>
  <rect x="714" y="120" width="198" height="170" rx="12" fill="#E8F6E3" stroke="#3A8235" stroke-width="2.5"/>
  <circle cx="738" cy="146" r="11" fill="#3A8235"/><text x="738" y="150.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">4</text>
  <text x="762" y="151" font-size="14" font-weight="700" fill="#3A8235" text-anchor="start">Mockups Listos</text>
  <text x="730" y="184" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Clínica Veterinaria</text>
  <text x="730" y="206" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">3 pantallas listas:</text>
  <text x="730" y="226" font-size="12.5" font-weight="600" fill="#556074" text-anchor="start">Signin, Login y Home</text>
  <text x="730" y="246" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Base para Entrega 1.</text>
  <path d="M244,205 H264" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#stFlujo-arrow)"/>
  <path d="M466,205 H486" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#stFlujo-arrow)"/>
  <path d="M688,205 H708" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#stFlujo-arrow)"/>
  <rect x="48" y="316" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="342" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">El agente inspecciona el diseño en vivo:</tspan> a través de Stitch MCP, Antigravity lee directamente los elementos visuales sin necesidad de exportar capturas ni medidas manuales.</text>
</svg>
```

El flujo comprende cuatro fases coordinadas:

1. **Prompts estructurados en Stitch:** Redactas el prompt con la identidad visual, los campos requeridos y las acciones clave directamente en el lienzo de Stitch.
2. **Extracción mediante Stitch MCP:** Antigravity se comunica con el servidor MCP de Stitch invocando herramientas como `stitch_get_screen` para obtener la jerarquía de nodos visuales, colores y tipografías.
3. **Auditoría e inspección en Antigravity:** El agente examina la distribución espacial, los contrastes de accesibilidad y la consistencia entre pantallas sin que tengas que exportar archivos ni capturas de pantalla manualmente.
4. **Mockups consolidados:** Las tres pantallas quedan validadas y alineadas con los requisitos de la aplicación, listas para la presentación de la Entrega 1.

## Prompt 1: Pantalla de Inicio de Sesión (`LoginScreen`)

El inicio de sesión de la clínica veterinaria "Patitas & Co." debe permitir a los tutores ingresar de forma rápida a la ficha de sus mascotas, ofreciendo accesos alternativos y recuperación de contraseña.

Copia este prompt para generar la pantalla en Stitch:

```text
Diseña una pantalla móvil moderna y acogedora de inicio de sesión para una app de clínica veterinaria llamada "Patitas & Co.".
- Contexto y atmósfera: Estilo cálido, profesional y amigable para dueños de mascotas. Fondo limpio en blanco cálido (#FDFCFB).
- Cabecera:
  * Icono o ilustración minimalista de una huella de perro/gato estilizada en tono esmeralda (#0F8478).
  * Título tipográfico claro: "Patitas & Co.".
  * Subtítulo cálido: "Cuidamos a quienes más quieres. Ingresa a tu cuenta para gestionar citas y salud de tu mascota".
- Campos del formulario:
  * Campo de texto para Correo Electrónico: icono de correo a la izquierda, borde redondeado suave, placeholder "propietario@ejemplo.com".
  * Campo de texto para Contraseña: icono de candado a la izquierda, icono de ojo a la derecha para ver/ocultar contraseña, placeholder "••••••••".
- Fila de opciones:
  * Casilla de verificación "Recordar sesión".
  * Enlace tipográfico a la derecha: "¿Olvidaste tu contraseña?".
- Acciones:
  * Botón principal de ancho completo en color verde esmeralda (#0F8478) con esquinas redondeadas y texto en blanco en negrita: "Iniciar Sesión".
  * Divisor sutil con texto central: "o continúa con".
  * Botón secundario contorneado (outline) con icono de Google: "Ingresar con Google".
- Pie de pantalla:
  * Texto sutil: "¿Aún no tienes cuenta? Regístrate aquí" (con "Regístrate aquí" resaltado en color esmeralda y negrita).
```

Puntos clave de este diseño:
- El fondo blanco cálido evita la fatiga visual frente al blanco puro clínico.
- Los campos incluyen iconos semánticos que guían al usuario antes de empezar a escribir.
- La jerarquía de acciones prioriza el botón esmeralda principal sobre el acceso social secundario.

## Prompt 2: Pantalla de Registro (`SigninScreen`)

Cuando un tutor llega por primera vez a la clínica, el formulario de registro debe capturar la información de contacto esencial y los datos de emergencia, vinculando de inmediato al animal de compañía.

Copia este prompt para generar la pantalla en Stitch:

```text
Diseña una pantalla móvil limpia y organizada de registro (Sign In / Register) para la app de la clínica veterinaria "Patitas & Co.".
- Contexto y navegación:
  * Barra superior con botón circular de regreso hacia la izquierda.
  * Título grande: "Crear Cuenta".
  * Subtítulo: "Únete a la familia Patitas y lleva el control médico de tus consentidos".
- Campos del formulario (agrupados con espaciado vertical cómodo):
  * Campo "Nombre completo del tutor": icono de usuario, placeholder "Ej. Mariana Pérez".
  * Campo "Teléfono de contacto / Emergencias": icono de teléfono, selector de prefijo de país, placeholder "300 123 4567".
  * Campo "Correo electrónico": icono de email, placeholder "mariana@correo.com".
  * Campo "Contraseña segura": indicador sutil de fortaleza de contraseña con barra de progreso verde/amarilla.
  * Campo "Nombre de tu primera mascota" (opcional para personalizar el onboarding): icono de huellita, placeholder "Ej. Milo, Luna, Rocky...".
- Términos y privacidad:
  * Casilla marcada para aceptar "Términos del Servicio y Política de Tratamiento de Datos Veterinarios".
- Acción principal:
  * Botón prominente de ancho completo en verde esmeralda (#0F8478) con esquinas redondeadas: "Registrarme".
- Pie de página:
  * Enlace inferior: "¿Ya tienes cuenta registrada? Inicia sesión".
```

Puntos clave de este diseño:
- Incluye el teléfono de emergencias, un campo crítico en el dominio veterinario que no suele estar en aplicaciones genéricas.
- El campo opcional de la primera mascota humaniza el proceso de bienvenida y prepara el contenido del Home.
- La barra de navegación superior permite abortar el flujo y regresar sin frustración.

## Prompt 3: Tablero Principal (`HomeScreen`)

Una vez autenticado el tutor, la pantalla principal debe actuar como el centro de mando para la salud preventiva del animal: mostrar qué mascota está activa, alertar sobre la próxima cita agendada, ofrecer accesos directos a servicios comunes y facilitar el contacto con urgencias médicas 24 horas.

Copia este prompt para generar la pantalla en Stitch:

```text
Diseña el dashboard o pantalla principal móvil (Home) para la app de la clínica veterinaria "Patitas & Co.".
- Barra superior de estado (AppBar):
  * Foto de perfil circular del tutor a la izquierda.
  * Saludo personalizado: "Hola, Mariana 👋" con subtítulo "3 mascotas registradas".
  * Botón de campana de notificaciones con punto rojo indicador a la derecha.
- Tarjeta destacada de la mascota activa (Hero Card):
  * Fondo verde menta suave (#E3F6F3) con borde redondeado pronunciado y sombra ligera.
  * Foto de un perro Golden Retriever sonriente en avatar grande.
  * Datos destacados: "Milo" (Golden Retriever, 2 años y medio, 28 kg).
  * Chip indicador de estado de salud: "Vacunas al día ✓" en verde oscuro.
  * Selector desplegable sutil para cambiar a otra mascota ("Luna - Gato Siamés").
- Banner de Próxima Cita Médica (Appointment Card):
  * Fondo blanco con borde naranja/ámbar cálido (#F0C572).
  * Icono de calendario y hora: "Mañana, 10:30 AM".
  * Detalle: "Control de Vacuna Antirrábica con Dra. Gómez".
  * Botón secundario compacto: "Reprogramar".
- Accesos rápidos a servicios clínicos (Grid de 4 botones circulares con etiquetas):
  * Icono de estetoscopio: "Agendar Cita".
  * Icono de jeringa: "Vacunación".
  * Icono de tijeras: "Peluquería".
  * Icono de ambulancia con alerta roja: "Urgencias 24h".
- Sección de Historial Clínico Reciente:
  * Lista de 2 tarjetas compactas con últimas atenciones:
    - "Desparasitación interna" - 12 de septiembre (Dr. Ramírez).
    - "Limpieza dental preventiva" - 04 de julio (Dra. Gómez).
- Barra de navegación inferior fija (BottomNavigationBar):
  * 4 iconos con etiqueta:
    - Inicio (activo, verde #0F8478).
    - Mascotas.
    - Citas.
    - Perfil / Ajustes.
```

Puntos clave de este diseño:
- **Hero Card de la mascota:** centraliza la información vital (peso, raza, estado de vacunas) y permite alternar entre mascotas registradas sin cambiar de cuenta.
- **Banner de cita:** el uso del color ámbar destaca el recordatorio inmediato sin alarmar al tutor.
- **Acceso a Urgencias 24h:** resaltado con alerta visual para situaciones críticas donde cada segundo cuenta.
- **Barra inferior fija:** garantiza navegación consistente hacia las demás secciones del sistema.

## Cómo Antigravity inspecciona las pantallas con Stitch MCP

Cuando Stitch MCP está configurado en tu archivo `.agents/mcp_config.json`, Antigravity dispone de herramientas para interactuar con tus lienzos de Stitch directamente desde el entorno de trabajo:

- `stitch_list_projects`: Enumera los proyectos de diseño activos asociados a tu clave de API de Stitch.
- `stitch_get_screen`: Descarga la descripción estructurada (tokens de color, tipografías, jerarquía de contenedores y componentes) de una pantalla específica mediante su identificador.

Por ejemplo, puedes pedirle a Antigravity:

> *"Inspecciona la pantalla de HomeScreen en mi proyecto de Stitch de la veterinaria. Lista los colores primarios y la jerarquía de componentes de la tarjeta de la mascota."*

Antigravity invoca `stitch_get_screen` y recibe una estructura JSON con los tokens exactos:

```json
{
  "screenId": "home-veterinaria-patitas",
  "name": "HomeScreen Patitas",
  "themeTokens": {
    "primary": "#0F8478",
    "surface": "#FDFCFB",
    "cardHero": "#E3F6F3",
    "alertWarning": "#F0C572",
    "textPrimary": "#161A26"
  },
  "sections": [
    { "type": "AppBar", "elements": ["AvatarTutor", "GreetingText", "NotificationBell"] },
    { "type": "HeroCard", "petName": "Milo", "status": "Vacunas al día" },
    { "type": "AppointmentBanner", "date": "Mañana, 10:30 AM" },
    { "type": "QuickServicesGrid", "items": ["Agendar", "Vacunación", "Peluquería", "Urgencias"] },
    { "type": "BottomBar", "tabs": ["Inicio", "Mascotas", "Citas", "Perfil"] }
  ]
}
```

Gracias a esta integración, no necesitas transcribir valores hexadecimales a ciegas ni adivinar el espaciado entre widgets. El agente utiliza los datos exactos del prototipo para cualquier análisis o documentación de tu proyecto.

## Paso a paso: Configurar y experimentar con Stitch MCP

Ahora pondrás en práctica la conexión entre tu entorno local y Google Stitch para experimentar la extracción de prototipos con Antigravity:

- **Paso 1: Obtener tu API Key en Google Stitch:**
  Para que el servidor MCP pueda conectarse a tu cuenta de Stitch sin abrir ventanas interactivas del navegador en cada ejecución, necesitas una clave de API:
  1. Ingresa a [stitch.withgoogle.com](https://stitch.withgoogle.com) con tu cuenta de Google.
  2. Haz clic en el icono de tu perfil o avatar en la esquina superior derecha de la pantalla.
  3. Selecciona **Settings** (Configuración) en el menú desplegable.
  4. Dirígete a la pestaña o sección **API Keys**.
  5. Haz clic en **Create Key** (o *Generate a Key*) y copia de inmediato la clave generada.
  
  *(Opción alternativa por consola: puedes ejecutar en tu terminal `npx @_davideast/stitch-mcp init` para autenticarte mediante el asistente guiado interactivo).*

- **Paso 2: Configurar el servidor en tu proyecto:**
  En la raíz de tu proyecto, abre o crea el archivo `.agents/mcp_config.json` y registra el servidor de Stitch dentro de `mcpServers`, reemplazando el valor de `STITCH_API_KEY` con tu clave:
  ```json
  {
    "mcpServers": {
      "stitch": {
        "command": "npx",
        "args": ["-y", "stitch-mcp"],
        "env": {
          "STITCH_API_KEY": "tu_clave_de_google_stitch"
        }
      }
    }
  }
  ```
  *Nota de seguridad:* Nunca hagas commit de tu clave en un repositorio público. Si compartes el repositorio de tu equipo, es recomendable definir la variable de entorno en tu sistema operativo (`export STITCH_API_KEY="..."`) o agregar el bloque a la configuración global en `~/.gemini/config/mcp_config.json`.

- **Paso 3: Generar el prototipo en Google Stitch:**
  En [stitch.withgoogle.com](https://stitch.withgoogle.com), crea un nuevo lienzo e ingresa los prompts estructurados de la clínica veterinaria vistos en esta lección (o los de tu proyecto de semestre). Verifica que se generen los mockups de `LoginScreen`, `SigninScreen` y `HomeScreen`.

- **Paso 4: Experimentar la consulta en Antigravity:**
  Abre una terminal en tu proyecto e inicia Antigravity. Como `.agents/mcp_config.json` se procesa al arrancar, el agente descubrirá de inmediato las herramientas de Stitch.
  
  Pídele al agente en lenguaje natural:
  ```text
  > Consulta mis proyectos en Google Stitch y muéstrame las pantallas disponibles del flujo de veterinaria.
  ```
  
  Luego, solicítale una inspección detallada:
  ```text
  > Extrae los tokens visuales de la pantalla HomeScreen en Stitch: colores primarios, fondo de tarjetas y componentes detectados.
  ```

- **Paso 5: Qué descubres con este ejercicio:**
  Antigravity ejecuta internamente `stitch_list_projects` y `stitch_get_screen`, mostrando el árbol de componentes y los códigos cromáticos exactos. Has conectado el diseño en la nube con tu asistente local, eliminando la transcripción manual de medidas.

