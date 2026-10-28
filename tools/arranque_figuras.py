"""Figuras SVG de las lecciones «Repositorio de arranque» (S0056 a S0062, sesiones 2 a 8).

    python3 tools/arranque_figuras.py <carpeta>     escribe un .svg por figura, para revisarlas
    python3 tools/arranque_figuras.py --inject      reemplaza cada bloque ```svg de esas lecciones
                                                    por la figura con el mismo id

Una figura por sesión: clonar su repositorio, bajar dependencias y correrlo en Chrome.
"""

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from console_frame import frame  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SESSIONS = range(2, 9)
LESSONS = [f'lessonS{54 + n}.md' for n in SESSIONS]

FIGS = {}


def clone(n):
    repo = f'262SeminarioSesion{n}'
    url = f'https://github.com/Domiciano/{repo}.git'
    return frame(dict(
        id=f'raClonar{n}',
        title=f'Clonar el repositorio de la sesión {n}',
        title_plain=f'Clonar el repositorio de la sesión {n}',
        desc=f'Una terminal parada en la carpeta develop. Primero git clone con la dirección de {repo}, que '
             f'crea la carpeta {repo}. Después cd {repo}, flutter pub get, que termina con Got dependencies, '
             'y flutter run -d chrome, que abre la app en Chrome. Tres recuadros numerados señalan la dirección '
             'del repositorio, flutter pub get y flutter run, cada uno con su tarjeta debajo.',
        sub='Cuatro comandos, desde la carpeta donde guardas tus proyectos.',
        term_title='Terminal · C:\\develop',
        lines=[
            ('P', f'git clone {url}', 'develop'),
            ('O', f"Cloning into '{repo}'..."),
            ('B', ''),
            ('P', f'cd {repo}', 'develop'),
            ('P', 'flutter pub get', repo),
            ('D', 'Resolving dependencies...'),
            ('K', 'Got dependencies!'),
            ('B', ''),
            ('P', 'flutter run -d chrome', repo),
            ('D', 'Launching lib/main.dart on Chrome in debug mode...'),
        ],
        rings=[
            (0, 9 + len('git clone '), len(url), 1),
            (4, len(repo) + 2, len('flutter pub get'), 2),
            (8, len(repo) + 2, len('flutter run -d chrome'), 3),
        ],
        cards=[
            (1, 'La dirección', ['Copia el proyecto en una', 'carpeta nueva con su nombre.'], False),
            (2, 'flutter pub get', ['Baja los paquetes. Sin él,', 'el editor marca errores.'], False),
            (3, 'flutter run', ['Abre la app en Chrome. Si', 'la ves, ya puedes empezar.'], False),
        ],
    ))


for _n in SESSIONS:
    FIGS[f'raClonar{_n}'] = (lambda n: lambda: clone(n))(_n)


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
