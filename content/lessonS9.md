# Entrega 3 · Specs completas de la aplicación

<!-- tags: Spec Driven Development, especificación técnica, specs, contrato antes del código, versionamiento de specs, CLAUDE.md, skills, entrega final, sustentación, evidencia del uso del agente -->

Tercera entrega: las **specs completas de la aplicación**, escritas con Spec Driven Development. Se presentan en la **entrega final**, junto con la app funcionando y la evidencia de cómo se dirigió al agente de IA.

```svg
<svg id="entE3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 264" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="entE3-ttl entE3-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="entE3-ttl">La entrega 3 en el calendario</title>
  <desc id="entE3-dsc">Las 16 sesiones del curso, dos por semana, de la semana 9 a la 16. Se trabaja en las sesiones 10, 14; se presenta en las sesiones 15, 16.</desc>
  <defs>
    <style>
      #entE3 .title{fill:#161A26;font-size:22px;font-weight:700}
      #entE3 .sub{fill:#79809A;font-size:13.5px}
      #entE3 .n{font-size:16px;font-weight:700}
      #entE3 .wk{fill:#79809A;font-size:12px}
      #entE3 .lg{fill:#454C61;font-size:13px}
    </style>
  </defs>
  <rect width="960" height="264" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La entrega 3 en el calendario</text>
  <text class="sub" x="48" y="80" data-fit="860">Se empieza en la sesión 10, se prepara en la 14 y se sustenta en la entrega final (sesiones 15 y 16).</text>
  <rect x="48" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="72" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">1</text>
  <rect x="102" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="126" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">2</text>
  <rect x="156" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="180" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">3</text>
  <rect x="210" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="234" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">4</text>
  <rect x="264" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="288" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">5</text>
  <rect x="318" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="342" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">6</text>
  <rect x="372" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="396" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">7</text>
  <rect x="426" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="450" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">8</text>
  <rect x="480" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="504" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">9</text>
  <rect x="534" y="112" width="48" height="56" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="2"/>
  <text class="n" x="558" y="140" dy="0.35em" text-anchor="middle" fill="#A96C05">10</text>
  <rect x="588" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="612" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">11</text>
  <rect x="642" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="666" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">12</text>
  <rect x="696" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="720" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">13</text>
  <rect x="750" y="112" width="48" height="56" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="2"/>
  <text class="n" x="774" y="140" dy="0.35em" text-anchor="middle" fill="#A96C05">14</text>
  <rect x="804" y="112" width="48" height="56" rx="8" fill="#4453C9" stroke="#4453C9" stroke-width="2"/>
  <text class="n" x="828" y="140" dy="0.35em" text-anchor="middle" fill="#FFFFFF">15</text>
  <rect x="858" y="112" width="48" height="56" rx="8" fill="#4453C9" stroke="#4453C9" stroke-width="2"/>
  <text class="n" x="882" y="140" dy="0.35em" text-anchor="middle" fill="#FFFFFF">16</text>
  <text class="wk" x="99" y="190" text-anchor="middle">semana 9</text>
  <text class="wk" x="207" y="190" text-anchor="middle">semana 10</text>
  <line x1="153" y1="108" x2="153" y2="196" stroke="#D9DEE8" stroke-width="1" stroke-dasharray="3 3"/>
  <text class="wk" x="315" y="190" text-anchor="middle">semana 11</text>
  <line x1="261" y1="108" x2="261" y2="196" stroke="#D9DEE8" stroke-width="1" stroke-dasharray="3 3"/>
  <text class="wk" x="423" y="190" text-anchor="middle">semana 12</text>
  <line x1="369" y1="108" x2="369" y2="196" stroke="#D9DEE8" stroke-width="1" stroke-dasharray="3 3"/>
  <text class="wk" x="531" y="190" text-anchor="middle">semana 13</text>
  <line x1="477" y1="108" x2="477" y2="196" stroke="#D9DEE8" stroke-width="1" stroke-dasharray="3 3"/>
  <text class="wk" x="639" y="190" text-anchor="middle">semana 14</text>
  <line x1="585" y1="108" x2="585" y2="196" stroke="#D9DEE8" stroke-width="1" stroke-dasharray="3 3"/>
  <text class="wk" x="747" y="190" text-anchor="middle">semana 15</text>
  <line x1="693" y1="108" x2="693" y2="196" stroke="#D9DEE8" stroke-width="1" stroke-dasharray="3 3"/>
  <text class="wk" x="855" y="190" text-anchor="middle">semana 16</text>
  <line x1="801" y1="108" x2="801" y2="196" stroke="#D9DEE8" stroke-width="1" stroke-dasharray="3 3"/>
  <text class="wk" x="48" y="104">SESIÓN DEL CURSO</text>
  <rect x="48" y="220" width="18" height="18" rx="4" fill="#FFF3DC" stroke="#F0C572" stroke-width="2"/>
  <text class="lg" x="74" y="229" dy="0.35em">se trabaja (en clase o fuera de clase)</text>
  <rect x="360" y="220" width="18" height="18" rx="4" fill="#4453C9"/>
  <text class="lg" x="386" y="229" dy="0.35em">se presenta en clase</text>
</svg>
```

## Qué se entrega

- Las **specs** de la aplicación: la especificación como contrato antes del código.
- Su **versionamiento**, con el seguimiento de cuáles están implementadas y cuáles no.
- En la entrega final, junto con las specs: la **demostración** de la app, el **repositorio**, el **CLAUDE.md**, las **skills** y la **evidencia** de cómo el equipo dirigió y auditó al agente.

## Cómo se trabaja

| Sesión | Qué se hace | Dónde |
|---|---|---|
| 10 | Spec Driven Development: la spec como contrato, skills de generación y de crítica de specs | En clase |
| 14 | Preparar la sustentación final: demostración, repositorio, CLAUDE.md, skills y specs | Fuera de clase · 4 h |
| 15 | **Entrega final I**: equipos 1 a 3, unos 30 minutos por equipo con la retroalimentación | En clase |
| 16 | **Entrega final II**: equipos 4 a 6, con el mismo formato, y cierre del curso | En clase |

## Uso de IA

Nivel **5 · Exploración con IAG**, y la entrega final es **evaluativa en IAG**: se evalúa también el proceso asistido por IA, no solo la app.

## Por confirmar

El peso en la nota lo define el profesor; el planeador no lo fija.
