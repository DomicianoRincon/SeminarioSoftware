"""Genera los frames de consola en SVG de las lecciones del Seminario.

Toda interacción con la consola (comandos y su salida) se muestra en las lecciones con
este frame, para que todas se vean igual. Ver CLAUDE.md → "Consola: siempre en un frame SVG".

Uso, desde un script propio:

    import sys; sys.path.insert(0, 'tools')
    from console_frame import frame
    svg = frame(dict(
        id='tcDevices',                       # único en todo el sitio; prefija CSS e ids
        title='Ver los dispositivos con <tspan class="mono">flutter devices</tspan>',
        title_plain='Ver los dispositivos con flutter devices',
        desc='Descripción accesible de lo que muestra la figura.',
        sub='Una línea que explica qué mirar.',
        term_title='Terminal · C:\\develop\\miapp1',
        lines=[('P', 'flutter devices', 'miapp1'),   # P: prompt (comando, carpeta)
               ('O', 'Found 3 connected devices:'),  # O: salida
               ('D', 'No wireless devices were found.'),  # D: salida tenue
               ('K', 'All done!'),                   # K: éxito, en verde
               ('C', '  && otro comando'),           # C: continuación de un comando largo
               ('B', '')],                           # B: línea en blanco
        rings=[(1, 6, 9, 1)],   # (línea, columna, largo, número): recuadro amarillo numerado
        cards=[(1, 'Título', ['línea 1', 'línea 2'], False)],  # tarjetas bajo la terminal;
                                                             # número 'i' = nota informativa
    ))

Las columnas de `rings` cuentan también el prompt ("miapp1> " son 8 caracteres).
Después de generar: validar con check.py y mirar el render de la skill svg-diagrams.
"""

from xml.sax.saxutils import escape as _esc


def escape(t):
    return _esc(t).replace('--', '<tspan letter-spacing="2">-</tspan>-')

CW = 7.8          # ancho de un carácter mono a 13 px
LH = 26           # alto de línea
X0, W = 48, 864   # terminal a todo el ancho útil
TX = X0 + 24      # x del texto


