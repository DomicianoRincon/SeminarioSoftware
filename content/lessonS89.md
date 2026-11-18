# De spec funcional a spec técnica

<!-- tags: sdd-tecnicas, spec técnica, TS-04, docs/tecnicas, tareas T-xx, impl_progress.md, preparación en Supabase, criterios de aceptación, la spec funcional no nombra tecnología -->

En la sesión 11 escribiste specs funcionales: qué hace la app, sin decir con qué. Para implementar falta el otro lado: con qué piezas se construye y en qué orden. Eso es la **spec técnica**, y la escribe la skill `sdd-tecnicas`.

```svg
<svg id="tiCadena" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tiCadena-ttl tiCadena-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tiCadena-ttl">De la spec funcional al código</title>
  <desc id="tiCadena-dsc">Tres documentos en fila. F-04, la spec funcional, dice qué hace la app sin tecnología. La skill sdd-tecnicas la lee y escribe TS-04, la spec técnica, con las piezas, los datos y los paquetes, y las tareas T-09 a T-12 pendientes en impl_progress.md. Debajo, la skill sdd-implementar toma una tarea, escribe el código en lib y la marca como hecha. Abajo a la izquierda, lo que hace la persona: preparar Supabase a mano y probar.</desc>
  <defs>
    <style>
      #tiCadena .title{fill:#161A26;font-size:22px;font-weight:700}
      #tiCadena .sub{fill:#79809A;font-size:13.5px}
      #tiCadena .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tiCadena .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tiCadena .nb{fill:#454C61;font-size:13px}
      #tiCadena .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tiCadena .foot{fill:#79809A;font-size:12px}
      #tiCadena .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tiCadena .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tiCadena-arrow)}
    </style>
    <marker id="tiCadena-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="520" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">De la spec funcional al código</text>
  <text class="sub" x="48" y="80" data-fit="860">Dos skills nuevas cierran el ciclo: una escribe las tareas y la otra las hace.</text>
<text x="48" y="132" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="103">docs/specs/</text><g><rect x="48" y="144" width="200" height="150" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="64" y="176" font-size="14.5" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="176">F-04 · funcional</text><text x="64" y="202" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="176">Qué hace la app.</text><text x="64" y="221" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="176">Sin tecnología.</text><text x="64" y="240" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="176">Criterios CA-1…CA-11.</text></g><text x="380" y="132" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="124">docs/tecnicas/</text><g><rect x="380" y="144" width="200" height="150" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><text x="396" y="176" font-size="14.5" font-weight="700" fill="#0F8478" text-anchor="start" class="mono" data-fit="176">TS-04 · técnica</text><text x="396" y="202" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="176">Con qué piezas: Screens,</text><text x="396" y="221" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="176">componentes, servicios,</text><text x="396" y="240" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="176">datos y paquetes.</text></g><text x="712" y="132" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="60">docs/</text><g><rect x="712" y="144" width="200" height="150" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="728" y="176" font-size="14.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono" data-fit="176">impl_progress.md</text><text x="728" y="202" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="176">T-09  [ ]</text><text x="728" y="221" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="176">T-10  [ ]</text><text x="728" y="240" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="176">T-11  [ ]</text><text x="728" y="259" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="176">T-12  [ ]</text></g><path class="link" d="M252,219 H372"/><rect x="257.8" y="184" width="108.4" height="24" rx="12" fill="#0F8478" stroke="#0F8478" stroke-width="1.2"/><text x="312" y="200.5" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" class="mono" data-fit="110">sdd-tecnicas</text><path class="link" d="M584,219 H704"/><rect x="599.4" y="184" width="89.2" height="24" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.2"/><text x="644" y="200.5" font-size="12" font-weight="700" fill="#0F8478" text-anchor="middle" data-fit="91">lo escribe</text><path class="link" d="M812,298 V356"/><rect x="675.0" y="316" width="130.0" height="24" rx="12" fill="#3A8235" stroke="#3A8235" stroke-width="1.2"/><text x="740" y="332.5" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" class="mono" data-fit="132">sdd-implementar</text><g><rect x="712" y="360" width="200" height="84" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/><text x="728" y="392" font-size="14.5" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="176">lib/</text><text x="728" y="418" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="176">El código de una tarea.</text></g><path class="link" d="M906,360 C940,330 940,300 906,290" stroke-dasharray="5 5"/><text x="930" y="330" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle" class="mono" data-fit="45">[x]</text><g><rect x="48" y="360" width="532" height="84" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="64" y="392" font-size="14.5" font-weight="700" fill="#A96C05" text-anchor="start" data-fit="508">Lo tuyo</text><text x="64" y="418" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="508">Revisar cada documento, hacer a mano lo que pide Supabase</text><text x="64" y="437" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="508">y probar la app al terminar cada tarea.</text></g><text x="48" y="492" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">La spec técnica sí nombra tecnología: es lo que la diferencia de la funcional.</text></svg>
```

## Dos specs, dos preguntas

La funcional responde *qué ve y qué hace el usuario*. La técnica responde *qué archivos se crean, qué estado guarda cada pantalla, qué métodos tiene cada servicio y qué paquetes hacen falta*. Cada criterio de aceptación de la funcional tiene que caer en alguna tarea de la técnica.

