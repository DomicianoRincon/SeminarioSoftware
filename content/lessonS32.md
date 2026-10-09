# Taller · Tu primera skill

<!-- tags: taller de skills, skill mer-svg, diagrama MER en SVG, docs/modelo.md, references/estilo.md, assets/ejemplo.svg, el agente no encuentra la skill, el diagrama sale desordenado, corregir la skill y no el SVG, diagrama entidad relación, Entrega 1 -->

Vas a armar una skill que dibuja el **diagrama MER** de tu app, el mismo que pide la Entrega 1, a partir de una lista de tablas escrita en texto.

```svg
<svg id="tsFlujo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 348" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tsFlujo-ttl tsFlujo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tsFlujo-ttl">Lo que vas a armar</title>
  <desc id="tsFlujo-dsc">Tres cajas en fila. docs/modelo.md, las tablas de tu app en texto, que escribes tú. La skill mer-svg, con las medidas, los colores y un ejemplo, que el agente lee. Y docs/mer.svg, el diagrama, que escribe el agente.</desc>
  <defs>
    <style>
      #tsFlujo .title{fill:#161A26;font-size:22px;font-weight:700}
      #tsFlujo .sub{fill:#79809A;font-size:13.5px}
      #tsFlujo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tsFlujo .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tsFlujo .nb{fill:#454C61;font-size:13px}
      #tsFlujo .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tsFlujo .foot{fill:#79809A;font-size:12px}
      #tsFlujo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tsFlujo .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tsFlujo-arrow)}
    </style>
    <marker id="tsFlujo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="348" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Lo que vas a armar</text>
  <text class="sub" x="48" y="80" data-fit="860">Tú escribes las tablas en texto y la skill. El agente escribe el diagrama.</text>
  <rect x="48" y="124" width="240" height="116" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="68" y="158" font-size="15" font-weight="700" fill="#A96C05" text-anchor="start" class="mono" data-fit="200">docs/modelo.md</text>
  <text x="68" y="188" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="200">Tus tablas, en texto.</text>
  <text x="68" y="212" font-size="13" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="200">Lo escribes tú.</text>
  <rect x="360" y="124" width="240" height="116" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="380" y="158" font-size="15" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="200">mer-svg</text>
  <text x="380" y="188" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="200">Medidas, colores y un ejemplo.</text>
  <text x="380" y="212" font-size="13" font-weight="700" fill="#7439B8" text-anchor="start" data-fit="200">La armas tú, una vez.</text>
  <rect x="672" y="124" width="240" height="116" rx="12" fill="#E3F6F3" stroke="#0F8478" stroke-width="2.5"/>
  <text x="692" y="158" font-size="15" font-weight="700" fill="#0F8478" text-anchor="start" class="mono" data-fit="200">docs/mer.svg</text>
  <text x="692" y="188" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="200">El diagrama.</text>
  <text x="692" y="212" font-size="13" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="200">Lo escribe el agente.</text>
  <path class="link" d="M288,182 H352"/>
  <path class="link" d="M600,182 H664"/>
  <text x="320" y="170" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">lee</text>
  <text x="632" y="170" font-size="12" font-weight="600" fill="#556074" text-anchor="middle">escribe</text>
  <rect x="48" y="264" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="290" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">Si el diagrama sale mal,</tspan> se corrige el modelo o la skill y se pide otra vez. El SVG no se toca a mano.</text>
</svg>
```

## Antes de empezar

Necesitas, de las lecciones anteriores:

- OpenCode abierto dentro de `miapp1`, con un modelo gratuito elegido.
- `opencode.json` y `AGENTS.md` en la raíz del proyecto.
- `docs/modelo.md` con las tablas de **tu** app. Si todavía tienes el de la biblioteca, cámbialo ahora: es lo que hace que el diagrama sea el de tu entrega.

## 1. Crea la carpeta de la skill

Desde VS Code, crea dentro de `miapp1` las carpetas `.agents/skills/mer-svg/`, y dentro de `mer-svg` las carpetas `references` y `assets`. El punto inicial de `.agents` es parte del nombre.

## 2. SKILL.md

Crea `.agents/skills/mer-svg/SKILL.md` con este contenido:

