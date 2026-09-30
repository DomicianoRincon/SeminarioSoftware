#!/usr/bin/env python3
"""Copia las figuras SVG de las lecciones de la Sesión 1 al deck.

Lee las lecciones de SeminarioSoftware/content/ y escribe slides/00-figuras.js con
window.FIG = { <id>: '<svg ...>' }. Dos ajustes por figura:

- Figuras normales: se recorta el título propio (la slide ya lo pone) y se escala al área de
  contenido de slideStandard, con width y height explícitos.
- Figuras de consola: se recorta a la ventana de la terminal; las tarjetas que la explican van
  como texto en la slide, a la derecha.

Uso:  python3 figuras.py   (desde cualquier carpeta)
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTENT = HERE.parents[1] / 'content'   # SeminarioSoftware/content
LESSONS = ['lessonS3.md', 'lessonS4.md', 'lessonS5.md', 'lessonS6.md', 'lessonS1.md']

NORMAL = ['feLados', 'feEstados', 'feLugares', 'pfNativo', 'fnServicios', 'fnEjemplo',
          'iaManos', 'iaTools', 'iaMando', 'fiPiezas', 'fiPasos']
CONSOLE = ['iaAgente', 'tcVersion', 'tcCreate', 'tcDevices', 'tcRun']

MAX_W, MAX_H = 1216, 400      # área de contenido de slideStandard, sin tocar el número de slide
CONSOLE_W = 760               # la terminal deja ~420 px a la derecha para la explicación
CROP_TOP = 64                 # quita el título (y=56); conserva la bajada (y=80)


def all_svgs():
    found = {}
    for name in LESSONS:
        text = (CONTENT / name).read_text(encoding='utf-8')
        for m in re.finditer(r'<svg id="(\w+)".*?</svg>', text, re.S):
            found[m.group(1)] = m.group(0)
    return found


def resize(svg, vb, w, h):
    svg = re.sub(r'viewBox="[^"]+"', f'viewBox="{vb}"', svg, count=1)
    svg = svg.replace(' width="100%"', f' width="{w:.0f}" height="{h:.0f}"', 1)
    svg = svg.replace('style="max-width:960px;display:block;margin:0 auto"',
                      'style="display:block;margin:0 auto"', 1)
    # El fondo de la lección (#FBFBFD) se vuelve blanco: en la slide la figura no es una tarjeta.
    svg = re.sub(r'(<rect width="960" height="\d+" rx="16" fill=")#FBFBFD(")', r'\1#FFFFFF\2', svg, count=1)
    return svg


# Figuras que no caben bien con el recorte general: (y inicial, y final, alto máximo).
# fiPasos: se quitan la bajada y la leyenda (van a las notas) para que la letra no quede chica.
OVERRIDES = {'fiPasos': (96, 576, 440)}


def normal(key, svg):
    full_h = float(re.search(r'viewBox="0 0 960 (\d+)"', svg).group(1))
    top, bottom, max_h = OVERRIDES.get(key, (CROP_TOP, full_h, MAX_H))
    h = bottom - top
    s = min(MAX_W / 960, max_h / h)
    return resize(svg, f'0 {top} 960 {h:.0f}', 960 * s, h * s)


def console(svg):
    m = re.search(r'<rect x="48" y="112" width="864" height="(\d+)" rx="12" fill="#1F2430"/>', svg)
    th = float(m.group(1))
    s = min(CONSOLE_W / 864, MAX_H / th)
    return resize(svg, f'48 112 864 {th:.0f}', 864 * s, th * s)


def main():
    svgs = all_svgs()
    fig = {}
    for k in NORMAL:
        fig[k] = normal(k, svgs[k])
    for k in CONSOLE:
        fig[k] = console(svgs[k])
    out = HERE / 'slides' / '00-figuras.js'
    body = ',\n'.join(f'  {k}: {json.dumps(v, ensure_ascii=False)}' for k, v in fig.items())
    out.write_text('// Generado por figuras.py a partir de las lecciones. No editar a mano.\n'
                   'window.FIG = {\n' + body + '\n};\n', encoding='utf-8')
    for k, v in fig.items():
        w, h = re.search(r'width="(\d+)" height="(\d+)"', v).groups()
        print(f'{k:12s} {w}x{h}')


if __name__ == '__main__':
    main()
