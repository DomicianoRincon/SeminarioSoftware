# Entrega 1 · Prototipo en Stitch/Figma y base de datos

<!-- tags: prototipo no funcional, Stitch, Figma, diseño de pantallas, modelo de datos, diagrama entidad relación, contrato mínimo común, propuesta de la aplicación, entregable del equipo -->

Primera entrega del proyecto del equipo: la **propuesta de la aplicación**, su **diseño no funcional** en Stitch y Figma, y el **modelo de datos mínimo** en diagrama. Es el plano de la app antes de escribir código.

```svg
<svg id="entE1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 264" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="entE1-ttl entE1-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="entE1-ttl">La entrega 1 en el calendario</title>
  <desc id="entE1-dsc">Las 16 sesiones del curso, dos por semana, de la semana 9 a la 16. Se trabaja en las sesiones 5, 10; el planeador no fija la sesión de presentación.</desc>
  <defs>
    <style>
      #entE1 .title{fill:#161A26;font-size:22px;font-weight:700}
      #entE1 .sub{fill:#79809A;font-size:13.5px}
      #entE1 .n{font-size:16px;font-weight:700}
      #entE1 .wk{fill:#79809A;font-size:12px}
      #entE1 .lg{fill:#454C61;font-size:13px}
    </style>
  </defs>
  <rect width="960" height="264" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La entrega 1 en el calendario</text>
  <text class="sub" x="48" y="80" data-fit="860">Se trabaja en dos momentos: el diseño en la sesión 5 y el modelo de datos en la sesión 10.</text>
  <rect x="48" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="72" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">1</text>
  <rect x="102" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="126" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">2</text>
  <rect x="156" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="180" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">3</text>
  <rect x="210" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="234" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">4</text>
  <rect x="264" y="112" width="48" height="56" rx="8" fill="#FFF3DC" stroke="#F0C572" stroke-width="2"/>
  <text class="n" x="288" y="140" dy="0.35em" text-anchor="middle" fill="#A96C05">5</text>
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
  <rect x="750" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="774" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">14</text>
  <rect x="804" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="828" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">15</text>
  <rect x="858" y="112" width="48" height="56" rx="8" fill="#EFF1F5" stroke="#D9DEE8" stroke-width="1.25"/>
  <text class="n" x="882" y="140" dy="0.35em" text-anchor="middle" fill="#79809A">16</text>
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
</svg>
```

## Qué se entrega

- La propuesta de la aplicación del reto.
- El diseño no funcional de sus pantallas, hecho en **Stitch** y **Figma**, respetando el contrato mínimo común.
- El **modelo de datos mínimo** de la aplicación, en diagrama.

## Cómo se trabaja

| Sesión | Qué se hace | Dónde |
|---|---|---|
| 5 | Propuesta de la aplicación y diseño no funcional en Stitch y Figma | Fuera de clase · 4 h |
| 10 | El modelo de datos mínimo en diagrama | Fuera de clase · 4 h |

## Uso de IA

Nivel **5 · Exploración con IAG**: se incentiva explorar la IA como parte del producto. Herramientas previstas: Stitch, Figma y el asistente de IA en consola, con sus skills y el servidor MCP de Supabase para el modelo de datos.

## Por confirmar

La fecha de entrega, el formato y el peso en la nota los define el profesor; el planeador del curso todavía no los fija.
