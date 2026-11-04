# ¿Qué es Spec Driven Development?

<!-- tags: Spec Driven Development, SDD, la spec como contrato, fases de SDD, spec funcional, spec técnica, spec-first, spec-anchored, spec-kit, BMAD, el agente inventa lo que no pedí, el agente hace algo distinto cada vez -->

En *Spec Driven Development* (SDD) primero se escribe qué debe hacer la app y después se construye. Lo escrito, la **spec**, es el contrato entre tu equipo y el agente.

## Sin spec, el agente adivina

```svg
<svg id="sddContrato" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 430" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="sddContrato-ttl sddContrato-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="sddContrato-ttl">Sin spec, el agente adivina</title>
  <desc id="sddContrato-dsc">Dos filas. Arriba, sin spec: un pedido corto llega al agente y cada vez sale una app distinta. Abajo, con spec: el agente lee la spec y lo que construye se compara con ella.</desc>
  <defs>
    <style>
      #sddContrato .title{fill:#161A26;font-size:22px;font-weight:700}
      #sddContrato .sub{fill:#79809A;font-size:13.5px}
      #sddContrato .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #sddContrato .nt{font-size:15px;font-weight:700;fill:#161A26}
      #sddContrato .nb{fill:#454C61;font-size:13px}
      #sddContrato .lbl{fill:#556074;font-size:12px;font-weight:600}
      #sddContrato .foot{fill:#79809A;font-size:12px}
      #sddContrato .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #sddContrato .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#sddContrato-arrow)}
    </style>
    <marker id="sddContrato-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="430" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Sin spec, el agente adivina</text>
  <text class="sub" x="48" y="80" data-fit="860">Con una spec, lo que construye se puede revisar contra algo escrito.</text>
<text x="48" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="77">SIN SPEC</text><g><rect x="48" y="144" width="220" height="84" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="64" y="176" font-size="14.5" font-weight="700" fill="#556074" text-anchor="start" data-fit="196">«Haz el login»</text><text x="64" y="202" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="196">Un pedido de una línea.</text></g><path class="link" d="M268,186 H330"/><g><rect x="332" y="144" width="180" height="84" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="348" y="176" font-size="14.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="156">Agente</text><text x="348" y="202" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="156">Llena los huecos</text><text x="348" y="221" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="156">como le parece.</text></g><path class="link" d="M512,186 H574"/><g><rect x="576" y="152" width="104" height="68" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="592" y="182" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="80">¿Con correo?</text></g><g><rect x="690" y="152" width="104" height="68" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="706" y="182" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="80">¿Con Google?</text></g><g><rect x="804" y="152" width="104" height="68" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="820" y="182" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="80">¿Y el error?</text></g><text x="576" y="244" font-size="12.5" font-weight="600" fill="#C2354F" text-anchor="start" data-fit="340">Cada vez decide distinto. ¿Cuál era la correcta?</text><text x="48" y="292" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="77">CON SPEC</text><g><path d="M48,308 h204 l16,16 v68 h-220 Z" fill="#FFFFFF" stroke="#86D3CA" stroke-width="1.5"/><path d="M252,308 v16 h16" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="158.0" y="355.0" font-size="12.5" font-weight="700" fill="#0F8478" text-anchor="middle" class="mono" data-fit="212">F-01 · Registrarse</text></g><path class="link" d="M268,350 H330"/><g><rect x="332" y="308" width="180" height="84" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="348" y="340" font-size="14.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="156">Agente</text><text x="348" y="366" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="156">Construye lo que</text><text x="348" y="385" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="156">dice la spec.</text></g><path class="link" d="M512,350 H574"/><g><rect x="576" y="308" width="336" height="84" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="592" y="340" font-size="14.5" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="312">Se revisa contra la spec</text><text x="592" y="366" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="312">¿Cumple cada criterio de aceptación?</text><text x="592" y="385" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="312">Sí o no, sin discutir gustos.</text></g></svg>
```

Un pedido de una línea deja huecos, y el agente los llena como le parece. Con una spec, lo que construye se puede revisar contra algo escrito: cumple o no cumple.

## Las seis fases