def frame(spec):
    fid = spec['id']
    lines = spec['lines']
    y0 = 112
    first = y0 + 32 + 30
    term_h = 32 + 30 + LH * (len(lines) - 1) + 24
    out = []
    a = out.append
    # tarjetas
    cards = spec.get('cards', [])
    n = len(cards)
    gap = 16
    cw = (W - gap * (n - 1)) / n if n else 0
    body_max = max((len(c[2]) for c in cards), default=0)
    card_h = spec.get('card_h') or (52 + 19 * body_max + 12)
    cy = y0 + term_h + 24
    height = cy + (card_h + 32 if n else 8) + spec.get('foot_pad', 0)
    if spec.get('foot'):
        height += 24

    a(f'<svg id="{fid}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 {height:.0f}" width="100%" '
      f'style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="{fid}-ttl {fid}-dsc" '
      f"font-family=\"ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif\">")
    a(f'  <title id="{fid}-ttl">{escape(spec["title_plain"])}</title>')
    a(f'  <desc id="{fid}-dsc">{escape(spec["desc"])}</desc>')
    a('  <defs>\n    <style>')
    a(f'      #{fid} .title{{fill:#161A26;font-size:22px;font-weight:700}}')
    a(f'      #{fid} .sub{{fill:#79809A;font-size:13.5px}}')
    a(f"      #{fid} .mono{{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}}")
    a(f'      #{fid} .tl{{font-size:13px;fill:#C9CFDA;white-space:pre}}')
    a(f'      #{fid} .pf{{fill:#7F8AA3}} #{fid} .cmd{{fill:#FFFFFF;font-weight:600}}')
    a(f'      #{fid} .dim{{fill:#8A93A6}} #{fid} .okk{{fill:#6BCB77;font-weight:600}}')
    a(f'      #{fid} .ring{{fill:none;stroke:#F2C069;stroke-width:2}}')
    a(f'      #{fid} .chipc{{fill:#F2C069}} #{fid} .chipt{{fill:#1F2430;font-size:11.5px;font-weight:700}}')
    a(f'      #{fid} .ct{{fill:#161A26;font-size:14px;font-weight:700}}')
    a(f'      #{fid} .cb{{fill:#454C61;font-size:13px}}')
    a(f'      #{fid} .foot{{fill:#79809A;font-size:12px}}')
    a('    </style>\n  </defs>')
    a(f'  <rect width="960" height="{height:.0f}" rx="16" fill="#FBFBFD"/>')
    a(f'  <text class="title" x="48" y="56">{spec["title"].replace("--", '<tspan letter-spacing="3">-</tspan>-')}</text>')
    a(f'  <text class="sub" x="48" y="80" data-fit="860">{escape(spec["sub"])}</text>')

    # terminal
    a(f'  <rect x="{X0}" y="{y0}" width="{W}" height="{term_h}" rx="12" fill="#1F2430"/>')
    a(f'  <path d="M{X0},{y0+12} A12,12 0 0 1 {X0+12},{y0} H{X0+W-12} A12,12 0 0 1 {X0+W},{y0+12} V{y0+32} H{X0} Z" fill="#2A3040"/>')
    a(f'  <circle cx="{X0+20}" cy="{y0+16}" r="5" fill="#F14C4C"/><circle cx="{X0+36}" cy="{y0+16}" r="5" fill="#E5C07B"/><circle cx="{X0+52}" cy="{y0+16}" r="5" fill="#6BCB77"/>')
    a(f'  <text x="{X0+W/2:.0f}" y="{y0+16}" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">{escape(spec.get("term_title","Terminal"))}</text>')

    for i, ln in enumerate(lines):
        kind, text = ln[0], ln[1]
        y = first + i * LH
        if kind == 'B':
            continue
        if kind == 'P':
            folder = ln[2]
            a(f'  <text class="tl mono" font-size="13" x="{TX}" y="{y}" data-fit="{W-48}">'
              f'<tspan class="pf">{escape(folder)}&gt; </tspan><tspan class="cmd">{escape(text)}</tspan></text>')
        else:
            cls = {'O': '', 'D': ' dim', 'K': ' okk', 'C': ' cmd'}[kind]
            a(f'  <text class="tl mono{cls}" font-size="13" x="{TX}" y="{y}" data-fit="{W-48}">{escape(text)}</text>')

    for (li, col, ln_, num) in spec.get('rings', []):
        y = first + li * LH
        x = TX + col * CW - 4
        w = ln_ * CW + 8
        a(f'  <rect class="ring" x="{x:.1f}" y="{y-16}" width="{w:.1f}" height="22" rx="5"/>')
        a(f'  <circle class="chipc" cx="{x+w:.1f}" cy="{y-15}" r="8"/>')
        a(f'  <text class="chipt" x="{x+w:.1f}" y="{y-15}" dy="0.35em" text-anchor="middle" font-size="10.5">{num}</text>')

    for k, (num, title, body, mono) in enumerate(cards):
        cx = X0 + k * (cw + gap)
        a(f'  <g transform="translate({cx:.1f},{cy:.0f})">')
        a(f'    <rect width="{cw:.1f}" height="{card_h}" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>')
        if num == 'i':
            a('    <circle cx="26" cy="26" r="10" fill="#4453C9"/>')
            a('    <text x="26" y="26" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="12" font-weight="700">i</text>')
        else:
            a('    <circle class="chipc" cx="26" cy="26" r="10"/>')
            a(f'    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">{num}</text>')
        mcls = ' mono' if mono else ''
        a(f'    <text class="ct{mcls}" x="46" y="26" dy="0.35em" data-fit="{cw-62:.0f}">{escape(title)}</text>')
        for j, b in enumerate(body):
            a(f'    <text class="cb" x="16" y="{60 + j*19}" data-fit="{cw-32:.0f}">{b}</text>')
        if spec.get('extra') and k in spec['extra']:
            a(spec['extra'][k](cw, card_h))
        a('  </g>')

    if spec.get('foot'):
        a(f'  <text class="foot" x="48" y="{height-28:.0f}" data-fit="860">{escape(spec["foot"])}</text>')
    a('</svg>')
    return '\n'.join(out) + '\n'
