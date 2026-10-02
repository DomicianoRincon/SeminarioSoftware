"""Figuras SVG de las lecciones de la sesión 2 (S0010 a S0018).

    python3 tools/sesion2_figuras.py <carpeta>     escribe un .svg por figura, para revisarlas
    python3 tools/sesion2_figuras.py --inject      reemplaza cada bloque ```svg de content/lessonS1x.md
                                                   por la figura con el mismo id
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from code_frame import frame  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SANS = "ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"
FAM = {
    'indigo': ('#EEF1FF', '#A9B4F2', '#4453C9'),
    'violet': ('#F4EBFF', '#C9A6EE', '#7439B8'),
    'amber': ('#FFF3DC', '#F0C572', '#A96C05'),
    'green': ('#E8F6E3', '#9FD68D', '#3A8235'),
    'slate': ('#EFF1F5', '#C4CBD8', '#556074'),
    'rose': ('#FFEBEF', '#F3A3B2', '#C2354F'),
    'teal': ('#E3F6F3', '#86D3CA', '#0F8478'),
}


def head(fid, h, title, plain, sub, desc, css=''):
    return f'''<svg id="{fid}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 {h}" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="{fid}-ttl {fid}-dsc" font-family="{SANS}">
  <title id="{fid}-ttl">{plain}</title>
  <desc id="{fid}-dsc">{desc}</desc>
  <defs>
    <style>
      #{fid} .title{{fill:#161A26;font-size:22px;font-weight:700}}
      #{fid} .sub{{fill:#79809A;font-size:13.5px}}
      #{fid} .h{{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}}
      #{fid} .nt{{font-size:15px;font-weight:700;fill:#161A26}}
      #{fid} .nb{{fill:#454C61;font-size:13px}}
      #{fid} .lbl{{fill:#556074;font-size:12px;font-weight:600}}
      #{fid} .foot{{fill:#79809A;font-size:12px}}
      #{fid} .mono{{font-family:{MONO}}}
      #{fid} .link{{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#{fid}-arrow)}}
{css}    </style>
    <marker id="{fid}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="{h}" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">{title}</text>
  <text class="sub" x="48" y="80" data-fit="860">{sub}</text>
'''


def note(y, color, title, lines, h=60):
    soft, border, strong = FAM[color]
    out = [f'<g transform="translate(16,{y})"><rect width="328" height="{h}" rx="10" fill="{soft}" stroke="{border}" stroke-width="1.5"/>',
           f'<text x="14" y="23" font-size="13.5" font-weight="700" fill="{strong}" data-fit="300">{title}</text>']
    for i, ln in enumerate(lines):
        out.append(f'<text x="14" y="{43 + i*17}" font-size="12.5" fill="#454C61" data-fit="300">{ln}</text>')
    out.append('</g>')
    return ''.join(out)


FIGS = {}

# ───────────────────────────── S0010 · El proyecto por dentro

def pp_carpetas():
    fid = 'ppCarpetas'
    rows = [
        (0, 'miapp1/', 'slate', 'La carpeta del proyecto', False),
        (1, 'lib/', 'indigo', 'Tu código Dart. Aquí pasas casi todo el tiempo', False),
        (2, 'main.dart', 'indigo', 'Punto de entrada: arranca la app y declara las rutas', False),
        (2, 'theme/', 'violet', 'Colores y tema de la app, en app_theme.dart', False),
        (2, 'models/', 'violet', 'Los datos que maneja la app', False),
        (2, 'components/', 'amber', 'Widgets reutilizables. Es lo que haces en esta sesión', True),
        (2, 'screens/', 'violet', 'Pantallas completas, con Scaffold (sesión 3)', False),
        (2, 'pages/', 'violet', 'Secciones que una pantalla hospeda (sesión 9)', False),
        (1, 'assets/', 'green', 'Imágenes y otros archivos que viajan con la app', False),
        (1, 'pubspec.yaml', 'green', 'Nombre, dependencias y assets declarados', False),
        (1, 'android/  ios/  web/', 'slate', 'Un proyecto por plataforma. Casi nunca se tocan', False),
    ]
    y0, rh = 124, 40
    h = y0 + rh * len(rows) + 72
    s = head(fid, h, 'Las carpetas del proyecto', 'Las carpetas del proyecto',
             'Flutter crea las de afuera. Las que están dentro de lib/ las creas tú, y cada una guarda una sola cosa.',
             'Árbol de carpetas de un proyecto Flutter: lib con main.dart, theme, models, components, screens y pages; assets; pubspec.yaml; y las carpetas de plataforma. Se destaca components, que es donde se trabaja en esta sesión.')
    s += f'  <rect x="48" y="104" width="312" height="{rh*len(rows)+24}" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
    for i, (lvl, name, color, text, hero) in enumerate(rows):
        soft, border, strong = FAM[color]
        y = y0 + i * rh + 12
        x = 68 + lvl * 28
        if lvl:
            s += f'  <path d="M{x-16},{y-rh/2-4 if i else y} V{y} H{x-4}" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>\n'
        folder = name.endswith('/')
        w = len(name) * 7.8 + 24
        sw = 2.5 if hero else 1.5
        s += f'  <rect x="{x}" y="{y-14}" width="{w:.0f}" height="28" rx="{8 if folder else 4}" fill="{soft}" stroke="{border}" stroke-width="{sw}"/>\n'
        s += f'  <text class="mono" x="{x+12}" y="{y}" dy="0.35em" font-size="13" font-weight="600" fill="{strong}" data-fit="{w-16:.0f}">{name}</text>\n'
        s += f'  <path d="M{x+w+8:.0f},{y} H384" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="2 5"/>\n'
        wt = 700 if hero else 400
        s += f'  <text x="396" y="{y}" dy="0.35em" font-size="14" font-weight="{wt}" fill="{"#161A26" if hero else "#454C61"}" data-fit="516">{text}</text>\n'
    s += f'  <text class="foot" x="48" y="{h-28}" data-fit="860">Los nombres de carpetas y archivos van en minúscula y con guion bajo: home_screen.dart, stat_card.dart.</text>\n</svg>\n'
    return s


FIGS['ppCarpetas'] = pp_carpetas

FIGS['ppMain'] = lambda: frame(dict(
    id='ppMain',
    title='<tspan class="mono">main.dart</tspan>, parte por parte',
    title_plain='main.dart, parte por parte',
    desc='El archivo main.dart anotado: los import, la función main que llama a runApp, la clase App que es un StatelessWidget, y MaterialApp con su tabla de rutas y su ruta inicial.',
    sub='Todo proyecto Flutter arranca aquí. Es corto, y cada bloque tiene un solo trabajo.',
    file='lib/main.dart',
    panel='QUÉ HACE CADA PARTE',
    code=[
        "import 'package:flutter/material.dart';",
        "import 'screens/home_screen.dart';",
        "import 'theme/app_theme.dart';",
        "",
        "void main() {",
        "  runApp(const App());",
        "}",
        "",
        "class App extends StatelessWidget {",
        "  const App({super.key});",
        "",
        "  @override",
        "  Widget build(BuildContext context) {",
        "    return MaterialApp(",
        "      title: 'Mi app',",
        "      theme: buildTheme(),",
        "      initialRoute: '/home',",
        "      routes: {",
        "        '/home': (context) => const HomeScreen(),",
        "      },",
        "    );",
        "  }",
        "}",
    ],
    result=(note(16, 'slate', 'import', ['Trae código de otros archivos: los widgets', 'de Flutter y tus propias pantallas.'], 68)
            + note(96, 'amber', 'main()', ['La primera función que se ejecuta.', 'Es la puerta de entrada de la app.'], 68)
            + note(176, 'green', 'runApp(...)', ['Recibe el widget raíz y lo pone en pantalla.', 'Todo lo demás cuelga de él.'], 68)
            + note(256, 'indigo', 'App', ['El widget raíz. Lo escribes tú, como', 'cualquier otro componente.'], 68)
            + note(336, 'violet', 'MaterialApp', ['Configura toda la app: título, tema', 'y pantallas.'], 68)
            + note(416, 'rose', 'routes e initialRoute', ['La tabla de pantallas, cada una con su', 'nombre, y por cuál se empieza.'], 68)),
    arrows=[
        dict(line=0, find='import', to=(16, 50), color='teal'),
        dict(line=4, find='main()', to=(16, 130), color='amber'),
        dict(line=5, find='runApp(const App())', to=(16, 210), color='green'),
        dict(line=8, find='App', to=(16, 290), color='indigo'),
        dict(line=13, find='MaterialApp', to=(16, 370), color='violet'),
        dict(line=17, find='routes', to=(16, 450), color='rose'),
    ],
))


def pp_declarativo():
    fid = 'ppDeclarativo'
    h = 500
    css = (f'      #{fid} .code{{font-size:13px;fill:#C9CFDA}}\n'
           f'      #{fid} .k{{fill:#F08FB0}} #{fid} .s{{fill:#A8D8A0}} #{fid} .c{{fill:#7FD1E8}}\n')
    s = head(fid, h, 'Dar órdenes o describir', 'Dar órdenes o describir',
             'Las dos formas de programar una interfaz. Flutter usa la segunda.',
             'Comparación entre el paradigma imperativo, donde el código modifica cada elemento de la pantalla paso a paso, y el declarativo, donde el código describe la interfaz a partir del estado y el framework la redibuja.', css)
    s += '''  <text class="h" x="48" y="124">IMPERATIVO · DAR ÓRDENES</text>
  <rect x="48" y="140" width="408" height="176" rx="12" fill="#1F2430"/>
  <text class="code mono" x="68" y="174" data-fit="372">counter = counter + 1;</text>
  <text class="code mono" x="68" y="202" data-fit="372">label.<tspan class="c">setText</tspan>(<tspan class="s">'3'</tspan>);</text>
  <text class="code mono" x="68" y="230" data-fit="372">label.<tspan class="c">setColor</tspan>(red);</text>
  <text class="code mono" x="68" y="258" data-fit="372">button.<tspan class="c">setEnabled</tspan>(<tspan class="k">false</tspan>);</text>
  <text class="code mono" x="68" y="286" data-fit="372">warning.<tspan class="c">show</tspan>();</text>
  <g transform="translate(48,332)">
    <rect width="408" height="100" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/>
    <text class="nt" x="16" y="30" fill="#C2354F" data-fit="376">Tú cambias cada pieza, una por una</text>
    <text class="nb" x="16" y="56" data-fit="376">Si olvidas una línea, la pantalla queda mostrando</text>
    <text class="nb" x="16" y="76" data-fit="376">algo que ya no es cierto.</text>
  </g>

  <text class="h" x="504" y="124">DECLARATIVO · DESCRIBIR</text>
  <g transform="translate(504,140)">
    <rect width="112" height="72" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
    <text x="56" y="28" text-anchor="middle" font-size="12" font-weight="700" fill="#A96C05" data-fit="96">ESTADO</text>
    <text class="mono" x="56" y="52" text-anchor="middle" font-size="14" font-weight="600" fill="#161A26" data-fit="96">counter = 3</text>
  </g>
  <path class="link" d="M616,176 H648"/>
  <g transform="translate(656,140)">
    <rect width="96" height="72" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="2.5"/>
    <text x="48" y="28" text-anchor="middle" font-size="12" font-weight="700" fill="#4453C9" data-fit="80">TU CÓDIGO</text>
    <text class="mono" x="48" y="52" text-anchor="middle" font-size="14" font-weight="600" fill="#161A26" data-fit="80">build()</text>
  </g>
  <path class="link" d="M752,176 H784"/>
  <g transform="translate(792,140)">
    <rect width="120" height="72" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
    <text x="60" y="28" text-anchor="middle" font-size="12" font-weight="700" fill="#3A8235" data-fit="104">INTERFAZ</text>
    <text x="60" y="52" text-anchor="middle" font-size="14" font-weight="600" fill="#161A26" data-fit="104">lo que se ve</text>
  </g>
  <rect x="504" y="228" width="408" height="88" rx="12" fill="#1F2430"/>
  <text class="code mono" x="524" y="262" data-fit="372"><tspan class="c">Text</tspan>(<tspan class="s">'$counter'</tspan>),</text>
  <text class="code mono" x="524" y="290" data-fit="372"><tspan class="k">if</tspan> (counter &gt;= 3) <tspan class="c">Text</tspan>(<tspan class="s">'Límite'</tspan>),</text>
  <g transform="translate(504,332)">
    <rect width="408" height="100" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
    <text class="nt" x="16" y="30" fill="#3A8235" data-fit="376">Tú describes cómo se ve para cada estado</text>
    <text class="nb" x="16" y="56" data-fit="376">Cuando el estado cambia, Flutter vuelve a llamar a</text>
    <text class="nb" x="16" y="76" data-fit="376">build() y redibuja. No hay pieza que se te olvide.</text>
  </g>
'''
    s += f'  <text class="foot" x="48" y="{h-28}" data-fit="860">interfaz = f(estado): la pantalla es el resultado de una función, no una lista de cambios.</text>\n</svg>\n'
    return s


FIGS['ppDeclarativo'] = pp_declarativo

# ───────────────────────────── S0011 · Text


def effect_row(y, color, before, after, text):
    soft, border, strong = FAM[color]
    return (f'<g transform="translate(20,{y})"><rect width="320" height="36" rx="8" fill="{soft}" stroke="{border}" stroke-width="1.5"/>'
            f'{before}<text x="62" y="18" dy="0.35em" font-size="14" fill="#79809A">→</text>{after}'
            f'<text x="140" y="18" dy="0.35em" font-size="13" fill="#454C61" data-fit="170">{text}</text></g>')


def aa(x, size=14, weight=400, fill='#161A26'):
    return f'<text x="{x}" y="18" dy="0.35em" font-size="{size}" font-weight="{weight}" fill="{fill}">Aa</text>'


FIGS['txAnatomia'] = lambda: frame(dict(
    id='txAnatomia',
    title='Las partes de un <tspan class="mono">Text</tspan>',
    title_plain='Las partes de un Text',
    desc='Un widget Text con la cadena Hola, Icesi y un TextStyle con fontSize 32, fontWeight bold y color indigo. A la derecha, el texto resultante y el efecto de cada propiedad por separado.',
    sub='El primer dato es lo que se escribe. Todo lo que cambia cómo se ve va dentro de style.',
    file='lib/main.dart',
    code=[
        "Text(",
        "  'Hola, Icesi',",
        "  style: TextStyle(",
        "    fontSize: 32,",
        "    fontWeight: FontWeight.bold,",
        "    color: Colors.indigo,",
        "  ),",
        ")",
    ],
    result=('<text x="188" y="47" dy="0.35em" text-anchor="middle" font-size="32" font-weight="700" fill="#3F51B5" data-fit="250">Hola, Icesi</text>'
            + effect_row(88, 'amber', aa(16, 11), aa(86, 20), 'tamaño de la letra')
            + effect_row(132, 'green', aa(16), aa(86, 14, 800), 'grosor: negrita')
            + effect_row(176, 'violet', aa(16), aa(86, 14, 400, '#3F51B5'), 'color de la letra')),
    arrows=[
        dict(line=1, find="'Hola, Icesi'", to=(84, 47), color='indigo'),
        dict(line=3, find='fontSize: 32', to=(20, 106), color='amber', lane=2),
        dict(line=4, find='fontWeight: FontWeight.bold', to=(20, 150), color='green', lane=1),
        dict(line=5, find='color: Colors.indigo', to=(20, 194), color='violet', lane=0),
    ],
))

FIGS['txLargo'] = lambda: frame(dict(
    id='txLargo',
    title='Cuando el texto no cabe',
    title_plain='Cuando el texto no cabe',
    desc='Un Text con maxLines 1 y overflow TextOverflow.ellipsis. A la derecha, el mismo texto sin límite ocupa tres renglones, y con el límite ocupa uno solo terminado en puntos suspensivos.',
    sub='Un texto largo ocupa los renglones que necesite. Con dos propiedades lo dejas en uno solo.',
    file='lib/main.dart',
    min_h=300,
    code=[
        "Text(",
        "  'Seminario de Ingeniería de Software, grupo 1',",
        "  maxLines: 1,",
        "  overflow: TextOverflow.ellipsis,",
        ")",
    ],
    result=('<text x="24" y="28" font-size="12" font-weight="700" fill="#79809A" letter-spacing=".06em">SIN LÍMITE</text>'
            '<rect x="24" y="40" width="176" height="84" rx="8" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>'
            '<text x="36" y="64" font-size="15" fill="#161A26" data-fit="156">Seminario de</text>'
            '<text x="36" y="86" font-size="15" fill="#161A26" data-fit="156">Ingeniería de</text>'
            '<text x="36" y="108" font-size="15" fill="#161A26" data-fit="156">Software, grupo 1</text>'
            '<text x="24" y="164" font-size="12" font-weight="700" fill="#79809A" letter-spacing=".06em">CON maxLines Y overflow</text>'
            '<rect x="24" y="176" width="176" height="40" rx="8" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>'
            '<text x="36" y="196" dy="0.35em" font-size="15" fill="#161A26" data-fit="156">Seminario de Ingeni…</text>'
            '<text x="216" y="190" font-size="12.5" fill="#454C61" data-fit="130">un solo renglón</text>'
            '<text x="216" y="208" font-size="12.5" fill="#454C61" data-fit="130">y tres puntos al final</text>'),
    arrows=[
        dict(line=2, find='maxLines: 1', to=(24, 196), color='green', lane=1),
        dict(line=3, find='overflow: TextOverflow.ellipsis', via=[(182, 240)], to=(182, 218), color='amber', lane=0),
    ],
))

# ───────────────────────────── S0012 · Image


def picture(x, y, w, h, cid):
    return (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/></clipPath>'
            f'<g clip-path="url(#{cid})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#CFE4FF"/>'
            f'<circle cx="{x+w*0.72}" cy="{y+h*0.28}" r="{h*0.13}" fill="#F7C948"/>'
            f'<path d="M{x},{y+h} L{x+w*0.34},{y+h*0.42} L{x+w*0.56},{y+h*0.74} L{x+w*0.72},{y+h*0.56} L{x+w},{y+h*0.9} V{y+h} Z" fill="#5B8C5A"/>'
            f'<path d="M{x},{y+h} L{x+w*0.34},{y+h*0.42} L{x+w*0.46},{y+h*0.6} L{x+w*0.2},{y+h} Z" fill="#3E6B45"/></g>')


FIGS['imNetwork'] = lambda: frame(dict(
    id='imNetwork',
    title='Una imagen desde internet',
    title_plain='Una imagen desde internet',
    desc='Image.network con la dirección de la imagen, width 160 y height 160. A la derecha, la imagen dibujada con sus dos medidas señaladas.',
    sub='La dirección dice de dónde se descarga. width y height reservan el espacio que ocupa.',
    file='lib/main.dart',
    min_h=300,
    code=[
        "Image.network(",
        "  'https://picsum.photos/400',",
        "  width: 160,",
        "  height: 160,",
        "  fit: BoxFit.cover,",
        ")",
    ],
    result=(picture(140, 72, 144, 144, 'imNetwork-clip')
            + '<path d="M140,232 H284 M140,226 V238 M284,226 V238" stroke="#3A8235" stroke-width="1.75" fill="none"/>'
            '<text x="212" y="252" text-anchor="middle" font-size="12.5" font-weight="700" fill="#3A8235">160</text>'
            '<path d="M124,72 V216 M118,72 H130 M118,216 H130" stroke="#7439B8" stroke-width="1.75" fill="none"/>'
            '<text x="110" y="144" dy="0.35em" text-anchor="end" font-size="12.5" font-weight="700" fill="#7439B8">160</text>'),
    arrows=[
        dict(line=1, find="'https://picsum.photos/400'", to=(212, 70), end='v', color='indigo'),
        dict(line=2, find='width: 160', via=[(60, 232)], to=(136, 232), color='green', lane=0),
        dict(line=3, find='height: 160', to=(84, 144), color='violet', lane=2),
    ],
))


def im_asset():
    fid = 'imAsset'
    h = 392
    css = f'      #{fid} .code{{font-size:13px;fill:#C9CFDA}}\n      #{fid} .s{{fill:#A8D8A0}} #{fid} .c{{fill:#7FD1E8}} #{fid} .k{{fill:#F08FB0}}\n'
    s = head(fid, h, 'Una imagen que viaja con la app', 'Una imagen que viaja con la app',
             'Tres pasos, siempre los mismos. Si falta el segundo, la app no encuentra el archivo.',
             'Los tres pasos para mostrar una imagen local: guardar el archivo en la carpeta assets del proyecto, declarar la carpeta en pubspec.yaml y usar Image.asset con la ruta del archivo.', css)
    cards = [
        ('1', 'Guarda el archivo', 'miapp1/', ['<tspan class="c">assets/</tspan>', '  logo.png', '<tspan class="c">lib/</tspan>', 'pubspec.yaml'],
         'En assets/, al lado de lib/'),
        ('2', 'Declara la carpeta', 'pubspec.yaml', ['<tspan class="k">flutter:</tspan>', '  <tspan class="k">assets:</tspan>', '    - assets/', ''],
         'La sangría de dos espacios importa'),
        ('3', 'Úsala en el código', 'lib/main.dart', ['<tspan class="c">Image</tspan>.asset(', "  <tspan class=\"s\">'assets/logo.png'</tspan>,", '  width: 120,', ')'],
         'La ruta completa desde la raíz'),
    ]
    for i, (num, title, file, lines, footn) in enumerate(cards):
        x = 48 + i * 296
        s += f'  <g transform="translate({x},112)">\n'
        s += '    <rect width="272" height="216" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
        s += '    <circle cx="28" cy="28" r="12" fill="#F2C069"/>\n'
        s += f'    <text x="28" y="28" dy="0.35em" text-anchor="middle" font-size="13" font-weight="700" fill="#1F2430">{num}</text>\n'
        s += f'    <text class="nt" x="50" y="28" dy="0.35em" data-fit="206">{title}</text>\n'
        s += '    <rect x="16" y="52" width="240" height="124" rx="8" fill="#1F2430"/>\n'
        s += f'    <text class="mono" x="28" y="72" font-size="12" fill="#8A93A6" data-fit="216">{file}</text>\n'
        for j, ln in enumerate(lines):
            if ln:
                ind = len(ln) - len(ln.lstrip())
                s += f'    <text class="code mono" x="{28 + ind*7.8:.1f}" y="{96 + j*22}" data-fit="{216 - ind*7.8:.0f}">{ln.lstrip()}</text>\n'
        s += f'    <text x="16" y="198" font-size="12.5" fill="#454C61" data-fit="240">{footn}</text>\n'
        s += '  </g>\n'
        if i < 2:
            s += f'  <path class="link" d="M{x+274},220 H{x+294}"/>\n'
    s += f'  <text class="foot" x="48" y="{h-28}" data-fit="860">Después de tocar pubspec.yaml hay que detener la app y volver a ejecutarla: el hot reload no carga assets nuevos.</text>\n</svg>\n'
    return s


FIGS['imAsset'] = im_asset


def im_fit():
    fid = 'imFit'
    h = 468
    s = head(fid, h, 'Qué hace <tspan class="mono">fit</tspan> cuando la imagen no tiene la forma de la caja',
             'Qué hace fit cuando la imagen no tiene la forma de la caja',
             'La misma imagen, casi cuadrada, en la misma caja alargada. Solo cambia fit.',
             'La misma imagen dentro de una caja alargada con tres valores de fit: cover llena la caja y recorta lo que sobra, contain muestra la imagen entera y deja espacio vacío, fill la estira hasta deformarla.')
    pic = ('<rect width="120" height="90" fill="#CFE4FF"/><circle cx="88" cy="24" r="12" fill="#F7C948"/>'
           '<path d="M0,90 L40,38 L66,66 L86,50 L120,82 V90 Z" fill="#5B8C5A"/><path d="M0,90 L40,38 L55,54 L24,90 Z" fill="#3E6B45"/>')
    s += f'  <defs><g id="{fid}-pic">{pic}</g></defs>\n'
    s += f'  <text class="h" x="48" y="124">LA IMAGEN ORIGINAL</text>\n  <g transform="translate(48,136)"><use href="#{fid}-pic"/></g>\n'
    s += '  <text class="nb" x="184" y="176" data-fit="300">Mide 4 de ancho por 3 de alto.</text>\n'
    s += '  <text class="nb" x="184" y="196" data-fit="300">La caja donde va es mucho más ancha que alta.</text>\n'
    boxes = [
        ('BoxFit.cover', 'green', 'Llena la caja y recorta lo que sobra.', 'La más usada: no deforma ni deja huecos.',
         'translate(0,-30) scale(2)'),
        ('BoxFit.contain', 'indigo', 'Muestra la imagen entera.', 'Deja espacio vacío a los lados.',
         'translate(40,0) scale(1.3333)'),
        ('BoxFit.fill', 'rose', 'Estira la imagen hasta llenar.', 'Se deforma: casi nunca es lo que quieres.',
         'scale(2,1.3333)'),
    ]
    for i, (name, color, l1, l2, tr) in enumerate(boxes):
        soft, border, strong = FAM[color]
        x = 48 + i * 312
        s += f'  <clipPath id="{fid}-c{i}"><rect width="240" height="120" rx="8"/></clipPath>\n'
        s += f'  <g transform="translate({x},288)">\n'
        s += f'    <text class="mono" x="0" y="-12" font-size="14" font-weight="700" fill="{strong}" data-fit="240">{name}</text>\n'
        s += f'    <rect width="240" height="120" rx="8" fill="#EFF1F5"/>\n'
        s += f'    <g clip-path="url(#{fid}-c{i})"><use href="#{fid}-pic" transform="{tr}"/></g>\n'
        s += f'    <rect width="240" height="120" rx="8" fill="none" stroke="{border}" stroke-width="2"/>\n'
        s += f'    <text class="nb" x="0" y="144" data-fit="240" font-weight="600">{l1}</text>\n'
        s += f'    <text class="nb" x="0" y="163" data-fit="250">{l2}</text>\n'
        s += '  </g>\n'
    s += '</svg>\n'
    return s


FIGS['imFit'] = im_fit

# ───────────────────────────── S0013 · Button

FIGS['btAnatomia'] = lambda: frame(dict(
    id='btAnatomia',
    title='Las dos partes de un botón',
    title_plain='Las dos partes de un botón',
    desc='Un ElevatedButton con onPressed, una función que imprime Guardado, y child, un Text que dice Guardar. A la derecha el botón dibujado y la consola con el mensaje que aparece al tocarlo.',
    sub='Un botón siempre responde dos preguntas: qué muestra y qué hace cuando lo tocan.',
    file='lib/main.dart',
    min_h=292,
    code=[
        "ElevatedButton(",
        "  onPressed: () {",
        "    print('Guardado');",
        "  },",
        "  child: Text('Guardar'),",
        ")",
    ],
    result=('<text x="24" y="28" font-size="12" font-weight="700" fill="#79809A" letter-spacing=".06em">LO QUE HACE AL TOCARLO</text>'
            '<rect x="24" y="40" width="312" height="56" rx="8" fill="#1F2430"/>'
            f'<text x="40" y="60" font-size="11.5" fill="#8A93A6" font-family="{MONO}">Consola</text>'
            f'<text x="40" y="82" font-size="13" fill="#C9CFDA" font-family="{MONO}">Guardado</text>'
            '<text x="24" y="150" font-size="12" font-weight="700" fill="#79809A" letter-spacing=".06em">LO QUE MUESTRA</text>'
            '<rect x="112" y="170" width="136" height="44" rx="22" fill="#0B1020" fill-opacity=".10"/>'
            '<rect x="112" y="166" width="136" height="44" rx="22" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>'
            '<text x="180" y="188" dy="0.35em" text-anchor="middle" font-size="15" font-weight="600" fill="#4453C9">Guardar</text>'),
    arrows=[
        dict(line=1, find='onPressed', to=(24, 68), color='amber', lane=1),
        dict(line=4, find="child: Text('Guardar')", to=(108, 188), color='indigo', lane=0),
    ],
))


def bt_tipos():
    fid = 'btTipos'
    h = 468
    s = head(fid, h, 'Los cuatro botones de siempre', 'Los cuatro botones de siempre',
             'Se escriben igual. Lo que cambia es cuánto llaman la atención.',
             'Los cuatro botones básicos de Flutter y su aspecto: ElevatedButton, OutlinedButton, TextButton e IconButton, en estado normal y deshabilitados con onPressed null.')
    kinds = [
        ('ElevatedButton', 'La acción principal', 'de la pantalla', 'e'),
        ('OutlinedButton', 'Una acción secundaria', 'que debe verse', 'o'),
        ('TextButton', 'Acciones discretas:', 'cancelar, ver más', 't'),
        ('IconButton', 'Una acción que se', 'entiende con un icono', 'i'),
    ]

    def draw(kind, on):
        ink = '#4453C9' if on else '#A0A8B8'
        if kind == 'i':
            heart = f'<path d="M96,26 c-5,-9 -18,-4 -14,6 c2,6 9,10 14,14 c5,-4 12,-8 14,-14 c4,-10 -9,-15 -14,-6 Z" fill="{"#C2354F" if on else "#C4CBD8"}"/>'
            return heart
        out = ''
        if kind == 'e':
            if on:
                out += '<rect x="36" y="14" width="120" height="40" rx="20" fill="#0B1020" fill-opacity=".10"/>'
            out += f'<rect x="36" y="10" width="120" height="40" rx="20" fill="{"#EEF1FF" if on else "#EFF1F5"}" stroke="{"#A9B4F2" if on else "#D9DEE8"}" stroke-width="1.5"/>'
        if kind == 'o':
            out += f'<rect x="36" y="10" width="120" height="40" rx="20" fill="none" stroke="{"#79809A" if on else "#D9DEE8"}" stroke-width="1.5"/>'
        out += f'<text x="96" y="30" dy="0.35em" text-anchor="middle" font-size="14.5" font-weight="600" fill="{ink}">Guardar</text>'
        return out

    s += '  <text class="h" x="48" y="124">CON UNA FUNCIÓN EN onPressed</text>\n'
    s += '  <text class="h" x="48" y="316">CON onPressed: null · DESHABILITADO</text>\n'
    for i, (name, l1, l2, kind) in enumerate(kinds):
        x = 48 + i * 224
        s += f'  <g transform="translate({x},140)">\n'
        s += '    <rect width="192" height="136" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
        s += f'    <g transform="translate(0,6)">{draw(kind, True)}</g>\n'
        s += f'    <text class="mono" x="96" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#161A26" data-fit="176">{name}</text>\n'
        s += f'    <text class="nb" x="96" y="106" text-anchor="middle" data-fit="176">{l1}</text>\n'
        s += f'    <text class="nb" x="96" y="124" text-anchor="middle" data-fit="176">{l2}</text>\n'
        s += '  </g>\n'
        s += f'  <g transform="translate({x},332)">\n'
        s += '    <rect width="192" height="64" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
        s += f'    <g transform="translate(0,2)">{draw(kind, False)}</g>\n'
        s += '  </g>\n'
    s += f'  <text class="foot" x="48" y="{h-28}" data-fit="860">Un botón sin función se pinta gris y no responde. Flutter lo hace solo: no hay una propiedad «enabled».</text>\n</svg>\n'
    return s


FIGS['btTipos'] = bt_tipos

# ───────────────────────────── S0014 · TextField

MAIL = ('<rect x="-9" y="-7" width="18" height="14" rx="2" fill="none" stroke="#556074" stroke-width="1.75"/>'
        '<path d="M-9,-6 L0,1 L9,-6" fill="none" stroke="#556074" stroke-width="1.75"/>')

FIGS['tfAnatomia'] = lambda: frame(dict(
    id='tfAnatomia',
    title='Las partes de un <tspan class="mono">TextField</tspan>',
    title_plain='Las partes de un TextField',
    desc='Un TextField con InputDecoration: labelText Correo, hintText con un correo de ejemplo, prefixIcon con un sobre y border OutlineInputBorder. A la derecha el campo dibujado, con cada parte señalada.',
    sub='El campo en sí no tiene propiedades de aspecto. Todo lo que se ve va en decoration.',
    file='lib/main.dart',
    min_h=336,
    code=[
        "TextField(",
        "  decoration: InputDecoration(",
        "    labelText: 'Correo',",
        "    hintText: 'nombre@icesi.edu.co',",
        "    prefixIcon: Icon(Icons.mail),",
        "    border: OutlineInputBorder(),",
        "  ),",
        ")",
    ],
    result=('<rect x="56" y="180" width="280" height="56" rx="6" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/>'
            '<rect x="68" y="172" width="56" height="16" fill="#FFFFFF"/>'
            '<text x="74" y="180" dy="0.35em" font-size="12.5" font-weight="600" fill="#4453C9">Correo</text>'
            f'<g transform="translate(82,208)">{MAIL}</g>'
            '<path d="M104,198 V218" stroke="#4453C9" stroke-width="1.5"/>'
            '<text x="110" y="208" dy="0.35em" font-size="15" fill="#A0A8B8">nombre@icesi.edu.co</text>'
            '<text x="196" y="296" text-anchor="middle" font-size="12" fill="#79809A" data-fit="300">Así se ve al tocarlo, antes de escribir.</text>'),
    arrows=[
        dict(line=2, find="labelText: 'Correo'", to=(96, 168), end='v', color='indigo'),
        dict(line=3, find="hintText: 'nombre@icesi.edu.co'", via=[(170, 276)], to=(170, 220), color='amber', lane=2),
        dict(line=4, find='prefixIcon: Icon(Icons.mail)', via=[(82, 264)], to=(82, 222), color='green', lane=1),
        dict(line=5, find='border: OutlineInputBorder()', to=(52, 226), color='violet', lane=0),
    ],
))


def keypad():
    out = '<rect x="96" y="212" width="168" height="124" rx="10" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>'
    keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '', '0', '⌫']
    for i, k in enumerate(keys):
        if not k:
            continue
        x = 106 + (i % 3) * 52
        y = 220 + (i // 3) * 28
        out += f'<rect x="{x}" y="{y}" width="44" height="22" rx="5" fill="#FFFFFF" stroke="#D9DEE8"/>'
        out += f'<text x="{x+22}" y="{y+11}" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="#454C61">{k}</text>'
    return out


FIGS['tfTipos'] = lambda: frame(dict(
    id='tfTipos',
    title='Contraseñas y teclados',
    title_plain='Contraseñas y teclados',
    desc='Dos TextField. El primero, con obscureText true, muestra puntos en lugar de la contraseña. El segundo, con keyboardType TextInputType.number, abre el teclado numérico.',
    sub='Estas dos sí son propiedades del campo, no de la decoración: cambian cómo se escribe.',
    file='lib/main.dart',
    min_h=404,
    code=[
        "TextField(",
        "  obscureText: true,",
        "  decoration: InputDecoration(",
        "    labelText: 'Contraseña',",
        "  ),",
        "),",
        "TextField(",
        "  keyboardType: TextInputType.number,",
        "  decoration: InputDecoration(",
        "    labelText: 'Edad',",
        "  ),",
        "),",
    ],
    result=('<text x="64" y="30" font-size="12" fill="#79809A">Contraseña</text>'
            '<text x="64" y="56" font-size="20" fill="#161A26" letter-spacing="3">••••••••</text>'
            '<path d="M64,68 H296" stroke="#79809A" stroke-width="1.5"/>'
            '<text x="64" y="150" font-size="12" fill="#79809A">Edad</text>'
            '<text x="64" y="174" font-size="16" fill="#161A26">21</text>'
            '<path d="M64,186 H296" stroke="#4453C9" stroke-width="2"/>'
            + keypad()),
    arrows=[
        dict(line=1, find='obscureText: true', to=(58, 49), color='violet', lane=0),
        dict(line=7, find='keyboardType: TextInputType.number', via=[(40, 191)], to=(92, 274), color='green', lane=0),
    ],
))

# ───────────────────────────── S0015 · StatelessWidget


def stat(x, y, number, label, color='indigo'):
    soft, border, strong = FAM[color]
    return (f'<g transform="translate({x},{y})"><rect width="96" height="72" rx="10" fill="{soft}" stroke="{border}" stroke-width="1.5"/>'
            f'<text x="48" y="32" text-anchor="middle" font-size="22" font-weight="700" fill="#161A26">{number}</text>'
            f'<text x="48" y="54" text-anchor="middle" font-size="11.5" fill="#556074" data-fit="88">{label}</text></g>')


def sw_repetido():
    fid = 'swRepetido'
    h = 532
    css = f'      #{fid} .code{{font-size:12.5px;fill:#C9CFDA}}\n      #{fid} .s{{fill:#A8D8A0}} #{fid} .c{{fill:#7FD1E8}} #{fid} .d{{fill:#7F8AA3}}\n'
    s = head(fid, h, 'Copiar y pegar, o hacer un componente', 'Copiar y pegar, o hacer un componente',
             'La misma fila de tres indicadores, escrita de dos formas.',
             'A la izquierda, el mismo bloque de widgets copiado tres veces, donde solo cambian dos datos. A la derecha, un componente StatCard definido una vez y usado tres veces con datos distintos.', css)
    s += '  <text class="h" x="48" y="124">SIN COMPONENTE · EL MISMO BLOQUE, TRES VECES</text>\n'
    data = [("'128'", "'Publicaciones'"), ("'2.4k'", "'Seguidores'"), ("'310'", "'Seguidos'")]
    for i, (n, l) in enumerate(data):
        y = 140 + i * 100
        s += f'  <rect x="48" y="{y}" width="408" height="88" rx="10" fill="#1F2430"/>\n'
        s += f'  <text class="code mono" x="64" y="{y+24}" data-fit="376"><tspan class="c">Column</tspan>(children: [</text>\n'
        s += f'  <text class="code mono" x="80" y="{y+46}" data-fit="360"><tspan class="c">Text</tspan>(<tspan class="s">{n}</tspan>, <tspan class="d">style: …</tspan>),</text>\n'
        s += f'  <text class="code mono" x="80" y="{y+68}" data-fit="360"><tspan class="c">Text</tspan>(<tspan class="s">{l}</tspan>, <tspan class="d">style: …</tspan>), ])</text>\n'
    s += '''  <g transform="translate(48,464)">
    <text class="nb" x="0" y="0" font-weight="700" fill="#C2354F" data-fit="408">Cambiar el diseño = editar tres lugares sin equivocarse.</text>
  </g>
  <text class="h" x="504" y="124">CON COMPONENTE · SE ESCRIBE UNA VEZ</text>
  <g transform="translate(504,140)">
    <rect width="408" height="88" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="2.5"/>
    <text class="mono" x="20" y="34" font-size="16" font-weight="700" fill="#4453C9" data-fit="368">StatCard</text>
    <text class="nb" x="20" y="60" data-fit="368">El diseño vive aquí, en lib/components/stat_card.dart</text>
  </g>
  <path class="link" d="M708,228 V252"/>
  <text class="lbl" x="720" y="246" data-fit="180">se usa tres veces</text>
  <rect x="504" y="260" width="408" height="88" rx="10" fill="#1F2430"/>
'''
    for i, (n, l) in enumerate(data):
        s += f'  <text class="code mono" x="520" y="{284 + i*22}" font-size="12" data-fit="380"><tspan class="c">StatCard</tspan>(number: <tspan class="s">{n}</tspan>, label: <tspan class="s">{l}</tspan>),</text>\n'
    s += '  <g transform="translate(504,0)">' + stat(36, 364, '128', 'Publicaciones') + stat(156, 364, '2.4k', 'Seguidores') + stat(276, 364, '310', 'Seguidos') + '</g>\n'
    s += '  <text class="nb" x="504" y="464" font-weight="700" fill="#3A8235" data-fit="408">Cambiar el diseño = editar un solo archivo.</text>\n'
    s += f'  <text class="foot" x="48" y="{h-28}" data-fit="860">La señal para crear un componente: estás copiando un bloque y solo le cambias los datos.</text>\n</svg>\n'
    return s


FIGS['swRepetido'] = sw_repetido

FIGS['swAnatomia'] = lambda: frame(dict(
    id='swAnatomia',
    title='Anatomía de un componente',
    title_plain='Anatomía de un componente',
    desc='La clase StatCard anotada: extiende StatelessWidget, declara sus datos como campos final, los recibe en un constructor con parámetros con nombre y describe su aspecto en el método build.',
    sub='Cuatro partes, siempre en este orden. Todos tus componentes van a tener esta forma.',
    file='lib/components/stat_card.dart',
    panel='LAS CUATRO PARTES',
    code=[
        "class StatCard extends StatelessWidget {",
        "  final String number;",
        "  final String label;",
        "",
        "  const StatCard({",
        "    super.key,",
        "    required this.number,",
        "    required this.label,",
        "  });",
        "",
        "  @override",
        "  Widget build(BuildContext context) {",
        "    return Column(",
        "      children: [",
        "        Text(number),",
        "        Text(label),",
        "      ],",
        "    );",
        "  }",
        "}",
    ],
    result=(note(16, 'indigo', '1 · Es un StatelessWidget', ['Un widget sin estado: recibe datos y los', 'muestra. No cambia por su cuenta.'], 68)
            + note(96, 'amber', '2 · Sus datos', ['Campos final: llegan de afuera y no se', 'modifican. Son lo que cambia entre usos.'], 68)
            + note(176, 'green', '3 · El constructor', ['Así se le entregan los datos, por nombre.', 'required obliga a pasarlos.'], 68)
            + note(256, 'violet', '4 · build', ['Describe cómo se ve, usando sus datos.', 'Devuelve otros widgets.'], 68)),
    arrows=[
        dict(line=0, find='extends StatelessWidget', to=(16, 50), color='indigo', lane=2),
        dict(line=1, find='final String number;', to=(16, 130), color='amber', lane=1),
        dict(line=4, find='const StatCard({', to=(16, 210), color='green', lane=0),
        dict(line=11, find='Widget build(BuildContext context)', to=(16, 290), color='violet', lane=0),
    ],
))

FIGS['swUso'] = lambda: frame(dict(
    id='swUso',
    title='Un componente, tres usos',
    title_plain='Un componente, tres usos',
    desc='Una Row con tres StatCard, cada una con su number y su label. A la derecha, las tres tarjetas dibujadas, cada una señalada desde la línea de código que la crea.',
    sub='Tu componente se usa como cualquier widget de Flutter. Cada línea produce una tarjeta distinta.',
    file='lib/screens/home_screen.dart',
    min_h=252,
    code=[
        "Row(",
        "  children: [",
        "    StatCard(number: '128', label: 'Publicaciones'),",
        "    StatCard(number: '2.4k', label: 'Seguidores'),",
        "    StatCard(number: '310', label: 'Seguidos'),",
        "  ],",
        ")",
    ],
    result=(stat(24, 56, '128', 'Publicaciones', 'amber') + stat(132, 56, '2.4k', 'Seguidores', 'green')
            + stat(240, 56, '310', 'Seguidos', 'violet')),
    arrows=[
        dict(line=2, find="StatCard(number: '128', label: 'Publicaciones')", via=[(72, 152)], to=(72, 132), color='amber', lane=2),
        dict(line=3, find="StatCard(number: '2.4k', label: 'Seguidores')", via=[(180, 166)], to=(180, 132), color='green', lane=1),
        dict(line=4, find="StatCard(number: '310', label: 'Seguidos')", via=[(288, 180)], to=(288, 132), color='violet', lane=0),
    ],
))


# ───────────────────────────── S0016 · Column y S0017 · Row


def chip(x, y, w, text, color='indigo', h=24):
    soft, border, strong = FAM[color]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{soft}" stroke="{border}" stroke-width="1.5"/>'
            f'<text x="{x + w/2}" y="{y + h/2}" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="600" fill="{strong}">{text}</text>')


FIGS['clAnatomia'] = lambda: frame(dict(
    id='clAnatomia',
    title='Las partes de una <tspan class="mono">Column</tspan>',
    title_plain='Las partes de una Column',
    desc='Una Column con mainAxisAlignment center, crossAxisAlignment start y tres Text como children. A la derecha, los tres textos apilados dentro del espacio de la columna, con el eje principal vertical y el eje cruzado horizontal señalados.',
    sub='children es la lista de widgets que apila. Las otras dos propiedades dicen dónde quedan dentro de su espacio.',
    file='lib/main.dart',
    min_h=312,
    code=[
        "Column(",
        "  mainAxisAlignment: MainAxisAlignment.center,",
        "  crossAxisAlignment: CrossAxisAlignment.start,",
        "  children: [",
        "    Text('Ana Torres'),",
        "    Text('Estudiante'),",
        "    Text('Cali'),",
        "  ],",
        ")",
    ],
    result=('<rect x="130" y="88" width="160" height="176" rx="8" fill="#FBFBFD" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>'
            + chip(138, 132, 96, 'Ana Torres') + chip(138, 164, 92, 'Estudiante') + chip(138, 196, 48, 'Cali')
            + '<path d="M130,71 H288" stroke="#3A8235" stroke-width="1.75" marker-end="url(#clAnatomia-ar-green)"/>'
            '<text x="210" y="63" text-anchor="middle" font-size="11.5" font-weight="700" fill="#3A8235">eje cruzado</text>'
            '<path d="M312,92 V262" stroke="#A96C05" stroke-width="1.75" marker-end="url(#clAnatomia-ar-amber)"/>'
            '<text x="330" y="176" text-anchor="middle" font-size="11.5" font-weight="700" fill="#A96C05" transform="rotate(90 330 176)">eje principal</text>'),
    arrows=[
        dict(line=1, find='mainAxisAlignment: MainAxisAlignment.center', to=(312, 88), end='v', color='amber'),
        dict(line=2, find='crossAxisAlignment: CrossAxisAlignment.start', to=(126, 71), color='green'),
        dict(line=3, find='children', to=(134, 176), color='indigo', lane=0),
    ],
))

FIGS['rwAnatomia'] = lambda: frame(dict(
    id='rwAnatomia',
    title='Las partes de una <tspan class="mono">Row</tspan>',
    title_plain='Las partes de una Row',
    desc='Una Row con mainAxisAlignment center, crossAxisAlignment center y tres widgets como children: un icono y dos textos. A la derecha, los tres en fila dentro del espacio de la fila, con el eje principal horizontal y el eje cruzado vertical señalados.',
    sub='Es una Column acostada: las mismas propiedades, con los ejes cambiados.',
    file='lib/main.dart',
    min_h=300,
    code=[
        "Row(",
        "  mainAxisAlignment: MainAxisAlignment.center,",
        "  crossAxisAlignment: CrossAxisAlignment.center,",
        "  children: [",
        "    Icon(Icons.star),",
        "    Text('4.8'),",
        "    Text('(120 reseñas)'),",
        "  ],",
        ")",
    ],
    result=('<path d="M52,47 H326" stroke="#A96C05" stroke-width="1.75" marker-end="url(#rwAnatomia-ar-amber)"/>'
            '<text x="190" y="66" text-anchor="middle" font-size="11.5" font-weight="700" fill="#A96C05">eje principal</text>'
            '<rect x="52" y="96" width="276" height="80" rx="8" fill="#FBFBFD" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>'
            '<path d="M32,98 V174" stroke="#3A8235" stroke-width="1.75" marker-end="url(#rwAnatomia-ar-green)"/>'
            '<text x="18" y="136" text-anchor="middle" font-size="11.5" font-weight="700" fill="#3A8235" transform="rotate(-90 18 136)">eje cruzado</text>'
            '<path d="M106,125 l3.5,7.5 l8,1 l-6,5.5 l1.5,8 l-7,-4 l-7,4 l1.5,-8 l-6,-5.5 l8,-1 Z" fill="#F7C948" stroke="#A96C05" stroke-width="1.25"/>'
            + chip(126, 124, 44, '4.8') + chip(178, 124, 108, '(120 reseñas)')),
    arrows=[
        dict(line=1, find='mainAxisAlignment: MainAxisAlignment.center', to=(48, 47), color='amber'),
        dict(line=2, find='crossAxisAlignment: CrossAxisAlignment.center', to=(32, 94), end='v', color='green'),
        dict(line=3, find='children', via=[(190, 204)], to=(190, 180), color='indigo', lane=0),
    ],
))


def spread(extent, sizes, mode, gap=6):
    total = sum(sizes)
    n = len(sizes)
    free = extent - total
    if mode == 'start':
        pos, step = 0, gap
    elif mode == 'end':
        pos, step = free - gap * (n - 1), gap
    elif mode == 'center':
        pos, step = (free - gap * (n - 1)) / 2, gap
    elif mode == 'spaceBetween':
        pos, step = 0, free / (n - 1)
    else:
        pos, step = free / (n + 1), free / (n + 1)
    out = []
    for sz in sizes:
        out.append(pos)
        pos += sz + step
    return out


def across(extent, size, mode):
    return {'start': (0, size), 'center': ((extent - size) / 2, size), 'end': (extent - size, size), 'stretch': (0, extent)}[mode]


MAIN = ['start', 'center', 'end', 'spaceBetween', 'spaceEvenly']
CROSS = ['start', 'center', 'end', 'stretch']
BLOCKS = ['indigo', 'violet', 'teal']


def cl_alineacion():
    fid = 'clAlineacion'
    h = 644
    s = head(fid, h, 'Dónde quedan los hijos de una <tspan class="mono">Column</tspan>', 'Dónde quedan los hijos de una Column',
             'Cada caja punteada es el espacio de la misma columna. Solo cambia la propiedad.',
             'Los valores de MainAxisAlignment en una Column: start, center, end, spaceBetween y spaceEvenly reparten los hijos a lo alto. Los valores de CrossAxisAlignment: start, center, end y stretch los ubican a lo ancho.')
    widths = [56, 88, 40]

    def box(x, y, name, main, cross):
        soft_w, bw, bh = 136, 136, 168
        o = f'  <g transform="translate({x},{y})">\n'
        o += f'    <rect width="{bw}" height="{bh}" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>\n'
        ys = spread(bh - 16, [22] * 3, main)
        for (w, c, yy) in zip(widths, BLOCKS, ys):
            xx, ww = across(bw - 16, w, cross)
            soft, border, _ = FAM[c]
            o += f'    <rect x="{8 + xx:.0f}" y="{8 + yy:.0f}" width="{ww:.0f}" height="22" rx="5" fill="{soft}" stroke="{border}" stroke-width="1.5"/>\n'
        o += f'    <text class="mono" x="{bw/2}" y="{bh + 22}" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="{bw + 30}">{name}</text>\n'
        o += '  </g>\n'
        return o

    s += '  <text class="h" x="48" y="124" fill="#A96C05">mainAxisAlignment · A LO ALTO</text>\n'
    for i, m in enumerate(MAIN):
        s += box(48 + i * 182, 140, m, m, 'center')
    s += '  <text class="h" x="48" y="372" fill="#3A8235">crossAxisAlignment · A LO ANCHO</text>\n'
    for i, c in enumerate(CROSS):
        s += box(48 + i * 182, 388, c, 'start', c)
    s += f'  <text class="foot" x="48" y="{h-28}" data-fit="860">Los valores por defecto son start a lo alto y center a lo ancho.</text>\n</svg>\n'
    return s


FIGS['clAlineacion'] = cl_alineacion


def rw_alineacion():
    fid = 'rwAlineacion'
    h = 560
    s = head(fid, h, 'Dónde quedan los hijos de una <tspan class="mono">Row</tspan>', 'Dónde quedan los hijos de una Row',
             'Cada caja punteada es el espacio de la misma fila. Solo cambia la propiedad.',
             'Los valores de MainAxisAlignment en una Row: start, center, end, spaceBetween y spaceEvenly reparten los hijos a lo ancho. Los valores de CrossAxisAlignment: start, center, end y stretch los ubican a lo alto.')
    heights = [20, 40, 28]

    def strip(x, y, name, main, cross, sh):
        sw = 408
        o = f'  <g transform="translate({x},{y})">\n'
        o += f'    <rect width="{sw - 150}" height="{sh}" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>\n'
        xs = spread(sw - 150 - 16, [44] * 3, main)
        for (bh, c, xx) in zip(heights, BLOCKS, xs):
            yy, hh = across(sh - 16, bh, cross)
            soft, border, _ = FAM[c]
            o += f'    <rect x="{8 + xx:.0f}" y="{8 + yy:.0f}" width="44" height="{hh:.0f}" rx="5" fill="{soft}" stroke="{border}" stroke-width="1.5"/>\n'
        o += f'    <text class="mono" x="{sw-134}" y="{sh/2}" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" data-fit="130">{name}</text>\n'
        o += '  </g>\n'
        return o

    s += '  <text class="h" x="48" y="124" fill="#A96C05">mainAxisAlignment · A LO ANCHO</text>\n'
    for i, m in enumerate(MAIN):
        s += strip(48, 140 + i * 72, m, m, 'center', 56)
    s += '  <text class="h" x="504" y="124" fill="#3A8235">crossAxisAlignment · A LO ALTO</text>\n'
    for i, c in enumerate(CROSS):
        s += strip(504, 140 + i * 90, c, 'start', c, 72)
    s += f'  <text class="foot" x="48" y="{h-28}" data-fit="860">Los valores por defecto son start a lo ancho y center a lo alto.</text>\n</svg>\n'
    return s


FIGS['rwAlineacion'] = rw_alineacion


# ───────────────────────────── S0018 · Taller

def tl_contacto():
    fid = 'tlContacto'
    h = 372
    s = head(fid, h, 'Contacto sugerido', 'Contacto sugerido',
             'Tu componente es una sola de estas tarjetas. La fila que se desliza hacia los lados se arma en la sesión 3.',
             'Una sección de contactos sugeridos con una fila de tarjetas pequeñas, cada una con una foto circular, un nombre y un usuario. La fila continúa más allá del borde derecho. La primera tarjeta está resaltada: es el componente que se construye.')
    people = [('Ana Torres', '@anatorres', 'indigo'), ('Luis Peña', '@luisp', 'teal'), ('Sofía Ruiz', '@sofiaruiz', 'rose'),
              ('Javier Montes', '@javimontes', 'amber'), ('Mariana Vale…', '@marianav', 'violet'), ('Camilo Díaz', '@camilod', 'green'),
              ('Laura Gómez', '@laurag', 'indigo'), ('Pedro Cano', '@pedroc', 'teal')]
    s += f'  <clipPath id="{fid}-clip"><rect x="48" y="112" width="864" height="196" rx="12"/></clipPath>\n'
    s += '  <rect x="48" y="112" width="864" height="196" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>\n'
    s += '  <text x="72" y="146" font-size="16" font-weight="700" fill="#161A26" data-fit="300">Contactos sugeridos</text>\n'
    s += f'  <g clip-path="url(#{fid}-clip)">\n'
    for i, (name, user, color) in enumerate(people):
        soft, border, strong = FAM[color]
        x = 72 + i * 116
        s += f'    <g transform="translate({x},168)">\n'
        if i == 0:
            s += '      <rect x="-6" y="-8" width="108" height="132" rx="10" fill="none" stroke="#F2C069" stroke-width="2.5"/>\n'
        s += f'      <circle cx="48" cy="32" r="30" fill="{soft}" stroke="{border}" stroke-width="1.5"/>\n'
        s += f'      <circle cx="48" cy="24" r="10" fill="{border}"/><path d="M28,54 a20,17 0 0 1 40,0 Z" fill="{border}"/>\n'
        s += f'      <text x="48" y="88" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="110">{name}</text>\n'
        s += f'      <text x="48" y="108" text-anchor="middle" font-size="12" fill="#79809A" data-fit="110">{user}</text>\n'
        s += '    </g>\n'
    s += '  </g>\n'
    s += '  <path d="M844,146 H884 M876,140 L884,146 L876,152" fill="none" stroke="#79809A" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>\n'
    s += '  <text x="832" y="146" dy="0.35em" text-anchor="end" font-size="12" fill="#79809A" data-fit="140">se desliza</text>\n'
    s += f'  <text class="foot" x="48" y="{h-28}" data-fit="860">Todas las tarjetas miden lo mismo de ancho, y un nombre que no cabe termina en puntos suspensivos.</text>\n</svg>\n'
    return s


def tl_boton():
    fid = 'tlBoton'
    h = 292
    s = head(fid, h, 'Botón principal y botón secundario', 'Botón principal y botón secundario',
             'La misma estructura en los dos: un icono y un texto en fila. Cambia el tipo de botón.',
             'Dos botones a todo el ancho con un icono y un texto centrados. El principal, PrimaryButton, es azul con el contenido blanco y dice Iniciar sesión. El secundario, SecondaryButton, es blanco con borde y contenido azules y dice Crear cuenta.')
    login = ('<path d="M-9,0 H3 M-1,-4 L3,0 L-1,4" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
             '<path d="M2,-8 H8 V8 H2" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    person = ('<circle cx="-2" cy="-4" r="3.5" fill="none" stroke="{c}" stroke-width="2"/>'
              '<path d="M-9,8 a7,6 0 0 1 14,0" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"/>'
              '<path d="M7,-5 V1 M4,-2 H10" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"/>')
    items = [('PrimaryButton', 'Iniciar sesión', login, '#2196F3', 'none', '#FFFFFF', ["label: 'Iniciar sesión'", 'icon: Icons.login'], 146),
             ('SecondaryButton', 'Crear cuenta', person, '#FFFFFF', '#2196F3', '#1976D2', ["label: 'Crear cuenta'", 'icon: Icons.person_add_outlined'], 150)]
    for i, (cls, label, icon, fill, stroke, ink, note, ix) in enumerate(items):
        x = 48 + i * 456
        s += f'  <g transform="translate({x},112)">\n'
        s += f'    <text class="mono" x="0" y="12" font-size="14" font-weight="700" fill="#161A26" data-fit="408">{cls}</text>\n'
        s += '    <rect y="28" width="408" height="84" rx="12" fill="#EFF1F5"/>\n'
        s += f'    <rect x="24" y="48" width="360" height="44" rx="22" fill="{fill}" stroke="{stroke}" stroke-width="1.75"/>\n'
        s += f'    <g transform="translate({ix},70)">{icon.format(c=ink)}</g>\n'
        s += f'    <text x="{ix + 20}" y="70" dy="0.35em" font-size="15" font-weight="600" fill="{ink}" data-fit="200">{label}</text>\n'
        for k, ln in enumerate(note):
            s += f'    <text class="mono" x="0" y="{136 + k*20}" font-size="12" fill="#556074" data-fit="408">{ln}</text>\n'
        s += '  </g>\n'
    s += '</svg>\n'
    return s


FIGS['tlContacto'] = tl_contacto
FIGS['tlBoton'] = tl_boton


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--inject':
        done = set()
        for path in sorted((ROOT / 'content').glob('lessonS1[0-8].md')):
            text = path.read_text(encoding='utf-8')

            def swap(m):
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
