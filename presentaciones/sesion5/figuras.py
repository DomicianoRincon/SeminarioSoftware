#!/usr/bin/env python3
"""Copia las figuras SVG de las lecciones de la Sesión 5 al deck.

Lee las lecciones de SeminarioSoftware/content/ y escribe slides/00-figuras.js con
window.FIG = { <id>: '<svg ...>' }. A todas se les recorta el título propio (la slide ya
dice de qué va); al código anotado (mcpConfiguracion) se le deja solo el editor y el panel.

Uso:  python3 figuras.py   (desde cualquier carpeta)
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]                   # SeminarioSoftware
CONTENT = REPO / 'content'

LESSONS = [f'lessonS{n}.md' for n in (34, 35, 36, 37, 39)]

FRAMES = ['mcpConfiguracion']
PLAIN = ['mcpArquitectura', 'mcpTriada', 'stCapacidades', 'stFlujo', 'pwCapacidades', 'pwFlujo',
         'ghCapacidades', 'ghFlujo']

MAX_W, MAX_H = 1216, 430      # área de contenido de slideStandard
WIDE_W, WIDE_H = 1100, 400    # una figura más ancha que WIDE_W llega al número de slide: baja a WIDE_H
CROP_TOP = 96                 # quita el título y la bajada
# Las de capacidades se muestran sin el recuadro de abajo (va en las notas), para que las
# cuatro tarjetas queden más grandes.
CROPS = {k: (40, 104, 880, 440) for k in ('stCapacidades', 'pwCapacidades', 'ghCapacidades')}


def all_svgs():
    found = {}
    for name in LESSONS:
        text = (CONTENT / name).read_text(encoding='utf-8')
        for m in re.finditer(r'```svg\n(<svg id="(\w+)".*?</svg>)\n```', text, re.S):
            found[m.group(2)] = m.group(1)
    return found


def resize(svg, box, max_w=MAX_W, max_h=MAX_H):
    x, y, w, h = box
    s = min(max_w / w, max_h / h)
    if w * s > WIDE_W:
        s = min(s, WIDE_H / h)
    svg = re.sub(r'viewBox="[^"]+"', f'viewBox="{x} {y} {w} {h}"', svg, count=1)
    svg = svg.replace(' width="100%"', f' width="{w*s:.0f}" height="{h*s:.0f}"', 1)
    svg = svg.replace('style="max-width:960px;display:block;margin:0 auto"',
                      'style="display:block;margin:0 auto"', 1)
    return svg.replace('#FBFBFD', '#FFFFFF')


def frame_box(svg):
    h = float(re.search(r'<rect x="48" y="112" width="456" height="([\d.]+)" rx="12" fill="#1F2430"/>', svg).group(1))
    return (40, 104, 880, h + 16)


def plain_box(key, svg):
    if key in CROPS:
        return CROPS[key]
    full = float(re.search(r'viewBox="0 0 960 ([\d.]+)"', svg).group(1))
    return (0, CROP_TOP, 960, full - CROP_TOP)


def main():
    svgs = all_svgs()
    fig = {}
    for k in FRAMES:
        fig[k] = resize(svgs[k], frame_box(svgs[k]))
    for k in PLAIN:
        fig[k] = resize(svgs[k], plain_box(k, svgs[k]))
    out = HERE / 'slides' / '00-figuras.js'
    body = ',\n'.join(f'  {k}: {json.dumps(v, ensure_ascii=False)}' for k, v in fig.items())
    out.write_text('// Generado por figuras.py a partir de las lecciones. No editar a mano.\n'
                   'window.FIG = {\n' + body + '\n};\n', encoding='utf-8')
    for k, v in fig.items():
        w, h = re.search(r'width="(\d+)" height="(\d+)"', v).groups()
        print(f'{k:18s} {w}x{h}')


if __name__ == '__main__':
    main()
