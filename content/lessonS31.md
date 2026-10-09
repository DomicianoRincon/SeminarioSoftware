# Skills

<!-- tags: skill, SKILL.md, .agents/skills, name y description, references y assets, scripts de una skill, cuándo se carga una skill, el agente no usa mi skill, skill de proyecto y skill global, AGENTS.md o skill, frontmatter, carpeta de la skill -->

`AGENTS.md` viaja en cada pedido, así que tiene que ser corto. Pero hay tareas que necesitan instrucciones largas y solo de vez en cuando: dibujar un diagrama, escribir un tipo de documento, seguir una lista de revisión. Eso va en una **skill**.

## Una skill es una carpeta

```svg
<svg id="skCarpeta" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 692" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="skCarpeta-ttl skCarpeta-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="skCarpeta-ttl">Una skill es una carpeta</title>
  <desc id="skCarpeta-dsc">El árbol de carpetas de mi_app_1: dentro de .agents y skills está la carpeta mer-svg, que es la skill. Adentro tiene el archivo SKILL.md, obligatorio, con las instrucciones; la carpeta references con estilo.md, lo que el agente consulta; la carpeta assets con ejemplo.svg, lo que el agente imita; y, atenuada porque esta skill no la usa, la carpeta scripts con tres programas de ejemplo que el agente ejecutaría: render.sh, render.bat y check.py.</desc>
  <defs>
    <style>
      #skCarpeta .title{fill:#161A26;font-size:22px;font-weight:700}
      #skCarpeta .sub{fill:#79809A;font-size:13.5px}
      #skCarpeta .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #skCarpeta .nt{font-size:15px;font-weight:700;fill:#161A26}
      #skCarpeta .nb{fill:#454C61;font-size:13px}
      #skCarpeta .lbl{fill:#556074;font-size:12px;font-weight:600}
      #skCarpeta .foot{fill:#79809A;font-size:12px}
      #skCarpeta .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #skCarpeta .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#skCarpeta-arrow)}
    </style>
    <marker id="skCarpeta-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="692" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Una skill es una carpeta</text>
  <text class="sub" x="48" y="80" data-fit="860">Vive dentro del proyecto, en .agents/skills/. El nombre de la carpeta es el nombre de la skill.</text>
  <path d="M64,132 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="98" y="145" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">mi_app_1/</text>
  <path d="M76,150 V182 H98" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M104,174 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="138" y="187" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">.agents/</text>
  <path d="M116,192 V224 H138" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M144,216 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="178" y="229" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">skills/</text>
  <path d="M156,234 V266 H178" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M184,258 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="218" y="271" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">mer-svg/</text>
  <path d="M196,276 V308 H218" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M228,299 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="258" y="313" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">SKILL.md</text>
  <path d="M196,276 V350 H218" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M224,342 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="258" y="355" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">references/</text>
  <path d="M236,360 V392 H258" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M268,383 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="298" y="397" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">estilo.md</text>
  <path d="M196,276 V434 H218" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M224,426 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="258" y="439" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">assets/</text>
  <path d="M236,444 V476 H258" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M268,467 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="298" y="481" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">ejemplo.svg</text>
  <g opacity=".55"><path d="M196,276 V518 H218" fill="none" stroke="#C4CBD8" stroke-width="1.5"/><path d="M224,510 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/><text x="258" y="523" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">scripts/</text></g>
  <g opacity=".55"><path d="M236,528 V560 H258" fill="none" stroke="#C4CBD8" stroke-width="1.5"/><path d="M268,551 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="298" y="565" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">render.sh</text></g>
  <g opacity=".55"><path d="M236,528 V602 H258" fill="none" stroke="#C4CBD8" stroke-width="1.5"/><path d="M268,593 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="298" y="607" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">render.bat</text></g>
  <g opacity=".55"><path d="M236,528 V644 H258" fill="none" stroke="#C4CBD8" stroke-width="1.5"/><path d="M268,635 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="298" y="649" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">check.py</text></g>
  <path d="M297,266 H552" stroke="#C9A6EE" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>
  <rect x="552" y="248" width="360" height="36" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="570" y="270.5" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="330"><tspan font-weight="700" fill="#7439B8">La skill.</tspan> Se llama como su carpeta.</text>
  <path d="M337,308 H552" stroke="#A9B4F2" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>
  <rect x="552" y="290" width="360" height="36" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="570" y="312.5" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="330"><tspan font-weight="700" fill="#4453C9">Obligatorio.</tspan> Cuándo se usa y qué pasos sigue.</text>
  <path d="M363,350 H552" stroke="#86D3CA" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>
  <rect x="552" y="332" width="360" height="36" rx="10" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="570" y="354.5" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="330"><tspan font-weight="700" fill="#0F8478">Lo que consulta.</tspan> Medidas, colores y reglas.</text>
  <path d="M328,434 H552" stroke="#F0C572" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>
  <rect x="552" y="416" width="360" height="36" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="570" y="438.5" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="330"><tspan font-weight="700" fill="#A96C05">Lo que imita.</tspan> Un ejemplo terminado.</text>
  <path d="M337,518 H552" stroke="#C4CBD8" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>
  <rect x="552" y="500" width="360" height="36" rx="10" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 4"/>
  <text x="570" y="522.5" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="330"><tspan font-weight="700" fill="#556074">Lo que ejecuta.</tspan> Programas. Esta skill no los usa.</text>
  <text x="414" y="565" font-size="12.5" font-weight="400" fill="#79809A" text-anchor="start">macOS y Linux</text>
  <text x="414" y="607" font-size="12.5" font-weight="400" fill="#79809A" text-anchor="start">Windows</text>
  <text x="414" y="649" font-size="12.5" font-weight="400" fill="#79809A" text-anchor="start">Python, en cualquiera</text>
</svg>
```

