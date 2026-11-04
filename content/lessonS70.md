# Anatomía de una spec

<!-- tags: anatomía de una spec, metadatos, frontmatter, versión semver, estado de la spec, criterios de aceptación, Dado cuando entonces, qué no va en una spec, docs/specs, índice de specs, la spec habla de widgets -->

Una spec es un archivo Markdown corto: arriba los metadatos, abajo el comportamiento.

## Las partes

```svg
<svg id="spAnatomia" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="spAnatomia-ttl spAnatomia-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="spAnatomia-ttl">Las partes de una spec</title>
  <desc id="spAnatomia-dsc">Un archivo F-03 a la izquierda con su encabezado de metadatos y sus apartados. A la derecha cuatro tarjetas: metadatos, comportamiento, cómo se comprueba y lo que falta, unidas a su parte del archivo.</desc>
  <defs>
    <style>
      #spAnatomia .title{fill:#161A26;font-size:22px;font-weight:700}
      #spAnatomia .sub{fill:#79809A;font-size:13.5px}
      #spAnatomia .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #spAnatomia .nt{font-size:15px;font-weight:700;fill:#161A26}
      #spAnatomia .nb{fill:#454C61;font-size:13px}
      #spAnatomia .lbl{fill:#556074;font-size:12px;font-weight:600}
      #spAnatomia .foot{fill:#79809A;font-size:12px}
      #spAnatomia .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #spAnatomia .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#spAnatomia-arrow)}
    </style>
    <marker id="spAnatomia-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="560" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las partes de una spec</text>
  <text class="sub" x="48" y="80" data-fit="860">Un archivo Markdown: arriba los metadatos, abajo el comportamiento.</text>
<rect x="48" y="116" width="420" height="408" rx="12" fill="#1F2430"/><text x="64" y="142" font-size="12" font-weight="400" fill="#9AA3B5" text-anchor="start" class="mono" data-fit="396">docs/specs/F-03-foto-de-perfil.md</text><text x="64" y="172" font-size="13" font-weight="400" fill="#79809A" text-anchor="start" class="mono" data-fit="396">---</text><text x="64" y="192" font-size="13" font-weight="400" fill="#7FD9A8" text-anchor="start" class="mono" data-fit="396">id: F-03</text><text x="64" y="212" font-size="13" font-weight="400" fill="#7FD9A8" text-anchor="start" class="mono" data-fit="396">titulo: Cambiar la foto de perfil</text><text x="64" y="232" font-size="13" font-weight="400" fill="#7FD9A8" text-anchor="start" class="mono" data-fit="396">version: 0.2.0</text><text x="64" y="252" font-size="13" font-weight="400" fill="#7FD9A8" text-anchor="start" class="mono" data-fit="396">fecha: 2026-11-04</text><text x="64" y="272" font-size="13" font-weight="400" fill="#7FD9A8" text-anchor="start" class="mono" data-fit="396">estado: borrador</text><text x="64" y="292" font-size="13" font-weight="400" fill="#7FD9A8" text-anchor="start" class="mono" data-fit="396">requisitos: [RF-07, RF-08]</text><text x="64" y="312" font-size="13" font-weight="400" fill="#79809A" text-anchor="start" class="mono" data-fit="396">---</text><text x="64" y="352" font-size="13" font-weight="700" fill="#E6EAF2" text-anchor="start" class="mono" data-fit="396"># F-03 · Cambiar la foto de perfil</text><text x="64" y="372" font-size="13" font-weight="400" fill="#A9B4F2" text-anchor="start" class="mono" data-fit="396">## Objetivo</text><text x="64" y="392" font-size="13" font-weight="400" fill="#A9B4F2" text-anchor="start" class="mono" data-fit="396">## Flujo principal</text><text x="64" y="412" font-size="13" font-weight="400" fill="#A9B4F2" text-anchor="start" class="mono" data-fit="396">## Reglas · ## Estados</text><text x="64" y="432" font-size="13" font-weight="400" fill="#F0C572" text-anchor="start" class="mono" data-fit="396">## Criterios de aceptación</text><text x="64" y="452" font-size="13" font-weight="400" fill="#F3A3B2" text-anchor="start" class="mono" data-fit="396">## Fuera de alcance</text><text x="64" y="472" font-size="13" font-weight="400" fill="#F3A3B2" text-anchor="start" class="mono" data-fit="396">## Preguntas abiertas</text><text x="64" y="492" font-size="13" font-weight="400" fill="#79809A" text-anchor="start" class="mono" data-fit="396">## Historial</text><rect x="54" y="156" width="408" height="168" rx="6" fill="none" stroke="#3A8235" stroke-width="2"/><rect x="54" y="357" width="408" height="60" rx="6" fill="none" stroke="#4453C9" stroke-width="2"/><rect x="54" y="418" width="408" height="20" rx="6" fill="none" stroke="#A96C05" stroke-width="2"/><rect x="54" y="439" width="408" height="40" rx="6" fill="none" stroke="#C2354F" stroke-width="2"/><g><rect x="508" y="116" width="404" height="100" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="524" y="148" font-size="14.5" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="380">Metadatos</text><text x="524" y="174" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">Qué spec es, de qué versión,</text><text x="524" y="193" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">de cuándo, en qué estado y</text><text x="524" y="212" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">qué requisitos cubre.</text></g><path d="M462,240.0 H488 V146 H506" fill="none" stroke="#3A8235" stroke-width="1.5"/><g><rect x="508" y="228" width="404" height="100" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="524" y="260" font-size="14.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="380">Comportamiento</text><text x="524" y="286" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">Para qué sirve, los pasos,</text><text x="524" y="305" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">las reglas y los estados</text><text x="524" y="324" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">de cargando, vacío y error.</text></g><path d="M462,387.0 H488 V258 H506" fill="none" stroke="#4453C9" stroke-width="1.5"/><g><rect x="508" y="340" width="404" height="84" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="524" y="372" font-size="14.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="380">Cómo se comprueba</text><text x="524" y="398" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">Criterios de aceptación:</text><text x="524" y="417" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">Dado… cuando… entonces…</text></g><path d="M462,428.0 H488 V370 H506" fill="none" stroke="#A96C05" stroke-width="1.5"/><g><rect x="508" y="436" width="404" height="84" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="524" y="468" font-size="14.5" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="380">Lo que falta</text><text x="524" y="494" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">Lo que no cubre y lo que</text><text x="524" y="513" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="380">el equipo no ha decidido.</text></g><path d="M462,459.0 H488 V466 H506" fill="none" stroke="#C2354F" stroke-width="1.5"/></svg>
```

