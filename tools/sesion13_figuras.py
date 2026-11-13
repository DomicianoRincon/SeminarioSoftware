"""Figuras SVG de las lecciones de la sesión 13 (S0083 a S0087, Servicio de autenticación).

    python3 tools/sesion13_figuras.py <carpeta> [id ...]   escribe un .svg por figura, para revisarlas
    python3 tools/sesion13_figuras.py --inject             reemplaza cada bloque ```svg de las lecciones
                                                           de la sesión por la figura con el mismo id

Registro, inicio y cierre de sesión con Supabase Auth sobre la app de tracks de la sesión 12
(repositorio 262SeminarioSesion13).
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from console_frame import frame  # noqa: E402
from sesion10_figuras import FAM, INK, BODY, MUTED, FAINT, LINE, txt, start, end, box, arrow, pill, tree  # noqa: E402
from sesion11_figuras import BX, BY, BW, browser, ring, side_cards, button  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
LESSONS = ['lessonS83.md', 'lessonS84.md', 'lessonS85.md', 'lessonS86.md', 'lessonS87.md']
STAMP = '20261118140000'
ACCENT = '#6750A4'

FIGS = {}


def fig(fn):
    FIGS[fn.__name__] = fn
    return fn


def mini(x, y, title, body, w=200, h=300, appbar=True, badge=None):
    """Teléfono pequeño: marco oscuro, barra de título opcional y un cuerpo ya dibujado en coordenadas absolutas."""
    o = f'<rect x="{x - 8}" y="{y - 8}" width="{w + 16}" height="{h + 16}" rx="26" fill="#1F2430"/>'
    o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="#FEF7FF"/>'
    if appbar:
        o += f'<path d="M{x},{y + 18} A18,18 0 0 1 {x + 18},{y} H{x + w - 18} A18,18 0 0 1 {x + w},{y + 18} V{y + 44} H{x} Z" fill="#D0BCFF"/>'
        o += txt(x + 14, y + 29, title, 13.5, 600, INK, fit=w - 50)
    o += body
    if badge:
        o += pill(x + w / 2, y + h + 30, badge, 'violet', mono=True)
    return o


def mfield(x, y, w, label):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="4" fill="#FFFFFF" stroke="#79747E"/>'
            + txt(x + 10, y + 18, label, 12, 400, '#79747E', fit=w - 16))


def mbutton(x, y, w, label):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="15" fill="{ACCENT}"/>'
            + txt(x + w / 2, y + 19.5, label, 12.5, 600, '#FFFFFF', 'middle', fit=w - 10))


def logout_icon(x, y, color=INK):
    return (f'<path d="M{x + 6},{y} h-6 v16 h6 M{x + 10},{y + 4} l4,4 -4,4 M{x + 14},{y + 8} h-9" fill="none" '
            f'stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>')


def table(x, y, w, name, cols, rows, color, col_w=None, note=None):
    """Tabla dibujada: nombre arriba, encabezado y filas. cols = nombres; rows = listas de celdas."""
    soft, border, strong = FAM[color]
    n = len(cols)
    col_w = col_w or [w / n] * n
    h = 44 + 28 * (len(rows) + 1) + 8
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#FFFFFF" stroke="{border}" stroke-width="1.5"/>'
    o += f'<path d="M{x},{y + 12} A12,12 0 0 1 {x + 12},{y} H{x + w - 12} A12,12 0 0 1 {x + w},{y + 12} V{y + 36} H{x} Z" fill="{soft}"/>'
    o += txt(x + 14, y + 24, name, 13.5, 700, strong, mono=True, fit=w - 20)
    if note:
        o += txt(x + w - 12, y + 24, note, 12, 400, MUTED, 'end', fit=w / 2)
    for r, cells in enumerate([cols] + rows):
        cy = y + 62 + r * 28
        cx = x + 14
        for c, cell in enumerate(cells):
            hl = isinstance(cell, tuple)
            value = cell[0] if hl else cell
            fill = cell[1] if hl else (MUTED if r == 0 else INK)
            o += txt(cx, cy, value, 12, 700 if r == 0 or hl else 400, fill, mono=True, fit=col_w[c] - 8)
            cx += col_w[c]
        if r == 0:
            o += f'<line x1="{x + 10}" y1="{cy + 9}" x2="{x + w - 10}" y2="{cy + 9}" stroke="{LINE}"/>'
    return o


# ───────────────────────────── S0083 · Repositorio de arranque

@fig
def auPantallas():
    fid, h = 'auPantallas', 610
    o = start(fid, h, 'Tres pantallas y una ruta inicial', 'La app abre en el login. Del login se va al registro o a la lista.',
              'Tres teléfonos en fila. LoginScreen, marcada como initialRoute /login, con correo, contraseña, el botón '
              'Entrar y el enlace Regístrate. SignupScreen con nombre, correo, contraseña, repetirla y Crear cuenta. '
              'HomeScreen con la lista de tracks y el ícono de cerrar sesión. Flechas: Regístrate abre el registro con '
              'pushNamed; Entrar y Crear cuenta llevan a la lista con pushNamedAndRemoveUntil; cerrar sesión vuelve '
              'al login de la misma forma.')
    y = 140
    # Login
    xs = [64, 380, 696]
    body = txt(xs[0] + 100, y + 70, '♪', 30, 700, ACCENT, 'middle') + txt(xs[0] + 100, y + 100, 'Tracks', 18, 700, INK, 'middle')
    body += mfield(xs[0] + 16, y + 124, 168, 'Correo') + mfield(xs[0] + 16, y + 162, 168, 'Contraseña')
    body += mbutton(xs[0] + 16, y + 204, 168, 'Entrar')
    body += txt(xs[0] + 100, y + 262, '¿No tienes cuenta? Regístrate', 12, 600, ACCENT, 'middle', fit=180)
    o += mini(xs[0], y, '', body, appbar=False, badge="initialRoute: '/login'")
    o += txt(xs[0] + 100, y - 18, 'LoginScreen', 13.5, 700, INK, 'middle', mono=True)
    # Signup
    body = ''.join(mfield(xs[1] + 16, y + 60 + i * 38, 168, t) for i, t in
                   enumerate(['Nombre', 'Correo', 'Contraseña', 'Repite la contraseña']))
    body += mbutton(xs[1] + 16, y + 222, 168, 'Crear cuenta')
    o += mini(xs[1], y, '← Crear cuenta', body, badge="'/signup'")
    o += txt(xs[1] + 100, y - 18, 'SignupScreen', 13.5, 700, INK, 'middle', mono=True)
    # Home
    body = (f'<rect x="{xs[2] + 14}" y="{y + 58}" width="172" height="30" rx="15" fill="{ACCENT}"/>'
            + txt(xs[2] + 100, y + 77.5, '+ Crear track', 12.5, 600, '#FFFFFF', 'middle'))
    for i, (n, a) in enumerate([('Yellow', 'Coldplay'), ('Clocks', 'Coldplay'), ('Bohemian…', 'Queen')]):
        cy = y + 102 + i * 58
        body += f'<rect x="{xs[2] + 14}" y="{cy}" width="172" height="48" rx="10" fill="#FFFFFF" stroke="#E3E3EA"/>'
        body += f'<rect x="{xs[2] + 22}" y="{cy + 8}" width="32" height="32" rx="7" fill="#B69DF8"/>'
        body += txt(xs[2] + 62, cy + 21, n, 12.5, 700, INK, fit=110) + txt(xs[2] + 62, cy + 37, a, 12, 400, MUTED, fit=110)
    body += logout_icon(xs[2] + 172, y + 14)
    o += mini(xs[2], y, 'Mis tracks', body, badge="'/home'")
    o += txt(xs[2] + 100, y - 18, 'HomeScreen', 13.5, 700, INK, 'middle', mono=True)
    # Flechas
    o += arrow(fid, f'M{xs[0] + 196},{y + 262} C{xs[0] + 250},{y + 262} {xs[1] - 70},{y + 140} {xs[1] - 12},{y + 140}')
    o += pill(xs[1] - 58, y + 116, 'pushNamed', 'indigo', mono=True)
    o += arrow(fid, f'M{xs[1] + 192},{y + 237} H{xs[2] - 12}')
    o += box(48, y + 372, 864, 44, 'amber', None, [])
    o += txt(480, y + 399, 'Entrar, Crear cuenta y cerrar sesión navegan con pushNamedAndRemoveUntil: la pila queda con una sola pantalla.',
             12.5, 600, FAM['amber'][2], 'middle', fit=840)
    return o + end(fid, h, 'Hoy los botones navegan sin preguntarle nada a Supabase: en el taller cada uno llama a su servicio.')


@fig
def auCarpetas():
    fid, h = 'auCarpetas', 534
    o = start(fid, h, 'Lo que trae el repositorio', 'Lo de la sesión 12, ya resuelto, más el login, el registro y dos servicios vacíos.',
              'Árbol de lib: main.dart con las cinco rutas e initialRoute /login, models con track y profile, '
              'components con login_form, signup_form y los de tracks, screens con login, signup, home y las dos de '
              'tracks, y services con auth_service y profile_service vacíos y track_services completo.')
    rows = [(0, 'lib/', 'dir', None),
            (1, 'main.dart', 'file', ("initialRoute: '/login'", 'violet')),
            (1, 'models/', 'dir', None),
            (2, 'track.dart', 'file', ('de la sesión 12', 'slate')),
            (2, 'profile.dart', 'file', ('Profile: id, name, email', 'indigo')),
            (1, 'components/', 'dir', None),
            (2, 'login_form.dart · signup_form.dart', 'file', ('el borrador y sus avisos', 'indigo')),
            (2, 'track_card · track_list · track_form', 'file', ('de la sesión 12', 'slate')),
            (1, 'screens/', 'dir', None),
            (2, 'login_screen.dart · signup_screen.dart', 'file', ('navegan sin preguntar', 'amber')),
            (2, 'home_screen.dart', 'file', ('con el botón de cerrar sesión', 'amber')),
            (1, 'services/', 'dir', None),
            (2, 'auth_service.dart', 'file', ('vacío: lo completas', 'rose')),
            (2, 'profile_service.dart', 'file', ('vacío: lo completas', 'rose')),
            (2, 'track_services.dart', 'file', ('completo, de la sesión 12', 'green'))]
    o += f'<rect x="48" y="112" width="864" height="{len(rows) * 26 + 24}" rx="12" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>'
    o += tree(rows, step=26, tag_x=600)
    return o + end(fid, h)


# ───────────────────────────── S0084 · Supabase Auth

@fig
def auDosLugares():
    fid, h = 'auDosLugares', 520
    uid = '3f9a1c27-…'
    o = start(fid, h, 'Un usuario vive en dos lugares', 'Auth guarda la cuenta. Tus tablas guardan todo lo demás, con el mismo id.',
              'A la izquierda, Supabase Auth con la tabla auth.users: id, email y la contraseña cifrada; la crea y la '
              'maneja Supabase. A la derecha, en Postgres, la tabla profiles con id, name y email, y la tabla tracks '
              'con su columna user_id. Una línea une el id de auth.users con el id de profiles, y otra el id de '
              'profiles con el user_id de tracks. Abajo, el teléfono guarda la sesión.')
    o += txt(48, 128, 'SUPABASE AUTH', 12, 700, MUTED)
    o += table(48, 140, 380, 'auth.users', ['id', 'email', 'password'],
               [[(uid, '#7439B8'), 'ana@correo.com', '$2a$10$…']], 'violet', [120, 150, 110], 'la crea Supabase')
    o += box(48, 288, 380, 84, 'slate', None, ['No la creas ni la editas tú. Se llena con', 'signUp y se consulta con signInWithPassword.'])
    o += txt(532, 128, 'POSTGRES · TUS TABLAS', 12, 700, MUTED)
    o += table(532, 140, 380, 'profiles', ['id', 'name', 'email'],
               [[(uid, '#7439B8'), 'Ana', 'ana@correo.com']], 'indigo', [120, 110, 150], 'la creas tú')
    o += table(532, 288, 380, 'tracks', ['id', 'name', 'user_id'],
               [['a1f3c9e2', 'Yellow', (uid, '#7439B8')]], 'teal', [100, 110, 170], 'sesión 12 + user_id')
    o += arrow(fid, 'M96,234 V268 H500 V226 H536')
    o += pill(300, 268, 'el mismo id', 'violet')
    o += arrow(fid, 'M590,234 V266 H880 V284')
    o += box(48, 400, 864, 72, 'amber', 'En el teléfono: la sesión', ['Al entrar, Supabase guarda la sesión en el dispositivo. Mientras exista, la app sabe quién es el usuario sin volver a preguntar.'],
             size=12.5, title_size=13.5)
    return o + end(fid, h)


@fig
def auMetodos():
    fid, h = 'auMetodos', 380
    o = start(fid, h, 'Cuatro llamadas de supabase.auth', 'Tres van a Supabase y cambian la sesión. La cuarta solo mira la que hay.',
              'Cuatro tarjetas en fila. signUp crea la cuenta y deja la sesión iniciada. signInWithPassword revisa '
              'correo y contraseña y guarda la sesión. signOut borra la sesión del dispositivo. currentSession lee '
              'la sesión guardada, sin ir a internet. Debajo de cada una, cómo queda la sesión: iniciada, iniciada, '
              'null y la misma.')
    cards = [
        ('signUp', ['Crea la cuenta en', 'auth.users.', 'Devuelve el user', 'con su id.'], 'teal', 'sesión iniciada', 'green'),
        ('signInWithPassword', ['Busca la cuenta y', 'revisa la contraseña.', 'No crea nada.'], 'indigo', 'sesión iniciada', 'green'),
        ('signOut', ['Borra la sesión', 'del dispositivo. La', 'cuenta sigue en', 'Supabase.'], 'rose', 'sesión: null', 'rose'),
        ('currentSession', ['Lee la sesión', 'guardada. No va a', 'internet: no lleva', 'await.'], 'slate', 'no la cambia', 'slate'),
    ]
    w, gap = 198, 24
    for i, (name, lines, c, result, rc) in enumerate(cards):
        x = 48 + i * (w + gap)
        o += box(x, 120, w, 146, c, name, lines, title_size=13.5, mono_title=True, size=12.5)
        o += arrow(fid, f'M{x + w / 2},{268} V{290}')
        o += pill(x + w / 2, 308, result, rc)
    return o + end(fid, h, 'Las tres primeras devuelven un Future y van con await. Si algo sale mal lanzan AuthException.')


@fig
def auConfirm():
    fid, h = 'auConfirm', 540
    o = start(fid, h, 'Apagar la confirmación de correo', 'Authentication › Sign In / Providers. Para clase, el usuario entra apenas se registra.',
              'Maqueta del panel de Supabase: menú de Authentication con Sign In / Providers seleccionado. En el panel, '
              'User Signups con Allow new users to sign up encendido y Confirm email apagado, señalado con el número 1, '
              'y el botón Save changes con el número 2. A la derecha, una tarjeta para cada uno.')
    o += browser('supabase.com/dashboard/project/abcdefghijklmnopqrst/auth/providers')
    o += f'<rect x="{BX + 1}" y="{BY + 36}" width="150" height="347" fill="#F7F8FA"/>'
    o += f'<line x1="{BX + 151}" y1="{BY + 36}" x2="{BX + 151}" y2="{BY + 384}" stroke="{LINE}"/>'
    o += txt(BX + 16, BY + 64, 'AUTHENTICATION', 11, 700, FAINT, fit=130)
    for i, item in enumerate(('Users', 'Sign In / Providers', 'Emails', 'URL Configuration', 'Policies')):
        yy = BY + 92 + i * 30
        if i == 1:
            o += f'<rect x="{BX + 8}" y="{yy - 16}" width="136" height="24" rx="6" fill="#E8F6E3"/>'
        o += txt(BX + 18, yy, item, 12.5, 700 if i == 1 else 400, INK if i == 1 else BODY, fit=124)
    x, w = BX + 176, 400

    def toggle(tx, ty, on):
        fill = '#3ECF8E' if on else '#D5D9E0'
        knob = tx + 24 if on else tx + 10
        return (f'<rect x="{tx}" y="{ty}" width="34" height="20" rx="10" fill="{fill}"/>'
                f'<circle cx="{knob}" cy="{ty + 10}" r="7" fill="#FFFFFF"/>')
    o += txt(x, BY + 70, 'Sign In / Providers', 18, 700, INK, fit=260)
    o += txt(x, BY + 104, 'User Signups', 13.5, 700, INK, fit=200)
    o += f'<rect x="{x}" y="{BY + 116}" width="{w}" height="150" rx="10" fill="#FFFFFF" stroke="{LINE}"/>'
    o += txt(x + 16, BY + 144, 'Allow new users to sign up', 12.5, 600, INK, fit=280) + toggle(x + w - 50, BY + 131, True)
    o += f'<line x1="{x}" y1="{BY + 166}" x2="{x + w}" y2="{BY + 166}" stroke="{LINE}"/>'
    o += txt(x + 16, BY + 194, 'Confirm email', 12.5, 600, INK, fit=280) + toggle(x + w - 50, BY + 181, False)
    o += txt(x + 16, BY + 212, 'Users need to confirm their email before signing in.', 11.5, 400, FAINT, fit=w - 80)
    o += ring(x + 8, BY + 174, w - 16, 46, 1)
    o += txt(x + 16, BY + 250, 'Minimum password length: 6', 12, 400, MUTED, fit=w - 30)
    o += button(x + w - 130, BY + 290, 130, 'Save changes', '#3ECF8E', '#1C1C1C')
    o += ring(x + w - 130, BY + 290, 130, 32, 2)
    o += side_cards([
        (1, 'Confirm email', ['Apagado: signUp deja la', 'sesión iniciada de una.', 'Encendido: hay que abrir', 'el correo primero.'], 'amber'),
        (2, 'Save changes', ['Sin guardar no cambia', 'nada.'], 'amber'),
    ])
    return o + end(fid, h, 'Maqueta de la interfaz de noviembre de 2026. En una app publicada la confirmación se deja encendida.')


# ───────────────────────────── S0085 · La tabla profiles

@fig
def auMigracion():
    name = 'create_profiles'
    return frame(dict(
        id='auMigracion',
        title='La migración de profiles',
        title_plain='La migración de profiles',
        desc=f'En el proyecto del equipo, npx supabase migration new {name} crea el archivo {STAMP}_{name}.sql. '
             'Después de escribir el SQL, npx supabase db push --remote lo aplica y termina con Finished supabase db '
             'push. Un recuadro señala el nombre de la migración y otro el archivo que se sube.',
        sub='En el proyecto de tu equipo, como en Migraciones con el CLI de Supabase.',
        term_title='Terminal · C:\\develop\\mi_app',
        lines=[
            ('P', f'npx supabase migration new {name}', 'mi_app'),
            ('K', f'Created new migration at supabase/migrations/{STAMP}_{name}.sql'),
            ('B', ''),
            ('P', 'npx supabase db push --remote', 'mi_app'),
            ('O', 'Do you want to push these migrations to the remote database?'),
            ('O', f' • {STAMP}_{name}.sql'),
            ('O', ' [Y/n] y'),
            ('K', 'Finished supabase db push.'),
        ],
        rings=[
            (0, 8 + len('npx supabase migration new '), len(name), 1),
            (5, 3, len(STAMP) + len(name) + 5, 2),
        ],
        cards=[
            (1, 'El nombre', ['Qué cambia la migración:', 'crea la tabla profiles.'], False),
            (2, 'Lo que se sube', ['Solo la migración nueva. Las', 'anteriores ya estaban arriba.'], False),
        ],
    ))


@fig
def auRegistro():
    fid, h = 'auRegistro', 430
    o = start(fid, h, 'Registrarse son dos pasos', 'Primero la cuenta en Auth, después la fila en profiles con el id que devolvió Auth.',
              'Cinco pasos en fila. Uno, SignupForm valida y llama a onSignup con nombre, correo y contraseña. Dos, '
              'AuthService.signUp crea la cuenta. Tres, signUp devuelve el id del usuario. Cuatro, '
              'ProfileService.createProfile guarda la fila con ese id, el nombre y el correo. Cinco, la pantalla '
              'navega a /home. Debajo, una nota: si el paso 2 falla, el 4 no corre.')
    items = [
        ('SignupForm', ['Valida y llama', 'a onSignup con', 'name, email y', 'password.'], 'slate'),
        ('signUp', ['AuthService crea', 'la cuenta en', 'auth.users.'], 'violet'),
        ('el id', ['signUp devuelve', 'response.user!.id,', 'un uuid.'], 'amber'),
        ('profile', ['ProfileService.', 'createProfile', 'inserta la fila', 'con ese id.'], 'indigo'),
        ("'/home'", ['La pantalla', 'navega y borra', 'la pila.'], 'green'),
    ]
    n, gap = len(items), 22
    w = (864 - gap * (n - 1)) / n
    for i, (title, lines, color) in enumerate(items):
        x = 48 + i * (w + gap)
        o += box(round(x), 124, round(w), 160, color, title, lines, num=i + 1, size=12.5, title_size=13, mono_title=True)
        if i < n - 1:
            o += arrow(fid, f'M{x + w + 2:.0f},204 H{x + w + gap - 2:.0f}')
    o += box(48, 312, 864, 64, 'rose', None, [])
    o += txt(68, 341, 'Van en ese orden y con await: createProfile necesita el id que devolvió signUp. Si signUp lanza', 13, 600, FAM['rose'][2], fit=830)
    o += txt(68, 361, 'AuthException (correo repetido, contraseña corta), el paso 4 no corre y no queda un perfil suelto.', 13, 600, FAM['rose'][2], fit=830)
    return o + end(fid, h)


@fig
def auDueno():
    fid, h = 'auDueno', 470
    uid = '3f9a1c27-…'
    o = start(fid, h, 'Cada track tiene dueño', 'Al crear, el servicio pone el id del usuario. Al listar, filtra por él.',
              'Arriba, la tabla tracks con la columna nueva user_id: dos filas de Ana y una de otro usuario. Abajo, '
              'dos tarjetas: createTrack agrega user_id con el id de currentUser antes del insert, y getTracks '
              'filtra con eq user_id, así que Ana solo ve sus dos filas.')
    o += table(48, 116, 864, 'tracks', ['id', 'name', 'artist_name', 'user_id'],
               [['a1f3c9e2', 'Yellow', 'Coldplay', (uid, '#7439B8')],
                ['b2c4d1f7', 'Clocks', 'Coldplay', (uid, '#7439B8')],
                ['c3d5e8a0', 'Bohemian Rhapsody', 'Queen', ('8b2e6d40-…', FAINT)]], 'teal', [150, 240, 200, 274])
    o += box(48, 300, 420, 120, 'indigo', 'createTrack', ["data['user_id'] = currentUser!.id", 'El formulario no lo pide: lo pone', 'el servicio, que sabe quién entró.'],
             title_size=13.5, mono_title=True, size=12.5)
    o += box(492, 300, 420, 120, 'violet', 'getTracks', [".select().eq('user_id', userId)", 'Ana ve Yellow y Clocks. La fila', 'de otro usuario no le llega.'],
             title_size=13.5, mono_title=True, size=12.5)
    return o + end(fid, h, 'user_id referencia a profiles(id): no puede apuntar a un usuario que no existe.')


# ───────────────────────────── S0086 · Sesión persistente y guardas

@fig
def auArranque():
    fid, h = 'auArranque', 430
    o = start(fid, h, 'Al abrir la app, ¿a qué pantalla?', 'Supabase.initialize recupera la sesión guardada. initialRoute decide con ella.',
              'Un flujo de izquierda a derecha. main corre Supabase.initialize, que lee la sesión guardada en el '
              'dispositivo. Después, la pregunta isLoggedIn. Si hay sesión, la flecha va a /home, HomeScreen. Si no, '
              'va a /login, LoginScreen.')
    o += box(48, 168, 220, 132, 'slate', 'main()', ['await Supabase.initialize', 'lee la sesión que quedó', 'guardada la última vez.'],
             title_size=14, mono_title=True, size=12.5)
    o += arrow(fid, 'M270,234 H344')
    o += f'<path d="M466,154 L582,234 L466,314 L350,234 Z" fill="{FAM["amber"][0]}" stroke="{FAM["amber"][1]}" stroke-width="1.5"/>'
    o += txt(466, 230, 'isLoggedIn()', 14, 700, FAM['amber'][2], 'middle', mono=True)
    o += txt(466, 250, '¿hay sesión?', 12.5, 400, BODY, 'middle')
    o += arrow(fid, 'M548,210 C600,170 620,150 680,150')
    o += arrow(fid, 'M548,258 C600,298 620,318 680,318')
    o += pill(610, 160, 'sí', 'green', solid=True)
    o += pill(610, 310, 'no', 'rose', solid=True)
    o += box(682, 112, 230, 84, 'green', "'/home'", ['HomeScreen: el usuario', 'sigue adentro.'], title_size=14, mono_title=True, size=12.5)
    o += box(682, 276, 230, 84, 'rose', "'/login'", ['LoginScreen: primera vez,', 'o cerró sesión.'], title_size=14, mono_title=True, size=12.5)
    return o + end(fid, h, "initialRoute: AuthService().isLoggedIn() ? '/home' : '/login'")


@fig
def auSalir():
    fid, h = 'auSalir', 420
    o = start(fid, h, 'Cerrar sesión y rehacer la pila', 'signOut borra la sesión. pushNamedAndRemoveUntil deja solo el login.',
              'A la izquierda, la pila antes: /home encima. Al centro, las dos líneas de _logout: await signOut y '
              'pushNamedAndRemoveUntil con route false. A la derecha, la pila después: solo /login. Debajo, la nota: '
              'con un pop, o con push sin quitar, el botón atrás volvería a la lista.')
    o += txt(48, 128, 'PILA ANTES', 12, 700, MUTED)
    o += box(48, 144, 200, 52, 'green', "'/home'", [], title_size=14, mono_title=True)
    o += txt(148, 222, 'la única pantalla', 12, 400, FAINT, 'middle')
    o += box(300, 128, 360, 132, 'indigo', '_logout()', ['await _authService.signOut();', 'if (!mounted) return;', "pushNamedAndRemoveUntil('/login',", '    (route) => false);'],
             title_size=14, mono_title=True, size=12.5)
    o += arrow(fid, 'M250,170 H298')
    o += arrow(fid, 'M662,170 H710')
    o += txt(712, 128, 'PILA DESPUÉS', 12, 700, MUTED)
    o += box(712, 144, 200, 52, 'rose', "'/login'", [], title_size=14, mono_title=True)
    o += txt(812, 222, 'atrás cierra la app', 12, 400, FAINT, 'middle')
    o += box(48, 292, 864, 72, 'amber', None, ['El orden importa: primero signOut y después navegar. Si solo navegas, la sesión sigue guardada', 'y la próxima vez que abra la app, initialRoute lo vuelve a meter a /home.'], size=12.5)
    return o + end(fid, h)


# ───────────────────────────── S0087 · Taller

@fig
def tlAuthPiezas():
    fid, h = 'tlAuthPiezas', 450
    o = start(fid, h, 'Quién llama a quién', 'Las pantallas llaman a los servicios. Solo los servicios hablan con Supabase.',
              'Tres columnas. Pantallas: LoginScreen, SignupScreen y HomeScreen. Servicios: AuthService, ProfileService '
              'y TrackService. Supabase: Auth, la tabla profiles y la tabla tracks. Flechas: Login a AuthService, '
              'Signup a AuthService y a ProfileService, Home a AuthService y a TrackService; cada servicio a su parte '
              'de Supabase. Los dos servicios vacíos están marcados.')
    cols = [(48, 'PANTALLAS', [('LoginScreen', 'slate'), ('SignupScreen', 'slate'), ('HomeScreen', 'slate')]),
            (364, 'SERVICIOS', [('AuthService', 'rose'), ('ProfileService', 'rose'), ('TrackService', 'green')]),
            (680, 'SUPABASE', [('Auth · auth.users', 'violet'), ('tabla profiles', 'indigo'), ('tabla tracks', 'teal')])]
    ys = [140, 230, 320]
    for x, label, items in cols:
        o += txt(x, 124, label, 12, 700, MUTED)
        for (name, c), y in zip(items, ys):
            o += box(x, y, 232, 60, c, None, [])
            o += txt(x + 116, y + 35, name, 14, 700, FAM[c][2], 'middle', mono=True)
    for a, b in [(0, 0), (1, 0), (1, 1), (2, 0), (2, 2)]:
        o += arrow(fid, f'M282,{ys[a] + 30} C320,{ys[a] + 30} 326,{ys[b] + 30} 362,{ys[b] + 30}')
    for i in range(3):
        o += arrow(fid, f'M598,{ys[i] + 30} H678')
    o += pill(540, 120, 'rojo: vacíos', 'rose')
    return o + end(fid, h, 'TrackService viene completo de la sesión 12. Al final del taller le agregas el dueño de cada track.')


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
