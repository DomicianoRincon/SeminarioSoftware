"""Figuras SVG de las lecciones de la sesión 3 (S0020 a S0028).

    python3 tools/sesion3_figuras.py <carpeta>     escribe un .svg por figura, para revisarlas
    python3 tools/sesion3_figuras.py --inject      reemplaza cada bloque ```svg de content/lessonS2[0-8].md
                                                   por la figura con el mismo id
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from code_frame import frame  # noqa: E402
from sesion2_figuras import FAM, MAIL, MONO, PH_, PW_, PX0, PY0, avatar, head, phone  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
INK, MUTED, FAINT = '#161A26', '#556074', '#79809A'

FIGS = {}


def txt(x, y, s, size=13, weight=400, fill=INK, anchor='start', cls='', fit=None):
    extra = f' class="{cls}"' if cls else ''
    extra += f' data-fit="{fit}"' if fit else ''
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{extra}>{s}</text>')


def mark(x, y, w, h, color, rx=10):
    strong = FAM[color][2]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{strong}" fill-opacity=".08" '
            f'stroke="{strong}" stroke-width="2"/>')


def device(x, y, w, h, inner, fill='#FFFFFF', cid=None):
    """Celular: marco oscuro y pantalla recortada. `inner` usa coordenadas de la pantalla."""
    clip = f'<clipPath id="{cid}"><rect width="{w}" height="{h}" rx="20"/></clipPath>' if cid else ''
    attr = f' clip-path="url(#{cid})"' if cid else ''
    return (f'{clip}<rect x="{x-7}" y="{y-7}" width="{w+14}" height="{h+14}" rx="27" fill="#1F2430"/>'
            f'<g transform="translate({x},{y})"><g{attr}><rect width="{w}" height="{h}" rx="20" fill="{fill}"/>'
            f'{inner}</g></g>')


# ───────────────────────────── S0020 · Scaffold


def sf_sin_scaffold():
    fid = 'sfSinScaffold'
    h = 560
    s = head(fid, h, 'El mismo <tspan class="mono">Text</tspan>, sin y con <tspan class="mono">Scaffold</tspan>',
             'El mismo Text, sin y con Scaffold',
             'Un texto suelto no es una pantalla. Scaffold le pone el fondo, el estilo y un lugar a cada parte.',
             'Dos celulares. En el de la izquierda, un Text suelto: letras rojas con subrayado amarillo sobre fondo negro. En el de la derecha, el mismo texto dentro de un Scaffold: fondo claro, una barra con el título Inicio y el texto en el centro.')
    left = ('<text x="14" y="40" font-size="26" font-weight="400" fill="#E53935">Pantalla</text>'
            '<path d="M14,46 H112 M14,50 H112" stroke="#FFEB3B" stroke-width="1.5"/>')
    right = ('<rect width="220" height="52" fill="#F1ECF8"/>'
             + txt(18, 31, 'Inicio', 17, 500)
             + txt(110, 196, 'Pantalla', 14, 400, INK, 'middle'))
    s += '  ' + device(150, 132, 220, 330, left, '#000000', f'{fid}-a') + '\n'
    s += '  ' + device(590, 132, 220, 330, right, '#FFFFFF', f'{fid}-b') + '\n'
    s += f'  <path class="link" d="M400,297 H560"/>\n'
    s += '  ' + txt(480, 285, 'dentro de un Scaffold', 12.5, 600, MUTED, 'middle', fit=150) + '\n'
    s += '  ' + txt(260, 502, 'Un Text suelto', 15, 700, INK, 'middle') + '\n'
    s += '  ' + txt(260, 524, 'Sin fondo, sin estilo de letra, sin barra.', 13, 400, MUTED, 'middle', fit=330) + '\n'
    s += '  ' + txt(700, 502, 'El mismo Text en el body de un Scaffold', 15, 700, INK, 'middle', fit=380) + '\n'
    s += '  ' + txt(700, 524, 'Fondo, letra del tema y barra con título.', 13, 400, MUTED, 'middle', fit=330) + '\n'
    return s + '</svg>\n'


FIGS['sfSinScaffold'] = sf_sin_scaffold


def sf_partes_result():
    o = '<rect x="78" y="22" width="204" height="396" rx="26" fill="#F0F1F4" stroke="#2A3040" stroke-width="3"/>'
    o += mark(84, 28, 192, 384, 'indigo', 20)
    o += mark(92, 44, 176, 54, 'amber', 12)
    o += txt(108, 71, 'Perfil', 17, 500).replace('<text ', '<text dy="0.35em" ')
    o += mark(92, 106, 176, 298, 'green', 12)
    o += txt(180, 220, 'Contenido', 13.5, 400, INK, 'middle')
    o += '<rect x="212" y="346" width="48" height="48" rx="14" fill="#FFEBEF" stroke="#C2354F" stroke-width="2"/>'
    o += '<path d="M236,360 V380 M226,370 H246" stroke="#C2354F" stroke-width="2.5" stroke-linecap="round"/>'
    return o


FIGS['sfPartes'] = lambda: frame(dict(
    id='sfPartes',
    title='Los lugares de un <tspan class="mono">Scaffold</tspan>',
    title_plain='Los lugares de un Scaffold',
    desc='Un Scaffold con backgroundColor, appBar, body y floatingActionButton, junto a la pantalla que produce: el color de fondo cubre toda la pantalla, la barra queda arriba, el contenido ocupa el resto y el botón flotante queda abajo a la derecha.',
    sub='Cada propiedad es un lugar fijo de la pantalla. Tú decides qué widget va en cada uno.',
    file='lib/screens/profile_screen.dart',
    panel='RESULTADO',
    min_h=472,
    code=[
        "return Scaffold(",
        "  backgroundColor: Colors.grey.shade100,",
        "  appBar: AppBar(title: const Text('Perfil')),",
        "  body: const Center(",
        "    child: Text('Contenido'),",
        "  ),",
        "  floatingActionButton: FloatingActionButton(",
        "    onPressed: () {",
        "      print('Nuevo');",
        "    },",
        "    child: const Icon(Icons.add),",
        "  ),",
        ");",
    ],
    result=sf_partes_result(),
    arrows=[
        dict(line=1, find='backgroundColor', to=(84, 47), color='indigo'),
        dict(line=2, find='appBar', to=(92, 71), color='amber'),
        dict(line=3, find='body', to=(92, 250), color='green', lane=2),
        dict(line=6, find='floatingActionButton', to=(212, 370), color='rose', lane=0),
    ],
))


def sf_screen():
    fid = 'sfScreen'
    h = 500
    s = head(fid, h, 'Screen y Page', 'Screen y Page',
             'Si tiene Scaffold, es una Screen. Una Page es un pedazo de pantalla que una Screen hospeda.',
             'Dos celulares. El de la izquierda es una Screen: un Scaffold completo, con su barra y su contenido, en lib/screens. El de la derecha muestra una Page: solo la zona de contenido, sin Scaffold, dentro de una Screen que tiene una barra de navegación abajo; vive en lib/pages y se ve en la sesión 9.')
    bar = '<rect width="180" height="44" fill="#F1ECF8"/>'
    lines = ''.join(f'<rect x="20" y="{y}" width="{w}" height="10" rx="5" fill="#D9DEE8"/>'
                    for y, w in ((70, 140), (92, 110), (114, 126), (160, 140), (182, 90)))
    left = bar + txt(16, 27, 'Perfil', 15, 500) + lines + mark(3, 3, 174, 294, 'indigo', 18)
    nav = ('<rect y="252" width="180" height="48" fill="#F1ECF8"/>'
           + ''.join(f'<circle cx="{cx}" cy="276" r="7" fill="{c}"/>' for cx, c in ((36, '#7439B8'), (90, '#C4CBD8'), (144, '#C4CBD8'))))
    right = (bar + txt(16, 27, 'Inicio', 15, 500) + nav + lines
             + '<rect x="6" y="50" width="168" height="196" rx="10" fill="#0F8478" fill-opacity=".08" stroke="#0F8478" stroke-width="2" stroke-dasharray="6 4"/>')
    s += '  ' + device(88, 136, 180, 300, left, '#FFFFFF', f'{fid}-a') + '\n'
    s += '  ' + device(536, 136, 180, 300, right, '#FFFFFF', f'{fid}-b') + '\n'

    def col(x, color, name, path, facts):
        strong = FAM[color][2]
        o = '  ' + txt(x, 152, name, 17, 700, strong, cls='mono', fit=180) + '\n'
        o += '  ' + txt(x, 176, path, 12.5, 400, MUTED, cls='mono', fit=180) + '\n'
        for i, (a, b) in enumerate(facts):
            y = 222 + i * 62
            o += '  ' + txt(x, y, a, 14, 700, INK, fit=180) + '\n'
            o += '  ' + txt(x, y + 20, b, 13, 400, MUTED, fit=180) + '\n'
        return o
    s += col(300, 'indigo', 'ProfileScreen', 'lib/screens/',
             [('Tiene Scaffold', 'Es la pantalla entera.'), ('Se abre por su ruta', 'Está en routes.'),
              ('Desde hoy', 'Todas tus pantallas.')])
    s += col(748, 'teal', 'FeedPage', 'lib/pages/',
             [('No tiene Scaffold', 'Solo el contenido.'), ('La hospeda una Screen', 'No tiene ruta propia.'),
              ('Sesión 9', 'Con la barra de abajo.')])
    s += f'  <path d="M480,128 V444" stroke="#D9DEE8" stroke-width="1.5" stroke-dasharray="4 5"/>\n'
    return s + '</svg>\n'


FIGS['sfScreen'] = sf_screen


# ───────────────────────────── S0021 · SafeArea

TOP, BOTTOM = 36, 24


def system(w, h):
    """Lo que el sistema dibuja encima de la app: hora, cámara, batería y barra de gestos."""
    return (txt(16, 22, '9:41', 11.5, 700)
            + f'<rect x="{w/2-32}" y="7" width="64" height="18" rx="9" fill="#1F2430"/>'
            + f'<rect x="{w-38}" y="11" width="22" height="11" rx="3" fill="none" stroke="{INK}" stroke-width="1.5"/>'
            + f'<rect x="{w-36}" y="13" width="13" height="7" rx="1.5" fill="{INK}"/>'
            + f'<rect x="{w/2-36}" y="{h-12}" width="72" height="5" rx="2.5" fill="#1F2430"/>')


def zone(y, w, h, color):
    soft, border, strong = FAM[color]
    return f'<rect y="{y}" width="{w}" height="{h}" fill="{strong}" fill-opacity=".13"/>'


def sa_zonas():
    fid = 'saZonas'
    h = 540
    w, ph = 220, 344
    s = head(fid, h, 'La pantalla no es toda tuya', 'La pantalla no es toda tuya',
             'El sistema dibuja encima de la app en los bordes. Lo que pongas ahí queda tapado.',
             'Un celular con tres zonas marcadas. Arriba, la barra de estado con la hora, la batería y el recorte de la cámara. Abajo, la barra de gestos. En medio, la zona segura, donde todo se ve y se puede tocar.')
    inner = (zone(0, w, TOP, 'rose') + zone(TOP, w, ph - TOP - BOTTOM, 'green') + zone(ph - BOTTOM, w, BOTTOM, 'rose')
             + f'<path d="M0,{TOP} H{w} M0,{ph-BOTTOM} H{w}" stroke="#FFFFFF" stroke-width="2"/>'
             + txt(w / 2, ph / 2 + 5, 'Zona segura', 15, 700, FAM['green'][2], 'middle')
             + system(w, ph))
    s += '  ' + device(136, 132, w, ph, inner, '#FFFFFF', f'{fid}-a') + '\n'
    rows = [(150, 'rose', 'Barra de estado y cámara', 'La hora, la batería y el recorte de la cámara.'),
            (304, 'green', 'Zona segura', 'Aquí todo se ve completo y se puede tocar.'),
            (464, 'rose', 'Barra de gestos', 'La raya para volver al inicio del teléfono.')]
    for y, color, a, b in rows:
        strong = FAM[color][2]
        s += f'  <path d="M366,{y} H432" stroke="{strong}" stroke-width="1.75"/><circle cx="366" cy="{y}" r="3.5" fill="{strong}"/>\n'
        s += '  ' + txt(448, y - 4, a, 15, 700, strong, fit=440) + '\n'
        s += '  ' + txt(448, y + 17, b, 13, 400, MUTED, fit=440) + '\n'
    s += '  ' + txt(448, 238, 'Las esquinas redondeadas también recortan.', 13, 400, FAINT, fit=440) + '\n'
    return s + '</svg>\n'


FIGS['saZonas'] = sa_zonas


def login_content(w, h, top, bottom, bar=False):
    """Título arriba y botón abajo, pegados a los márgenes que se le den."""
    o = ''
    if bar:
        o += f'<rect width="{w}" height="{TOP + 44}" fill="#F1ECF8"/>' + txt(16, TOP + 28, 'Inicio', 15, 500)
        top = TOP + 44
    o += txt(w / 2, top + 26, 'Bienvenido', 20, 700, INK, 'middle')
    o += txt(w / 2, top + 48, 'Inicia sesión para continuar', 12, 400, MUTED, 'middle')
    o += f'<rect x="16" y="{h - bottom - 40}" width="{w - 32}" height="40" rx="20" fill="#2196F3"/>'
    o += txt(w / 2, h - bottom - 15, 'Entrar', 14, 600, '#FFFFFF', 'middle')
    return o


def sa_casos():
    fid = 'saCasos'
    h = 556
    w, ph = 200, 300
    s = head(fid, h, 'Tres pantallas con el mismo contenido', 'Tres pantallas con el mismo contenido',
             'Un título arriba y un botón abajo. Lo que cambia es qué los protege de los bordes.',
             'Tres celulares con un título arriba y un botón abajo. En el primero, sin AppBar ni SafeArea, la cámara tapa el título y la barra de gestos queda encima del botón. En el segundo, con AppBar, el título ya se ve pero el botón sigue tapado. En el tercero, con SafeArea, todo queda dentro de la zona segura.')
    cases = [(80, login_content(w, ph, 0, 0), 'rose', 'Sin AppBar ni SafeArea', 'La cámara tapa el título', 'y los gestos, el botón.'),
             (380, login_content(w, ph, 0, 0, bar=True), 'amber', 'Con AppBar', 'Arriba ya está resuelto.', 'El botón sigue tapado.'),
             (680, login_content(w, ph, TOP, BOTTOM), 'green', 'Con SafeArea', 'Todo queda dentro', 'de la zona segura.')]
    for i, (x, inner, color, a, b, c) in enumerate(cases):
        strong = FAM[color][2]
        s += '  ' + device(x, 132, w, ph, inner + system(w, ph), '#FFFFFF', f'{fid}-{i}') + '\n'
        s += '  ' + txt(x + w / 2, 476, a, 15, 700, strong, 'middle', fit=280) + '\n'
        s += '  ' + txt(x + w / 2, 498, b, 13, 400, MUTED, 'middle', fit=280) + '\n'
        s += '  ' + txt(x + w / 2, 516, c, 13, 400, MUTED, 'middle', fit=280) + '\n'
    return s + '</svg>\n'


FIGS['saCasos'] = sa_casos


def sa_codigo_result():
    w, ph = 204, 380
    inner = (zone(0, w, TOP, 'rose') + zone(ph - BOTTOM, w, BOTTOM, 'rose')
             + txt(w / 2, 82, 'Bienvenido', 20, 700, INK, 'middle')
             + txt(w / 2, 106, 'Inicia sesión para continuar', 12, 400, MUTED, 'middle')
             + system(w, ph))
    o = (f'<rect x="78" y="22" width="{w}" height="{ph}" rx="26" fill="#FFFFFF" stroke="#2A3040" stroke-width="3"/>'
         f'<clipPath id="saCodigo-scr"><rect width="{w}" height="{ph}" rx="26"/></clipPath>'
         f'<g transform="translate(78,22)" clip-path="url(#saCodigo-scr)">{inner}</g>'
         f'<rect x="78" y="22" width="{w}" height="{ph}" rx="26" fill="none" stroke="#2A3040" stroke-width="3"/>')
    o += mark(84, 22 + TOP + 4, w - 12, ph - TOP - BOTTOM - 8, 'green', 12)
    return o


FIGS['saCodigo'] = lambda: frame(dict(
    id='saCodigo',
    title='<tspan class="mono">SafeArea</tspan> envuelve el contenido',
    title_plain='SafeArea envuelve el contenido',
    desc='Un Scaffold sin appBar cuyo body es un SafeArea con una Column adentro. En el resultado, el contenido empieza debajo de la barra de estado y termina antes de la barra de gestos.',
    sub='Va en el body, alrededor de todo lo demás. Deja libres los bordes que ocupa el sistema.',
    file='lib/screens/login_screen.dart',
    panel='RESULTADO',
    min_h=456,
    code=[
        "return const Scaffold(",
        "  body: SafeArea(",
        "    child: Column(",
        "      children: [",
        "        Text('Bienvenido'),",
        "        Text('Inicia sesión para continuar'),",
        "      ],",
        "    ),",
        "  ),",
        ");",
    ],
    result=sa_codigo_result(),
    arrows=[
        dict(line=1, find='SafeArea', to=(84, 240), color='green', lane=1),
    ],
))


# ───────────────────────────── S0028 · AppBar


def ab_icon(name, cx, cy, color=INK, k=1):
    paths = {
        'menu': 'M-9,-6 H9 M-9,0 H9 M-9,6 H9',
        'search': 'M-8,-2 a6,6 0 1 0 12,0 a6,6 0 1 0 -12,0 M2.5,2.5 L8,8',
        'settings': ('M-3.5,0 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M0,-9 V-6.5 M0,6.5 V9 M-9,0 H-6.5 M6.5,0 H9 '
                     'M-6.4,-6.4 L-4.6,-4.6 M4.6,4.6 L6.4,6.4 M-6.4,6.4 L-4.6,4.6 M4.6,-4.6 L6.4,-6.4'),
    }
    return (f'<path transform="translate({cx},{cy}) scale({k})" d="{paths[name]}" fill="none" stroke="{color}" '
            f'stroke-width="{2 / k:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')


def ab_bar(w, bar, title, size, fill='#F1ECF8', ink=INK, center=False, k=1):
    """Barra de arriba con menú, título y dos acciones, en coordenadas de la pantalla."""
    o = f'<rect width="{w}" height="{bar}" fill="{fill}"/>'
    o += ab_icon('menu', 36 * k, bar / 2, ink, k)
    if center:
        o += txt(w / 2, bar / 2, title, size, 500, ink, 'middle').replace('<text ', '<text dy="0.35em" ')
    else:
        o += txt(76 * k, bar / 2, title, size, 500, ink).replace('<text ', '<text dy="0.35em" ')
    o += ab_icon('search', w - 92 * k, bar / 2, ink, k) + ab_icon('settings', w - 36 * k, bar / 2, ink, k)
    return o


def ab_crop(fid, key, x, y, w, h, inner):
    """La parte de arriba de un celular: se recorta a `h` y se desvanece hacia el fondo."""
    return (f'<clipPath id="{fid}-{key}c"><rect x="{x - 10}" y="{y - 10}" width="{w + 20}" height="{h + 10}"/></clipPath>'
            f'<linearGradient id="{fid}-{key}f" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBFBFD" stop-opacity="0"/>'
            f'<stop offset="1" stop-color="#FBFBFD"/></linearGradient>'
            f'<g clip-path="url(#{fid}-{key}c)">' + device(x, y, w, h + 80, inner, '#FFFFFF', f'{fid}-{key}s') + '</g>'
            f'<rect x="{x - 10}" y="{y + h - 44}" width="{w + 20}" height="46" fill="url(#{fid}-{key}f)"/>')


def ab_partes():
    fid = 'abPartes'
    h = 412
    s = head(fid, h, 'Las partes de un <tspan class="mono">AppBar</tspan>', 'Las partes de un AppBar',
             'Tres lugares, de izquierda a derecha. Solo title es de uso diario; los otros dos son opcionales.',
             'La parte de arriba de un celular con una barra. A la izquierda, un botón de menú: es leading. Después, el título Perfil: es title. A la derecha, dos botones, buscar y ajustes: son actions.')
    x, y, w, bar = 260, 228, 440, 72
    s += '  ' + ab_crop(fid, 'a', x, y, w, 150, ab_bar(w, bar, 'Perfil', 22)) + '\n'
    parts = [('indigo', x + 12, 48, 180, 'leading', 'Un widget a la izquierda.', 'Casi siempre un IconButton.'),
             ('amber', x + 66, 84, 480, 'title', 'El nombre de la pantalla.', 'Casi siempre un Text.'),
             ('green', x + w - 122, 112, 770, 'actions', 'Una lista de widgets a la derecha.', 'Los botones de la pantalla.')]
    for color, mx, mw, lx, name, a, b in parts:
        strong = FAM[color][2]
        cx = mx + mw / 2
        s += '  ' + mark(mx, y + 12, mw, 48, color, 12) + '\n'
        s += f'  <path d="M{lx},184 V204 H{cx:g} V{y + 12}" fill="none" stroke="{strong}" stroke-width="1.75"/>\n'
        s += '  ' + txt(lx, 132, name, 15, 700, strong, 'middle', cls='mono') + '\n'
        s += '  ' + txt(lx, 154, a, 13, 400, MUTED, 'middle', fit=280) + '\n'
        s += '  ' + txt(lx, 172, b, 13, 400, MUTED, 'middle', fit=280) + '\n'
    return s + '</svg>\n'


FIGS['abPartes'] = ab_partes


def ab_variantes():
    fid = 'abVariantes'
    h = 372
    s = head(fid, h, 'La misma barra, con tres ajustes', 'La misma barra, con tres ajustes',
             'El contenido no cambia. Cambian dónde queda el título y de qué color es la barra.',
             'Tres barras con el mismo título y los mismos botones. La primera, sin ajustes: el título queda a la izquierda. La segunda, con centerTitle en true: el título queda centrado. La tercera, con backgroundColor morado y foregroundColor blanco: fondo oscuro con el título y los iconos en blanco.')
    w, bar, k = 256, 52, .72
    cases = [(64, 'a', {}, 'Sin ajustes', 'El título queda a la izquierda.', None),
             (352, 'b', dict(center=True), 'centerTitle: true', 'El título queda en el centro.', 'mono'),
             (640, 'c', dict(fill='#673AB7', ink='#FFFFFF'), 'backgroundColor', 'Con foregroundColor: Colors.white.', 'mono')]
    for x, key, opts, a, b, cls in cases:
        s += '  ' + ab_crop(fid, key, x, 132, w, 120, ab_bar(w, bar, 'Perfil', 16, k=k, **opts)) + '\n'
        s += '  ' + txt(x + w / 2, 292, a, 14, 700, INK, 'middle', cls=cls or '', fit=272) + '\n'
        s += '  ' + txt(x + w / 2, 314, b, 13, 400, MUTED, 'middle', fit=272) + '\n'
    return s + '</svg>\n'


FIGS['abVariantes'] = ab_variantes


# ───────────────────────────── S0027 · BottomNavigationBar


def bn_item(cx, y, icon, label, color):
    paths = {
        'home': 'M-8,1 L0,-7 L8,1 M-6,-0.5 V7 H6 V-0.5',
        'chat': 'M-7,-7 h14 a2,2 0 0 1 2,2 v7 a2,2 0 0 1 -2,2 h-8 l-4,3 v-3 h-2 a2,2 0 0 1 -2,-2 v-7 a2,2 0 0 1 2,-2 Z',
        'person': 'M-3.5,-4 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M-7,7 a7,6 0 0 1 14,0',
    }
    return (f'<path transform="translate({cx},{y})" d="{paths[icon]}" fill="none" stroke="{color}" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round"/>'
            + txt(cx, y + 24, label, 12, 600, color, 'middle'))


def bn_codigo_result():
    x, y, w, ph, bar = 78, 40, 204, 440, 60
    selected = '#6750A4'
    inner = ('<rect width="204" height="52" fill="#F1ECF8"/>'
             + txt(18, 31, 'Inicio', 17, 500)
             + txt(w / 2, 216, 'Contenido', 13.5, 400, INK, 'middle')
             + f'<rect y="{ph - bar}" width="{w}" height="{bar}" fill="#F3EDF7"/>'
             + bn_item(34, ph - 38, 'home', 'Inicio', selected)
             + bn_item(102, ph - 38, 'chat', 'Chats', MUTED)
             + bn_item(170, ph - 38, 'person', 'Perfil', MUTED))
    o = (f'<clipPath id="bnCodigo-scr"><rect width="{w}" height="{ph}" rx="26"/></clipPath>'
         f'<g transform="translate({x},{y})"><rect width="{w}" height="{ph}" rx="26" fill="#FFFFFF"/>'
         f'<g clip-path="url(#bnCodigo-scr)">{inner}</g></g>'
         f'<rect x="{x}" y="{y}" width="{w}" height="{ph}" rx="26" fill="none" stroke="#2A3040" stroke-width="3"/>')
    o += mark(x + 6, y + ph - bar + 4, w - 12, bar - 8, 'amber', 14)
    return o


FIGS['bnCodigo'] = lambda: frame(dict(
    id='bnCodigo',
    title='Tres botones en <tspan class="mono">bottomNavigationBar</tspan>',
    title_plain='Tres botones en bottomNavigationBar',
    desc='Un Scaffold con appBar, body y bottomNavigationBar. La barra de abajo es un BottomNavigationBar con tres BottomNavigationBarItem: Inicio, Chats y Perfil. En el resultado, la barra queda pegada al borde de abajo con los tres botones repartidos a lo ancho, y el primero, Inicio, aparece resaltado.',
    sub='La barra queda fija abajo. El body ocupa lo que queda entre ella y la barra de arriba.',
    file='lib/screens/home_screen.dart',
    panel='RESULTADO',
    code=[
        "return Scaffold(",
        "  appBar: AppBar(title: const Text('Inicio')),",
        "  body: const Center(child: Text('Contenido')),",
        "  bottomNavigationBar: BottomNavigationBar(",
        "    currentIndex: 0,",
        "    items: const [",
        "      BottomNavigationBarItem(",
        "        icon: Icon(Icons.home),",
        "        label: 'Inicio',",
        "      ),",
        "      BottomNavigationBarItem(",
        "        icon: Icon(Icons.chat),",
        "        label: 'Chats',",
        "      ),",
        "      BottomNavigationBarItem(",
        "        icon: Icon(Icons.person),",
        "        label: 'Perfil',",
        "      ),",
        "    ],",
        "  ),",
        ");",
    ],
    result=bn_codigo_result(),
    arrows=[
        dict(line=3, find='bottomNavigationBar', to=(84, 450), color='amber', lane=1),
    ],
    cards=[
        ('amber', 'items', ['Los botones, de izquierda', 'a derecha. Mínimo dos.']),
        ('indigo', 'icon y label', ['Cada botón lleva un icono', 'y un texto debajo.']),
        ('green', 'currentIndex', ['El botón resaltado. Se cuenta', 'desde 0: aquí es Inicio.']),
    ],
))


# ───────────────────────────── S0022 · Container y Padding


def dim(x1, y1, x2, y2, label, color='amber'):
    """Cota: una línea con topes y su medida."""
    strong = FAM[color][2]
    if x1 == x2:
        ticks = f'M{x1-4},{y1} H{x1+4} M{x1-4},{y2} H{x1+4}'
        tx, ty, anchor = x1 + 8, (y1 + y2) / 2, 'start'
    else:
        ticks = f'M{x1},{y1-4} V{y1+4} M{x2},{y1-4} V{y1+4}'
        tx, ty, anchor = (x1 + x2) / 2, y1 - 7, 'middle'
    return (f'<path d="M{x1},{y1} L{x2},{y2} {ticks}" stroke="{strong}" stroke-width="1.5" fill="none"/>'
            f'<text x="{tx}" y="{ty}" dy="0.35em" font-size="12" font-weight="700" fill="{strong}" text-anchor="{anchor}">{label}</text>')


def padded(x, y, w, h, l, t, r, b, label='child'):
    soft, border, strong = FAM['amber']
    isoft, iborder, istrong = FAM['indigo']
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{soft}" stroke="{border}" stroke-width="1.5" stroke-dasharray="5 4"/>'
            f'<rect x="{x+l}" y="{y+t}" width="{w-l-r}" height="{h-t-b}" rx="6" fill="{isoft}" stroke="{iborder}" stroke-width="1.5"/>'
            f'<text x="{x+l+(w-l-r)/2}" y="{y+t+(h-t-b)/2}" dy="0.35em" text-anchor="middle" font-size="13" font-weight="600" fill="{istrong}">{label}</text>')


FIGS['cpPadding'] = lambda: frame(dict(
    id='cpPadding',
    title='<tspan class="mono">Padding</tspan>: aire alrededor de un widget',
    title_plain='Padding: aire alrededor de un widget',
    desc='Un Padding con EdgeInsets.all(16) y un Text como child. En el resultado, el texto queda separado 16 píxeles de cada borde del espacio que le dieron.',
    sub='Envuelve a un widget y lo separa de lo que tiene alrededor. No se ve: solo ocupa espacio.',
    file='lib/screens/profile_screen.dart',
    panel='RESULTADO',
    min_h=288,
    code=[
        "Padding(",
        "  padding: EdgeInsets.all(16),",
        "  child: Text('Mariana Valenzuela'),",
        ")",
    ],
    result=(padded(40, 36, 280, 150, 32, 32, 32, 32, 'Mariana Valenzuela')
            + dim(56, 36, 56, 68, '16') + dim(288, 200, 320, 200, '16')
            + txt(180, 232, 'La zona amarilla es el padding.', 12, 400, FAINT, 'middle', fit=300)),
    arrows=[
        dict(line=1, find='padding', to=(40, 47), color='amber'),
        dict(line=2, find='child', to=(72, 130), color='indigo', lane=1),
    ],
))


def cp_insets():
    fid = 'cpInsets'
    h = 408
    s = head(fid, h, 'Tres formas de decir cuánto aire', 'Tres formas de decir cuánto aire',
             'EdgeInsets dice cuántos píxeles dejar en cada lado. Se elige el constructor según qué lados sean iguales.',
             'Tres cajas. En la primera, EdgeInsets.all(16) deja el mismo espacio por los cuatro lados. En la segunda, EdgeInsets.symmetric deja 24 a los lados y 8 arriba y abajo. En la tercera, EdgeInsets.only deja espacio solo arriba.')
    cells = [(48, (24, 24, 24, 24), 'EdgeInsets.all(16)', 'Lo mismo por los cuatro lados'),
             (344, (36, 12, 36, 12), 'EdgeInsets.symmetric(', 'Unos lados y otros, por parejas'),
             (640, (0, 36, 0, 0), 'EdgeInsets.only(top: 24)', 'Solo los lados que nombres')]
    for x, ins, name, body in cells:
        s += '  ' + padded(x, 128, 272, 152, *ins) + '\n'
        s += '  ' + txt(x, 316, name, 13.5, 700, INK, cls='mono', fit=272) + '\n'
        if name.endswith('('):
            s += '  ' + txt(x, 336, '  horizontal: 24, vertical: 8)', 13.5, 700, INK, cls='mono', fit=272).replace('<text ', '<text xml:space="preserve" ') + '\n'
            s += '  ' + txt(x, 362, body, 13, 400, MUTED, fit=272) + '\n'
        else:
            s += '  ' + txt(x, 342, body, 13, 400, MUTED, fit=272) + '\n'
    return s + '</svg>\n'


FIGS['cpInsets'] = cp_insets


FIGS['cpContainer'] = lambda: frame(dict(
    id='cpContainer',
    title='<tspan class="mono">Container</tspan>: una caja que se ve',
    title_plain='Container: una caja que se ve',
    desc='Un Container con padding y un BoxDecoration con color blanco, borde índigo y esquinas redondeadas, y un Text como child. En el resultado, una tarjeta blanca con borde y esquinas redondas, con el texto separado del borde.',
    sub='Hace lo mismo que Padding y además pinta: fondo, borde y esquinas van en decoration.',
    file='lib/screens/profile_screen.dart',
    panel='RESULTADO',
    min_h=336,
    code=[
        "Container(",
        "  padding: EdgeInsets.all(16),",
        "  decoration: BoxDecoration(",
        "    color: Colors.white,",
        "    border: Border.all(color: Colors.indigo),",
        "    borderRadius: BorderRadius.circular(16),",
        "  ),",
        "  child: Text('Mariana Valenzuela'),",
        ")",
    ],
    result=('<rect x="24" y="84" width="312" height="180" rx="8" fill="#EEF0F4"/>'
            '<rect x="60" y="120" width="240" height="100" rx="18" fill="#FFFFFF" stroke="#4453C9" stroke-width="2.5"/>'
            + txt(180, 175, 'Mariana Valenzuela', 15, 600, INK, 'middle')),
    arrows=[
        dict(line=1, find='padding', to=(240, 124), end='v', color='amber'),
        dict(line=3, find='color', to=(104, 140), color='green', lane=2),
        dict(line=4, find='border', to=(60, 190), color='indigo', lane=1),
        dict(line=5, find='borderRadius', to=(70, 220), via=[(70, 244)], color='rose', lane=0),
    ],
))


def cp_caja():
    fid = 'cpCaja'
    h = 440
    s = head(fid, h, 'Las capas de un <tspan class="mono">Container</tspan>', 'Las capas de un Container',
             'De afuera hacia adentro: margin, la decoración, padding y el child.',
             'Cajas anidadas. La de afuera es margin, el aire por fuera del Container. Sigue el borde y el fondo, que son la decoración. Adentro, padding, el aire entre el borde y el contenido. En el centro, el child.')
    ss, sb, sst = FAM['slate']
    s += f'  <rect x="96" y="128" width="400" height="264" rx="10" fill="{ss}" stroke="{sb}" stroke-width="1.5" stroke-dasharray="5 4"/>\n'
    s += f'  <rect x="136" y="168" width="320" height="184" rx="18" fill="{FAM["amber"][0]}" stroke="{FAM["indigo"][2]}" stroke-width="3"/>\n'
    s += f'  <rect x="172" y="204" width="248" height="112" rx="6" fill="{FAM["indigo"][0]}" stroke="{FAM["indigo"][1]}" stroke-width="1.5"/>\n'
    s += '  ' + txt(296, 265, 'child', 15, 700, FAM['indigo'][2], 'middle', cls='mono') + '\n'
    rows = [(148, 478, 'slate', 'margin', 'Aire por fuera. Separa la caja de sus vecinas.'),
            (216, 438, 'amber', 'padding', 'Aire por dentro, entre el borde y el contenido.'),
            (284, 404, 'indigo', 'child', 'El contenido: un solo widget.'),
            (340, 456, 'indigo', 'decoration', 'El fondo, el borde y las esquinas.')]
    for y, px, color, name, body in rows:
        strong = FAM[color][2]
        s += f'  <path d="M{px},{y} H556" stroke="{strong}" stroke-width="1.5"/><circle cx="{px}" cy="{y}" r="3.5" fill="{strong}"/>\n'
        s += '  ' + txt(572, y - 4, name, 15, 700, strong, cls='mono', fit=340) + '\n'
        s += '  ' + txt(572, y + 17, body, 13, 400, MUTED, fit=340) + '\n'
    return s + '</svg>\n'


FIGS['cpCaja'] = cp_caja


# ───────────────────────────── S0023 · Expanded


def ex_sobra():
    fid = 'exSobra'
    h = 432
    gs, gb, gst = FAM['green']
    s = head(fid, h, 'Una fila con un texto largo', 'Una fila con un texto largo',
             'Sin Expanded, el texto pide todo el ancho que necesita. Con Expanded, recibe solo el que sobra.',
             'La misma fila de chat dos veces. Arriba, sin Expanded, el mensaje se sale por la derecha de la pantalla y aparece la franja amarilla y negra. Abajo, con Expanded, la columna de textos ocupa el espacio que dejan la foto y la hora, y el mensaje se corta con puntos suspensivos.')
    s += (f'  <defs><pattern id="{fid}-warn" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
          f'<rect width="10" height="10" fill="#FFD600"/><rect width="5" height="10" fill="#1F2430"/></pattern></defs>\n')
    x0, x1 = 232, 792
    for y in (128, 264):
        s += f'  <rect x="{x0}" y="{y}" width="{x1-x0}" height="80" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
        s += '  ' + avatar(x0 + 40, y + 40, 24, 'amber') + '\n'
        s += '  ' + txt(x0 + 80, y + 34, 'Javier Montes', 15, 700) + '\n'
    s += '  ' + txt(x0 + 80, 184, '¿Te parece si revisamos los avances del proyecto antes de la reunión de mañana con el cliente?', 13.5, 400, MUTED) + '\n'
    s += f'  <rect x="{x1}" y="120" width="140" height="96" fill="#FBFBFD" fill-opacity=".72"/>\n'
    s += f'  <rect x="{x1-14}" y="128" width="14" height="80" fill="url(#{fid}-warn)"/>\n'
    s += f'  <rect x="{x0+72}" y="272" width="{x1-x0-72-76}" height="64" rx="8" fill="{gst}" fill-opacity=".08" stroke="{gst}" stroke-width="2"/>\n'
    s += '  ' + txt(x0 + 80, 320, '¿Te parece si revisamos los avances del proyecto antes…', 13.5, 400, MUTED, fit=400) + '\n'
    s += '  ' + txt(x1 - 16, 309, '10:24', 13, 400, FAINT, 'end') + '\n'
    for a, b, label, color in ((x0 + 12, x0 + 68, 'fijo', 'slate'), (x0 + 72, x1 - 76, 'Expanded: lo que sobra', 'green'), (x1 - 68, x1 - 8, 'fijo', 'slate')):
        strong = FAM[color][2]
        s += f'  <path d="M{a},364 V370 H{b} V364" fill="none" stroke="{strong}" stroke-width="1.5"/>\n'
        s += '  ' + txt((a + b) / 2, 390, label, 12.5, 700, strong, 'middle') + '\n'
    s += '  ' + txt(48, 162, 'Sin Expanded', 15, 700, FAM['rose'][2], fit=170) + '\n'
    s += '  ' + txt(48, 184, 'El texto se sale.', 13, 400, MUTED, fit=170) + '\n'
    s += '  ' + txt(48, 298, 'Con Expanded', 15, 700, gst, fit=170) + '\n'
    s += '  ' + txt(48, 320, 'El texto se ajusta.', 13, 400, MUTED, fit=170) + '\n'
    return s + '</svg>\n'


FIGS['exSobra'] = ex_sobra


def ex_codigo_result():
    gst = FAM['green'][2]
    o = txt(180, 150, 'La foto y la hora miden lo suyo.', 12.5, 400, FAINT, 'middle', fit=320)
    o += txt(180, 170, 'Expanded se queda con el resto.', 12.5, 400, FAINT, 'middle', fit=320)
    o += '<rect x="12" y="268" width="336" height="64" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>'
    o += avatar(44, 300, 20, 'amber')
    o += f'<rect x="74" y="276" width="208" height="48" rx="8" fill="{gst}" fill-opacity=".08" stroke="{gst}" stroke-width="2"/>'
    o += txt(84, 296, 'Javier Montes', 13.5, 700)
    o += txt(84, 314, '¿Te parece si revisamos…', 12.5, 400, MUTED, fit=190)
    o += txt(338, 304, '10:24', 12.5, 400, FAINT, 'end')
    return o


FIGS['exCodigo'] = lambda: frame(dict(
    id='exCodigo',
    title='<tspan class="mono">Expanded</tspan> dentro de una <tspan class="mono">Row</tspan>',
    title_plain='Expanded dentro de una Row',
    desc='Una Row con un CircleAvatar, un Expanded que envuelve una Column con dos textos, y un Text con la hora. En el resultado, la foto y la hora ocupan su tamaño y la columna de textos ocupa todo el espacio que queda entre las dos.',
    sub='Se envuelve al hijo que debe adaptarse. Los demás conservan su tamaño.',
    file='lib/components/chat_item.dart',
    panel='RESULTADO',
    code=[
        "Row(",
        "  children: [",
        "    CircleAvatar(radius: 24),",
        "    SizedBox(width: 12),",
        "    Expanded(",
        "      child: Column(",
        "        crossAxisAlignment: CrossAxisAlignment.start,",
        "        children: [",
        "          Text('Javier Montes'),",
        "          Text(",
        "            '¿Te parece si revisamos los avances?',",
        "            maxLines: 1,",
        "            overflow: TextOverflow.ellipsis,",
        "          ),",
        "        ],",
        "      ),",
        "    ),",
        "    Text('10:24'),",
        "  ],",
        ")",
    ],
    result=ex_codigo_result(),
    arrows=[
        dict(line=2, find='CircleAvatar', to=(22, 300), color='amber', lane=2),
        dict(line=4, find='Expanded', to=(178, 328), via=[(178, 368)], color='green', lane=1),
        dict(line=17, find="Text('10:24')", to=(322, 316), via=[(322, 431)], color='indigo', lane=0),
    ],
))


def ex_flex():
    fid = 'exFlex'
    h = 392
    s = head(fid, h, 'Repartir el espacio con <tspan class="mono">flex</tspan>', 'Repartir el espacio con flex',
             'Cuando hay varios Expanded en la misma fila, se reparten lo que sobra. flex dice en qué proporción.',
             'Tres filas del mismo ancho. En la primera, dos Expanded se reparten la fila por mitades. En la segunda, uno con flex 2 y otro con flex 1 se la reparten en dos tercios y un tercio. En la tercera, un hijo de ancho fijo conserva su tamaño y un Expanded ocupa el resto.')
    x0, w = 368, 544
    rows = [(128, [('indigo', 1, 'Expanded'), ('violet', 1, 'Expanded')], 'Mitad y mitad', 'Dos Expanded sin flex.'),
            (208, [('indigo', 2, 'Expanded(flex: 2)'), ('violet', 1, 'Expanded(flex: 1)')], 'Dos partes y una', 'El primero recibe el doble.'),
            (288, [('slate', 0, 'ancho fijo'), ('indigo', 1, 'Expanded')], 'Uno fijo y uno flexible', 'Primero se mide el fijo.')]
    for y, parts, a, b in rows:
        s += '  ' + txt(48, y + 22, a, 15, 700, INK, fit=290) + '\n'
        s += '  ' + txt(48, y + 43, b, 13, 400, MUTED, fit=290) + '\n'
        fixed = sum(136 for _, f, _ in parts if f == 0)
        gaps = 8 * (len(parts) - 1)
        total = sum(f for _, f, _ in parts)
        x = x0
        for color, f, label in parts:
            pw = 136 if f == 0 else (w - fixed - gaps) * f / total
            soft, border, strong = FAM[color]
            s += f'  <rect x="{x:.0f}" y="{y}" width="{pw:.0f}" height="56" rx="8" fill="{soft}" stroke="{border}" stroke-width="1.5"/>\n'
            s += '  ' + txt(f'{x + pw/2:.0f}', y + 28, label, 13, 700, strong, 'middle', cls='mono', fit=f'{pw-16:.0f}').replace('<text ', '<text dy="0.35em" ') + '\n'
            x += pw + 8
    return s + '</svg>\n'


FIGS['exFlex'] = ex_flex


# ───────────────────────────── S0024 · SingleChildScrollView

PIECES = [('ProfileInfo', 'violet', 90), ('StatsRow', 'indigo', 56), ('PrimaryButton', 'teal', 36),
          ('ContactCard × 4', 'amber', 72), ('ChatItem', 'rose', 48), ('ChatItem', 'rose', 48), ('ChatItem', 'rose', 48)]


def pieces(x, y, w, cut=None, size=12.5):
    """Los componentes de la pantalla de perfil, apilados. Lo que pasa de `cut` sale tenue."""
    o = ''
    for name, color, ph in PIECES:
        soft, border, strong = FAM[color]
        out = cut is not None and y + ph / 2 > cut
        op = ' opacity=".42"' if out else ''
        dash = ' stroke-dasharray="5 4"' if out else ''
        o += (f'<g{op}><rect x="{x}" y="{y}" width="{w}" height="{ph}" rx="8" fill="{soft}" stroke="{border}" stroke-width="1.5"{dash}/>'
              f'<text x="{x + w/2}" y="{y + ph/2}" dy="0.35em" text-anchor="middle" font-size="{size}" font-weight="700" fill="{strong}" font-family="{MONO}">{name}</text></g>')
        y += ph + 10
    return o


def sc_ventana():
    fid = 'scVentana'
    h = 664
    w, ph = 200, 300
    s = head(fid, h, 'La pantalla es una ventana', 'La pantalla es una ventana',
             'Los componentes del perfil miden más que la pantalla. Con scroll, la pantalla se desliza sobre ellos.',
             'La misma pila de componentes en dos celulares. A la izquierda, sin scroll, lo que no cabe queda por fuera de la pantalla y aparece la franja amarilla y negra abajo. A la derecha, con SingleChildScrollView, la columna conserva todo su alto y sigue por debajo del celular: la pantalla es una ventana que se desliza sobre ella.')
    s += (f'  <defs><pattern id="{fid}-warn" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
          f'<rect width="10" height="10" fill="#FFD600"/><rect width="5" height="10" fill="#1F2430"/></pattern></defs>\n')
    left = pieces(10, 10, w - 20) + f'<rect y="{ph-12}" width="{w}" height="12" fill="url(#{fid}-warn)"/>'
    s += '  ' + device(112, 132, w, ph, left, '#FFFFFF', f'{fid}-a') + '\n'
    s += '  ' + txt(212, 476, 'Sin scroll', 15, 700, FAM['rose'][2], 'middle') + '\n'
    s += '  ' + txt(212, 498, 'Lo que no cabe queda por fuera.', 13, 400, MUTED, 'middle', fit=280) + '\n'
    x = 496
    s += f'  <rect x="{x}" y="132" width="{w}" height="{ph}" rx="20" fill="#FFFFFF"/>\n'
    s += '  ' + pieces(x + 10, 142, w - 20, cut=132 + ph) + '\n'
    s += f'  <rect x="{x-3.5}" y="128.5" width="{w+7}" height="{ph+7}" rx="23.5" fill="none" stroke="#1F2430" stroke-width="7"/>\n'
    s += f'  <path d="M{x+w+32},240 V560" fill="none" stroke="#556074" stroke-width="1.75" marker-start="url(#{fid}-arrow)" marker-end="url(#{fid}-arrow)"/>\n'
    s += '  ' + txt(x + w + 52, 366, 'Con scroll', 15, 700, FAM['green'][2], fit=180) + '\n'
    for i, ln in enumerate(('La Column conserva', 'todo su alto.')):
        s += '  ' + txt(x + w + 52, 394 + i * 19, ln, 13, 400, MUTED, fit=180) + '\n'
    for i, ln in enumerate(('La pantalla se desliza', 'sobre ella.')):
        s += '  ' + txt(x + w + 52, 448 + i * 19, ln, 13, 400, MUTED, fit=180) + '\n'
    return s + '</svg>\n'


FIGS['scVentana'] = sc_ventana


def sc_codigo_result():
    o = '<rect x="96" y="20" width="168" height="226" rx="22" fill="#FFFFFF" stroke="#2A3040" stroke-width="3"/>'
    o += mark(102, 26, 156, 214, 'green', 16)
    rows = ((38, 'ProfileInfo', 'violet', 84), (130, 'StatsRow', 'indigo', 52), (190, 'ChatItem', 'rose', 44),
            (258, 'ChatItem', 'rose', 44), (310, 'ChatItem', 'rose', 44))
    for y, name, color, ph in rows:
        soft, border, strong = FAM[color]
        out = y > 246
        o += (f'<g{" opacity=\".42\"" if out else ""}><rect x="114" y="{y}" width="132" height="{ph}" rx="7" fill="{soft}" stroke="{border}" stroke-width="1.5"{" stroke-dasharray=\"5 4\"" if out else ""}/>'
              f'<text x="180" y="{y + ph/2}" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="{strong}" font-family="{MONO}">{name}</text></g>')
    return o


FIGS['scCodigo'] = lambda: frame(dict(
    id='scCodigo',
    title='<tspan class="mono">SingleChildScrollView</tspan> envuelve la <tspan class="mono">Column</tspan>',
    title_plain='SingleChildScrollView envuelve la Column',
    desc='Un SafeArea cuyo child es un SingleChildScrollView con padding y una Column de componentes. En el resultado, el scroll ocupa la pantalla y la columna sigue por debajo de ella.',
    sub='El scroll mide lo que mide la pantalla. La Column, adentro, mide lo que necesiten sus hijos.',
    file='lib/screens/profile_screen.dart',
    panel='RESULTADO',
    min_h=420,
    code=[
        "body: SafeArea(",
        "  child: SingleChildScrollView(",
        "    padding: EdgeInsets.all(16),",
        "    child: Column(",
        "      children: [",
        "        ProfileInfo(...),",
        "        StatsRow(...),",
        "        ChatItem(...),",
        "        ChatItem(...),",
        "      ],",
        "    ),",
        "  ),",
        "),",
    ],
    result=sc_codigo_result(),
    arrows=[
        dict(line=1, find='SingleChildScrollView', to=(102, 150), color='green', lane=1),
        dict(line=3, find='Column', to=(114, 332), color='rose', lane=0),
    ],
))


def sc_horizontal():
    fid = 'scHorizontal'
    h = 420
    s = head(fid, h, 'El mismo scroll, de lado', 'El mismo scroll, de lado',
             'Con scrollDirection horizontal, lo que se desliza es una Row. Es la fila de contactos sugeridos.',
             'Una fila de seis tarjetas de contacto más ancha que la pantalla. Un marco muestra el ancho de la pantalla: tres tarjetas se ven completas y las demás quedan por fuera, a los lados, hasta que la persona desliza la fila.')
    people = [('Ana', '@ana', 'indigo'), ('Luis Peña', '@luisp', 'teal'), ('Sofía Ruiz', '@sofiaruiz', 'rose'),
              ('Javier M…', '@javim', 'amber'), ('Mariana V…', '@marianav', 'violet'), ('David Luna', '@davidl', 'green')]
    for i, (n, u, c) in enumerate(people):
        x = 156 + i * 112
        out = x < 368 or x + 96 > 712
        s += f'  <g{" opacity=\".4\"" if out else ""}><rect x="{x}" y="144" width="96" height="124" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>'
        s += avatar(x + 48, 186, 24, c) + txt(x + 48, 234, n, 12.5, 700, INK, 'middle') + txt(x + 48, 252, u, 12, 400, FAINT, 'middle') + '</g>\n'
    s += '  <rect x="368" y="128" width="344" height="156" rx="14" fill="none" stroke="#1F2430" stroke-width="3"/>\n'
    s += '  <path d="M368,304 V310 H712 V304" fill="none" stroke="#556074" stroke-width="1.5"/>\n'
    s += '  ' + txt(540, 330, 'ancho de la pantalla', 12.5, 700, MUTED, 'middle') + '\n'
    s += f'  <path d="M96,206 H132" fill="none" stroke="#556074" stroke-width="1.75" marker-start="url(#{fid}-arrow)"/>\n'
    s += f'  <path d="M836,206 H872" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#{fid}-arrow)"/>\n'
    s += '  ' + txt(480, 376, 'scrollDirection: Axis.horizontal', 14, 700, FAM['indigo'][2], 'middle', cls='mono') + '\n'
    return s + '</svg>\n'


FIGS['scHorizontal'] = sc_horizontal


# ───────────────────────────── S0025 · Armar una pantalla


def ap_capas():
    fid = 'apCapas'
    h = 464
    s = head(fid, h, 'Una pantalla, de afuera hacia adentro', 'Una pantalla, de afuera hacia adentro',
             'Cada widget envuelve al siguiente y resuelve una sola cosa. Tus componentes van en el centro.',
             'Cajas anidadas. La de afuera es Scaffold, la pantalla. Adentro, SafeArea, que aleja el contenido de los bordes. Adentro, SingleChildScrollView, que lo deja deslizar. Adentro, Column, que apila. En el centro, tres componentes: ProfileInfo, StatsRow y ChatItem.')
    layers = [('Scaffold', 'indigo', 'La pantalla: fondo y barra'), ('SafeArea', 'green', 'Lejos de la cámara y de los gestos'),
              ('SingleChildScrollView', 'amber', 'Se desliza si no cabe'), ('Column', 'teal', 'Apila uno debajo de otro')]
    for k, (name, color, role) in enumerate(layers):
        soft, border, strong = FAM[color]
        x, y, w, bh = 48 + 24 * k, 112 + 44 * k, 864 - 48 * k, 304 - 60 * k
        s += f'  <rect x="{x}" y="{y}" width="{w}" height="{bh}" rx="12" fill="{soft}" stroke="{border}" stroke-width="1.5"/>\n'
        s += '  ' + txt(x + 16, y + 27, name, 14.5, 700, strong, cls='mono') + '\n'
        s += '  ' + txt(x + w - 16, y + 27, role, 13, 400, MUTED, 'end', fit=360) + '\n'
    for i, name in enumerate(('ProfileInfo', 'StatsRow', 'ChatItem')):
        x = 136 + i * 232
        s += f'  <rect x="{x}" y="288" width="224" height="64" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>\n'
        s += '  ' + txt(x + 112, 320, name, 14, 700, INK, 'middle', cls='mono').replace('<text ', '<text dy="0.35em" ') + '\n'
    s += '  ' + txt(480, 440, 'Se escribe en este orden y se lee igual: de afuera hacia adentro.', 12.5, 400, FAINT, 'middle', fit=860) + '\n'
    return s + '</svg>\n'


FIGS['apCapas'] = ap_capas


def ap_perfil_result():
    o = '<rect x="40" y="20" width="280" height="420" rx="26" fill="#FFFFFF" stroke="#2A3040" stroke-width="3"/>'
    o += '<rect x="42" y="22" width="276" height="44" rx="24" fill="#F1ECF8"/><rect x="42" y="44" width="276" height="22" fill="#F1ECF8"/>'
    o += txt(60, 50, 'Perfil', 15, 500)
    o += avatar(180, 116, 30, 'violet')
    o += txt(180, 170, 'Mariana Valenzuela', 15.5, 700, INK, 'middle')
    o += txt(180, 190, '@marianav • Diseñadora de Producto', 12, 400, MUTED, 'middle', fit=250)
    o += txt(180, 210, 'm.val@estudio.com · Madrid, ES', 12, 400, FAINT, 'middle', fit=250)
    for i, (n, l) in enumerate([('128', 'Publicaciones'), ('2.4k', 'Seguidores'), ('310', 'Seguidos')]):
        x = 52 + i * 87
        o += f'<rect x="{x}" y="252" width="82" height="60" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>'
        o += txt(x + 41, 278, n, 17, 700, INK, 'middle') + txt(x + 41, 298, l, 12, 400, MUTED, 'middle', fit=80)
    o += mark(46, 76, 268, 148, 'violet', 12)
    o += mark(46, 244, 268, 76, 'indigo', 12)
    return o


FIGS['apPerfil'] = lambda: frame(dict(
    id='apPerfil',
    title='Tus componentes, dentro de la pantalla',
    title_plain='Tus componentes, dentro de la pantalla',
    desc='El body de ProfileScreen: SafeArea, SingleChildScrollView y una Column con ProfileInfo, un SizedBox y StatsRow. En el resultado, el bloque de información del perfil arriba y la fila de estadísticas debajo.',
    sub='La pantalla no dibuja nada por su cuenta: ordena componentes y les entrega sus datos.',
    file='lib/screens/profile_screen.dart',
    panel='RESULTADO',
    code=[
        "body: SafeArea(",
        "  child: SingleChildScrollView(",
        "    padding: EdgeInsets.all(16),",
        "    child: Column(",
        "      children: [",
        "        ProfileInfo(",
        "          name: 'Mariana Valenzuela',",
        "          username: '@marianav',",
        "          ...",
        "        ),",
        "        SizedBox(height: 24),",
        "        StatsRow(",
        "          posts: '128',",
        "          followers: '2.4k',",
        "          following: '310',",
        "        ),",
        "      ],",
        "    ),",
        "  ),",
        "),",
    ],
    result=ap_perfil_result(),
    arrows=[
        dict(line=5, find='ProfileInfo', to=(46, 143), color='violet'),
        dict(line=11, find='StatsRow', to=(46, 287), color='indigo'),
    ],
))


# ───────────────────────────── S0026 · Taller · Pantallas


def tp_pantallas():
    fid = 'tpPantallas'
    h = PY0 + PH_ + 10 + 72
    s = head(fid, h, 'La pantalla del taller', 'La pantalla del taller',
             'Se arma en cuatro bloques, de arriba hacia abajo, con los componentes de la sesión 2.',
             'Un celular con la pantalla de perfil, dividida en cuatro bloques numerados de arriba hacia abajo. Uno, la información del perfil y sus tres indicadores. Dos, los botones Seguir y Enviar mensaje. Tres, los contactos sugeridos. Cuatro, las últimas conversaciones. Debajo, el nombre de la clase, ProfileScreen, y su ruta, /profile.')
    s += phone(fid)
    strong = FAM['indigo'][2]
    for n, (name, _sub, _desc, y0, y1, _parts) in enumerate(TP_BLOQUES, 1):
        a, b = PY0 + y0 + 6, PY0 + y1 - 6
        mid = (a + b) / 2
        s += f'  <path d="M672,{a} H682 V{b} H672" fill="none" stroke="{strong}" stroke-width="1.75"/>\n'
        s += f'  <circle cx="712" cy="{mid:g}" r="14" fill="{strong}"/>\n'
        s += '  ' + txt(712, f'{mid:g}', n, 14, 700, '#FFFFFF', 'middle').replace('<text ', '<text dy="0.35em" ') + '\n'
        s += '  ' + txt(736, f'{mid:g}', name, 14, 700, INK, fit=200).replace('<text ', '<text dy="0.35em" ') + '\n'
    cx, y = PX0 + PW_ / 2, PY0 + PH_ + 44
    s += '  ' + txt(f'{cx:g}', y, 'ProfileScreen', 15, 700, FAM['indigo'][2], 'middle', cls='mono') + '\n'
    s += '  ' + txt(f'{cx:g}', y + 20, "'/profile'", 13, 400, MUTED, 'middle', cls='mono') + '\n'
    return s + '</svg>\n'


FIGS['tpPantallas'] = tp_pantallas


def tp_bloque(n):
    """Un bloque de la pantalla del taller, ampliado, con el componente que hace cada parte."""
    name, sub, desc, y0, y1, parts = TP_BLOQUES[n - 1]
    fid = f'tpBloque{n}'
    k, x, y = 1.5, 48, 112
    w, bh = PW_ * k, (y1 - y0) * k
    s = head(fid, y + bh + 40, f'Bloque {n} · {name}', f'Bloque {n} · {name}', sub, desc)
    s += f'  <clipPath id="{fid}-crop"><rect x="{x}" y="{y}" width="{w:g}" height="{bh:g}" rx="12"/></clipPath>\n'
    s += (f'  <g clip-path="url(#{fid}-crop)"><svg x="{x}" y="{y}" width="{w:g}" height="{bh:g}" '
          f'viewBox="{PX0} {PY0 + y0} {PW_} {y1 - y0}">\n' + phone(fid).replace('rx="28"', 'rx="0"') + '  </svg></g>\n')
    s += f'  <rect x="{x}" y="{y}" width="{w:g}" height="{bh:g}" rx="12" fill="none" stroke="#D9DEE8" stroke-width="1.5"/>\n'
    for a, b, color, comp, note in parts:
        strong = FAM[color][2]
        my, mh = y + (a - y0) * k, (b - a) * k
        mid = my + mh / 2
        s += '  ' + mark(x + 6, f'{my:g}', f'{w - 12:g}', f'{mh:g}', color, 12) + '\n'
        s += f'  <path d="M{x + w - 6:g},{mid:g} H596" stroke="{strong}" stroke-width="1.75"/><circle cx="596" cy="{mid:g}" r="3.5" fill="{strong}"/>\n'
        s += '  ' + txt(612, f'{mid - 3:g}', comp, 15, 700, strong, cls='mono', fit=300) + '\n'
        s += '  ' + txt(612, f'{mid + 17:g}', note, 13, 400, MUTED, fit=300) + '\n'
    return s + '</svg>\n'


TP_BLOQUES = [
    ('La información del perfil', 'Dos componentes, uno debajo del otro. Los dos quedan centrados.',
     'La parte de arriba de la pantalla de perfil. Primero ProfileInfo, con la foto, el nombre, el usuario, el correo y la ciudad. Debajo StatsRow, con tres indicadores: publicaciones, seguidores y seguidos.',
     56, 292, [(60, 210, 'violet', 'ProfileInfo', 'Foto, nombre, usuario, correo y ciudad.'),
               (218, 290, 'indigo', 'StatsRow', 'Tres StatCard en una fila.')]),
    ('Los botones', 'Dos botones a todo el ancho, uno debajo del otro.',
     'Dos botones. Arriba PrimaryButton, azul, con el texto Seguir. Debajo SecondaryButton, con borde, con el texto Enviar mensaje.',
     292, 402, [(296, 346, 'indigo', 'PrimaryButton', 'Seguir.'),
                (348, 398, 'teal', 'SecondaryButton', 'Enviar mensaje.')]),
    ('Contactos sugeridos', 'Un título y, debajo, una fila de tarjetas que se desliza de lado.',
     'El título Contactos sugeridos, hecho con SectionHeader. Debajo, una fila de ContactCard con la foto, el nombre y el usuario de cada contacto. La última tarjeta queda cortada: la fila sigue hacia la derecha.',
     402, 526, [(406, 432, 'amber', 'SectionHeader', 'El título de la sección.'),
                (434, 522, 'teal', 'ContactCard', 'Seis o más, en una fila que se desliza.')]),
    ('Últimas conversaciones', 'Un título y, debajo, una conversación por renglón.',
     'El título Últimas conversaciones, hecho con SectionHeader. Debajo, dos ChatItem con la foto, el nombre, el último mensaje y la hora.',
     526, 670, [(530, 556, 'amber', 'SectionHeader', 'El título de la sección.'),
                (558, 666, 'rose', 'ChatItem', 'Cuatro o más, uno debajo del otro.')]),
]

for _n in range(1, 5):
    FIGS[f'tpBloque{_n}'] = lambda _n=_n: tp_bloque(_n)


def tp_carpetas():
    fid = 'tpCarpetas'
    h = 604
    s = head(fid, h, 'Tu proyecto al terminar el taller', 'Tu proyecto al terminar el taller',
             'Los componentes ya los tienes. Hoy agregas uno que te entregamos, cuatro secciones y una pantalla.',
             'La carpeta lib con main.dart y dos subcarpetas. En components están los siete componentes de la sesión 2 y cinco archivos nuevos: section_header.dart y las cuatro secciones, profile_summary_section.dart, profile_actions_section.dart, suggested_contacts_section.dart y recent_chats_section.dart. En screens están home_screen.dart y la pantalla nueva, profile_screen.dart.')

    def folder(x, y, name):
        return (f'<path d="M{x},{y-8} h9 l3,3 h12 v13 h-24 Z" fill="{FAM["amber"][0]}" stroke="{FAM["amber"][2]}" stroke-width="1.5" stroke-linejoin="round"/>'
                + txt(x + 34, y + 5, name, 14.5, 700, INK, cls='mono'))

    def item(x, y, name, new=False, bx=232):
        strong = FAM['green'][2]
        o = f'<path d="M{x},{y-9} h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="{strong if new else "#79809A"}" stroke-width="1.5" stroke-linejoin="round"/>'
        o += txt(x + 26, y + 5, name, 13.5, 700 if new else 400, strong if new else MUTED, cls='mono')
        if new:
            o += (f'<rect x="{x + bx}" y="{y-10}" width="56" height="22" rx="11" fill="{FAM["green"][0]}" stroke="{FAM["green"][1]}" stroke-width="1.5"/>'
                  + txt(x + bx + 28, y + 5, 'nuevo', 12, 700, strong, 'middle'))
        return o
    s += '  ' + folder(64, 140, 'lib/') + '\n'
    s += '  ' + item(104, 176, 'main.dart') + '\n'
    s += '  ' + folder(104, 218, 'components/') + '\n'
    comps = ['chat_item.dart', 'contact_card.dart', 'primary_button.dart', 'profile_actions_section.dart',
             'profile_info.dart', 'profile_summary_section.dart', 'recent_chats_section.dart',
             'secondary_button.dart', 'section_header.dart', 'stat_card.dart', 'stats_row.dart',
             'suggested_contacts_section.dart']
    for i, n in enumerate(comps):
        s += '  ' + item(144, 252 + i * 28, n, n == 'section_header.dart' or n.endswith('_section.dart'), 300) + '\n'
    s += '  ' + folder(536, 218, 'screens/') + '\n'
    for i, (n, new) in enumerate((('home_screen.dart', False), ('profile_screen.dart', True))):
        s += '  ' + item(576, 252 + i * 28, n, new) + '\n'
    s += '  <path d="M76,156 V218 H96 M76,176 H96" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>\n'
    s += '  <path d="M116,234 V560 M548,234 V280" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>\n'
    s += '  <path d="M76,198 H508 V218 H528" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>\n'
    return s + '</svg>\n'


FIGS['tpCarpetas'] = tp_carpetas


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--inject':
        done = set()
        for path in sorted((ROOT / 'content').glob('lessonS2[0-8].md')):
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
