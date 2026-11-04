# Métricas del conjunto de specs

<!-- tags: métricas de specs, completitud, trazabilidad, verificabilidad, ambigüedad, consistencia, atomicidad, sdd-critica, reporte.md, requisito sin spec, criterio de aceptación no medible -->

Una spec puede estar bien escrita y aun así al conjunto le pueden faltar piezas. Estas métricas miden el conjunto.

## La traza

```svg
<svg id="mtTraza" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 404" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="mtTraza-ttl mtTraza-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="mtTraza-ttl">La traza: del objetivo al criterio</title>
  <desc id="mtTraza-dsc">Una cadena de izquierda a derecha: el objetivo O-02 del PRD, los requisitos RF-07 y RF-08, la spec F-03 y sus criterios CA-1 y CA-2. Abajo, RF-09 sin ninguna spec, marcado en rojo porque baja la completitud.</desc>
  <defs>
    <style>
      #mtTraza .title{fill:#161A26;font-size:22px;font-weight:700}
      #mtTraza .sub{fill:#79809A;font-size:13.5px}
      #mtTraza .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #mtTraza .nt{font-size:15px;font-weight:700;fill:#161A26}
      #mtTraza .nb{fill:#454C61;font-size:13px}
      #mtTraza .lbl{fill:#556074;font-size:12px;font-weight:600}
      #mtTraza .foot{fill:#79809A;font-size:12px}
      #mtTraza .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #mtTraza .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#mtTraza-arrow)}
    </style>
    <marker id="mtTraza-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="404" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La traza: del objetivo al criterio</text>
  <text class="sub" x="48" y="80" data-fit="860">Cada documento cita al anterior. Un eslabón suelto es un problema.</text>
<text x="48" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="44">PRD</text><text x="272" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="91">REQUISITOS</text><text x="496" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="50">SPEC</text><text x="720" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="84">CRITERIOS</text><g><rect x="48" y="168" width="192" height="64" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="64" y="200" font-size="14.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="168">O-02</text><text x="64" y="226" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="168">Mostrarse con su foto.</text></g><g><rect x="272" y="144" width="192" height="52" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="288" y="176" font-size="13.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="168">RF-07 · elegir foto</text></g><g><rect x="272" y="208" width="192" height="52" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="288" y="240" font-size="13.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="168">RF-08 · límite 5 MB</text></g><g><rect x="496" y="168" width="192" height="64" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="512" y="200" font-size="14.5" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="168">F-03</text><text x="512" y="226" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="168">Foto de perfil.</text></g><g><rect x="720" y="144" width="192" height="52" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="736" y="176" font-size="13.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="168">CA-1 · la ve</text></g><g><rect x="720" y="208" width="192" height="52" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="736" y="240" font-size="13.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="168">CA-2 · aviso</text></g><path class="link" d="M240,200 C256,200 256,170 270,170"/><path class="link" d="M240,200 C256,200 256,234 270,234"/><path class="link" d="M464,170 C480,170 480,200 494,200"/><path class="link" d="M464,234 C480,234 480,200 494,200"/><path class="link" d="M688,200 C704,200 704,170 718,170"/><path class="link" d="M688,200 C704,200 704,234 718,234"/><g><rect x="272" y="292" width="192" height="52" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="288" y="324" font-size="13.5" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="168">RF-09 · quitar foto</text></g><path d="M464,318 H556" stroke="#C2354F" stroke-width="2" stroke-dasharray="5 5"/><text x="566" y="314" font-size="13" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="184">Ninguna spec lo cubre.</text><text x="566" y="334" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="220">La completitud queda en 8/9.</text></svg>
```

Cada documento cita al anterior: la spec dice qué RF cubre y cada RF dice qué objetivo atiende. Si un eslabón queda suelto, algo sobra o algo falta.

## Las diez métricas