```markdown
---
name: mer-svg
description: Dibuja el diagrama entidad-relación (MER) de la app como un archivo SVG, a partir de docs/modelo.md. Úsala cuando pidan el MER, el diagrama de base de datos, el diagrama entidad-relación o "dibuja el modelo de datos".
---

# MER en SVG

Escribes el SVG a mano, como código. No uses Mermaid ni ninguna librería.

## Pasos

1. Lee `docs/modelo.md`. Es la única fuente: no agregues ni quites tablas o atributos.
2. Lee `references/estilo.md`. Trae las medidas, los colores y cómo se dibuja cada relación.
3. Lee `assets/ejemplo.svg`. Es un diagrama terminado: el tuyo debe verse igual.
4. Ordena las tablas para que las que se relacionan queden vecinas.
5. Calcula la posición de cada tabla con las medidas de `references/estilo.md` antes de escribir.
6. Escribe el resultado en `docs/mer.svg`.
7. Revisa: cada tabla y cada atributo de `docs/modelo.md` está en el SVG, y cada relación tiene su línea.

## Reglas

- El texto en SVG no se parte solo: una línea por `<text>`.
- Fondo claro fijo. Sin modo oscuro, sin imágenes y sin enlaces externos.
- Los nombres de tablas y atributos van igual que en `docs/modelo.md`.
- Si una relación no cabe entre tablas vecinas, cambia el orden de las tablas. No cruces líneas sobre una tabla.
```

Lee los pasos antes de seguir: son las instrucciones que el agente va a obedecer. El paso 7 hace que revise su propio trabajo.

## 3. references/estilo.md

Aquí está lo que hace que el diagrama se vea bien: medidas exactas en vez de "hazlo bonito". Crea `.agents/skills/mer-svg/references/estilo.md`:

```markdown
# Estilo del MER

## Lienzo

- `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 ALTO" role="img">`, con `<title>` y `<desc>`.
- Fondo: `<rect width="960" height="ALTO" rx="16" fill="#FBFBFD"/>`.
- Título en x=32, y=44, 20 px, negrita, color `#161A26`. Subtítulo en x=32, y=66, 13 px, color `#79809A`.
- Fuente del texto: `ui-sans-serif, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif`.
- Fuente de tablas y atributos: `ui-monospace, Menlo, Consolas, monospace`, 13 px, color `#161A26`.

## Rejilla

- Cuatro columnas. La x de cada tabla es 32, 272, 512 o 752. Todas miden 176 de ancho.
- La primera fila de tablas empieza en y=88.
- Si hay más de cuatro tablas, la siguiente fila empieza 64 px debajo de la tabla más alta de la fila anterior.
- ALTO = donde termina la última fila + 48.

## Una tabla

Para una tabla en (X, Y) con N atributos:

- Alto = 40 + 28 × N.
- Caja: `<rect x="X" y="Y" width="176" height="ALTO_TABLA" rx="10" stroke-width="1.5"/>` con el relleno y el borde de su color.
- Nombre: centrado en x = X + 88, y = Y + 21, negrita, 14 px, con el color fuerte.
- Línea bajo el nombre: de (X, Y + 32) a (X + 176, Y + 32), con el color del borde.
- El atributo número i (el primero es 0) va centrado en y = Y + 46 + 28 × i, con `dy="0.35em"`, en x = X + 46.
- Insignia PK o FK, a la izquierda del atributo: `<rect x="X+10" y="centro-9" width="26" height="18" rx="9"/>` y encima el texto `PK` o `FK` en blanco, 10.5 px, negrita, centrado en x = X + 23.
  - PK: relleno con el color fuerte de la tabla.
  - FK: relleno `#556074`.

## Colores

Un color por tabla, en este orden. Si hay más de cuatro tablas, se repiten.

- Azul: relleno `#EEF1FF`, borde `#A9B4F2`, fuerte `#4453C9`.
- Verde: relleno `#E3F6F3`, borde `#86D3CA`, fuerte `#0F8478`.
- Ámbar: relleno `#FFF3DC`, borde `#F0C572`, fuerte `#A96C05`.
- Morado: relleno `#F4EBFF`, borde `#C9A6EE`, fuerte `#7439B8`.

## Relaciones

Todas las líneas: `fill="none" stroke="#556074" stroke-width="1.75"`.

