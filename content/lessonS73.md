# Taller · Del contexto al PRD y los requisitos

<!-- tags: sdd-prd, sdd-requisitos, PRD, requisitos funcionales, requisitos no funcionales, AGENTS.md, .agents/skills, mi proyecto se trata de, docs/prd.md, docs/requisitos.md, la skill no se carga -->

Este taller se hace **en el proyecto de tu equipo**. Al terminar tendrás los tres primeros documentos.

```svg
<svg id="taCrece" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 360" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="taCrece-ttl taCrece-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="taCrece-ttl">El proyecto se va formando · pasos 1 a 3</title>
  <desc id="taCrece-dsc">Cinco columnas en orden: contexto, PRD, requisitos, spine y specs. Cada una con el pedido al agente, el archivo que deja y el valor que agrega. Las de este taller están resaltadas; las otras, atenuadas.</desc>
  <defs>
    <style>
      #taCrece .title{fill:#161A26;font-size:22px;font-weight:700}
      #taCrece .sub{fill:#79809A;font-size:13.5px}
      #taCrece .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #taCrece .nt{font-size:15px;font-weight:700;fill:#161A26}
      #taCrece .nb{fill:#454C61;font-size:13px}
      #taCrece .lbl{fill:#556074;font-size:12px;font-weight:600}
      #taCrece .foot{fill:#79809A;font-size:12px}
      #taCrece .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #taCrece .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#taCrece-arrow)}
    </style>
    <marker id="taCrece-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="360" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">El proyecto se va formando · pasos 1 a 3</text>
  <text class="sub" x="48" y="80" data-fit="860">En este taller: el contexto, el PRD y los requisitos.</text>
<g><rect x="48" y="116" width="152" height="196" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><circle cx="74" cy="142" r="13" fill="#FFFFFF" stroke="#556074" stroke-width="2"/><text x="74" y="146.5" font-size="13" font-weight="700" fill="#556074" text-anchor="middle" data-fit="31">1</text><text x="96" y="147" font-size="14.5" font-weight="700" fill="#556074" text-anchor="start" data-fit="98">Contexto</text><text x="60" y="178" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="136">«Actualiza</text><text x="60" y="195" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="136">AGENTS.md»</text><rect x="56" y="208" width="136" height="32" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.2"/><text x="124.0" y="229" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="134">AGENTS.md</text><text x="60" y="264" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">Agrega:</text><text x="60" y="282" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="136">El agente sabe</text><text x="60" y="299" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="136">de qué va la app</text></g><path class="link" d="M201,214 H207"/><g><rect x="208" y="116" width="160" height="196" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="234" cy="142" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="234" y="146.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="31">2</text><text x="256" y="147" font-size="14.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="106">PRD</text><text x="220" y="178" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="144">«Mi proyecto se</text><text x="220" y="195" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="144">trata de…»</text><rect x="216" y="208" width="144" height="32" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.2"/><text x="288.0" y="229" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="142">docs/prd.md</text><text x="220" y="264" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">Agrega:</text><text x="220" y="282" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="144">Un problema y</text><text x="220" y="299" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="144">objetivos medibles</text></g><path class="link" d="M369,214 H375"/><g><rect x="376" y="116" width="168" height="196" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="402" cy="142" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="402" y="146.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="31">3</text><text x="424" y="147" font-size="14.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="114">Requisitos</text><text x="388" y="178" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="152">«Crea los</text><text x="388" y="195" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="152">requerimientos»</text><rect x="384" y="208" width="152" height="32" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.2"/><text x="460.0" y="229" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="150">docs/requisitos.md</text><text x="388" y="264" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">Agrega:</text><text x="388" y="282" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="152">Una lista que</text><text x="388" y="299" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="152">se puede comprobar</text></g><path class="link" d="M545,214 H551"/><g opacity=".4"><rect x="552" y="116" width="196" height="196" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="578" cy="142" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="578" y="146.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="31">4</text><text x="600" y="147" font-size="14.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="142">Spine</text><text x="564" y="178" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="180">«…especifica la</text><text x="564" y="195" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="180">arquitectura»</text><rect x="560" y="208" width="180" height="32" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.2"/><text x="650.0" y="229" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="178">architectural_spine.md</text><text x="564" y="264" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">Agrega:</text><text x="564" y="282" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="180">Reglas que nadie</text><text x="564" y="299" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="180">decide distinto</text></g><path class="link" d="M749,214 H755"/><g opacity=".4"><rect x="756" y="116" width="156" height="196" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><circle cx="782" cy="142" r="13" fill="#FFFFFF" stroke="#0F8478" stroke-width="2"/><text x="782" y="146.5" font-size="13" font-weight="700" fill="#0F8478" text-anchor="middle" data-fit="31">5</text><text x="804" y="147" font-size="14.5" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="102">Specs</text><text x="768" y="178" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="140">«Crea las specs</text><text x="768" y="195" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="140">funcionales»</text><rect x="764" y="208" width="140" height="32" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.2"/><text x="834.0" y="229" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="138">docs/specs/</text><text x="768" y="264" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">Agrega:</text><text x="768" y="282" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="140">Un contrato por</text><text x="768" y="299" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="140">funcionalidad</text></g><text x="48" y="332" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Cada paso lee lo que dejaron los anteriores: por eso el orden importa.</text></svg>
```

