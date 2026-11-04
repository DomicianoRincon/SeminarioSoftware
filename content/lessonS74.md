# Taller · Spine y specs funcionales

<!-- tags: sdd-arquitectura, sdd-specs, sdd-critica, architectural_spine.md, especifica la arquitectura, specs funcionales, docs/specs, reporte de métricas, subir la versión de una spec, la spec nombra Supabase -->

Continúa el [taller de la sesión 10](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0073): sobre el PRD y los requisitos que ya tienes, ahora la spine y las specs.

```svg
<svg id="tcCrece" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 360" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tcCrece-ttl tcCrece-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tcCrece-ttl">El proyecto se va formando · pasos 4 y 5</title>
  <desc id="tcCrece-dsc">Cinco columnas en orden: contexto, PRD, requisitos, spine y specs. Cada una con el pedido al agente, el archivo que deja y el valor que agrega. Las de este taller están resaltadas; las otras, atenuadas.</desc>
  <defs>
    <style>
      #tcCrece .title{fill:#161A26;font-size:22px;font-weight:700}
      #tcCrece .sub{fill:#79809A;font-size:13.5px}
      #tcCrece .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tcCrece .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tcCrece .nb{fill:#454C61;font-size:13px}
      #tcCrece .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tcCrece .foot{fill:#79809A;font-size:12px}
      #tcCrece .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tcCrece .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tcCrece-arrow)}
    </style>
    <marker id="tcCrece-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="360" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">El proyecto se va formando · pasos 4 y 5</text>
  <text class="sub" x="48" y="80" data-fit="860">En este taller: la spine y las specs funcionales, sobre lo que ya tienes.</text>
<g opacity=".4"><rect x="48" y="116" width="152" height="196" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><circle cx="74" cy="142" r="13" fill="#FFFFFF" stroke="#556074" stroke-width="2"/><text x="74" y="146.5" font-size="13" font-weight="700" fill="#556074" text-anchor="middle" data-fit="31">1</text><text x="96" y="147" font-size="14.5" font-weight="700" fill="#556074" text-anchor="start" data-fit="98">Contexto</text><text x="60" y="178" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="136">«Actualiza</text><text x="60" y="195" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="136">AGENTS.md»</text><rect x="56" y="208" width="136" height="32" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.2"/><text x="124.0" y="229" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="134">AGENTS.md</text><text x="60" y="264" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">Agrega:</text><text x="60" y="282" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="136">El agente sabe</text><text x="60" y="299" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="136">de qué va la app</text></g><path class="link" d="M201,214 H207"/><g opacity=".4"><rect x="208" y="116" width="160" height="196" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="234" cy="142" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="234" y="146.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="31">2</text><text x="256" y="147" font-size="14.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="106">PRD</text><text x="220" y="178" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="144">«Mi proyecto se</text><text x="220" y="195" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="144">trata de…»</text><rect x="216" y="208" width="144" height="32" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.2"/><text x="288.0" y="229" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="142">docs/prd.md</text><text x="220" y="264" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">Agrega:</text><text x="220" y="282" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="144">Un problema y</text><text x="220" y="299" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="144">objetivos medibles</text></g><path class="link" d="M369,214 H375"/><g opacity=".4"><rect x="376" y="116" width="168" height="196" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="402" cy="142" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="2"/><text x="402" y="146.5" font-size="13" font-weight="700" fill="#4453C9" text-anchor="middle" data-fit="31">3</text><text x="424" y="147" font-size="14.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="114">Requisitos</text><text x="388" y="178" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="152">«Crea los</text><text x="388" y="195" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="152">requerimientos»</text><rect x="384" y="208" width="152" height="32" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.2"/><text x="460.0" y="229" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="150">docs/requisitos.md</text><text x="388" y="264" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">Agrega:</text><text x="388" y="282" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="152">Una lista que</text><text x="388" y="299" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="152">se puede comprobar</text></g><path class="link" d="M545,214 H551"/><g><rect x="552" y="116" width="196" height="196" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="578" cy="142" r="13" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/><text x="578" y="146.5" font-size="13" font-weight="700" fill="#A96C05" text-anchor="middle" data-fit="31">4</text><text x="600" y="147" font-size="14.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="142">Spine</text><text x="564" y="178" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="180">«…especifica la</text><text x="564" y="195" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="180">arquitectura»</text><rect x="560" y="208" width="180" height="32" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.2"/><text x="650.0" y="229" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="178">architectural_spine.md</text><text x="564" y="264" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">Agrega:</text><text x="564" y="282" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="180">Reglas que nadie</text><text x="564" y="299" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="180">decide distinto</text></g><path class="link" d="M749,214 H755"/><g><rect x="756" y="116" width="156" height="196" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><circle cx="782" cy="142" r="13" fill="#FFFFFF" stroke="#0F8478" stroke-width="2"/><text x="782" y="146.5" font-size="13" font-weight="700" fill="#0F8478" text-anchor="middle" data-fit="31">5</text><text x="804" y="147" font-size="14.5" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="102">Specs</text><text x="768" y="178" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="140">«Crea las specs</text><text x="768" y="195" font-size="12" font-weight="600" fill="#161A26" text-anchor="start" data-fit="140">funcionales»</text><rect x="764" y="208" width="140" height="32" rx="8" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.2"/><text x="834.0" y="229" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle" class="mono" data-fit="138">docs/specs/</text><text x="768" y="264" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="71">Agrega:</text><text x="768" y="282" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="140">Un contrato por</text><text x="768" y="299" font-size="12" font-weight="400" fill="#454C61" text-anchor="start" data-fit="140">funcionalidad</text></g><text x="48" y="332" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Cada paso lee lo que dejaron los anteriores: por eso el orden importa.</text></svg>
```

