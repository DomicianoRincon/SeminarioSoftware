"""Figuras SVG de las lecciones de la sesión 6 (S0040 a S0045).

    python3 tools/sesion6_figuras.py <carpeta>     escribe un .svg por figura, para revisarlas
    python3 tools/sesion6_figuras.py --inject      reemplaza cada bloque ```svg de content/lessonS4[0-5].md
                                                   por la figura con el mismo id

Lo que se aprende tocando (el contador, el árbol, el ciclo de vida y la playlist) va en
bloques ```interactive; estas figuras son las vistas fijas que los acompañan.
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

FIGS = {}


def box(x, y, w, h, color, rx=12, dashed=False):
    soft, border, _ = FAM[color]
    dash = ' stroke-dasharray="6 5"' if dashed else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{soft}" '
            f'stroke="{border}" stroke-width="1.5"{dash}/>')


def chip(cx, cy, n, color):
    _, border, strong = FAM[color]
    return (f'<circle cx="{cx}" cy="{cy}" r="13" fill="#FFFFFF" stroke="{strong}" stroke-width="2"/>'
            + txt(cx, cy + 4.5, str(n), 13, 700, strong, 'middle'))


def lines(x, y, rows, size=13, fill='#454C61', step=19, cls='', fit=None, anchor='start'):
    cw = size * 0.6 if cls == 'mono' else 0
    return ''.join(txt(x + cw * (len(r) - len(r.lstrip())), y + i * step, r.lstrip(), size, 400, fill, anchor, cls, fit)
                   for i, r in enumerate(rows))


def arrow(d):
    return f'<path class="link" d="{d}"/>'


# ───────────────────────────── S0040 · Stateless frente a Stateful


def ew_pantalla():
    fid = 'ewPantalla'
    s = head(fid, 640, 'El estado detrás de una pantalla', 'El estado detrás de una pantalla',
             'A la izquierda, la app con sus datos. A la derecha, los datos que pueden cambiar: el estado.',
             'Un reproductor de música en un celular: la barra con el título Mi playlist, la canción que suena '
             '(Levitating, de Dua Lipa), un botón de pausa, 12 me gusta y una lista de tres canciones. A la '
             'derecha, la sección Estado con cuatro variables, cada una con una flecha de su color hacia la '
             'parte de la pantalla que la muestra: _current a la canción que suena, _isPlaying al botón de '
             'pausa, _likes al contador de me gusta y _songs a la lista. Una nota gris señala que el título de '
             'la barra no es estado porque nunca cambia.')
    colors = {'violet': '#7439B8', 'amber': '#A96C05', 'rose': '#C2354F', 'teal': '#0F8478', 'slate': '#79809A'}
    marks = ''.join(
        f'<marker id="{fid}-{c}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        f'markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="{v}"/></marker>'
        for c, v in colors.items())
    s = s.replace('  </defs>', '    ' + marks + '\n    ' + GRAD.format(f'{fid}-cover') + '\n  </defs>', 1)

    px, py, pw, ph = 96, 112, 320, 456
    s += f'  <rect x="{px - 10}" y="{py - 10}" width="{pw + 20}" height="{ph + 20}" rx="36" fill="#1F2430"/>\n'
    s += f'  <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="26" fill="#FEF7FF"/>\n'
    s += (f'  <path d="M{px},{py + 26} A26,26 0 0 1 {px + 26},{py} H{px + pw - 26} A26,26 0 0 1 {px + pw},{py + 26} '
          f'V{py + 56} H{px} Z" fill="#D0BCFF"/>\n')
    s += '  ' + txt(px + 18, py + 37, 'Mi playlist', 17, 500) + '\n'

    s += f'  <rect x="{px + 14}" y="196" width="{pw - 28}" height="148" rx="16" fill="#FFFFFF" stroke="#E6E0F2"/>\n'
    s += '  ' + cover(px + 28, 208, 56, 12, f'{fid}-cover') + '\n'
    s += '  ' + txt(px + 26, 194 - 6, 'SONANDO AHORA', 11, 700, '#625B71') + '\n'
    s += '  ' + txt(px + 98, 230, 'Levitating', 16, 700) + '\n'
    s += '  ' + txt(px + 98, 250, 'Dua Lipa', 13, 400, '#625B71') + '\n'
    s += f'  <circle cx="{px + pw / 2}" cy="290" r="20" fill="#6750A4"/>\n'
    s += (f'  <rect x="{px + pw / 2 - 7}" y="281" width="5" height="18" rx="1.5" fill="#FFFFFF"/>'
          f'<rect x="{px + pw / 2 + 2}" y="281" width="5" height="18" rx="1.5" fill="#FFFFFF"/>\n')
    hx, hy = px + 34, 326
    s += (f'  <path d="M{hx},{hy + 5} l-6,-6 a3.6,3.6 0 0 1 6,-4 a3.6,3.6 0 0 1 6,4 Z" fill="#C2354F"/>\n')
    s += '  ' + txt(hx + 12, hy + 4, '12 me gusta', 13, 600, '#C2354F') + '\n'

    s += '  ' + txt(px + 18, 376, 'Siguiente en la lista', 13, 700, '#49454F') + '\n'
    queue = [('Imagine', 'John Lennon'), ('Yellow', 'Coldplay'), ('Bohemian Rhapsody', 'Queen')]
    for j, (t, a) in enumerate(queue):
        y = 388 + j * 54
        s += f'  <rect x="{px + 14}" y="{y}" width="{pw - 28}" height="46" rx="12" fill="#FFFFFF" stroke="#E6E0F2"/>\n'
        s += '  ' + cover(px + 22, y + 7, 32, 7, f'{fid}-cover') + '\n'
        s += '  ' + txt(px + 66, y + 21, t, 13.5, 700) + '\n'
        s += '  ' + txt(px + 66, y + 37, a, 12, 400, '#625B71') + '\n'

    s += '  <rect x="504" y="150" width="424" height="324" rx="16" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="2"/>\n'
    s += '  ' + txt(524, 178, 'ESTADO', 13, 700, '#7439B8', cls='h') + '\n'
    s += '  ' + txt(596, 178, 'vive en _PlayerScreenState', 12, 400, '#625B71', cls='mono') + '\n'
    s += '  <path d="M520,192 H912" stroke="#C9A6EE" stroke-width="1.5"/>\n'
    rows = [
        ('violet', 222, 'Song _current', "Song('Levitating', …)", px + pw - 14),
        ('amber', 290, 'bool _isPlaying', 'true', px + pw / 2 + 24),
        ('rose', 326, 'int _likes', '12', hx + 96),
        ('teal', 442, 'List&lt;Song&gt; _songs', '3 canciones', px + pw - 14),
    ]
    for color, y, name, value, tx in rows:
        soft, border, strong = FAM[color]
        s += f'  <rect x="520" y="{y - 16}" width="392" height="32" rx="8" fill="{soft}" stroke="{border}" stroke-width="1.5"/>\n'
        s += '  ' + txt(534, y + 5, name, 13, 700, strong, cls='mono') + '\n'
        s += f'  <rect x="724" y="{y - 11}" width="180" height="22" rx="6" fill="#FFFFFF" stroke="{border}"/>\n'
        s += '  ' + txt(814, y + 4.5, value, 12.5, 600, INK, 'middle', 'mono', 168) + '\n'
        s += (f'  <path d="M520,{y} H{tx + 6}" fill="none" stroke="{strong}" stroke-width="2" '
              f'marker-end="url(#{fid}-{color})"/>\n')
        s += f'  <circle cx="520" cy="{y}" r="3.5" fill="{strong}"/>\n'
    s += f'  <path d="M{px + pw - 14},380 H{px + pw - 6} V{388 + 2 * 54 + 46} H{px + pw - 14}" fill="none" stroke="#0F8478" stroke-width="2"/>\n'
    s += f'  <path d="M{px + pw - 14},200 H{px + pw - 8} V266 H{px + pw - 14}" fill="none" stroke="#7439B8" stroke-width="2"/>\n'

    s += '  ' + txt(520, 128, 'No es estado: el título nunca cambia', 12.5, 400, FAINT) + '\n'
    s += (f'  <path d="M512,124 H360 V144 H198" fill="none" stroke="#79809A" stroke-width="1.5" stroke-dasharray="4 4" '
          f'marker-end="url(#{fid}-slate)"/>\n')

    s += '  ' + txt(520, 504, 'Cada flecha va de un dato a la parte de la pantalla', 13, 400, '#454C61', fit=392) + '\n'
    s += '  ' + txt(520, 524, 'que lo muestra. Si el dato cambia, esa parte cambia.', 13, 400, '#454C61', fit=392) + '\n'
    s += '  ' + txt(48, 612, 'El estado vive en el objeto State de la pantalla. El build() lo lee para dibujar.', 13, 400, MUTED, fit=864) + '\n'
    return s + '</svg>\n'


def note_box(x, y, w, color, title, rows, h=None):
    soft, border, strong = FAM[color]
    h = h or 28 + 19 * len(rows) + 10
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#FFFFFF" stroke="{border}" stroke-width="1.5"/>'
    o += txt(x + 16, y + 22, title, 13.5, 700, strong, fit=w - 32)
    o += lines(x + 16, y + 42, rows, 12.5, '#454C61', 17, fit=w - 32)
    return o


FIGS['ewPantalla'] = ew_pantalla


def ew_anatomia_result():
    o = note(16, 'indigo', 'El widget', ['Hereda de StatefulWidget. Solo guarda', 'la configuración: aquí no va el estado.'], 72)
    o += note(112, 'amber', 'createState()', ['Flutter lo llama una vez y conecta', 'el widget con su objeto State.'], 72)
    o += note(208, 'violet', 'Los datos que cambian', ['Campos normales del State, sin final.', 'Por convención empiezan con _.'], 72)
    o += note(304, 'green', 'build() vive en el State', ['Lee los campos y dibuja la pantalla', 'con lo que valen en ese momento.'], 72)
    return o


FIGS['ewAnatomia'] = lambda: frame(dict(
    id='ewAnatomia',
    title='Las dos clases de un <tspan class="mono">StatefulWidget</tspan>',
    title_plain='Las dos clases de un StatefulWidget',
    desc='El código de HomeScreen, que hereda de StatefulWidget y en createState devuelve un _HomeScreenState. '
         'El State tiene el campo _isOn y el método build. Cuatro tarjetas explican el widget, createState, '
         'los datos que cambian y build.',
    sub='El widget se declara arriba y el State abajo. El estado y el build van en el State.',
    file='lib/screens/home_screen.dart',
    panel='QUÉ HACE CADA PARTE',
    code=[
        "class HomeScreen extends StatefulWidget {",
        "  const HomeScreen({super.key});",
        "",
        "  @override",
        "  State<HomeScreen> createState() =>",
        "      _HomeScreenState();",
        "}",
        "",
        "class _HomeScreenState extends State<HomeScreen> {",
        "  bool _isOn = false;",
        "",
        "  @override",
        "  Widget build(BuildContext context) {",
        "    return Text(_isOn ? 'Sí' : 'No');",
        "  }",
        "}",
    ],
    result=ew_anatomia_result(),
    arrows=[
        dict(line=0, find='StatefulWidget', to=(16, 46), color='indigo'),
        dict(line=4, find='createState', to=(16, 142), color='amber'),
        dict(line=9, find='_isOn', to=(16, 238), color='violet'),
        dict(line=12, find='build', to=(16, 334), color='green'),
    ],
))


# ───────────────────────────── S0041 · setState


def ss_ciclo():
    fid = 'ssCiclo'
    s = head(fid, 372, 'Lo que pasa cuando se pulsa <tspan class="mono">+</tspan>', 'Lo que pasa cuando se pulsa +',
             'setState no dibuja nada: cambia el dato y le avisa a Flutter que el State quedó sucio.',
             'Cuatro pasos en fila. Uno: el toque llama a _incrementCounter. Dos: setState suma uno a _counter y '
             'marca el State como sucio. Tres: Flutter vuelve a llamar build. Cuatro: el Text muestra el valor '
             'nuevo. Una flecha vuelve al inicio. Debajo del paso dos, un aviso: sin setState el dato cambia pero '
             'build no corre y la pantalla no cambia.')
    steps = [
        ('amber', 'El toque', ['onPressed llama a'], ['_incrementCounter()']),
        ('violet', 'setState', ['Cambia el dato y marca', 'el State como sucio.'], ['_counter++']),
        ('indigo', 'build()', ['Flutter lo vuelve a', 'llamar en el siguiente', 'cuadro de la pantalla.'], []),
        ('green', 'La pantalla', ['Text muestra el', 'valor nuevo.'], ["Text('$_counter')"]),
    ]
    for i, (color, title, body, code) in enumerate(steps):
        x = 48 + i * 220
        s += '  ' + box(x, 120, 196, 140, color) + '\n'
        s += '  ' + chip(x + 26, 148, i + 1, color) + '\n'
        s += '  ' + txt(x + 48, 153, title, 15, 700, INK, fit=136) + '\n'
        s += '  ' + lines(x + 18, 186, body, 13, '#454C61', 19, fit=164) + '\n'
        if code:
            s += '  ' + txt(x + 18, 186 + 19 * len(body) + 6, code[0], 13, 600, FAM[color][2], cls='mono', fit=164) + '\n'
        if i < 3:
            s += '  ' + arrow(f'M{x + 198},190 H{x + 218}') + '\n'
    s += '  ' + arrow('M806,262 V288 H146 V264') + '\n'
    s += '  ' + txt(476, 282, 'el siguiente toque empieza otra vuelta', 12, 400, FAINT, 'middle') + '\n'
    soft, border, strong = FAM['rose']
    s += (f'  <rect x="48" y="304" width="864" height="44" rx="10" fill="{soft}" stroke="{border}" stroke-width="1.5"/>\n'
          + '  ' + txt(68, 331, 'Sin setState el paso 2 solo cambia el dato: build() no corre y la pantalla se queda con el valor viejo.',
                       13, 600, strong, fit=824) + '\n')
    return s + '</svg>\n'


FIGS['ssCiclo'] = ss_ciclo


# ───────────────────────────── S0042 · Ciclo de vida




# ───────────────────────────── S0043 · Playlist en texto

SONGS = [('Imagine', 'John Lennon'), ('Yellow', 'Coldplay'), ('Levitating', 'Dua Lipa')]


def field(x, y, w, text, muted=False):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="5" fill="#FFFFFF" stroke="#8D93A5" stroke-width="1.2"/>'
            + txt(x + 8, y + 17, text, 12, 400, FAINT if muted else INK, fit=w - 16))


def pl_flujo():
    fid = 'plFlujo'
    s = head(fid, 424, 'Del formulario a la lista', 'Del formulario a la lista',
             'El botón no pinta nada en la lista: agrega al estado, y build() vuelve a pintar todo.',
             'Cuatro etapas. El formulario con nombre, artista y URL de la imagen y el botón Agregar. La función '
             '_addSong, que dentro de setState agrega a _songs una Song con el texto de los controllers. El estado _songs con '
             'tres canciones. Y build, que pinta un Text por cada canción.')
    titles = [('amber', 'Formulario'), ('violet', '_addSong()'), ('indigo', '_songs'), ('green', 'build()')]
    for i, (color, title) in enumerate(titles):
        x = 48 + i * 220
        s += '  ' + box(x, 120, 196, 232, color) + '\n'
        s += '  ' + chip(x + 26, 148, i + 1, color) + '\n'
        s += '  ' + txt(x + 48, 153, title, 15, 700, INK, cls='mono' if i else '', fit=136) + '\n'
        if i < 3:
            s += '  ' + arrow(f'M{x + 198},236 H{x + 218}') + '\n'
    s += '  ' + field(64, 176, 164, 'Levitating') + '\n'
    s += '  ' + field(64, 210, 164, 'Dua Lipa') + '\n'
    s += '  ' + field(64, 244, 164, 'picsum.photos/400') + '\n'
    s += '  <rect x="64" y="284" width="164" height="30" rx="15" fill="#6750A4"/>\n'
    s += '  ' + txt(146, 304, 'Agregar', 13, 600, '#FFFFFF', 'middle') + '\n'
    code = ['setState(() {', '  _songs.add(Song(', '    title: …,', '    artist: …,', '    imageUrl: …,', '  ));', '});']
    s += '  ' + lines(286, 186, code, 12, '#454C61', 17, 'mono', 160) + '\n'
    for j, (t, a) in enumerate(SONGS):
        y = 178 + j * 50
        s += f'  <rect x="504" y="{y}" width="164" height="40" rx="8" fill="#FFFFFF" stroke="{FAM["indigo"][1]}" stroke-width="1.2"/>\n'
        s += '  ' + txt(514, y + 17, f'[{j}] Song(', 12, 600, FAM['indigo'][2], cls='mono') + '\n'
        s += '  ' + txt(524, y + 33, f"'{t}', …)", 12, 400, '#454C61', cls='mono', fit=140) + '\n'
    for j, (t, a) in enumerate(SONGS):
        s += '  ' + txt(724, 190 + j * 26, f'{t} · {a}', 12.5, 400, INK, fit=168) + '\n'
    s += '  ' + lines(724, 288, ['Un Text por cada', 'canción del estado.'], 12, FAINT, 17) + '\n'
    s += '  ' + txt(48, 388, 'Si setState no envuelve el add, la canción entra a _songs pero la lista de la pantalla no cambia.',
                    13, 400, MUTED, fit=864) + '\n'
    return s + '</svg>\n'


FIGS['plFlujo'] = pl_flujo


# ───────────────────────────── S0044 · SongCard


def cover(x, y, s=64, rx=12, gid='sgCover'):
    return (f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{rx}" fill="url(#{gid})"/>'
            f'<circle cx="{x + s*0.68:.1f}" cy="{y + s*0.32:.1f}" r="{s*0.12:.1f}" fill="#FFFFFF" fill-opacity=".7"/>'
            f'<path d="M{x},{y + s*0.82:.1f} L{x + s*0.36:.1f},{y + s*0.5:.1f} L{x + s*0.62:.1f},{y + s*0.72:.1f} '
            f'L{x + s*0.78:.1f},{y + s*0.6:.1f} L{x + s},{y + s*0.8:.1f} V{y + s - rx} '
            f'A{rx},{rx} 0 0 1 {x + s - rx},{y + s} H{x + rx} A{rx},{rx} 0 0 1 {x},{y + s - rx} Z" fill="#FFFFFF" fill-opacity=".35"/>')


def song_card(x, y, w, title, artist, gid, shadow=True):
    o = ''
    if shadow:
        o += f'<rect x="{x}" y="{y + 4}" width="{w}" height="88" rx="16" fill="#6750A4" fill-opacity=".12"/>'
    o += f'<rect x="{x}" y="{y}" width="{w}" height="88" rx="16" fill="#FFFFFF" stroke="#E6E0F2" stroke-width="1"/>'
    o += cover(x + 12, y + 12, gid=gid)
    o += txt(x + 88, y + 40, title, 15, 700, INK, fit=w - 136)
    o += txt(x + 88, y + 62, artist, 13, 400, '#625B71')
    o += (f'<path d="M{x + w - 30},{y + 34} V{y + 52} M{x + w - 30},{y + 34} L{x + w - 20},{y + 31} V{y + 37} '
          f'L{x + w - 30},{y + 40}" fill="none" stroke="#6750A4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
          f'<circle cx="{x + w - 34}" cy="{y + 53}" r="4" fill="#6750A4"/>')
    return o


GRAD = ('<linearGradient id="{0}" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#B69DF8"/><stop offset="1" stop-color="#6750A4"/></linearGradient>')


def sg_codigo_result():
    o = '<defs>' + GRAD.format('sgCodigo-cover') + '</defs>'
    o += txt(24, 380, "Song('Levitating', 'Dua Lipa', …)", 12, 400, FAINT, cls='mono', fit=312)
    o += song_card(24, 420, 312, 'Levitating', 'Dua Lipa', 'sgCodigo-cover')
    return o


FIGS['sgCodigo'] = lambda: frame(dict(
    id='sgCodigo',
    title='El componente <tspan class="mono">SongCard</tspan>',
    title_plain='El componente SongCard',
    desc='Código resumido de SongCard: un Container blanco con bordes redondeados y sombra, una fila con la '
         'portada redondeada, el título y el artista. Flechas de colores van del borderRadius a la tarjeta, de '
         'Image.network a la portada y de song.title al título.',
    sub='Resumido: el código completo está debajo. Todo lo que muestra sale de la Song que recibe.',
    file='lib/components/song_card.dart',
    panel='RESULTADO',
    code=[
        "Container(",
        "  padding: const EdgeInsets.all(12),",
        "  decoration: BoxDecoration(",
        "    color: Colors.white,",
        "    borderRadius: BorderRadius.circular(16),",
        "    boxShadow: const [BoxShadow(blurRadius: 12)],",
        "  ),",
        "  child: Row(",
        "    children: [",
        "      Container(",
        "        width: 64,",
        "        height: 64,",
        "        clipBehavior: Clip.antiAlias,",
        "        decoration: BoxDecoration(",
        "          borderRadius: BorderRadius.circular(12),",
        "        ),",
        "        child: Image.network(song.imageUrl),",
        "      ),",
        "      Expanded(",
        "        child: Column(",
        "          children: [",
        "            Text(song.title),",
        "            Text(song.artist),",
        "          ],",
        "        ),",
        "      ),",
        "      const Icon(Icons.music_note),",
        "    ],",
        "  ),",
        ")",
    ],
    result=sg_codigo_result(),
    arrows=[
        dict(line=4, find='borderRadius', to=(300, 420), color='amber', end='v'),
        dict(line=16, find='Image.network', to=(68, 432), color='violet', end='v'),
        dict(line=21, find='song.title', to=(190, 466), color='green', end='v'),
    ],
    cards=[
        ('amber', 'Tarjeta', ['Container con color, borde', 'redondeado y sombra suave.']),
        ('violet', 'Portada', ['clipBehavior recorta la imagen', 'con el borde: sin ClipRRect.']),
        ('green', 'Datos', ['song.title y song.artist salen', 'de la Song que recibe.']),
    ],
))


def sg_datos():
    fid = 'sgDatos'
    s = head(fid, 424, 'Del estado a las tarjetas', 'Del estado a las tarjetas',
             'La Screen tiene la lista. Por cada Song crea una SongCard y se la pasa por el constructor.',
             'A la izquierda, el estado _songs de la pantalla con tres canciones. En el centro, el código '
             'for final song in _songs, SongCard song: song. A la derecha, tres tarjetas, cada una conectada con '
             'su canción.')
    s = s.replace('  </defs>', '    ' + GRAD.format('sgDatos-cover') + '\n  </defs>', 1)
    s += '  ' + txt(48, 128, '_PLAYLISTSCREENSTATE', 12, 700, MUTED, cls='h') + '\n'
    s += '  ' + box(48, 140, 268, 236, 'indigo') + '\n'
    s += '  ' + txt(68, 170, 'List&lt;Song&gt; _songs', 14, 700, INK, cls='mono') + '\n'
    for j, (t, a) in enumerate(SONGS):
        y = 188 + j * 60
        s += f'  <rect x="68" y="{y}" width="228" height="44" rx="8" fill="#FFFFFF" stroke="{FAM["indigo"][1]}" stroke-width="1.2"/>\n'
        s += '  ' + txt(80, y + 19, f'[{j}] Song(', 12, 600, FAM['indigo'][2], cls='mono') + '\n'
        s += '  ' + txt(92, y + 36, f"'{t}', '{a}')", 12, 400, '#454C61', cls='mono', fit=196) + '\n'
        s += '  ' + arrow(f'M298,{y + 22} H{592}') + '\n'
    s += '  <rect x="340" y="116" width="236" height="58" rx="10" fill="#1F2430"/>\n'
    s += '  ' + txt(354, 140, 'for (final song in _songs)', 12.5, 400, '#C9CFDA', cls='mono', fit=208) + '\n'
    s += '  ' + txt(354 + 15, 160, 'SongCard(song: song)', 12.5, 400, '#A8D8A0', cls='mono', fit=208) + '\n'
    s += '  ' + txt(456, 196, 'una por canción', 12, 400, FAINT, 'middle') + '\n'
    s += '  ' + txt(600, 128, 'LO QUE SE VE', 12, 700, MUTED, cls='h') + '\n'
    for j, (t, a) in enumerate(SONGS):
        y = 188 + j * 60
        s += f'  <rect x="600" y="{y - 4}" width="312" height="52" rx="12" fill="#FFFFFF" stroke="#E6E0F2" stroke-width="1.2"/>\n'
        s += '  ' + cover(608, y + 2, 40, 8, 'sgDatos-cover') + '\n'
        s += '  ' + txt(660, y + 18, t, 13.5, 700, INK, fit=200) + '\n'
        s += '  ' + txt(660, y + 36, a, 12, 400, '#625B71') + '\n'
    s += '  ' + txt(48, 404, 'SongCard no sabe que existe una lista: solo recibe una Song y la dibuja.',
                    13, 400, MUTED, fit=864) + '\n'
    return s + '</svg>\n'


FIGS['sgDatos'] = sg_datos


# ───────────────────────────── S0045 · Taller


def pt_meta():
    fid = 'ptMeta'
    s = head(fid, 668, 'La playlist que vas a construir', 'La playlist que vas a construir',
             'La app de las dos lecciones anteriores, con cuatro mejoras. Todo el estado sigue en PlaylistScreen.',
             'Maqueta de la app terminada: barra con el título Mi playlist y la cantidad de canciones, el '
             'formulario con un mensaje de error en rojo, y la lista de tarjetas, cada una con un ícono de quitar. '
             'Cuatro tarjetas numeradas explican las mejoras: contador en la barra, mensaje cuando faltan datos, '
             'quitar una canción y mensaje cuando la lista está vacía.')
    s = s.replace('  </defs>', '    ' + GRAD.format('ptMeta-cover') + '\n  </defs>', 1)
    px, py, pw, ph = 96, 112, 320, 528
    s += f'  <rect x="{px - 10}" y="{py - 10}" width="{pw + 20}" height="{ph + 20}" rx="36" fill="#1F2430"/>\n'
    s += f'  <rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="26" fill="#FEF7FF"/>\n'
    s += f'  <path d="M{px},{py + 26} A26,26 0 0 1 {px + 26},{py} H{px + pw - 26} A26,26 0 0 1 {px + pw},{py + 26} V{py + 60} H{px} Z" fill="#D0BCFF"/>\n'
    s += '  ' + txt(px + 18, py + 44, 'Mi playlist', 17, 500) + '\n'
    s += f'  <rect x="{px + 204}" y="{py + 28}" width="100" height="24" rx="12" fill="#FFFFFF" fill-opacity=".7"/>\n'
    s += '  ' + txt(px + 254, py + 45, '3 canciones', 12, 600, '#4F378B', 'middle') + '\n'
    s += '  ' + field(px + 16, py + 76, pw - 32, 'Nombre de la canción', True) + '\n'
    s += '  ' + field(px + 16, py + 110, pw - 32, 'Artista', True) + '\n'
    s += '  ' + field(px + 16, py + 144, pw - 32, 'picsum.photos/400') + '\n'
    s += '  ' + txt(px + 18, py + 190, 'Escribe el nombre y el artista', 12.5, 600, '#C2354F') + '\n'
    s += f'  <rect x="{px + 16}" y="{py + 202}" width="{pw - 32}" height="34" rx="17" fill="#6750A4"/>\n'
    s += '  ' + txt(px + pw / 2, py + 224, 'Agregar', 13.5, 600, '#FFFFFF', 'middle') + '\n'
    for j, (t, a) in enumerate(SONGS):
        y = py + 256 + j * 84
        s += f'  <rect x="{px + 16}" y="{y + 3}" width="{pw - 32}" height="72" rx="14" fill="#6750A4" fill-opacity=".1"/>\n'
        s += f'  <rect x="{px + 16}" y="{y}" width="{pw - 32}" height="72" rx="14" fill="#FFFFFF" stroke="#E6E0F2"/>\n'
        s += '  ' + cover(px + 26, y + 10, 52, 10, 'ptMeta-cover') + '\n'
        s += '  ' + txt(px + 90, y + 32, t, 14, 700, INK, fit=150) + '\n'
        s += '  ' + txt(px + 90, y + 52, a, 12.5, 400, '#625B71') + '\n'
        tx, ty = px + pw - 42, y + 36
        s += (f'  <path d="M{tx - 7},{ty - 6} H{tx + 7} M{tx - 3},{ty - 6} V{ty - 9} H{tx + 3} V{ty - 6} '
              f'M{tx - 5},{ty - 6} L{tx - 4},{ty + 8} H{tx + 4} L{tx + 5},{ty - 6}" fill="none" stroke="#C2354F" '
              f'stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>\n')
    s += '  ' + mark(px + 198, py + 22, 112, 36, 'amber', 18) + '\n'
    s += '  ' + mark(px + 10, py + 172, 210, 26, 'rose', 8) + '\n'
    s += '  ' + mark(px + pw - 60, py + 270, 36, 40, 'violet', 8) + '\n'
    s += '  ' + chip(px + 198, py + 22, 1, 'amber') + '\n'
    s += '  ' + chip(px + 220, py + 172, 2, 'rose') + '\n'
    s += '  ' + chip(px + pw - 24, py + 270, 3, 'violet') + '\n'
    cards = [
        ('amber', 'Contador en la barra', ['El AppBar muestra cuántas canciones hay.', 'Sale de _songs.length.']),
        ('rose', 'Aviso cuando faltan datos', ['Si falta el nombre o el artista, no se agrega', 'y aparece un mensaje en rojo.']),
        ('violet', 'Quitar una canción', ['Cada tarjeta tiene un botón que la saca', 'de _songs dentro de setState.']),
        ('green', 'Lista vacía', ['Sin canciones, en lugar de la lista se ve', 'Todavía no hay canciones.']),
    ]
    for k, (color, title, body) in enumerate(cards):
        y = 112 + k * 132
        soft, border, strong = FAM[color]
        s += f'  <rect x="480" y="{y}" width="432" height="112" rx="12" fill="#FFFFFF" stroke="{border}" stroke-width="1.5"/>\n'
        s += '  ' + chip(508, y + 30, k + 1, color) + '\n'
        s += '  ' + txt(532, y + 35, title, 15, 700, INK, fit=360) + '\n'
        s += '  ' + lines(504, y + 68, body, 13, '#454C61', 20, fit=392) + '\n'
    return s + '</svg>\n'


FIGS['ptMeta'] = pt_meta


FIGS['ptCrear'] = lambda: console(dict(
    id='ptCrear',
    title='Crear el proyecto <tspan class="mono">playlist_app</tspan>',
    title_plain='Crear el proyecto playlist_app',
    desc='Terminal en la carpeta develop. Se ejecuta flutter create con la organización icesi.edu.co y el '
         'nombre playlist_app, la salida termina en All done, y luego cd playlist_app.',
    sub='El mismo comando de la sesión 1, con otro nombre. El nombre va en minúsculas y con guion bajo.',
    term_title='Terminal · C:\\develop',
    lines=[('P', 'flutter create --org icesi.edu.co playlist_app', 'develop'),
           ('O', 'Creating project playlist_app...'),
           ('D', 'Resolving dependencies in `playlist_app`...'),
           ('D', 'Got dependencies in `playlist_app`.'),
           ('D', 'Wrote 130 files.'),
           ('B', ''),
           ('K', 'All done!'),
           ('B', ''),
           ('P', 'cd playlist_app', 'develop'),
           ('P', '', 'playlist_app')],
    rings=[(0, 43, 12, 1), (8, 9, 15, 2)],
    cards=[(1, 'El nombre del proyecto', ['Es también el nombre del paquete:', 'package:playlist_app/...'], False),
           (2, 'Entrar a la carpeta', ['Abre esta carpeta en VS Code', 'antes de crear los archivos.'], False)],
))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--inject':
        done = set()
        for path in sorted((ROOT / 'content').glob('lessonS4[0-5].md')):
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
