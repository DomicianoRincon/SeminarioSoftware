"""Figuras SVG de las lecciones de la sesión 7 (S0046 a S0049 y el taller S0045).

    python3 tools/sesion7_figuras.py <carpeta>     escribe un .svg por figura, para revisarlas
    python3 tools/sesion7_figuras.py --inject      reemplaza cada bloque ```svg de las lecciones
                                                   de la sesión por la figura con el mismo id

Lo que se aprende tocando (el paquete que baja y sube entre widgets) va en el bloque
```interactive lift; estas figuras son las vistas fijas que lo acompañan.
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sesion2_figuras import FAM, head  # noqa: E402
from sesion3_figuras import device, mark, txt  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
LESSONS = ['lessonS45.md', 'lessonS46.md', 'lessonS47.md', 'lessonS48.md', 'lessonS49.md']
INK, MUTED, FAINT = '#161A26', '#556074', '#79809A'
DOWN, UP = '#2F6FD6', '#C27A0E'

FIGS = {}


def markers(fid):
    out = ''
    for name, color in (('down', DOWN), ('up', UP), ('gray', '#9AA1B2')):
        out += (f'<marker id="{fid}-{name}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                f'markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">'
                f'<path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="{color}"/></marker>')
    return out


def start(fid, h, title, plain, sub, desc):
    s = head(fid, h, title, plain, sub, desc)
    return s.replace('  </defs>', '    ' + markers(fid) + '\n  </defs>', 1)


def flow(fid, d, kind, dashed=False):
    color = {'down': DOWN, 'up': UP, 'gray': '#9AA1B2'}[kind]
    dash = ' stroke-dasharray="6 5"' if dashed else ''
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.25"{dash} '
            f'marker-end="url(#{fid}-{kind})"/>')


def widget(x, y, w, name, color='slate', tag='', h=44, sub=''):
    soft, border, strong = FAM[color]
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{soft}" stroke="{border}" stroke-width="1.5"/>'
    o += txt(x + 14, y + (26 if not sub else 22), name, 14, 700, INK, cls='mono', fit=w - 28)
    if sub:
        o += txt(x + 14, y + 40, sub, 12, 400, MUTED, fit=w - 28)
    if tag:
        o += txt(x + w - 12, y + 26, tag, 12, 600, strong, 'end')
    return o


def param(x, y, label, kind):
    """A constructor parameter: blue = data that comes down, orange = event that goes up,
    gray = received only to hand it to a child."""
    fill, border, ink = {
        'down': ('#E6F0FF', '#7FA6E8', '#1F4FA8'),
        'up': ('#FFF3DC', '#E2B25C', '#8A5600'),
        'gray': ('#F1F2F5', '#B8BDC9', '#79809A'),
    }[kind]
    w = round(len(label) * 7.4 + 18)
    dash = ' stroke-dasharray="4 3"' if kind == 'gray' else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="22" rx="11" fill="{fill}" stroke="{border}"{dash}/>'
            + txt(x + w / 2, y + 15.5, label, 12, 600, ink, 'middle', 'mono')), w


def params(x, y, items):
    o = ''
    for label, kind in items:
        chip, w = param(x, y, label, kind)
        o += chip
        x += w + 6
    return o


def card(x, y, w, h, color, title, rows, num=None):
    soft, border, strong = FAM[color]
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#FFFFFF" stroke="{border}" stroke-width="1.5"/>'
    tx = x + 16
    if num is not None:
        o += (f'<circle cx="{x + 28}" cy="{y + 26}" r="13" fill="#FFFFFF" stroke="{strong}" stroke-width="2"/>'
              + txt(x + 28, y + 30.5, str(num), 13, 700, strong, 'middle'))
        tx = x + 50
    o += txt(tx, y + 31, title, 14.5, 700, INK, fit=x + w - tx - 12)
    for i, row in enumerate(rows):
        o += txt(x + 16, y + 58 + i * 19, row, 13, 400, '#454C61', fit=w - 32)
    return o


# ───────────────────────────── S0048 · Modelos con copyWith


def song_object(x, y, num, rows, color):
    soft, border, strong = FAM[color]
    o = f'<rect x="{x}" y="{y}" width="300" height="196" rx="12" fill="#FFFFFF" stroke="{border}" stroke-width="1.5"/>'
    o += f'<path d="M{x},{y + 12} A12,12 0 0 1 {x + 12},{y} H{x + 288} A12,12 0 0 1 {x + 300},{y + 12} V{y + 40} H{x} Z" fill="{soft}"/>'
    o += txt(x + 16, y + 26, f'Song #{num}', 14, 700, strong, cls='mono')
    for i, (name, value, note, hl) in enumerate(rows):
        ry = y + 52 + i * 34
        if hl:
            o += f'<rect x="{x + 8}" y="{ry}" width="284" height="28" rx="6" fill="{FAM[hl][0]}" stroke="{FAM[hl][1]}"/>'
        o += txt(x + 18, ry + 19, name, 13, 600, INK, cls='mono')
        o += txt(x + 120, ry + 19, value, 13, 400, '#454C61', cls='mono', fit=118)
        if note:
            o += txt(x + 286, ry + 19, note, 11.5, 600, FAM[hl][2] if hl else FAINT, 'end')
    return o


def cw_copia():
    fid = 'cwCopia'
    s = start(fid, 520, '<tspan class="mono">copyWith</tspan>: una copia con un campo cambiado',
              'copyWith: una copia con un campo cambiado',
              'Song tiene sus campos final: no se puede cambiar. Se crea otra Song igual, salvo lo que cambia.',
              'A la izquierda, Song número 1 con título Yellow, artista Coldplay, la URL de la imagen e isFavorite en '
              'false. Una flecha con song.copyWith(isFavorite: true) lleva a Song número 2, con los tres primeros '
              'campos copiados e isFavorite en true. Debajo, el intento song.isFavorite = true marcado como error '
              'porque el campo es final, y la lista _songs, cuya posición 1 ahora apunta a la Song nueva.')
    old = [('title', "'Yellow'", '', None), ('artist', "'Coldplay'", '', None),
           ('imageUrl', "'…/400'", '', None), ('isFavorite', 'false', '', 'rose')]
    new = [('title', "'Yellow'", 'copiado', None), ('artist', "'Coldplay'", 'copiado', None),
           ('imageUrl', "'…/400'", 'copiado', None), ('isFavorite', 'true', 'cambia', 'green')]
    s += '  ' + song_object(48, 112, 1, old, 'slate') + '\n'
    s += '  ' + song_object(612, 112, 2, new, 'green') + '\n'
    s += '  ' + flow(fid, 'M356,210 H604', 'down') + '\n'
    s += '  <rect x="364" y="166" width="232" height="30" rx="8" fill="#1F2430"/>\n'
    s += '  ' + txt(480, 186, 'song.copyWith(', 13, 400, '#C9CFDA', 'middle', 'mono') + '\n'
    s += '  <rect x="364" y="218" width="232" height="28" rx="8" fill="#1F2430"/>\n'
    s += '  ' + txt(480, 237, 'isFavorite: true)', 13, 400, '#A8D8A0', 'middle', 'mono') + '\n'

    s += '  <rect x="48" y="332" width="300" height="56" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/>\n'
    s += '  ' + txt(64, 356, 'song.isFavorite = true;', 13, 700, '#C2354F', cls='mono') + '\n'
    s += '  ' + txt(64, 376, 'No compila: isFavorite es final.', 12.5, 400, '#454C61') + '\n'

    s += '  ' + txt(48, 428, 'LA LISTA DE LA SCREEN', 12, 700, MUTED, cls='h') + '\n'
    labels = [('[0]', 'Song #3 · Imagine', 'slate'), ('[1]', 'Song #2 · Yellow ♥', 'green'), ('[2]', 'Song #4 · Levitating', 'slate')]
    for i, (idx, label, color) in enumerate(labels):
        x = 48 + i * 288
        soft, border, strong = FAM[color]
        s += f'  <rect x="{x}" y="440" width="272" height="36" rx="8" fill="{soft}" stroke="{border}" stroke-width="1.5"/>\n'
        s += '  ' + txt(x + 14, 463, idx, 13, 700, strong, cls='mono') + '\n'
        s += '  ' + txt(x + 48, 463, label, 13, 600, INK, fit=212) + '\n'
    s += '  ' + flow(fid, 'M700,308 V372 H472 V434', 'down', dashed=True) + '\n'
    s += '  ' + txt(712, 352, '_songs[1] = la copia', 12.5, 600, DOWN, cls='mono') + '\n'
    s += '  ' + txt(48, 504, 'Song #1 no se tocó: ya nadie la usa y Dart la recoge. La Screen cambió su lista dentro de setState.',
                    12.5, 400, MUTED, fit=864) + '\n'
    return s + '</svg>\n'


FIGS['cwCopia'] = cw_copia


# ───────────────────────────── S0049 · Prop drilling


def code_box(x, y, w, title, kind, rows, color):
    """Dark editor box. `rows` are (text, highlight) pairs; highlight is a substring to box."""
    soft, border, strong = FAM[color]
    h = 56 + len(rows) * 22 + 12
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#1F2430"/>'
    o += f'<path d="M{x},{y + 12} A12,12 0 0 1 {x + 12},{y} H{x + w - 12} A12,12 0 0 1 {x + w},{y + 12} V{y + 36} H{x} Z" fill="{soft}"/>'
    o += txt(x + 14, y + 24, title, 14, 700, INK, cls='mono')
    o += txt(x + w - 12, y + 24, kind, 12, 600, strong, 'end')
    spots = {}
    for i, (line, hl) in enumerate(rows):
        ly = y + 62 + i * 22
        indent = len(line) - len(line.lstrip())
        if hl:
            start_col = line.index(hl)
            hx = x + 14 + start_col * 7.5 - 3
            hw = len(hl) * 7.5 + 6
            o += f'<rect x="{hx}" y="{ly - 15}" width="{hw}" height="21" rx="5" fill="#2F6FD6" fill-opacity=".28" stroke="#7FA6E8"/>'
            spots.setdefault(hl, (hx, ly - 15, hw, 21))
        o += (f'<text x="{x + 14 + indent * 7.5}" y="{ly}" font-size="12.5" fill="#C9CFDA" class="mono" '
              f'textLength="{len(line.lstrip()) * 7.5}" lengthAdjust="spacingAndGlyphs">{line.lstrip()}</text>')
    return o, h, spots


def pd_camino():
    """Animada: seis pasos de 2,5 s. A la izquierda la pantalla se construye; a la derecha se
    ilumina el código que la construye y la flecha por la que baja el dato."""
    fid, h = 'pdCamino', 720
    steps, secs = 6, 2.5
    s = start(fid, h, 'El camino de una canción', 'El camino de una canción',
              'La pantalla se construye de arriba abajo: cada nivel recibe el dato por su constructor y se lo pasa al siguiente.',
              'Animación en seis pasos. A la izquierda, un celular; a la derecha, el código de PlaylistScreen, SongList y '
              'SongCard, uno debajo del otro, con flechas que van de _songs al campo songs de SongList y de song al campo '
              'song de SongCard. Uno: la pantalla en blanco. Dos: PlaylistScreen construye la barra y guarda tres canciones '
              'en _songs. Tres: la lista baja a SongList, que dibuja un esqueleto de tres filas. Cuatro, cinco y seis: el for '
              'de SongList crea una SongCard por canción y cada una llena su fila.')
    pct = lambda k: round(k * 100 / steps, 2)
    spans = {
        'k2': [(pct(1), pct(2))], 'k3': [(pct(2), pct(3))], 'k456': [(pct(3), 100)],
        'f2': [(pct(1), 100)], 'f3': [(pct(2), 100)],
        'f4': [(pct(3), 100)], 'f5': [(pct(4), 100)], 'f6': [(pct(5), 100)],
        'c1': [(0, pct(1))], 'c2': [(pct(1), pct(2))], 'c3': [(pct(2), pct(3))],
        'c4': [(pct(3), pct(4))], 'c5': [(pct(4), pct(5))], 'c6': [(pct(5), 100)],
    }

    def keyframes(name, sp):
        pts = {0: 0, 100: 0}
        for a, b in sp:
            pts.update({a: 0, round(a + 1.5, 2): 1, round(b - 1.5, 2): 1, b: 0})
        body = ' '.join(f'{k}%{{opacity:{v}}}' for k, v in sorted(pts.items()))
        return f'      #{fid} .{name}{{animation-name:{fid}-{name}}}\n      @keyframes {fid}-{name}{{{body}}}\n'

    css = (f'      #{fid} .an{{opacity:0;animation-duration:{steps * secs}s;animation-iteration-count:infinite;'
           f'animation-timing-function:linear}}\n')
    css += ''.join(keyframes(k, v) for k, v in spans.items())
    css += (f'      @media (prefers-reduced-motion: reduce){{#{fid} .an{{animation:none;opacity:1}}'
            f'#{fid} .cap,#{fid} .glow{{opacity:0}}#{fid} .c6{{opacity:1}}}}\n')
    s = s.replace('    </style>', css + '    </style>', 1)
    s = s.replace(f'<svg id="{fid}"', f'<svg id="{fid}" data-steps="{steps}" data-step-seconds="{secs}"', 1)

    # ── right: the three components, top to bottom
    boxes = [
        (112, 'PlaylistScreen', 'guarda', 'violet', [
            ('final List<Song> _songs = […];', None), ('…', None), ('SongList(songs: _songs),', '_songs')]),
        (280, 'SongList', 'recibe y reparte', 'indigo', [
            ('final List<Song> songs;', None), ('const SongList({super.key, required this.songs});', 'this.songs'),
            ('for (final song in songs)', None), ('  SongCard(song: song),', 'song)')]),
        (470, 'SongCard', 'recibe y muestra', 'indigo', [
            ('final Song song;', None), ('const SongCard({super.key, required this.song});', 'this.song'),
            ('Text(song.title),', None), ('Text(song.artist),', None)]),
    ]
    glow = ['k2', 'k3', 'k456']
    spots = []
    for (y, title, kind, color, rows), g in zip(boxes, glow):
        o, bh, sp = code_box(440, y, 472, title, kind, rows, color)
        s += '  ' + o.replace('List<Song>', 'List&lt;Song&gt;') + '\n'
        s += (f'  <rect class="an glow {g}" x="436" y="{y - 4}" width="480" height="{bh + 8}" rx="15" fill="none" '
              f'stroke="#2F6FD6" stroke-width="3"/>\n')
        spots.append(sp)
    for (a, b, cls) in ((spots[0]['_songs'], spots[1]['this.songs'], 'k3'), (spots[1]['song)'], spots[2]['this.song'], 'k456')):
        d = f'M{a[0] + a[2]},{a[1] + 10} H932 V{b[1] + 10} H{b[0] + b[2] + 28}'
        s += f'  <path d="{d}" fill="none" stroke="#C4CBD8" stroke-width="2" marker-end="url(#{fid}-gray)"/>\n'
        s += '  ' + flow(fid, d, 'down').replace('<path ', f'<path class="an {cls}" ', 1) + '\n'

    # ── captions under the code
    caps = [
        ('1', 'La app arranca: todavía no hay nada que mostrar.'),
        ('2', 'PlaylistScreen construye la barra y guarda tres canciones.'),
        ('3', 'La lista baja a SongList, que arma una fila por canción.'),
        ('4', 'El for de SongList crea la primera SongCard y le pasa su song.'),
        ('5', 'Segunda vuelta del for: otra SongCard, otra song.'),
        ('6', 'Tercera vuelta: la lista está completa. Nadie tomó el dato del aire.'),
    ]
    for i, (n, text) in enumerate(caps, start=1):
        s += (f'  <g class="an cap c{i}"><circle cx="454" cy="664" r="13" fill="#2F6FD6"/>'
              + txt(454, 668.5, n, 13, 700, '#FFFFFF', 'middle')
              + txt(476, 669, text, 14, 500, INK, fit=436) + '</g>\n')

    # ── left: the phone, built step by step
    w, ph = 300, 560
    inner = f'<g class="an f2"><rect width="{w}" height="56" fill="#D0BCFF"/>' + txt(16, 35, 'Mi playlist', 17, 500) + '</g>'
    inner += f'<rect class="an k2" x="3" y="3" width="{w - 6}" height="{ph - 6}" rx="18" fill="none" stroke="#7439B8" stroke-width="2" stroke-dasharray="6 5"/>'
    inner += f'<g class="an k2">' + txt(w / 2, ph / 2, 'PlaylistScreen', 13, 700, '#7439B8', 'middle', 'mono') + '</g>'
    inner += f'<g class="an f3"><rect x="10" y="70" width="{w - 20}" height="272" rx="12" fill="none" stroke="#4453C9" stroke-width="1.5" stroke-dasharray="6 5"/>'
    inner += txt(w - 18, 88, 'SongList', 12, 700, '#4453C9', 'end', 'mono') + '</g>'
    songs = [('Imagine', 'John Lennon'), ('Yellow', 'Coldplay'), ('Levitating', 'Dua Lipa')]
    for i, (t, a) in enumerate(songs):
        y = 96 + i * 80
        inner += (f'<g class="an f3"><rect x="22" y="{y}" width="{w - 44}" height="68" rx="12" fill="#EEF0F4"/>'
                  f'<rect x="32" y="{y + 10}" width="48" height="48" rx="10" fill="#DDE1E8"/>'
                  f'<rect x="92" y="{y + 18}" width="110" height="11" rx="5" fill="#DDE1E8"/>'
                  f'<rect x="92" y="{y + 38}" width="76" height="9" rx="4" fill="#DDE1E8"/></g>')
        inner += (f'<g class="an f{4 + i}"><rect x="22" y="{y}" width="{w - 44}" height="68" rx="12" fill="#FFFFFF" stroke="#E6E0F2"/>'
                  f'<rect x="32" y="{y + 10}" width="48" height="48" rx="10" fill="#9C7FE0"/>'
                  + txt(92, y + 30, t, 14, 700) + txt(92, y + 49, a, 12.5, 400, '#625B71') + '</g>')
        inner += (f'<rect class="an c{4 + i}" x="18" y="{y - 4}" width="{w - 36}" height="76" rx="14" fill="none" '
                  f'stroke="#2F6FD6" stroke-width="2.5"/>')
    s += '  ' + device(72, 120, w, ph, inner, '#FFFFFF', f'{fid}-clip') + '\n'
    return s + '</svg>\n'


FIGS['pdCamino'] = pd_camino


def drill_column(x, y, title, color, rows):
    soft, border, strong = FAM[color]
    o = f'<rect x="{x}" y="{y}" width="420" height="344" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>'
    o += f'<path d="M{x},{y + 14} A14,14 0 0 1 {x + 14},{y} H{x + 406} A14,14 0 0 1 {x + 420},{y + 14} V{y + 40} H{x} Z" fill="{soft}"/>'
    o += txt(x + 18, y + 26, title, 14, 700, strong, fit=384)
    cy = y + 60
    step = (344 - 76) // len(rows)
    for i, (name, chips, used) in enumerate(rows):
        ny = cy + i * step
        if i:
            o += f'<path d="M{x + 40},{ny - step + 44} V{ny}" stroke="#C4CBD8" stroke-width="1.5"/>'
        fill = '#FFFFFF' if used else '#F6F7F9'
        o += f'<rect x="{x + 18}" y="{ny}" width="384" height="44" rx="10" fill="{fill}" stroke="{"#C9A6EE" if i == 0 else "#D9DEE8"}" stroke-width="1.5"/>'
        o += txt(x + 32, ny + 27, name, 13.5, 700, INK if used else FAINT, cls='mono', fit=150)
        o += params(x + 176, ny + 11, chips)
    return o


def pd_niveles():
    fid = 'pdNiveles'
    s = start(fid, 640, 'Prop drilling: pasar algo que no se usa', 'Prop drilling: pasar algo que no se usa',
              'Un widget recibe un parámetro solo para entregárselo a su hijo. Un nivel se tolera; varios duelen.',
              'Dos columnas. A la izquierda, la playlist: PlaylistScreen, SongList con songs y SongCard con song, todos '
              'en azul porque cada uno usa lo que recibe. A la derecha, una app más grande: la Screen, una Page y una '
              'sección reciben songs en gris sin usarlo, solo para pasarlo, hasta SongList y SongCard. '
              'Debajo, tres señales de que el drilling empieza a doler.')
    s += '  ' + drill_column(48, 112, 'La playlist: cada nivel usa lo que recibe', 'green', [
        ('PlaylistScreen', [], True),
        ('SongList', [('songs', 'down')], True),
        ('SongCard', [('song', 'down')], True),
    ]) + '\n'
    s += '  ' + drill_column(492, 112, 'Una app más grande: cuatro niveles', 'rose', [
        ('HomeScreen', [], True),
        ('LibraryPage', [('songs', 'gray')], False),
        ('RecentSection', [('songs', 'gray')], False),
        ('SongList', [('songs', 'down')], True),
        ('SongCard', [('song', 'down')], True),
    ]) + '\n'
    signals = [
        ('Recibe lo que no usa', ['Un widget tiene en su', 'constructor algo que solo pasa.']),
        ('Un cambio, tres archivos', ['Agregar un dato obliga a', 'tocar tres archivos o más.']),
        ('Cinco parámetros o más', ['El constructor ya no se lee', 'de un vistazo.']),
    ]
    for i, (title, rows) in enumerate(signals):
        s += '  ' + card(48 + i * 296, 480, 272, 104, 'amber', title, rows, num=i + 1) + '\n'
    s += '  ' + txt(48, 616, 'En este curso el drilling corto es lo correcto: es explícito y se sigue con los ojos.',
                    12.5, 400, MUTED, fit=864) + '\n'
    return s + '</svg>\n'


FIGS['pdNiveles'] = pd_niveles


# ───────────────────────────── S0045 · Taller


def folder(x, y, name, depth, kind='dir', tag=None):
    ix = x + depth * 28
    if kind == 'dir':
        icon = (f'<path d="M{ix},{y - 9} h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" '
                f'stroke-linejoin="round"/>')
    else:
        icon = f'<rect x="{ix + 2}" y="{y - 11}" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/>'
    o = icon + txt(ix + 28, y + 4, name, 13.5, 700 if kind == 'dir' else 400, INK, cls='mono')
    if tag:
        label, color = tag
        soft, border, strong = FAM[color]
        w = len(label) * 7.2 + 20
        o += f'<rect x="420" y="{y - 11}" width="{w}" height="22" rx="11" fill="{soft}" stroke="{border}"/>'
        o += txt(420 + w / 2, y + 4, label, 12, 600, strong, 'middle')
    return o


def ta_carpetas():
    fid = 'taCarpetas'
    s = start(fid, 481, 'Los archivos de <tspan class="mono">playlist_app</tspan>',
              'Los archivos de playlist_app',
              'Un archivo por clase. Solo dos guardan estado: la Screen y el formulario.',
              'La carpeta lib con main.dart y tres carpetas: models con song.dart, components con song_card.dart, '
              'song_form.dart y song_list.dart, y screens con playlist_screen.dart. Al lado de cada archivo, una '
              'etiqueta: playlist_screen y song_form son StatefulWidget y guardan estado; los demás son Stateless.')
    rows = [
        ('lib/', 0, 'dir', None),
        ('main.dart', 1, 'file', ('App y la tabla de rutas', 'slate')),
        ('models/', 1, 'dir', None),
        ('song.dart', 2, 'file', ('Song con copyWith', 'slate')),
        ('components/', 1, 'dir', None),
        ('playlist_summary.dart', 2, 'file', ('Stateless', 'slate')),
        ('song_card.dart', 2, 'file', ('Stateless', 'slate')),
        ('song_form.dart', 2, 'file', ('StatefulWidget · guarda el borrador', 'violet')),
        ('song_list.dart', 2, 'file', ('Stateless', 'slate')),
        ('screens/', 1, 'dir', None),
        ('playlist_screen.dart', 2, 'file', ('StatefulWidget · guarda _songs', 'violet')),
    ]
    s += '  <rect x="48" y="104" width="864" height="345" rx="14" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
    for i, (name, depth, kind, tag) in enumerate(rows):
        s += '  ' + folder(72, 136 + i * 29, name, depth, kind, tag) + '\n'
    return s + '</svg>\n'


FIGS['taCarpetas'] = ta_carpetas


def ta_meta():
    fid = 'taMeta'
    s = start(fid, 600, 'Lo que vas a agregar', 'Lo que vas a agregar',
              'La playlist de las lecciones, con dos mejoras más. Las dos salen de la Screen y vuelven a ella.',
              'Un celular con la playlist: arriba del formulario, una fila con el texto 3 canciones y un corazón para '
              'filtrar favoritas; debajo, el formulario de tres campos y tres tarjetas con el corazón y la '
              'papelera. Dos marcas numeradas señalan el contador y el filtro, '
              'cada una con su tarjeta a la derecha.')
    w, h = 300, 470

    def heart(hx, hy, full, color='#C2354F'):
        return (f'<path d="M{hx},{hy} l-7,-7 a4.2,4.2 0 0 1 7,-5 a4.2,4.2 0 0 1 7,5 Z" '
                f'fill="{color if full else "none"}" stroke="{color}" stroke-width="1.8" stroke-linejoin="round"/>')

    inner = f'<rect width="{w}" height="56" fill="#D0BCFF"/>'
    inner += txt(16, 34, 'Mi playlist', 17, 500)
    inner += txt(16, 86, '3 canciones', 13.5, 500, '#1C1B1F')
    inner += heart(w - 26, 88, False)
    for i, label in enumerate(('Canción', 'Artista', 'URL de la imagen')):
        inner += f'<rect x="16" y="{104 + i * 40}" width="{w - 32}" height="32" rx="4" fill="none" stroke="#79747E"/>'
        inner += txt(28, 125 + i * 40, label, 12.5, 400, '#79747E')
    inner += f'<rect x="16" y="226" width="{w - 32}" height="32" rx="16" fill="#6750A4"/>'
    inner += txt(w / 2, 247, 'Agregar', 13, 600, '#FFFFFF', 'middle')
    songs = [('Imagine', 'John Lennon', False), ('Yellow', 'Coldplay', True), ('Levitating', 'Dua Lipa', False)]
    for i, (t, a, fav) in enumerate(songs):
        y = 268 + i * 66
        inner += f'<rect x="12" y="{y}" width="{w - 24}" height="60" rx="14" fill="#FFFFFF" stroke="#E6E0F2"/>'
        inner += f'<rect x="22" y="{y + 8}" width="44" height="44" rx="10" fill="#9C7FE0"/>'
        inner += txt(80, y + 27, t, 13.5, 700)
        inner += txt(80, y + 44, a, 12, 400, '#625B71')
        inner += heart(w - 58, y + 36, fav)
        tx = w - 28
        inner += (f'<path d="M{tx - 6},{y + 24} H{tx + 6} M{tx - 4},{y + 24} L{tx - 3},{y + 38} H{tx + 3} L{tx + 4},{y + 24}" '
                  f'fill="none" stroke="#49454F" stroke-width="1.6" stroke-linejoin="round"/>')
    px, py = 80, 104
    s += '  ' + device(px, py, w, h, inner, '#FEF7FF', f'{fid}-clip') + '\n'
    s += '  ' + mark(px + 10, py + 68, 96, 26, 'amber', 8) + '\n'
    s += '  ' + mark(px + w - 42, py + 68, 32, 26, 'rose', 8) + '\n'
    cards = [
        ('amber', 'El resumen', ['PlaylistSummary, arriba del formulario: recibe', 'count desde _songs.length y el corazón.']),
        ('rose', 'Solo favoritas', ['El corazón avisa a la Screen, que guarda el bool.', 'SongList recibe la lista ya filtrada.']),
    ]
    for k, (color, title, body) in enumerate(cards):
        y = 112 + k * 148
        s += '  ' + card(480, y, 432, 124, color, title, body, num=k + 1) + '\n'
    chips = [(px + 120, py + 81, 1, 'amber'), (px + w - 58, py + 81, 2, 'rose')]
    for cx, cy, n, color in chips:
        strong = FAM[color][2]
        s += (f'  <circle cx="{cx}" cy="{cy}" r="13" fill="#FFFFFF" stroke="{strong}" stroke-width="2"/>'
              + txt(cx, cy + 4.5, str(n), 13, 700, strong, 'middle') + '\n')
    s += '  ' + txt(480, 424, 'Y una prueba: un print en cada build para ver quién se reconstruye.', 12.5, 400, MUTED, fit=432) + '\n'
    return s + '</svg>\n'


FIGS['taMeta'] = ta_meta


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
