"""Figuras SVG de las lecciones de la sesión 11 (S0075 a S0078, Servicio de base de datos).

    python3 tools/sesion11_figuras.py <carpeta> [id ...]   escribe un .svg por figura, para revisarlas
    python3 tools/sesion11_figuras.py --inject             reemplaza cada bloque ```svg de las lecciones
                                                           de la sesión por la figura con el mismo id

Migraciones con el CLI de Supabase en el proyecto del equipo, y la app de tracks del taller.
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from console_frame import frame  # noqa: E402
from sesion10_figuras import FAM, INK, BODY, MUTED, FAINT, LINE, txt, start, end, box, arrow, pill, tree  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
LESSONS = ['lessonS75.md', 'lessonS76.md', 'lessonS79.md', 'lessonS77.md', 'lessonS80.md', 'lessonS78.md']
STAMP = '20261111140000'

FIGS = {}


def fig(fn):
    FIGS[fn.__name__] = fn
    return fn


def chain(fid, items, y=128, h=150):
    """Fila de pasos numerados unidos por flechas."""
    n = len(items)
    gap = 26
    w = (864 - gap * (n - 1)) / n
    o = ''
    for i, (title, lines, color) in enumerate(items):
        x = 48 + i * (w + gap)
        o += box(round(x), y, round(w), h, color, title, lines, num=i + 1, size=12.5, title_size=13.5)
        if i < n - 1:
            o += arrow(fid, f'M{x + w + 2:.0f},{y + h / 2:.0f} H{x + w + gap - 2:.0f}')
    return o


# ───────────────────────────── S0075 · Migraciones con el CLI de Supabase

@fig
def mgFlujo():
    fid, h = 'mgFlujo', 388
    o = start(fid, h, 'Del modelo de datos a las tablas', 'Tú creas el archivo vacío; el agente lo llena leyendo tu modelo.',
              'Cinco pasos en fila. Uno, el modelo de datos del equipo vive en docs. Dos, AGENTS.md dice dónde está. '
              'Tres, supabase migration new crea un archivo SQL vacío. Cuatro, el agente escribe el SQL a partir del '
              'modelo. Cinco, db push remote crea las tablas en Supabase. Debajo, una nota: tú revisas el SQL antes '
              'del push.')
    o += chain(fid, [
        ('El modelo', ['docs/modelo.pdf', 'o el MER de la', 'entrega 1.'], 'slate'),
        ('AGENTS.md', ['Dice dónde está', 'el modelo y cómo', 'se escriben las', 'migraciones.'], 'indigo'),
        ('migration new', ['Crea un .sql', 'vacío en', 'supabase/', 'migrations/.'], 'amber'),
        ('El agente', ['Lee el modelo y', 'escribe el SQL', 'en ese archivo.'], 'violet'),
        ('db push', ['Corre el SQL en', 'tu proyecto: las', 'tablas aparecen', 'en Supabase.'], 'green'),
    ])
    o += box(48, 300, 864, 48, 'rose', None, [])
    o += txt(68, 329, 'Entre el paso 4 y el 5 lees el SQL. Lo que se sube a la base de datos es responsabilidad tuya, '
             'no del agente.', 13, 600, FAM['rose'][2], fit=830)
    return o + end(fid, h)


@fig
def mgInit():
    return frame(dict(
        id='mgInit',
        title='Conectar el proyecto con Supabase',
        title_plain='Conectar el proyecto con Supabase',
        desc='Una terminal en la carpeta del proyecto del equipo, mi_app. npx supabase init termina con Finished '
             'supabase init. npx supabase login abre el navegador y termina con You are now logged in. npx supabase '
             'link con el project ref termina con Finished supabase link. Tres recuadros señalan init, login y el '
             'project ref.',
        sub='Tres comandos, una sola vez por proyecto. Siempre desde la carpeta raíz de tu app.',
        term_title='Terminal · C:\\develop\\mi_app',
        lines=[
            ('P', 'npx supabase init', 'mi_app'),
            ('K', 'Finished supabase init.'),
            ('B', ''),
            ('P', 'npx supabase login', 'mi_app'),
            ('D', 'Hit enter to open browser and login automatically.'),
            ('K', 'You are now logged in. Happy coding!'),
            ('B', ''),
            ('P', 'npx supabase link --project-ref abcdefghijklmnopqrst', 'mi_app'),
            ('D', 'Enter your database password:'),
            ('K', 'Finished supabase link.'),
        ],
        rings=[
            (0, 8 + len('npx supabase '), len('init'), 1),
            (3, 8 + len('npx supabase '), len('login'), 2),
            (7, 8 + len('npx supabase link --project-ref '), len('abcdefghijklmnopqrst'), 3),
        ],
        cards=[
            (1, 'init', ['Crea la carpeta supabase/', 'con config.toml y migrations/.'], False),
            (2, 'login', ['Autoriza la consola con tu', 'cuenta. Abre el navegador.'], False),
            (3, 'El project ref', ['Las 20 letras de tu Project', 'URL. Pide la clave de la BD.'], False),
        ],
    ))


@fig
def mgNueva():
    return frame(dict(
        id='mgNueva',
        title='Crear la migración vacía',
        title_plain='Crear la migración vacía',
        desc='npx supabase migration new initial_schema responde con la ruta del archivo creado, '
             f'supabase/migrations/{STAMP}_initial_schema.sql, y el mensaje Migration created. Un recuadro señala el '
             'nombre de la migración y otro la marca de tiempo del archivo.',
        sub='El nombre lo eliges tú. La fecha y la hora delante del nombre las pone el comando.',
        term_title='Terminal · C:\\develop\\mi_app',
        lines=[
            ('P', 'npx supabase migration new initial_schema', 'mi_app'),
            ('O', '{"path":"…/supabase/migrations/'),
            ('O', f'  {STAMP}_initial_schema.sql",'),
            ('K', ' "message":"Migration created"}'),
        ],
        rings=[
            (0, 8 + len('npx supabase migration new '), len('initial_schema'), 1),
            (2, 2, len(STAMP), 2),
        ],
        cards=[
            (1, 'El nombre', ['Corto, en inglés y con guion bajo:', 'qué cambia esta migración.'], False),
            (2, 'La marca de tiempo', ['Ordena las migraciones. Se corren', 'de la más vieja a la más nueva.'], False),
        ],
    ))


@fig
def mgCarpetas():
    fid, h = 'mgCarpetas', 446
    o = start(fid, h, 'Dónde queda cada cosa', 'El modelo y las migraciones viven en el repositorio, junto al código.',
              'Árbol del proyecto mi_app: AGENTS.md, la carpeta docs con modelo.pdf, la carpeta lib y la carpeta '
              'supabase con config.toml y migrations, que tiene initial_schema.sql y create_tracks.sql.')
    rows = [(0, 'mi_app/', 'dir', None),
            (1, 'AGENTS.md', 'file', ('nombra docs/modelo.pdf', 'indigo')),
            (1, 'docs/', 'dir', None),
            (2, 'modelo.pdf', 'file', ('el modelo de datos del equipo', 'slate')),
            (1, 'lib/', 'dir', ('tu app Flutter, sin cambios', 'slate')),
            (1, 'supabase/', 'dir', ('la crea npx supabase init', 'amber')),
            (2, 'config.toml', 'file', None),
            (2, 'migrations/', 'dir', None),
            (3, f'{STAMP}_initial_schema.sql', 'file', ('lo escribe el agente', 'violet')),
            (3, '20261111143000_create_tracks.sql', 'file', ('la tabla de práctica', 'teal'))]
    o += f'<rect x="48" y="112" width="864" height="{len(rows) * 28 + 24}" rx="12" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>'
    o += tree(rows, step=28, tag_x=600)
    return o + end(fid, h)


@fig
def mgPush():
    return frame(dict(
        id='mgPush',
        title='Subir las migraciones',
        title_plain='Subir las migraciones',
        desc=f'npx supabase db push --remote lista la migración {STAMP}_initial_schema.sql, pregunta si se sube y, '
             'tras responder y, la aplica y termina con Finished supabase db push. Un recuadro señala --remote y otro '
             'la lista de migraciones pendientes.',
        sub='Solo sube lo que la base de datos todavía no tiene. Una migración ya subida no se vuelve a correr.',
        term_title='Terminal · C:\\develop\\mi_app',
        lines=[
            ('P', 'npx supabase db push --remote', 'mi_app'),
            ('O', 'Do you want to push these migrations to the remote database?'),
            ('O', f' • {STAMP}_initial_schema.sql'),
            ('B', ''),
            ('O', ' [Y/n] y'),
            ('D', f'Applying migration {STAMP}_initial_schema.sql...'),
            ('K', 'Finished supabase db push.'),
        ],
        rings=[
            (0, 8 + len('npx supabase db push '), len('--remote'), 1),
            (2, 3, len(STAMP) + len('_initial_schema.sql'), 2),
        ],
        cards=[
            (1, '--remote', ['Sin él, el CLI busca una base de', 'datos local que no estás usando.'], False),
            (2, 'Lo pendiente', ['Si la lista sale vacía, ya estaba', 'arriba: crea otra migración.'], False),
        ],
    ))


# ───────────────────────────── S0079 · Map<String, dynamic>

@fig
def mpFila():
    fid, h = 'mpFila', 430
    o = start(fid, h, 'Una fila, tres formas de verla', 'La misma fila de tracks: en la tabla, como JSON y como Map en Dart.',
              'Tres columnas unidas por flechas. A la izquierda, una fila de la tabla tracks con id, name, artist_name '
              'e image_url. En el centro, la misma fila como JSON, con cada columna como llave entre comillas. A la '
              'derecha, el Map en Dart y tres lecturas con corchetes: row de name da Yellow, row de artist_name da '
              'Coldplay y row de year da null porque esa llave no existe.')
    o += txt(48, 128, 'EN LA TABLA', 12, 700, MUTED)
    o += txt(336, 128, 'COMO JSON', 12, 700, MUTED)
    o += txt(624, 128, 'EN DART', 12, 700, MUTED)
    o += f'<rect x="48" y="144" width="240" height="196" rx="12" fill="#FFFFFF" stroke="{FAM['violet'][1]}" stroke-width="1.5"/>'
    o += f'<rect x="48" y="144" width="240" height="36" rx="12" fill="{FAM['violet'][0]}"/>'
    o += txt(64, 168, 'tracks', 13.5, 700, FAM['violet'][2], mono=True)
    for i, (col, val) in enumerate((('id', "'a1f…'"), ('name', "'Yellow'"), ('artist_name', "'Coldplay'"), ('image_url', "'picsum…'"))):
        y = 206 + i * 34
        o += txt(64, y, col, 12.5, 700, INK, mono=True, fit=110)
        o += txt(170, y, val, 12.5, 400, BODY, mono=True, fit=120)
    o += arrow(fid, 'M288,242 H334')
    o += f'<rect x="336" y="144" width="240" height="196" rx="12" fill="#1F2430"/>'
    json_lines = ['{', '  "id": "a1f…",', '  "name": "Yellow",', '  "artist_name": "Coldplay",', '  "image_url": "picsum…"', '}']
    for i, ln in enumerate(json_lines):
        o += txt(352, 176 + i * 26, ln.replace(' ', '\u00a0'), 12.5, 400, '#E6E9F0', mono=True, fit=216)
    o += arrow(fid, 'M576,242 H622')
    o += box(624, 144, 288, 196, 'teal', 'Map<String, dynamic>', [], title_size=13, mono_title=True)
    reads = [("row['name']", "'Yellow'", 'green'), ("row['artist_name']", "'Coldplay'", 'green'), ("row['year']", 'null', 'rose')]
    for i, (expr, val, c) in enumerate(reads):
        y = 214 + i * 38
        o += txt(640, y, expr, 12.5, 700, INK, mono=True, fit=150)
        o += pill(852, y - 4, val, c, mono=True)
    o += box(48, 364, 864, 40, 'slate', None, [])
    o += txt(64, 389, 'La llave es el nombre de la columna, tal cual: artist_name, no artistName. Una llave que no existe da null.',
             12.5, 400, BODY, fit=830)
    return o + end(fid, h)


# ───────────────────────────── S0080 · Primeros pasos con Supabase

SB_GREEN, SB_DARK = '#3ECF8E', '#1C1C1C'
BX, BY, BW, BH = 48, 112, 600, 384


def browser(url, h=BH):
    """Ventana de navegador con barra de dirección, a la izquierda de la figura."""
    return (f'<rect x="{BX}" y="{BY}" width="{BW}" height="{h}" rx="12" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>'
            f'<path d="M{BX},{BY + 12} A12,12 0 0 1 {BX + 12},{BY} H{BX + BW - 12} A12,12 0 0 1 {BX + BW},{BY + 12} V{BY + 36} H{BX} Z" fill="#EFF1F5"/>'
            f'<circle cx="{BX + 18}" cy="{BY + 18}" r="5" fill="#F14C4C"/><circle cx="{BX + 34}" cy="{BY + 18}" r="5" fill="#E5C07B"/>'
            f'<circle cx="{BX + 50}" cy="{BY + 18}" r="5" fill="#6BCB77"/>'
            f'<rect x="{BX + 70}" y="{BY + 8}" width="{BW - 86}" height="20" rx="10" fill="#FFFFFF" stroke="{LINE}"/>'
            + txt(BX + 84, BY + 22, url, 11.5, 400, MUTED, mono=True, fit=BW - 110))


def ring(x, y, w, h, n, color='#F2A93B'):
    return (f'<rect x="{x - 4}" y="{y - 4}" width="{w + 8}" height="{h + 8}" rx="8" fill="none" stroke="{color}" stroke-width="2.5"/>'
            f'<circle cx="{x + w + 4}" cy="{y - 4}" r="10" fill="{color}"/>'
            + txt(x + w + 4, y, str(n), 12, 700, '#FFFFFF', 'middle'))


def side_cards(cards, y0=BY, gap=12):
    """Tarjetas numeradas a la derecha: (n, título, líneas, color)."""
    o = ''
    x, w = 680, 232
    y = y0
    for n, title, lines, color in cards:
        h = 44 + 18 * len(lines)
        stroke = '#F2A93B' if color == 'amber' else FAM[color][1]
        o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#FFFFFF" stroke="{stroke}" stroke-width="1.5"/>'
        badge = '#F2A93B' if color == 'amber' else FAM[color][2]
        o += f'<circle cx="{x + 24}" cy="{y + 22}" r="10" fill="{badge}"/>' + txt(x + 24, y + 26, str(n), 12, 700, '#FFFFFF', 'middle')
        o += txt(x + 42, y + 27, title, 13.5, 700, INK, fit=w - 50)
        for i, ln in enumerate(lines):
            o += txt(x + 16, y + 50 + i * 18, ln, 12.5, 400, BODY, fit=w - 24)
        y += h + gap
    return o


def field(x, y, w, label, value, mono=False, h=32):
    return (txt(x, y, label, 12, 600, MUTED, fit=w)
            + f'<rect x="{x}" y="{y + 8}" width="{w}" height="{h}" rx="6" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.2"/>'
            + txt(x + 12, y + 8 + h / 2 + 4.5, value, 12.5, 400, INK, mono=mono, fit=w - 20))


def button(x, y, w, label, fill, fg='#FFFFFF', h=32, stroke=None):
    st = stroke or fill
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{st}" stroke-width="1.2"/>'
            + txt(x + w / 2, y + h / 2 + 4.5, label, 12.5, 600, fg, 'middle', fit=w - 8))


def settings_nav(active):
    o = f'<rect x="{BX + 1}" y="{BY + 36}" width="150" height="{BH - 37}" fill="#F7F8FA"/>'
    o += f'<line x1="{BX + 151}" y1="{BY + 36}" x2="{BX + 151}" y2="{BY + BH}" stroke="{LINE}"/>'
    o += txt(BX + 16, BY + 64, 'PROJECT SETTINGS', 11, 700, FAINT, fit=130)
    for i, item in enumerate(('General', 'Compute and Disk', 'Data API', 'API Keys', 'JWT Keys')):
        y = BY + 92 + i * 30
        if item == active:
            o += f'<rect x="{BX + 8}" y="{y - 16}" width="136" height="24" rx="6" fill="#E8F6E3"/>'
        o += txt(BX + 18, y, item, 12.5, 700 if item == active else 400, INK if item == active else BODY, fit=124)
    return o


@fig
def sbLogin():
    fid, h = 'sbLogin', 540
    o = start(fid, h, 'Entrar a Supabase', 'supabase.com › Start your project. Una sola cuenta para todos tus proyectos.',
              'Maqueta de la página de inicio de sesión de Supabase: Welcome back, el botón Continue with GitHub '
              'señalado con el número 1, Continue with SSO, los campos de correo y contraseña y el botón Sign In. A la '
              'derecha, una tarjeta que dice que se entra con la cuenta de GitHub y una nota sobre Sign up.')
    o += browser('supabase.com/dashboard/sign-in')
    cx = BX + BW / 2
    o += txt(cx - 140, BY + 84, 'Welcome back', 20, 700, INK, fit=280)
    o += txt(cx - 140, BY + 106, 'Sign in to your account', 13, 400, FAINT, fit=280)
    o += button(cx - 140, BY + 126, 280, 'Continue with GitHub', SB_DARK)
    o += ring(cx - 140, BY + 126, 280, 32, 1)
    o += button(cx - 140, BY + 168, 280, 'Continue with SSO', '#FFFFFF', INK, stroke=LINE)
    o += f'<line x1="{cx - 140}" y1="{BY + 222}" x2="{cx + 140}" y2="{BY + 222}" stroke="{LINE}"/>'
    o += f'<rect x="{cx - 14}" y="{BY + 212}" width="28" height="20" fill="#FFFFFF"/>' + txt(cx, BY + 226, 'or', 12, 400, FAINT, 'middle')
    o += field(cx - 140, BY + 252, 280, 'Email', 'tu@correo.com')
    o += field(cx - 140, BY + 306, 280, 'Password', '••••••••')
    o += button(cx - 140, BY + 348, 280, 'Sign In', SB_GREEN, SB_DARK, h=28)
    o += side_cards([
        (1, 'Continue with GitHub', ['Entra con la misma cuenta', 'de GitHub de tus', 'repositorios. No hay que', 'inventar otra contraseña.'], 'amber'),
        ('i', 'Primera vez', ['Si no tienes cuenta,', 'Start your project en', 'supabase.com la crea con', 'el mismo botón de GitHub.'], 'indigo'),
    ])
    return o + end(fid, h, 'El plan gratuito alcanza para el curso: dos proyectos activos por cuenta.')


@fig
def sbNuevo():
    fid, h = 'sbNuevo', 540
    o = start(fid, h, 'Crear el proyecto', 'Dashboard › New project. Un proyecto es una base de datos con su Auth y su Storage.',
              'Maqueta del formulario Create a new project: Organization, Project name con el número 1, Database '
              'password con Generate a password y el número 2, Region con el número 3 y el botón verde Create new '
              'project con el número 4. A la derecha, una tarjeta por número.')
    o += browser('supabase.com/dashboard/new/mi-organizacion')
    x, w = BX + 32, 536
    o += txt(x, BY + 74, 'Create a new project', 18, 700, INK, fit=320)
    o += field(x, BY + 100, w, 'Organization', 'mi-organizacion')
    o += field(x, BY + 156, w, 'Project name', 'mi-app')
    o += ring(x, BY + 164, w, 32, 1)
    o += field(x, BY + 222, w - 170, 'Database password', '••••••••••••••')
    o += txt(x + w - 150, BY + 251, 'Generate a password', 12.5, 600, '#3A8235', fit=150)
    o += ring(x, BY + 230, w, 32, 2)
    o += field(x, BY + 288, w, 'Region', 'East US (North Virginia)')
    o += ring(x, BY + 296, w, 32, 3)
    o += button(x + w - 170, BY + 344, 170, 'Create new project', SB_GREEN, SB_DARK, h=28)
    o += ring(x + w - 170, BY + 344, 170, 28, 4)
    o += side_cards([
        (1, 'Project name', ['El nombre de tu app.'], 'amber'),
        (2, 'Database password', ['Genérala y guárdala:', 'link y db push la piden.'], 'amber'),
        (3, 'Region', ['La más cercana. Para', 'Colombia, East US.'], 'amber'),
        (4, 'Create new project', ['Tarda un par de minutos', 'en quedar listo.'], 'amber'),
    ], gap=10)
    return o + end(fid, h, 'Un proyecto por equipo: todos se conectan al mismo. Quien lo crea invita a los demás en Organization › Team.')


@fig
def sbLlaves():
    fid, h = 'sbLlaves', 540
    o = start(fid, h, 'La publishable key', 'Project Settings › API Keys. La que va en la app empieza por sb_publishable_.',
              'Maqueta de Project Settings con API Keys seleccionado. Arriba, Publishable key con el valor '
              'sb_publishable_ y un botón Copy, señalados con el número 1. Abajo, Secret keys con el valor oculto, '
              'señalado en rojo con el número 2. A la derecha, una tarjeta para cada una.')
    o += browser('supabase.com/dashboard/project/abcdefghijklmnopqrst/settings/api-keys')
    o += settings_nav('API Keys')
    x, w = BX + 176, 400
    o += txt(x, BY + 70, 'API Keys', 18, 700, INK, fit=200)
    o += txt(x, BY + 104, 'Publishable key', 13.5, 700, INK, fit=200)
    o += txt(x, BY + 124, 'Safe to use in a browser.', 12, 400, FAINT, fit=w)
    o += f'<rect x="{x}" y="{BY + 136}" width="{w - 70}" height="32" rx="6" fill="#F7F8FA" stroke="{LINE}"/>'
    o += txt(x + 12, BY + 156.5, 'sb_publishable_Xy7k2…', 12.5, 400, INK, mono=True, fit=w - 90)
    o += button(x + w - 62, BY + 136, 62, 'Copy', '#FFFFFF', INK, stroke=LINE)
    o += ring(x, BY + 136, w, 32, 1)
    o += txt(x, BY + 214, 'Secret keys', 13.5, 700, INK, fit=200)
    o += txt(x, BY + 234, 'Full access to your project. Keep it private.', 12, 400, FAINT, fit=w)
    o += f'<rect x="{x}" y="{BY + 246}" width="{w - 70}" height="32" rx="6" fill="#F7F8FA" stroke="{LINE}"/>'
    o += txt(x + 12, BY + 266.5, 'sb_secret_••••••••••••', 12.5, 400, INK, mono=True, fit=w - 90)
    o += button(x + w - 62, BY + 246, 62, 'Reveal', '#FFFFFF', INK, stroke=LINE)
    o += ring(x, BY + 246, w, 32, 2, FAM['rose'][2])
    o += side_cards([
        (1, 'Publishable key', ['Va en main.dart, en', 'Supabase.initialize.', 'Es pública por diseño.'], 'amber'),
        (2, 'Secret key', ['Salta todos los permisos.', 'Nunca en la app ni en', 'el repositorio.'], 'rose'),
    ])
    return o + end(fid, h, 'En tutoriales viejos aparece la anon key: la publishable key la reemplaza.')


@fig
def sbRef():
    fid, h = 'sbRef', 540
    o = start(fid, h, 'El Project ID y la Project URL', 'Project Settings › General. Las mismas veinte letras están en los dos.',
              'Maqueta de Project Settings con General seleccionado: Project name mi-app y Project ID '
              'abcdefghijklmnopqrst con un botón Copy, señalado con el número 1. Debajo, la Project URL, que contiene '
              'el mismo identificador, señalada con el número 2. A la derecha, una tarjeta para cada uno.')
    o += browser('supabase.com/dashboard/project/abcdefghijklmnopqrst/settings/general')
    o += settings_nav('General')
    x, w = BX + 176, 400
    o += txt(x, BY + 70, 'General settings', 18, 700, INK, fit=240)
    o += field(x, BY + 100, w, 'Project name', 'mi-app')
    o += txt(x, BY + 168, 'Project ID', 12, 600, MUTED, fit=w)
    o += f'<rect x="{x}" y="{BY + 176}" width="{w - 70}" height="32" rx="6" fill="#F7F8FA" stroke="{LINE}"/>'
    o += txt(x + 12, BY + 196.5, 'abcdefghijklmnopqrst', 12.5, 700, INK, mono=True, fit=w - 90)
    o += button(x + w - 62, BY + 176, 62, 'Copy', '#FFFFFF', INK, stroke=LINE)
    o += ring(x, BY + 176, w, 32, 1)
    o += f'<rect x="{x}" y="{BY + 236}" width="{w}" height="112" rx="10" fill="#F7F8FA" stroke="{LINE}"/>'
    o += txt(x + 16, BY + 262, 'Project URL', 13, 700, INK, fit=200)
    o += txt(x + 16, BY + 280, 'En Data API o en el botón Connect.', 12, 400, FAINT, fit=w - 30)
    o += f'<rect x="{x + 16}" y="{BY + 292}" width="{w - 32}" height="32" rx="6" fill="#FFFFFF" stroke="{LINE}"/>'
    o += (txt(x + 28, BY + 312.5, 'abcdefghijklmnopqrst', 12.5, 700, '#A96C05', mono=True, fit=160)
          + txt(x + 178, BY + 312.5, '.supabase.co', 12.5, 400, MUTED, mono=True, fit=100))
    o += ring(x + 16, BY + 292, w - 32, 32, 2)
    o += side_cards([
        (1, 'Project ID', ['Es el project ref de', 'npx supabase link', '--project-ref <ID>.'], 'amber'),
        (2, 'Project URL', ['Va en main.dart, en', 'Supabase.initialize.', 'Lleva el mismo ID.'], 'amber'),
    ])
    return o + end(fid, h)


# ───────────────────────────── S0077 · Repositorio de arranque

@fig
def acCarpetas():
    fid, h = 'acCarpetas', 474
    o = start(fid, h, 'Lo que trae el repositorio', 'La app ya funciona en memoria. Lo que falta está en services/.',
              'Árbol de lib: main.dart con las tres rutas, models con track.dart, components con track_card, '
              'track_list y track_form, screens con home_screen, add_track_screen y track_detail_screen, y services '
              'con track_services.dart, con los métodos vacíos que se completan en el taller.')
    rows = [(0, 'lib/', 'dir', None),
            (1, 'main.dart', 'file', ("rutas '/', '/add-track' y '/track'", 'slate')),
            (1, 'models/', 'dir', None),
            (2, 'track.dart', 'file', ('Track con fromMap, toMap, copyWith', 'indigo')),
            (1, 'components/', 'dir', None),
            (2, 'track_card.dart · track_list.dart', 'file', ('la lista', 'slate')),
            (2, 'track_form.dart', 'file', ('el borrador del track', 'slate')),
            (1, 'screens/', 'dir', None),
            (2, 'home_screen.dart', 'file', ('dueña de _tracks', 'amber')),
            (2, 'add_track_screen.dart · track_detail_screen.dart', 'file', None),
            (1, 'services/', 'dir', None),
            (2, 'track_services.dart', 'file', ('métodos vacíos: los completas', 'rose'))]
    o += f'<rect x="48" y="112" width="864" height="{len(rows) * 26 + 24}" rx="12" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>'
    o += tree(rows, step=26, tag_x=620)
    return o + end(fid, h)


# ───────────────────────────── S0078 · Taller · CRUD de tracks

@fig
def tlPiezas():
    fid, h = 'tlPiezas', 410
    o = start(fid, h, 'Quién habla con quién', 'La pantalla pide, el servicio habla con Supabase, la tabla guarda.',
              'Arriba, main.dart llama a Supabase.initialize con la URL y la publishable key escritas ahí mismo. '
              'Abajo, tres cajas en fila: HomeScreen con _tracks y setState, TrackService con getTracks, createTrack y '
              'deleteTrack, y la tabla tracks en Supabase. Las flechas de ida llevan la llamada y las de vuelta un '
              'Future.')
    o += box(48, 116, 864, 72, 'slate', 'main.dart', ['Supabase.initialize con la Project URL y la publishable key, antes de runApp.'],
             title_size=13.5, mono_title=True)
    cols = [(48, 'HomeScreen', ['Dueña de _tracks.', 'Llama al servicio con', 'await y luego setState.'], 'indigo'),
            (364, 'TrackService', ['getTracks()', 'createTrack(track)', 'deleteTrack(id)'], 'teal'),
            (680, 'tabla tracks', ['id · name', 'artist_name', 'image_url'], 'violet')]
    for x, title, lines, c in cols:
        o += box(x, 232, 232, 128, c, title, lines, title_size=14, mono_title=True)
    o += arrow(fid, 'M280,276 H362')
    o += arrow(fid, 'M596,276 H678')
    o += arrow(fid, 'M678,320 H598', dashed=True)
    o += arrow(fid, 'M362,320 H282', dashed=True)
    o += pill(322, 298, 'Future', 'amber')
    o += pill(638, 298, 'Future', 'amber')
    return o + end(fid, h, 'Línea continua: la llamada. Punteada: la respuesta, que llega después.')


@fig
def tlConsola():
    return frame(dict(
        id='tlConsola',
        title='Instalar supabase_flutter',
        title_plain='Instalar supabase_flutter',
        desc='En la carpeta 262SeminarioSesion12, flutter pub add supabase_flutter termina con Changed dependencies. '
             'Después flutter run -d chrome lanza la app en Chrome. Un recuadro señala el paquete y otro el '
             'resultado.',
        sub='Se instala una sola vez, desde la carpeta del proyecto.',
        term_title='Terminal · C:\\develop\\262SeminarioSesion12',
        lines=[
            ('P', 'flutter pub add supabase_flutter', '262SeminarioSesion12'),
            ('D', 'Resolving dependencies...'),
            ('O', '+ supabase_flutter 2.x.x'),
            ('K', 'Changed xx dependencies!'),
            ('B', ''),
            ('P', 'flutter run -d chrome', '262SeminarioSesion12'),
            ('D', 'Launching lib/main.dart on Chrome in debug mode...'),
        ],
        rings=[
            (0, 22 + len('flutter pub add '), len('supabase_flutter'), 1),
            (3, 0, len('Changed xx dependencies!'), 2),
        ],
        cards=[
            (1, 'supabase_flutter', ['El SDK de Supabase para Flutter.'], False),
            (2, 'Changed dependencies', ['Quedó en pubspec.yaml, en', 'dependencies.'], False),
        ],
    ))


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--inject':
        done = set()
        for name in LESSONS:
            path = ROOT / 'content' / name
            if not path.exists():
                continue
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
