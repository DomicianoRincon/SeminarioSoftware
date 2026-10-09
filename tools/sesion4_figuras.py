"""Figuras SVG de las lecciones de la sesión 4 (S0029 a S0033).

    python3 tools/sesion4_figuras.py <carpeta>     escribe un .svg por figura, para revisarlas
    python3 tools/sesion4_figuras.py --inject      reemplaza cada bloque ```svg de content/lessonS29.md a
                                                   lessonS33.md por la figura con el mismo id
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from code_frame import frame  # noqa: E402
from console_frame import frame as console  # noqa: E402
from sesion2_figuras import FAM, head, note  # noqa: E402
from sesion3_figuras import device, mark, txt  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
INK, MUTED, FAINT = '#161A26', '#556074', '#79809A'
LESSONS = ('lessonS29.md', 'lessonS30.md', 'lessonS31.md', 'lessonS32.md', 'lessonS33.md')

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
    """Árbol de carpetas. nodes: (profundidad, nombre, 'd'|'f', nuevo). Devuelve (svg, posiciones).

    Con 'd?' o 'f?' el elemento se dibuja atenuado: existe en el formato, pero no se usa aquí."""
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


# ───────────────────────────── S0029 · El agente en consola

def ag_agente():
    """El panel «Agente en consola» de la figura iaTools de S0006, recortado."""
    src = (ROOT / 'content/lessonS6.md').read_text(encoding='utf-8')
    svg = re.search(r'<svg id="iaTools".*?</svg>', src, re.S).group(0).replace('iaTools', 'agAgente')
    defs = re.search(r'<defs>.*?</defs>', svg, re.S).group(0)
    body = svg[svg.index('<rect x="504" y="112"'):svg.index('<text x="48" y="440"')]
    return ('<svg id="agAgente" xmlns="http://www.w3.org/2000/svg" viewBox="480 88 456 344" width="100%" '
            'style="max-width:560px;display:block;margin:0 auto" role="img" aria-labelledby="agAgente-ttl agAgente-dsc" '
            "font-family=\"ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif\">\n"
            '  <title id="agAgente-ttl">Agente en consola</title>\n'
            '  <desc id="agAgente-dsc">Un modelo de IA conectado a un tool system con cuatro herramientas: leer archivos, buscar en el código, editar archivos y ejecutar comandos. Con ellas actúa directamente sobre tu proyecto.</desc>\n'
            f'  {defs}\n  <rect x="480" y="88" width="456" height="344" rx="16" fill="#FBFBFD"/>\n  {body.rstrip()}\n</svg>\n')


FIGS['agAgente'] = ag_agente


def ag_reglas():
    fid = 'agReglas'
    h = 388
    s = head(fid, h, 'Lo que cada agente hace sin preguntar', 'Lo que cada agente hace sin preguntar',
             'Así vienen de fábrica. Con las reglas de esta lección, los dos preguntan antes de editar y de ejecutar.',
             'Dos tarjetas. OpenCode, tal como viene, edita archivos y ejecuta comandos sin preguntar. Antigravity CLI edita archivos dentro del proyecto sin preguntar, pero pregunta antes de ejecutar un comando. Con las reglas de la lección, los dos preguntan en ambos casos.')

    def card(x, color, name, rows):
        strong = FAM[color][2]
        o = '  ' + box(x, 112, 408, 172, color) + '\n'
        o += '  ' + txt(x + 24, 148, name, 18, 700, strong) + '\n'
        for i, (what, asks) in enumerate(rows):
            y = 190 + i * 44
            o += '  ' + txt(x + 24, y, what, 14, 400, INK, fit=210) + '\n'
            fill, ink, label = ('#E8F6E3', '#3A8235', 'pregunta') if asks else ('#FFEBEF', '#C2354F', 'no pregunta')
            o += f'  <rect x="{x + 264}" y="{y - 18}" width="120" height="28" rx="14" fill="{fill}" stroke="{ink}" stroke-width="1.5"/>\n'
            o += '  ' + txt(x + 324, y + 0.5, label, 12.5, 700, ink, 'middle') + '\n'
        return o
    s += card(48, 'violet', 'OpenCode', [('Editar un archivo', False), ('Ejecutar un comando', False)])
    s += card(504, 'indigo', 'Antigravity CLI', [('Editar un archivo', False), ('Ejecutar un comando', True)])
    s += '  ' + callout(308, '<tspan font-weight="700">Tú diriges:</tspan> en el curso, el agente pregunta antes de editar y antes de ejecutar.') + '\n'
    return s + '</svg>\n'


FIGS['agReglas'] = ag_reglas

FIGS['agInstalar'] = lambda: console(dict(
    id='agInstalar',
    title='Instalar OpenCode',
    title_plain='Instalar OpenCode',
    desc='En la consola, el comando npm install -g opencode-ai instala OpenCode. Después, el comando de versión de opencode responde con su número.',
    sub='Se instala una sola vez y queda disponible en todas tus carpetas.',
    term_title='Terminal · C:\\develop',
    lines=[('P', 'npm install -g opencode-ai', 'develop'),
           ('D', 'added 1 package in 12s'),
           ('B', ''),
           ('P', 'opencode --version', 'develop'),
           ('O', '2.x.x')],
    rings=[(0, 9, 26, 1), (4, 0, 5, 2)],
    cards=[(1, 'Instalar', ['El <tspan font-weight="700">-g</tspan> lo deja disponible', 'en todo el equipo.'], False),
           (2, 'Comprobar', ['Si responde con un número', 'de versión, quedó instalado.'], False)],
))

FIGS['agSesion'] = lambda: console(dict(
    id='agSesion',
    title='La primera pregunta',
    title_plain='La primera pregunta',
    desc='Dentro de la carpeta del proyecto se ejecuta opencode. Se le pide que explique el proyecto; el agente busca y lee archivos de lib y responde con un resumen.',
    sub='Una sesión de OpenCode, simplificada. El agente se abre dentro de la carpeta del proyecto.',
    term_title='Terminal · C:\\develop\\mi_app_1',
    lines=[('P', 'opencode', 'mi_app_1'),
           ('B', ''),
           ('O', '> Explícame este proyecto'),
           ('B', ''),
           ('D', '✱ Glob "lib/**"'),
           ('O', '→ Read lib/main.dart'),
           ('O', '→ Read lib/screens/profile_screen.dart'),
           ('B', ''),
           ('K', 'Es una app Flutter con una pantalla, ProfileScreen, y siete componentes.')],
    rings=[(2, 0, 26, 1), (5, 0, 21, 2), (8, 0, 72, 3)],
    cards=[(1, 'Tú preguntas', ['En lenguaje natural,', 'como en un chat.'], False),
           (2, 'El agente lee', ['Cada archivo que abre', 'queda a la vista.'], False),
           (3, 'Responde', ['Con lo que encontró.', 'No cambió nada.'], False)],
))


def ag_modos():
    fid = 'agModos'
    h = 404
    s = head(fid, h, 'Dos modos: <tspan class="mono">plan</tspan> y <tspan class="mono">build</tspan>',
             'Dos modos: plan y build',
             'El agente arranca en build. La tecla Tab cambia de modo, y el modo actual se ve abajo a la derecha.',
             'Dos tarjetas. Plan: el agente lee los archivos y propone qué haría, y pide permiso para editar o ejecutar. Build: crea y edita archivos y ejecuta comandos. La tecla Tab cambia de un modo al otro.')

    def card(x, color, name, tag, facts, last):
        strong = FAM[color][2]
        o = '  ' + box(x, 112, 408, 208, color) + '\n'
        o += '  ' + txt(x + 24, 148, name, 20, 700, strong, cls='mono') + '\n'
        o += '  ' + txt(x + 24, 172, tag, 13.5, 400, MUTED, fit=360) + '\n'
        for i, f in enumerate(facts):
            y = 208 + i * 28
            o += f'  <circle cx="{x + 30}" cy="{y - 4}" r="3.5" fill="{strong}"/>\n'
            o += '  ' + txt(x + 46, y, f, 13.5, 400, INK, fit=340) + '\n'
        o += '  ' + txt(x + 24, 300, last, 13, 700, strong, fit=360) + '\n'
        return o
    s += card(48, 'teal', 'plan', 'Lee y propone.',
              ['Lee tus archivos.', 'Te dice qué haría y en qué orden.', 'Para editar o ejecutar, pide permiso.'],
              'Antes de un cambio grande.')
    s += card(504, 'violet', 'build', 'Hace los cambios.',
              ['Crea y edita archivos.', 'Ejecuta comandos.', 'Es el modo en que arranca.'],
              'Cuando ya sabes qué quieres.')
    s += '  <rect x="48" y="344" width="64" height="32" rx="8" fill="#FFFFFF" stroke="#556074" stroke-width="1.75"/>\n'
    s += '  ' + txt(80, 365, 'Tab', 13.5, 700, INK, 'middle', cls='mono') + '\n'
    s += '  ' + txt(128, 365, 'cambia de un modo al otro. Mira siempre en cuál estás antes de pedir algo.', 13.5, 400, MUTED, fit=760) + '\n'
    return s + '</svg>\n'


FIGS['agModos'] = ag_modos

FIGS['agPermiso'] = lambda: console(dict(
    id='agPermiso',
    title='El agente pide permiso',
    title_plain='El agente pide permiso',
    desc='Se le pide al agente crear una pantalla de ajustes. Antes de escribir el archivo, el agente muestra qué va a editar y ofrece tres opciones: una vez, siempre o rechazar.',
    sub='Con opencode.json en el proyecto, cada edición y cada comando esperan tu respuesta. Simplificado y en español.',
    term_title='Terminal · C:\\develop\\mi_app_1',
    lines=[('O', '> Crea una pantalla de ajustes'),
           ('B', ''),
           ('O', '→ Read lib/main.dart'),
           ('B', ''),
           ('O', '? Permiso para editar lib/screens/settings_screen.dart'),
           ('O', '  Una vez    Siempre    Rechazar')],
    rings=[(4, 2, 52, 1), (5, 2, 31, 2)],
    cards=[(1, 'Qué va a tocar', ['Lee el nombre del archivo', 'o el comando completo.'], False),
           (2, 'Tú decides', ['<tspan font-weight="700">Siempre</tspan> vale para lo que', 'queda de la sesión.'], False)],
))


FIGS['agAntigravity'] = lambda: console(dict(
    id='agAntigravity',
    title='Instalar Antigravity CLI',
    title_plain='Instalar Antigravity CLI',
    desc='En el Símbolo del sistema de Windows, un comando descarga el instalador de Antigravity CLI, lo ejecuta y lo borra. Después, el comando de versión de agy responde con su número.',
    sub='En Windows se instala desde el Símbolo del sistema (cmd). No necesita Node.js.',
    term_title='Símbolo del sistema · C:\\develop',
    lines=[('P', 'curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd', 'develop'),
           ('C', '         && install.cmd && del install.cmd'),
           ('B', ''),
           ('P', 'agy --version', 'develop'),
           ('O', '1.x.x')],
    rings=[(0, 9, 68, 1), (4, 0, 5, 2)],
    cards=[(1, 'Instalar', ['Es una sola línea: descarga el', 'instalador, lo ejecuta y lo borra.'], False),
           (2, 'Comprobar', ['Abre una consola nueva', 'antes de probarlo.'], False)],
))


# ───────────────────────────── S0030 · El archivo de contexto

def cx_que_ve():
    fid = 'cxQueVe'
    h = 468
    s = head(fid, h, 'Lo que el agente ve y lo que no', 'Lo que el agente ve y lo que no',
             'El modelo solo trabaja con lo que le llega. Lo demás no existe para él.',
             'A la izquierda, lo que el agente ve: tu pedido, los archivos que abre y el archivo AGENTS.md, que llega siempre. Las tres cosas entran al modelo de IA. A la derecha, lo que no ve: de qué trata tu app, qué datos guarda y lo que se acordó en clase. Lo que no ve, lo inventa.')
    s += '  ' + txt(48, 124, 'LO QUE VE', cls='h') + '\n'
    s += '  ' + txt(612, 124, 'LO QUE NO VE', cls='h') + '\n'
    left = [('indigo', 'Tu pedido', 'Lo que escribes en ese momento.', False),
            ('teal', 'Los archivos que abre', 'Tu código: de ahí copia el estilo.', False),
            ('amber', 'AGENTS.md', 'Siempre, en cada pedido.', True)]
    for i, (c, t, d, strong) in enumerate(left):
        y = 140 + i * 76
        s += '  ' + box(48, y, 300, 64, c, strong) + '\n'
        s += '  ' + txt(68, y + 27, t, 14.5, 700, FAM[c][2], cls='mono' if strong else '', fit=260) + '\n'
        s += '  ' + txt(68, y + 48, d, 13, 400, '#454C61', fit=260) + '\n'
    s += '  <path class="link" d="M348,172 L404,232"/>\n  <path class="link" d="M348,248 H404"/>\n  <path class="link" d="M348,324 L404,264"/>\n'
    s += '  <rect x="412" y="204" width="136" height="88" rx="12" fill="#7439B8"/>\n'
    s += '  ' + txt(480, 244, 'Modelo', 14.5, 700, '#FFFFFF', 'middle') + '\n'
    s += '  ' + txt(480, 263, 'de IA', 14.5, 700, '#FFFFFF', 'middle') + '\n'
    right = [('De qué trata tu app', 'Red profesional, tienda, reservas…'),
             ('Qué datos guarda', 'Las tablas y sus atributos.'),
             ('Lo que acordaron en clase', 'Lo que todavía no está en el código.')]
    for i, (t, d) in enumerate(right):
        y = 140 + i * 76
        s += '  ' + box(612, y, 300, 64, 'slate', dashed=True) + '\n'
        s += '  ' + txt(632, y + 27, t, 14.5, 700, MUTED, fit=260) + '\n'
        s += '  ' + txt(632, y + 48, d, 13, 400, '#454C61', fit=260) + '\n'
    s += '  ' + callout(388, '<tspan font-weight="700">Lo que no ve, lo inventa.</tspan> El archivo de contexto pasa esas tres cosas a la columna de la izquierda.') + '\n'
    return s + '</svg>\n'


FIGS['cxQueVe'] = cx_que_ve


def cx_antes_despues():
    fid = 'cxAntesDespues'
    h = 560
    s = head(fid, h, 'El mismo pedido, sin y con contexto', 'El mismo pedido, sin y con contexto',
             'Pedido: «Crea la pantalla de inicio con las publicaciones recientes». Resultado real de un modelo gratuito, redibujado.',
             'Dos celulares con la pantalla de inicio de la red profesional. Sin contexto, el agente copió el estilo del proyecto pero inventó una foto en cada publicación, contadores de me gusta y de comentarios y un botón de compartir. Con AGENTS.md, cada publicación muestra solo su autor con usuario y cargo, el texto y la fecha, que sí están en el modelo de datos.')
    bar = '<rect width="200" height="44" fill="#F1ECF8"/>'

    def author(y, name, sub):
        return (f'<circle cx="30" cy="{y}" r="11" fill="#C9A6EE"/>' + txt(48, y - 2, name, 11.5, 700)
                + txt(48, y + 12, sub, 10, 400, MUTED))

    def card(y, hh):
        return f'<rect x="10" y="{y}" width="180" height="{hh}" rx="8" fill="#FFFFFF" stroke="#DCDDE6" stroke-width="1.5"/>'
    left = (bar + txt(16, 27, 'Inicio', 14, 500) + card(54, 224) + author(76, 'Mariana Valenzuela', '@marianav · 2 h')
            + '<rect x="20" y="96" width="160" height="92" rx="6" fill="#E3E7EF"/><path d="M20,176 l40,-36 l30,24 l26,-18 l64,42 v0 h-160 Z" fill="#C4CBD8"/>'
            + txt(20, 206, 'Nuevo avance del rediseño…', 11, 400)
            + txt(22, 262, '♡ 124', 12, 600, INK) + txt(78, 262, '◌ 18', 12, 600, INK) + txt(160, 262, '↗', 13, 600, INK)
            + card(288, 60) + author(310, 'Javier Montes', '@javierm · 5 h')
            + mark(15, 92, 170, 100, 'rose', 8) + mark(15, 244, 170, 28, 'rose', 8))
    right = (bar + txt(16, 27, 'Publicaciones recientes', 14, 500)
             + card(54, 104) + author(76, 'Mariana Valenzuela', '@marianav · Diseñadora')
             + txt(20, 108, 'Nuevo avance del rediseño', 11, 400) + txt(20, 123, 'del componente de pagos.', 11, 400)
             + txt(180, 146, 'Hace 10 min', 10, 400, MUTED, 'end')
             + card(168, 104) + author(190, 'Javier Montes', '@javierm · Ingeniero')
             + txt(20, 222, 'Cerramos la demo con el', 11, 400) + txt(20, 237, 'cliente esta mañana.', 11, 400)
             + txt(180, 260, 'Hace 1 h', 10, 400, MUTED, 'end')
             + card(282, 70) + author(304, 'Ana Torres', '@anatorres · Gerente')
             + mark(15, 62, 170, 90, 'teal', 8))
    s += '  ' + device(64, 136, 200, 340, left, '#F7F7FB', f'{fid}-a') + '\n'
    s += '  ' + device(512, 136, 200, 340, right, '#F7F7FB', f'{fid}-b') + '\n'

    def col(x, color, name, facts):
        strong = FAM[color][2]
        o = '  ' + txt(x, 150, name, 13, 700, strong, cls='h', fit=176) + '\n'
        for i, (a, b) in enumerate(facts):
            y = 196 + i * 66
            o += '  ' + txt(x, y, a, 14, 700, INK, fit=176) + '\n'
            o += '  ' + txt(x, y + 20, b, 12.5, 400, MUTED, fit=176) + '\n'
        return o
    s += col(292, 'rose', 'SIN CONTEXTO',
             [('Copió el estilo', 'Tarjetas, colores, avatar.'), ('Inventó los datos', 'Foto, me gusta, comentarios.'),
              ('Tocó de más', 'Reescribió test/.')])
    s += col(740, 'teal', 'CON AGENTS.md',
             [('Solo datos del modelo', 'Autor, cargo, texto, fecha.'), ('Respetó los límites', 'No tocó test/ y lo dijo.'),
              ('Componente aparte', 'PostItem, en components/.')])
    s = s.replace(f'#{fid} .h{{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}}',
                  f'#{fid} .h{{font-size:12px;font-weight:700;letter-spacing:.08em}}')
    s += '  <path d="M488,128 V488" stroke="#D9DEE8" stroke-width="1.5" stroke-dasharray="4 5"/>\n'
    s += '  ' + txt(48, 528, 'El código le enseñó cómo escribir. De qué trata la app no estaba en ninguna parte.', 13.5, 400, '#454C61', fit=860) + '\n'
    return s + '</svg>\n'


FIGS['cxAntesDespues'] = cx_antes_despues

FIGS['cxInit'] = lambda: console(dict(
    id='cxInit',
    title='Crear el archivo con <tspan class="mono">/init</tspan>',
    title_plain='Crear el archivo con /init',
    desc='Dentro de OpenCode se escribe /init. El agente lee pubspec.yaml y los archivos de lib, y escribe AGENTS.md en la raíz del proyecto.',
    sub='El agente recorre el proyecto y escribe un primer borrador. Es un punto de partida, no el archivo final.',
    term_title='Terminal · C:\\develop\\mi_app_1',
    lines=[('O', '> /init'),
           ('B', ''),
           ('D', '→ Read pubspec.yaml'),
           ('D', '→ Read lib/main.dart'),
           ('D', '→ Read lib/screens/profile_screen.dart'),
           ('O', '← Write AGENTS.md'),
           ('B', ''),
           ('K', 'Creé AGENTS.md con la guía del proyecto.')],
    rings=[(0, 2, 5, 1), (5, 0, 17, 2)],
    cards=[(1, 'Un comando del agente', ['Empieza por <tspan font-weight="700">/</tspan> y se escribe', 'dentro de OpenCode.'], False),
           (2, 'En la raíz del proyecto', ['Junto a <tspan font-weight="700">pubspec.yaml</tspan>.', 'Se sube al repositorio.'], False)],
))


def cx_partes():
    fid = 'cxPartes'
    h = 500
    s = head(fid, h, 'Los seis apartados de <tspan class="mono">AGENTS.md</tspan>', 'Los seis apartados de AGENTS.md',
             'Casi todo ya lo tienes escrito o acordado. Solo hay que ponerlo donde el agente lo lea.',
             'Un documento con seis apartados y de dónde sale cada uno: Qué es, del párrafo de contexto de la Entrega 1. Cómo se ejecuta y se revisa, de los comandos de la sesión 1. Estructura, de las carpetas de la sesión 2. Convenciones, de lo acordado en las sesiones 2 y 3. Modelo de datos, que apunta a docs/modelo.md de la Entrega 1. Reglas para el agente, que son lo que tú le exiges.')
    s += '  <rect x="48" y="112" width="384" height="356" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
    s += '  <path d="M48,144 H432" stroke="#D9DEE8" stroke-width="1.5"/>\n'
    s += '  ' + txt(64, 133, 'AGENTS.md', 12.5, 700, MUTED, cls='mono') + '\n'
    rows = [('indigo', '## Qué es', 'El párrafo de contexto de la Entrega 1.', 200),
            ('slate', '## Cómo se ejecuta y se revisa', 'Los comandos de la sesión 1.', 120),
            ('amber', '## Estructura', 'Las carpetas de la sesión 2.', 160),
            ('teal', '## Convenciones', 'Lo acordado en las sesiones 2 y 3.', 240),
            ('indigo', '## Modelo de datos', 'Apunta a docs/modelo.md, de la Entrega 1.', 100),
            ('violet', '## Reglas para el agente', 'Lo que tú le exiges al agente.', 180)]
    for i, (c, hd, src, w) in enumerate(rows):
        cy = 180 + i * 52
        soft, border, strong = FAM[c]
        s += '  ' + txt(72, cy - 2, hd, 13.5, 700, strong, cls='mono', fit=340) + '\n'
        s += f'  <rect x="72" y="{cy + 9}" width="{w}" height="6" rx="3" fill="#E3E7EF"/>\n'
        s += f'  <path d="M432,{cy} H480" stroke="{border}" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>\n'
        s += f'  <rect x="480" y="{cy - 20}" width="432" height="40" rx="10" fill="{soft}" stroke="{border}" stroke-width="1.5"/>\n'
        s += '  ' + txt(500, cy + 4.5, src, 13.5, 400, INK, fit=396) + '\n'
    return s + '</svg>\n'


FIGS['cxPartes'] = cx_partes


# ───────────────────────────── S0031 · Skills

def sk_carpeta():
    fid = 'skCarpeta'
    h = 692
    s = head(fid, h, 'Una skill es una carpeta', 'Una skill es una carpeta',
             'Vive dentro del proyecto, en .agents/skills/. El nombre de la carpeta es el nombre de la skill.',
             'El árbol de carpetas de mi_app_1: dentro de .agents y skills está la carpeta mer-svg, que es la skill. Adentro tiene el archivo SKILL.md, obligatorio, con las instrucciones; la carpeta references con estilo.md, lo que el agente consulta; la carpeta assets con ejemplo.svg, lo que el agente imita; y, atenuada porque esta skill no la usa, la carpeta scripts con tres programas de ejemplo que el agente ejecutaría: render.sh, render.bat y check.py.')
    nodes = [(0, 'mi_app_1/', 'd', False), (1, '.agents/', 'd', False), (2, 'skills/', 'd', False),
             (3, 'mer-svg/', 'd', False), (4, 'SKILL.md', 'f', False), (4, 'references/', 'd', False),
             (5, 'estilo.md', 'f', False), (4, 'assets/', 'd', False), (5, 'ejemplo.svg', 'f', False),
             (4, 'scripts/', 'd?', False), (5, 'render.sh', 'f?', False), (5, 'render.bat', 'f?', False),
             (5, 'check.py', 'f?', False)]
    t, pos = tree(nodes, step=42)
    s += '  ' + t + '\n'
    notes = [('mer-svg/', 'violet', 'La skill', 'Se llama como su carpeta.', False),
             ('SKILL.md', 'indigo', 'Obligatorio', 'Cuándo se usa y qué pasos sigue.', False),
             ('references/', 'teal', 'Lo que consulta', 'Medidas, colores y reglas.', False),
             ('assets/', 'amber', 'Lo que imita', 'Un ejemplo terminado.', False),
             ('scripts/', 'slate', 'Lo que ejecuta', 'Programas. Esta skill no los usa.', True)]
    for name, c, title, body, dashed in notes:
        x, y = pos[name]
        soft, border, strong = FAM[c]
        end = x + 44 + len(name) * 8.6
        extra = ' stroke-dasharray="6 4"' if dashed else ''
        s += f'  <path d="M{end:.0f},{y} H552" stroke="{border}" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>\n'
        s += f'  <rect x="552" y="{y - 18}" width="360" height="36" rx="10" fill="{soft}" stroke="{border}" stroke-width="1.5"{extra}/>\n'
        s += ('  ' + txt(570, y + 4.5, f'<tspan font-weight="700" fill="{strong}">{title}.</tspan> {body}', 13, 400, '#454C61', fit=330) + '\n')
    for name, what in (('render.sh', 'macOS y Linux'), ('render.bat', 'Windows'), ('check.py', 'Python, en cualquiera')):
        x, y = pos[name]
        s += '  ' + txt(x + 150, y + 5, what, 12.5, 400, FAINT) + '\n'
    return s + '</svg>\n'


FIGS['skCarpeta'] = sk_carpeta

FIGS['skSkillMd'] = lambda: frame(dict(
    id='skSkillMd',
    title='Las partes de <tspan class="mono">SKILL.md</tspan>',
    title_plain='Las partes de SKILL.md',
    desc='El archivo SKILL.md empieza con un bloque entre dos líneas de tres guiones, con name y description. Después va el cuerpo en Markdown, con los pasos que sigue el agente.',
    sub='Arriba, entre las dos líneas de guiones, los datos de la skill. Debajo, las instrucciones.',
    file='.agents/skills/mer-svg/SKILL.md',
    code=['---',
          'name: mer-svg',
          'description: Dibuja el MER de la app en SVG.',
          '  Úsala cuando pidan el diagrama de datos.',
          '---',
          '',
          '# MER en SVG',
          '',
          '## Pasos',
          '',
          '1. Lee docs/modelo.md.',
          '2. Lee references/estilo.md.',
          '3. Escribe el resultado en docs/mer.svg.'],
    panel='QUÉ ES CADA PARTE',
    min_h=376,
    result=(note(16, 'indigo', 'name', ['Igual al nombre de la carpeta.', 'Minúsculas y guiones.'], 68)
            + note(100, 'amber', 'description', ['Qué hace y cuándo usarla.', 'El agente decide con esto.'], 68)
            + note(212, 'teal', 'El cuerpo', ['Los pasos, en orden.', 'Nombra los archivos que debe leer.'], 68)),
    arrows=[dict(line=1, find='name', to=(16, 50), color='indigo', lane=0),
            dict(line=2, find='description', to=(16, 134), color='amber', lane=1),
            dict(line=8, find='## Pasos', to=(16, 246), color='teal', lane=0)],
))


def sk_carga():
    fid = 'skCarga'
    h = 396
    s = head(fid, h, 'El agente no lee toda la skill de entrada', 'El agente no lee toda la skill de entrada',
             'Carga cada parte solo cuando la necesita. Así una skill larga no gasta contexto si no se usa.',
             'Tres momentos. Uno, siempre: el agente tiene en su contexto el name y la description de cada skill instalada. Dos, cuando tu pedido coincide con una description: abre el SKILL.md de esa skill. Tres, solo si un paso lo pide: abre los archivos de references y assets.')
    cols = [('slate', 'Siempre', 'name y description', ['De cada skill instalada.', 'Unas pocas líneas.']),
            ('violet', 'Si tu pedido coincide', 'SKILL.md', ['Los pasos y las reglas', 'de esa skill.']),
            ('teal', 'Si un paso lo pide', 'references/ y assets/', ['El detalle y los ejemplos,', 'archivo por archivo.'])]
    for i, (c, when, what, body) in enumerate(cols):
        x = 48 + i * 296
        strong = FAM[c][2]
        s += '  ' + box(x, 120, 272, 168, c) + '\n'
        s += '  ' + chip(x + 30, 150, i + 1, c) + '\n'
        s += '  ' + txt(x + 52, 155, when, 14, 700, strong, fit=200) + '\n'
        s += '  ' + txt(x + 20, 198, what, 15, 700, INK, cls='mono', fit=236) + '\n'
        for j, b in enumerate(body):
            s += '  ' + txt(x + 20, 228 + j * 20, b, 13, 400, '#454C61', fit=236) + '\n'
        if i < 2:
            s += f'  <path class="link" d="M{x + 272},204 H{x + 290}"/>\n'
    s += '  ' + callout(312, '<tspan font-weight="700">La description decide:</tspan> es lo único que el agente lee para saber si usa la skill.') + '\n'
    return s + '</svg>\n'


FIGS['skCarga'] = sk_carga


# ───────────────────────────── S0032 · Taller · Tu primera skill

def ts_flujo():
    fid = 'tsFlujo'
    h = 348
    s = head(fid, h, 'Lo que vas a armar', 'Lo que vas a armar',
             'Tú escribes las tablas en texto y la skill. El agente escribe el diagrama.',
             'Tres cajas en fila. docs/modelo.md, las tablas de tu app en texto, que escribes tú. La skill mer-svg, con las medidas, los colores y un ejemplo, que el agente lee. Y docs/mer.svg, el diagrama, que escribe el agente.')
    cols = [('amber', 'docs/modelo.md', 'Tus tablas, en texto.', 'Lo escribes tú.'),
            ('violet', 'mer-svg', 'Medidas, colores y un ejemplo.', 'La armas tú, una vez.'),
            ('teal', 'docs/mer.svg', 'El diagrama.', 'Lo escribe el agente.')]
    for i, (c, name, a, b) in enumerate(cols):
        x = 48 + i * 312
        s += '  ' + box(x, 124, 240, 116, c, strong=(i == 2)) + '\n'
        s += '  ' + txt(x + 20, 158, name, 15, 700, FAM[c][2], cls='mono', fit=200) + '\n'
        s += '  ' + txt(x + 20, 188, a, 13, 400, INK, fit=200) + '\n'
        s += '  ' + txt(x + 20, 212, b, 13, 700, FAM[c][2], fit=200) + '\n'
    s += '  <path class="link" d="M288,182 H352"/>\n  <path class="link" d="M600,182 H664"/>\n'
    s += '  ' + txt(320, 170, 'lee', 12, 600, MUTED, 'middle') + '\n'
    s += '  ' + txt(632, 170, 'escribe', 12, 600, MUTED, 'middle') + '\n'
    s += '  ' + callout(264, '<tspan font-weight="700">Si el diagrama sale mal,</tspan> se corrige el modelo o la skill y se pide otra vez. El SVG no se toca a mano.') + '\n'
    return s + '</svg>\n'


FIGS['tsFlujo'] = ts_flujo

FIGS['tsUso'] = lambda: console(dict(
    id='tsUso',
    title='Pedir el diagrama',
    title_plain='Pedir el diagrama',
    desc='Se le pide al agente que dibuje el MER de la app. El agente carga la skill mer-svg, lee docs/modelo.md, el estilo y el ejemplo de la skill, y escribe docs/mer.svg.',
    sub='El pedido no nombra la skill. El agente la elige por su description.',
    term_title='Terminal · C:\\develop\\mi_app_1',
    lines=[('O', '> Dibuja el MER de la app'),
           ('B', ''),
           ('O', '→ Skill "mer-svg"'),
           ('D', '→ Read docs/modelo.md'),
           ('D', '→ Read .agents/skills/mer-svg/references/estilo.md'),
           ('D', '→ Read .agents/skills/mer-svg/assets/ejemplo.svg'),
           ('O', '← Write docs/mer.svg'),
           ('B', ''),
           ('K', 'Listo: docs/mer.svg con 4 tablas y 3 relaciones.')],
    rings=[(2, 0, 17, 1), (4, 0, 50, 2), (6, 0, 20, 3)],
    cards=[(1, 'Eligió la skill', ['La encontró por su', 'description.'], False),
           (2, 'Leyó lo que la skill pide', ['El modelo, el estilo', 'y el ejemplo.'], False),
           (3, 'Escribió el archivo', ['Ábrelo en Chrome', 'para verlo.'], False)],
))


def embedded(path, old_id, new_id):
    src = (ROOT / path).read_text(encoding='utf-8').replace(old_id, new_id)
    src = src.replace(f'<svg id="{new_id}" ', f'<svg id="{new_id}" width="100%" style="max-width:960px;display:block;margin:0 auto" ', 1)
    return src if src.endswith('\n') else src + '\n'


def ts_resultado():
    return embedded('recursos/sesion4/docs/mer.svg', 'merRed', 'tsResultado')


FIGS['tsPrimerIntento'] = lambda: embedded('recursos/sesion4/docs/mer-primer-intento.svg', 'merApp', 'tsPrimerIntento')


FIGS['tsResultado'] = ts_resultado


TS_FILES = [('SKILL.md', 4, None), ('estilo.md', 5, 'references/'), ('ejemplo.svg', 5, 'assets/')]


def ts_nodes(step):
    """Árbol de la skill tras el paso `step` (1 = carpetas, 2 a 4 = un archivo más). El último elemento va como nuevo."""
    fresh = step == 1
    nodes = [(0, 'mi_app_1/', 'd', False), (1, '.agents/', 'd', fresh), (2, 'skills/', 'd', fresh), (3, 'mer-svg/', 'd', fresh)]
    for i, (name, depth, folder) in enumerate(TS_FILES):
        if i == 0:
            if step >= 2:
                nodes.append((depth, name, 'f', step == 2))
            continue
        nodes.append((4, folder, 'd', fresh))
        if step >= i + 2:
            nodes.append((depth, name, 'f', step == i + 2))
    return nodes


def ts_estructura():
    fid = 'tsEstructura'
    nodes = [(d, n, k, False) for d, n, k, _ in ts_nodes(4)]
    h = 140 + (len(nodes) - 1) * 36 + 56
    s = head(fid, h, 'La skill completa', 'La skill completa',
             'Esto es lo que vas a tener al final. Se arma en cuatro pasos, uno por elemento.',
             'El árbol de la skill dentro de mi_app_1: las carpetas .agents, skills y mer-svg, que se crean en el paso 1 junto con references y assets; el archivo SKILL.md, del paso 2; references/estilo.md, del paso 3; y assets/ejemplo.svg, del paso 4.')
    t, pos = tree(nodes)
    s += '  ' + t + '\n'
    marks = [('mer-svg/', 1, 'Las carpetas', 'indigo'), ('SKILL.md', 2, 'Las instrucciones', 'violet'),
             ('estilo.md', 3, 'Las medidas y los colores', 'teal'), ('ejemplo.svg', 4, 'Un diagrama terminado', 'amber')]
    for name, n, label, c in marks:
        x, y = pos[name]
        s += '  ' + chip(540, y, n, c) + '\n'
        s += '  ' + txt(562, y + 4.5, f'<tspan font-weight="700" fill="{FAM[c][2]}">Paso {n}.</tspan> {label}', 13.5, 400, '#454C61', fit=340) + '\n'
    return s + '</svg>\n'


FIGS['tsEstructura'] = ts_estructura


def ts_paso(step):
    fid = f'tsPaso{step}'
    title = {1: 'Paso 1 · Las carpetas', 2: 'Paso 2 · SKILL.md', 3: 'Paso 3 · references/estilo.md',
             4: 'Paso 4 · assets/ejemplo.svg'}[step]
    sub = {1: 'Cinco carpetas vacías. El punto de .agents es parte del nombre.',
           2: 'El único archivo obligatorio. Va directamente dentro de mer-svg.',
           3: 'Lo que el agente consulta. Va dentro de references.',
           4: 'Lo que el agente imita. Va dentro de assets.'}[step]
    desc = {1: 'El árbol de mi_app_1 con cinco carpetas nuevas: .agents, dentro skills, dentro mer-svg, y dentro de mer-svg las carpetas references y assets.',
            2: 'El mismo árbol, con un archivo nuevo dentro de mer-svg: SKILL.md.',
            3: 'El mismo árbol, con un archivo nuevo dentro de references: estilo.md.',
            4: 'El mismo árbol, con un archivo nuevo dentro de assets: ejemplo.svg. La skill está completa.'}[step]
    nodes = ts_nodes(step)
    h = 140 + (len(nodes) - 1) * 36 + 56
    s = head(fid, h, title, title, sub, desc)
    t, _ = tree(nodes, badge_x=480)
    return s + '  ' + t + '\n</svg>\n'


for _n in (1, 2, 3, 4):
    FIGS[f'tsPaso{_n}'] = (lambda n: lambda: ts_paso(n))(_n)


def ts_modelo():
    fid = 'tsModelo'
    h = 536
    s = head(fid, h, 'De la descripción al modelo', 'De la descripción al modelo',
             'Se parte de contar la app en dos frases. Los sustantivos son las tablas.',
             'Arriba, la descripción de la red profesional. De sus sustantivos salen cuatro tablas: usuarios, publicaciones, seguidores y mensajes. Abajo, tres pasadas para escribir el modelo: una lista por tabla con su llave primaria y sus atributos, las llaves foráneas en la tabla del lado muchos, y las relaciones escritas como frases.')
    s += '  <rect x="48" y="112" width="864" height="76" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
    b = 'font-weight="700" fill="#161A26"'
    s += '  ' + txt(68, 143, f'Cada <tspan {b}>usuario</tspan> tiene un perfil con su cargo y su ciudad, y escribe <tspan {b}>publicaciones</tspan> sobre su trabajo.', 14, 400, '#454C61', fit=820) + '\n'
    s += '  ' + txt(68, 169, f'Sigue a otras personas, que pasan a tenerlo entre sus <tspan {b}>seguidores</tspan>, y les envía <tspan {b}>mensajes</tspan>.', 14, 400, '#454C61', fit=820) + '\n'
    s += '  <path class="link" d="M480,188 V214"/>\n'
    names = [('usuarios', 'indigo'), ('publicaciones', 'teal'), ('seguidores', 'amber'), ('mensajes', 'violet')]
    for i, (n, c) in enumerate(names):
        x = 48 + i * 222
        soft, border, strong = FAM[c]
        s += f'  <rect x="{x}" y="224" width="198" height="36" rx="18" fill="{soft}" stroke="{border}" stroke-width="1.5"/>\n'
        s += '  ' + txt(x + 99, 247, n, 13.5, 700, strong, 'middle', cls='mono') + '\n'
    cards = [('teal', 232, 'Una lista por tabla', ['## publicaciones', '- id (PK)', '- texto', '- fecha'], 'Primero la llave primaria.', True),
             ('indigo', 296, 'Las llaves foráneas', ['- usuario_id (FK a usuarios)', '- emisor_id (FK a usuarios)'], 'Van en la tabla del lado "muchos".', True),
             ('amber', 304, 'Las relaciones, en frases', ['- Un usuario tiene muchos mensajes.', '- Un usuario tiene muchos seguidores.'], 'Una frase por cada relación.', False)]
    x = 48
    for i, (c, w, title, lines, foot, mono) in enumerate(cards):
        strong = FAM[c][2]
        s += '  ' + box(x, 292, w, 212, c) + '\n'
        s += '  ' + chip(x + 30, 322, i + 1, c) + '\n'
        s += '  ' + txt(x + 52, 327, title, 14, 700, strong, fit=w - 72) + '\n'
        s += f'  <rect x="{x + 16}" y="346" width="{w - 32}" height="108" rx="8" fill="#FFFFFF" stroke="{FAM[c][1]}" stroke-width="1"/>\n'
        for j, ln in enumerate(lines):
            s += '  ' + txt(x + 28, 372 + j * 22, ln, 12, 400, INK, cls='mono' if mono else '', fit=w - 52) + '\n'
        s += '  ' + txt(x + 20, 482, foot, 12.5, 400, '#454C61', fit=w - 36) + '\n'
        x += w + 16
    return s + '</svg>\n'


FIGS['tsModelo'] = ts_modelo


def ts_ejemplo():
    return embedded('recursos/sesion4/.agents/skills/mer-svg/assets/ejemplo.svg', 'merEjemplo', 'tsEjemplo')


FIGS['tsEjemplo'] = ts_ejemplo


def ts_carpetas():
    fid = 'tsCarpetas'
    h = 566
    s = head(fid, h, 'Tu proyecto al terminar', 'Tu proyecto al terminar',
             'Nada de lib/ cambió. Lo nuevo es lo que dirige al agente y lo que el agente produjo.',
             'El árbol de mi_app_1 al terminar el taller. Son nuevos la carpeta .agents con la skill mer-svg y sus tres archivos, SKILL.md, estilo.md y ejemplo.svg; la carpeta docs con modelo.md y mer.svg; y en la raíz AGENTS.md. La carpeta lib queda igual.')
    nodes = [(0, 'mi_app_1/', 'd', False), (1, '.agents/', 'd', False), (2, 'skills/', 'd', False),
             (3, 'mer-svg/', 'd', False), (4, 'SKILL.md', 'f', True), (4, 'references/estilo.md', 'f', True),
             (4, 'assets/ejemplo.svg', 'f', True), (1, 'docs/', 'd', False), (2, 'modelo.md', 'f', True),
             (2, 'mer.svg', 'f', True), (1, 'lib/', 'd', False), (1, 'AGENTS.md', 'f', True)]
    t, pos = tree(nodes, step=34, badge_x=520)
    s += '  ' + t + '\n'
    x, y = pos['lib/']
    s += '  ' + txt(x + 80, y + 5, 'sin cambios', 12.5, 400, FAINT) + '\n'
    return s + '</svg>\n'


FIGS['tsCarpetas'] = ts_carpetas


# ───────────────────────────── S0033 · Una skill para armar pantallas

def fp_carpeta():
    fid = 'fpCarpeta'
    nodes = [(0, 'mi_app_1/', 'd', False), (1, '.agents/', 'd', False), (2, 'skills/', 'd', False),
             (3, 'mer-svg/', 'd?', False), (3, 'flutter-pantallas/', 'd', True), (4, 'SKILL.md', 'f', True),
             (4, 'references/', 'd', True), (5, 'widgets.md', 'f', True), (4, 'assets/', 'd', True),
             (5, 'component.dart', 'f', True), (5, 'screen.dart', 'f', True)]
    h = 140 + (len(nodes) - 1) * 40 + 52
    s = head(fid, h, 'La segunda skill del proyecto', 'La segunda skill del proyecto',
             'Va junto a mer-svg, en la misma carpeta skills. Cuatro archivos.',
             'El árbol de mi_app_1: dentro de .agents y skills, junto a la skill mer-svg que ya existe, la carpeta nueva flutter-pantallas con SKILL.md, que son los pasos; references con widgets.md, que es la paleta; y assets con dos plantillas, component.dart y screen.dart.')
    t, pos = tree(nodes, step=40, badge_x=470)
    s += '  ' + t + '\n'
    notes = [('SKILL.md', 'indigo', 'Los pasos', 'Cómo se arma una pantalla.'),
             ('widgets.md', 'teal', 'La paleta', 'Los únicos widgets permitidos.'),
             ('component.dart', 'amber', 'Plantilla', 'Cómo se escribe un componente.'),
             ('screen.dart', 'amber', 'Plantilla', 'Cómo se escribe una pantalla.')]
    for name, c, title, body in notes:
        x, y = pos[name]
        soft, border, strong = FAM[c]
        s += f'  <rect x="552" y="{y - 17}" width="360" height="34" rx="10" fill="{soft}" stroke="{border}" stroke-width="1.5"/>\n'
        s += ('  ' + txt(570, y + 4.5, f'<tspan font-weight="700" fill="{strong}">{title}.</tspan> {body}', 13, 400, '#454C61', fit=330) + '\n')
    return s + '</svg>\n'


FIGS['fpCarpeta'] = fp_carpeta


def fp_paleta():
    fid = 'fpPaleta'
    groups = [('CONTENIDO', 'indigo', ['Text', 'Icon', 'Image', 'CircleAvatar']),
              ('BOTONES', 'violet', ['ElevatedButton', 'OutlinedButton', 'TextButton', 'IconButton']),
              ('ENTRADA', 'amber', ['TextField']),
              ('ACOMODAR', 'teal', ['Column', 'Row', 'SizedBox', 'Expanded', 'Spacer', 'Padding', 'Container', 'Card',
                                    'Center', 'SingleChildScrollView']),
              ('ESTRUCTURA', 'slate', ['Scaffold', 'SafeArea', 'AppBar', 'BottomNavigationBar', 'FloatingActionButton']),
              ('FUERA', 'rose', ['ListView', 'GridView', 'Stack', 'ListTile', 'StatefulWidget', 'Navigator', 'paquetes nuevos'])]
    body, y = '', 128
    for label, c, items in groups:
        soft, border, strong = FAM[c]
        out = c == 'rose'
        if out:
            y += 10
            body += f'  <path d="M48,{y - 14} H912" stroke="#D9DEE8" stroke-width="1.5" stroke-dasharray="4 5"/>\n'
            y += 12
        body += '  ' + txt(48, y + 5, label, 12, 700, strong, cls='h') + '\n'
        x = 176
        for it in items:
            w = round(len(it) * 8.1 + 26)
            if x + w > 912:
                x, y = 176, y + 40
            dash = ' stroke-dasharray="5 4"' if out else ''
            body += f'  <rect x="{x}" y="{y - 15}" width="{w}" height="30" rx="15" fill="{soft}" stroke="{border}" stroke-width="1.5"{dash}/>\n'
            body += '  ' + txt(x + w / 2, y + 4.5, it, 13, 600, strong, 'middle', cls='' if it == 'paquetes nuevos' else 'mono') + '\n'
            x += w + 8
        y += 48
    h = y + 36
    s = head(fid, h, 'La paleta de widgets', 'La paleta de widgets',
             'Lo que has visto hasta la sesión 3. El agente arma las pantallas solo con esto.',
             'Los widgets permitidos, en cinco grupos. Contenido: Text, Icon, Image y CircleAvatar. Botones: ElevatedButton, OutlinedButton, TextButton e IconButton. Entrada: TextField. Acomodar: Column, Row, SizedBox, Expanded, Spacer, Padding, Container, Card, Center y SingleChildScrollView. Estructura: Scaffold, SafeArea, AppBar, BottomNavigationBar y FloatingActionButton. Fuera de la paleta por ahora: ListView, GridView, Stack, ListTile, StatefulWidget, Navigator y cualquier paquete nuevo.')
    s = s.replace(f'#{fid} .h{{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}}',
                  f'#{fid} .h{{font-size:12px;font-weight:700;letter-spacing:.08em}}')
    s += body
    s += '  ' + txt(48, h - 26, 'Lo de abajo no está prohibido para siempre: entra a la paleta cuando lo veas en clase.', 13, 400, '#454C61', fit=860) + '\n'
    return s + '</svg>\n'


FIGS['fpPaleta'] = fp_paleta


def fp_componentes():
    fid = 'fpComponentes'
    h = 560
    s = head(fid, h, 'Un componente, cinco usos', 'Un componente, cinco usos',
             'La pantalla de mensajes que armó el agente: no escribió nada nuevo para las filas, reutilizó ChatItem.',
             'Un celular con la pantalla Mensajes: cinco filas de conversación, cada una con avatar, nombre, último mensaje y hora. Las cinco salen del mismo componente, ChatItem, que vive en lib/components/chat_item.dart y recibe cuatro datos: image, name, message y time. La pantalla solo las acomoda en una Column.')
    rows = [('Javier Montes', 'Perfecto, quedamos mañana…', '10:24'), ('Mariana Valenzuela', 'Gracias por los comentarios…', '9:05'),
            ('Ana Torres', '¿Pudiste revisar el docu…', 'Ayer'), ('Carlos Restrepo', 'Listo, reviso el presupu…', 'Mar'),
            ('Lucía Fernández', '¡Felicitaciones por el…', 'Lun')]
    inner = '<rect width="220" height="46" fill="#F1ECF8"/>' + txt(16, 29, 'Mensajes', 15, 500)
    for i, (n, m, tm) in enumerate(rows):
        y = 62 + i * 58
        inner += (f'<circle cx="28" cy="{y + 22}" r="14" fill="#C9A6EE"/>' + txt(50, y + 18, n, 11.5, 700)
                  + txt(50, y + 33, m, 10, 400, MUTED) + txt(208, y + 18, tm, 9.5, 400, MUTED, 'end')
                  + mark(6, y, 208, 46, 'teal', 8))
    s += '  ' + device(96, 132, 220, 370, inner, '#FFFFFF', f'{fid}-a') + '\n'
    for i in range(5):
        y = 132 + 62 + i * 58 + 23
        s += f'  <path d="M324,{y} C420,{y} 440,300 512,300" fill="none" stroke="{FAM["teal"][1]}" stroke-width="1.75"/>\n'
    s += '  ' + box(520, 172, 392, 256, 'teal', strong=True) + '\n'
    s += '  ' + txt(544, 208, 'ChatItem', 18, 700, FAM['teal'][2], cls='mono') + '\n'
    s += '  ' + txt(544, 230, 'lib/components/chat_item.dart', 12.5, 400, MUTED, cls='mono', fit=340) + '\n'
    s += '  ' + txt(544, 268, 'Se escribe una vez. Lo que cambia en cada fila', 13.5, 400, INK, fit=344) + '\n'
    s += '  ' + txt(544, 288, 'llega por el constructor:', 13.5, 400, INK, fit=344) + '\n'
    for i, par in enumerate(('image', 'name', 'message', 'time')):
        x = 544 + i * 88
        s += f'  <rect x="{x}" y="308" width="80" height="30" rx="15" fill="#FFFFFF" stroke="{FAM["teal"][1]}" stroke-width="1.5"/>\n'
        s += '  ' + txt(x + 40, 327.5, par, 12.5, 600, FAM['teal'][2], 'middle', cls='mono') + '\n'
    s += '  ' + txt(544, 376, 'La pantalla no dibuja filas: las acomoda', 13.5, 400, INK, fit=344) + '\n'
    s += '  ' + txt(544, 396, 'en una Column y les pasa sus datos.', 13.5, 400, INK, fit=344) + '\n'
    return s + '</svg>\n'


FIGS['fpComponentes'] = fp_componentes

FIGS['fpUso'] = lambda: console(dict(
    id='fpUso',
    title='Pedir una pantalla',
    title_plain='Pedir una pantalla',
    desc='Se le pide al agente la pantalla de mensajes. El agente lee los componentes que ya existen, carga la skill flutter-pantallas, lee la paleta y las plantillas, escribe la pantalla nueva y edita main.dart para registrarla.',
    sub='Una sesión real, recortada. Primero mira lo que ya hay, después carga la skill.',
    term_title='Terminal · C:\\develop\\mi_app_1',
    lines=[('O', '> Crea la pantalla de mensajes con la lista de conversaciones'),
           ('B', ''),
           ('D', '→ Read lib/components/chat_item.dart'),
           ('O', '→ Skill "flutter-pantallas"'),
           ('D', '→ Read .agents/skills/flutter-pantallas/references/widgets.md'),
           ('D', '→ Read .agents/skills/flutter-pantallas/assets/screen.dart'),
           ('O', '← Write lib/screens/messages_screen.dart'),
           ('O', '← Edit lib/main.dart'),
           ('B', ''),
           ('K', 'Listo: MessagesScreen reutiliza ChatItem. Sin errores en lib/.')],
    rings=[(2, 0, 36, 1), (3, 0, 27, 2), (6, 0, 40, 3)],
    cards=[(1, 'Miró lo que ya había', ['Encontró un componente', 'que servía.'], False),
           (2, 'Cargó la skill', ['Y con ella, la paleta', 'y las plantillas.'], False),
           (3, 'Un solo archivo nuevo', ['La pantalla. Ningún', 'componente repetido.'], False)],
))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--inject':
        done = set()
        for name in LESSONS:
            path = ROOT / 'content' / name
            text = path.read_text(encoding='utf-8')

            def swap(m):
                done.add(m.group(1))
                return '```svg\n' + FIGS[m.group(1)]() + '```'
            new = re.sub(r'```svg\n<svg id="(\w+)".*?```', swap, text, flags=re.S)
            path.write_text(new, encoding='utf-8')
        missing = set(FIGS) - done
        print('inyectadas:', len(done), '· sin usar:', sorted(missing) or 'ninguna')
        return
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    only = sys.argv[2:]
    for fid, fn in FIGS.items():
        if only and fid not in only:
            continue
        (out / f'{fid}.svg').write_text(fn(), encoding='utf-8')
    print(len(FIGS), 'figuras en', out)


if __name__ == '__main__':
    main()