Lo único obligatorio es `SKILL.md`. Las otras carpetas son una costumbre útil, y cada una guarda una cosa distinta:

- `references/`: lo que el agente **consulta**.
- `assets/`: lo que el agente **copia o imita**.
- `scripts/`: lo que el agente **ejecuta**.

La skill de esta sesión no lleva `scripts/`, pero conviene saber que existe. Un script sirve cuando un paso tiene que salir siempre igual y un programa lo hace mejor que el modelo: validar un archivo, convertir un SVG en imagen, contar algo. El `SKILL.md` le dice al agente cuándo correrlo, por ejemplo: "Al terminar, ejecuta `scripts/check.py docs/mer.svg`".

Un script es un archivo de texto con comandos, y su extensión dice quién lo corre: `.sh` en macOS y Linux, `.bat` en Windows y `.py` en cualquier equipo con Python. Si la skill la va a usar gente con sistemas distintos, o se escribe en Python o se incluyen el `.sh` y el `.bat`.

Como ejecutar un script es ejecutar un comando, el agente te pide permiso antes, igual que con `flutter analyze`.

## SKILL.md

```svg
<svg id="skSkillMd" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="skSkillMd-ttl skSkillMd-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="skSkillMd-ttl">Las partes de SKILL.md</title>
  <desc id="skSkillMd-dsc">El archivo SKILL.md empieza con un bloque entre dos líneas de tres guiones, con name y description. Después va el cuerpo en Markdown, con los pasos que sigue el agente.</desc>
  <defs>
    <style>
      #skSkillMd .title{fill:#161A26;font-size:22px;font-weight:700}
      #skSkillMd .sub{fill:#79809A;font-size:13.5px}
      #skSkillMd .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #skSkillMd .cl{font-size:13px;fill:#C9CFDA}
      #skSkillMd .s{fill:#A8D8A0} #skSkillMd .n{fill:#F2B880} #skSkillMd .c{fill:#7FD1E8}
      #skSkillMd .p{fill:#D5B8F5} #skSkillMd .k{fill:#F08FB0}
      #skSkillMd .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #skSkillMd .ct{fill:#161A26;font-size:14px;font-weight:700}
      #skSkillMd .cb{fill:#454C61;font-size:13px}
      #skSkillMd .rt{fill:#161A26;font-size:14px} #skSkillMd .rs{fill:#79809A;font-size:12px}
      #skSkillMd .foot{fill:#79809A;font-size:12px}
      #skSkillMd .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #skSkillMd .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #skSkillMd .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#skSkillMd-ar-amber)}
      #skSkillMd .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #skSkillMd .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #skSkillMd .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#skSkillMd-ar-indigo)}
      #skSkillMd .hl-teal{fill:#86D3CA;fill-opacity:.16;stroke:#86D3CA;stroke-width:1.5}
      #skSkillMd .ld-teal{fill:none;stroke:#86D3CA;stroke-width:1.5;stroke-dasharray:3 4}
      #skSkillMd .ar-teal{fill:none;stroke:#0F8478;stroke-width:1.75;marker-end:url(#skSkillMd-ar-teal)}
    </style>
    <marker id="skSkillMd-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="skSkillMd-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="skSkillMd-ar-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#0F8478"/></marker>
  </defs>
  <rect width="960" height="520" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las partes de <tspan class="mono">SKILL.md</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Arriba, entre las dos líneas de guiones, los datos de la skill. Debajo, las instrucciones.</text>
  <rect x="48" y="112" width="456" height="376" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">.agents/skills/mer-svg/SKILL.md</text>
  <rect x="552" y="112" width="360" height="376" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">QUÉ ES CADA PARTE</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="64.0" y="180" width="39.2" height="22" rx="5"/>
  <rect class="hl-amber" x="64.0" y="204" width="93.8" height="22" rx="5"/>
  <rect class="hl-teal" x="64.0" y="348" width="70.4" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="23.4" lengthAdjust="spacingAndGlyphs" data-fit="432">---</text>
  <text class="cl mono" font-size="13" x="68.0" y="196" textLength="101.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">name</tspan>: mer-svg</text>
  <text class="cl mono" font-size="13" x="68.0" y="220" textLength="343.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">description</tspan>: <tspan class="c">Dibuja</tspan> el <tspan class="c">MER</tspan> de la app en <tspan class="c">SVG</tspan>.</text>
  <text class="cl mono" font-size="13" x="83.6" y="244" textLength="312.0" lengthAdjust="spacingAndGlyphs" data-fit="432">Úsala cuando pidan el diagrama de datos.</text>
  <text class="cl mono" font-size="13" x="68.0" y="268" textLength="23.4" lengthAdjust="spacingAndGlyphs" data-fit="432">---</text>
  <text class="cl mono" font-size="13" x="68.0" y="316" textLength="93.6" lengthAdjust="spacingAndGlyphs" data-fit="432"># <tspan class="c">MER</tspan> en <tspan class="c">SVG</tspan></text>
  <text class="cl mono" font-size="13" x="68.0" y="364" textLength="62.4" lengthAdjust="spacingAndGlyphs" data-fit="432">## <tspan class="c">Pasos</tspan></text>
  <text class="cl mono" font-size="13" x="68.0" y="412" textLength="171.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="n">1</tspan>. <tspan class="c">Lee</tspan> docs/modelo.md.</text>
  <text class="cl mono" font-size="13" x="68.0" y="436" textLength="218.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="n">2</tspan>. <tspan class="c">Lee</tspan> references/estilo.md.</text>
  <text class="cl mono" font-size="13" x="68.0" y="460" textLength="312.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="n">3</tspan>. <tspan class="c">Escribe</tspan> el resultado en docs/mer.svg.</text>
  <g transform="translate(552,144)">
<g transform="translate(16,16)"><rect width="328" height="68" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#4453C9" data-fit="300">name</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Igual al nombre de la carpeta.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">Minúsculas y guiones.</text></g><g transform="translate(16,100)"><rect width="328" height="68" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#A96C05" data-fit="300">description</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Qué hace y cuándo usarla.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">El agente decide con esto.</text></g><g transform="translate(16,212)"><rect width="328" height="68" rx="10" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#0F8478" data-fit="300">El cuerpo</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Los pasos, en orden.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">Nombra los archivos que debe leer.</text></g>
  </g>
  <path class="ld-indigo" d="M175.4,191 H504"/>
  <path class="ar-indigo" d="M504,191 H514 V194 H568"/>
  <path class="ld-amber" d="M417.2,215 H504"/>
  <path class="ar-amber" d="M504,215 H523 V278 H568"/>
  <path class="ld-teal" d="M136.4,359 H504"/>
  <path class="ar-teal" d="M504,359 H514 V390 H568"/>
</svg>
```

