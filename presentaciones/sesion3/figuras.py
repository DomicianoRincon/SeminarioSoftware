#!/usr/bin/env python3
"""Copia las figuras SVG de las lecciones de la Sesión 3 al deck.

Lee las lecciones de SeminarioSoftware/content/ y escribe slides/00-figuras.js con
window.FIG = { <id>: '<svg ...>' }. Ajustes por tipo de figura:

- Código anotado (FRAMES): se recorta al editor y al panel de resultado. El título lo pone la
  slide y las tarjetas de abajo, si las hay, van en las notas de orador.
- Las demás (PLAIN): se recorta el título propio. CROPS da el recorte de las que necesitan otro.
- tpPantallas (PHONE): solo el celular; los cuatro bloques los lista la slide al lado.
- bnCodigo no se copia: con 21 líneas queda ilegible, así que se arma una versión de 14
  (solo la barra, con icon y label en un renglón) con el generador de las lecciones.

Uso:  python3 figuras.py   (desde cualquier carpeta)
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]                   # SeminarioSoftware
CONTENT = REPO / 'content'
sys.path.insert(0, str(REPO / 'tools'))
from code_frame import frame                    # noqa: E402
from sesion3_figuras import bn_codigo_result     # noqa: E402

LESSONS = [f'lessonS{n}.md' for n in (20, 21, 28, 27, 22, 23, 24, 25, 26)]

FRAMES = ['sfPartes', 'saCodigo', 'cpPadding', 'cpContainer', 'exCodigo', 'scCodigo',
          'apEstructura', 'apRutas']
PLAIN = ['sfSinScaffold', 'sfScreen', 'saZonas', 'saCasos', 'abPartes', 'abVariantes', 'cpInsets',
         'cpCaja', 'exSobra', 'exFlex', 'scVentana', 'scHorizontal', 'apCapas', 'tpCarpetas',
         'tpBloque1', 'tpBloque2', 'tpBloque3', 'tpBloque4']

MAX_W, MAX_H = 1216, 430      # área de contenido de slideStandard
WIDE_W, WIDE_H = 1100, 400    # una figura más ancha que WIDE_W llega al número de slide: baja a WIDE_H
CROP_TOP = 96                 # quita el título y la bajada: la slide ya dice de qué va
# Recortes propios: (x, y, ancho, alto) del viewBox.
CROPS = {}
PHONE_BOX = (292, 106, 376, 712)
PHONE_H = 452


BN = dict(
    id='bnCodigo', title='bottomNavigationBar', title_plain='Tres botones en bottomNavigationBar',
    desc='Un BottomNavigationBar con tres BottomNavigationBarItem: Inicio, Chats y Perfil. En el resultado, la barra queda pegada al borde de abajo con los tres botones repartidos a lo ancho, y el primero aparece resaltado.',
    sub='', file='lib/screens/home_screen.dart', panel='RESULTADO',
    code=[
        "bottomNavigationBar: BottomNavigationBar(",
        "  currentIndex: 0,",
        "  items: const [",
        "    BottomNavigationBarItem(",
        "      icon: Icon(Icons.home), label: 'Inicio',",
        "    ),",
        "    BottomNavigationBarItem(",
        "      icon: Icon(Icons.chat), label: 'Chats',",
        "    ),",
        "    BottomNavigationBarItem(",
        "      icon: Icon(Icons.person), label: 'Perfil',",
        "    ),",
        "  ],",
        "),",
    ],
    result=bn_codigo_result(16, 332),
    arrows=[dict(line=0, find='bottomNavigationBar', to=(84, 318), color='amber', lane=1)],
)


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
    # El fondo de la lección (#FBFBFD) se vuelve blanco, también en los degradados y parches que
    # lo usan para tapar: en la slide la figura no es una tarjeta.
    svg = svg.replace('#FBFBFD', '#FFFFFF')
    return svg


def frame_box(svg):
    h = float(re.search(r'<rect x="48" y="112" width="456" height="(\d+)" rx="12" fill="#1F2430"/>', svg).group(1))
    return (40, 104, 880, h + 16)


def plain_box(key, svg):
    if key in CROPS:
        return CROPS[key]
    full = float(re.search(r'viewBox="0 0 960 ([\d.]+)"', svg).group(1))
    return (0, CROP_TOP, 960, full - CROP_TOP)


def main():
    svgs = all_svgs()
    fig = {}
    bn = frame(BN)
    fig['bnCodigo'] = resize(bn, frame_box(bn))
    for k in FRAMES:
        fig[k] = resize(svgs[k], CROPS.get(k) or frame_box(svgs[k]))
    for k in PLAIN:
        fig[k] = resize(svgs[k], plain_box(k, svgs[k]))
    fig['tpPantallas'] = resize(svgs['tpPantallas'], PHONE_BOX, max_h=PHONE_H)
    out = HERE / 'slides' / '00-figuras.js'
    body = ',\n'.join(f'  {k}: {json.dumps(v, ensure_ascii=False)}' for k, v in fig.items())
    out.write_text('// Generado por figuras.py a partir de las lecciones. No editar a mano.\n'
                   'window.FIG = {\n' + body + '\n};\n', encoding='utf-8')
    for k, v in fig.items():
        w, h = re.search(r'width="(\d+)" height="(\d+)"', v).groups()
        print(f'{k:14s} {w}x{h}  escala {int(w) / float(re.search(r"viewBox=.[-\d.]+ [-\d.]+ ([\d.]+)", v).group(1)):.2f}')


if __name__ == '__main__':
    main()
