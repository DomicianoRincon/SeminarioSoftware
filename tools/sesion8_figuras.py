"""Figuras SVG de las lecciones de la sesión 8 (S0050 a S0055).

    python3 tools/sesion8_figuras.py <carpeta>     escribe un .svg por figura, para revisarlas
    python3 tools/sesion8_figuras.py --inject      reemplaza cada bloque ```svg de las lecciones
                                                   de la sesión por la figura con el mismo id

Lo que se aprende tocando (la pila que crece y se encoge, el await que espera) va en los
bloques ```interactive nav-stack y nav-result; estas figuras son las vistas fijas.
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from code_frame import frame  # noqa: E402
from sesion2_figuras import FAM, head, note  # noqa: E402
from sesion3_figuras import device, txt  # noqa: E402
from sesion7_figuras import card, folder  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
LESSONS = ['lessonS50.md', 'lessonS51.md', 'lessonS52.md', 'lessonS53.md', 'lessonS54.md', 'lessonS55.md']
INK, MUTED, FAINT = '#161A26', '#556074', '#79809A'
PUSH, POP, RESET = '#2F6FD6', '#C27A0E', '#C2354F'
KINDS = {'push': PUSH, 'pop': POP, 'reset': RESET}

FIGS = {}


def start(fid, h, title, plain, sub, desc):
    s = head(fid, h, title, plain, sub, desc)
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


def legend(x, y):
    o = ''
    items = [('push', 'pushNamed · abre encima'), ('pop', 'pop · vuelve a la de abajo'),
             ('reset', 'pushNamedAndRemoveUntil · rehace la pila')]
    for kind, label in items:
        o += f'<path d="M{x},{y} H{x + 28}" stroke="{KINDS[kind]}" stroke-width="2.5"/>'
        o += txt(x + 36, y + 4.5, label, 12.5, 500, '#454C61')
        x += 36 + len(label) * 7 + 36
    return o


# ───────────────────────────── piezas de las maquetas


def appbar(w, title, back=False, action=None, k=1.0):
    h = 40 * k
    o = f'<rect width="{w}" height="{h}" fill="#D0BCFF"/>'
    tx = 12 * k
    if back:
        o += txt(12 * k, 26 * k, '←', 15 * k, 600)
        tx = 32 * k
    o += txt(tx, 26 * k, title, 13.5 * k, 600, INK, fit=w - tx - (30 if action else 8) * k)
    if action == 'logout':
        o += logout_icon(w - 20 * k, 20 * k, k)
    return o


def logout_icon(cx, cy, k=1.0):
    """Icons.logout: a door bracket and an arrow that leaves it."""
    u = 6 * k
    return (f'<path d="M{cx - u * .2},{cy - u} H{cx - u} V{cy + u} H{cx - u * .2}" fill="none" stroke="{INK}" '
            f'stroke-width="{1.6 * k}" stroke-linejoin="round"/>'
            f'<path d="M{cx - u * .4},{cy} H{cx + u * 1.1} M{cx + u * .5},{cy - u * .6} L{cx + u * 1.1},{cy} '
            f'L{cx + u * .5},{cy + u * .6}" fill="none" stroke="{INK}" stroke-width="{1.6 * k}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def song_row(x, y, w, title, artist, k=1.0):
    h = 42 * k
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{10 * k}" fill="#FFFFFF" stroke="#E6E0F2"/>'
    o += f'<rect x="{x + 6 * k}" y="{y + 6 * k}" width="{30 * k}" height="{30 * k}" rx="{7 * k}" fill="#9C7FE0"/>'
    o += txt(x + 44 * k, y + 19 * k, title, 11.5 * k, 700, INK, fit=w - 52 * k)
    o += txt(x + 44 * k, y + 33 * k, artist, 10 * k, 400, '#625B71', fit=w - 52 * k)
    return o


def button(cx, y, w, label, k=1.0):
    return (f'<rect x="{cx - w / 2}" y="{y}" width="{w}" height="{26 * k}" rx="{13 * k}" fill="#6750A4"/>'
            + txt(cx, y + 17 * k, label, 11.5 * k, 600, '#FFFFFF', 'middle'))


def screen_login(w, h):
    o = f'<circle cx="{w / 2}" cy="{h * .36}" r="22" fill="#EADDFF"/>'
    o += txt(w / 2, h * .36 + 7, '♫', 20, 700, '#6750A4', 'middle')
    o += txt(w / 2, h * .36 + 50, 'Mi playlist', 14, 700, INK, 'middle')
    o += button(w / 2, h * .36 + 66, 84, 'Entrar')
    return o


def screen_playlist(w, h):
    o = appbar(w, 'Mi playlist', action='logout')
    for i, (t, a) in enumerate([('Imagine', 'John Lennon'), ('Yellow', 'Coldplay'), ('Levitating', 'Dua Lipa')]):
        o += song_row(8, 50 + i * 48, w - 16, t, a)
    o += f'<rect x="{w - 44}" y="{h - 46}" width="34" height="34" rx="10" fill="#EADDFF"/>'
    o += txt(w - 27, h - 23, '+', 18, 600, '#21005D', 'middle')
    return o


def screen_detail(w, h):
    o = appbar(w, 'Yellow', back=True)
    side = min(w - 48, 70)
    o += f'<rect x="{(w - side) / 2}" y="54" width="{side}" height="{side}" rx="14" fill="#9C7FE0"/>'
    o += txt(w / 2, 72 + side, 'Yellow', 13, 700, INK, 'middle')
    o += txt(w / 2, 88 + side, 'Coldplay', 11, 400, '#625B71', 'middle')
    o += button(w / 2, 100 + side, w - 30, 'Volver')
    return o


def screen_add(w, h):
    o = appbar(w, 'Nueva canción', back=True)
    for i, label in enumerate(('Canción', 'Artista')):
        o += f'<rect x="10" y="{54 + i * 36}" width="{w - 20}" height="28" rx="4" fill="none" stroke="#79747E"/>'
        o += txt(18, 72 + i * 36, label, 11, 400, '#79747E')
    o += button(w / 2, 132, w - 20, 'Agregar')
    return o


def phone_at(fid, key, x, y, w, h, inner):
    return device(x, y, w, h, inner, '#FEF7FF', f'{fid}-{key}')


def label_above(cx, y, route, screen):
    return (txt(cx, y - 26, route, 13, 700, '#6750A4', 'middle', 'mono')
            + txt(cx, y - 10, screen, 12, 500, MUTED, 'middle', 'mono'))


# ───────────────────────────── S0050 · Taller


def tn_meta():
    fid = 'tnMeta'
    s = start(fid, 660, 'Las cuatro pantallas de la playlist', 'Las cuatro pantallas de la playlist',
              'Cada flecha es una llamada al Navigator. El color dice cuál: abrir encima, volver o rehacer la pila.',
              'Cuatro celulares. A la izquierda LoginScreen con el botón Entrar; en el centro PlaylistScreen con tres '
              'canciones, el botón de cerrar sesión y el botón más; a la derecha, arriba, SongDetailScreen con la '
              'canción Yellow, y abajo AddSongScreen con el formulario. Entrar y Cerrar sesión, en rojo, usan '
              'pushNamedAndRemoveUntil. Tocar una canción y el botón más, en azul, usan pushNamed: el primero manda '
              'la canción en arguments y el segundo espera un resultado con await. Volver y Agregar, en naranja, '
              'usan pop; Agregar devuelve la canción nueva.')
    lw, lh = 156, 290
    rw, rh = 140, 210
    lx, px, rx = 56, 324, 720
    ly = 212
    dy, ay = 128, 404
    s += '  ' + label_above(lx + lw / 2, ly, "'/'", 'LoginScreen') + '\n'
    s += '  ' + label_above(px + lw / 2, ly, "'/playlist'", 'PlaylistScreen') + '\n'
    s += '  ' + label_above(rx + rw / 2, dy, "'/song'", 'SongDetailScreen') + '\n'
    s += '  ' + label_above(rx + rw / 2, ay, "'/add-song'", 'AddSongScreen') + '\n'
    s += '  ' + phone_at(fid, 'l', lx, ly, lw, lh, screen_login(lw, lh)) + '\n'
    s += '  ' + phone_at(fid, 'p', px, ly, lw, lh, screen_playlist(lw, lh)) + '\n'
    s += '  ' + phone_at(fid, 'd', rx, dy, rw, rh, screen_detail(rw, rh)) + '\n'
    s += '  ' + phone_at(fid, 'a', rx, ay, rw, rh, screen_add(rw, rh)) + '\n'

    e1, e2 = lx + lw + 12, px - 12
    s += '  ' + nav(fid, f'M{e1},{ly + 110} H{e2}', 'reset') + '\n'
    s += '  ' + chip((e1 + e2) / 2, ly + 88, 'Entrar', 'reset') + '\n'
    s += '  ' + nav(fid, f'M{e2},{ly + 190} H{e1}', 'reset') + '\n'
    s += '  ' + chip((e1 + e2) / 2, ly + 212, 'Cerrar sesión', 'reset') + '\n'

    p1, r1 = px + lw + 12, rx - 12
    s += '  ' + nav(fid, f'M{p1},{ly + 70} C{p1 + 100},{ly + 70} {r1 - 110},{dy + 70} {r1},{dy + 70}', 'push') + '\n'
    s += '  ' + chip(600, 152, 'toque · arguments', 'push') + '\n'
    s += '  ' + nav(fid, f'M{r1},{dy + 150} C{r1 - 90},{dy + 150} {p1 + 90},{ly + 112} {p1},{ly + 112}', 'pop') + '\n'
    s += '  ' + chip(612, 300, 'Volver · pop', 'pop') + '\n'
    s += '  ' + nav(fid, f'M{p1},{ly + 200} C{p1 + 90},{ly + 200} {r1 - 100},{ay + 70} {r1},{ay + 70}', 'push') + '\n'
    s += '  ' + chip(596, 420, '+ · await', 'push') + '\n'
    s += '  ' + nav(fid, f'M{r1},{ay + 150} C{r1 - 110},{ay + 150} {p1 + 100},{ly + 250} {p1},{ly + 250}', 'pop') + '\n'
    s += '  ' + chip(612, 540, 'Agregar · pop(song)', 'pop') + '\n'

    s += '  ' + legend(56, 628) + '\n'
    return s + '</svg>\n'


FIGS['tnMeta'] = tn_meta


def tn_carpetas():
    fid = 'tnCarpetas'
    s = start(fid, 568, 'Los archivos de <tspan class="mono">playlist_app</tspan> al terminar',
              'Los archivos de playlist_app al terminar',
              'Tres pantallas nuevas en screens/. Los componentes no cambian de carpeta ni saben que hay navegación.',
              'La carpeta lib con main.dart, que tiene la tabla de las cuatro rutas, y tres carpetas: models con '
              'song.dart; components con playlist_summary.dart de la sesión 7, song_card.dart, song_form.dart y '
              'song_list.dart; y screens con login_screen.dart, playlist_screen.dart, song_detail_screen.dart y '
              'add_song_screen.dart. Las tres pantallas nuevas están marcadas como nuevas, y cada archivo dice si '
              'guarda estado.')
    new = ('nueva', 'green')
    rows = [
        ('lib/', 0, 'dir', None, None),
        ('main.dart', 1, 'file', ('App y la tabla de las cuatro rutas', 'indigo'), None),
        ('models/', 1, 'dir', None, None),
        ('song.dart', 2, 'file', ('Song con copyWith', 'slate'), None),
        ('components/', 1, 'dir', None, None),
        ('playlist_summary.dart', 2, 'file', ('de la sesión 7', 'slate'), None),
        ('song_card.dart', 2, 'file', ('Stateless · ahora con onTap', 'slate'), None),
        ('song_form.dart', 2, 'file', ('StatefulWidget · guarda el borrador', 'violet'), None),
        ('song_list.dart', 2, 'file', ('Stateless · ahora con onOpen', 'slate'), None),
        ('screens/', 1, 'dir', None, None),
        ('login_screen.dart', 2, 'file', ('StatefulWidget · el nombre', 'violet'), new),
        ('playlist_screen.dart', 2, 'file', ('StatefulWidget · guarda _songs', 'violet'), None),
        ('song_detail_screen.dart', 2, 'file', ('Stateless · lee arguments', 'slate'), new),
        ('add_song_screen.dart', 2, 'file', ('Stateless · hospeda el formulario', 'slate'), new),
    ]
    s += '  <rect x="48" y="104" width="864" height="432" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
    for i, (name, depth, kind, tag, extra) in enumerate(rows):
        y = 136 + i * 29
        s += '  ' + folder(72, y, name, depth, kind, tag) + '\n'
        if extra:
            label, color = extra
            soft, border, strong = FAM[color]
            s += (f'  <rect x="812" y="{y - 11}" width="72" height="22" rx="11" fill="{soft}" stroke="{border}"/>'
                  + txt(848, y + 4, label, 12, 700, strong, 'middle') + '\n')
    return s + '</svg>\n'


FIGS['tnCarpetas'] = tn_carpetas


# ───────────────────────────── S0051 · La pila


def stack_card(x, y, w, route, screen, tag, kind):
    """kind: top (visible), alive (debajo), cross (sale), new (recién llegada)."""
    fill, border, tag_fill, tag_ink = {
        'top': ('#FFFFFF', '#6750A4', '#E8F6E3', '#3A8235'),
        'alive': ('#F4EBFF', '#C9A6EE', '#EEF1FF', '#4453C9'),
        'cross': ('#FFEBEF', '#F3A3B2', '#FFEBEF', '#C2354F'),
    }[kind]
    o = f'<rect x="{x}" y="{y}" width="{w}" height="52" rx="10" fill="{fill}" stroke="{border}" stroke-width="1.5"/>'
    o += txt(x + 16, y + 22, route, 13, 700, '#6750A4', cls='mono')
    o += txt(x + 16, y + 41, screen, 12.5, 400, INK, cls='mono')
    if kind == 'cross':
        o += f'<path d="M{x + 14},{y + 37} H{x + 18 + len(screen) * 7.5}" stroke="#C2354F" stroke-width="1.5"/>'
    tw = len(tag) * 6.8 + 20
    o += (f'<rect x="{x + w - tw - 12}" y="{y + 15}" width="{tw:.1f}" height="22" rx="11" fill="{tag_fill}"/>'
          + txt(x + w - tw / 2 - 12, y + 30, tag, 11.5, 600, tag_ink, 'middle'))
    return o


def base_line(x, y, w):
    return (f'<path d="M{x},{y} H{x + w}" stroke="#C4CBD8" stroke-width="3"/>'
            + txt(x + w / 2, y + 18, 'base de la pila', 11.5, 500, FAINT, 'middle'))


def pl_pila():
    fid = 'plPila'
    s = start(fid, 520, 'La pila de pantallas', 'La pila de pantallas',
              'El Navigator guarda las pantallas abiertas una encima de otra. Solo se ve la de arriba.',
              'A la izquierda, un celular con SongDetailScreen de la canción Yellow. A la derecha, la pila con tres '
              'tarjetas: arriba la ruta /song con SongDetailScreen, visible; en medio /playlist con PlaylistScreen y '
              'abajo / con LoginScreen, las dos marcadas como debajo y vivas. Una flecha azul entra por arriba: '
              'pushNamed pone una encima. Una flecha naranja sale por arriba: pop quita la de arriba. Debajo, tres '
              'tarjetas: solo se ve la de arriba, las de abajo siguen vivas, y atrás es un pop.')
    w, h = 170, 270
    s += '  ' + phone_at(fid, 'p', 72, 120, w, h, screen_detail(w, h)) + '\n'
    sx, sw = 404, 372
    s += '  ' + txt(sx, 128, 'LA PILA DEL NAVIGATOR', 12, 700, MUTED, cls='h') + '\n'
    s += '  ' + stack_card(sx, 200, sw, "'/song'", 'SongDetailScreen', 'visible', 'top') + '\n'
    s += '  ' + stack_card(sx, 262, sw, "'/playlist'", 'PlaylistScreen', 'debajo · viva', 'alive') + '\n'
    s += '  ' + stack_card(sx, 324, sw, "'/'", 'LoginScreen', 'debajo · viva', 'alive') + '\n'
    s += '  ' + base_line(sx, 390, sw) + '\n'
    s += '  ' + f'<path d="M{72 + w + 18},{226} H{sx - 14}" stroke="#9AA1B2" stroke-width="1.75" stroke-dasharray="5 5"/>' + '\n'
    s += '  ' + nav(fid, f'M{sx + 110},{140} V{190}', 'push') + '\n'
    s += '  ' + txt(sx + 100, 162, 'pushNamed', 12.5, 700, PUSH, 'end', 'mono') + '\n'
    s += '  ' + txt(sx + 100, 178, 'pone una encima', 12, 400, '#454C61', 'end') + '\n'
    s += '  ' + nav(fid, f'M{sx + 262},{190} V{140}', 'pop') + '\n'
    s += '  ' + txt(sx + 274, 162, 'pop', 12.5, 700, POP, cls='mono') + '\n'
    s += '  ' + txt(sx + 274, 178, 'quita la de arriba', 12, 400, '#454C61') + '\n'
    cards = [
        ('violet', 'Solo se ve la de arriba', ['La pantalla visible es la última', 'que entró a la pila.']),
        ('indigo', 'Las de abajo siguen vivas', ['No se destruyen: su State y sus', 'datos esperan intactos.']),
        ('amber', 'Atrás es un pop', ['La flecha del AppBar y el botón', 'del sistema sacan la de arriba.']),
    ]
    for i, (color, title, rows) in enumerate(cards):
        s += '  ' + card(48 + i * 296, 420, 272, 84, color, title, rows) + '\n'
    return s + '</svg>\n'


FIGS['plPila'] = pl_pila


# ───────────────────────────── S0052 · Rutas nombradas


def rn_tabla_result():
    o = note(12, 'amber', 'initialRoute', ['El nombre de la ruta con la que', 'arranca la pila.'], 60)
    o += note(84, 'violet', 'LoginScreen', ["'/' es la primera que se ve."], 46)
    o += note(150, 'indigo', 'PlaylistScreen', ["'/playlist' se abre al tocar Entrar."], 46)
    return o


FIGS['rnTabla'] = lambda: frame(dict(
    id='rnTabla',
    title='La tabla <tspan class="mono">routes:</tspan> de <tspan class="mono">MaterialApp</tspan>',
    title_plain='La tabla routes: de MaterialApp',
    desc='El código de MaterialApp con initialRoute igual a barra y la tabla routes con dos entradas: barra '
         'construye LoginScreen y barra playlist construye PlaylistScreen. Una flecha de initialRoute a una tarjeta '
         'que explica que es la ruta con la que arranca la pila, y una flecha de cada nombre a la Screen que '
         'construye. Debajo, dos tarjetas: pushNamed busca el nombre en la tabla y pone esa Screen encima; pop '
         'quita la de arriba.',
    sub='Cada nombre apunta a una función que construye su Screen. Navegar es decir un nombre.',
    file='lib/main.dart',
    panel='QUÉ CONSTRUYE CADA NOMBRE',
    code=[
        "MaterialApp(",
        "  initialRoute: '/',",
        "  routes: {",
        "    '/': (context) => const LoginScreen(),",
        "    '/playlist': (context) =>",
        "        const PlaylistScreen(),",
        "  },",
        ")",
    ],
    result=rn_tabla_result(),
    arrows=[
        dict(line=1, find="'/'", to=(16, 46), color='amber', lane=0),
        dict(line=3, find="'/'", to=(16, 95), color='violet', lane=1),
        dict(line=4, find="'/playlist'", to=(16, 173), color='indigo', lane=2),
    ],
    cards=[
        ('indigo', "pushNamed(context, '/playlist')",
         ['Busca el nombre en routes: y pone', 'esa Screen encima de la pila.']),
        ('amber', 'pop(context)',
         ['Quita la de arriba. La flecha del AppBar', 'y el atrás del sistema hacen lo mismo.']),
    ],
))


# ───────────────────────────── S0053 · Rehacer la pila


def ru_pila():
    fid = 'ruPila'
    s = start(fid, 476, 'Entrar sin dejar el login debajo', 'Entrar sin dejar el login debajo',
              'Con pushNamed el login sigue en la pila. Con pushNamedAndRemoveUntil sale, y atrás ya no vuelve a él.',
              'Tres columnas. La primera, con pushNamed: la pila tiene PlaylistScreen encima de LoginScreen, y atrás '
              'vuelve al login. La segunda, con pushNamedAndRemoveUntil: PlaylistScreen entra arriba y LoginScreen, '
              'abajo, aparece tachada porque el predicado route flecha false responde que no se queda. La tercera, '
              'la pila nueva: solo PlaylistScreen, y atrás cierra la app.')
    cw = 264
    cols = [48, 348, 648]
    heads = [('pushNamed', PUSH, 'El login queda debajo'),
             ('pushNamedAndRemoveUntil', RESET, 'Entra y pregunta por las de abajo'),
             ('La pila nueva', '#3A8235', 'Solo queda la playlist')]
    for x, (name, color, sub) in zip(cols, heads):
        s += '  ' + txt(x, 128, name, 14, 700, color, cls='mono' if name != 'La pila nueva' else '', fit=cw) + '\n'
        s += '  ' + txt(x, 148, sub, 12.5, 400, MUTED, fit=cw) + '\n'
    x = cols[0]
    s += '  ' + stack_card(x, 176, cw, "'/playlist'", 'PlaylistScreen', 'visible', 'top') + '\n'
    s += '  ' + stack_card(x, 238, cw, "'/'", 'LoginScreen', 'debajo · viva', 'alive') + '\n'
    s += '  ' + base_line(x, 304, cw) + '\n'
    x = cols[1]
    s += '  ' + stack_card(x, 176, cw, "'/playlist'", 'PlaylistScreen', 'entra', 'top') + '\n'
    s += '  ' + stack_card(x, 238, cw, "'/'", 'LoginScreen', '(route) => false', 'cross') + '\n'
    s += '  ' + base_line(x, 304, cw) + '\n'
    x = cols[2]
    s += '  ' + stack_card(x, 238, cw, "'/playlist'", 'PlaylistScreen', 'visible', 'top') + '\n'
    s += '  ' + base_line(x, 304, cw) + '\n'
    s += '  ' + nav(fid, f'M{cols[0] + cw + 8},{258} H{cols[1] - 8}', 'reset') + '\n'
    s += '  ' + nav(fid, f'M{cols[1] + cw + 8},{258} H{cols[2] - 8}', 'reset') + '\n'
    outs = [
        ('rose', 'Atrás vuelve al login', ['La persona ya entró y el botón', 'atrás la saca otra vez.']),
        ('amber', 'El predicado decide', ['Se llama con cada ruta de abajo.', 'false = esa ruta sale.']),
        ('green', 'Atrás cierra la app', ['No hay nada debajo. El AppBar', 'tampoco pone la flecha.']),
    ]
    for i, (color, title, rows) in enumerate(outs):
        s += '  ' + card(cols[i], 348, cw, 84, color, title, rows) + '\n'
    return s + '</svg>\n'


FIGS['ruPila'] = ru_pila


# ───────────────────────────── S0054 · arguments


def pa_args_result():
    o = '<rect x="16" y="16" width="328" height="124" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>'
    o += txt(32, 42, 'La ruta nueva · settings', 12, 700, '#4453C9', cls='h')
    o += '<rect x="28" y="56" width="304" height="30" rx="7" fill="#FFFFFF" stroke="#D9DEE8"/>'
    o += txt(40, 76, "name: '/song'", 13, 400, INK, cls='mono')
    o += '<rect x="28" y="96" width="304" height="30" rx="7" fill="#E6F0FF" stroke="#7FA6E8"/>'
    o += txt(40, 116, "arguments: Song('Yellow')", 13, 600, '#1F4FA8', cls='mono')
    o += note(160, 'amber', 'as Song', ['arguments llega como Object?.', 'as Song le dice a Dart qué es.'], 62)
    return o


FIGS['paArgs'] = lambda: frame(dict(
    id='paArgs',
    title='La canción viaja en <tspan class="mono">arguments</tspan>',
    title_plain='La canción viaja en arguments',
    desc='Arriba, en PlaylistScreen, Navigator.pushNamed con context, el nombre barra song y arguments igual a song. '
         'Abajo, en SongDetailScreen, final song igual a ModalRoute.of context, settings.arguments as Song. A la '
         'derecha, la ruta nueva con su settings: name barra song y arguments con la canción Yellow. Una flecha va '
         'del nombre al name, otra de arguments a arguments, y otra de settings.arguments a la misma caja. La '
         'última va de as Song a una tarjeta que explica que arguments llega como Object con signo de pregunta. '
         'Debajo, el error que sale si se olvida arguments.',
    sub='pushNamed mete la canción en la ruta nueva. La pantalla que llega la saca de ahí en su build.',
    file='lib/screens/',
    panel='LO QUE LLEVA LA RUTA',
    min_h=276,
    code=[
        "Navigator.pushNamed(",
        "  context,",
        "  '/song',",
        "  arguments: song,",
        ");",
        "",
        "final song = ModalRoute.of(context)!",
        "    .settings.arguments as Song;",
    ],
    result=pa_args_result(),
    arrows=[
        dict(line=2, find="'/song'", to=(28, 71), color='indigo', lane=0),
        dict(line=3, find="arguments", to=(28, 108), color='teal', lane=1),
        dict(line=7, find="as Song", to=(16, 190), color='amber', lane=0),
    ],
    cards=[
        ('rose', "type 'Null' is not a subtype of type 'Song' in type cast",
         ['Se olvidó arguments en el pushNamed: la ruta llegó vacía, settings.arguments vale null y el as Song falla.']),
    ],
))


# ───────────────────────────── S0055 · resultado


def re_await_result():
    o = note(16, 'violet', 'await', ['_openAddSong queda en pausa aquí', 'hasta que AddSongScreen haga pop.'], 64)
    o += note(92, 'rose', 'result is Song', ['result es lo que mandó pop, o null', 'si se volvió con atrás sin guardar.'], 64)
    o += note(168, 'green', '_addSong(result)', ['El setState de siempre. Aquí ya se', 'sabe que result es una Song.'], 64)
    return o


FIGS['reAwait'] = lambda: frame(dict(
    id='reAwait',
    title='Abrir una pantalla y esperar su respuesta',
    title_plain='Abrir una pantalla y esperar su respuesta',
    desc='El código de _openAddSong, una función async: final result igual a await Navigator.pushNamed con context y '
         'barra add-song; si result is Song, llama a _addSong con result. Tres tarjetas a la derecha: await deja la '
         'función en pausa hasta el pop; result es lo que mandó pop o null si se volvió con atrás; y _addSong es el '
         'setState de siempre. Debajo, dos tarjetas: Navigator.pop con context y song, que cierra y entrega la '
         'canción, y Navigator.pop solo con context, el del botón atrás, que entrega null.',
    sub='pushNamed devuelve un Future. Lo que se mande en el pop llega en result.',
    file='lib/screens/playlist_screen.dart',
    panel='QUÉ PASA EN CADA LÍNEA',
    code=[
        "Future<void> _openAddSong() async {",
        "  final result = await Navigator.pushNamed(",
        "    context,",
        "    '/add-song',",
        "  );",
        "  if (result is Song) {",
        "    _addSong(result);",
        "  }",
        "}",
    ],
    result=re_await_result(),
    arrows=[
        dict(line=1, find='await', to=(16, 48), color='violet', lane=0, end='v'),
        dict(line=5, find='result is Song', to=(16, 124), color='rose', lane=1),
        dict(line=6, find='_addSong(result)', to=(16, 200), color='green', lane=2),
    ],
    cards=[
        ('green', 'Navigator.pop(context, song)',
         ['En AddSongScreen: cierra la pantalla', 'y entrega song como resultado.']),
        ('rose', 'Navigator.pop(context)',
         ['El atrás del sistema: cierra sin', 'resultado, y result llega null.']),
    ],
))


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