```svg
<svg id="sddFases" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 452" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="sddFases-ttl sddFases-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="sddFases-ttl">Las seis fases de Spec Driven Development</title>
  <desc id="sddFases-dsc">Seis tarjetas en fila: producto, funcional, arquitectura, tareas, implementación y validación, cada una con su pregunta. Una flecha vuelve de validación a las specs: si no cumple, se corrige la spec o el código.</desc>
  <defs>
    <style>
      #sddFases .title{fill:#161A26;font-size:22px;font-weight:700}
      #sddFases .sub{fill:#79809A;font-size:13.5px}
      #sddFases .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #sddFases .nt{font-size:15px;font-weight:700;fill:#161A26}
      #sddFases .nb{fill:#454C61;font-size:13px}
      #sddFases .lbl{fill:#556074;font-size:12px;font-weight:600}
      #sddFases .foot{fill:#79809A;font-size:12px}
      #sddFases .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #sddFases .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#sddFases-arrow)}
    </style>
    <marker id="sddFases-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="452" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las seis fases de Spec Driven Development</text>
  <text class="sub" x="48" y="80" data-fit="860">Cada fase responde una pregunta y deja un documento. Las tres primeras son specs.</text>
<path d="M48.0,132 H472.8" stroke="#4453C9" stroke-width="3" stroke-linecap="round"/><text x="48.0" y="122" font-size="12" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="420">LAS SPECS · EL QUÉ Y EL CÓMO</text><path d="M487.20000000000005,132 H912.0" stroke="#9AA1B2" stroke-width="3" stroke-linecap="round"/><text x="487.20000000000005" y="122" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="420">CONSTRUIR Y COMPROBAR</text><rect x="48.0" y="156" width="132" height="168" rx="14" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="74.0" cy="184" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="74.0" y="188.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="31">1</text><text x="62.0" y="228" font-size="15" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="112">Producto</text><text x="62.0" y="248" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="112">Requirements</text><text x="62.0" y="280" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">¿Qué problema,</text><text x="62.0" y="299" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">para quién?</text><path class="link" d="M181.0,240 H193.4"/><rect x="194.4" y="156" width="132" height="168" rx="14" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><circle cx="220.4" cy="184" r="13" fill="#FFFFFF" stroke="#0F8478" stroke-width="2"/><text x="220.4" y="188.5" font-size="13" font-weight="700" fill="#0F8478" text-anchor="middle" data-fit="31">2</text><text x="208.4" y="228" font-size="15" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="112">Funcional</text><text x="208.4" y="248" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="112">Functional spec</text><text x="208.4" y="280" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">¿Qué hace el</text><text x="208.4" y="299" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">sistema?</text><path class="link" d="M327.4,240 H339.79999999999995"/><rect x="340.8" y="156" width="132" height="168" rx="14" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="366.8" cy="184" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="366.8" y="188.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="31">3</text><text x="354.8" y="228" font-size="15" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="112">Arquitectura</text><text x="354.8" y="248" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="112">Technical design</text><text x="354.8" y="280" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">¿Cómo se</text><text x="354.8" y="299" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">construye?</text><path class="link" d="M473.8,240 H486.2"/><rect x="487.20000000000005" y="156" width="132" height="168" rx="14" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><circle cx="513.2" cy="184" r="13" fill="#FFFFFF" stroke="#7439B8" stroke-width="2"/><text x="513.2" y="188.5" font-size="13" font-weight="700" fill="#7439B8" text-anchor="middle" data-fit="31">4</text><text x="501.20000000000005" y="228" font-size="15" font-weight="700" fill="#7439B8" text-anchor="start" data-fit="112">Tareas</text><text x="501.20000000000005" y="248" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="112">Plan / Tasks</text><text x="501.20000000000005" y="280" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">¿En qué</text><text x="501.20000000000005" y="299" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">orden?</text><path class="link" d="M620.2,240 H632.6"/><rect x="633.6" y="156" width="132" height="168" rx="14" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><circle cx="659.6" cy="184" r="13" fill="#FFFFFF" stroke="#3A8235" stroke-width="2"/><text x="659.6" y="188.5" font-size="13" font-weight="700" fill="#3A8235" text-anchor="middle" data-fit="31">5</text><text x="647.6" y="228" font-size="15" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="112">Código</text><text x="647.6" y="248" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="112">Implementation</text><text x="647.6" y="280" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">Se escribe o</text><text x="647.6" y="299" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">se genera.</text><path class="link" d="M766.6,240 H779.0"/><rect x="780.0" y="156" width="132" height="168" rx="14" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><circle cx="806.0" cy="184" r="13" fill="#FFFFFF" stroke="#C2354F" stroke-width="2"/><text x="806.0" y="188.5" font-size="13" font-weight="700" fill="#C2354F" text-anchor="middle" data-fit="31">6</text><text x="794.0" y="228" font-size="15" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="112">Validación</text><text x="794.0" y="248" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="112">Testing</text><text x="794.0" y="280" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">¿Cumple la</text><text x="794.0" y="299" font-size="13" font-weight="600" fill="#161A26" text-anchor="start" data-fit="112">spec?</text><path class="link" d="M846.0,326 V364 H260.4 V328"/><text x="553.2" y="386" font-size="13" font-weight="600" fill="#556074" text-anchor="middle" data-fit="560">Si no cumple, se corrige la spec o el código, y se vuelve a validar.</text></svg>
```