Entre dos tablas vecinas de la misma fila, la línea es horizontal y va a 76 px del borde de arriba (LY = Y + 76). Sea A el borde derecho de la tabla de la izquierda y B el borde izquierdo de la tabla de la derecha (B = A + 64).

- Línea: `M A,LY H B`.
- Lado "uno": una barra vertical a 14 px de la tabla. Si el "uno" está a la izquierda: `M A+14,LY-9 V LY+9`. Si está a la derecha: `M B-14,LY-9 V LY+9`.
- Lado "muchos": una pata de gallo de 24 px que se abre hacia la tabla. Si el "muchos" está a la derecha: `M B-24,LY L B,LY-11 M B-24,LY L B,LY M B-24,LY L B,LY+11`. Si está a la izquierda: `M A+24,LY L A,LY-11 M A+24,LY L A,LY M A+24,LY L A,LY+11`.
- Sobre la línea, a 18 px por encima, un `1` cerca del lado uno y una `N` cerca del lado muchos: 13 px, negrita, color `#556074`.

Entre una tabla y la que está justo debajo, la línea es vertical por el centro de la columna (x = X + 88), desde el borde inferior de la de arriba hasta el borde superior de la de abajo, con la barra y la pata de gallo giradas.

## Pie

Una línea de texto bajo las tablas, 12.5 px, color `#79809A`, que dice cómo se leen las relaciones.
```

## 4. assets/ejemplo.svg

Un diagrama terminado, para que el agente vea cómo se ve uno bien hecho. Es el de la biblioteca de la Entrega 1. Crea `.agents/skills/mer-svg/assets/ejemplo.svg`:

```xml
<svg id="erEjemplo" viewBox="0 0 960 320" role="img" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
<title id="erEjemplo-t">Ejemplo de diagrama entidad-relación</title>
<desc id="erEjemplo-d">Cuatro tablas de una biblioteca: categorias, libros, prestamos y usuarios, con relaciones uno a muchos.</desc>
<style>
#erEjemplo .mono{font-family:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace;font-size:13px;fill:#161A26}
#erEjemplo .nt{font-size:14px;font-weight:700}
#erEjemplo .lk{fill:none;stroke:#556074;stroke-width:1.75}
#erEjemplo .card{stroke-width:1.5}
#erEjemplo .bd{font-size:10.5px;font-weight:700;fill:#fff;letter-spacing:.04em}
#erEjemplo .card-t{font-size:13px;font-weight:700;fill:#161A26}
#erEjemplo .card-b{font-size:12px;fill:#454C61}
#erEjemplo .ca{font-size:13px;font-weight:700;fill:#556074}
</style>
<rect width="960" height="320" rx="16" fill="#FBFBFD"/>
<text x="32" y="44" font-size="20" font-weight="700" fill="#161A26">Ejemplo: biblioteca de préstamos</text>
<text x="32" y="66" font-size="13" fill="#79809A">Cada caja es una tabla; cada línea, una relación entre dos tablas.</text>
<g><rect class="card" x="32" y="88" width="176" height="152" rx="10" fill="#EEF1FF" stroke="#A9B4F2"/>
<path d="M32,120 H208" stroke="#A9B4F2" stroke-width="1.5"/>
<text class="nt mono" x="120" y="109" text-anchor="middle" fill="#4453C9" style="fill:#4453C9;font-size:14px">categorias</text>
<rect x="42" y="125" width="26" height="18" rx="9" fill="#4453C9"/><text class="bd" x="55" y="134" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="78" y="134" dy="0.35em">id</text>
<text class="mono" x="78" y="162" dy="0.35em">nombre</text>
<text class="mono" x="78" y="190" dy="0.35em">descripcion</text>
</g>
<g><rect class="card" x="272" y="88" width="176" height="152" rx="10" fill="#E3F6F3" stroke="#86D3CA"/>
<path d="M272,120 H448" stroke="#86D3CA" stroke-width="1.5"/>
<text class="nt mono" x="360" y="109" text-anchor="middle" fill="#0F8478" style="fill:#0F8478;font-size:14px">libros</text>
<rect x="282" y="125" width="26" height="18" rx="9" fill="#0F8478"/><text class="bd" x="295" y="134" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="318" y="134" dy="0.35em">id</text>
<text class="mono" x="318" y="162" dy="0.35em">titulo</text>
<text class="mono" x="318" y="190" dy="0.35em">autor</text>
<rect x="282" y="209" width="26" height="18" rx="9" fill="#556074"/><text class="bd" x="295" y="218" text-anchor="middle" dy="0.35em">FK</text>
<text class="mono" x="318" y="218" dy="0.35em">categoria_id</text>
</g>
<g><rect class="card" x="512" y="88" width="176" height="152" rx="10" fill="#FFF3DC" stroke="#F0C572"/>
<path d="M512,120 H688" stroke="#F0C572" stroke-width="1.5"/>
<text class="nt mono" x="600" y="109" text-anchor="middle" fill="#A96C05" style="fill:#A96C05;font-size:14px">prestamos</text>
<rect x="522" y="125" width="26" height="18" rx="9" fill="#A96C05"/><text class="bd" x="535" y="134" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="558" y="134" dy="0.35em">id</text>
<rect x="522" y="153" width="26" height="18" rx="9" fill="#556074"/><text class="bd" x="535" y="162" text-anchor="middle" dy="0.35em">FK</text>
<text class="mono" x="558" y="162" dy="0.35em">libro_id</text>
<rect x="522" y="181" width="26" height="18" rx="9" fill="#556074"/><text class="bd" x="535" y="190" text-anchor="middle" dy="0.35em">FK</text>
<text class="mono" x="558" y="190" dy="0.35em">usuario_id</text>
<text class="mono" x="558" y="218" dy="0.35em">fecha_prestamo</text>
</g>
<g><rect class="card" x="752" y="88" width="176" height="152" rx="10" fill="#F4EBFF" stroke="#C9A6EE"/>
<path d="M752,120 H928" stroke="#C9A6EE" stroke-width="1.5"/>
<text class="nt mono" x="840" y="109" text-anchor="middle" fill="#7439B8" style="fill:#7439B8;font-size:14px">usuarios</text>
<rect x="762" y="125" width="26" height="18" rx="9" fill="#7439B8"/><text class="bd" x="775" y="134" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="798" y="134" dy="0.35em">id</text>
<text class="mono" x="798" y="162" dy="0.35em">nombre</text>
<text class="mono" x="798" y="190" dy="0.35em">correo</text>
</g>
<path class="lk" d="M208,164 H272"/><path class="lk" d="M222,155 V173"/><path class="lk" d="M248,164 L272,153 M248,164 L272,164 M248,164 L272,175"/>
<path class="lk" d="M448,164 H512"/><path class="lk" d="M462,155 V173"/><path class="lk" d="M488,164 L512,153 M488,164 L512,164 M488,164 L512,175"/>
<path class="lk" d="M688,164 H752"/><path class="lk" d="M712,164 L688,153 M712,164 L688,164 M712,164 L688,175"/><path class="lk" d="M738,155 V173"/>
<text class="ca" x="220" y="146" text-anchor="middle">1</text>
<text class="ca" x="260" y="146" text-anchor="middle">N</text>
<text class="ca" x="460" y="146" text-anchor="middle">1</text>
<text class="ca" x="500" y="146" text-anchor="middle">N</text>
<text class="ca" x="700" y="146" text-anchor="middle">N</text>
<text class="ca" x="740" y="146" text-anchor="middle">1</text>
<text x="32" y="284" font-size="12.5" fill="#79809A">Se lee así: una categoría tiene muchos libros · un libro se presta muchas veces · un usuario hace muchos préstamos.</text>
</svg>
```

Ábrelo en Chrome para comprobar que se ve: arrastra el archivo a una pestaña.

## 5. Pide el diagrama

Cierra OpenCode y ábrelo de nuevo, para que encuentre la skill. Luego pídelo sin nombrarla:

```svg
<svg id="tsUso" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 564" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tsUso-ttl tsUso-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tsUso-ttl">Pedir el diagrama</title>
  <desc id="tsUso-dsc">Se le pide al agente que dibuje el MER de la app. El agente carga la skill mer-svg, lee docs/modelo.md, el estilo y el ejemplo de la skill, y escribe docs/mer.svg.</desc>
  <defs>
    <style>
      #tsUso .title{fill:#161A26;font-size:22px;font-weight:700}
      #tsUso .sub{fill:#79809A;font-size:13.5px}
      #tsUso .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tsUso .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #tsUso .pf{fill:#7F8AA3} #tsUso .cmd{fill:#FFFFFF;font-weight:600}
      #tsUso .dim{fill:#8A93A6} #tsUso .okk{fill:#6BCB77;font-weight:600}
      #tsUso .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #tsUso .chipc{fill:#F2C069} #tsUso .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #tsUso .ct{fill:#161A26;font-size:14px;font-weight:700}
      #tsUso .cb{fill:#454C61;font-size:13px}
      #tsUso .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="564" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Pedir el diagrama</text>
  <text class="sub" x="48" y="80" data-fit="860">El pedido no nombra la skill. El agente la elige por su description.</text>
  <rect x="48" y="112" width="864" height="294" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\miapp1</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816">&gt; Dibuja el MER de la app</text>
  <text class="tl mono" font-size="13" x="72" y="226" data-fit="816">→ Skill "mer-svg"</text>
  <text class="tl mono dim" font-size="13" x="72" y="252" data-fit="816">→ Read docs/modelo.md</text>
  <text class="tl mono dim" font-size="13" x="72" y="278" data-fit="816">→ Read .agents/skills/mer-svg/references/estilo.md</text>
  <text class="tl mono dim" font-size="13" x="72" y="304" data-fit="816">→ Read .agents/skills/mer-svg/assets/ejemplo.svg</text>
  <text class="tl mono" font-size="13" x="72" y="330" data-fit="816">← Write docs/mer.svg</text>
  <text class="tl mono okk" font-size="13" x="72" y="382" data-fit="816">Listo: docs/mer.svg con 6 tablas y 5 relaciones.</text>
  <rect class="ring" x="68.0" y="210" width="140.6" height="22" rx="5"/>
  <circle class="chipc" cx="208.6" cy="211" r="8"/>
  <text class="chipt" x="208.6" y="211" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="68.0" y="262" width="398.0" height="22" rx="5"/>
  <circle class="chipc" cx="466.0" cy="263" r="8"/>
  <text class="chipt" x="466.0" y="263" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <rect class="ring" x="68.0" y="314" width="164.0" height="22" rx="5"/>
  <circle class="chipc" cx="232.0" cy="315" r="8"/>
  <text class="chipt" x="232.0" y="315" dy="0.35em" text-anchor="middle" font-size="10.5">3</text>
  <g transform="translate(48.0,430)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">Eligió la skill</text>
    <text class="cb" x="16" y="60" data-fit="245">La encontró por su</text>
    <text class="cb" x="16" y="79" data-fit="245">description.</text>
  </g>
  <g transform="translate(341.3,430)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">Leyó lo que la skill pide</text>
    <text class="cb" x="16" y="60" data-fit="245">El modelo, el estilo</text>
    <text class="cb" x="16" y="79" data-fit="245">y el ejemplo.</text>
  </g>
  <g transform="translate(634.7,430)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">3</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">Escribió el archivo</text>
    <text class="cb" x="16" y="60" data-fit="245">Ábrelo en Chrome</text>
    <text class="cb" x="16" y="79" data-fit="245">para verlo.</text>
  </g>
