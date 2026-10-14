# Prototipado con Stitch MCP

<!-- tags: Stitch MCP, Google Stitch, prototipo de interfaz, login en Flutter, registro en Flutter, diseño a código, Entrega 1, flutter-pantallas y Stitch, stitch.withgoogle.com -->

En la Entrega 1 del curso debes presentar el prototipo no funcional de tu aplicación en **Stitch o Figma**. En lugar de copiar a mano cada medida, color y campo de texto desde la herramienta gráfica hacia Flutter, puedes conectar a Antigravity directamente con tu diseño usando el **MCP de Google Stitch**.

## Qué es Google Stitch

**Google Stitch** (`stitch.withgoogle.com`) es un entorno experimental de diseño de interfaces desarrollado por Google Labs. Permite conceptualizar y refinar pantallas completas a partir de descripciones en lenguaje natural, ajustando la tipografía, los contrastes y la distribución de los componentes visuales en un lienzo interactivo.

Tradicionalmente, pasar de un mockup a código requiere inspeccionar visualmente cada elemento y transcribirlo línea por línea. Con el servidor MCP de Stitch, Antigravity puede consultar la estructura del lienzo y traducir los elementos visuales a widgets de Flutter.

## El flujo de diseño a código

El diseño visual entrega la apariencia y los colores, pero la skill `flutter-pantallas` impone la disciplina arquitectónica:

```svg
<svg id="stFlujo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 440" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="stFlujo-ttl stFlujo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="stFlujo-ttl">De Stitch al código Flutter con Antigravity</title>
  <desc id="stFlujo-dsc">Cuatro pasos enlazados. 1: Diseño en Stitch canvas. 2: Antigravity consulta Stitch MCP. 3: Antigravity filtra con la skill flutter-pantallas. 4: Código generado en lib/screens/login_screen.dart.</desc>
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
  <text class="title" x="48" y="56">De Stitch al código Flutter con Antigravity</text>
  <text class="sub" x="48" y="80" data-fit="860">El diseño en Stitch entrega la apariencia; la skill flutter-pantallas impone los componentes permitidos.</text>
  <rect x="48" y="120" width="196" height="170" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <circle cx="72" cy="146" r="11" fill="#A96C05"/><text x="72" y="150.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">1</text>
  <text x="96" y="151" font-size="14" font-weight="700" fill="#A96C05" text-anchor="start">Lienzo Stitch</text>
  <text x="64" y="184" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Diseño con IA</text>
  <text x="64" y="206" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Mockup visual de</text>
  <text x="64" y="226" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Login y Registro</text>
  <text x="64" y="250" font-size="11.5" font-weight="600" fill="#A96C05" text-anchor="start" class="mono">stitch.withgoogle</text>
  <rect x="270" y="120" width="196" height="170" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <circle cx="294" cy="146" r="11" fill="#7439B8"/><text x="294" y="150.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">2</text>
  <text x="318" y="151" font-size="14" font-weight="700" fill="#7439B8" text-anchor="start">Stitch MCP</text>
  <text x="286" y="184" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Extracción</text>
  <text x="286" y="206" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Lee campos de texto,</text>
  <text x="286" y="226" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">botones, colores y</text>
  <text x="286" y="246" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">distribución espacial.</text>
  <rect x="492" y="120" width="196" height="170" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <circle cx="516" cy="146" r="11" fill="#4453C9"/><text x="516" y="150.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">3</text>
  <text x="540" y="151" font-size="14" font-weight="700" fill="#4453C9" text-anchor="start">Skill Pantallas</text>
  <text x="508" y="184" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start">Auditoría</text>
  <text x="508" y="206" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Exige widgets.md,</text>
  <text x="508" y="226" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">StatelessWidget y</text>
  <text x="508" y="246" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">reutilizar componentes.</text>
  <rect x="714" y="120" width="198" height="170" rx="12" fill="#E8F6E3" stroke="#3A8235" stroke-width="2.5"/>
  <circle cx="738" cy="146" r="11" fill="#3A8235"/><text x="738" y="150.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">4</text>
  <text x="762" y="151" font-size="14" font-weight="700" fill="#3A8235" text-anchor="start">Código Flutter</text>
  <text x="730" y="184" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">LoginScreen</text>
  <text x="730" y="206" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">Limpia, navegable y</text>
  <text x="730" y="226" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">100% entendible para</text>
  <text x="730" y="246" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start">el estudiante.</text>
  <path d="M244,205 H264" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#stFlujo-arrow)"/>
  <path d="M466,205 H486" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#stFlujo-arrow)"/>
  <path d="M688,205 H708" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#stFlujo-arrow)"/>
  <rect x="48" y="316" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="342" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">El agente no inventa la UI:</tspan> toma la intención visual de Stitch, pero la traduce únicamente con los widgets autorizados del curso.</text>
</svg>
```