Cada fase deja un documento que lee la siguiente:

1. **Producto**: el PRD y los requisitos.
2. **Funcional**: una spec por funcionalidad.
3. **Arquitectura**: la architectural spine y, más adelante, la spec técnica.
4. **Tareas**: el plan, dividido en pasos pequeños.
5. **Código**: lo escribe el agente, una spec a la vez.
6. **Validación**: se revisa contra los criterios de aceptación.

Hoy se cubren las fases 1 a 3.

## Lo que vas a hacer

```svg
<svg id="sddHoy" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 400" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="sddHoy-ttl sddHoy-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="sddHoy-ttl">Del contexto a las specs, documento por documento</title>
  <desc id="sddHoy-dsc">Cinco documentos numerados en orden: AGENTS.md, docs/prd.md, docs/requisitos.md, docs/architectural_spine.md y docs/specs/, cada uno con la fase a la que pertenece. Debajo, atenuados, los de las próximas sesiones: spec técnica, tareas, código y pruebas.</desc>
  <defs>
    <style>
      #sddHoy .title{fill:#161A26;font-size:22px;font-weight:700}
      #sddHoy .sub{fill:#79809A;font-size:13.5px}
      #sddHoy .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #sddHoy .nt{font-size:15px;font-weight:700;fill:#161A26}
      #sddHoy .nb{fill:#454C61;font-size:13px}
      #sddHoy .lbl{fill:#556074;font-size:12px;font-weight:600}
      #sddHoy .foot{fill:#79809A;font-size:12px}
      #sddHoy .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #sddHoy .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#sddHoy-arrow)}
    </style>
    <marker id="sddHoy-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="400" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Del contexto a las specs, documento por documento</text>
  <text class="sub" x="48" y="80" data-fit="860">Cinco pasos en tu proyecto, en dos sesiones. Cada uno lee lo que dejó el anterior.</text>
<text x="48" y="128" font-size="12" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="131">SESIONES 10 Y 11</text><rect x="48" y="144" width="148" height="112" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><circle cx="74" cy="170" r="13" fill="#FFFFFF" stroke="#556074" stroke-width="2"/><text x="74" y="174.5" font-size="13" font-weight="700" fill="#556074" text-anchor="middle" data-fit="31">1</text><rect x="106.2" y="158" width="75.8" height="24" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.2"/><text x="144.12" y="174.5" font-size="12" font-weight="700" fill="#556074" text-anchor="middle" data-fit="77">Contexto</text><text x="62" y="222" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="128">AGENTS.md</text><path class="link" d="M197,200 H203"/><rect x="204" y="144" width="156" height="112" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="230" cy="170" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="230" y="174.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="31">2</text><rect x="283.7" y="158" width="62.3" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="314.84" y="174.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="64">Fase 1</text><text x="218" y="222" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="136">docs/prd.md</text><path class="link" d="M361,200 H367"/><rect x="368" y="144" width="164" height="112" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="394" cy="170" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="394" y="174.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="31">3</text><rect x="455.7" y="158" width="62.3" height="24" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.2"/><text x="486.84" y="174.5" font-size="12" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="64">Fase 1</text><text x="382" y="222" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="144">docs/requisitos.md</text><path class="link" d="M533,200 H539"/><rect x="540" y="144" width="228" height="112" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="566" cy="170" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="566" y="174.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="31">4</text><rect x="624.5" y="158" width="129.5" height="24" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.2"/><text x="689.24" y="174.5" font-size="12" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="131">Fase 3 · inicial</text><text x="554" y="214" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="208">docs/</text><text x="554" y="234" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="208">architectural_spine.md</text><path class="link" d="M769,200 H775"/><rect x="776" y="144" width="136" height="112" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><circle cx="802" cy="170" r="13" fill="#FFFFFF" stroke="#0F8478" stroke-width="2"/><text x="802" y="174.5" font-size="13" font-weight="700" fill="#0F8478" text-anchor="middle" data-fit="31">5</text><rect x="835.7" y="158" width="62.3" height="24" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.2"/><text x="866.84" y="174.5" font-size="12" font-weight="700" fill="#0F8478" text-anchor="middle" data-fit="64">Fase 2</text><text x="790" y="222" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="116">docs/specs/</text><text x="48" y="300" font-size="12" font-weight="700" fill="#79809A" text-anchor="start" data-fit="138">PRÓXIMAS SESIONES</text><g opacity=".45"><rect x="48" y="314" width="204" height="44" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 5"/></g><text x="150" y="341" font-size="13.5" font-weight="700" fill="#79809A" text-anchor="middle" data-fit="114">Spec técnica</text><g opacity=".45"><rect x="268" y="314" width="204" height="44" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 5"/></g><text x="370" y="341" font-size="13.5" font-weight="700" fill="#79809A" text-anchor="middle" data-fit="69">Tareas</text><g opacity=".45"><rect x="488" y="314" width="204" height="44" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 5"/></g><text x="590" y="341" font-size="13.5" font-weight="700" fill="#79809A" text-anchor="middle" data-fit="69">Código</text><g opacity=".45"><rect x="708" y="314" width="204" height="44" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 5"/></g><text x="810" y="341" font-size="13.5" font-weight="700" fill="#79809A" text-anchor="middle" data-fit="76">Pruebas</text></svg>
```

