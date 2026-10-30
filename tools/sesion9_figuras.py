"""Figuras SVG de las lecciones de la sesión 9 (S0065 a S0068).

    python3 tools/sesion9_figuras.py <carpeta>     escribe un .svg por figura, para revisarlas
    python3 tools/sesion9_figuras.py --inject      reemplaza cada bloque ```svg de las lecciones
                                                   de la sesión por la figura con el mismo id

Lo que se aprende tocando (la Page que se destruye o sigue viva al cambiar de pestaña) va en
el bloque ```interactive tab-state; estas figuras son las vistas fijas.
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from code_frame import frame  # noqa: E402
from sesion2_figuras import FAM, head  # noqa: E402
from sesion3_figuras import device, mark, txt  # noqa: E402
from sesion7_figuras import card, folder  # noqa: E402
from sesion8_figuras import appbar, button, song_row  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
LESSONS = ['lessonS65.md', 'lessonS66.md', 'lessonS67.md', 'lessonS68.md']
INK, MUTED, FAINT = '#161A26', '#556074', '#79809A'
SELECTED, BAR_BG, PILL = '#6750A4', '#F3EDF7', '#E8DEF8'
PUSH, POP, TAB = '#2F6FD6', '#C27A0E', '#3A8235'
KINDS = {'push': PUSH, 'pop': POP, 'tab': TAB}

ICONS = {
    'home': 'M-8,1 L0,-7 L8,1 M-6,-0.5 V7 H6 V-0.5',
    'chat': 'M-7,-7 h14 a2,2 0 0 1 2,2 v7 a2,2 0 0 1 -2,2 h-8 l-4,3 v-3 h-2 a2,2 0 0 1 -2,-2 v-7 a2,2 0 0 1 2,-2 Z',
    'person': 'M-3.5,-4 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M-7,7 a7,6 0 0 1 14,0',
    'list': 'M-8,-5 H6 M-8,0 H6 M-8,5 H1',
    'heart': 'M0,7 C-9,1 -9,-6 -4.5,-6 C-2,-6 0,-4 0,-2.5 C0,-4 2,-6 4.5,-6 C9,-6 9,1 0,7 Z',
    'settings': ('M-3.5,0 a3.5,3.5 0 1 0 7,0 a3.5,3.5 0 1 0 -7,0 M0,-9 V-6.5 M0,6.5 V9 M-9,0 H-6.5 M6.5,0 H9 '
                 'M-6.4,-6.4 L-4.6,-4.6 M4.6,4.6 L6.4,6.4 M-6.4,6.4 L-4.6,4.6 M4.6,-4.6 L6.4,-6.4'),
}

DEMO = [('home', 'Inicio'), ('chat', 'Chats'), ('person', 'Perfil')]
PLAYLIST = [('list', 'Playlist'), ('heart', 'Favoritas'), ('person', 'Perfil')]

FIGS = {}


def start(fid, h, title, plain, sub, desc, css=''):
    s = head(fid, h, title, plain, sub, desc, css)
    out = ''
    for name, color in KINDS.items():
        out += (f'<marker id="{fid}-{name}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                f'markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">'
                f'<path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="{color}"/></marker>')
    return s.replace('  </defs>', '    ' + out + '\n  </defs>', 1)


def nav(fid, d, kind):
    return (f'<path d="{d}" fill="none" stroke="{KINDS[kind]}" stroke-width="2.25" '
            f'marker-end="url(#{fid}-{kind})"/>')


def chip(cx, cy, label, kind, mono=False):
    color = KINDS[kind]
    w = len(label) * (7.6 if mono else 7) + 20
    return (f'<rect x="{cx - w / 2:.1f}" y="{cy - 12}" width="{w:.1f}" height="24" rx="12" fill="#FFFFFF" '
            f'stroke="{color}" stroke-width="1.5"/>'
            + txt(cx, cy + 4.5, label, 12, 600, color, 'middle', 'mono' if mono else ''))


def icon(name, cx, cy, color, k=1.0):
    return (f'<path transform="translate({cx},{cy}) scale({k})" d="{ICONS[name]}" fill="none" stroke="{color}" '
            f'stroke-width="{2 / k:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')


def bar(x, y, w, items, selected, h=60, k=1.0, labels='all', colors=None):
    """Barra de abajo: `items` son (icono, texto); `labels` es all, selected o none."""
    on, off = colors or (SELECTED, MUTED)
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{BAR_BG}"/>'
    n = len(items)
    for i, (name, label) in enumerate(items):
        cx = x + w * (2 * i + 1) / (2 * n)
        cy = y + h * .38
        color = on if i == selected else off
        if i == selected and labels == 'all':
            o += f'<rect x="{cx - 26 * k:.1f}" y="{cy - 13 * k:.1f}" width="{52 * k:.1f}" height="{26 * k:.1f}" rx="{13 * k:.1f}" fill="{PILL}"/>'
        o += icon(name, f'{cx:.1f}', f'{cy:.1f}', color, k)
        if labels == 'all' or (labels == 'selected' and i == selected):
            o += txt(f'{cx:.1f}', f'{y + h * .82:.1f}', label, 11.5 * k, 600, color, 'middle')
    return o


def phone_at(fid, key, x, y, w, h, inner):
    return device(x, y, w, h, inner, '#FEF7FF', f'{fid}-{key}')


# ───────────────────────────── S0065 · Taller


def tab_screen(w, h, selected, body):
    o = appbar(w, 'Hola, Ana', action='logout') + body
    return o + bar(0, h - 48, w, PLAYLIST, selected, 48, .8)


def body_playlist(w, h):
    o = ''
    for i, (t, a) in enumerate([('Imagine', 'John Lennon'), ('Yellow', 'Coldplay'), ('Levitating', 'Dua Lipa')]):
        o += song_row(8, 50 + i * 48, w - 16, t, a)
    o += f'<rect x="{w - 44}" y="{h - 92}" width="34" height="34" rx="10" fill="#EADDFF"/>'
    o += txt(w - 27, h - 69, '+', 18, 600, '#21005D', 'middle')
    return o


def body_favorites(w, h):
    o = song_row(8, 50, w - 16, 'Yellow', 'Coldplay')
    o += icon('heart', w - 24, 71, '#E91E63', .7)
    o += txt(w / 2, 128, 'Solo las favoritas', 11, 400, FAINT, 'middle')
    return o


def body_profile(w, h):
    o = f'<circle cx="{w / 2}" cy="92" r="26" fill="#EADDFF"/>'
    o += icon('person', w / 2, 92, '#6750A4', 1.6)
    o += txt(w / 2, 142, 'Ana', 15, 700, INK, 'middle')
    o += txt(w / 2, 162, '3 canciones', 11.5, 400, '#625B71', 'middle')
    o += txt(w / 2, 178, '1 favorita', 11.5, 400, '#625B71', 'middle')
    return o


def screen_detail(w, h):
    o = appbar(w, 'Yellow', back=True)
    side = min(w - 48, 70)
    o += f'<rect x="{(w - side) / 2}" y="54" width="{side}" height="{side}" rx="14" fill="#9C7FE0"/>'
    o += txt(w / 2, 72 + side, 'Yellow', 13, 700, INK, 'middle')
    o += txt(w / 2, 88 + side, 'Coldplay', 11, 400, '#625B71', 'middle')
    o += button(w / 2, 100 + side, w - 30, 'Volver')
    return o


def legend(x, y, items):
    o = ''
    for kind, label in items:
        o += f'<path d="M{x},{y} H{x + 28}" stroke="{KINDS[kind]}" stroke-width="2.5"/>'
        o += txt(x + 36, y + 4.5, label, 12.5, 500, '#454C61')
        x += 36 + len(label) * 7 + 36
    return o


def tb_meta():
    fid = 'tbMeta'
    s = start(fid, 640, 'Una Screen, tres pestañas', 'Una Screen, tres pestañas',
              'Cambiar de pestaña es setState dentro de MainScreen. Abrir una canción sigue siendo un push.',
              'Tres celulares con la misma MainScreen, en la ruta /playlist: la barra de arriba dice Hola, Ana y la '
              'de abajo tiene Playlist, Favoritas y Perfil. En el primero está la pestaña Playlist con tres '
              'canciones y el botón más; en el segundo, Favoritas, con solo Yellow; en el tercero, Perfil, con el '
              'nombre Ana y cuántas canciones y favoritas hay. Flechas verdes entre ellos: tocar la barra es '
              'setState. A la derecha, SongDetailScreen con Yellow: una flecha azul desde la lista, pushNamed, y una '
              'naranja de vuelta, pop.')
    w, h = 156, 320
    xs = [48, 252, 456]
    y = 176
    names = [('PlaylistPage', body_playlist), ('FavoritesPage', body_favorites), ('ProfilePage', body_profile)]
    s += f'  <rect x="32" y="112" width="596" height="{y + h + 24 - 112}" rx="16" fill="#F4EBFF" fill-opacity=".5" stroke="#C9A6EE" stroke-width="1.5" stroke-dasharray="6 5"/>\n'
    s += '  ' + txt(48, 138, "'/playlist' · MainScreen", 14, 700, '#7439B8', cls='mono') + '\n'
    s += '  ' + txt(612, 138, 'un solo Scaffold', 12.5, 500, MUTED, 'end') + '\n'
    for i, (x, (name, body)) in enumerate(zip(xs, names)):
        s += '  ' + txt(x + w / 2, y - 14, name, 12.5, 600, MUTED, 'middle', 'mono') + '\n'
        s += '  ' + phone_at(fid, f'p{i}', x, y, w, h, tab_screen(w, h, i, body(w, h))) + '\n'
    for i in range(2):
        a, b = xs[i] + w + 10, xs[i + 1] - 10
        s += '  ' + nav(fid, f'M{a},{y + h - 24} H{b}', 'tab') + '\n'
        s += '  ' + nav(fid, f'M{b},{y + h - 4} H{a}', 'tab') + '\n'
    dx, dw, dh = 744, 140, 230
    dy = 220
    s += '  ' + txt(dx + dw / 2, dy - 30, "'/song'", 13, 700, '#6750A4', 'middle', 'mono') + '\n'
    s += '  ' + txt(dx + dw / 2, dy - 14, 'SongDetailScreen', 12, 500, MUTED, 'middle', 'mono') + '\n'
    s += '  ' + phone_at(fid, 'd', dx, dy, dw, dh, screen_detail(dw, dh)) + '\n'
    s += f'  <rect x="56" y="{y + 92}" width="{w - 16}" height="44" rx="10" fill="none" stroke="{PUSH}" stroke-width="2"/>\n'
    gy = y + h + 44
    s += '  ' + nav(fid, f'M{xs[0] + 24},{y + 136} H40 V{gy} H{dx + dw / 2} V{dy + dh + 12}', 'push') + '\n'
    s += '  ' + chip(686, gy, 'toque en Yellow · pushNamed', 'push') + '\n'
    s += '  ' + nav(fid, f'M{dx - 12},{dy + 120} H{640}', 'pop') + '\n'
    s += '  ' + chip(692, dy + 92, 'Volver · pop', 'pop') + '\n'
    s += '  ' + legend(48, 604, [('tab', 'setState · cambia de pestaña'), ('push', 'pushNamed · abre encima'),
                                 ('pop', 'pop · vuelve')]) + '\n'
    return s + '</svg>\n'


FIGS['tbMeta'] = tb_meta


def tb_carpetas():
    fid = 'tbCarpetas'
    s = start(fid, 655, 'Los archivos de <tspan class="mono">playlist_app</tspan>',
              'Los archivos de playlist_app',
              'Todo viene en el repositorio de arranque. En el taller solo se edita main_screen.dart.',
              'La carpeta lib con main.dart, que tiene las cuatro rutas, y cuatro carpetas: models con song.dart; '
              'components con song_card.dart, song_form.dart y song_list.dart; pages con playlist_page.dart, '
              'favorites_page.dart y profile_page.dart, las tres sin estado; y screens con login_screen.dart, '
              'main_screen.dart, que reemplaza a playlist_screen.dart y guarda _songs y _currentIndex, '
              'song_detail_screen.dart y add_song_screen.dart. Solo main_screen.dart está marcada: es la que se edita.')
    edit = ('se edita', 'amber')
    rows = [
        ('lib/', 0, 'dir', None, None),
        ('main.dart', 1, 'file', ("'/playlist' construye MainScreen", 'indigo'), None),
        ('models/', 1, 'dir', None, None),
        ('song.dart', 2, 'file', ('Song con copyWith', 'slate'), None),
        ('components/', 1, 'dir', None, None),
        ('song_card.dart', 2, 'file', ('Stateless', 'slate'), None),
        ('song_form.dart', 2, 'file', ('StatefulWidget · guarda el borrador', 'violet'), None),
        ('song_list.dart', 2, 'file', ('Stateless', 'slate'), None),
        ('pages/', 1, 'dir', None, None),
        ('playlist_page.dart', 2, 'file', ('Stateless · recibe songs', 'slate'), None),
        ('favorites_page.dart', 2, 'file', ('Stateless · filtra las favoritas', 'slate'), None),
        ('profile_page.dart', 2, 'file', ('Stateless · nombre y conteos', 'slate'), None),
        ('screens/', 1, 'dir', None, None),
        ('login_screen.dart', 2, 'file', ('StatefulWidget · el nombre', 'violet'), None),
        ('main_screen.dart', 2, 'file', ('StatefulWidget · _songs y _currentIndex', 'violet'), edit),
        ('song_detail_screen.dart', 2, 'file', ('Stateless · lee arguments', 'slate'), None),
        ('add_song_screen.dart', 2, 'file', ('Stateless · hospeda el formulario', 'slate'), None),
    ]
    s += f'  <rect x="48" y="104" width="864" height="{len(rows) * 29 + 26}" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
    for i, (name, depth, kind, tag, extra) in enumerate(rows):
        y = 136 + i * 29
        s += '  ' + folder(72, y, name, depth, kind, tag) + '\n'
        if extra:
            label, color = extra
            soft, border, strong = FAM[color]
            s += (f'  <rect x="796" y="{y - 11}" width="88" height="22" rx="11" fill="{soft}" stroke="{border}"/>'
                  + txt(840, y + 4, label, 12, 700, strong, 'middle') + '\n')
    return s + '</svg>\n'


FIGS['tbCarpetas'] = tb_carpetas


# ───────────────────────────── S0066 · Una pieza del Scaffold


def bp_scaffold():
    fid = 'bpScaffold'
    h = 600
    s = head(fid, h, 'La barra tiene su lugar en el <tspan class="mono">Scaffold</tspan>',
             'La barra tiene su lugar en el Scaffold',
             'bottomNavigationBar es un lugar más del Scaffold, como appBar o body. Queda fija en el borde de abajo.',
             'Un celular con una pantalla armada con Scaffold. Arriba, la barra con el título Mi app: es appBar. En '
             'medio, el contenido: es body. Abajo a la derecha, un botón redondo: es floatingActionButton. Pegada al '
             'borde de abajo, una barra con tres botones, Inicio, Chats y Perfil: es bottomNavigationBar, resaltada. '
             'El body ocupa lo que queda entre las dos barras, y el botón flotante queda encima de la de abajo.')
    x, y, w, ph = 370, 120, 220, 440
    inner = '<rect width="220" height="52" fill="#F1ECF8"/>' + txt(18, 32, 'Mi app', 17, 500)
    inner += txt(w / 2, 220, 'Contenido', 13.5, 400, INK, 'middle')
    inner += f'<rect x="{w - 64}" y="{ph - 60 - 64}" width="48" height="48" rx="14" fill="#EADDFF"/>'
    inner += f'<path d="M{w - 40},{ph - 112} V{ph - 92} M{w - 50},{ph - 102} H{w - 30}" stroke="#21005D" stroke-width="2.5" stroke-linecap="round"/>'
    inner += bar(0, ph - 60, w, DEMO, 0)
    s += '  ' + device(x, y, w, ph, inner, '#FFFFFF', f'{fid}-scr') + '\n'
    zones = [
        ('amber', x + 6, y + 6, w - 12, 42, 'left', 'appBar', 'La barra de arriba, con el título.'),
        ('green', x + 6, y + 58, w - 12, ph - 58 - 66, 'left', 'body', 'El contenido. Ocupa lo que sobra.'),
        ('rose', x + w - 68, y + ph - 128, 56, 56, 'right', 'floatingActionButton', 'Flota sobre el body.'),
        ('indigo', x + 4, y + ph - 58, w - 8, 54, 'right', 'bottomNavigationBar', 'La barra de abajo. Hoy, esta.'),
    ]
    for color, zx, zy, zw, zh, side, name, line in zones:
        strong = FAM[color][2]
        s += '  ' + mark(zx, zy, zw, zh, color, 10) + '\n'
        cy = zy + zh / 2
        if side == 'left':
            s += f'  <path d="M{zx},{cy} H{x - 28}" stroke="{strong}" stroke-width="1.75" stroke-dasharray="4 4"/>\n'
            s += '  ' + txt(x - 36, cy - 4, name, 15, 700, strong, 'end', 'mono') + '\n'
            s += '  ' + txt(x - 36, cy + 16, line, 13, 400, MUTED, 'end', fit=280) + '\n'
        else:
            s += f'  <path d="M{zx + zw},{cy} H{x + w + 28}" stroke="{strong}" stroke-width="1.75" stroke-dasharray="4 4"/>\n'
            s += '  ' + txt(x + w + 36, cy - 4, name, 15, 700, strong, cls='mono') + '\n'
            s += '  ' + txt(x + w + 36, cy + 16, line, 13, 400, MUTED, fit=300) + '\n'
    return s + '</svg>\n'


FIGS['bpScaffold'] = bp_scaffold


def bp_partes_result():
    o = txt(16, 40, 'LA BARRA, DE CERCA', 12, 700, MUTED, cls='h')
    x, y, w, h = 16, 56, 328, 100
    o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{BAR_BG}" stroke="#E6E0F2"/>'
    for i, (name, label) in enumerate(DEMO):
        cx = x + w * (2 * i + 1) / 6
        color = SELECTED if i == 0 else MUTED
        if i == 0:
            o += f'<rect x="{cx - 32:.1f}" y="{y + 12}" width="64" height="34" rx="17" fill="{PILL}"/>'
        o += icon(name, f'{cx:.1f}', y + 29, color, 1.4)
        o += txt(f'{cx:.1f}', y + 76, label, 14, 600, color, 'middle')
    cx0 = x + w / 6
    o += f'<path d="M{cx0:.1f},{y + h + 4} V196" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="4 4"/>'
    o += '<rect x="16" y="196" width="328" height="124" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>'
    o += txt(32, 218, 'Un BottomNavigationBarItem', 12.5, 700, MUTED, cls='mono')
    o += '<rect x="32" y="230" width="40" height="40" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>'
    o += icon('home', 52, 250, '#4453C9', 1.2)
    o += txt(84, 255, 'icon · el dibujo', 13, 400, '#454C61')
    o += '<rect x="32" y="280" width="64" height="28" rx="8" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>'
    o += txt(64, 299, 'Inicio', 13, 600, '#0F8478', 'middle')
    o += txt(108, 299, 'label · el texto', 13, 400, '#454C61')
    return o


FIGS['bpPartes'] = lambda: frame(dict(
    id='bpPartes',
    title='Las partes de un <tspan class="mono">BottomNavigationBar</tspan>',
    title_plain='Las partes de un BottomNavigationBar',
    desc='El código de un BottomNavigationBar con currentIndex en 0 y una lista items con tres '
         'BottomNavigationBarItem, cada uno con icon y label: Inicio, Chats y Perfil. A la derecha, la barra de '
         'cerca: currentIndex señala el primer botón, resaltado con una píldora; items señala la barra completa. '
         'Debajo, un botón desarmado: icon es el dibujo de la casa y label es el texto Inicio.',
    sub='La barra es una lista de botones y un número que dice cuál está resaltado.',
    file='lib/screens/home_screen.dart',
    panel='RESULTADO',
    code=[
        "bottomNavigationBar: BottomNavigationBar(",
        "  currentIndex: 0,",
        "  items: const [",
        "    BottomNavigationBarItem(",
        "      icon: Icon(Icons.home),",
        "      label: 'Inicio',",
        "    ),",
        "    BottomNavigationBarItem(",
        "      icon: Icon(Icons.chat),",
        "      label: 'Chats',",
        "    ),",
        "    BottomNavigationBarItem(",
        "      icon: Icon(Icons.person),",
        "      label: 'Perfil',",
        "    ),",
        "  ],",
        "),",
    ],
    result=bp_partes_result(),
    arrows=[
        dict(line=1, find='currentIndex', to=(40, 85), color='green', lane=3),
        dict(line=2, find='items', to=(16, 142), color='amber', lane=2),
        dict(line=4, find='icon', to=(32, 250), color='indigo', lane=1),
        dict(line=5, find='label', to=(32, 294), color='teal', lane=0),
    ],
    cards=[
        ('green', 'currentIndex', ['El botón resaltado. Se cuenta', 'desde 0: aquí es Inicio.']),
        ('amber', 'items', ['Los botones, de izquierda a', 'derecha. Mínimo dos.']),
        ('indigo', 'icon y label', ['Cada botón: un Icon y un', 'texto. Los dos obligatorios.']),
    ],
))


def bp_tipos():
    fid = 'bpTipos'
    h = 404
    s = head(fid, h, 'Con cuatro botones, la barra cambia de estilo', 'Con cuatro botones, la barra cambia de estilo',
             'Con tres o menos, Flutter usa fixed. Con cuatro o más, shifting: hay que pedir fixed a mano.',
             'Dos barras con cuatro botones: Inicio, Chats, Perfil y Ajustes. La de la izquierda, sin type: es '
             'shifting, los iconos quedan casi blancos sobre el fondo y solo el botón resaltado muestra su texto. La '
             'de la derecha, con type BottomNavigationBarType.fixed: los cuatro iconos y los cuatro textos se ven, y '
             'el resaltado va en morado.')
    items = DEMO + [('settings', 'Ajustes')]
    w = 384
    cols = [(64, 'Sin type', 'shifting · casi invisible', 'rose', 'selected', ('#E4DFEC', '#ECE8F2')),
            (512, 'type: BottomNavigationBarType.fixed', 'fixed · se ve todo', 'green', 'all', None)]
    for x, name, sub, color, labels, colors in cols:
        strong = FAM[color][2]
        s += '  ' + txt(x, 132, name, 14, 700, INK, cls='mono', fit=w) + '\n'
        s += '  ' + txt(x, 152, sub, 12.5, 500, strong, fit=w) + '\n'
        s += f'  <rect x="{x}" y="176" width="{w}" height="120" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
        inner = bar(x, 236, w, items, 0, 60, 1.0, labels, colors)
        if colors:
            inner = inner.replace(f'fill="{BAR_BG}"', 'fill="#FFFFFF"', 1)
        s += f'  <g>{inner}</g>\n'
        s += f'  <path d="M{x},236 H{x + w}" stroke="#EFF1F5" stroke-width="1.5"/>\n'
        s += '  ' + txt(x + 16, 206, 'Contenido', 13, 400, FAINT) + '\n'
    s += '  ' + card(64, 320, 384, 64, 'rose', 'Los iconos se pierden', ['shifting pinta los botones en blanco.']) + '\n'
    s += '  ' + card(512, 320, 384, 64, 'green', 'Con fixed, como con tres', ['Todos los textos y el color del tema.']) + '\n'
    return s + '</svg>\n'


FIGS['bpTipos'] = bp_tipos


# ───────────────────────────── S0067 · El índice en el estado


def page_card(y, idx, name, color, glyph, on):
    soft, border, strong = FAM[color]
    stroke = strong if on else border
    o = (f'<rect x="16" y="{y}" width="328" height="56" rx="12" fill="{soft if on else "#FFFFFF"}" '
         f'stroke="{stroke}" stroke-width="{2 if on else 1.5}"/>')
    o += f'<circle cx="44" cy="{y + 28}" r="16" fill="#FFFFFF" stroke="{border}" stroke-width="1.5"/>'
    o += icon(glyph, 44, y + 28, strong, .9)
    o += txt(72, y + 24, name, 13.5, 700, INK, cls='mono')
    o += txt(72, y + 43, f'case {idx}' if idx < 2 else 'default', 12, 400, MUTED, cls='mono')
    if on:
        o += (f'<rect x="262" y="{y + 17}" width="70" height="22" rx="11" fill="#FFFFFF" stroke="{strong}"/>'
              + txt(297, y + 32, 'se ve', 12, 700, strong, 'middle'))
    return o


def bi_switch_result():
    o = ('<rect x="16" y="16" width="328" height="56" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>'
         + txt(30, 40, '_currentIndex vale 1', 13.5, 700, '#A96C05', cls='mono')
         + txt(30, 59, 'Lo puso el onTap al tocar Chats.', 12.5, 400, '#454C61'))
    o += page_card(96, 0, 'HomePage()', 'violet', 'home', False)
    o += page_card(164, 1, 'ChatsPage()', 'teal', 'chat', True)
    o += page_card(232, 2, 'ProfilePage()', 'indigo', 'person', False)
    return o


FIGS['biSwitch'] = lambda: frame(dict(
    id='biSwitch',
    title='Un número elige la <tspan class="mono">Page</tspan>',
    title_plain='Un número elige la Page',
    desc='El método _buildPage con un switch sobre _currentIndex: case 0 devuelve HomePage, case 1 devuelve '
         'ChatsPage y default devuelve ProfilePage. A la derecha, una tarjeta dice que _currentIndex vale 1, y '
         'debajo las tres Pages; ChatsPage está resaltada porque es la que se ve. Debajo, dos tarjetas: con if y '
         'else se elige igual, y default atrapa cualquier otro número.',
    sub='build() llama a _buildPage(), y el switch devuelve la Page que corresponde al número.',
    file='lib/screens/home_screen.dart',
    panel='QUÉ DEVUELVE CADA CASO',
    min_h=330,
    code=[
        "Widget _buildPage() {",
        "  switch (_currentIndex) {",
        "    case 0:",
        "      return const HomePage();",
        "    case 1:",
        "      return const ChatsPage();",
        "    default:",
        "      return const ProfilePage();",
        "  }",
        "}",
    ],
    result=bi_switch_result(),
    arrows=[
        dict(line=1, find='_currentIndex', to=(16, 44), color='amber', lane=3),
        dict(line=3, find='HomePage()', to=(16, 124), color='violet', lane=2),
        dict(line=5, find='ChatsPage()', to=(16, 192), color='teal', lane=1),
        dict(line=7, find='ProfilePage()', to=(16, 260), color='indigo', lane=0),
    ],
    cards=[
        ('amber', 'if / else if / else', ['La misma elección, con if. El switch', 'se lee mejor cuando hay tres o más.']),
        ('green', 'default', ['Atrapa cualquier otro número: el', 'método siempre devuelve una Page.']),
    ],
))


def bi_ciclo():
    """Animada: cinco pasos de 2,5 s. Tocar Chats, setState, build, el switch elige y se ve."""
    fid, h = 'biCiclo', 690
    steps, secs = 5, 2.5
    s = start(fid, h, 'Qué pasa al tocar un botón de la barra', 'Qué pasa al tocar un botón de la barra',
              'El toque cambia un número en el estado. El resto lo hace build() con ese número.',
              'Animación en cinco pasos. A la izquierda, un celular con la barra Inicio, Chats y Perfil; a la derecha, '
              'el estado _currentIndex y cuatro pasos. Uno: se toca Chats y la barra llama a onTap con 1. Dos: '
              'setState cambia _currentIndex de 0 a 1. Tres: build corre otra vez. Cuatro: _buildPage entra al '
              'switch y devuelve ChatsPage. Cinco: el body muestra ChatsPage y la barra resalta Chats.')
    pct = lambda k: round(k * 100 / steps, 2)
    spans = {
        'r1': [(0, pct(1))], 'r2': [(pct(1), pct(2))], 'r3': [(pct(2), pct(3))], 'r4': [(pct(3), pct(4))],
        'tap': [(0, pct(1))], 'v0': [(0, pct(1))], 'v1': [(pct(1), 100)],
        'pg0': [(0, pct(4))], 'pg1': [(pct(4), 100)], 'hl': [(pct(4), 100)],
        'c1': [(0, pct(1))], 'c2': [(pct(1), pct(2))], 'c3': [(pct(2), pct(3))],
        'c4': [(pct(3), pct(4))], 'c5': [(pct(4), 100)],
    }

    def keyframes(name, sp):
        pts = {0: 0, 100: 0}
        for a, b in sp:
            pts.update({a: 0, round(a + 1.5, 2): 1, round(b - 1.5, 2): 1, b: 0})
        if sp[0][0] == 0:
            pts[0] = 1
        body = ' '.join(f'{k}%{{opacity:{v}}}' for k, v in sorted(pts.items()))
        return f'      #{fid} .{name}{{animation-name:{fid}-{name}}}\n      @keyframes {fid}-{name}{{{body}}}\n'

    css = (f'      #{fid} .an{{opacity:0;animation-duration:{steps * secs}s;animation-iteration-count:infinite;'
           f'animation-timing-function:linear}}\n')
    css += ''.join(keyframes(k, v) for k, v in spans.items())
    css += (f'      @media (prefers-reduced-motion: reduce){{#{fid} .an{{animation:none;opacity:0}}'
            f'#{fid} .v1,#{fid} .pg1,#{fid} .hl,#{fid} .c5{{opacity:1}}}}\n')
    s = s.replace('    </style>', css + '    </style>', 1)
    s = s.replace(f'<svg id="{fid}"', f'<svg id="{fid}" data-steps="{steps}" data-step-seconds="{secs}"', 1)

    w, ph = 260, 500
    inner = '<rect width="260" height="56" fill="#F1ECF8"/>' + txt(18, 35, 'Mi app', 17, 500)
    inner += (f'<g class="an pg0">{icon("home", w / 2, 210, "#6750A4", 3)}'
              + txt(w / 2, 270, 'HomePage', 16, 600, INK, 'middle', 'mono') + '</g>')
    inner += (f'<g class="an pg1">{icon("chat", w / 2, 210, "#0F8478", 3)}'
              + txt(w / 2, 270, 'ChatsPage', 16, 600, INK, 'middle', 'mono') + '</g>')
    by = ph - 64
    inner += f'<rect y="{by}" width="{w}" height="64" fill="{BAR_BG}"/>'
    for i, (name, label) in enumerate(DEMO):
        cx = w * (2 * i + 1) / 6
        if i == 0:
            inner += f'<g class="an pg0"><rect x="{cx - 26:.1f}" y="{by + 11}" width="52" height="28" rx="14" fill="{PILL}"/>{icon(name, f"{cx:.1f}", by + 25, SELECTED)}{txt(f"{cx:.1f}", by + 54, label, 12, 600, SELECTED, "middle")}</g>'
            inner += f'<g class="an pg1">{icon(name, f"{cx:.1f}", by + 25, MUTED)}{txt(f"{cx:.1f}", by + 54, label, 12, 600, MUTED, "middle")}</g>'
        elif i == 1:
            inner += f'<g class="an pg0">{icon(name, f"{cx:.1f}", by + 25, MUTED)}{txt(f"{cx:.1f}", by + 54, label, 12, 600, MUTED, "middle")}</g>'
            inner += f'<g class="an pg1"><rect x="{cx - 26:.1f}" y="{by + 11}" width="52" height="28" rx="14" fill="{PILL}"/>{icon(name, f"{cx:.1f}", by + 25, SELECTED)}{txt(f"{cx:.1f}", by + 54, label, 12, 600, SELECTED, "middle")}</g>'
        else:
            inner += icon(name, f'{cx:.1f}', by + 25, MUTED) + txt(f'{cx:.1f}', by + 54, label, 12, 600, MUTED, 'middle')
    inner += f'<circle class="an tap" cx="{w / 2}" cy="{by + 25}" r="17" fill="#2F6FD6" fill-opacity=".18" stroke="#2F6FD6" stroke-width="2"/>'
    inner += f'<rect class="an hl" x="4" y="60" width="{w - 8}" height="{by - 66}" rx="12" fill="none" stroke="#2F6FD6" stroke-width="2.5"/>'
    s += '  ' + device(72, 120, w, ph, inner, '#FFFFFF', f'{fid}-scr') + '\n'

    sx, sw = 420, 492
    s += '  ' + txt(sx, 130, 'STATE DE HOMESCREEN', 12, 700, MUTED, cls='h') + '\n'
    s += f'  <rect x="{sx}" y="144" width="{sw}" height="56" rx="12" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/>\n'
    s += '  ' + txt(sx + 20, 178, 'int _currentIndex =', 15, 600, INK, cls='mono') + '\n'
    s += (f'  <g class="an v0"><rect x="{sx + 224}" y="156" width="48" height="32" rx="8" fill="#FFFFFF" stroke="#7439B8" stroke-width="2"/>'
          + txt(sx + 248, 178, '0', 17, 700, '#7439B8', 'middle', 'mono') + '</g>\n')
    s += (f'  <g class="an v1"><rect x="{sx + 224}" y="156" width="48" height="32" rx="8" fill="#FFF3DC" stroke="#A96C05" stroke-width="2"/>'
          + txt(sx + 248, 178, '1', 17, 700, '#A96C05', 'middle', 'mono') + '</g>\n')
    rows = [
        ('r1', 'onTap(1)', 'La barra avisa qué botón se tocó.'),
        ('r2', 'setState(() => _currentIndex = 1)', 'Cambia el número y pide reconstruir.'),
        ('r3', 'build()', 'Flutter vuelve a construir la Screen.'),
        ('r4', '_buildPage() → ChatsPage()', 'El switch elige la Page del número.'),
    ]
    s += f'  <path d="M{sx + 30},266 V{232 + 3 * 86 + 34}" stroke="#C4CBD8" stroke-width="2"/>\n'
    for i, (cls, code, line) in enumerate(rows):
        y = 232 + i * 86
        s += f'  <rect x="{sx}" y="{y}" width="{sw}" height="68" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
        s += f'  <rect class="an {cls}" x="{sx}" y="{y}" width="{sw}" height="68" rx="12" fill="#EEF4FF" stroke="#2F6FD6" stroke-width="2.5"/>\n'
        s += (f'  <circle cx="{sx + 30}" cy="{y + 34}" r="13" fill="#FFFFFF" stroke="#2F6FD6" stroke-width="2"/>'
              + txt(sx + 30, y + 38.5, str(i + 1), 13, 700, '#2F6FD6', 'middle') + '\n')
        s += '  ' + txt(sx + 56, y + 29, code, 14, 700, INK, cls='mono', fit=sw - 72) + '\n'
        s += '  ' + txt(sx + 56, y + 50, line, 13, 400, '#454C61', fit=sw - 72) + '\n'

    caps = [
        ('1', 'Tocas Chats: la barra llama a onTap con su índice, 1.'),
        ('2', 'setState cambia _currentIndex de 0 a 1.'),
        ('3', 'Como hubo setState, build() corre otra vez.'),
        ('4', 'En build, _buildPage() entra al switch y devuelve ChatsPage.'),
        ('5', 'El body muestra ChatsPage y la barra resalta Chats.'),
    ]
    for i, (n, text) in enumerate(caps, start=1):
        s += (f'  <g class="an c{i}"><circle cx="{sx + 14}" cy="{h - 44}" r="13" fill="#2F6FD6"/>'
              + txt(sx + 14, h - 39.5, n, 13, 700, '#FFFFFF', 'middle')
              + txt(sx + 36, h - 39, text, 14, 500, INK, fit=sw - 40) + '</g>\n')
    return s + '</svg>\n'


FIGS['biCiclo'] = bi_ciclo


# ───────────────────────────── S0068 · IndexedStack


def kid_card(x, y, w, idx, name, tag, kind):
    """kind: visible, alive (oculta y viva) o ghost (no existe)."""
    fill, border, tag_fill, tag_ink, dash = {
        'visible': ('#FFFFFF', '#6750A4', '#E8F6E3', '#3A8235', ''),
        'alive': ('#F4EBFF', '#C9A6EE', '#EEF1FF', '#4453C9', ''),
        'ghost': ('#FBFBFD', '#C4CBD8', '#EFF1F5', '#556074', ' stroke-dasharray="6 5"'),
    }[kind]
    o = f'<rect x="{x}" y="{y}" width="{w}" height="56" rx="10" fill="{fill}" stroke="{border}" stroke-width="1.5"{dash}/>'
    o += txt(x + 16, y + 23, idx if isinstance(idx, str) else f'children[{idx}]', 12.5, 700,
             '#6750A4' if kind != 'ghost' else FAINT, cls='mono')
    o += txt(x + 16, y + 43, name, 13, 400, INK if kind != 'ghost' else FAINT, cls='mono')
    if kind == 'ghost':
        o += f'<path d="M{x + 14},{y + 39} H{x + 18 + len(name) * 7.8}" stroke="{FAINT}" stroke-width="1.5"/>'
    tw = len(tag) * 6.8 + 20
    o += (f'<rect x="{x + w - tw - 12}" y="{y + 17}" width="{tw:.1f}" height="22" rx="11" fill="{tag_fill}"/>'
          + txt(x + w - tw / 2 - 12, y + 32, tag, 11.5, 600, tag_ink, 'middle'))
    return o


def is_pila():
    fid = 'isPila'
    s = start(fid, 520, 'Lo que hay en el body, pestaña por pestaña', 'Lo que hay en el body, pestaña por pestaña',
              'Con el switch solo existe la Page que se ve. Con IndexedStack existen las tres y solo se pinta una.',
              'Dos columnas con la pestaña Chats abierta. La primera, con el switch: solo existe ChatsPage, visible; '
              'HomePage y ProfilePage aparecen punteadas y tachadas porque no existen. La segunda, con IndexedStack: '
              'los tres hijos existen; ChatsPage, el número 1, es la visible, y HomePage y ProfilePage están ocultas '
              'pero vivas. Debajo, tres tarjetas: al cambiar de pestaña con el switch la Page sale y pierde su State; '
              'IndexedStack las conserva; y el costo es que las tres viven en memoria desde el arranque.')
    cw = 392
    cols = [(48, 'switch (_currentIndex)', 'Solo existe la que se ve'),
            (520, 'IndexedStack(index: 1)', 'Existen las tres, se pinta una')]
    for x, name, sub in cols:
        s += '  ' + txt(x, 128, name, 14, 700, INK, cls='mono', fit=cw) + '\n'
        s += '  ' + txt(x, 148, sub, 12.5, 400, MUTED, fit=cw) + '\n'
    names = ['HomePage()', 'ChatsPage()', 'ProfilePage()']
    for i, n in enumerate(names):
        y = 172 + i * 68
        if i == 1:
            s += '  ' + kid_card(48, y, cw, 'case 1', n, 'visible · borrador: Hola', 'visible') + '\n'
            s += '  ' + kid_card(520, y, cw, i, n, 'visible · borrador: Hola', 'visible') + '\n'
        else:
            s += '  ' + kid_card(48, y, cw, 'case 0' if i == 0 else 'default', n, 'no existe', 'ghost') + '\n'
            s += '  ' + kid_card(520, y, cw, i, n, 'oculta · sigue viva', 'alive') + '\n'
    s += f'  <path d="M480,120 V376" stroke="#D9DEE8" stroke-width="1.5" stroke-dasharray="4 5"/>\n'
    outs = [
        ('rose', 'Con switch, se pierde', ['Al cambiar de pestaña sale del árbol:', 'dispose(). Al volver, State nuevo.']),
        ('green', 'Con IndexedStack, se queda', ['index solo decide cuál se pinta.', 'El borrador sigue ahí al volver.']),
        ('amber', 'El costo', ['Las tres viven en memoria y corren', 'su initState() al arrancar la app.']),
    ]
    for i, (color, title, rows) in enumerate(outs):
        s += '  ' + card(48 + i * 296, 400, 272, 88, color, title, rows) + '\n'
    return s + '</svg>\n'


FIGS['isPila'] = is_pila


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--inject':
        done = set()
        for name in LESSONS:
            path = ROOT / 'content' / name
            text = path.read_text(encoding='utf-8')

            def swap(m):
                if m.group(1) not in FIGS:
                    return m.group(0)
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