</svg>
```

Con un modelo gratuito tarda **entre tres y cinco minutos**. Mientras tanto, lee qué archivos va abriendo.

Cuando termine, abre `docs/mer.svg` en Chrome. Este es el resultado de un modelo gratuito con una app de reserva de canchas, sin retoques:

```svg
<svg id="tsResultado" width="100%" style="max-width:960px;display:block;margin:0 auto" viewBox="0 0 960 560" role="img" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
<title id="tsResultado-t">MER de la app</title>
<desc id="tsResultado-d">Seis tablas: sedes, canchas, deportes, usuarios, reservas y pagos, con relaciones uno a muchos.</desc>
<style>
#tsResultado .mono{font-family:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace;font-size:13px;fill:#161A26}
#tsResultado .nt{font-size:14px;font-weight:700}
#tsResultado .lk{fill:none;stroke:#556074;stroke-width:1.75}
#tsResultado .card{stroke-width:1.5}
#tsResultado .bd{font-size:10.5px;font-weight:700;fill:#fff;letter-spacing:.04em}
#tsResultado .ca{font-size:13px;font-weight:700;fill:#556074}
</style>
<rect width="960" height="560" rx="16" fill="#FBFBFD"/>
<text x="32" y="44" font-size="20" font-weight="700" fill="#161A26">MER: reserva de canchas</text>
<text x="32" y="66" font-size="13" fill="#79809A">Cada caja es una tabla; cada línea, una relación entre dos tablas.</text>