## 4. La spine

Cuéntale al agente qué servicio cubre qué. Para la red profesional:

```text
El frontend de mi app está en Flutter y se conecta
a un backend provisto por Supabase. Se usará:
- Auth para el registro, el inicio y el cierre de sesión.
- Postgres/PostgREST para usuarios, publicaciones,
  seguidores y mensajes.
- Storage para las fotos de perfil.
Especifica la arquitectura.
```

Revisa `docs/architectural_spine.md`:

- El diagrama mermaid se ve en GitHub.
- Cada invariante tiene *Regla* y *Evita*.
- No aparecen servicios que no nombraste.

## 5. Las specs funcionales

```text
Crea las specs funcionales
```

La skill propone primero la lista de funcionalidades. Corrígela antes de que escriba. Después revisa `docs/specs/`:

- Cada spec tiene sus metadatos y está en `0.1.0`.
- Ninguna nombra Supabase, Flutter ni widgets.
- Todo RF aparece en alguna spec.

## 6. Critica y corrige

```text
Critica las specs
```

```svg
<svg id="tcCritica" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 340" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tcCritica-ttl tcCritica-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tcCritica-ttl">Criticar, corregir y subir la versión</title>
  <desc id="tcCritica-dsc">Tres columnas: el primer reporte con verificabilidad 6 de 10 y ambigüedad 2; las correcciones aplicadas a F-02 y F-03; y el segundo reporte con verificabilidad 10 de 10, ambigüedad 0 y las specs en la versión 0.2.0.</desc>
  <defs>
    <style>
      #tcCritica .title{fill:#161A26;font-size:22px;font-weight:700}
      #tcCritica .sub{fill:#79809A;font-size:13.5px}
      #tcCritica .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tcCritica .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tcCritica .nb{fill:#454C61;font-size:13px}
      #tcCritica .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tcCritica .foot{fill:#79809A;font-size:12px}
      #tcCritica .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tcCritica .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tcCritica-arrow)}
    </style>
    <marker id="tcCritica-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="340" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Criticar, corregir y subir la versión</text>
  <text class="sub" x="48" y="80" data-fit="860">La crítica no cambia nada sola: propone, tú decides y la versión sube.</text>
<g><rect x="48" y="116" width="264" height="184" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="64" y="148" font-size="14.5" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="240">Reporte 1</text><text x="64" y="174" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Verificabilidad: 6/10</text><text x="64" y="193" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Ambigüedad: 2</text><text x="64" y="212" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">F-02 dice «rápido»</text><text x="64" y="231" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">F-03, CA-2: «se ve bien»</text><text x="64" y="250" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240"></text><text x="64" y="269" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">specs en 0.1.0</text></g><path class="link" d="M312,208 H346"/><g><rect x="348" y="116" width="264" height="184" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="364" y="148" font-size="14.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="240">Corregir</text><text x="364" y="174" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Tú aceptas los cambios.</text><text x="364" y="193" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">F-02: «en menos de 2 s».</text><text x="364" y="212" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">F-03, CA-2: aviso si pesa</text><text x="364" y="231" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">más de 5 MB.</text><text x="364" y="250" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240"></text><text x="364" y="269" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Historial: 0.2.0</text></g><path class="link" d="M612,208 H646"/><g><rect x="648" y="116" width="264" height="184" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="664" y="148" font-size="14.5" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="240">Reporte 2</text><text x="664" y="174" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Verificabilidad: 10/10</text><text x="664" y="193" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Ambigüedad: 0</text><text x="664" y="212" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240"></text><text x="664" y="231" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240"></text><text x="664" y="250" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240"></text><text x="664" y="269" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">specs en 0.2.0</text></g></svg>
```