## 0. Instala las skills

Crea las carpetas desde la raíz del proyecto. En macOS, Linux o Git Bash:

```shell
mkdir -p .agents/skills/sdd-prd/references .agents/skills/sdd-prd/assets
mkdir -p .agents/skills/sdd-requisitos/references
mkdir -p .agents/skills/sdd-requisitos/assets
mkdir -p .agents/skills/sdd-arquitectura/references
mkdir -p .agents/skills/sdd-arquitectura/assets
mkdir -p .agents/skills/sdd-specs/references .agents/skills/sdd-specs/assets
mkdir -p .agents/skills/sdd-critica/references
mkdir -p .agents/skills/sdd-critica/assets
```

En PowerShell, usa las mismas líneas sin `-p`.

```interactive
skill-files sdd
```

Por cada archivo, créalo con ese nombre en esa carpeta y pega el contenido con **Copiar**.

## 1. El archivo de contexto

Si tu proyecto ya tiene `AGENTS.md` (sesión 4), pídele al agente que lo ponga al día:

```text
Actualiza AGENTS.md: el qué es de la app, la estructura
actual de lib/ y una sección Documentos que diga que
docs/ tiene el PRD, los requisitos, la spine y las specs.
```

Si no lo tiene, créalo con `/init`, como en la sesión 4.

## 2. El PRD

```text
Mi proyecto se trata de …
```

Completa la frase con dos o tres líneas de tu app.

```svg
<svg id="taEntrevista" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="taEntrevista-ttl taEntrevista-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="taEntrevista-ttl">La skill entrevista antes de escribir</title>
  <desc id="taEntrevista-dsc">Una conversación: el estudiante cuenta que su proyecto es una red profesional; la skill repite lo que entendió y hace la ronda 1 de preguntas sobre el problema; el estudiante responde; la skill escribe docs/prd.md en la versión 0.1.0 con tres objetivos y dos preguntas abiertas.</desc>
  <defs>
    <style>
      #taEntrevista .title{fill:#161A26;font-size:22px;font-weight:700}
      #taEntrevista .sub{fill:#79809A;font-size:13.5px}
      #taEntrevista .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #taEntrevista .nt{font-size:15px;font-weight:700;fill:#161A26}
      #taEntrevista .nb{fill:#454C61;font-size:13px}
      #taEntrevista .lbl{fill:#556074;font-size:12px;font-weight:600}
      #taEntrevista .foot{fill:#79809A;font-size:12px}
      #taEntrevista .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #taEntrevista .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#taEntrevista-arrow)}
    </style>
    <marker id="taEntrevista-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="540" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La skill entrevista antes de escribir</text>
  <text class="sub" x="48" y="80" data-fit="860">Tú cuentas la idea; ella pregunta lo que falta y deja docs/prd.md.</text>
<rect x="48" y="112" width="560" height="74" rx="14" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="64" y="134" font-size="12" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="37">Tú</text><text x="64" y="156" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="536">Mi proyecto se trata de una red profesional para</text><text x="64" y="175" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="536">estudiantes de Icesi: perfil, publicaciones y mensajes.</text><rect x="352" y="200" width="560" height="93" rx="14" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><text x="368" y="222" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="131">Agente · sdd-prd</text><text x="368" y="244" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="536">Entiendo: una red para mostrarse y conversar.</text><text x="368" y="263" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="536">Ronda 1 · ¿Qué problema resuelve? ¿Cómo lo</text><text x="368" y="282" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="536">resuelven hoy? ¿Qué les molesta de eso?</text><rect x="48" y="307" width="560" height="74" rx="14" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="64" y="329" font-size="12" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="37">Tú</text><text x="64" y="351" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="536">Hoy usan LinkedIn, pero ahí no encuentran</text><text x="64" y="370" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="536">a otros estudiantes de su carrera.</text><rect x="352" y="395" width="560" height="93" rx="14" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/><text x="368" y="417" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="131">Agente · sdd-prd</text><text x="368" y="439" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="536">Escribí docs/prd.md · v0.1.0 · borrador.</text><text x="368" y="458" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="536">3 objetivos · 2 preguntas abiertas.</text><text x="368" y="477" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" data-fit="536">Sigue con sdd-requisitos.</text><text x="48" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Si una respuesta es vaga («que sea fácil»), la skill pide un ejemplo o un número.</text></svg>
```

Responde con datos, no con adjetivos. Revisa `docs/prd.md`:

- Cada objetivo dice cómo se sabe que se cumplió.
- *No incluye* tiene al menos una cosa.
- Nada de tecnologías ni pantallas.

## 3. Los requisitos

```text
Crea los requerimientos
```

Revisa `docs/requisitos.md`:

- Cada RF cita un objetivo (`O-01`…) y cada objetivo tiene RF.
- Los RNF tienen un número: segundos, megas, dispositivos.
- Cada uno tiene prioridad: *Debe*, *Debería* o *Podría*.

## Qué debes tener al terminar

- [ ] Las cinco skills en `.agents/skills/`
- [ ] `AGENTS.md` al día
- [ ] `docs/prd.md` en la versión 0.1.0
- [ ] `docs/requisitos.md` en la versión 0.1.0
