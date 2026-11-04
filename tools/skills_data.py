"""Copia las skills de tools/skills/ al diagrama interactivo skill-files (sección IA, S0063).

    python3 tools/skills_data.py      reescribe el bloque SKILLS de skillSims.js

Las skills se editan en tools/skills/<nombre>/ y se vuelve a correr este script. El orden de
SKILLS y los textos de cada pestaña (resumen, pedidos de ejemplo, lo que escribe) viven aquí.
mer-svg y flutter-pantallas son copia de recursos/sesion4/.agents/skills/ (sesión 4).

Cada skill tiene un grupo: 'base' (las cuatro de S0063, lo que muestra `skill-files` sin
opciones) o 'sdd' (las cinco de Spec Driven Development, sesión 10: `skill-files sdd`).
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
    dict(name='sdd-prd', group='sdd', color='#4453C9', soft='#EEF1FF',
         summary='Te entrevista sobre el proyecto en rondas cortas y escribe el PRD: el problema, '
                 'los usuarios, los objetivos medibles y lo que queda fuera del alcance.',
         prompts=['Mi proyecto se trata de…'],
         writes=['docs/prd.md']),
    dict(name='sdd-requisitos', group='sdd', color='#0F8478', soft='#E3F6F3',
         summary='Lee el PRD y saca los requisitos funcionales y no funcionales, numerados, '
                 'verificables y ligados al objetivo que atienden.',
         prompts=['Crea los requerimientos'],
         writes=['docs/requisitos.md']),
    dict(name='sdd-arquitectura', group='sdd', color='#A96C05', soft='#FFF3DC',
         summary='Escribe la architectural spine: resumen, diagrama mermaid, stack, qué cubre cada '
                 'servicio de Supabase y las invariantes que nadie del equipo puede decidir distinto.',
         prompts=['Mi app está en Flutter y se conecta a Supabase… especifica la arquitectura'],
         writes=['docs/architectural_spine.md']),
    dict(name='sdd-specs', group='sdd', color='#7439B8', soft='#F4EBFF',
         summary='Propone la lista de funcionalidades y escribe una spec funcional por cada una, '
                 'con metadatos, flujos, estados y criterios de aceptación, más el índice.',
         prompts=['Crea las specs funcionales'],
         writes=['docs/specs/F-xx-*.md', 'docs/specs/README.md']),
    dict(name='sdd-critica', group='sdd', color='#C2354F', soft='#FFEBEF',
         summary='Revisa todo el conjunto sin cambiarlo, calcula las métricas y propone las '
                 'correcciones más importantes. Solo las aplica si le dices que sí.',
         prompts=['Critica las specs'],
         writes=['docs/specs/reporte.md']),
]


def files(name):
    base = SRC / name
    paths = sorted((p for p in base.rglob('*') if p.is_file()),
                   key=lambda p: (p.name != 'SKILL.md', str(p.relative_to(base))))
    return [dict(path=str(p.relative_to(base)), content=p.read_text(encoding='utf-8')) for p in paths]


def main():
    skills = [dict({'group': 'base'}, **m, files=files(m['name'])) for m in META]
    block = '// <skills-data>\nexport const SKILLS = ' + json.dumps(skills, ensure_ascii=False, indent=2) + ';\n// </skills-data>'
    text = SIM.read_text(encoding='utf-8')
    SIM.write_text(re.sub(r'// <skills-data>.*?// </skills-data>', lambda _: block, text, flags=re.S), encoding='utf-8')
    print('skills:', ', '.join(f"{s['name']} ({len(s['files'])})" for s in skills))


if __name__ == '__main__':
    main()