## Los metadatos

Van entre dos líneas `---`, al inicio del archivo:

```yaml
---
id: F-03
titulo: Cambiar la foto de perfil
version: 0.2.0
fecha: 2026-11-04
estado: borrador
autores: [Ana, Luis]
requisitos: [RF-07, RF-08]
depende_de: [F-01]
---
```

- **id**: no cambia nunca, aunque cambie el título.
- **version** y **fecha**: cuál es la última y de cuándo.
- **estado**: en qué va (ver abajo).
- **requisitos**: los RF que cubre. Así se calcula la completitud.
- **depende_de**: otras specs que tienen que existir antes.

## Una spec de ejemplo

```markdown
# F-03 · Cambiar la foto de perfil

## Objetivo
El usuario cambia su foto para que lo reconozcan.

## Flujo principal
1. En su perfil, el usuario toca su foto.
2. Elige una imagen de su galería.
3. Ve la foto nueva en su perfil.

## Reglas
- La foto pesa máximo 5 MB.

## Estados
- Cargando: la foto anterior se ve atenuada.
- Error: «No se pudo subir la foto». La anterior se conserva.

## Criterios de aceptación
- CA-1 Dado una foto de 2 MB, cuando la elige,
  entonces la ve en su perfil.
- CA-2 Dado una foto de 8 MB, cuando la elige,
  entonces ve «La foto pesa demasiado».

## Fuera de alcance
- Recortar la foto.

## Preguntas abiertas
- ¿Se puede quitar la foto?

## Historial
- 0.2.0 · 2026-11-04 · CA-2 con el límite de 5 MB.
- 0.1.0 · 2026-11-04 · Primera versión.
```