<g><rect class="card" x="32" y="88" width="176" height="124" rx="10" fill="#EEF1FF" stroke="#A9B4F2"/>
<path d="M32,120 H208" stroke="#A9B4F2" stroke-width="1.5"/>
<text class="nt mono" x="120" y="109" text-anchor="middle" style="fill:#4453C9;font-size:14px">sedes</text>
<rect x="42" y="125" width="26" height="18" rx="9" fill="#4453C9"/><text class="bd" x="55" y="134" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="78" y="134" dy="0.35em">id</text>
<text class="mono" x="78" y="162" dy="0.35em">nombre</text>
<text class="mono" x="78" y="190" dy="0.35em">direccion</text>
</g>

<g><rect class="card" x="272" y="88" width="176" height="180" rx="10" fill="#E3F6F3" stroke="#86D3CA"/>
<path d="M272,120 H448" stroke="#86D3CA" stroke-width="1.5"/>
<text class="nt mono" x="360" y="109" text-anchor="middle" style="fill:#0F8478;font-size:14px">canchas</text>
<rect x="282" y="125" width="26" height="18" rx="9" fill="#0F8478"/><text class="bd" x="295" y="134" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="318" y="134" dy="0.35em">id</text>
<text class="mono" x="318" y="162" dy="0.35em">nombre</text>
<text class="mono" x="318" y="190" dy="0.35em">precio_hora</text>
<rect x="282" y="209" width="26" height="18" rx="9" fill="#556074"/><text class="bd" x="295" y="218" text-anchor="middle" dy="0.35em">FK</text>
<text class="mono" x="318" y="218" dy="0.35em">sede_id</text>
<rect x="282" y="237" width="26" height="18" rx="9" fill="#556074"/><text class="bd" x="295" y="246" text-anchor="middle" dy="0.35em">FK</text>
<text class="mono" x="318" y="246" dy="0.35em">deporte_id</text>
</g>

