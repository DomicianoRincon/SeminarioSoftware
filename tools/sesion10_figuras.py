"""Figuras SVG de las lecciones de la sesión 10 (S0069 a S0074, Spec Driven Development).

    python3 tools/sesion10_figuras.py <carpeta> [id ...]   escribe un .svg por figura, para revisarlas
    python3 tools/sesion10_figuras.py --inject             reemplaza cada bloque ```svg de las lecciones
                                                           de la sesión por la figura con el mismo id

El ejemplo de todas las figuras es la red profesional de la sesión 4 (recursos/sesion4/).
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sesion2_figuras import FAM, head  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
LESSONS = ['lessonS69.md', 'lessonS70.md', 'lessonS71.md', 'lessonS72.md', 'lessonS73.md', 'lessonS74.md']
INK, BODY, MUTED, FAINT, LINE = '#161A26', '#454C61', '#556074', '#79809A', '#C4CBD8'
PHASE = ['indigo', 'teal', 'amber', 'violet', 'green', 'rose']

FIGS = {}


def fig(fn):
    FIGS[fn.__name__] = fn
    return fn


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def width(s, size, mono=False):
    return len(s) * size * (0.6 if mono else 0.56)


def txt(x, y, s, size=13, weight=400, fill=BODY, anchor='start', mono=False, fit=None):
    cls = ' class="mono"' if mono else ''
    fit = fit or int(width(s, size, mono) + 24)
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{cls} data-fit="{fit}">{esc(s)}</text>')


def start(fid, h, title, sub, desc):
    return head(fid, h, title, title, sub, desc)


def end(fid, h, foot=None):
    out = txt(48, h - 28, foot, 12, 400, FAINT, fit=864) if foot else ''
    return out + '</svg>\n'


def box(x, y, w, h, color, title=None, lines=(), num=None, fill=None, size=13, title_size=14.5, mono_title=False,
        dashed=False, faded=False):
    soft, border, strong = FAM[color]
    dash = ' stroke-dasharray="6 5"' if dashed else ''
    op = ' opacity=".45"' if faded else ''
    o = (f'<g{op}><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill or soft}" stroke="{border}" '
         f'stroke-width="1.5"{dash}/>')
    tx = x + 16
    if num is not None:
        o += (f'<circle cx="{x + 28}" cy="{y + 27}" r="13" fill="#FFFFFF" stroke="{strong}" stroke-width="2"/>'
              + txt(x + 28, y + 31.5, str(num), 13, 700, strong, 'middle'))
        tx = x + 50
    ly = y + 30
    if title:
        o += txt(tx, y + 32, title, title_size, 700, strong, mono=mono_title, fit=x + w - tx - 8)
        ly = y + 58
    for i, line in enumerate(lines):
        o += txt(x + 16, ly + i * 19, line, size, 400, BODY, fit=w - 24)
    return o + '</g>'


def arrow(fid, d, dashed=False):
    dash = ' stroke-dasharray="5 5"' if dashed else ''
    return f'<path class="link" d="{d}"{dash}/>'


def pill(cx, cy, label, color, mono=False, solid=False):
    soft, border, strong = FAM[color]
    w = width(label, 12, mono) + 22
    bg, fg = (strong, '#FFFFFF') if solid else (soft, strong)
    return (f'<rect x="{cx - w / 2:.1f}" y="{cy - 12}" width="{w:.1f}" height="24" rx="12" fill="{bg}" '
            f'stroke="{border if not solid else strong}" stroke-width="1.2"/>'
            + txt(cx, cy + 4.5, label, 12, 700, fg, 'middle', mono))


def doc(x, y, w, h, name, color='slate', faded=False):
    soft, border, strong = FAM[color]
    op = ' opacity=".45"' if faded else ''
    return (f'<g{op}><path d="M{x},{y} h{w - 16} l16,16 v{h - 16} h-{w} Z" fill="#FFFFFF" stroke="{border}" stroke-width="1.5"/>'
            f'<path d="M{x + w - 16},{y} v16 h16" fill="{soft}" stroke="{border}" stroke-width="1.5"/>'
            + txt(x + w / 2, y + h / 2 + 5, name, 12.5, 700, strong, 'middle', True, fit=w - 8) + '</g>')


# ───────────────────────────── S0069 · ¿Qué es Spec Driven Development?

@fig
def sddContrato():
    fid, h = 'sddContrato', 430
    o = start(fid, h, 'Sin spec, el agente adivina', 'Con una spec, lo que construye se puede revisar contra algo escrito.',
              'Dos filas. Arriba, sin spec: un pedido corto llega al agente y cada vez sale una app distinta. '
              'Abajo, con spec: el agente lee la spec y lo que construye se compara con ella.')
    o += txt(48, 128, 'SIN SPEC', 12, 700, MUTED)
    o += box(48, 144, 220, 84, 'slate', '«Haz el login»', ['Un pedido de una línea.'])
    o += arrow(fid, 'M268,186 H330')
    o += box(332, 144, 180, 84, 'indigo', 'Agente', ['Llena los huecos', 'como le parece.'])
    o += arrow(fid, 'M512,186 H574')
    for i, (t, c) in enumerate((('¿Con correo?', 'amber'), ('¿Con Google?', 'amber'), ('¿Y el error?', 'rose'))):
        o += box(576 + i * 114, 152, 104, 68, c, None, [t], size=12.5)
    o += txt(576, 244, 'Cada vez decide distinto. ¿Cuál era la correcta?', 12.5, 600, '#C2354F', fit=340)
    o += txt(48, 292, 'CON SPEC', 12, 700, MUTED)
    o += doc(48, 308, 220, 84, 'F-01 · Registrarse', 'teal')
    o += arrow(fid, 'M268,350 H330')
    o += box(332, 308, 180, 84, 'indigo', 'Agente', ['Construye lo que', 'dice la spec.'])
    o += arrow(fid, 'M512,350 H574')
    o += box(576, 308, 336, 84, 'green', 'Se revisa contra la spec', ['¿Cumple cada criterio de aceptación?', 'Sí o no, sin discutir gustos.'])
    return o + end(fid, h)


@fig
def sddFases():
    fid, h = 'sddFases', 452
    o = start(fid, h, 'Las seis fases de Spec Driven Development',
              'Cada fase responde una pregunta y deja un documento. Las tres primeras son specs.',
              'Seis tarjetas en fila: producto, funcional, arquitectura, tareas, implementación y validación, '
              'cada una con su pregunta. Una flecha vuelve de validación a las specs: si no cumple, se corrige '
              'la spec o el código.')
    phases = [('Producto', 'Requirements', ['¿Qué problema,', 'para quién?']),
              ('Funcional', 'Functional spec', ['¿Qué hace el', 'sistema?']),
              ('Arquitectura', 'Technical design', ['¿Cómo se', 'construye?']),
              ('Tareas', 'Plan / Tasks', ['¿En qué', 'orden?']),
              ('Código', 'Implementation', ['Se escribe o', 'se genera.']),
              ('Validación', 'Testing', ['¿Cumple la', 'spec?'])]
    w, gap, y = 132, 14.4, 156
    xs = [48 + i * (w + gap) for i in range(6)]
    o += f'<path d="M{xs[0]},132 H{xs[2] + w}" stroke="#4453C9" stroke-width="3" stroke-linecap="round"/>'
    o += txt(xs[0], 122, 'LAS SPECS · EL QUÉ Y EL CÓMO', 12, 700, '#4453C9', fit=420)
    o += f'<path d="M{xs[3]},132 H{xs[5] + w}" stroke="#9AA1B2" stroke-width="3" stroke-linecap="round"/>'
    o += txt(xs[3], 122, 'CONSTRUIR Y COMPROBAR', 12, 700, MUTED, fit=420)
    for i, (name, en, q) in enumerate(phases):
        soft, border, strong = FAM[PHASE[i]]
        x = xs[i]
        o += f'<rect x="{x}" y="{y}" width="{w}" height="168" rx="14" fill="{soft}" stroke="{border}" stroke-width="1.5"/>'
        o += (f'<circle cx="{x + 26}" cy="{y + 28}" r="13" fill="#FFFFFF" stroke="{strong}" stroke-width="2"/>'
              + txt(x + 26, y + 32.5, str(i + 1), 13, 700, strong, 'middle'))
        o += txt(x + 14, y + 72, name, 15, 700, strong, fit=w - 20)
        o += txt(x + 14, y + 92, en, 12, 400, FAINT, fit=w - 20)
        for j, line in enumerate(q):
            o += txt(x + 14, y + 124 + j * 19, line, 13, 600, INK, fit=w - 20)
        if i < 5:
            o += arrow(fid, f'M{x + w + 1},{y + 84} H{x + w + gap - 1}')
    by = y + 168
    o += arrow(fid, f'M{xs[5] + w / 2},{by + 2} V{by + 40} H{xs[1] + w / 2} V{by + 4}')
    o += txt((xs[1] + xs[5] + w) / 2, by + 62, 'Si no cumple, se corrige la spec o el código, y se vuelve a validar.',
             13, 600, MUTED, 'middle', fit=560)
    return o + end(fid, h)


@fig
def sddHoy():
    fid, h = 'sddHoy', 400
    o = start(fid, h, 'Del contexto a las specs, documento por documento',
              'Cinco pasos en tu proyecto, en dos sesiones. Cada uno lee lo que dejó el anterior.',
              'Cinco documentos numerados en orden: AGENTS.md, docs/prd.md, docs/requisitos.md, '
              'docs/architectural_spine.md y docs/specs/, cada uno con la fase a la que pertenece. Debajo, atenuados, '
              'los de las próximas sesiones: spec técnica, tareas, código y pruebas.')
    steps = [('AGENTS.md', 'Contexto', 'slate'), ('docs/prd.md', 'Fase 1', 'indigo'),
             ('docs/requisitos.md', 'Fase 1', 'indigo'), ('docs/architectural_spine.md', 'Fase 3 · inicial', 'amber'),
             ('docs/specs/', 'Fase 2', 'teal')]
    o += txt(48, 128, 'SESIONES 10 Y 11', 12, 700, '#4453C9')
    ws, gap = [148, 156, 164, 228, 136], 8
    for i, (name, phase, c) in enumerate(steps):
        w = ws[i]
        x = 48 + sum(ws[:i]) + i * gap
        soft, border, strong = FAM[c]
        o += f'<rect x="{x}" y="144" width="{w}" height="112" rx="12" fill="{soft}" stroke="{border}" stroke-width="1.5"/>'
        o += (f'<circle cx="{x + 26}" cy="170" r="13" fill="#FFFFFF" stroke="{strong}" stroke-width="2"/>'
              + txt(x + 26, 174.5, str(i + 1), 13, 700, strong, 'middle'))
        o += pill(x + w - 14 - (width(phase, 12) + 22) / 2, 170, phase, c)
        parts = name.split('/', 1) if len(name) > 18 else [name]
        if len(parts) > 1:
            o += txt(x + 14, 214, parts[0] + '/', 12.5, 700, INK, mono=True, fit=w - 20)
            o += txt(x + 14, 234, parts[1], 12.5, 700, INK, mono=True, fit=w - 20)
        else:
            o += txt(x + 14, 222, name, 12.5, 700, INK, mono=True, fit=w - 20)
        if i < 4:
            o += arrow(fid, f'M{x + w + 1},200 H{x + w + gap - 1}')
    o += txt(48, 300, 'PRÓXIMAS SESIONES', 12, 700, FAINT)
    for i, name in enumerate(('Spec técnica', 'Tareas', 'Código', 'Pruebas')):
        o += box(48 + i * 220, 314, 204, 44, 'slate', None, [], dashed=True, faded=True)
        o += txt(48 + i * 220 + 102, 341, name, 13.5, 700, FAINT, 'middle')
    return o + end(fid, h)


@fig
def sddQueComo():
    fid, h = 'sddQueComo', 360
    o = start(fid, h, 'Spec funcional y spec técnica', 'La misma funcionalidad, dos preguntas distintas.',
              'Dos columnas sobre cambiar la foto de perfil. A la izquierda la spec funcional dice qué ve y qué '
              'puede hacer el usuario, sin tecnología. A la derecha, atenuada, la spec técnica dice con qué '
              'pantallas, servicios y almacenamiento se construye; se hace más adelante.')
    o += box(48, 120, 420, 196, 'teal', 'Funcional · el qué', [
        'El usuario elige una foto de su galería.', 'Ve la foto nueva en su perfil.',
        'Si pesa más de 5 MB, ve «La foto pesa demasiado».', 'Sin conexión, la foto anterior se conserva.',
        '', 'Habla el idioma del usuario.', 'No nombra ninguna tecnología.'])
    o += box(492, 120, 420, 196, 'amber', 'Técnica · el cómo', [
        'ProfileScreen guarda la foto con setState.', 'ProfileService la sube al bucket avatars.',
        'La ruta queda en la columna foto_url.', 'Usa supabase_flutter.', '',
        'Habla el idioma del código.', 'Llega en una sesión posterior.'], dashed=True)
    o += pill(830, 152, 'después', 'amber')
    return o + end(fid, h)


# ───────────────────────────── S0070 · Anatomía de una spec

@fig
def spAnatomia():
    fid, h = 'spAnatomia', 560
    o = start(fid, h, 'Las partes de una spec', 'Un archivo Markdown: arriba los metadatos, abajo el comportamiento.',
              'Un archivo F-03 a la izquierda con su encabezado de metadatos y sus apartados. A la derecha cuatro '
              'tarjetas: metadatos, comportamiento, cómo se comprueba y lo que falta, unidas a su parte del archivo.')
    x, y, w = 48, 116, 420
    o += f'<rect x="{x}" y="{y}" width="{w}" height="408" rx="12" fill="#1F2430"/>'
    o += txt(x + 16, y + 26, 'docs/specs/F-03-foto-de-perfil.md', 12, 400, '#9AA3B5', mono=True, fit=w - 24)
    meta = ['---', 'id: F-03', 'titulo: Cambiar la foto de perfil', 'version: 0.2.0', 'fecha: 2026-11-04',
            'estado: borrador', 'requisitos: [RF-07, RF-08]', '---']
    for i, ln in enumerate(meta):
        col = '#7FD9A8' if ':' in ln else '#79809A'
        o += txt(x + 16, y + 56 + i * 20, ln, 13, 400, col, mono=True, fit=w - 24)
    secs = [('# F-03 · Cambiar la foto de perfil', '#E6EAF2'), ('## Objetivo', '#A9B4F2'), ('## Flujo principal', '#A9B4F2'),
            ('## Reglas · ## Estados', '#A9B4F2'), ('## Criterios de aceptación', '#F0C572'),
            ('## Fuera de alcance', '#F3A3B2'), ('## Preguntas abiertas', '#F3A3B2'), ('## Historial', '#79809A')]
    for i, (ln, col) in enumerate(secs):
        o += txt(x + 16, y + 236 + i * 20, ln, 13, 700 if i == 0 else 400, col, mono=True, fit=w - 24)
    marks = [(y + 40, 168, 'green'), (y + 241, 60, 'indigo'), (y + 302, 20, 'amber'), (y + 323, 40, 'rose')]
    for (my, mh, c) in marks:
        o += f'<rect x="{x + 6}" y="{my}" width="{w - 12}" height="{mh}" rx="6" fill="none" stroke="{FAM[c][2]}" stroke-width="2"/>'
    cards = [('green', 'Metadatos', ['Qué spec es, de qué versión,', 'de cuándo, en qué estado y', 'qué requisitos cubre.']),
             ('indigo', 'Comportamiento', ['Para qué sirve, los pasos,', 'las reglas y los estados', 'de cargando, vacío y error.']),
             ('amber', 'Cómo se comprueba', ['Criterios de aceptación:', 'Dado… cuando… entonces…']),
             ('rose', 'Lo que falta', ['Lo que no cubre y lo que', 'el equipo no ha decidido.'])]
    cy = [116, 228, 340, 436]
    hs = [100, 100, 84, 84]
    for i, (c, t, lines) in enumerate(cards):
        o += box(508, cy[i], 404, hs[i], c, t, lines)
        my, mh, _ = marks[i]
        o += f'<path d="M{x + w - 6},{my + mh / 2} H488 V{cy[i] + 30} H506" fill="none" stroke="{FAM[c][2]}" stroke-width="1.5"/>'
    return o + end(fid, h)


@fig
def spSiNo():
    fid, h = 'spSiNo', 480
    o = start(fid, h, 'Qué sí va y qué no va en una spec', 'Si describe lo que ve el usuario, va. Si describe cómo se construye, no.',
              'Dos columnas. Sí va: actor y objetivo, flujos, reglas, estados, criterios de aceptación y preguntas '
              'abiertas. No va: código y widgets, tablas y SQL, colores y tamaños, tareas y palabras vagas.')
    yes = [('Quién y para qué', 'El usuario cambia su foto de perfil.'), ('Los pasos', '1. Elige la foto. 2. La ve en su perfil.'),
           ('Las reglas', 'La foto pesa máximo 5 MB.'), ('Los estados', 'Error: «No se pudo subir la foto».'),
           ('Criterios', 'Dado… cuando… entonces…'), ('Lo que falta', '¿Se puede quitar la foto?')]
    no = [('Código y widgets', 'Un ElevatedButton con setState.'), ('Tablas y SQL', 'UPDATE usuarios SET foto_url…'),
          ('Colores y tamaños', 'Botón azul de 48 px.'), ('Tareas', 'Crear ProfileService.'),
          ('Palabras vagas', 'Que sea rápido e intuitivo.'), ('Tecnología', 'Se sube a Supabase Storage.')]
    for col, (items, c, title) in enumerate(((yes, 'green', 'SÍ VA'), (no, 'rose', 'NO VA'))):
        x = 48 + col * 444
        soft, border, strong = FAM[c]
        o += txt(x, 124, title, 12.5, 700, strong)
        for i, (k, ex) in enumerate(items):
            yy = 138 + i * 48
            o += f'<rect x="{x}" y="{yy}" width="420" height="40" rx="10" fill="{soft}" stroke="{border}" stroke-width="1.2"/>'
            o += txt(x + 14, yy + 25, k, 13, 700, strong, fit=150)
            o += txt(x + 160, yy + 25, ex, 12.5, 400, BODY, fit=250)
    return o + end(fid, h, 'Lo de la derecha no se pierde: va al prototipo, al modelo de datos, a la spec técnica o al plan.')


@fig
def spVersiones():
    fid, h = 'spVersiones', 372
    o = start(fid, h, 'Versión y estado', 'Dos metadatos que dicen qué tan madura está la spec y si ya se construyó.',
              'Arriba, una versión 1.2.0 con sus tres números: mayor si cambia el comportamiento, menor si se '
              'agrega algo, parche si solo cambia la redacción. Abajo, los estados: borrador, aprobada e implementada, '
              'y obsoleta para la que ya no aplica.')
    o += txt(48, 128, 'VERSIÓN', 12, 700, MUTED)
    parts = [('1', 'Mayor', 'Cambia el comportamiento.', 'rose'), ('2', 'Menor', 'Se agrega algo.', 'amber'),
             ('0', 'Parche', 'Solo cambia la redacción.', 'slate')]
    for i, (n, name, what, c) in enumerate(parts):
        x = 48 + i * 296
        soft, border, strong = FAM[c]
        o += f'<rect x="{x}" y="140" width="272" height="76" rx="12" fill="{soft}" stroke="{border}" stroke-width="1.5"/>'
        o += txt(x + 34, 192, n, 34, 700, strong, 'middle', True)
        o += txt(x + 68, 170, name, 14.5, 700, strong, fit=196)
        o += txt(x + 68, 194, what, 12.5, 400, BODY, fit=196)
    o += txt(48, 252, 'ESTADO', 12, 700, MUTED)
    states = [('borrador', 'slate', '0.x.y'), ('aprobada', 'indigo', '1.0.0'), ('implementada', 'green', 'en el código')]
    for i, (s, c, note) in enumerate(states):
        x = 48 + i * 232
        o += pill(x + 80, 284, s, c, solid=True)
        o += txt(x + 80, 316, note, 12, 400, FAINT, 'middle')
        if i < 2:
            o += arrow(fid, f'M{x + 150},284 H{x + 238}')
    o += arrow(fid, 'M700,284 H756', dashed=True)
    o += pill(816, 284, 'obsoleta', 'rose')
    o += txt(816, 316, 'ya no aplica', 12, 400, FAINT, 'middle')
    return o + end(fid, h)


def tree(rows, x=72, y=136, step=30, tag_x=520):
    o = ''
    for depth, name, kind, tag in rows:
        ix = x + depth * 28
        yy = y
        if kind == 'dir':
            o += (f'<path d="M{ix},{yy - 9} h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" '
                  'stroke-linejoin="round"/>')
        else:
            o += f'<rect x="{ix + 2}" y="{yy - 11}" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/>'
        o += txt(ix + 28, yy + 4, name, 13.5, 700 if kind == 'dir' else 400, INK, mono=True)
        if tag:
            label, c = tag
            o += pill(tag_x + (width(label, 12) + 22) / 2, yy, label, c)
        y += step
    return o


@fig
def spCarpeta():
    fid, h = 'spCarpeta', 448
    o = start(fid, h, 'Dónde viven las specs', 'Todo en docs/, junto al código. El índice dice en qué va cada spec.',
              'Árbol de la carpeta docs con prd.md, requisitos.md, architectural_spine.md, modelo.md y la carpeta '
              'specs con README.md, tres specs F-01 a F-03 y reporte.md, cada uno con lo que es.')
    rows = [(0, 'docs/', 'dir', None), (1, 'prd.md', 'file', ('el problema y los objetivos', 'indigo')),
            (1, 'requisitos.md', 'file', ('RF y RNF numerados', 'indigo')),
            (1, 'architectural_spine.md', 'file', ('stack e invariantes', 'amber')),
            (1, 'modelo.md', 'file', ('las tablas, de la sesión 4', 'slate')),
            (1, 'specs/', 'dir', None), (2, 'README.md', 'file', ('el índice, con versión y estado', 'teal')),
            (2, 'F-01-registro.md', 'file', ('una spec por funcionalidad', 'teal')),
            (2, 'F-02-publicar.md', 'file', None), (2, 'F-03-foto-de-perfil.md', 'file', None),
            (2, 'reporte.md', 'file', ('las métricas de la crítica', 'rose'))]
    o += f'<rect x="48" y="112" width="864" height="{len(rows) * 26 + 24}" rx="12" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>'
    o += tree(rows, step=26)
    return o + end(fid, h)


# ───────────────────────────── S0071 · Métricas del conjunto de specs

@fig
def mtTraza():
    fid, h = 'mtTraza', 404
    o = start(fid, h, 'La traza: del objetivo al criterio', 'Cada documento cita al anterior. Un eslabón suelto es un problema.',
              'Una cadena de izquierda a derecha: el objetivo O-02 del PRD, los requisitos RF-07 y RF-08, la spec F-03 '
              'y sus criterios CA-1 y CA-2. Abajo, RF-09 sin ninguna spec, marcado en rojo porque baja la completitud.')
    cols = [(48, 'PRD', 'indigo'), (272, 'REQUISITOS', 'indigo'), (496, 'SPEC', 'teal'), (720, 'CRITERIOS', 'amber')]
    for x, t, c in cols:
        o += txt(x, 128, t, 12, 700, MUTED)
    o += box(48, 168, 192, 64, 'indigo', 'O-02', ['Mostrarse con su foto.'])
    o += box(272, 144, 192, 52, 'indigo', 'RF-07 · elegir foto', [], title_size=13.5)
    o += box(272, 208, 192, 52, 'indigo', 'RF-08 · límite 5 MB', [], title_size=13.5)
    o += box(496, 168, 192, 64, 'teal', 'F-03', ['Foto de perfil.'])
    o += box(720, 144, 192, 52, 'amber', 'CA-1 · la ve', [], title_size=13.5)
    o += box(720, 208, 192, 52, 'amber', 'CA-2 · aviso', [], title_size=13.5)
    for d in ('M240,200 C256,200 256,170 270,170', 'M240,200 C256,200 256,234 270,234',
              'M464,170 C480,170 480,200 494,200', 'M464,234 C480,234 480,200 494,200',
              'M688,200 C704,200 704,170 718,170', 'M688,200 C704,200 704,234 718,234'):
        o += arrow(fid, d)
    o += box(272, 292, 192, 52, 'rose', 'RF-09 · quitar foto', [], title_size=13.5)
    o += f'<path d="M464,318 H556" stroke="#C2354F" stroke-width="2" stroke-dasharray="5 5"/>'
    o += txt(566, 314, 'Ninguna spec lo cubre.', 13, 700, '#C2354F')
    o += txt(566, 334, 'La completitud queda en 8/9.', 12.5, 400, BODY)
    return o + end(fid, h)


@fig
def mtTablero():
    fid, h = 'mtTablero', 512
    o = start(fid, h, 'Diez métricas para el conjunto de specs', 'La skill sdd-critica las calcula y deja el reporte en docs/specs/reporte.md.',
              'Diez tarjetas en dos filas, cada una con el nombre de la métrica, qué cuenta y un valor de ejemplo con su '
              'color: completitud, trazabilidad, verificabilidad, ambigüedad, consistencia, atomicidad, pureza funcional, '
              'preguntas abiertas, avance y estabilidad.')
    ms = [('Completitud', ['RF con spec', '÷ RF totales'], '8/9', 'amber'),
          ('Trazabilidad', ['RF ↔ objetivo', 'spec ↔ RF'], '100 %', 'green'),
          ('Verificabilidad', ['criterios medibles', '÷ criterios'], '6/10', 'rose'),
          ('Ambigüedad', ['palabras vagas', 'meta: 0'], '2', 'amber'),
          ('Consistencia', ['contradicciones', 'meta: 0'], '0', 'green'),
          ('Atomicidad', ['specs con dos', 'funcionalidades'], '0', 'green'),
          ('Pureza funcional', ['specs que nombran', 'tecnología'], '1', 'amber'),
          ('Preguntas abiertas', ['deuda de spec', 'debe bajar'], '3', 'slate'),
          ('Avance', ['implementadas ÷', 'aprobadas'], '0/4', 'slate'),
          ('Estabilidad', ['cambios de versión', 'mayor por spec'], '0', 'green')]
    w, gap = 160, 16
    for i, (name, lines, val, c) in enumerate(ms):
        x = 48 + (i % 5) * (w + gap)
        y = 120 + (i // 5) * 176
        soft, border, strong = FAM[c]
        o += f'<rect x="{x}" y="{y}" width="{w}" height="160" rx="12" fill="#FFFFFF" stroke="{border}" stroke-width="1.5"/>'
        o += f'<rect x="{x}" y="{y}" width="{w}" height="6" rx="3" fill="{strong}"/>'
        o += txt(x + 14, y + 34, name, 13.5, 700, INK, fit=w - 20)
        o += txt(x + 14, y + 86, val, 28, 700, strong, fit=w - 20)
        for j, ln in enumerate(lines):
            o += txt(x + 14, y + 116 + j * 18, ln, 12, 400, MUTED, fit=w - 20)
    return o + end(fid, h, 'Verde: en la meta. Amarillo: cerca. Rojo: hay que corregir antes de implementar.')


# ───────────────────────────── S0072 · La arquitectura

@fig
def arServicios():
    fid, h = 'arServicios', 476
    o = start(fid, h, 'La app y los tres servicios de Supabase', 'Un solo SDK en la app; detrás, tres servicios con un trabajo cada uno.',
              'A la izquierda la app Flutter en tres capas: pantallas, servicios y el SDK supabase_flutter, con la '
              'publishable key. A la derecha Supabase con Auth para las cuentas, la base de datos con PostgREST para '
              'usuarios, publicaciones, seguidores y mensajes, y Storage para las fotos de perfil.')
    o += f'<rect x="48" y="112" width="340" height="320" rx="16" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>'
    o += txt(68, 142, 'App Flutter', 15, 700, INK)
    o += box(68, 160, 300, 72, 'indigo', 'Screens y Pages', ['Muestran y piden datos.'], title_size=13.5)
    o += arrow(fid, 'M218,232 V246')
    o += box(68, 248, 300, 72, 'violet', 'Servicios', ['Los únicos que hablan con Supabase.'], title_size=13.5)
    o += arrow(fid, 'M218,320 V334')
    o += box(68, 336, 300, 72, 'slate', 'supabase_flutter', ['Un solo SDK con los tres servicios.'], title_size=13.5, mono_title=True)
    o += pill(300, 356, 'publishable key', 'green')
    o += f'<rect x="508" y="112" width="404" height="320" rx="16" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>'
    o += txt(528, 142, 'Supabase', 15, 700, '#3A8235')
    svc = [('Auth', 'antes GoTrue', ['Cuentas: registro, inicio y', 'cierre de sesión. Da el uuid.'], 'amber'),
           ('Base de datos', 'Postgres + PostgREST', ['usuarios, publicaciones,', 'seguidores y mensajes.'], 'teal'),
           ('Storage', 'buckets de archivos', ['Las fotos de perfil.', 'La tabla guarda la ruta.'], 'rose')]
    for i, (n, sub, lines, c) in enumerate(svc):
        y = 160 + i * 88
        o += box(528, y, 364, 72, c, None, [])
        o += txt(544, y + 26, n, 14, 700, FAM[c][2])
        o += txt(544 + width(n, 14, False) + 18, y + 26, sub, 12, 400, FAINT, fit=200)
        for j, ln in enumerate(lines):
            o += txt(544, y + 46 + j * 17, ln, 12.5, 400, BODY, fit=340)
    o += arrow(fid, 'M368,380 C440,380 440,196 526,196')
    o += arrow(fid, 'M368,380 C440,380 440,284 526,284')
    o += arrow(fid, 'M368,380 C440,380 440,372 526,372')
    return o + end(fid, h, 'Sin backend propio: la app habla directo con Supabase. La secret key nunca va en la app.')


@fig
def arRecorrido():
    fid, h = 'arRecorrido', 470
    o = start(fid, h, 'Cuatro pedidos de la red profesional', 'Una fila por pedido. Cada uno pasa por la capa de servicios y llega a un servicio.',
              'Cuatro filas con tres columnas, pantalla, servicio y Supabase: iniciar sesión va a Auth y vuelve el '
              'uuid; ver el feed lee publicaciones por PostgREST; cambiar la foto sube el archivo a Storage y vuelve la '
              'ruta; guardar la ruta actualiza la fila del usuario por PostgREST.')
    heads = [(48, 'PANTALLA'), (360, 'SERVICIO'), (648, 'SUPABASE')]
    for x, t in heads:
        o += txt(x, 124, t, 12, 700, MUTED)
    rows = [('Iniciar sesión', 'AuthService', 'Auth', 'vuelve la sesión con el uuid', 'amber'),
            ('Ver el feed', 'PostService', 'PostgREST', 'vuelven las publicaciones', 'teal'),
            ('Cambiar la foto', 'ProfileService', 'Storage', 'vuelve la ruta del archivo', 'rose'),
            ('Guardar la ruta', 'ProfileService', 'PostgREST', 'foto_url en usuarios', 'teal')]
    for i, (screen, svc, dest, back, c) in enumerate(rows):
        y = 140 + i * 76
        o += box(48, y, 264, 56, 'indigo', None, [])
        o += txt(64, y + 34, screen, 14, 700, '#4453C9')
        o += box(360, y, 240, 56, 'violet', None, [])
        o += txt(376, y + 34, svc, 13.5, 700, '#7439B8', mono=True)
        o += box(648, y, 264, 56, c, None, [])
        o += txt(664, y + 25, dest, 14, 700, FAM[c][2])
        o += txt(664, y + 44, back, 12, 400, BODY, fit=240)
        o += arrow(fid, f'M312,{y + 28} H358')
        o += arrow(fid, f'M600,{y + 28} H646')
    return o + end(fid, h)


@fig
def arSpine():
    fid, h = 'arSpine', 420
    o = start(fid, h, 'Las partes de la architectural spine', 'Una o dos páginas. Lo central son las invariantes.',
              'Cinco bloques: resumen, diagrama, stack, invariantes y diferido. Las invariantes están resaltadas, con la '
              'pregunta que las define: si dos integrantes pueden decidirlo distinto y eso rompe la app, es una invariante.')
    parts = [('Resumen', ['Qué es la app, dónde', 'corre, con qué backend.'], 'slate'),
             ('Diagrama', ['Un flowchart de', 'mermaid.'], 'indigo'),
             ('Stack', ['Flutter, supabase_flutter', 'y los tres servicios.'], 'teal'),
             ('Diferido', ['Lo que no se decide', 'todavía.'], 'slate')]
    for i, (t, lines, c) in enumerate(parts):
        o += box(48, 116 + i * 70, 300, 60, c, None, [])
        o += txt(64, 140 + i * 70, t, 14, 700, FAM[c][2])
        o += txt(64, 160 + i * 70, ' '.join(lines), 12, 400, BODY, fit=276)
    o += f'<rect x="380" y="116" width="532" height="270" rx="14" fill="#FFF3DC" stroke="#F0C572" stroke-width="2"/>'
    o += txt(400, 148, 'Invariantes · AD-01, AD-02…', 15, 700, '#A96C05')
    o += txt(400, 176, '¿Dos integrantes podrían decidirlo distinto, y eso rompería la app?', 13, 600, INK, fit=500)
    o += txt(400, 196, 'Si sí, se fija aquí con una Regla y lo que Evita.', 13, 400, BODY, fit=500)
    o += box(400, 216, 492, 72, 'amber', 'AD-03 · El usuario es el de Auth', ['Regla: toda fila de alguien guarda el uuid de Auth.'],
             fill='#FFFFFF', title_size=13.5, size=12.5)
    o += box(400, 298, 492, 72, 'amber', 'AD-04 · Los archivos van en Storage', ['Regla: la tabla guarda solo la ruta del archivo.'],
             fill='#FFFFFF', title_size=13.5, size=12.5)
    return o + end(fid, h)


# ───────────────────────────── S0073 y S0074 · Talleres

STEPS = [('1', 'Contexto', ['«Actualiza', 'AGENTS.md»'], 'AGENTS.md', ['El agente sabe', 'de qué va la app'], 'slate'),
         ('2', 'PRD', ['«Mi proyecto se', 'trata de…»'], 'docs/prd.md', ['Un problema y', 'objetivos medibles'], 'indigo'),
         ('3', 'Requisitos', ['«Crea los', 'requerimientos»'], 'docs/requisitos.md', ['Una lista que', 'se puede comprobar'], 'indigo'),
         ('4', 'Spine', ['«…especifica la', 'arquitectura»'], 'architectural_spine.md', ['Reglas que nadie', 'decide distinto'], 'amber'),
         ('5', 'Specs', ['«Crea las specs', 'funcionales»'], 'docs/specs/', ['Un contrato por', 'funcionalidad'], 'teal')]


def crece(fid, on, title, sub):
    h = 360
    o = start(fid, h, title, sub,
              'Cinco columnas en orden: contexto, PRD, requisitos, spine y specs. Cada una con el pedido al agente, el '
              'archivo que deja y el valor que agrega. Las de este taller están resaltadas; las otras, atenuadas.')
    ws, gap = [152, 160, 168, 196, 156], 8
    for i, (n, name, prompt, path, value, c) in enumerate(STEPS):
        w = ws[i]
        x = 48 + sum(ws[:i]) + i * gap
        faded = i not in on
        soft, border, strong = FAM[c]
        op = ' opacity=".4"' if faded else ''
        o += f'<g{op}><rect x="{x}" y="116" width="{w}" height="196" rx="12" fill="{soft}" stroke="{border}" stroke-width="1.5"/>'
        o += (f'<circle cx="{x + 26}" cy="142" r="13" fill="#FFFFFF" stroke="{strong}" stroke-width="2"/>'
              + txt(x + 26, 146.5, n, 13, 700, strong, 'middle'))
        o += txt(x + 48, 147, name, 14.5, 700, strong, fit=w - 54)
        for j, ln in enumerate(prompt):
            o += txt(x + 12, 178 + j * 17, ln, 12, 600, INK, fit=w - 16)
        o += f'<rect x="{x + 8}" y="208" width="{w - 16}" height="32" rx="8" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.2"/>'
        o += txt(x + w / 2, 229, path, 12, 700, INK, 'middle', True, fit=w - 18)
        o += txt(x + 12, 264, 'Agrega:', 12, 700, MUTED)
        for j, ln in enumerate(value):
            o += txt(x + 12, 282 + j * 17, ln, 12, 400, BODY, fit=w - 16)
        o += '</g>'
        if i < 4:
            o += arrow(fid, f'M{x + w + 1},214 H{x + w + gap - 1}')
    return o + end(fid, h, 'Cada paso lee lo que dejaron los anteriores: por eso el orden importa.')


@fig
def taCrece():
    return crece('taCrece', {0, 1, 2}, 'El proyecto se va formando · pasos 1 a 3',
                 'En este taller: el contexto, el PRD y los requisitos.')


@fig
def tcCrece():
    return crece('tcCrece', {3, 4}, 'El proyecto se va formando · pasos 4 y 5',
                 'En este taller: la spine y las specs funcionales, sobre lo que ya tienes.')


def bubble(x, y, w, lines, who):
    user = who == 'user'
    fill, stroke, color = ('#EEF1FF', '#A9B4F2', '#4453C9') if user else ('#FFFFFF', LINE, MUTED)
    hh = 36 + 19 * len(lines)
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{hh}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
    o += txt(x + 16, y + 22, 'Tú' if user else 'Agente · sdd-prd', 12, 700, color)
    for i, ln in enumerate(lines):
        o += txt(x + 16, y + 44 + i * 19, ln, 13, 400, INK, fit=w - 24)
    return o, hh


@fig
def taEntrevista():
    fid, h = 'taEntrevista', 540
    o = start(fid, h, 'La skill entrevista antes de escribir', 'Tú cuentas la idea; ella pregunta lo que falta y deja docs/prd.md.',
              'Una conversación: el estudiante cuenta que su proyecto es una red profesional; la skill repite lo que '
              'entendió y hace la ronda 1 de preguntas sobre el problema; el estudiante responde; la skill escribe '
              'docs/prd.md en la versión 0.1.0 con tres objetivos y dos preguntas abiertas.')
    y = 112
    turns = [(48, 560, ['Mi proyecto se trata de una red profesional para', 'estudiantes de Icesi: perfil, publicaciones y mensajes.'], 'user'),
             (352, 560, ['Entiendo: una red para mostrarse y conversar.', 'Ronda 1 · ¿Qué problema resuelve? ¿Cómo lo', 'resuelven hoy? ¿Qué les molesta de eso?'], 'agent'),
             (48, 560, ['Hoy usan LinkedIn, pero ahí no encuentran', 'a otros estudiantes de su carrera.'], 'user'),
             (352, 560, ['Escribí docs/prd.md · v0.1.0 · borrador.', '3 objetivos · 2 preguntas abiertas.', 'Sigue con sdd-requisitos.'], 'agent')]
    for x, w, lines, who in turns:
        b, hh = bubble(x, y, w, lines, who)
        o += b
        y += hh + 14
    return o + end(fid, h, 'Si una respuesta es vaga («que sea fácil»), la skill pide un ejemplo o un número.')


@fig
def tcCritica():
    fid, h = 'tcCritica', 340
    o = start(fid, h, 'Criticar, corregir y subir la versión', 'La crítica no cambia nada sola: propone, tú decides y la versión sube.',
              'Tres columnas: el primer reporte con verificabilidad 6 de 10 y ambigüedad 2; las correcciones aplicadas a '
              'F-02 y F-03; y el segundo reporte con verificabilidad 10 de 10, ambigüedad 0 y las specs en la versión 0.2.0.')
    o += box(48, 116, 264, 184, 'rose', 'Reporte 1', ['Verificabilidad: 6/10', 'Ambigüedad: 2', 'F-02 dice «rápido»', 'F-03, CA-2: «se ve bien»', '', 'specs en 0.1.0'])
    o += arrow(fid, 'M312,208 H346')
    o += box(348, 116, 264, 184, 'amber', 'Corregir', ['Tú aceptas los cambios.', 'F-02: «en menos de 2 s».', 'F-03, CA-2: aviso si pesa', 'más de 5 MB.', '', 'Historial: 0.2.0'])
    o += arrow(fid, 'M612,208 H646')
    o += box(648, 116, 264, 184, 'green', 'Reporte 2', ['Verificabilidad: 10/10', 'Ambigüedad: 0', '', '', '', 'specs en 0.2.0'])
    return o + end(fid, h)


@fig
def tcSiguiente():
    fid, h = 'tcSiguiente', 300
    o = start(fid, h, 'Por qué todavía no se implementa', 'Las specs dicen qué. Para el código falta decir cómo, con las reglas del curso.',
              'Tres bloques: lo que ya está, PRD, requisitos, spine y specs; lo que falta, la spec técnica y una skill de '
              'implementación que conozca las convenciones del front; y después el código.')
    o += box(48, 116, 264, 140, 'green', 'Ya está', ['PRD y requisitos', 'Architectural spine', 'Specs funcionales v0.2.0'])
    o += arrow(fid, 'M312,186 H346')
    o += box(348, 116, 264, 140, 'amber', 'Falta', ['La spec técnica', 'Una skill que conozca el front:', 'Screens y Pages, setState,', 'components/, imports package:'], dashed=True)
    o += arrow(fid, 'M612,186 H646', dashed=True)
    o += box(648, 116, 264, 140, 'slate', 'Después', ['El código, pedido spec', 'por spec.'], faded=True, dashed=True)
    return o + end(fid, h)


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