## Los criterios, en Gherkin

Los criterios de aceptación son escenarios de Gherkin. Puedes escribirlos así dentro de la spec:

```gherkin
# language: es
Característica: Cambiar la foto de perfil

  Escenario: Foto dentro del límite
    Dado que el usuario está en su perfil
    Cuando elige una foto de 2 MB
    Entonces ve la foto nueva en su perfil

  Escenario: Foto demasiado pesada
    Dado que el usuario está en su perfil
    Cuando elige una foto de 8 MB
    Entonces ve el aviso «La foto pesa demasiado»
    Y su foto anterior se conserva
```

Cada `Entonces` describe algo que el usuario ve, no algo del código. Más adelante, cada escenario se convierte en una prueba.

## Qué sí y qué no

```svg
<svg id="spSiNo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="spSiNo-ttl spSiNo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="spSiNo-ttl">Qué sí va y qué no va en una spec</title>
  <desc id="spSiNo-dsc">Dos columnas. Sí va: actor y objetivo, flujos, reglas, estados, criterios de aceptación y preguntas abiertas. No va: código y widgets, tablas y SQL, colores y tamaños, tareas y palabras vagas.</desc>
  <defs>
    <style>
      #spSiNo .title{fill:#161A26;font-size:22px;font-weight:700}
      #spSiNo .sub{fill:#79809A;font-size:13.5px}
      #spSiNo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #spSiNo .nt{font-size:15px;font-weight:700;fill:#161A26}
      #spSiNo .nb{fill:#454C61;font-size:13px}
      #spSiNo .lbl{fill:#556074;font-size:12px;font-weight:600}
      #spSiNo .foot{fill:#79809A;font-size:12px}
      #spSiNo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #spSiNo .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#spSiNo-arrow)}
    </style>
    <marker id="spSiNo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="480" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Qué sí va y qué no va en una spec</text>
  <text class="sub" x="48" y="80" data-fit="860">Si describe lo que ve el usuario, va. Si describe cómo se construye, no.</text>
<text x="48" y="124" font-size="12.5" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="59">SÍ VA</text><rect x="48" y="138" width="420" height="40" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="62" y="163" font-size="13" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="150">Quién y para qué</text><text x="208" y="163" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">El usuario cambia su foto de perfil.</text><rect x="48" y="186" width="420" height="40" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="62" y="211" font-size="13" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="150">Los pasos</text><text x="208" y="211" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">1. Elige la foto. 2. La ve en su perfil.</text><rect x="48" y="234" width="420" height="40" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="62" y="259" font-size="13" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="150">Las reglas</text><text x="208" y="259" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">La foto pesa máximo 5 MB.</text><rect x="48" y="282" width="420" height="40" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="62" y="307" font-size="13" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="150">Los estados</text><text x="208" y="307" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">Error: «No se pudo subir la foto».</text><rect x="48" y="330" width="420" height="40" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="62" y="355" font-size="13" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="150">Criterios</text><text x="208" y="355" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">Dado… cuando… entonces…</text><rect x="48" y="378" width="420" height="40" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.2"/><text x="62" y="403" font-size="13" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="150">Lo que falta</text><text x="208" y="403" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">¿Se puede quitar la foto?</text><text x="492" y="124" font-size="12.5" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="59">NO VA</text><rect x="492" y="138" width="420" height="40" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="506" y="163" font-size="13" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="150">Código y widgets</text><text x="652" y="163" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">Un ElevatedButton con setState.</text><rect x="492" y="186" width="420" height="40" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="506" y="211" font-size="13" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="150">Tablas y SQL</text><text x="652" y="211" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">UPDATE usuarios SET foto_url…</text><rect x="492" y="234" width="420" height="40" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="506" y="259" font-size="13" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="150">Colores y tamaños</text><text x="652" y="259" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">Botón azul de 48 px.</text><rect x="492" y="282" width="420" height="40" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="506" y="307" font-size="13" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="150">Tareas</text><text x="652" y="307" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">Crear ProfileService.</text><rect x="492" y="330" width="420" height="40" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="506" y="355" font-size="13" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="150">Palabras vagas</text><text x="652" y="355" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">Que sea rápido e intuitivo.</text><rect x="492" y="378" width="420" height="40" rx="10" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="506" y="403" font-size="13" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="150">Tecnología</text><text x="652" y="403" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="250">Se sube a Supabase Storage.</text><text x="48" y="452" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Lo de la derecha no se pierde: va al prototipo, al modelo de datos, a la spec técnica o al plan.</text></svg>
```

