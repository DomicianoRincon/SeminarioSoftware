"""Figuras SVG de las lecciones de la sesión 14 (S0088 a S0092, Servicio de storage).

    python3 tools/sesion14_figuras.py <carpeta> [id ...]   escribe un .svg por figura, para revisarlas
    python3 tools/sesion14_figuras.py --inject             reemplaza cada bloque ```svg de las lecciones
                                                           de la sesión por la figura con el mismo id

Foto de perfil en un bucket público de Supabase Storage, hecha con las skills sdd-tecnicas y
sdd-implementar sobre la app de tracks (repositorio 262SeminarioSesion14).
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from console_frame import frame  # noqa: E402
from sesion2_figuras import FAM  # noqa: E402
from sesion10_figuras import INK, BODY, MUTED, FAINT, LINE, txt, start, end, box, arrow, pill, tree, doc  # noqa: E402
from sesion11_figuras import BX, BY, BW, browser, ring, side_cards, button  # noqa: E402
from sesion13_figuras import mini, table, logout_icon, ACCENT  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
LESSONS = ['lessonS88.md', 'lessonS89.md', 'lessonS90.md', 'lessonS91.md', 'lessonS92.md']
STAMP = '20261125140000'
UID = '3f9a1c27-…'

FIGS = {}


def fig(fn):
    FIGS[fn.__name__] = fn
    return fn


def avatar(cx, cy, r, letter='A'):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#E8DEF8"/>'
            + txt(cx, cy + r * 0.34, letter, r * 0.9, 700, ACCENT, 'middle'))


def icon(kind, x, y, color=INK):
    """Íconos de 18 px: galería, cámara e historial."""
    s = f'fill="none" stroke="{color}" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"'
    if kind == 'gallery':
        return f'<rect x="{x}" y="{y}" width="18" height="16" rx="3" {s}/><path d="M{x + 2},{y + 13} l5,-6 4,4 2,-2 3,4" {s}/>'
    if kind == 'camera':
        return (f'<path d="M{x},{y + 4} h4 l2,-3 h6 l2,3 h4 v12 h-18 Z" {s}/>'
                f'<circle cx="{x + 9}" cy="{y + 10}" r="3.5" {s}/>')
    return f'<circle cx="{x + 9}" cy="{y + 9}" r="8" {s}/><path d="M{x + 9},{y + 4} v5 l3,2" {s}/>'


def check(x, y, done):
    if done:
        return (f'<rect x="{x}" y="{y - 11}" width="14" height="14" rx="3" fill="#3A8235"/>'
                f'<path d="M{x + 3},{y - 4} l3,3 5,-6" fill="none" stroke="#FFFFFF" stroke-width="1.8"/>')
    return f'<rect x="{x}" y="{y - 11}" width="14" height="14" rx="3" fill="#FFFFFF" stroke="{MUTED}" stroke-width="1.4"/>'


# ───────────────────────────── S0088 · Repositorio de arranque

@fig
def fpPantallas():
    fid, h = 'fpPantallas', 620
    o = start(fid, h, 'De dónde sale y a dónde va la foto', 'La lista y el perfil ya vienen. Lo punteado es lo que hace el implementador en el taller.',
              'Tres teléfonos en fila. HomeScreen con la lista de tracks y, arriba a la derecha, el botón de perfil con '
              'la inicial A. ProfileScreen con un círculo grande con la A, el nombre Ana Gómez, el correo y un botón '
              'punteado Cambiar foto. El tercero es el mismo perfil oscurecido con un panel que sube desde abajo: '
              'Cambiar foto de perfil, con Elegir de la galería (T-09), Tomar una foto (T-11) y Mis fotos anteriores '
              '(T-12). Flechas: el botón de perfil abre ProfileScreen con pushNamed y Cambiar foto abre el panel.')
    y, xs = 140, [64, 380, 696]
    body = (f'<rect x="{xs[0] + 14}" y="{y + 58}" width="172" height="30" rx="15" fill="{ACCENT}"/>'
            + txt(xs[0] + 100, y + 77.5, '+ Crear track', 12.5, 600, '#FFFFFF', 'middle'))
    for i, (n, a) in enumerate([('Yellow', 'Coldplay'), ('Clocks', 'Coldplay'), ('Bohemian…', 'Queen')]):
        cy = y + 102 + i * 58
        body += f'<rect x="{xs[0] + 14}" y="{cy}" width="172" height="48" rx="10" fill="#FFFFFF" stroke="#E3E3EA"/>'
        body += f'<rect x="{xs[0] + 22}" y="{cy + 8}" width="32" height="32" rx="7" fill="#B69DF8"/>'
        body += txt(xs[0] + 62, cy + 21, n, 12.5, 700, INK, fit=110) + txt(xs[0] + 62, cy + 37, a, 12, 400, MUTED, fit=110)
    body += avatar(xs[0] + 150, y + 22, 12) + logout_icon(xs[0] + 174, y + 14)
    o += mini(xs[0], y, 'Mis tracks', body, badge="'/home'")
    o += txt(xs[0] + 100, y - 18, 'HomeScreen', 13.5, 700, INK, 'middle', mono=True)
    o += f'<rect x="{xs[0] + 134}" y="{y + 6}" width="32" height="32" rx="8" fill="none" stroke="#C2354F" stroke-width="2" stroke-dasharray="4 3"/>'
    o += pill(xs[0] + 186, y - 18, 'T-10', 'rose', mono=True)

    def profile(x, dim=False):
        b = avatar(x + 100, y + 104, 40)
        b += txt(x + 100, y + 172, 'Ana Gómez', 15, 700, INK, 'middle')
        b += txt(x + 100, y + 192, 'ana@correo.com', 12, 400, MUTED, 'middle')
        b += (f'<rect x="{x + 48}" y="{y + 210}" width="104" height="28" rx="14" fill="#FFFFFF" stroke="{ACCENT}" '
              f'stroke-width="1.5" stroke-dasharray="5 4"/>' + txt(x + 100, y + 228.5, 'Cambiar foto', 12, 600, ACCENT, 'middle'))
        if dim:
            b += f'<rect x="{x}" y="{y}" width="200" height="300" rx="18" fill="#161A26" opacity=".45"/>'
        return b
    o += mini(xs[1], y, '← Mi perfil', profile(xs[1]), badge="'/profile'")
    o += txt(xs[1] + 100, y - 18, 'ProfileScreen', 13.5, 700, INK, 'middle', mono=True)
    sheet = profile(xs[2], True)
    sy = y + 132
    sheet += (f'<path d="M{xs[2]},{sy + 16} A16,16 0 0 1 {xs[2] + 16},{sy} H{xs[2] + 184} A16,16 0 0 1 {xs[2] + 200},{sy + 16} '
              f'V{y + 282} A18,18 0 0 1 {xs[2] + 182},{y + 300} H{xs[2] + 18} A18,18 0 0 1 {xs[2]},{y + 282} Z" fill="#FFFFFF"/>')
    sheet += f'<rect x="{xs[2] + 84}" y="{sy + 8}" width="32" height="4" rx="2" fill="#C4CBD8"/>'
    sheet += txt(xs[2] + 16, sy + 36, 'Cambiar foto de perfil', 13, 700, INK, fit=170)
    for i, (k, label, task) in enumerate([('gallery', 'Elegir de la galería', 'T-09'), ('camera', 'Tomar una foto', 'T-11'),
                                          ('history', 'Mis fotos anteriores', 'T-12')]):
        ry = sy + 56 + i * 36
        sheet += icon(k, xs[2] + 14, ry) + txt(xs[2] + 40, ry + 13, label, 11.5, 400, INK, fit=112)
        sheet += pill(xs[2] + 176, ry + 8, task, 'rose', mono=True)
    o += mini(xs[2], y, '← Mi perfil', sheet, badge='showModalBottomSheet')
    o += txt(xs[2] + 100, y - 18, 'el panel de abajo', 13.5, 700, INK, 'middle')
    o += arrow(fid, f'M{xs[0] + 162},{y + 36} C{xs[0] + 250},{y + 60} {xs[1] - 60},{y + 104} {xs[1] - 12},{y + 104}')
    o += pill(xs[1] - 58, y + 80, 'pushNamed', 'indigo', mono=True)
    o += arrow(fid, f'M{xs[1] + 156},{y + 224} H{xs[2] - 12}')
    o += box(48, y + 380, 864, 44, 'slate', None, [])
    o += txt(480, y + 407, 'Ya viene: el botón de perfil con la inicial y ProfileScreen. En rojo, la tarea del implementador que lo completa.',
             12.5, 600, BODY, 'middle', fit=840)
    return o + end(fid, h, 'La inicial sale del nombre del perfil. Cuando haya foto, ProfileAvatar muestra la foto en su lugar.')


@fig
def fpCarpetas():
    fid = 'fpCarpetas'
    rows = [(0, '262SeminarioSesion14/', 'dir', None),
            (1, '.agents/skills/', 'dir', ('Antigravity CLI · 11 skills', 'indigo')),
            (1, '.claude/skills/', 'dir', ('Claude Code · las mismas 11', 'indigo')),
            (1, 'AGENTS.md · CLAUDE.md', 'file', ('CLAUDE.md solo importa AGENTS.md', 'slate')),
            (1, 'docs/', 'dir', None),
            (2, 'prd.md · requisitos.md · spine', 'file', ('de las sesiones 10 y 11', 'slate')),
            (2, 'specs/', 'dir', ('F-01 a F-04, sin tecnología', 'violet')),
            (2, 'tecnicas/', 'dir', ('TS-01 a TS-04, con sus tareas', 'teal')),
            (2, 'impl_progress.md', 'file', ('8 de 12 tareas hechas', 'green')),
            (2, 'standard_code.md', 'file', ('las reglas del código', 'amber')),
            (1, 'lib/', 'dir', None),
            (2, 'components/profile_avatar.dart', 'file', ('la foto o la inicial', 'indigo')),
            (2, 'screens/profile_screen.dart', 'file', ('nombre, correo y avatar', 'indigo')),
            (2, 'services/ · models/ · screens/', 'file', ('la solución de la sesión 13', 'slate'))]
    h = 136 + len(rows) * 26 + 64
    o = start(fid, h, 'Lo que trae el repositorio', 'La app de la sesión 13 resuelta, el perfil, las specs y las skills para Antigravity y para Claude.',
              'Árbol del repositorio: .agents/skills y .claude/skills con las mismas once skills, AGENTS.md y CLAUDE.md, '
              'docs con el PRD, los requisitos, la spine, specs F-01 a F-04, tecnicas TS-01 a TS-04, impl_progress.md '
              'con 8 de 12 tareas hechas y standard_code.md, y en lib el componente profile_avatar y la pantalla '
              'profile_screen.')
    o += f'<rect x="48" y="112" width="864" height="{len(rows) * 26 + 24}" rx="12" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>'
    o += tree(rows, step=26, tag_x=600)
    return o + end(fid, h)


# ───────────────────────────── S0089 · De spec funcional a spec técnica

@fig
def tiCadena():
    fid, h = 'tiCadena', 520
    o = start(fid, h, 'De la spec funcional al código', 'Dos skills nuevas cierran el ciclo: una escribe las tareas y la otra las hace.',
              'Tres documentos en fila. F-04, la spec funcional, dice qué hace la app sin tecnología. La skill '
              'sdd-tecnicas la lee y escribe TS-04, la spec técnica, con las piezas, los datos y los paquetes, y las '
              'tareas T-09 a T-12 pendientes en impl_progress.md. Debajo, la skill sdd-implementar toma una tarea, '
              'escribe el código en lib y la marca como hecha. Abajo a la izquierda, lo que hace la persona: preparar '
              'Supabase a mano y probar.')
    cols = [(48, 'violet', 'docs/specs/', 'F-04 · funcional', ['Qué hace la app.', 'Sin tecnología.', 'Criterios CA-1…CA-11.']),
            (380, 'teal', 'docs/tecnicas/', 'TS-04 · técnica', ['Con qué piezas: Screens,', 'componentes, servicios,', 'datos y paquetes.']),
            (712, 'green', 'docs/', 'impl_progress.md', ['T-09  [ ]', 'T-10  [ ]', 'T-11  [ ]', 'T-12  [ ]'])]
    for x, c, folder, title, lines in cols:
        o += txt(x, 132, folder, 12, 700, MUTED, mono=True)
        o += box(x, 144, 200, 150, c, title, lines, mono_title=True, size=12.5)
    o += arrow(fid, 'M252,219 H372') + pill(312, 196, 'sdd-tecnicas', 'teal', mono=True, solid=True)
    o += arrow(fid, 'M584,219 H704') + pill(644, 196, 'lo escribe', 'teal')
    o += arrow(fid, 'M812,298 V356')
    o += pill(740, 328, 'sdd-implementar', 'green', mono=True, solid=True)
    o += box(712, 360, 200, 84, 'slate', 'lib/', ['El código de una tarea.'], mono_title=True, size=12.5)
    o += f'<path class="link" d="M906,360 C940,330 940,300 906,290" stroke-dasharray="5 5"/>'
    o += txt(930, 330, '[x]', 12, 700, FAM['green'][2], 'middle', mono=True)
    o += box(48, 360, 532, 84, 'amber', 'Lo tuyo', ['Revisar cada documento, hacer a mano lo que pide Supabase', 'y probar la app al terminar cada tarea.'],
             size=12.5)
    return o + end(fid, h, 'La spec técnica sí nombra tecnología: es lo que la diferencia de la funcional.')


@fig
def tiFuncTec():
    rows = [('Desde abajo sube un panel con las', 'opciones de dónde sacar la foto.',
             'showModalBottomSheet con el componente', 'PhotoSourceSheet: una función por opción.'),
            ('La foto nueva aparece en el perfil', 'sin reiniciar la app.',
             '_profile = _profile!.copyWith(avatarUrl: url)', 'dentro de setState, en ProfileScreen.'),
            ('Cada foto subida queda en el historial,', 'aunque ya no sea la del perfil.',
             'avatars/<id del usuario>/<milisegundos>.jpg', 'en un bucket público. Nunca se sobrescribe.'),
            ('Se puede tomar con la cámara en', 'Android, iOS, web y macOS.',
             'camera en Android, iOS y web;', 'camera_macos en macOS, según la plataforma.')]
    fid, h = 'tiFuncTec', 140 + len(rows) * 90 + 40
    o = start(fid, h, 'La misma regla, dicha dos veces', 'A la izquierda lo que pide F-04. A la derecha cómo lo resuelve TS-04.',
              'Cuatro filas. Cada una une una frase de la spec funcional, sin tecnología, con su traducción técnica: el '
              'panel que sube desde abajo es showModalBottomSheet con PhotoSourceSheet; la foto que aparece sin '
              'reiniciar es copyWith dentro de setState; el historial es la ruta avatars/id/milisegundos.jpg en un '
              'bucket público; la cámara en cuatro plataformas es camera y camera_macos.')
    o += txt(48, 128, 'F-04 · FUNCIONAL', 12, 700, FAM['violet'][2]) + txt(512, 128, 'TS-04 · TÉCNICA', 12, 700, FAM['teal'][2])
    for i, (a, b, c, d) in enumerate(rows):
        y = 144 + i * 90
        o += box(48, y, 400, 72, 'violet', None, [a, b], size=12.5)
        o += box(512, y, 400, 72, 'teal', None, [], size=12.5)
        o += txt(528, y + 30, c, 12, 700, INK, mono=True, fit=372) + txt(528, y + 50, d, 12.5, 400, BODY, fit=372)
        o += arrow(fid, f'M452,{y + 36} H504')
    return o + end(fid, h, 'Si mañana cambia el paquete de la cámara, cambia la técnica. La funcional sigue igual.')


# ───────────────────────────── S0090 · El implementador

@fig
def tiManifiesto():
    fid, h = 'tiManifiesto', 560
    o = start(fid, h, 'impl_progress.md, el manifiesto', 'Una línea por tarea. Lo escribe sdd-tecnicas y lo marca sdd-implementar.',
              'Maqueta del archivo docs/impl_progress.md. Arriba, Actualizado y Hechas: 8 de 12, señalado con el 1. '
              'Debajo, la sección TS-03 con la tarea T-08 marcada, con su fecha, sus archivos y una nota, señalada con '
              'el 2. Después la sección TS-04 con T-09 a T-12 sin marcar, cada una con los criterios que cubre y de qué '
              'tarea depende, señaladas con el 3.')
    x, w, y0 = 48, 600, 112
    o += f'<rect x="{x}" y="{y0}" width="{w}" height="392" rx="12" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>'
    o += f'<path d="M{x},{y0 + 12} A12,12 0 0 1 {x + 12},{y0} H{x + w - 12} A12,12 0 0 1 {x + w},{y0 + 12} V{y0 + 36} H{x} Z" fill="#EFF1F5"/>'
    o += txt(x + 16, y0 + 23, 'docs/impl_progress.md', 12, 700, MUTED, mono=True)
    lx = x + 20
    o += txt(lx, y0 + 66, '# Avance de la implementación · Tracks', 13, 700, INK, mono=True, fit=w - 40)
    o += txt(lx, y0 + 92, 'Actualizado: 2026-11-17 · Hechas: 8 de 12', 12, 400, BODY, mono=True, fit=w - 40)
    o += ring(lx + 168, y0 + 78, 132, 20, 1)
    o += txt(lx, y0 + 128, '## TS-03 · Perfil', 12.5, 700, FAM['teal'][2], mono=True)
    o += check(lx, y0 + 156, True) + txt(lx + 22, y0 + 156, 'T-08 ProfileScreen, su ruta y el botón · CA-1, CA-2', 12, 400, INK, mono=True, fit=w - 60)
    for i, ln in enumerate(['- Hecha: 2026-11-17', '- Archivos: lib/screens/profile_screen.dart (nuevo), …', '- Notas: nada.']):
        o += txt(lx + 34, y0 + 178 + i * 20, ln, 12, 400, MUTED, mono=True, fit=w - 80)
    o += ring(lx - 4, y0 + 142, w - 32, 96, 2)
    o += txt(lx, y0 + 266, '## TS-04 · Foto de perfil', 12.5, 700, FAM['teal'][2], mono=True)
    for i, t in enumerate(['T-09 Cambiar la foto desde la galería · depende de: T-08', 'T-10 La foto en el botón de HomeScreen · depende de: T-09',
                           'T-11 Tomar la foto con la cámara · depende de: T-09', 'T-12 Historial de fotos · depende de: T-09']):
        yy = y0 + 294 + i * 22
        o += check(lx, yy, False) + txt(lx + 22, yy, t, 12, 400, INK, mono=True, fit=w - 60)
    o += ring(lx - 4, y0 + 280, w - 32, 82, 3)
    o += side_cards([
        (1, 'La cuenta', ['Cuántas van. La actualiza', 'el implementador.'], 'amber'),
        (2, 'Una tarea hecha', ['[x], la fecha, los archivos', 'que tocó y lo que el', 'siguiente debe saber.'], 'amber'),
        (3, 'Lo que falta', ['[ ], los criterios que', 'cubre y de qué tarea', 'depende.'], 'amber'),
    ])
    return o + end(fid, h, 'Es texto plano: lo lees tú, lo lee tu compañero y lo lee el agente en la siguiente sesión.')


@fig
def tiBucle():
    fid, h = 'tiBucle', 470
    o = start(fid, h, 'Lo que hace sdd-implementar con una tarea', 'Siete pasos, siempre en el mismo orden. Solo marca la tarea si compila.',
              'Siete cajas en dos filas. Arriba, de izquierda a derecha: 1 elige la tarea, la pedida o la primera '
              'pendiente con sus dependencias hechas; 2 lee la spec técnica y standard_code.md; 3 pregunta por la '
              'preparación en Supabase, que haces tú en el dashboard; 4 implementa solo esa tarea. Abajo, de derecha '
              'a izquierda: 5 flutter analyze, que vuelve al 4 si hay errores; 6 marca la tarea en impl_progress.md; '
              '7 te dice cómo probarla.')
    top = [('Elige la tarea', ['La que pidas, o la', 'primera [ ] con sus', 'dependencias en [x].'], 'indigo'),
           ('Lee', ['La TS de la tarea,', 'la spec funcional y', 'standard_code.md.'], 'indigo'),
           ('Pregunta', ['¿Ya está la', 'preparación en', 'Supabase? Tú la haces.'], 'amber'),
           ('Implementa', ['Solo esa tarea.', 'Paquetes con', 'flutter pub add.'], 'violet')]
    bottom = [('flutter analyze', ['Si hay errores,', 'vuelve al 4.'], 'violet'),
              ('Marca [x]', ['Fecha, archivos y', 'notas en', 'impl_progress.md.'], 'green'),
              ('Te dice qué probar', ['Qué hacer en la app', 'y qué debes ver.'], 'green')]
    w, gap = 192, 32
    for i, (t, ls, c) in enumerate(top):
        x = 48 + i * (w + gap)
        o += box(x, 120, w, 130, c, t, ls, num=i + 1, size=12.5)
        if i < 3:
            o += arrow(fid, f'M{x + w + 2},185 H{x + w + gap - 4}')
    for i, (t, ls, c) in enumerate(bottom):
        x = 48 + (3 - i) * (w + gap)
        o += box(x, 300, w, 112, c, t, ls, num=i + 5, size=12.5)
        if i < 2:
            o += arrow(fid, f'M{x - 2},356 H{x - gap + 4}')
    o += arrow(fid, 'M816,254 V296')
    o += arrow(fid, 'M780,296 V254', dashed=True)
    o += pill(744, 276, 'errores', 'rose')
    return o + end(fid, h, 'Si la tarea choca con standard_code.md, gana el estándar y el agente lo anota en la spec técnica.')


@fig
def tiEstandar():
    fid, h = 'tiEstandar', 520
    o = start(fid, h, 'standard_code.md en un dibujo', 'Solo la Screen guarda estado. Los datos bajan por el constructor y los eventos suben con funciones.',
              'ProfileScreen arriba, en violeta, como StatefulWidget con _profile y _uploading, que cambia con setState. '
              'Debajo, dos componentes StatelessWidget: ProfileAvatar recibe name y avatarUrl, y PhotoSourceSheet '
              'recibe onGallery, onCamera y onHistory y avisa hacia arriba. A la derecha, los servicios ProfileService, '
              'StorageService y PhotoService, los únicos que hablan con Supabase o con el dispositivo, llamados con await.')
    o += box(220, 120, 340, 120, 'violet', 'ProfileScreen · StatefulWidget', ['Estado: _profile, _uploading', 'Lo cambia con setState y copyWith'],
             mono_title=True, size=12.5)
    o += box(96, 340, 260, 100, 'slate', 'ProfileAvatar', ['StatelessWidget', 'recibe name y avatarUrl'], mono_title=True, size=12.5)
    o += box(424, 340, 260, 100, 'slate', 'PhotoSourceSheet', ['StatelessWidget', 'recibe onGallery, onCamera…'], mono_title=True, size=12.5)
    o += arrow(fid, 'M300,244 V336') + pill(300, 290, 'baja: name, avatarUrl', 'indigo', mono=True)
    o += arrow(fid, 'M520,336 V244') + pill(560, 290, 'sube: onGallery()', 'amber', mono=True)
    o += box(724, 120, 188, 320, 'teal', 'lib/services/', ['ProfileService', 'StorageService', 'PhotoService', '', 'Los únicos que', 'hablan con Supabase', 'o con el dispositivo.'],
             mono_title=True, size=12.5)
    o += arrow(fid, 'M564,180 H720') + pill(642, 160, 'await', 'teal', mono=True)
    return o + end(fid, h, 'Las Screens, las Pages y los formularios son StatefulWidget. Todo lo demás, StatelessWidget.')


# ───────────────────────────── S0091 · Supabase Storage

@fig
def fpRuta():
    fid, h = 'fpRuta', 540
    o = start(fid, h, 'Bucket, ruta y URL', 'El archivo vive en el bucket. El perfil guarda la URL pública para encontrarlo.',
              'Arriba, el bucket público avatars con una carpeta por usuario, 3f9a1c27, y dentro dos fotos con nombre de '
              'milisegundos. En el medio, la URL pública partida en cinco tramos de colores: el proyecto, la parte '
              'object/public que permite leer sin sesión, el bucket, la carpeta con el id del usuario y el nombre del '
              'archivo. Abajo, la fila de profiles de Ana con avatar_url igual a esa URL.')
    o += box(48, 116, 864, 120, 'amber', None, [])
    o += txt(68, 146, 'Storage · bucket', 12, 700, MUTED) + txt(196, 146, 'avatars', 13.5, 700, FAM['amber'][2], mono=True)
    o += pill(300, 141, 'público', 'amber', solid=True)
    o += (f'<path d="M80,{172} h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2"/>'
          + txt(108, 185, f'{UID}/', 13, 700, INK, mono=True))
    for i, n in enumerate(['1763481200000.jpg', '1763494511000.jpg']):
        x = 300 + i * 240
        o += f'<rect x="{x}" y="170" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/>'
        o += txt(x + 24, 184, n, 13, 400, INK, mono=True)
    o += txt(68, 218, 'Una carpeta por usuario. Cada foto con un nombre nuevo: el momento en que se subió.', 12.5, 400, BODY, fit=820)
    parts = [('https://abcdefghijklmnopqrst.supabase.co', 'tu proyecto', 'slate'),
             ('/storage/v1/object/public/', 'se lee sin sesión', 'green'),
             ('avatars', 'el bucket', 'amber'),
             (f'/{UID}/', 'id del usuario', 'violet'),
             ('1763494511000.jpg', 'el archivo', 'indigo')]
    x, cw = 48, 7.7
    for s, label, c in parts:
        w = len(s) * cw + 8
        soft, border, strong = FAM[c]
        o += f'<rect x="{x}" y="272" width="{w:.1f}" height="30" rx="4" fill="{soft}" stroke="{border}"/>'
        o += txt(x + 4, 292, s, 12, 700, strong, mono=True)
        o += txt(x + w / 2, 324, label, 12, 600, strong, 'middle', fit=max(w, 90))
        x += w
    o += txt(48, 262, 'getPublicUrl(ruta) arma la URL. No va a internet: solo junta texto.', 12.5, 600, BODY, fit=860)
    o += table(48, 356, 864, 'profiles', ['id', 'name', 'avatar_url'],
               [[(UID, '#7439B8'), 'Ana', ('https://…/object/public/avatars/3f9a1c27-…/1763494511000.jpg', '#4453C9')]],
               'indigo', [130, 90, 644], 'la columna nueva')
    return o + end(fid, h, 'Bucket público: cualquiera con la URL ve la foto. Para subir hace falta una policy, aunque sea público.')


@fig
def fpMismoNombre():
    fid, h = 'fpMismoNombre', 470
    o = start(fid, h, 'Por qué cada foto lleva un nombre nuevo', 'Las cachés guardan la imagen por su URL. Una URL nueva no la tiene nadie.',
              'Dos columnas. A la izquierda, en rojo, el mismo nombre avatar.jpg: se sube la foto nueva encima de la vieja, '
              'la URL no cambia, y Image.network, el navegador y el CDN responden con la foto vieja que ya tenían. A la '
              'derecha, en verde, un nombre por subida: la URL es nueva, ninguna caché la tiene y se descarga la foto '
              'nueva; las fotos anteriores siguen en el bucket y son el historial.')
    for x, c, title, name, lines, tag in [
            (48, 'rose', 'Mismo nombre', 'avatars/3f9a…/avatar.jpg',
             ['Subes la foto nueva encima de la vieja.', 'La URL es la misma de antes.', 'Image.network, el navegador y el CDN',
              'ya la tienen guardada: muestran la vieja.'], 'la foto no cambia'),
            (496, 'green', 'Un nombre por subida', 'avatars/3f9a…/1763494511000.jpg',
             ['Subes con el momento como nombre.', 'La URL es nueva: nadie la tiene.', 'Se descarga la foto nueva.',
              'Las anteriores siguen ahí: son el historial.'], 'la foto cambia y hay historial')]:
        o += box(x, 120, 416, 250, c, title, [], size=12.5)
        o += txt(x + 16, 182, name, 12.5, 700, INK, mono=True, fit=384)
        for i, ln in enumerate(lines):
            o += txt(x + 16, 222 + i * 26, ln, 12.5, 400, BODY, fit=384)
        o += pill(x + 208, 398, tag, c, solid=True)
    return o + end(fid, h, 'Por eso el taller nunca usa upsert ni borra archivos: cada subida es un archivo nuevo.')


# ───────────────────────────── S0092 · Taller

def storage_nav(active):
    o = f'<rect x="{BX + 1}" y="{BY + 36}" width="150" height="347" fill="#F7F8FA"/>'
    o += f'<line x1="{BX + 151}" y1="{BY + 36}" x2="{BX + 151}" y2="{BY + 384}" stroke="{LINE}"/>'
    o += txt(BX + 16, BY + 64, 'STORAGE', 11, 700, FAINT, fit=130)
    for i, item in enumerate(('Files', 'Policies', 'Settings')):
        yy = BY + 92 + i * 30
        if item == active:
            o += f'<rect x="{BX + 8}" y="{yy - 16}" width="136" height="24" rx="6" fill="#E8F6E3"/>'
        o += txt(BX + 18, yy, item, 12.5, 700 if item == active else 400, INK if item == active else BODY, fit=124)
    return o


def toggle(tx, ty, on):
    fill = '#3ECF8E' if on else '#D5D9E0'
    knob = tx + 24 if on else tx + 10
    return (f'<rect x="{tx}" y="{ty}" width="34" height="20" rx="10" fill="{fill}"/>'
            f'<circle cx="{knob}" cy="{ty + 10}" r="7" fill="#FFFFFF"/>')


@fig
def fpNuevoBucket():
    fid, h = 'fpNuevoBucket', 540
    o = start(fid, h, 'Crear el bucket avatars', 'Storage › Files › New bucket. Se hace una sola vez, en el proyecto de tu equipo.',
              'Maqueta del panel de Supabase: menú Storage con Files seleccionado y, encima, la ventana Create a file '
              'bucket. Name of bucket con avatars, señalado con el 1. Public bucket encendido, señalado con el 2. '
              'Restrict file size apagado. El botón Create, señalado con el 3. A la derecha, una tarjeta para cada uno.')
    o += browser('supabase.com/dashboard/project/abcdefghijklmnopqrst/storage/files')
    o += storage_nav('Files')
    x, w = BX + 176, 400
    o += f'<rect x="{BX + 152}" y="{BY + 37}" width="{BW - 153}" height="346" fill="#161A26" opacity=".12"/>'
    o += f'<rect x="{x - 8}" y="{BY + 52}" width="{w + 16}" height="316" rx="12" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>'
    o += txt(x + 8, BY + 84, 'Create a file bucket', 16, 700, INK, fit=300)
    o += txt(x + 8, BY + 116, 'Name of bucket', 12.5, 600, INK)
    o += f'<rect x="{x + 8}" y="{BY + 126}" width="{w - 16}" height="32" rx="6" fill="#FFFFFF" stroke="{LINE}"/>'
    o += txt(x + 20, BY + 147, 'avatars', 13, 400, INK, mono=True)
    o += ring(x + 8, BY + 126, w - 16, 32, 1)
    o += txt(x + 8, BY + 190, 'Public bucket', 12.5, 600, INK) + toggle(x + w - 50, BY + 176, True)
    o += txt(x + 8, BY + 208, 'Anyone can read any object without any authorization.', 11.5, 400, FAINT, fit=w - 70)
    o += ring(x + 4, BY + 172, w - 8, 44, 2)
    o += txt(x + 8, BY + 248, 'Restrict file size', 12.5, 600, INK) + toggle(x + w - 50, BY + 234, False)
    o += txt(x + 8, BY + 280, 'Restrict MIME types', 12.5, 600, INK) + toggle(x + w - 50, BY + 266, False)
    o += button(x + w - 196, BY + 318, 90, 'Cancel', '#FFFFFF', INK, stroke=LINE)
    o += button(x + w - 96, BY + 318, 88, 'Create', '#3ECF8E', '#1C1C1C')
    o += ring(x + w - 96, BY + 318, 88, 32, 3)
    o += side_cards([
        (1, 'El nombre', ['avatars, en minúscula.', 'El código lo busca así.'], 'amber'),
        (2, 'Public bucket', ['Encendido: la foto se', 've con su URL, sin', 'sesión ni token.'], 'amber'),
        (3, 'Create', ['El bucket aparece en', 'la lista, vacío.'], 'amber'),
    ])
    return o + end(fid, h, 'Maqueta de la interfaz de noviembre de 2026. Si tu panel se ve distinto, busca los mismos tres campos.')


@fig
def fpPolicy():
    fid, h = 'fpPolicy', 540
    o = start(fid, h, 'Las policies del bucket', 'Storage › Policies › New policy en avatars. Público deja leer, no subir.',
              'Maqueta del editor de policies de Supabase: Policy name con subir fotos; Allowed operation con INSERT '
              'marcado, señalado con el 1; Target roles con authenticated, señalado con el 2; Policy definition con '
              "bucket_id = 'avatars', señalado con el 3; y el botón Save policy. A la derecha, una tarjeta para cada uno "
              'y una cuarta que dice que se repite con SELECT para el historial.')
    o += browser('supabase.com/dashboard/project/abcdefghijklmnopqrst/storage/policies')
    o += storage_nav('Policies')
    x, w = BX + 176, 400
    o += txt(x, BY + 66, 'Adding new policy to avatars', 15, 700, INK, fit=w)
    o += txt(x, BY + 96, 'Policy name', 12.5, 600, INK)
    o += f'<rect x="{x}" y="{BY + 104}" width="{w}" height="28" rx="6" fill="#FFFFFF" stroke="{LINE}"/>'
    o += txt(x + 10, BY + 122, 'subir fotos', 12.5, 400, INK)
    o += txt(x, BY + 156, 'Allowed operation', 12.5, 600, INK)
    for i, op in enumerate(('SELECT', 'INSERT', 'UPDATE', 'DELETE')):
        cx = x + i * 96
        o += check(cx, BY + 182, op == 'INSERT') + txt(cx + 20, BY + 182, op, 12, 600, INK, mono=True)
    o += ring(x + 92, BY + 166, 82, 22, 1)
    o += txt(x, BY + 214, 'Target roles', 12.5, 600, INK)
    o += f'<rect x="{x}" y="{BY + 222}" width="{w}" height="28" rx="6" fill="#FFFFFF" stroke="{LINE}"/>'
    o += pill(x + 56, BY + 236, 'authenticated', 'slate', mono=True)
    o += ring(x, BY + 222, w, 28, 2)
    o += txt(x, BY + 274, 'Policy definition', 12.5, 600, INK)
    o += f'<rect x="{x}" y="{BY + 282}" width="{w}" height="40" rx="6" fill="#1F2430"/>'
    o += txt(x + 12, BY + 307, "bucket_id = 'avatars'", 12.5, 400, '#E5C07B', mono=True)
    o += ring(x, BY + 282, w, 40, 3)
    o += button(x + w - 110, BY + 336, 110, 'Save policy', '#3ECF8E', '#1C1C1C')
    o += side_cards([
        (1, 'INSERT', ['Deja subir archivos', 'nuevos. Lo pide T-09.'], 'amber'),
        (2, 'authenticated', ['Solo quien inició sesión.'], 'amber'),
        (3, 'La definición', ['Solo en este bucket. Ya', 'viene escrita así.'], 'amber'),
        (4, 'Otra vez, con SELECT', ['Una segunda policy para', 'listar las fotos (T-12).'], 'teal'),
    ])
    return o + end(fid, h, 'Maqueta de la interfaz de noviembre de 2026. Sin la de INSERT: new row violates row-level security policy.')


@fig
def fpMigracion():
    name = 'add_avatar_url'
    return frame(dict(
        id='fpMigracion',
        title='La columna avatar_url',
        title_plain='La columna avatar_url',
        desc=f'En el proyecto del equipo, npx supabase migration new {name} crea el archivo {STAMP}_{name}.sql. '
             'Después de escribir el alter table, npx supabase db push --remote lo aplica y termina con Finished '
             'supabase db push. Un recuadro señala el nombre de la migración y otro el archivo que se sube.',
        sub='En el proyecto de tu equipo, como en la sesión 13.',
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
            (1, 'El nombre', ['Qué cambia: le agrega', 'una columna a profiles.'], False),
            (2, 'Lo que se sube', ['Solo la migración nueva.', 'profiles ya tenía su grant.'], False),
        ],
    ))


@fig
def fpTareas():
    fid, h = 'fpTareas', 536
    o = start(fid, h, 'Las cuatro tareas del taller', 'T-09 es obligatoria. Después escoge una o dos de las otras: todas dependen solo de T-09.',
              'A la izquierda, T-09 en una caja grande: modal inferior con Elegir de la galería, subir al bucket avatars '
              'y mostrar la foto en el perfil; necesita la columna, el bucket y la policy de INSERT. Tres flechas salen '
              'hacia la derecha: T-10, la foto en el botón de perfil de HomeScreen; T-11, Tomar una foto con camera y '
              'camera_macos; T-12, Mis fotos anteriores, que necesita la policy de SELECT.')
    o += box(48, 128, 300, 300, 'rose', 'T-09 · Galería', ['Modal inferior con', '«Elegir de la galería».', 'Sube a avatars y guarda', 'la URL en avatar_url.',
                                                           'La foto aparece en', 'el perfil.', '', 'Necesita: columna,', 'bucket y policy INSERT.'],
             size=12.5)
    o += pill(198, 452, 'obligatoria', 'rose', solid=True)
    right = [('T-10 · Avatar en Home', ['El botón de perfil de HomeScreen muestra la foto,', 'o la inicial si no hay.'], 'indigo'),
             ('T-11 · Cámara', ['Opción «Tomar una foto» y CameraScreen: camera en', 'Android, iOS y web; camera_macos en macOS.'], 'violet'),
             ('T-12 · Mis fotos anteriores', ['Opción en el modal y AvatarHistoryScreen con la', 'cuadrícula. Necesita: policy SELECT.'], 'teal')]
    for i, (t, ls, c) in enumerate(right):
        y = 128 + i * 104
        o += box(424, y, 488, 88, c, t, ls, size=12.5)
        o += arrow(fid, f'M352,278 C388,278 388,{y + 44} 420,{y + 44}')
    o += pill(668, 452, 'escoge una o dos', 'slate')
    return o + end(fid, h, 'Cada tarea se pide por separado y se prueba antes de pedir la siguiente.')


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