La spine va antes que las specs funcionales: así el agente sabe qué puede hacer la app (hay cuentas, hay fotos). Pero la spec funcional **no nombra tecnología**. Si dice *Supabase* o *setState*, se está metiendo en el cómo.

## Funcional y técnica

```svg
<svg id="sddQueComo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 360" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="sddQueComo-ttl sddQueComo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="sddQueComo-ttl">Spec funcional y spec técnica</title>
  <desc id="sddQueComo-dsc">Dos columnas sobre cambiar la foto de perfil. A la izquierda la spec funcional dice qué ve y qué puede hacer el usuario, sin tecnología. A la derecha, atenuada, la spec técnica dice con qué pantallas, servicios y almacenamiento se construye; se hace más adelante.</desc>
  <defs>
    <style>
      #sddQueComo .title{fill:#161A26;font-size:22px;font-weight:700}
      #sddQueComo .sub{fill:#79809A;font-size:13.5px}
      #sddQueComo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #sddQueComo .nt{font-size:15px;font-weight:700;fill:#161A26}
      #sddQueComo .nb{fill:#454C61;font-size:13px}
      #sddQueComo .lbl{fill:#556074;font-size:12px;font-weight:600}
      #sddQueComo .foot{fill:#79809A;font-size:12px}
      #sddQueComo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #sddQueComo .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#sddQueComo-arrow)}
    </style>
    <marker id="sddQueComo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="360" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Spec funcional y spec técnica</text>
  <text class="sub" x="48" y="80" data-fit="860">La misma funcionalidad, dos preguntas distintas.</text>
<g><rect x="48" y="120" width="420" height="196" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="64" y="152" font-size="14.5" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="396">Funcional · el qué</text><text x="64" y="178" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">El usuario elige una foto de su galería.</text><text x="64" y="197" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">Ve la foto nueva en su perfil.</text><text x="64" y="216" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">Si pesa más de 5 MB, ve «La foto pesa demasiado».</text><text x="64" y="235" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">Sin conexión, la foto anterior se conserva.</text><text x="64" y="254" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396"></text><text x="64" y="273" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">Habla el idioma del usuario.</text><text x="64" y="292" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">No nombra ninguna tecnología.</text></g><g><rect x="492" y="120" width="420" height="196" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5" stroke-dasharray="6 5"/><text x="508" y="152" font-size="14.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="396">Técnica · el cómo</text><text x="508" y="178" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">ProfileScreen guarda la foto con setState.</text><text x="508" y="197" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">ProfileService la sube al bucket avatars.</text><text x="508" y="216" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">La ruta queda en la columna foto_url.</text><text x="508" y="235" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">Usa supabase_flutter.</text><text x="508" y="254" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396"></text><text x="508" y="273" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">Habla el idioma del código.</text><text x="508" y="292" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="396">Llega en una sesión posterior.</text></g><rect x="795.5" y="140" width="69.0" height="24" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.2"/><text x="830" y="156.5" font-size="12" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="71">después</text></svg>
```

La funcional se escribe hoy. La técnica llega cuando se vea Supabase en la app, junto con una skill que conozca cómo se escribe el front en el curso.

## Qué tanto manda la spec

- **Spec-first**: se escribe antes del código y después se olvida.
- **Spec-anchored**: vive en el repositorio junto al código y cambia con él. Es lo que se hace en el curso.
- **Spec-as-source**: la spec es lo único que se edita y el código se regenera desde ella.

## En la industria

- **spec-kit** de GitHub: comandos para especificar, planear, dividir en tareas e implementar.
- **BMAD Method**: agentes con roles (analista, product manager, arquitecto) que entrevistan y escriben cada documento.
- **Kiro** de AWS: un editor que pasa de requisitos a diseño y a tareas.

Las cinco skills de esta sesión son una versión pequeña de esas ideas.
