"""Figuras SVG de las lecciones de la sesión 5 (S0034 a S0039).

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
LESSONS = ('lessonS34.md', 'lessonS35.md', 'lessonS36.md', 'lessonS37.md', 'lessonS39.md')

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
             'Antigravity actúa como Host y Cliente. Se comunica con servidores locales (stdio) y remotos (HTTP).',
             'Tres bloques horizontales. A la izquierda, Antigravity Host y Cliente. En el centro, dos Servidores MCP: Stitch (remoto HTTP) y Playwright (local stdio). A la derecha, los servicios externos: el lienzo de Stitch y el navegador Chromium.')
    
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
    s += '  ' + txt(376, 174, 'Servidor remoto · HTTP', 12.5, 400, MUTED) + '\n'
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

    s += '  ' + callout(356, '<tspan font-weight="700">Protocolo abierto:</tspan> Antigravity no conoce cada servicio por dentro: solo usa el catálogo que publica cada servidor.') + '\n'
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
        desc='El archivo mcp_config.json define los servidores en la clave mcpServers. Soporta servidores remotos (serverUrl y headers) y locales (command y args).',
        sub='Antigravity conecta o levanta cada servidor al arrancar la sesión.',
        file='.agents/mcp_config.json',
        code=[
            '{',
            '  "mcpServers": {',
            '    "stitch": {',
            '      "serverUrl": "https://stitch.googleapis.com/mcp",',
            '      "headers": {',
            '        "X-Goog-Api-Key": "key"',
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
<g transform="translate(16,26)">
  <rect width="328" height="90" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="16" y="32" font-size="14" font-weight="700" fill="#A96C05" class="mono">stitch</text>
  <text x="16" y="54" font-size="12.5" fill="#454C61">Servidor remoto en la nube.</text>
  <text x="16" y="74" font-size="12.5" fill="#454C61">Extrae tokens visuales, colores y pantallas.</text>
</g>
<g transform="translate(16,194)">
  <rect width="328" height="90" rx="10" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="16" y="32" font-size="14" font-weight="700" fill="#0F8478" class="mono">playwright</text>
  <text x="16" y="54" font-size="12.5" fill="#454C61">Controla Chromium en vivo.</text>
  <text x="16" y="74" font-size="12.5" fill="#454C61">Lee el árbol de accesibilidad y simula clics.</text>
</g>
''',
        arrows=[
            dict(line=2, find='"stitch":', to=(16, 71), color='amber'),
            dict(line=8, find='"playwright":', to=(16, 239), color='teal'),
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
    s = head(fid, h, 'Flujo de prototipado de UI con Stitch MCP',
             'Flujo de prototipado de UI con Stitch MCP',
             'De los prompts en lenguaje natural a los mockups consultados por Antigravity.',
             'Cuatro pasos enlazados. 1: Prompts estructurados en Stitch (Clínica Veterinaria). 2: Stitch MCP extrae jerarquía y tokens. 3: Antigravity inspecciona pantallas y elementos. 4: Mockups validados listos para SigninScreen, LoginScreen y HomeScreen.')

    # Paso 1: Stitch
    s += '  ' + box(48, 120, 196, 170, 'amber') + '\n'
    s += '  ' + chip(72, 146, 1, 'amber') + '\n'
    s += '  ' + txt(96, 151, 'Lienzo Stitch', 14, 700, FAM['amber'][2]) + '\n'
    s += '  ' + txt(64, 184, 'Prompts UI', 13.5, 700, INK) + '\n'
    s += '  ' + txt(64, 206, 'Veterinaria Peludos', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(64, 226, 'Signin, Login y Home', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(64, 250, 'stitch.withgoogle', 11.5, 600, FAM['amber'][2], cls='mono') + '\n'

    # Paso 2: Stitch MCP
    s += '  ' + box(270, 120, 196, 170, 'violet') + '\n'
    s += '  ' + chip(294, 146, 2, 'violet') + '\n'
    s += '  ' + txt(318, 151, 'Stitch MCP', 14, 700, FAM['violet'][2]) + '\n'
    s += '  ' + txt(286, 184, 'Extracción', 13.5, 700, INK) + '\n'
    s += '  ' + txt(286, 206, 'stitch_get_screen', 12, 600, FAM['violet'][2], cls='mono') + '\n'
    s += '  ' + txt(286, 226, 'Lee campos, botones,', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(286, 246, 'colores y jerarquía.', 12.5, 400, MUTED) + '\n'

    # Paso 3: Antigravity
    s += '  ' + box(492, 120, 196, 170, 'indigo') + '\n'
    s += '  ' + chip(516, 146, 3, 'indigo') + '\n'
    s += '  ' + txt(540, 151, 'Antigravity', 14, 700, FAM['indigo'][2]) + '\n'
    s += '  ' + txt(508, 184, 'Auditoría Visual', 13.5, 700, INK) + '\n'
    s += '  ' + txt(508, 206, 'Verifica accesibilidad,', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(508, 226, 'contraste de colores y', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(508, 246, 'distribución mobile.', 12.5, 400, MUTED) + '\n'

    # Paso 4: Mockups Listos
    s += '  ' + box(714, 120, 198, 170, 'green', strong=True) + '\n'
    s += '  ' + chip(738, 146, 4, 'green') + '\n'
    s += '  ' + txt(762, 151, 'Mockups Listos', 14, 700, FAM['green'][2]) + '\n'
    s += '  ' + txt(730, 184, 'Clínica Veterinaria', 13.5, 700, INK) + '\n'
    s += '  ' + txt(730, 206, '3 pantallas listas:', 12.5, 400, MUTED) + '\n'
    s += '  ' + txt(730, 226, 'Signin, Login y Home', 12.5, 600, MUTED) + '\n'
    s += '  ' + txt(730, 246, 'Base para Entrega 1.', 12.5, 400, MUTED) + '\n'

    # Conectores
    s += f'  <path d="M244,205 H264" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M466,205 H486" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M688,205 H708" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'

    s += '  ' + callout(316, '<tspan font-weight="700">El agente inspecciona el diseño en vivo:</tspan> Antigravity lee los elementos visuales por Stitch MCP, sin exportar capturas.') + '\n'
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

    s += '  ' + callout(306, '<tspan font-weight="700">Accesibilidad semántica:</tspan> el agente lee botones, etiquetas y campos como texto, sin gastar tokens en capturas.') + '\n'
    return s + '</svg>\n'


FIGS['pwFlujo'] = pw_flujo


# ───────────────────────────── S0039 · Colaboración con GitHub MCP

def gh_flujo():
    fid = 'ghFlujo'
    h = 420
    s = head(fid, h, 'Gestión colaborativa con GitHub MCP',
             'Gestión colaborativa con GitHub MCP',
             'Antigravity interactúa con el repositorio remoto para consultar issues, reportar hallazgos y abrir pull requests.',
             'Tres bloques. A la izquierda, Antigravity gestionando el flujo de trabajo. En el centro, GitHub MCP Server con herramientas de issues y PRs. A la derecha, la plataforma de GitHub con el repositorio del equipo.')

    # Antigravity
    s += '  ' + box(48, 120, 250, 160, 'indigo', strong=True) + '\n'
    s += '  ' + txt(72, 154, 'Antigravity', 16, 700, FAM['indigo'][2]) + '\n'
    s += '  ' + txt(72, 180, '1. Lee requerimientos', 13, 400, INK) + '\n'
    s += '  ' + txt(72, 204, '2. Implementa y audita', 13, 400, INK) + '\n'
    s += '  ' + txt(72, 228, '3. Documenta hallazgos', 13, 400, INK) + '\n'
    s += '  ' + txt(72, 252, '4. Abre Pull Request', 13, 400, INK) + '\n'

    # GitHub MCP Server
    s += '  ' + box(348, 120, 240, 160, 'violet') + '\n'
    s += '  ' + txt(372, 154, 'GitHub MCP Server', 16, 700, FAM['violet'][2], cls='mono') + '\n'
    s += '  ' + txt(372, 182, '• list_issues / get', 13, 600, MUTED, cls='mono') + '\n'
    s += '  ' + txt(372, 206, '• create_issue', 13, 600, MUTED, cls='mono') + '\n'
    s += '  ' + txt(372, 230, '• create_pull_request', 13, 600, MUTED, cls='mono') + '\n'
    s += '  ' + txt(372, 254, '• get_file_contents', 13, 600, MUTED, cls='mono') + '\n'

    # GitHub Remoto
    s += '  ' + box(638, 120, 274, 160, 'green') + '\n'
    s += '  ' + txt(662, 154, 'GitHub del Equipo', 16, 700, FAM['green'][2]) + '\n'
    s += '  ' + txt(662, 182, 'Issue #3: Pantalla de Login', 13, 400, INK) + '\n'
    s += '  ' + txt(662, 206, 'PR #12: feat/auth-screens', 13, 600, FAM['indigo'][2]) + '\n'
    s += '  ' + txt(662, 230, 'Revisión por compañeros', 13, 400, MUTED) + '\n'
    s += '  ' + txt(662, 254, 'Trazabilidad del reto', 12.5, 700, FAM['green'][2]) + '\n'

    # Flechas bidireccionales
    s += f'  <path d="M298,185 H342" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M342,215 H298" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M588,185 H632" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M632,215 H588" fill="none" stroke="{MUTED}" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'

    s += '  ' + callout(306, '<tspan font-weight="700">Trazabilidad en equipo:</tspan> Antigravity une el trabajo local con GitHub: documenta avances y abre revisiones.') + '\n'
    return s + '</svg>\n'


FIGS['ghFlujo'] = gh_flujo


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


# ───────────────────────────── Figuras de apertura: qué permite hacer cada servidor

def cap_card(x, y, n, color, title, lines, art):
    """Tarjeta de capacidad: dibujo de 176×168 a la izquierda, número, título y texto a la derecha."""
    out = box(x, y, 420, 200, color)
    out += f'<g transform="translate({x + 16},{y + 16})">{art}</g>'
    out += chip(x + 220, y + 40, n, color)
    out += txt(x + 240, y + 45, title, 15, 700, FAM[color][2], fit=164)
    for i, ln in enumerate(lines):
        out += txt(x + 208, y + 80 + i * 21, ln, 13, 400, '#454C61', fit=196)
    return out


def cap_figure(fid, title, sub, desc, cards, note_text):
    s = head(fid, 636, title, title, sub, desc)
    pos = [(48, 112), (492, 112), (48, 336), (492, 336)]
    for (x, y), (n, card) in zip(pos, enumerate(cards, 1)):
        s += '  ' + cap_card(x, y, n, *card) + '\n'
    s += '  ' + callout(560, note_text) + '\n'
    return s + '</svg>\n'


def phone(x, y, w, h, inner=''):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#1F2430"/>'
            f'<rect x="{x + 4}" y="{y + 4}" width="{w - 8}" height="{h - 8}" rx="9" fill="#FFFFFF"/>'
            f'<g transform="translate({x + 4},{y + 4})">{inner}</g>')


def bar(x, y, w, h=8, fill='#E3E7EF', rx=4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"/>'


def login_screen(w, accent, extra=False):
    """Pantalla de login en miniatura, en coordenadas de la pantalla del teléfono."""
    c = w / 2
    out = f'<circle cx="{c}" cy="16" r="8" fill="{accent}"/>'
    out += bar(8, 32, w - 16, 10, '#FFFFFF') + f'<rect x="8" y="32" width="{w - 16}" height="10" rx="4" fill="none" stroke="#C4CBD8"/>'
    out += f'<rect x="8" y="48" width="{w - 16}" height="10" rx="4" fill="none" stroke="#C4CBD8"/>'
    out += bar(8, 64, w - 16, 12, accent)
    if extra:
        out += (f'<rect x="8" y="81" width="{w - 16}" height="12" rx="4" fill="#E8F6E3" stroke="#3A8235" stroke-width="1.5"/>')
    return out


def check(cx, cy, color='green'):
    return (f'<circle cx="{cx}" cy="{cy}" r="9" fill="{FAM[color][2]}"/>'
            f'<path d="M{cx - 4},{cy} l3,3 l5,-6" fill="none" stroke="#FFFFFF" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def bubble(w, text, color):
    soft, border, st = FAM[color]
    return (f'<rect x="0" y="0" width="{w}" height="30" rx="10" fill="#FFFFFF" stroke="{border}" stroke-width="1.5"/>'
            + txt(12, 20, text, 12, 600, st, cls='mono'))


def st_capacidades():
    teal, amber = FAM['teal'][2], FAM['amber'][2]
    a1 = (bubble(176, '"Login para Peludos"', 'indigo')
          + f'<path d="M88,34 V52" class="link"/>'
          + phone(52, 58, 72, 110, login_screen(64, teal)))
    a2 = (bubble(176, '"Agrega Google"', 'teal')
          + phone(10, 48, 64, 110, login_screen(56, teal))
          + f'<path d="M80,103 H96" class="link"/>'
          + phone(102, 48, 64, 110, login_screen(56, teal, extra=True)))
    a3 = ''.join(phone(4 + i * 58, 30, 52, 100, login_screen(44, c))
                 for i, c in enumerate((teal, FAM['indigo'][2], amber)))
    a3 += txt(88, 156, '3 versiones', 12, 600, FAM['violet'][2], 'middle')
    a4 = ('<rect width="176" height="168" rx="10" fill="#1F2430"/>'
          + txt(12, 24, 'stitch_get_screen', 12, 600, '#9AA3B8', cls='mono')
          + ''.join(txt(12, 56 + i * 26, k, 12, 400, '#E6E9F0', cls='mono') for i, k in
                    enumerate(('primary', 'surface', 'TextField ×2', 'Button ×1')))
          + f'<rect x="140" y="45" width="22" height="14" rx="3" fill="{teal}"/>'
          + '<rect x="140" y="71" width="22" height="14" rx="3" fill="#FDFCFB"/>')
    return cap_figure(
        'stCapacidades', 'Lo que puedes hacer con Stitch MCP',
        'Cuatro cosas que haces con tus pantallas cuando Stitch está conectado a Antigravity.',
        'Cuatro tarjetas. 1: describir una pantalla en lenguaje natural y Stitch la dibuja. 2: corregirla con un prompt corto, por ejemplo agregar un botón. 3: explorar variantes con otros colores. 4: Antigravity lee colores y componentes del diseño con stitch_get_screen.',
        [('indigo', 'Generar pantallas', ['Describes la pantalla en', 'español y Stitch la dibuja', 'con campos y botones.'], a1),
         ('teal', 'Corregir rápido', ['Pides solo el cambio y', 'Stitch ajusta la pantalla', 'sin rehacerla.'], a2),
         ('violet', 'Explorar variantes', ['Genera versiones con otros', 'colores o distribución', 'para compararlas.'], a3),
         ('amber', 'Leer el diseño', ['Antigravity lee colores y', 'componentes para pasar', 'el diseño a Flutter.'], a4)],
        '<tspan font-weight="700">Tú describes, Stitch dibuja:</tspan> y Antigravity lee el diseño para convertirlo en código, sin copiar colores ni medidas a mano.')


FIGS['stCapacidades'] = st_capacidades


def browser(y, h, url):
    return (f'<rect x="0" y="{y}" width="176" height="{h}" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>'
            f'<path d="M0,{y + 26} H176" stroke="#C4CBD8" stroke-width="1.5"/>'
            + ''.join(f'<circle cx="{12 + i * 11}" cy="{y + 13}" r="3.5" fill="{c}"/>'
                      for i, c in enumerate(('#F3A3B2', '#F0C572', '#9FD68D')))
            + f'<rect x="48" y="{y + 5}" width="120" height="16" rx="8" fill="#EFF1F5"/>'
            + txt(56, y + 17, url, 12, 400, MUTED, cls='mono'))


def pw_capacidades():
    green, violet, indigo = FAM['green'][2], FAM['violet'][2], FAM['indigo'][2]
    a1 = (browser(8, 152, 'localhost:8080')
          + '<rect x="40" y="52" width="96" height="16" rx="5" fill="none" stroke="#C4CBD8"/>'
          + '<rect x="40" y="76" width="96" height="16" rx="5" fill="none" stroke="#C4CBD8"/>'
          + bar(40, 100, 96, 18, FAM['indigo'][2], 5)
          + txt(88, 140, 'Chromium', 12, 600, MUTED, 'middle'))
    rows = (('heading', '"Peludos"'), ('textbox', '"Correo"'), ('textbox', '"Clave"'), ('button', '"Entrar"'))
    a2 = '<rect width="176" height="168" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>'
    a2 += txt(12, 24, '- page', 12, 700, INK, cls='mono')
    for i, (role, name) in enumerate(rows):
        yy = 52 + i * 28
        a2 += f'<path d="M16,{yy - 22} V{yy - 4} H24" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>'
        a2 += txt(28, yy, role, 12, 600, violet, cls='mono') + txt(96, yy, name, 12, 400, INK, cls='mono')
    a3 = ('<rect width="176" height="168" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>'
          + '<rect x="16" y="24" width="144" height="28" rx="6" fill="#FFFFFF" stroke="#0F8478" stroke-width="2"/>'
          + txt(26, 43, 'ana@mail.com', 12, 400, INK, cls='mono')
          + '<path d="M120,30 V46" stroke="#0F8478" stroke-width="1.5"/>'
          + '<rect x="16" y="64" width="144" height="28" rx="6" fill="none" stroke="#C4CBD8"/>'
          + bar(16, 104, 144, 30, indigo, 6) + txt(64, 124, 'Entrar', 13, 700, '#FFFFFF', 'middle')
          + '<circle cx="128" cy="119" r="13" fill="none" stroke="#F0C572" stroke-width="2"/>'
          + '<path d="M128,119 l0,24 l6,-6 l5,10 l4,-2 l-5,-10 l8,0 Z" fill="#161A26" stroke="#FFFFFF" stroke-width="1.25" stroke-linejoin="round"/>')
    a4 = '<rect width="176" height="168" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>'
    for i, t in enumerate(('Abrió /home', 'Ve "Hola, Ana"', '0 errores')):
        a4 += check(26, 34 + i * 36) + txt(44, 39 + i * 36, t, 12.5, 600, INK)
    a4 += ('<rect x="16" y="128" width="144" height="26" rx="6" fill="#EFF1F5"/>'
           + txt(88, 145, 'captura.png', 12, 600, MUTED, 'middle', cls='mono'))
    return cap_figure(
        'pwCapacidades', 'Lo que puedes hacer con Playwright MCP',
        'Antigravity usa un navegador real para probar tu app como lo haría una persona.',
        'Cuatro tarjetas. 1: abrir la app en un navegador Chromium. 2: leer la página como árbol de accesibilidad, con el rol y el nombre de cada elemento. 3: escribir en los campos y hacer clic en los botones. 4: verificar el resultado, revisar la consola y tomar capturas.',
        [('indigo', 'Abrir tu app', ['Lanza un navegador real', 'y entra a tu app Flutter', 'web o a cualquier URL.'], a1),
         ('violet', 'Leer la página', ['Ve la página como árbol', 'de accesibilidad: el rol', 'y nombre de cada cosa.'], a2),
         ('teal', 'Escribir y hacer clic', ['Rellena campos, pulsa', 'botones y navega como', 'lo haría un usuario.'], a3),
         ('green', 'Verificar', ['Comprueba el resultado,', 'revisa la consola y', 'toma capturas.'], a4)],
        '<tspan font-weight="700">Pruebas sin clics manuales:</tspan> tú das la instrucción en español y Playwright la convierte en acciones reales en el navegador.')


FIGS['pwCapacidades'] = pw_capacidades


def pill(x, y, text, color):
    soft, border, st = FAM[color]
    w = int(len(text) * 7.2 + 16)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="20" rx="10" fill="{soft}" stroke="{border}"/>'
            + txt(x + w / 2, y + 14, text, 12, 700, st, 'middle'))


def gh_capacidades():
    green, rose, indigo = FAM['green'][2], FAM['rose'][2], FAM['indigo'][2]
    card = '<rect width="176" height="168" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>'
    a1 = (card + f'<circle cx="20" cy="22" r="7" fill="none" stroke="{green}" stroke-width="2"/>'
          + f'<circle cx="20" cy="22" r="2" fill="{green}"/>'
          + txt(34, 27, '#3 Pantalla login', 12.5, 700, INK)
          + pill(14, 40, 'frontend', 'indigo')
          + txt(14, 86, 'Criterios:', 12, 700, MUTED))
    for i, t in enumerate(('Campo correo', 'Campo clave', 'Botón Entrar')):
        a1 += (f'<rect x="14" y="{98 + i * 22}" width="12" height="12" rx="3" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>'
               + txt(34, 109 + i * 22, t, 12, 400, INK))
    a2 = (card + f'<circle cx="20" cy="22" r="7" fill="none" stroke="{green}" stroke-width="2"/>'
          + f'<circle cx="20" cy="22" r="2" fill="{green}"/>'
          + txt(34, 27, 'Botón no responde', 12.5, 700, INK)
          + pill(14, 40, 'bug', 'rose')
          + txt(14, 86, 'Pasos:', 12, 700, MUTED)
          + ''.join(txt(14, 108 + i * 20, t, 12, 400, INK) for i, t in
                    enumerate(('1. Abrir /registro', '2. Llenar campos', '3. Pulsar Registrar'))))
    main_y, feat_y = 128, 64
    a3 = card + txt(14, 24, 'PR #12', 13, 700, FAM['violet'][2]) + pill(70, 10, 'abierto', 'green')
    a3 += f'<path d="M12,{main_y} H164" stroke="{MUTED}" stroke-width="2"/>'
    a3 += f'<path d="M40,{main_y} C60,{main_y} 52,{feat_y} 76,{feat_y} H120" fill="none" stroke="{indigo}" stroke-width="2"/>'
    a3 += f'<path d="M120,{feat_y} C144,{feat_y} 136,{main_y} 156,{main_y}" fill="none" stroke="{indigo}" stroke-width="2" stroke-dasharray="5 4"/>'
    for cx, cy, c in ((24, main_y, MUTED), (40, main_y, MUTED), (88, feat_y, indigo), (116, feat_y, indigo)):
        a3 += f'<circle cx="{cx}" cy="{cy}" r="6" fill="#FFFFFF" stroke="{c}" stroke-width="2.5"/>'
    a3 += txt(88, feat_y - 14, 'feat/login', 12, 600, indigo, 'middle', cls='mono')
    a3 += txt(12, main_y + 24, 'main', 12, 600, MUTED, cls='mono')
    nodes = ((0, 'equipo/app', 'd'), (1, 'lib', 'd'), (2, 'screens', 'd'), (3, 'login.dart', 'f'))
    a4 = card
    for i, (d, name, kind) in enumerate(nodes):
        x, y = 14 + d * 16, 30 + i * 32
        if d:
            a4 += f'<path d="M{x - 10},{y - 22} V{y - 4} H{x - 2}" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>'
        if kind == 'd':
            a4 += (f'<path d="M{x},{y - 9} h7 l3,3 h10 v12 h-20 Z" fill="{FAM["amber"][0]}" '
                   f'stroke="{FAM["amber"][2]}" stroke-width="1.5" stroke-linejoin="round"/>')
        else:
            a4 += (f'<path d="M{x + 3},{y - 10} h9 l5,5 v12 h-14 Z" fill="#FFFFFF" '
                   f'stroke="{indigo}" stroke-width="1.5" stroke-linejoin="round"/>')
        a4 += txt(x + 26, y + 4, name, 12, 700 if kind == 'f' else 600, indigo if kind == 'f' else INK, cls='mono')
    a4 += txt(88, 156, 'sin clonar', 12, 600, MUTED, 'middle')
    return cap_figure(
        'ghCapacidades', 'Lo que puedes hacer con GitHub MCP',
        'Antigravity trabaja sobre el repositorio del equipo sin salir de la conversación.',
        'Cuatro tarjetas. 1: leer un issue con sus criterios de aceptación. 2: crear un issue de bug con los pasos para reproducirlo. 3: abrir un pull request desde la rama feat/login hacia main. 4: consultar archivos de un repositorio sin clonarlo.',
        [('green', 'Leer issues', ['Lista las tareas del equipo', 'y lee los criterios de', 'aceptación de cada una.'], a1),
         ('rose', 'Reportar fallos', ['Crea un issue con título,', 'etiqueta y los pasos', 'para reproducirlo.'], a2),
         ('violet', 'Abrir pull requests', ['Crea la rama y el PR con', 'un resumen de los cambios', 'para que el equipo revise.'], a3),
         ('amber', 'Leer otros repos', ['Consulta archivos y ramas', 'de un repositorio sin', 'tener que clonarlo.'], a4)],
        '<tspan font-weight="700">Lo delicado se confirma:</tspan> fusionar un PR, subir archivos directo o borrarlos quedan en "ask", y el agente te pregunta antes.')


FIGS['ghCapacidades'] = gh_capacidades


# FIGS['tsCarpetasMcp'] = ts_carpetas_mcp


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