El proceso sigue cuatro momentos claros:

1. **Diseño en el lienzo:** Creas el prompt de la pantalla en Stitch (o partes de una plantilla prediseñada). En esta sesión trabajaremos con el flujo de autenticación: la pantalla de inicio de sesión (`LoginScreen`) y la pantalla de registro de nuevo usuario (`RegisterScreen`).
2. **Consulta vía MCP:** Antigravity llama a las herramientas de Stitch MCP para extraer la información estructural: qué títulos hay, qué campos de entrada se necesitan (`TextField`), qué botones de acción existen y qué paleta cromática se definió.
3. **Filtro con la skill del curso:** Antigravity no genera código descontrolado. Como tiene activa la skill `flutter-pantallas`, toma los datos de Stitch pero los traduce estrictamente a la paleta de `widgets.md` vista en clase. Si Stitch sugiere elementos no cubiertos todavía (como animaciones o gestores de estado complejos), la skill obliga al agente a ceñirse a `StatelessWidget` y componentes limpios.
4. **Archivos generados:** El agente escribe los archivos en `lib/screens/` y los registra en las rutas de `lib/main.dart`.

## La pantalla de inicio de sesión (LoginScreen)

La pantalla de login para la red profesional `mi_app_1` reúne los widgets esenciales de entrada y acción:

```dart
import 'package:flutter/material.dart';

class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFFBFBFD),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 32),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 20),
              const Center(
                child: CircleAvatar(
                  radius: 36,
                  backgroundColor: Color(0xFFEEF1FF),
                  child: Icon(Icons.work_outline, size: 36, color: Color(0xFF4453C9)),
                ),
              ),
              const SizedBox(height: 24),
              const Text(
                'Bienvenido de nuevo',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.w700, color: Color(0xFF161A26)),
              ),
              const SizedBox(height: 8),
              const Text(
                'Ingresa con tus credenciales profesionales',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 14, color: Color(0xFF556074)),
              ),
              const SizedBox(height: 36),
              const TextField(
                keyboardType: TextInputType.emailAddress,
                decoration: InputDecoration(
                  labelText: 'Correo electrónico',
                  hintText: 'tu.nombre@empresa.com',
                  prefixIcon: Icon(Icons.email_outlined),
                  border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(10))),
                ),
              ),
              const SizedBox(height: 16),
              const TextField(
                obscureText: true,
                decoration: InputDecoration(
                  labelText: 'Contraseña',
                  hintText: '••••••••',
                  prefixIcon: Icon(Icons.lock_outline),
                  border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(10))),
                ),
              ),
              const SizedBox(height: 12),
              Align(
                alignment: Alignment.centerRight,
                child: TextButton(
                  onPressed: () {},
                  child: const Text('¿Olvidaste tu contraseña?', style: TextStyle(color: Color(0xFF4453C9), fontWeight: FontWeight.w600)),
                ),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {},
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color(0xFF4453C9),
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                ),
                child: const Text('Iniciar sesión', style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600)),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

## La pantalla de registro (RegisterScreen)

La pantalla de registro complementa el flujo solicitando el nombre, titular profesional, correo y contraseña:

- Se hospeda en `lib/screens/register_screen.dart`.
- Utiliza un `AppBar` con botón para volver atrás.
- Organiza los campos dentro de una `Column` con scroll para evitar desbordamientos verticales (*overflow*).
- Respeta la regla de que los botones tienen `onPressed: () {}` porque el estado dinámico y la lógica de autenticación corresponden a sesiones posteriores.

## Cómo pedirle la pantalla al agente

Con el servidor MCP configurado y la skill en `.agents/skills/flutter-pantallas/`, abres Antigravity y haces la solicitud de forma directa:

```text
> Consulta el diseño de autenticación en Stitch e implementa LoginScreen y RegisterScreen en lib/screens/, asegurando que cumplan la paleta de flutter-pantallas.
```

Antigravity consultará el servidor MCP de Stitch, leerá `widgets.md`, escribirá los archivos y registrará las rutas en `main.dart`. En la siguiente lección veremos cómo verificar estas pantallas en un navegador real usando Playwright MCP.