```svg
<svg id="tiFuncTec" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tiFuncTec-ttl tiFuncTec-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tiFuncTec-ttl">La misma regla, dicha dos veces</title>
  <desc id="tiFuncTec-dsc">Cuatro filas. Cada una une una frase de la spec funcional, sin tecnología, con su traducción técnica: el panel que sube desde abajo es showModalBottomSheet con PhotoSourceSheet; la foto que aparece sin reiniciar es copyWith dentro de setState; el historial es la ruta avatars/id/milisegundos.jpg en un bucket público; la cámara en cuatro plataformas es camera y camera_macos.</desc>
  <defs>
    <style>
      #tiFuncTec .title{fill:#161A26;font-size:22px;font-weight:700}
      #tiFuncTec .sub{fill:#79809A;font-size:13.5px}
      #tiFuncTec .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tiFuncTec .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tiFuncTec .nb{fill:#454C61;font-size:13px}
      #tiFuncTec .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tiFuncTec .foot{fill:#79809A;font-size:12px}
      #tiFuncTec .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tiFuncTec .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tiFuncTec-arrow)}
    </style>
    <marker id="tiFuncTec-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="540" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La misma regla, dicha dos veces</text>
  <text class="sub" x="48" y="80" data-fit="860">A la izquierda lo que pide F-04. A la derecha cómo lo resuelve TS-04.</text>
<text x="48" y="128" font-size="12" font-weight="700" fill="#7439B8" text-anchor="start" data-fit="131">F-04 · FUNCIONAL</text><text x="512" y="128" font-size="12" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="124">TS-04 · TÉCNICA</text><g><rect x="48" y="144" width="400" height="72" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="64" y="174" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="376">Desde abajo sube un panel con las</text><text x="64" y="193" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="376">opciones de dónde sacar la foto.</text></g><g><rect x="512" y="144" width="400" height="72" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/></g><text x="528" y="174" font-size="12" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="372">showModalBottomSheet con el componente</text><text x="528" y="194" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="372">PhotoSourceSheet: una función por opción.</text><path class="link" d="M452,180 H504"/><g><rect x="48" y="234" width="400" height="72" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="64" y="264" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="376">La foto nueva aparece en el perfil</text><text x="64" y="283" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="376">sin reiniciar la app.</text></g><g><rect x="512" y="234" width="400" height="72" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/></g><text x="528" y="264" font-size="12" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="372">_profile = _profile!.copyWith(avatarUrl: url)</text><text x="528" y="284" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="372">dentro de setState, en ProfileScreen.</text><path class="link" d="M452,270 H504"/><g><rect x="48" y="324" width="400" height="72" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="64" y="354" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="376">Cada foto subida queda en el historial,</text><text x="64" y="373" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="376">aunque ya no sea la del perfil.</text></g><g><rect x="512" y="324" width="400" height="72" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/></g><text x="528" y="354" font-size="12" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="372">avatars/&lt;id del usuario&gt;/&lt;milisegundos&gt;.jpg</text><text x="528" y="374" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="372">en un bucket público. Nunca se sobrescribe.</text><path class="link" d="M452,360 H504"/><g><rect x="48" y="414" width="400" height="72" rx="12" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="64" y="444" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="376">Se puede tomar con la cámara en</text><text x="64" y="463" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="376">Android, iOS, web y macOS.</text></g><g><rect x="512" y="414" width="400" height="72" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/></g><text x="528" y="444" font-size="12" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="372">camera en Android, iOS y web;</text><text x="528" y="464" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="372">camera_macos en macOS, según la plataforma.</text><path class="link" d="M452,450 H504"/><text x="48" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Si mañana cambia el paquete de la cámara, cambia la técnica. La funcional sigue igual.</text></svg>
```

## Qué trae una spec técnica

Abre `docs/tecnicas/TS-04-foto-de-perfil.md`. Tiene estos apartados:

- **Preparación en Supabase.** Lo que se hace a mano en el dashboard: el agente no lo puede hacer. En `TS-04` son la columna `avatar_url`, el bucket y sus policies.
- **Piezas.** Cada archivo, si es nuevo o cambia, de qué tipo es y qué tarea lo toca: `(T-09)`.
- **Estado, Datos, Paquetes y plataformas.** Dónde vive cada variable, qué columnas y rutas se usan, y lo que pide iOS, macOS, Android o web.
- **Tareas.** Cada `T-xx` con los criterios que cubre, de qué depende y cómo se prueba.

## La skill

```interactive
skill-files impl sdd-tecnicas
```

Se pide así, con la spec funcional ya aprobada:

```text
Haz la spec técnica de F-04
```

La skill lee la spec, la spine, `standard_code.md` y lo que ya hay en `lib/`, te muestra las piezas y las tareas, y **pregunta antes de escribir**. Cuando dices que sí, escribe `TS-04` y agrega las tareas, todas `[ ]`, a `impl_progress.md`.

En el repositorio de arranque esto ya está hecho: `TS-04` y sus cuatro tareas son la salida de esta skill. En tu proyecto la vas a correr tú, una vez por cada spec funcional.