```svg
<svg id="mtTablero" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 512" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="mtTablero-ttl mtTablero-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="mtTablero-ttl">Diez métricas para el conjunto de specs</title>
  <desc id="mtTablero-dsc">Diez tarjetas en dos filas, cada una con el nombre de la métrica, qué cuenta y un valor de ejemplo con su color: completitud, trazabilidad, verificabilidad, ambigüedad, consistencia, atomicidad, pureza funcional, preguntas abiertas, avance y estabilidad.</desc>
  <defs>
    <style>
      #mtTablero .title{fill:#161A26;font-size:22px;font-weight:700}
      #mtTablero .sub{fill:#79809A;font-size:13.5px}
      #mtTablero .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #mtTablero .nt{font-size:15px;font-weight:700;fill:#161A26}
      #mtTablero .nb{fill:#454C61;font-size:13px}
      #mtTablero .lbl{fill:#556074;font-size:12px;font-weight:600}
      #mtTablero .foot{fill:#79809A;font-size:12px}
      #mtTablero .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #mtTablero .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#mtTablero-arrow)}
    </style>
    <marker id="mtTablero-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="512" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Diez métricas para el conjunto de specs</text>
  <text class="sub" x="48" y="80" data-fit="860">La skill sdd-critica las calcula y deja el reporte en docs/specs/reporte.md.</text>
<rect x="48" y="120" width="160" height="160" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><rect x="48" y="120" width="160" height="6" rx="3" fill="#A96C05"/><text x="62" y="154" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="140">Completitud</text><text x="62" y="206" font-size="28" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="140">8/9</text><text x="62" y="236" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">RF con spec</text><text x="62" y="254" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">÷ RF totales</text><rect x="224" y="120" width="160" height="160" rx="12" fill="#FFFFFF" stroke="#9FD68D" stroke-width="1.5"/><rect x="224" y="120" width="160" height="6" rx="3" fill="#3A8235"/><text x="238" y="154" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="140">Trazabilidad</text><text x="238" y="206" font-size="28" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="140">100 %</text><text x="238" y="236" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">RF ↔ objetivo</text><text x="238" y="254" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">spec ↔ RF</text><rect x="400" y="120" width="160" height="160" rx="12" fill="#FFFFFF" stroke="#F3A3B2" stroke-width="1.5"/><rect x="400" y="120" width="160" height="6" rx="3" fill="#C2354F"/><text x="414" y="154" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="140">Verificabilidad</text><text x="414" y="206" font-size="28" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="140">6/10</text><text x="414" y="236" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">criterios medibles</text><text x="414" y="254" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">÷ criterios</text><rect x="576" y="120" width="160" height="160" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><rect x="576" y="120" width="160" height="6" rx="3" fill="#A96C05"/><text x="590" y="154" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="140">Ambigüedad</text><text x="590" y="206" font-size="28" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="140">2</text><text x="590" y="236" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">palabras vagas</text><text x="590" y="254" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">meta: 0</text><rect x="752" y="120" width="160" height="160" rx="12" fill="#FFFFFF" stroke="#9FD68D" stroke-width="1.5"/><rect x="752" y="120" width="160" height="6" rx="3" fill="#3A8235"/><text x="766" y="154" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="140">Consistencia</text><text x="766" y="206" font-size="28" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="140">0</text><text x="766" y="236" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">contradicciones</text><text x="766" y="254" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">meta: 0</text><rect x="48" y="296" width="160" height="160" rx="12" fill="#FFFFFF" stroke="#9FD68D" stroke-width="1.5"/><rect x="48" y="296" width="160" height="6" rx="3" fill="#3A8235"/><text x="62" y="330" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="140">Atomicidad</text><text x="62" y="382" font-size="28" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="140">0</text><text x="62" y="412" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">specs con dos</text><text x="62" y="430" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">funcionalidades</text><rect x="224" y="296" width="160" height="160" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><rect x="224" y="296" width="160" height="6" rx="3" fill="#A96C05"/><text x="238" y="330" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="140">Pureza funcional</text><text x="238" y="382" font-size="28" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="140">1</text><text x="238" y="412" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">specs que nombran</text><text x="238" y="430" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">tecnología</text><rect x="400" y="296" width="160" height="160" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><rect x="400" y="296" width="160" height="6" rx="3" fill="#556074"/><text x="414" y="330" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="140">Preguntas abiertas</text><text x="414" y="382" font-size="28" font-weight="700" fill="#556074" text-anchor="start" data-fit="140">3</text><text x="414" y="412" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">deuda de spec</text><text x="414" y="430" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">debe bajar</text><rect x="576" y="296" width="160" height="160" rx="12" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><rect x="576" y="296" width="160" height="6" rx="3" fill="#556074"/><text x="590" y="330" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="140">Avance</text><text x="590" y="382" font-size="28" font-weight="700" fill="#556074" text-anchor="start" data-fit="140">0/4</text><text x="590" y="412" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">implementadas ÷</text><text x="590" y="430" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">aprobadas</text><rect x="752" y="296" width="160" height="160" rx="12" fill="#FFFFFF" stroke="#9FD68D" stroke-width="1.5"/><rect x="752" y="296" width="160" height="6" rx="3" fill="#3A8235"/><text x="766" y="330" font-size="13.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="140">Estabilidad</text><text x="766" y="382" font-size="28" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="140">0</text><text x="766" y="412" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">cambios de versión</text><text x="766" y="430" font-size="12" font-weight="400" fill="#556074" text-anchor="start" data-fit="140">mayor por spec</text><text x="48" y="484" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Verde: en la meta. Amarillo: cerca. Rojo: hay que corregir antes de implementar.</text></svg>
```

- **Completitud**: RF con spec ÷ RF totales.
- **Trazabilidad**: RF que citan objetivo, y specs que citan RF.
- **Verificabilidad**: criterios con Dado / cuando / entonces ÷ criterios.
- **Ambigüedad**: palabras vagas como *fácil*, *rápido* o *etc.*
- **Consistencia**: contradicciones entre specs, o con la spine o el modelo.
- **Atomicidad**: specs que mezclan dos funcionalidades.
- **Pureza funcional**: specs que nombran tecnología.
- **Preguntas abiertas**: lo que falta decidir. Debe bajar con cada versión.
- **Avance**: specs implementadas ÷ aprobadas.
- **Estabilidad**: veces que cambió la versión mayor.

## La skill que las calcula

`sdd-critica` lee todo `docs/`, calcula las métricas y escribe `docs/specs/reporte.md`. No cambia ninguna spec: propone las tres correcciones más importantes y espera tu sí.