<g><rect class="card" x="512" y="88" width="176" height="96" rx="10" fill="#FFF3DC" stroke="#F0C572"/>
<path d="M512,120 H688" stroke="#F0C572" stroke-width="1.5"/>
<text class="nt mono" x="600" y="109" text-anchor="middle" style="fill:#A96C05;font-size:14px">deportes</text>
<rect x="522" y="125" width="26" height="18" rx="9" fill="#A96C05"/><text class="bd" x="535" y="134" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="558" y="134" dy="0.35em">id</text>
<text class="mono" x="558" y="162" dy="0.35em">nombre</text>
</g>

<g><rect class="card" x="32" y="332" width="176" height="152" rx="10" fill="#F4EBFF" stroke="#C9A6EE"/>
<path d="M32,364 H208" stroke="#C9A6EE" stroke-width="1.5"/>
<text class="nt mono" x="120" y="353" text-anchor="middle" style="fill:#7439B8;font-size:14px">usuarios</text>
<rect x="42" y="369" width="26" height="18" rx="9" fill="#7439B8"/><text class="bd" x="55" y="378" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="78" y="378" dy="0.35em">id</text>
<text class="mono" x="78" y="406" dy="0.35em">nombre</text>
<text class="mono" x="78" y="434" dy="0.35em">correo</text>
<text class="mono" x="78" y="462" dy="0.35em">telefono</text>
</g>

