"""Copia las skills de tools/skills/ al diagrama interactivo skill-files (sección IA, S0063).

    python3 tools/skills_data.py      reescribe el bloque SKILLS de skillSims.js

Las skills se editan en tools/skills/<nombre>/ y se vuelve a correr este script. El orden de
SKILLS y los textos de cada pestaña (resumen, pedidos de ejemplo, lo que escribe) viven aquí.
mer-svg y flutter-pantallas son copia de recursos/sesion4/.agents/skills/ (sesión 4).
"""

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'tools' / 'skills'
SIM = ROOT / 'classnotesapp' / 'src' / 'components' / 'interactive' / 'skillSims.js'

META = [
    dict(name='disenador-bd', color='#4453C9', soft='#EEF1FF',
         summary='Te entrevista sobre la app, arma un borrador de tablas y lo normaliza paso a paso: 1FN, '
                 '2FN y 3FN, mostrando qué rompe cada regla y pidiendo tu visto bueno antes de seguir.',
         prompts=['Ayúdame a diseñar la base de datos de mi app',
                  'Lleva docs/modelo.md a tercera forma normal'],
         writes=['docs/modelo.md']),
    dict(name='mer-svg', color='#0F8478', soft='#E3F6F3',
         summary='Dibuja el diagrama entidad-relación de docs/modelo.md como un SVG escrito a mano, con '
                 'una rejilla, un color por tabla y patas de gallo en las relaciones. La armaste en la sesión 4.',
         prompts=['Dibuja el MER de la app'],
         writes=['docs/mer.svg']),
    dict(name='flutter-pantallas', color='#A96C05', soft='#FFF3DC',
         summary='Maqueta pantallas estáticas con la paleta mínima de widgets y componentes reutilizables. '
                 'Sin estado ni navegación: sirve para el prototipo. La viste en la sesión 4.',
         prompts=['Maqueta la pantalla de perfil'],
         writes=['lib/screens/', 'lib/components/']),
    dict(name='flutter-componentes', color='#7439B8', soft='#F4EBFF',
         summary='Crea y conecta componentes como en las sesiones 6 a 8: datos por el constructor, '
                 'eventos con Function(), copyWith en el modelo y el estado y el Navigator solo en la Screen.',
         prompts=['Saca la tarjeta de producto a un componente',
                  'Haz que tocar la card abra el detalle'],
         writes=['lib/components/', 'lib/models/']),
]


def files(name):
    base = SRC / name
    paths = sorted((p for p in base.rglob('*') if p.is_file()),
                   key=lambda p: (p.name != 'SKILL.md', str(p.relative_to(base))))
    return [dict(path=str(p.relative_to(base)), content=p.read_text(encoding='utf-8')) for p in paths]


def main():
    skills = [dict(m, files=files(m['name'])) for m in META]
    block = '// <skills-data>\nexport const SKILLS = ' + json.dumps(skills, ensure_ascii=False, indent=2) + ';\n// </skills-data>'
    text = SIM.read_text(encoding='utf-8')
    SIM.write_text(re.sub(r'// <skills-data>.*?// </skills-data>', lambda _: block, text, flags=re.S), encoding='utf-8')
    print('skills:', ', '.join(f"{s['name']} ({len(s['files'])})" for s in skills))


if __name__ == '__main__':
    main()
