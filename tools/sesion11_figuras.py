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
LESSONS = ['lessonS75.md', 'lessonS76.md', 'lessonS79.md', 'lessonS77.md', 'lessonS78.md']
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


# ───────────────────────────── S0077 · Repositorio de arranque

@fig
def acCarpetas():
    fid, h = 'acCarpetas', 474
    o = start(fid, h, 'Lo que trae el repositorio', 'La app ya funciona en memoria. Lo que falta está en services/.',
              'Árbol de lib: main.dart con las tres rutas, models con track.dart, components con track_card, '
              'track_list y track_form, screens con home_screen, add_track_screen y track_detail_screen, y services '
              'con track_services.dart vacío, señalado como lo que se llena en el taller.')
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
            (2, 'track_services.dart', 'file', ('vacío: lo llenas tú', 'rose'))]
    o += f'<rect x="48" y="112" width="864" height="{len(rows) * 26 + 24}" rx="12" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>'
    o += tree(rows, step=26, tag_x=620)
    return o + end(fid, h)


# ───────────────────────────── S0078 · Taller · CRUD de tracks

@fig
def tlPiezas():
    fid, h = 'tlPiezas', 410
    o = start(fid, h, 'Quién habla con quién', 'La pantalla pide, el servicio habla con Supabase, la tabla guarda.',
              'Arriba, env.json con la URL y la publishable key entra a main.dart, que llama a Supabase.initialize. '
              'Abajo, tres cajas en fila: HomeScreen con _tracks y setState, TrackService con getTracks, createTrack y '
              'deleteTrack, y la tabla tracks en Supabase. Las flechas de ida llevan la llamada y las de vuelta un '
              'Future.')
    o += box(48, 116, 300, 72, 'slate', 'env.json', ['SUPABASE_URL y la publishable key.'], title_size=13.5, mono_title=True)
    o += arrow(fid, 'M348,152 H404')
    o += box(406, 116, 506, 72, 'slate', 'main.dart', ['Supabase.initialize(url, publishableKey) antes de runApp.'],
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
        title='El paquete y las llaves',
        title_plain='El paquete y las llaves',
        desc='En la carpeta 262SeminarioSesion11, flutter pub add supabase_flutter termina con Changed dependencies. '
             'Después flutter run -d chrome con dart-define-from-file igual a env.json lanza la app en Chrome. Un '
             'recuadro señala el paquete y otro el archivo de llaves.',
        sub='El paquete se agrega una vez. Las llaves van en cada flutter run.',
        term_title='Terminal · C:\\develop\\262SeminarioSesion11',
        lines=[
            ('P', 'flutter pub add supabase_flutter', '262SeminarioSesion11'),
            ('D', 'Resolving dependencies...'),
            ('O', '+ supabase_flutter 2.x.x'),
            ('K', 'Changed xx dependencies!'),
            ('B', ''),
            ('P', 'flutter run -d chrome --dart-define-from-file=env.json', '262SeminarioSesion11'),
            ('D', 'Launching lib/main.dart on Chrome in debug mode...'),
        ],
        rings=[
            (0, 22 + len('flutter pub add '), len('supabase_flutter'), 1),
            (5, 22 + len('flutter run -d chrome --dart-define-from-file='), len('env.json'), 2),
        ],
        cards=[
            (1, 'supabase_flutter', ['El SDK. Queda en pubspec.yaml.'], False),
            (2, 'env.json', ['Las llaves, fuera del código. Sin', 'él, la URL llega vacía.'], False),
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
