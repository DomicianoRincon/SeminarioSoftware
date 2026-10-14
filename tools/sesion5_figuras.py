"""Figuras SVG de las lecciones de la sesión 5 (S0034 a S0038).

    python3 tools/sesion5_figuras.py <carpeta>     escribe un .svg por figura, para revisarlas
    python3 tools/sesion5_figuras.py --inject      reemplaza cada bloque ```svg de content/lessonS34.md a
                                                   lessonS38.md por la figura con el mismo id
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from code_frame import frame  # noqa: E402
from console_frame import frame as console  # noqa: E402
from sesion2_figuras import FAM, head, note  # noqa: E402
from sesion3_figuras import mark, txt  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
INK, MUTED, FAINT = '#161A26', '#556074', '#79809A'
LESSONS = ('lessonS34.md', 'lessonS35.md', 'lessonS36.md', 'lessonS37.md', 'lessonS38.md')

FIGS = {}


def box(x, y, w, h, color, strong=False, dashed=False):
    soft, border, st = FAM[color]
    extra = ' stroke-dasharray="6 4"' if dashed else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{soft}" '
            f'stroke="{st if strong else border}" stroke-width="{2.5 if strong else 1.5}"{extra}/>')


def callout(y, text, fid_fit=820):
    return (f'<rect x="48" y="{y}" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" '
            f'stroke-width="1.25" stroke-dasharray="5 4"/>'
            f'<text x="68" y="{y + 26}" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="{fid_fit}">{text}</text>')


def chip(cx, cy, n, color):
    return (f'<circle cx="{cx}" cy="{cy}" r="11" fill="{FAM[color][2]}"/>'
            + txt(cx, cy + 4.5, str(n), 12.5, 700, '#FFFFFF', 'middle'))


def tree(nodes, x0=64, y0=140, step=36, indent=40, badge_x=560):
    """Árbol de carpetas. nodes: (profundidad, nombre, 'd'|'f', nuevo)."""
    out, pos, last = [], {}, {}
    green = FAM['green']
    for i, (depth, name, kind, new) in enumerate(nodes):
        x, y = x0 + depth * indent, y0 + i * step
        pos[name] = (x, y)
        dim = kind.endswith('?')
        kind = kind[0]
        start = len(out)
        if depth:
            px, py = last[depth - 1]
            out.append(f'<path d="M{px + 12},{py + 10} V{y} H{x - 6}" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>')
        last[depth] = (x, y)
        if kind == 'd':
            out.append(f'<path d="M{x},{y - 8} h9 l3,3 h12 v13 h-24 Z" fill="{FAM["amber"][0]}" '
                       f'stroke="{FAM["amber"][2]}" stroke-width="1.5" stroke-linejoin="round"/>')
            out.append(txt(x + 34, y + 5, name, 14, 700, INK, cls='mono'))
        else:
            out.append(f'<path d="M{x + 4},{y - 9} h10 l5,5 v13 h-15 Z" fill="#FFFFFF" '
                       f'stroke="{green[2] if new else FAINT}" stroke-width="1.5" stroke-linejoin="round"/>')
            out.append(txt(x + 34, y + 5, name, 13.5, 700 if new else 400, green[2] if new else MUTED, cls='mono'))
        if new:
            out.append(f'<rect x="{badge_x}" y="{y - 10}" width="56" height="22" rx="11" fill="{green[0]}" '
                       f'stroke="{green[1]}" stroke-width="1.5"/>' + txt(badge_x + 28, y + 5, 'nuevo', 12, 700, green[2], 'middle'))
        if dim:
            out[start:] = ['<g opacity=".55">' + ''.join(out[start:]) + '</g>']
    return '\n  '.join(out), pos


# ───────────────────────────── S0034 · ¿Qué es MCP?

def mcp_arquitectura():
    fid = 'mcpArquitectura'
    h = 440
    s = head(fid, h, 'Arquitectura del Model Context Protocol (MCP)',
             'Arquitectura del Model Context Protocol (MCP)',
             'Antigravity actúa como Host y Cliente. Se comunica con servidores independientes mediante stdio (JSON-RPC).',
             'Tres bloques horizontales. A la izquierda, Antigravity Host y Cliente. En el centro, dos Servidores MCP: Stitch y Playwright. A la derecha, los servicios externos: el lienzo de Stitch y el navegador Chromium.')
    
    # Host Antigravity
    s += '  ' + box(48, 120, 260, 210, 'indigo', strong=True) + '\n'
    s += '  ' + txt(72, 154, 'Google Antigravity', 17, 700, FAM['indigo'][2]) + '\n'
    s += '  ' + txt(72, 178, 'Host y Cliente MCP', 13, 600, MUTED) + '\n'
    s += '  ' + txt(72, 212, '• Motor de razonamiento', 13.5, 400, INK) + '\n'
    s += '  ' + txt(72, 236, '• Reglas de AGENTS.md', 13.5, 400, INK) + '\n'
    s += '  ' + txt(72, 260, '• Skills activadas', 13.5, 400, INK) + '\n'
    s += '  ' + txt(72, 284, '• Gestión de permisos', 13.5, 400, INK) + '\n'

    # Servidores MCP (centro)
    s += '  ' + box(356, 120, 250, 96, 'amber') + '\n'
    s += '  ' + txt(376, 150, 'Stitch MCP Server', 15, 700, FAM['amber'][2], cls='mono') + '\n'
    s += '  ' + txt(376, 174, 'Proceso local · stdio', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(376, 194, 'Herramientas de UI / tokens', 12.5, 600, INK) + '\n'

    s += '  ' + box(356, 234, 250, 96, 'teal') + '\n'
    s += '  ' + txt(376, 264, 'Playwright MCP Server', 15, 700, FAM['teal'][2], cls='mono') + '\n'
    s += '  ' + txt(376, 288, 'Proceso local · stdio', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(376, 308, 'Herramientas de navegador', 12.5, 600, INK) + '\n'

    # Recursos externos (derecha)
    s += '  ' + box(654, 120, 258, 96, 'amber', dashed=True) + '\n'
    s += '  ' + txt(674, 150, 'Google Stitch Web', 15, 700, FAM['amber'][2]) + '\n'
    s += '  ' + txt(674, 174, 'stitch.withgoogle.com', 12.5, 400, MUTED, cls='mono') + '\n'
    s += '  ' + txt(674, 194, 'Lienzo de diseño con IA', 12.5, 400, INK) + '\n'

    s += '  ' + box(654, 234, 258, 96, 'teal', dashed=True) + '\n'
    s += '  ' + txt(674, 264, 'Navegador Chromium', 15, 700, FAM['teal'][2]) + '\n'
    s += '  ' + txt(674, 288, 'Local · Headless / Visible', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(674, 308, 'Árbol de accesibilidad y clics', 12.5, 400, INK) + '\n'

    # Flechas conectoras
    s += f'  <path d="M308,168 H350" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M308,282 H350" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M606,168 H648" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M606,282 H648" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'

    s += '  ' + callout(356, '<tspan font-weight="700">Protocolo abierto:</tspan> Antigravity no sabe qué hace cada servicio internamente; solo se comunica mediante el catálogo de herramientas que cada servidor MCP publica.') + '\n'
    return s + '</svg>\n'


FIGS['mcpArquitectura'] = mcp_arquitectura


def mcp_triada():
    fid = 'mcpTriada'
    h = 390
    s = head(fid, h, 'La tríada del desarrollo con Antigravity',
             'La tríada del desarrollo con Antigravity',
             'Reglas fijas, metodologías bajo demanda y herramientas externas vivas.',
             'Tres tarjetas comparativas. AGENTS.md representa las reglas fijas en cada pedido. Las Skills representan metodologías bajo demanda en Markdown. Los Servidores MCP representan herramientas y conexiones vivas ejecutables.')
    
    # 1. Reglas
    s += '  ' + box(48, 120, 264, 180, 'violet') + '\n'
    s += '  ' + chip(76, 146, 1, 'violet') + '\n'
    s += '  ' + txt(98, 151, 'AGENTS.md', 15, 700, FAM['violet'][2], cls='mono') + '\n'
    s += '  ' + txt(68, 184, 'Reglas fijas', 14, 700, INK) + '\n'
    s += '  ' + txt(68, 208, 'Viaja en cada pedido.', 13, 400, MUTED) + '\n'
    s += '  ' + txt(68, 228, 'Convenciones del equipo,', 13, 400, MUTED) + '\n'
    s += '  ' + txt(68, 248, 'imports y estilo de código.', 13, 400, MUTED) + '\n'
    s += '  ' + txt(68, 276, 'Alcance: Todo el repo', 12, 700, FAM['violet'][2]) + '\n'

    # 2. Skills
    s += '  ' + box(348, 120, 264, 180, 'indigo') + '\n'
    s += '  ' + chip(376, 146, 2, 'indigo') + '\n'
    s += '  ' + txt(398, 151, 'Skills', 15, 700, FAM['indigo'][2], cls='mono') + '\n'
    s += '  ' + txt(368, 184, 'Metodología', 14, 700, INK) + '\n'
    s += '  ' + txt(368, 208, 'Se carga solo si coincide.', 13, 400, MUTED) + '\n'
    s += '  ' + txt(368, 228, 'Paleta de widgets, pasos', 13, 400, MUTED) + '\n'
    s += '  ' + txt(368, 248, 'y plantillas de código.', 13, 400, MUTED) + '\n'
    s += '  ' + txt(368, 276, 'Alcance: Tareas específicas', 12, 700, FAM['indigo'][2]) + '\n'

    # 3. MCP
    s += '  ' + box(648, 120, 264, 180, 'teal', strong=True) + '\n'
    s += '  ' + chip(676, 146, 3, 'teal') + '\n'
    s += '  ' + txt(698, 151, 'Servidores MCP', 15, 700, FAM['teal'][2], cls='mono') + '\n'
    s += '  ' + txt(668, 184, 'Herramientas vivas', 14, 700, INK) + '\n'
    s += '  ' + txt(668, 208, 'Conexión con el exterior.', 13, 400, MUTED) + '\n'
    s += '  ' + txt(668, 228, 'Consultar Stitch, abrir', 13, 400, MUTED) + '\n'
    s += '  ' + txt(668, 248, 'el navegador, bases de datos.', 13, 400, MUTED) + '\n'
    s += '  ' + txt(668, 276, 'Alcance: El mundo exterior', 12, 700, FAM['teal'][2]) + '\n'

    s += '  ' + callout(316, '<tspan font-weight="700">Diferencia clave:</tspan> Una skill le enseña al agente cómo pensar; un servidor MCP le da manos y ojos para interactuar con sistemas reales.') + '\n'
    return s + '</svg>\n'


FIGS['mcpTriada'] = mcp_triada


# ───────────────────────────── S0035 · Configuración de MCP

def mcp_configuracion():
    fid = 'mcpConfiguracion'
    return frame(dict(
        id=fid,
        title='Configuración en <tspan class="mono">.agents/mcp_config.json</tspan>',
        title_plain='Configuración en .agents/mcp_config.json',
        desc='El archivo mcp_config.json define los servidores en la clave mcpServers. Cada servidor declara su comando ejecutable, argumentos y variables de entorno.',
        sub='Antigravity levanta cada servidor al arrancar la sesión.',
        file='.agents/mcp_config.json',
        code=[
            '{',
            '  "mcpServers": {',
            '    "stitch": {',
            '      "command": "npx",',
            '      "args": ["-y", "stitch-mcp"],',
            '      "env": {',
            '        "STITCH_API_KEY": "..."',
            '      }',
            '    },',
            '    "playwright": {',
            '      "command": "npx",',
            '      "args": ["-y", "@playwright/mcp@latest"]',
            '    }',
            '  }',
            '}'
        ],
        panel='QUÉ HACE CADA SERVIDOR',
        result='''
<g transform="translate(16,16)">
  <rect width="328" height="110" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="14" y="24" font-size="14" font-weight="700" fill="#A96C05" class="mono">stitch</text>
  <text x="14" y="46" font-size="12.5" fill="#454C61">Conecta con Google Stitch.</text>
  <text x="14" y="66" font-size="12.5" fill="#454C61">Extrae tokens visuales, colores</text>
  <text x="14" y="86" font-size="12.5" fill="#454C61">y estructura de pantallas.</text>
</g>
<g transform="translate(16,140)">
  <rect width="328" height="110" rx="10" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="14" y="24" font-size="14" font-weight="700" fill="#0F8478" class="mono">playwright</text>
  <text x="14" y="46" font-size="12.5" fill="#454C61">Controla Chromium en vivo.</text>
  <text x="14" y="66" font-size="12.5" fill="#454C61">Lee el árbol de accesibilidad y</text>
  <text x="14" y="86" font-size="12.5" fill="#454C61">simula escritura y clics.</text>
</g>
''',
        arrows=[
            dict(line=2, find='"stitch":', to=(40, 60), color='amber', lane=0),
            dict(line=9, find='"playwright":', to=(40, 185), color='teal', lane=1),
        ],
        cards=[
            ('amber', 'Stitch MCP', ['Prototipado rápido de interfaces', 'y extracción de diseño.']),
            ('teal', 'Playwright MCP', ['Automatización y verificación', 'de la app en el navegador.']),
        ],
    ))


FIGS['mcpConfiguracion'] = mcp_configuracion


# ───────────────────────────── S0036 · Prototipado con Stitch MCP

def st_flujo():
    fid = 'stFlujo'
    h = 440
    s = head(fid, h, 'De Stitch al código Flutter con Antigravity',
             'De Stitch al código Flutter con Antigravity',
             'El diseño en Stitch entrega la apariencia; la skill flutter-pantallas impone los componentes permitidos.',
             'Cuatro pasos enlazados. 1: Diseño en Stitch canvas. 2: Antigravity consulta Stitch MCP. 3: Antigravity filtra con la skill flutter-pantallas. 4: Código generado en lib/screens/login_screen.dart.')

    # Paso 1: Stitch
    s += '  ' + box(48, 120, 196, 170, 'amber') + '\n'
    s += '  ' + chip(72, 146, 1, 'amber') + '\n'
    s += '  ' + txt(96, 151, 'Lienzo Stitch', 14, 700, FAM['amber'][2]) + '\n'
    s += '  ' + txt(64, 184, 'Diseño con IA', 13.5, 700, INK) + '\n'
    s += '  ' + txt(64, 206, 'Mockup visual de', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(64, 226, 'Login y Registro', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(64, 250, 'stitch.withgoogle', 11.5, 600, FAM['amber'][2], cls='mono') + '\n'

    # Paso 2: Stitch MCP
    s += '  ' + box(270, 120, 196, 170, 'violet') + '\n'
    s += '  ' + chip(294, 146, 2, 'violet') + '\n'
    s += '  ' + txt(318, 151, 'Stitch MCP', 14, 700, FAM['violet'][2]) + '\n'
    s += '  ' + txt(286, 184, 'Extracción', 13.5, 700, INK) + '\n'
    s += '  ' + txt(286, 206, 'Lee campos de texto,', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(286, 226, 'botones, colores y', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(286, 246, 'distribución espacial.', 12.5, 400, MUTED) + '\n'

    # Paso 3: Skill flutter-pantallas
    s += '  ' + box(492, 120, 196, 170, 'indigo') + '\n'
    s += '  ' + chip(516, 146, 3, 'indigo') + '\n'
    s += '  ' + txt(540, 151, 'Skill Pantallas', 14, 700, FAM['indigo'][2]) + '\n'
    s += '  ' + txt(508, 184, 'Auditoría', 13.5, 700, INK) + '\n'
    s += '  ' + txt(508, 206, 'Exige widgets.md,', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(508, 226, 'StatelessWidget y', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(508, 246, 'reutilizar componentes.', 12.5, 400, MUTED) + '\n'

    # Paso 4: Código Flutter
    s += '  ' + box(714, 120, 198, 170, 'green', strong=True) + '\n'
    s += '  ' + chip(738, 146, 4, 'green') + '\n'
    s += '  ' + txt(762, 151, 'Código Flutter', 14, 700, FAM['green'][2]) + '\n'
    s += '  ' + txt(730, 184, 'LoginScreen', 13.5, 700, INK, cls='mono') + '\n'
    s += '  ' + txt(730, 206, 'Limpia, navegable y', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(730, 226, '100% entendible para', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(730, 246, 'el estudiante.', 12.5, 400, MUTED) + '\n'

    # Conectores
    s += f'  <path d="M244,205 H264" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M466,205 H486" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M688,205 H708" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'

    s += '  ' + callout(316, '<tspan font-weight="700">El agente no inventa la UI:</tspan> toma la intención visual de Stitch, pero la traduce únicamente con los widgets autorizados del curso.') + '\n'
    return s + '</svg>\n'


FIGS['stFlujo'] = st_flujo


# ───────────────────────────── S0037 · Automatización con Playwright MCP

def pw_flujo():
    fid = 'pwFlujo'
    h = 420
    s = head(fid, h, 'Cómo Playwright MCP interactúa con la aplicación',
             'Cómo Playwright MCP interactúa con la aplicación',
             'Antigravity inspecciona la semántica del navegador mediante el árbol de accesibilidad.',
             'El agente envía instrucciones a Playwright MCP. Playwright lee el árbol de accesibilidad de la página y ejecuta acciones reales: rellenar campos, hacer clic y verificar la respuesta.')

    # Antigravity
    s += '  ' + box(48, 120, 250, 160, 'indigo', strong=True) + '\n'
    s += '  ' + txt(72, 154, 'Antigravity', 16, 700, FAM['indigo'][2]) + '\n'
    s += '  ' + txt(72, 180, '1. Solicita navegar a URL', 13, 400, INK) + '\n'
    s += '  ' + txt(72, 204, '2. Analiza el snapshot', 13, 400, INK) + '\n'
    s += '  ' + txt(72, 228, '3. Ordena fill y click', 13, 400, INK) + '\n'
    s += '  ' + txt(72, 252, '4. Verifica resultado', 13, 400, INK) + '\n'

    # Playwright MCP
    s += '  ' + box(348, 120, 240, 160, 'teal') + '\n'
    s += '  ' + txt(372, 154, 'Playwright MCP', 16, 700, FAM['teal'][2], cls='mono') + '\n'
    s += '  ' + txt(372, 182, '• browser_navigate', 13, 600, MUTED, cls='mono') + '\n'
    s += '  ' + txt(372, 206, '• accessibility_snapshot', 13, 600, MUTED, cls='mono') + '\n'
    s += '  ' + txt(372, 230, '• fill / click', 13, 600, MUTED, cls='mono') + '\n'
    s += '  ' + txt(372, 254, '• take_screenshot', 13, 600, MUTED, cls='mono') + '\n'

    # Navegador Chromium
    s += '  ' + box(638, 120, 274, 160, 'amber') + '\n'
    s += '  ' + txt(662, 154, 'Navegador Chromium', 16, 700, FAM['amber'][2]) + '\n'
    s += '  ' + txt(662, 182, 'Campo: Correo electrónico', 13, 400, INK) + '\n'
    s += '  ' + txt(662, 206, 'Campo: Contraseña', 13, 400, INK) + '\n'
    s += '  ' + txt(662, 230, 'Botón: [ Iniciar sesión ]', 13, 700, FAM['indigo'][2]) + '\n'
    s += '  ' + txt(662, 254, 'Estado: Interacción verificada', 12.5, 600, FAM['teal'][2]) + '\n'

    # Flechas bidireccionales
    s += f'  <path d="M298,185 H342" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M342,215 H298" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M588,185 H632" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M632,215 H588" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'

    s += '  ' + callout(306, '<tspan font-weight="700">Accesibilidad semántica:</tspan> Playwright MCP entrega a Antigravity la estructura de botones, etiquetas y campos de entrada en texto estructurado, ahorrando miles de tokens frente a procesar capturas de imagen.') + '\n'
    return s + '</svg>\n'


FIGS['pwFlujo'] = pw_flujo


# ───────────────────────────── S0038 · Taller y Carpetas

def ts_carpetas_mcp():
    fid = 'tsCarpetasMcp'
    h = 490
    s = head(fid, h, 'Tu proyecto con servidores MCP y autenticación',
             'Tu proyecto con servidores MCP y autenticación',
             'El archivo mcp_config.json conecta las herramientas; lib/screens/ recibe las pantallas de Login y Registro.',
             'El árbol de carpetas de mi_app_1: dentro de .agents se agrega mcp_config.json. Dentro de lib/screens se agregan login_screen.dart y register_screen.dart.')

    nodes = [
        (0, 'mi_app_1/', 'd', False),
        (1, '.agents/', 'd', False),
        (2, 'mcp_config.json', 'f', True),
        (2, 'skills/', 'd', False),
        (3, 'mer-svg/', 'd?', False),
        (3, 'flutter-pantallas/', 'd', False),
        (1, 'lib/', 'd', False),
        (2, 'components/', 'd', False),
        (2, 'screens/', 'd', False),
        (3, 'messages_screen.dart', 'f', False),
        (3, 'login_screen.dart', 'f', True),
        (3, 'register_screen.dart', 'f', True),
        (2, 'main.dart', 'f', False),
    ]
    tree_svg, _ = tree(nodes, x0=64, y0=132, step=25, indent=36, badge_x=470)
    s += '  ' + tree_svg + '\n'

    # Notas a la derecha
    s += '  ' + box(552, 150, 360, 80, 'teal') + '\n'
    s += '  ' + txt(570, 178, '.agents/mcp_config.json', 13.5, 700, FAM['teal'][2], cls='mono') + '\n'
    s += '  ' + txt(570, 202, 'Registra Stitch y Playwright para Antigravity.', 12.5, 400, INK) + '\n'

    s += '  ' + box(552, 250, 360, 110, 'green') + '\n'
    s += '  ' + txt(570, 278, 'login_screen y register_screen', 13.5, 700, FAM['green'][2], cls='mono') + '\n'
    s += '  ' + txt(570, 302, 'Pantallas generadas a partir del diseño', 12.5, 400, INK) + '\n'
    s += '  ' + txt(570, 322, 'de Stitch y auditadas con Playwright.', 12.5, 400, INK) + '\n'
    s += '  ' + txt(570, 342, 'Insumo directo para la Entrega 1.', 12, 700, FAM['green'][2]) + '\n'

    s += '  ' + callout(410, '<tspan font-weight="700">Resultado del taller:</tspan> Dos pantallas nuevas listas en tu aplicación, diseñadas desde Stitch y verificadas con Playwright.') + '\n'
    return s + '</svg>\n'


FIGS['tsCarpetasMcp'] = ts_carpetas_mcp


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--inject':
        done = set()
        for name in LESSONS:
            path = ROOT / 'content' / name
            if not path.exists():
                continue
            text = path.read_text(encoding='utf-8')

            def swap(m):
                fid = m.group(1)
                if fid in FIGS:
                    done.add(fid)
                    return '```svg\n' + FIGS[fid]() + '```'
                return m.group(0)

            new = re.sub(r'```svg\n<svg id="(\w+)".*?```', swap, text, flags=re.S)
            path.write_text(new, encoding='utf-8')
        missing = set(FIGS) - done
        print('inyectadas:', len(done), '· sin usar:', sorted(missing) or 'ninguna')
        return

    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'build_figuras_sesion5')
    out.mkdir(parents=True, exist_ok=True)
    only = sys.argv[2:] if len(sys.argv) > 2 else []
    for fid, fn in FIGS.items():
        if only and fid not in only:
            continue
        (out / f'{fid}.svg').write_text(fn(), encoding='utf-8')
    print(len(FIGS), 'figuras generadas en', out)


if __name__ == '__main__':
    main()