```markdown
---
name: mer-svg
description: Dibuja el MER de la app en SVG. Úsala cuando pidan el diagrama de datos.
---

# MER en SVG

## Pasos

1. Lee docs/modelo.md.
2. Lee references/estilo.md.
3. Escribe el resultado en docs/mer.svg.
```

El bloque de arriba, entre las dos líneas de `---`, tiene dos datos obligatorios:

- `name`: en minúsculas, con guiones y **exactamente igual al nombre de la carpeta**. Si no coinciden, la skill no aparece.
- `description`: qué hace y cuándo se usa.

Debajo va el cuerpo, en Markdown normal: los pasos y las reglas, como se los explicarías a una persona que no conoce el proyecto.

## Cuándo se carga

```svg
<svg id="skCarga" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 396" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="skCarga-ttl skCarga-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="skCarga-ttl">El agente no lee toda la skill de entrada</title>
  <desc id="skCarga-dsc">Tres momentos. Uno, siempre: el agente tiene en su contexto el name y la description de cada skill instalada. Dos, cuando tu pedido coincide con una description: abre el SKILL.md de esa skill. Tres, solo si un paso lo pide: abre los archivos de references y assets.</desc>
  <defs>
    <style>
      #skCarga .title{fill:#161A26;font-size:22px;font-weight:700}
      #skCarga .sub{fill:#79809A;font-size:13.5px}
      #skCarga .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #skCarga .nt{font-size:15px;font-weight:700;fill:#161A26}
      #skCarga .nb{fill:#454C61;font-size:13px}
      #skCarga .lbl{fill:#556074;font-size:12px;font-weight:600}
      #skCarga .foot{fill:#79809A;font-size:12px}
      #skCarga .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #skCarga .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#skCarga-arrow)}
    </style>
    <marker id="skCarga-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="396" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">El agente no lee toda la skill de entrada</text>
  <text class="sub" x="48" y="80" data-fit="860">Carga cada parte solo cuando la necesita. Así una skill larga no gasta contexto si no se usa.</text>
  <rect x="48" y="120" width="272" height="168" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <circle cx="78" cy="150" r="11" fill="#556074"/><text x="78" y="154.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">1</text>
  <text x="100" y="155" font-size="14" font-weight="700" fill="#556074" text-anchor="start" data-fit="200">Siempre</text>
  <text x="68" y="198" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="236">name y description</text>
  <text x="68" y="228" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="236">De cada skill instalada.</text>
  <text x="68" y="248" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="236">Unas pocas líneas.</text>
  <path class="link" d="M320,204 H338"/>
  <rect x="344" y="120" width="272" height="168" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <circle cx="374" cy="150" r="11" fill="#7439B8"/><text x="374" y="154.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">2</text>
  <text x="396" y="155" font-size="14" font-weight="700" fill="#7439B8" text-anchor="start" data-fit="200">Si tu pedido coincide</text>
  <text x="364" y="198" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="236">SKILL.md</text>
  <text x="364" y="228" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="236">Los pasos y las reglas</text>
  <text x="364" y="248" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="236">de esa skill.</text>
  <path class="link" d="M616,204 H634"/>
  <rect x="640" y="120" width="272" height="168" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <circle cx="670" cy="150" r="11" fill="#0F8478"/><text x="670" y="154.5" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">3</text>
  <text x="692" y="155" font-size="14" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="200">Si un paso lo pide</text>
  <text x="660" y="198" font-size="15" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="236">references/ y assets/</text>
  <text x="660" y="228" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="236">El detalle y los ejemplos,</text>
  <text x="660" y="248" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="236">archivo por archivo.</text>
  <rect x="48" y="312" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="338" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">La description decide:</tspan> es lo único que el agente lee para saber si usa la skill.</text>
</svg>
```

