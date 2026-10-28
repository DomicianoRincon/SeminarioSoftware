"""Figuras SVG de la sección IA (S0063, Skills para tu proyecto).

    python3 tools/ia_figuras.py <carpeta>     escribe un .svg por figura, para revisarlas
    python3 tools/ia_figuras.py --inject      reemplaza cada bloque ```svg de esas lecciones
                                              por la figura con el mismo id
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LESSONS = ['lessonS63.md']

FONT = "ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif"

COLORS = {
    'blue': ('#EEF1FF', '#A9B4F2', '#4453C9'),
    'green': ('#E3F6F3', '#86D3CA', '#0F8478'),
    'amber': ('#FFF3DC', '#F0C572', '#A96C05'),
    'purple': ('#F4EBFF', '#C9A6EE', '#7439B8'),
}


def card(fid, x, y, color, name, lines):
    fill, stroke, strong = COLORS[color]
    out = [f'<rect x="{x}" y="{y}" width="200" height="100" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>',
           f'<text class="mono" x="{x + 16}" y="{y + 30}" font-size="15" font-weight="700" fill="{strong}">{name}</text>']
    for i, line in enumerate(lines):
        out.append(f'<text class="nb" x="{x + 16}" y="{y + 56 + 20 * i}">{line}</text>')
    return out


def chip(fid, x, y, path, note):
    return [f'<rect x="{x}" y="{y + 30}" width="160" height="40" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>',
            f'<text class="mono" x="{x + 80}" y="{y + 50}" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" text-anchor="middle">{path}</text>',
            f'<text class="lbl" x="{x + 80}" y="{y + 90}" text-anchor="middle">{note}</text>']


def arrow(fid, x1, x2, y):
    return [f'<path class="link" d="M{x1},{y} H{x2 - 2}"/>']


def lane(fid, y, label, items):
    out = [f'<text class="h" x="48" y="{y - 12}">{label}</text>']
    (c1, n1, l1), (p1, d1), (c2, n2, l2), (p2, d2) = items
    out += card(fid, 48, y, c1, n1, l1)
    out += arrow(fid, 248, 296, y + 50)
    out += chip(fid, 296, y, p1, d1)
    out += arrow(fid, 456, 504, y + 50)
    out += card(fid, 504, y, c2, n2, l2)
    out += arrow(fid, 704, 752, y + 50)
    out += chip(fid, 752, y, p2, d2)
    return out


def mapa():
    fid = 'iaSkillsMapa'
    h = 492
    body = []
    body += lane(fid, 140, 'LA BASE DE DATOS · TRABAJAN SOBRE docs/', [
        ('blue', 'disenador-bd', ['Te entrevista y lleva', 'el modelo hasta 3FN.']),
        ('docs/modelo.md', 'las tablas, en 3FN'),
        ('green', 'mer-svg', ['Dibuja el modelo como', 'diagrama en SVG.']),
        ('docs/mer.svg', 'el diagrama MER'),
    ])
    body += lane(fid, 312, 'LA APP · TRABAJAN SOBRE lib/', [
        ('amber', 'flutter-pantallas', ['Maqueta pantallas', 'estáticas.']),
        ('lib/screens/', 'el prototipo'),
        ('purple', 'flutter-componentes', ['Datos, eventos y', 'estado en la Screen.']),
        ('lib/components/', 'con estado y eventos'),
    ])
    return f'''<svg id="{fid}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 {h}" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="{fid}-ttl {fid}-dsc" font-family="{FONT}">
  <title id="{fid}-ttl">Las cuatro skills y lo que deja cada una</title>
  <desc id="{fid}-dsc">Dos filas. Arriba, la base de datos: disenador-bd te entrevista y deja docs/modelo.md en tercera forma normal; mer-svg lo lee y dibuja docs/mer.svg. Abajo, la app: flutter-pantallas maqueta pantallas estáticas en lib/screens/, y flutter-componentes crea componentes con datos, eventos y el estado en la Screen, en lib/components/.</desc>
  <defs>
    <style>
      #{fid} .title{{fill:#161A26;font-size:22px;font-weight:700}}
      #{fid} .sub{{fill:#79809A;font-size:13.5px}}
      #{fid} .h{{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}}
      #{fid} .nb{{fill:#454C61;font-size:13px}}
      #{fid} .lbl{{fill:#556074;font-size:12px;font-weight:600}}
      #{fid} .foot{{fill:#79809A;font-size:12px}}
      #{fid} .mono{{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}}
      #{fid} .link{{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#{fid}-arrow)}}
    </style>
    <marker id="{fid}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="{h}" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las cuatro skills y lo que deja cada una</text>
  <text class="sub" x="48" y="80">Cada fila va en orden: lo que deja la primera skill es lo que usa la segunda.</text>
  {chr(10).join('  ' + line for line in body).strip()}
  <text class="foot" x="48" y="{h - 28}">Cada skill es una carpeta en .agents/skills/ del proyecto. El agente la carga cuando tu pedido coincide con su description.</text>
</svg>
'''


FIGS = {'iaSkillsMapa': mapa}


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--inject':
        done = set()
        for name in LESSONS:
            path = ROOT / 'content' / name
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
    for fid, fn in FIGS.items():
        (out / f'{fid}.svg').write_text(fn(), encoding='utf-8')
    print(len(FIGS), 'figuras en', out)


if __name__ == '__main__':
    main()