Acepta las correcciones que tengan sentido y rechaza las que no. Las specs que cambien suben a `0.2.0`.

## Por qué todavía no se implementa

```svg
<svg id="tcSiguiente" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 300" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tcSiguiente-ttl tcSiguiente-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tcSiguiente-ttl">Por qué todavía no se implementa</title>
  <desc id="tcSiguiente-dsc">Tres bloques: lo que ya está, PRD, requisitos, spine y specs; lo que falta, la spec técnica y una skill de implementación que conozca las convenciones del front; y después el código.</desc>
  <defs>
    <style>
      #tcSiguiente .title{fill:#161A26;font-size:22px;font-weight:700}
      #tcSiguiente .sub{fill:#79809A;font-size:13.5px}
      #tcSiguiente .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tcSiguiente .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tcSiguiente .nb{fill:#454C61;font-size:13px}
      #tcSiguiente .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tcSiguiente .foot{fill:#79809A;font-size:12px}
      #tcSiguiente .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tcSiguiente .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tcSiguiente-arrow)}
    </style>
    <marker id="tcSiguiente-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="300" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Por qué todavía no se implementa</text>
  <text class="sub" x="48" y="80" data-fit="860">Las specs dicen qué. Para el código falta decir cómo, con las reglas del curso.</text>
<g><rect x="48" y="116" width="264" height="140" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="64" y="148" font-size="14.5" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="240">Ya está</text><text x="64" y="174" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">PRD y requisitos</text><text x="64" y="193" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Architectural spine</text><text x="64" y="212" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Specs funcionales v0.2.0</text></g><path class="link" d="M312,186 H346"/><g><rect x="348" y="116" width="264" height="140" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5" stroke-dasharray="6 5"/><text x="364" y="148" font-size="14.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="240">Falta</text><text x="364" y="174" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">La spec técnica</text><text x="364" y="193" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Una skill que conozca el front:</text><text x="364" y="212" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">Screens y Pages, setState,</text><text x="364" y="231" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">components/, imports package:</text></g><path class="link" d="M612,186 H646" stroke-dasharray="5 5"/><g opacity=".45"><rect x="648" y="116" width="264" height="140" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 5"/><text x="664" y="148" font-size="14.5" font-weight="700" fill="#556074" text-anchor="start" data-fit="240">Después</text><text x="664" y="174" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">El código, pedido spec</text><text x="664" y="193" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">por spec.</text></g></svg>
```

Las specs dicen qué hace la app. Para escribir el código falta decir cómo, con las reglas del curso: Screens y Pages, el estado con `setState`, los componentes en `components/`. Eso será otra skill, en las próximas sesiones.

## Qué debes tener al terminar

- [ ] `docs/architectural_spine.md` con diagrama e invariantes
- [ ] Una spec por funcionalidad en `docs/specs/`
- [ ] `docs/specs/README.md` con la versión y el estado de cada una
- [ ] `docs/specs/reporte.md` sin métricas en rojo