<g><rect class="card" x="272" y="332" width="176" height="180" rx="10" fill="#EEF1FF" stroke="#A9B4F2"/>
<path d="M272,364 H448" stroke="#A9B4F2" stroke-width="1.5"/>
<text class="nt mono" x="360" y="353" text-anchor="middle" style="fill:#4453C9;font-size:14px">reservas</text>
<rect x="282" y="369" width="26" height="18" rx="9" fill="#4453C9"/><text class="bd" x="295" y="378" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="318" y="378" dy="0.35em">id</text>
<rect x="282" y="397" width="26" height="18" rx="9" fill="#556074"/><text class="bd" x="295" y="406" text-anchor="middle" dy="0.35em">FK</text>
<text class="mono" x="318" y="406" dy="0.35em">cancha_id</text>
<rect x="282" y="425" width="26" height="18" rx="9" fill="#556074"/><text class="bd" x="295" y="434" text-anchor="middle" dy="0.35em">FK</text>
<text class="mono" x="318" y="434" dy="0.35em">usuario_id</text>
<text class="mono" x="318" y="462" dy="0.35em">fecha</text>
<text class="mono" x="318" y="490" dy="0.35em">hora_inicio</text>
</g>

<g><rect class="card" x="512" y="332" width="176" height="152" rx="10" fill="#E3F6F3" stroke="#86D3CA"/>
<path d="M512,364 H688" stroke="#86D3CA" stroke-width="1.5"/>
<text class="nt mono" x="600" y="353" text-anchor="middle" style="fill:#0F8478;font-size:14px">pagos</text>
<rect x="522" y="369" width="26" height="18" rx="9" fill="#0F8478"/><text class="bd" x="535" y="378" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="558" y="378" dy="0.35em">id</text>
<rect x="522" y="397" width="26" height="18" rx="9" fill="#556074"/><text class="bd" x="535" y="406" text-anchor="middle" dy="0.35em">FK</text>
<text class="mono" x="558" y="406" dy="0.35em">reserva_id</text>
<text class="mono" x="558" y="434" dy="0.35em">valor</text>
<text class="mono" x="558" y="462" dy="0.35em">metodo</text>
</g>

<path class="lk" d="M208,164 H272"/><path class="lk" d="M222,155 V173"/><path class="lk" d="M248,164 L272,153 M248,164 L272,164 M248,164 L272,175"/>
<text class="ca" x="220" y="146" text-anchor="middle">1</text>
<text class="ca" x="260" y="146" text-anchor="middle">N</text>

<path class="lk" d="M448,164 H512"/><path class="lk" d="M498,155 V173"/><path class="lk" d="M472,164 L448,153 M472,164 L448,164 M472,164 L448,175"/>
<text class="ca" x="500" y="146" text-anchor="middle">1</text>
<text class="ca" x="460" y="146" text-anchor="middle">N</text>

<path class="lk" d="M360,268 V332"/><path class="lk" d="M351,282 H369"/><path class="lk" d="M360,308 L349,332 M360,308 L360,332 M360,308 L371,332"/>
<text class="ca" x="378" y="287" text-anchor="middle">1</text>
<text class="ca" x="378" y="326" text-anchor="middle">N</text>

<path class="lk" d="M208,408 H272"/><path class="lk" d="M222,399 V417"/><path class="lk" d="M248,408 L272,397 M248,408 L272,408 M248,408 L272,419"/>
<text class="ca" x="220" y="390" text-anchor="middle">1</text>
<text class="ca" x="260" y="390" text-anchor="middle">N</text>

<path class="lk" d="M448,408 H512"/><path class="lk" d="M462,399 V417"/><path class="lk" d="M488,408 L512,397 M488,408 L512,408 M488,408 L512,419"/>
<text class="ca" x="460" y="390" text-anchor="middle">1</text>
<text class="ca" x="500" y="390" text-anchor="middle">N</text>

