#!/usr/bin/env python3
"""Copia las figuras SVG de las lecciones de la Sesión 2 al deck.

Lee las lecciones de SeminarioSoftware/content/ y escribe slides/00-figuras.js con
window.FIG = { <id>: '<svg ...>' }. Ajustes por tipo de figura:

- Código anotado (FRAMES): se recorta al editor y al panel de resultado. El título lo pone la
  slide y las tarjetas de abajo van en las notas de orador.
- Las demás (PLAIN): se recorta el título propio. CROPS da el recorte de las que necesitan otro,
  sean de un tipo o del otro.
- Celular de perfil (PHONES): solo el celular; a swPiezas se le quitan las guías y los
  nombres, que la slide pone como tarjetas a los lados.
- tlTodos se vuelve a generar en tres columnas (en la lección va en dos), con el generador
  de las lecciones, tools/sesion2_figuras.py.
- ppMain no se copia: entera queda ilegible, así que se arma en dos mitades (ppMainA y
  ppMainB) con el mismo generador de las lecciones, tools/code_frame.py.

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
from code_frame import frame             # noqa: E402
from sesion2_figuras import note, tl_todos   # noqa: E402

LESSONS = [f'lessonS{n}.md' for n in (10, 11, 12, 13, 14, 16, 17, 15, 18)]

FRAMES = ['ppScaffold', 'txAnatomia', 'txLargo', 'imNetwork', 'btAnatomia', 'tfAnatomia', 'tfTipos',
          'clAnatomia', 'rwAnatomia', 'swAnatomia', 'swUso']
PLAIN = ['ppCarpetas', 'imAsset', 'imFit', 'btTipos', 'clAlineacion', 'rwAlineacion',
         'swRepetido', 'tlBoton', 'tlStats', 'tlContacto']
PHONES = ['swPantalla', 'swPiezas']

MAX_W, MAX_H = 1216, 430      # área de contenido de slideStandard
WIDE_W, WIDE_H = 1100, 400    # una figura más ancha que WIDE_W llega al número de slide: baja a WIDE_H
CROP_TOP = 96                 # quita el título y la bajada: la slide ya dice de qué va
# Recortes propios: (x, y, ancho, alto) del viewBox.
CROPS = {
    'ppCarpetas': (32, 96, 896, 480),      # sin la nota del pie, que va en las notas de orador
    'clAlineacion': (40, 100, 880, 496),   # las dos filas de cajas, sin la nota del pie
    'rwAlineacion': (40, 100, 880, 396),
    # Hasta la firma de build: el cuerpo, que solo devuelve una Column, va en las notas.
    'swAnatomia': (40, 104, 880, 368),
}
PHONE_BOX = (292, 106, 376, 712)
PHONE_H = 452


def all_svgs():
    found = {}
    for name in LESSONS:
        text = (CONTENT / name).read_text(encoding='utf-8')
        for m in re.finditer(r'<svg id="(\w+)".*?</svg>', text, re.S):
            found[m.group(1)] = m.group(0)
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
    # 'assets/…' es código mostrado en la figura; con la entidad, build.py no lo toma por una imagen.
    svg = svg.replace('assets/', 'assets&#47;')
    # El fondo de la lección (#FBFBFD) se vuelve blanco: en la slide la figura no es una tarjeta.
    svg = re.sub(r'(<rect width="960" height="\d+" rx="16" fill=")#FBFBFD(")', r'\1#FFFFFF\2', svg, count=1)
    return svg


def frame_box(svg):
    h = float(re.search(r'<rect x="48" y="112" width="456" height="(\d+)" rx="12" fill="#1F2430"/>', svg).group(1))
    return (40, 104, 880, h + 16)


def plain_box(key, svg):
    if key in CROPS:
        return CROPS[key]
    full = float(re.search(r'viewBox="0 0 960 (\d+)"', svg).group(1))
    return (0, CROP_TOP, 960, full - CROP_TOP)


def phone(key, svg):
    if key == 'swPiezas':
        svg = re.sub(r'  <path d="[^"]+" fill="none" stroke="#[0-9A-F]{6}" stroke-width="2"/>\n', '', svg)
        svg = re.sub(r'  <circle cx="[\d.]+" cy="[\d.]+" r="3\.5" fill="#[0-9A-F]{6}"/>\n', '', svg)
        svg = re.sub(r'  <g transform="translate\((?:700|56),\d+\)">.*?  </g>\n', '', svg, flags=re.S)
    return resize(svg, PHONE_BOX, max_h=PHONE_H)


MAIN_A = dict(
    id='ppMainA', title='main.dart', title_plain='main.dart: el arranque',
    desc='La primera mitad de main.dart: el import, la función main que llama a runApp y la clase App.',
    sub='', file='lib/main.dart', panel='QUÉ HACE CADA PARTE', min_h=384,
    code=[
        "import 'package:flutter/material.dart';",
        "",
        "void main() {",
        "  runApp(const App());",
        "}",
        "",
        "class App extends StatelessWidget {",
        "  const App({super.key});",
    ],
    result=(note(16, 'slate', 'import', ['Trae código de otros archivos. Este trae', 'los widgets de Flutter.'], 68)
            + note(96, 'amber', 'main()', ['La primera función que se ejecuta.', 'Es la puerta de entrada de la app.'], 68)
            + note(176, 'green', 'runApp(...)', ['Recibe el widget raíz y lo pone en pantalla.', 'Todo lo demás cuelga de él.'], 68)
            + note(256, 'indigo', 'App', ['El widget raíz. Lo escribes tú, como', 'cualquier otro componente.'], 68)),
    arrows=[
        dict(line=0, find='import', to=(16, 50), color='teal'),
        dict(line=2, find='main()', to=(16, 130), color='amber', lane=3),
        dict(line=3, find='runApp(const App())', to=(16, 210), color='green', lane=2),
        dict(line=6, find='App', to=(16, 276), color='indigo', lane=1),
    ],
)

MAIN_B = dict(
    id='ppMainB', title='main.dart', title_plain='main.dart: MaterialApp',
    desc='La segunda mitad de main.dart: el método build de App, que devuelve un MaterialApp con título, tema, ruta inicial y tabla de rutas.',
    sub='', file='lib/main.dart', panel='QUÉ HACE CADA PARTE',
    code=[
        "  @override",
        "  Widget build(BuildContext context) {",
        "    return MaterialApp(",
        "      title: 'Mi app',",
        "      theme: ThemeData(",
        "        colorScheme: ColorScheme.fromSeed(",
        "          seedColor: Colors.deepPurple,",
        "        ),",
        "      ),",
        "      initialRoute: '/home',",
        "      routes: {",
        "        '/home': (context) => const Text(\"Pantalla\"),",
        "      },",
        "    );",
        "  }",
        "}",
    ],
    result=(note(37, 'violet', 'MaterialApp', ['Configura toda la app: título, tema', 'y pantallas.'], 68)
            + note(133, 'teal', 'theme', ['Los colores de toda la app salen', 'de un solo color.'], 68)
            + note(229, 'rose', 'routes e initialRoute', ['La tabla de pantallas, cada una con su', 'nombre, y por cuál se empieza.'], 68)),
    arrows=[
        dict(line=2, find='MaterialApp', to=(16, 71), color='violet'),
        dict(line=4, find='theme', to=(16, 167), color='teal', lane=1),
        dict(line=10, find='routes', to=(16, 263), color='rose'),
    ],
)


def main():
    svgs = all_svgs()
    fig = {}
    for spec in (MAIN_A, MAIN_B):
        svg = frame(spec)
        fig[spec['id']] = resize(svg, frame_box(svg))
    for k in FRAMES:
        fig[k] = resize(svgs[k], CROPS.get(k) or frame_box(svgs[k]))
    for k in PLAIN:
        fig[k] = resize(svgs[k], plain_box(k, svgs[k]))
    for k in PHONES:
        fig[k] = phone(k, svgs[k])
    # Los seis componentes del taller, en tres columnas para que quepan a lo ancho de la slide.
    fig['tlTodos'] = resize(tl_todos(cols=3), (40, 104, 1324, 368))
    out = HERE / 'slides' / '00-figuras.js'
    body = ',\n'.join(f'  {k}: {json.dumps(v, ensure_ascii=False)}' for k, v in fig.items())
    out.write_text('// Generado por figuras.py a partir de las lecciones. No editar a mano.\n'
                   'window.FIG = {\n' + body + '\n};\n', encoding='utf-8')
    for k, v in fig.items():
        w, h = re.search(r'width="(\d+)" height="(\d+)"', v).groups()
        print(f'{k:14s} {w}x{h}  escala {int(w) / float(re.search(r"viewBox=.[-\d.]+ [-\d.]+ ([\d.]+)", v).group(1)):.2f}')


if __name__ == '__main__':
    main()