La prueba rápida: ¿un usuario entendería esta línea? Si no, probablemente es del cómo.

## Versión y estado

```svg
<svg id="spVersiones" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 372" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="spVersiones-ttl spVersiones-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="spVersiones-ttl">Versión y estado</title>
  <desc id="spVersiones-dsc">Arriba, una versión 1.2.0 con sus tres números: mayor si cambia el comportamiento, menor si se agrega algo, parche si solo cambia la redacción. Abajo, los estados: borrador, aprobada e implementada, y obsoleta para la que ya no aplica.</desc>
  <defs>
    <style>
      #spVersiones .title{fill:#161A26;font-size:22px;font-weight:700}
      #spVersiones .sub{fill:#79809A;font-size:13.5px}
      #spVersiones .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #spVersiones .nt{font-size:15px;font-weight:700;fill:#161A26}
      #spVersiones .nb{fill:#454C61;font-size:13px}
      #spVersiones .lbl{fill:#556074;font-size:12px;font-weight:600}
      #spVersiones .foot{fill:#79809A;font-size:12px}
      #spVersiones .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #spVersiones .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#spVersiones-arrow)}
    </style>
    <marker id="spVersiones-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="372" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Versión y estado</text>
  <text class="sub" x="48" y="80" data-fit="860">Dos metadatos que dicen qué tan madura está la spec y si ya se construyó.</text>
<text x="48" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">VERSIÓN</text><rect x="48" y="140" width="272" height="76" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="82" y="192" font-size="34" font-weight="700" fill="#C2354F" text-anchor="middle" class="mono" data-fit="44">1</text><text x="116" y="170" font-size="14.5" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="196">Mayor</text><text x="116" y="194" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">Cambia el comportamiento.</text><rect x="344" y="140" width="272" height="76" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="378" y="192" font-size="34" font-weight="700" fill="#A96C05" text-anchor="middle" class="mono" data-fit="44">2</text><text x="412" y="170" font-size="14.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="196">Menor</text><text x="412" y="194" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">Se agrega algo.</text><rect x="640" y="140" width="272" height="76" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="674" y="192" font-size="34" font-weight="700" fill="#556074" text-anchor="middle" class="mono" data-fit="44">0</text><text x="708" y="170" font-size="14.5" font-weight="700" fill="#556074" text-anchor="start" data-fit="196">Parche</text><text x="708" y="194" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">Solo cambia la redacción.</text><text x="48" y="252" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="64">ESTADO</text><rect x="90.1" y="272" width="75.8" height="24" rx="12" fill="#556074" stroke="#556074" stroke-width="1.2"/><text x="128" y="288.5" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="77">borrador</text><text x="128" y="316" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="57">0.x.y</text><path class="link" d="M198,284 H286"/><rect x="322.1" y="272" width="75.8" height="24" rx="12" fill="#4453C9" stroke="#4453C9" stroke-width="1.2"/><text x="360" y="288.5" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="77">aprobada</text><text x="360" y="316" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="57">1.0.0</text><path class="link" d="M430,284 H518"/><rect x="540.7" y="272" width="102.6" height="24" rx="12" fill="#3A8235" stroke="#3A8235" stroke-width="1.2"/><text x="592" y="288.5" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="104">implementada</text><text x="592" y="316" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="104">en el código</text><path class="link" d="M700,284 H756" stroke-dasharray="5 5"/><rect x="778.1" y="272" width="75.8" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="816" y="288.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" data-fit="77">obsoleta</text><text x="816" y="316" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="104">ya no aplica</text></svg>
```