Puedes tener veinte skills instaladas y el agente solo carga la que necesita. El costo fijo de cada una son las dos líneas de arriba.

## Una buena description

Si el agente no usa tu skill, casi siempre el problema está aquí. Una buena description:

- Dice **qué produce**: "Dibuja el MER de la app en SVG".
- Dice **cuándo se usa**, con las palabras que tú usarías al pedirlo: "cuando pidan el MER, el diagrama de base de datos, el diagrama entidad-relación".
- No es vaga. "Ayuda con diagramas" no le sirve para decidir.

## Dónde viven

- **En el proyecto**, en `.agents/skills/`. Se sube al repositorio y la tiene todo el equipo. Es la que usamos.
- **En tu equipo**, en la carpeta `.agents/skills/` de tu usuario. Queda disponible en todos tus proyectos, pero solo para ti.

OpenCode y Antigravity CLI leen las dos. OpenCode también lee `.opencode/skills/` y `.claude/skills/`.

## AGENTS.md o skill

- Si aplica a **todo** lo que el agente hace en el proyecto, va en `AGENTS.md`. Ejemplo: "imports con `package:`".
- Si aplica a **una tarea** que se repite, va en una skill. Ejemplo: cómo se dibuja un diagrama.
- Si es de **una sola vez**, no va en ninguno: se escribe en el pedido.