<text x="32" y="544" font-size="12.5" fill="#79809A">Se lee así: sede→canchas, deporte→canchas, cancha→reservas, usuario→reservas y reserva→pagos; siempre del uno a los muchos.</text>
</svg>
```

## 6. Revísalo

Compara el diagrama con `docs/modelo.md`, tabla por tabla:

- ¿Están todas las tablas y todos los atributos?
- ¿Cada llave tiene su insignia, PK o FK?
- ¿Cada relación tiene su línea, con el `1` y la `N` del lado correcto?
- ¿Alguna línea pasa por encima de una tabla?

## 7. Si sale mal, corrige la skill

No edites el SVG a mano: la próxima vez saldría mal otra vez. Busca de dónde viene el error.

- **Falta una tabla o un atributo.** Revisa `docs/modelo.md`: casi siempre el error está ahí.
- **El agente no usó la skill.** Revisa que `name` sea igual al nombre de la carpeta y que la `description` diga cuándo se usa.
- **Las tablas se montan o las líneas se cruzan.** Agrega una regla a `SKILL.md` o una medida a `references/estilo.md`, y pide el diagrama otra vez.
- **Quieres otros colores u otro título.** Cámbialos en `references/estilo.md`.

Es la misma idea del archivo de contexto: lo que se va a repetir se corrige en las instrucciones, no en el resultado.

## Qué debes tener al terminar

```svg
<svg id="tsCarpetas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 600" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tsCarpetas-ttl tsCarpetas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tsCarpetas-ttl">Tu proyecto al terminar</title>
  <desc id="tsCarpetas-dsc">El árbol de miapp1 al terminar el taller. Son nuevos la carpeta .agents con la skill mer-svg y sus tres archivos, SKILL.md, estilo.md y ejemplo.svg; la carpeta docs con modelo.md y mer.svg; y en la raíz AGENTS.md y opencode.json. La carpeta lib queda igual.</desc>
  <defs>
    <style>
      #tsCarpetas .title{fill:#161A26;font-size:22px;font-weight:700}
      #tsCarpetas .sub{fill:#79809A;font-size:13.5px}
      #tsCarpetas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tsCarpetas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tsCarpetas .nb{fill:#454C61;font-size:13px}
      #tsCarpetas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tsCarpetas .foot{fill:#79809A;font-size:12px}
      #tsCarpetas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tsCarpetas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tsCarpetas-arrow)}
    </style>
    <marker id="tsCarpetas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="600" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Tu proyecto al terminar</text>
  <text class="sub" x="48" y="80" data-fit="860">Nada de lib/ cambió. Lo nuevo es lo que dirige al agente y lo que el agente produjo.</text>
  <path d="M64,132 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="98" y="145" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">miapp1/</text>
  <path d="M76,150 V174 H98" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M104,166 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="138" y="179" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">.agents/</text>
  <path d="M116,184 V208 H138" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M144,200 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="178" y="213" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">skills/</text>
  <path d="M156,218 V242 H178" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M184,234 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="218" y="247" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">mer-svg/</text>
  <path d="M196,252 V276 H218" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M228,267 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="258" y="281" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">SKILL.md</text>
  <rect x="520" y="266" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="548" y="281" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M196,252 V310 H218" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M228,301 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="258" y="315" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">references/estilo.md</text>
  <rect x="520" y="300" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="548" y="315" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M196,252 V344 H218" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M228,335 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="258" y="349" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">assets/ejemplo.svg</text>
  <rect x="520" y="334" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="548" y="349" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M76,150 V378 H98" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M104,370 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="138" y="383" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">docs/</text>
  <path d="M116,388 V412 H138" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M148,403 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="178" y="417" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">modelo.md</text>
  <rect x="520" y="402" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="548" y="417" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M116,388 V446 H138" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M148,437 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="178" y="451" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">mer.svg</text>
  <rect x="520" y="436" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="548" y="451" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M76,150 V480 H98" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M104,472 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="138" y="485" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">lib/</text>
  <path d="M76,150 V514 H98" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M108,505 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="138" y="519" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">AGENTS.md</text>
  <rect x="520" y="504" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="548" y="519" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M76,150 V548 H98" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M108,539 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="138" y="553" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">opencode.json</text>
  <rect x="520" y="538" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="548" y="553" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <text x="184" y="485" font-size="12.5" font-weight="400" fill="#79809A" text-anchor="start">sin cambios</text>
</svg>
```

- `AGENTS.md` con los seis apartados y el contexto de tu app.
- `docs/modelo.md` con tus tablas.
- La skill `mer-svg` con sus tres archivos.
- `docs/mer.svg`, revisado contra el modelo.

Lleva todo al repositorio de tu equipo. El `docs/mer.svg` sirve como diagrama de base de datos de la **Entrega 1**. En la próxima sesión usas el agente para generar una pantalla y la auditas contra tu `AGENTS.md`.