Cada cambio sube la versión, cambia la fecha y deja una línea en el *Historial*. El estado `implementada` es lo que dice qué ya está en el código.

## Dónde viven

```svg
<svg id="spCarpeta" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 448" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="spCarpeta-ttl spCarpeta-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="spCarpeta-ttl">Dónde viven las specs</title>
  <desc id="spCarpeta-dsc">Árbol de la carpeta docs con prd.md, requisitos.md, architectural_spine.md, modelo.md y la carpeta specs con README.md, tres specs F-01 a F-03 y reporte.md, cada uno con lo que es.</desc>
  <defs>
    <style>
      #spCarpeta .title{fill:#161A26;font-size:22px;font-weight:700}
      #spCarpeta .sub{fill:#79809A;font-size:13.5px}
      #spCarpeta .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #spCarpeta .nt{font-size:15px;font-weight:700;fill:#161A26}
      #spCarpeta .nb{fill:#454C61;font-size:13px}
      #spCarpeta .lbl{fill:#556074;font-size:12px;font-weight:600}
      #spCarpeta .foot{fill:#79809A;font-size:12px}
      #spCarpeta .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #spCarpeta .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#spCarpeta-arrow)}
    </style>
    <marker id="spCarpeta-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="448" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Dónde viven las specs</text>
  <text class="sub" x="48" y="80" data-fit="860">Todo en docs/, junto al código. El índice dice en qué va cada spec.</text>
<rect x="48" y="112" width="864" height="310" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><path d="M72,127 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="100" y="140" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="64">docs/</text><rect x="102" y="151" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="128" y="166" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="72">prd.md</text><rect x="520.0" y="150" width="203.4" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="621.72" y="166.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="205">el problema y los objetivos</text><rect x="102" y="177" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="128" y="192" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="129">requisitos.md</text><rect x="520.0" y="176" width="143.0" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="591.48" y="192.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="144">RF y RNF numerados</text><rect x="102" y="203" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="128" y="218" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="202">architectural_spine.md</text><rect x="520.0" y="202" width="149.7" height="24" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.2"/><text x="594.84" y="218.5" font-size="12" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="151">stack e invariantes</text><rect x="102" y="229" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="128" y="244" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="96">modelo.md</text><rect x="520.0" y="228" width="196.7" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="618.36" y="244.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="198">las tablas, de la sesión 4</text><path d="M100,257 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2" stroke-linejoin="round"/><text x="128" y="270" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="72">specs/</text><rect x="130" y="281" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="296" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="96">README.md</text><rect x="520.0" y="280" width="230.3" height="24" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.2"/><text x="635.16" y="296.5" font-size="12" font-weight="700" fill="#0F8478" text-anchor="middle" data-fit="232">el índice, con versión y estado</text><rect x="130" y="307" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="322" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="153">F-01-registro.md</text><rect x="520.0" y="306" width="196.7" height="24" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.2"/><text x="618.36" y="322.5" font-size="12" font-weight="700" fill="#0F8478" text-anchor="middle" data-fit="198">una spec por funcionalidad</text><rect x="130" y="333" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="348" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="153">F-02-publicar.md</text><rect x="130" y="359" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="374" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="202">F-03-foto-de-perfil.md</text><rect x="130" y="385" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="156" y="400" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="105">reporte.md</text><rect x="520.0" y="384" width="196.7" height="24" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.2"/><text x="618.36" y="400.5" font-size="12" font-weight="700" fill="#C2354F" text-anchor="middle" data-fit="198">las métricas de la crítica</text></svg>
```

El índice, `docs/specs/README.md`, tiene una línea por spec:

```markdown
- [F-01 · Registrarse](F-01-registro.md) · v1.0.0 · implementada
- [F-02 · Publicar](F-02-publicar.md) · v1.0.0 · aprobada
- [F-03 · Foto de perfil](F-03-foto-de-perfil.md) · v0.2.0 · borrador
```
