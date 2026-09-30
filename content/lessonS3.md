# ¿Qué es el frontend?

<!-- tags: frontend y backend, estados de una pantalla, cargando vacío y error, camino feliz, interfaz de usuario, multiplataforma, diseño responsivo, cliente y servidor, experiencia de usuario, una base de código -->

Hasta ahora has construido software que responde a otros programas: funciones, servicios, APIs. En este curso vas a construir la parte que responde a **personas**. Esa parte se llama **frontend**, y tiene sus propios problemas de ingeniería.

## Dos lados de una misma app

```svg
<svg id="feLados" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 472" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="feLados-ttl feLados-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="feLados-ttl">Dos lados de una misma app</title>
  <desc id="feLados-dsc">A la izquierda el frontend, que corre en el dispositivo del usuario: muestra la información, reacciona a toques y gestos y recuerda qué pasa en la pantalla. A la derecha el backend, en servidores: guarda los datos, aplica las reglas del negocio y comparte la información entre usuarios. Se comunican por la red: el frontend pide datos y el backend responde con JSON.</desc>
  <defs>
    <style>
      #feLados .title{fill:#161A26;font-size:22px;font-weight:700}
      #feLados .sub{fill:#79809A;font-size:13.5px}
      #feLados .h{font-size:13px;font-weight:700;letter-spacing:.08em}
      #feLados .hs{fill:#79809A;font-size:12px}
      #feLados .it{fill:#454C61;font-size:13px}
      #feLados .lbl{fill:#556074;font-size:12px;font-weight:600}
      #feLados .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #feLados .foot{fill:#454C61;font-size:13px}
    </style>
    <marker id="feLados-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>

  <rect width="960" height="472" rx="16" fill="#FBFBFD"/>

  <text class="title" x="48" y="56">Dos lados de una misma app</text>
  <text class="sub" x="48" y="80" data-fit="860">Lo que el usuario ve y toca, y lo que pasa lejos de él.</text>

  <rect x="48" y="112" width="352" height="296" rx="16" fill="#FAF6FF" stroke="#C9A6EE" stroke-width="1.5" stroke-dasharray="6 5"/>
  <text class="h" x="68" y="142" fill="#7439B8">FRONTEND</text>
  <text class="hs" x="68" y="160" data-fit="300">en el dispositivo del usuario</text>

  <rect x="72" y="176" width="128" height="216" rx="20" fill="#1F2430"/>
  <rect x="80" y="188" width="112" height="192" rx="12" fill="#FFFFFF"/>
  <path d="M80,200 A12,12 0 0 1 92,188 H180 A12,12 0 0 1 192,200 V216 H80 Z" fill="#EADDFF"/>
  <text x="90" y="202" dy="0.35em" fill="#1D1B20" font-size="11" font-weight="600">Mis cursos</text>
  <g fill="#C9A6EE"><circle cx="94" cy="236" r="7"/><circle cx="94" cy="268" r="7"/><circle cx="94" cy="300" r="7"/></g>
  <g fill="#D9DEE8"><rect x="106" y="230" width="70" height="6" rx="3"/><rect x="106" y="262" width="62" height="6" rx="3"/><rect x="106" y="294" width="74" height="6" rx="3"/></g>
  <g fill="#EDEFF3"><rect x="106" y="240" width="46" height="5" rx="2.5"/><rect x="106" y="272" width="52" height="5" rx="2.5"/><rect x="106" y="304" width="40" height="5" rx="2.5"/></g>
  <circle cx="174" cy="358" r="12" fill="#7439B8"/>
  <text x="174" y="358" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="700">+</text>

  <g>
    <circle cx="224" cy="214" r="4" fill="#7439B8"/>
    <text class="it" x="236" y="219" data-fit="156">Muestra la</text>
    <text class="it" x="236" y="237" data-fit="156">información</text>
    <circle cx="224" cy="270" r="4" fill="#7439B8"/>
    <text class="it" x="236" y="275" data-fit="156">Reacciona a toques</text>
    <text class="it" x="236" y="293" data-fit="156">y gestos</text>
    <circle cx="224" cy="326" r="4" fill="#7439B8"/>
    <text class="it" x="236" y="331" data-fit="156">Recuerda qué pasa</text>
    <text class="it" x="236" y="349" data-fit="156">en la pantalla</text>
  </g>

  <path d="M408,232 H552" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#feLados-arrow)"/>
  <text class="lbl" x="480" y="218" text-anchor="middle" data-fit="140">pide datos</text>
  <text class="lbl mono" x="480" y="252" text-anchor="middle" font-weight="400" data-fit="140">GET /cursos</text>
  <path d="M552,312 H408" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#feLados-arrow)"/>
  <text class="lbl" x="480" y="298" text-anchor="middle" data-fit="140">responde</text>
  <text class="lbl mono" x="480" y="332" text-anchor="middle" font-weight="400" data-fit="140">JSON</text>
  <text class="hs" x="480" y="376" text-anchor="middle" data-fit="140">por la red</text>

  <rect x="560" y="112" width="352" height="296" rx="16" fill="#F2FAF8" stroke="#86D3CA" stroke-width="1.5" stroke-dasharray="6 5"/>
  <text class="h" x="580" y="142" fill="#0F8478">BACKEND</text>
  <text class="hs" x="580" y="160" data-fit="300">en servidores, lejos del usuario</text>

  <rect x="584" y="184" width="120" height="84" rx="10" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <g fill="#86D3CA"><rect x="596" y="198" width="96" height="12" rx="3"/><rect x="596" y="218" width="96" height="12" rx="3"/><rect x="596" y="238" width="96" height="12" rx="3"/></g>
  <g fill="#0F8478"><circle cx="604" cy="204" r="2.5"/><circle cx="604" cy="224" r="2.5"/><circle cx="604" cy="244" r="2.5"/></g>
  <path d="M584,304 A60,12 0 0 1 704,304 V368 A60,12 0 0 1 584,368 Z" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <path d="M584,304 A60,12 0 0 0 704,304" fill="none" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="644" y="344" text-anchor="middle" fill="#0F8478" font-size="12" font-weight="600">datos</text>
  <line x1="644" y1="268" x2="644" y2="292" stroke="#86D3CA" stroke-width="1.5"/>

  <g>
    <circle cx="732" cy="214" r="4" fill="#0F8478"/>
    <text class="it" x="744" y="219" data-fit="156">Guarda los datos</text>
    <circle cx="732" cy="270" r="4" fill="#0F8478"/>
    <text class="it" x="744" y="275" data-fit="156">Aplica las reglas</text>
    <text class="it" x="744" y="293" data-fit="156">del negocio</text>
    <circle cx="732" cy="326" r="4" fill="#0F8478"/>
    <text class="it" x="744" y="331" data-fit="156">Comparte entre</text>
    <text class="it" x="744" y="349" data-fit="156">todos los usuarios</text>
  </g>

  <text class="foot" x="48" y="440" data-fit="860">En este curso el backend ya existe (Supabase). Tú construyes el lado izquierdo.</text>
</svg>
```

Toda app tiene dos lados. El **backend** vive en servidores: guarda los datos y aplica las reglas del negocio. El **frontend** vive en el dispositivo del usuario: muestra la información, reacciona a lo que la persona hace y recuerda qué está pasando en la pantalla. Se hablan por la red.

## Lo difícil: una pantalla, muchos estados

```svg
<svg id="feEstados" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="feEstados-ttl feEstados-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="feEstados-ttl">Una pantalla, cuatro estados</title>
  <desc id="feEstados-dsc">La misma pantalla Mis cursos dibujada cuatro veces: cargando, mientras llegan los datos; vacía, cuando no hay nada que mostrar; con error, cuando la red o el servidor fallan; y lista, con los datos. El estado lista es el único que se suele diseñar.</desc>
  <defs>
    <style>
      #feEstados .title{fill:#161A26;font-size:22px;font-weight:700}
      #feEstados .sub{fill:#79809A;font-size:13.5px}
      #feEstados .st{font-size:14px;font-weight:700}
      #feEstados .sd{fill:#454C61;font-size:12.5px}
      #feEstados .sc{fill:#454C61;font-size:10.5px}
    </style>
  </defs>
  <rect width="960" height="520" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Una pantalla, cuatro estados</text>
  <text class="sub" x="48" y="80" data-fit="860">El usuario ve todos. El que casi siempre se diseña es solo el último.</text>
  <rect x="76" y="120" width="160" height="288" rx="22" fill="#1F2430"/>
  <rect x="84" y="132" width="144" height="264" rx="14" fill="#FFFFFF"/>
  <path d="M84,146 A14,14 0 0 1 98,132 H214 A14,14 0 0 1 228,146 V164 H84 Z" fill="#EADDFF"/>
  <text x="96" y="149" dy="0.35em" fill="#1D1B20" font-size="11.5" font-weight="600">Mis cursos</text>
  <circle cx="102" cy="190" r="9" fill="#EDEFF3"/>
  <rect x="118" y="183" width="90" height="7" rx="3.5" fill="#EDEFF3"/>
  <rect x="118" y="194" width="56" height="6" rx="3" fill="#F3F4F7"/>
  <circle cx="102" cy="230" r="9" fill="#EDEFF3"/>
  <rect x="118" y="223" width="84" height="7" rx="3.5" fill="#EDEFF3"/>
  <rect x="118" y="234" width="60" height="6" rx="3" fill="#F3F4F7"/>
  <circle cx="102" cy="270" r="9" fill="#EDEFF3"/>
  <rect x="118" y="263" width="78" height="7" rx="3.5" fill="#EDEFF3"/>
  <rect x="118" y="274" width="64" height="6" rx="3" fill="#F3F4F7"/>
  <circle cx="102" cy="310" r="9" fill="#EDEFF3"/>
  <rect x="118" y="303" width="72" height="7" rx="3.5" fill="#EDEFF3"/>
  <rect x="118" y="314" width="68" height="6" rx="3" fill="#F3F4F7"/>
  <circle cx="156" cy="356" r="12" fill="none" stroke="#F0C572" stroke-width="3"/>
  <path d="M156,344 A12,12 0 0 1 168,356" fill="none" stroke="#A96C05" stroke-width="3" stroke-linecap="round"/>
  <rect x="108" y="426" width="96" height="26" rx="13" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.25"/>
  <text class="st" x="156" y="439" dy="0.35em" text-anchor="middle" fill="#A96C05" data-fit="90">Cargando</text>
  <text class="sd" x="156" y="468" text-anchor="middle" data-fit="200">mientras llegan</text>
  <text class="sd" x="156" y="486" text-anchor="middle" data-fit="200">los datos</text>
  <rect x="292" y="120" width="160" height="288" rx="22" fill="#1F2430"/>
  <rect x="300" y="132" width="144" height="264" rx="14" fill="#FFFFFF"/>
  <path d="M300,146 A14,14 0 0 1 314,132 H430 A14,14 0 0 1 444,146 V164 H300 Z" fill="#EADDFF"/>
  <text x="312" y="149" dy="0.35em" fill="#1D1B20" font-size="11.5" font-weight="600">Mis cursos</text>
  <path d="M350,234 L372,222 L394,234 L394,262 L350,262 Z" fill="none" stroke="#A0A8B8" stroke-width="2" stroke-linejoin="round"/>
  <path d="M350,234 L372,246 L394,234 M372,246 V262" fill="none" stroke="#A0A8B8" stroke-width="2" stroke-linejoin="round"/>
  <text class="sc" x="372" y="290" text-anchor="middle" data-fit="160">Aún no tienes cursos</text>
  <rect x="332" y="306" width="80" height="26" rx="13" fill="none" stroke="#7439B8" stroke-width="1.5"/>
  <text x="372" y="319" dy="0.35em" text-anchor="middle" fill="#7439B8" font-size="11" font-weight="600">Explorar</text>
  <rect x="324" y="426" width="96" height="26" rx="13" fill="#EFF1F5" stroke="#556074" stroke-width="1.25"/>
  <text class="st" x="372" y="439" dy="0.35em" text-anchor="middle" fill="#556074" data-fit="90">Vacía</text>
  <text class="sd" x="372" y="468" text-anchor="middle" data-fit="200">cuando no hay nada</text>
  <text class="sd" x="372" y="486" text-anchor="middle" data-fit="200">que mostrar</text>
  <rect x="508" y="120" width="160" height="288" rx="22" fill="#1F2430"/>
  <rect x="516" y="132" width="144" height="264" rx="14" fill="#FFFFFF"/>
  <path d="M516,146 A14,14 0 0 1 530,132 H646 A14,14 0 0 1 660,146 V164 H516 Z" fill="#EADDFF"/>
  <text x="528" y="149" dy="0.35em" fill="#1D1B20" font-size="11.5" font-weight="600">Mis cursos</text>
  <circle cx="588" cy="242" r="20" fill="#FFEBEF" stroke="#C2354F" stroke-width="2"/>
  <text x="588" y="242" dy="0.35em" text-anchor="middle" fill="#C2354F" font-size="20" font-weight="700">!</text>
  <text class="sc" x="588" y="284" text-anchor="middle" data-fit="130">Sin conexión</text>
  <rect x="544" y="300" width="88" height="26" rx="13" fill="#C2354F"/>
  <text x="588" y="313" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="11" font-weight="600">Reintentar</text>
  <rect x="540" y="426" width="96" height="26" rx="13" fill="#FFEBEF" stroke="#C2354F" stroke-width="1.25"/>
  <text class="st" x="588" y="439" dy="0.35em" text-anchor="middle" fill="#C2354F" data-fit="90">Con error</text>
  <text class="sd" x="588" y="468" text-anchor="middle" data-fit="200">cuando la red o</text>
  <text class="sd" x="588" y="486" text-anchor="middle" data-fit="200">el servidor fallan</text>
  <rect x="724" y="120" width="160" height="288" rx="22" fill="#1F2430"/>
  <rect x="732" y="132" width="144" height="264" rx="14" fill="#FFFFFF"/>
  <path d="M732,146 A14,14 0 0 1 746,132 H862 A14,14 0 0 1 876,146 V164 H732 Z" fill="#EADDFF"/>
  <text x="744" y="149" dy="0.35em" fill="#1D1B20" font-size="11.5" font-weight="600">Mis cursos</text>
  <circle cx="750" cy="190" r="9" fill="#C9A6EE"/>
  <text x="766" y="190" fill="#1D1B20" font-size="11" font-weight="600">Cálculo I</text>
  <rect x="766" y="195" width="56" height="5" rx="2.5" fill="#EDEFF3"/>
  <circle cx="750" cy="230" r="9" fill="#86D3CA"/>
  <text x="766" y="230" fill="#1D1B20" font-size="11" font-weight="600">Física</text>
  <rect x="766" y="235" width="62" height="5" rx="2.5" fill="#EDEFF3"/>
  <circle cx="750" cy="270" r="9" fill="#F0C572"/>
  <text x="766" y="270" fill="#1D1B20" font-size="11" font-weight="600">Seminario</text>
  <rect x="766" y="275" width="68" height="5" rx="2.5" fill="#EDEFF3"/>
  <circle cx="750" cy="310" r="9" fill="#A9B4F2"/>
  <text x="766" y="310" fill="#1D1B20" font-size="11" font-weight="600">Inglés</text>
  <rect x="766" y="315" width="74" height="5" rx="2.5" fill="#EDEFF3"/>
  <circle cx="854" cy="374" r="13" fill="#7439B8"/>
  <text x="854" y="374" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="16" font-weight="700">+</text>
  <rect x="756" y="426" width="96" height="26" rx="13" fill="#E8F6E3" stroke="#3A8235" stroke-width="1.25"/>
  <text class="st" x="804" y="439" dy="0.35em" text-anchor="middle" fill="#3A8235" data-fit="90">Lista</text>
  <text class="sd" x="804" y="468" text-anchor="middle" data-fit="200">con los datos:</text>
  <text class="sd" x="804" y="486" text-anchor="middle" data-fit="200">el camino feliz</text>
</svg>
```

Un backend recibe peticiones con un formato fijo y responde. Un frontend, en cambio, recibe **personas**: tocan dos veces, se quedan sin señal, abren la app sin datos todavía. Cada una de esas situaciones es un **estado** de la pantalla, y el usuario ve todos.

El error típico de quien empieza es diseñar solo el estado *Lista*, el camino feliz. Una app bien hecha decide también qué se ve mientras carga, cuando no hay nada y cuando algo falla.

## Y muchas pantallas donde correr

```svg
<svg id="feLugares" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 456" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="feLugares-ttl feLugares-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="feLugares-ttl">Una base de código, muchas pantallas</title>
  <desc id="feLugares-dsc">Un mismo código de Flutter corre en un celular, una tablet y un navegador. En el celular la lista ocupa todo; en la tablet las tarjetas se reparten en dos columnas; en el navegador hay un menú lateral y tres columnas.</desc>
  <defs>
    <style>
      #feLugares .title{fill:#161A26;font-size:22px;font-weight:700}
      #feLugares .sub{fill:#79809A;font-size:13.5px}
      #feLugares .dn{fill:#161A26;font-size:14px;font-weight:700}
      #feLugares .dd{fill:#454C61;font-size:12.5px}
      #feLugares .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
    </style>
    <marker id="feLugares-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/>
    </marker>
  </defs>
  <rect width="960" height="456" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Una base de código, muchas pantallas</text>
  <text class="sub" x="48" y="80" data-fit="860">Flutter lleva la misma app a celular, tablet y web. Que se vea bien en cada una es trabajo tuyo.</text>
  <rect x="48" y="144" width="208" height="208" rx="12" fill="#1F2430"/>
  <path d="M48,156 A12,12 0 0 1 60,144 H244 A12,12 0 0 1 256,156 V172 H48 Z" fill="#2A3040"/>
  <text class="mono" x="62" y="158" dy="0.35em" fill="#9AA3B5" font-size="11">lib/main.dart</text>
  <rect x="64" y="188" width="40" height="7" rx="3.5" fill="#569CD6" opacity="0.85"/>
  <rect x="110" y="205" width="60" height="7" rx="3.5" fill="#DCDCAA" opacity="0.85"/>
  <rect x="76" y="222" width="90" height="7" rx="3.5" fill="#D4D8E3" opacity="0.85"/>
  <rect x="88" y="239" width="70" height="7" rx="3.5" fill="#4EC9B0" opacity="0.85"/>
  <rect x="88" y="256" width="100" height="7" rx="3.5" fill="#D4D8E3" opacity="0.85"/>
  <rect x="100" y="273" width="56" height="7" rx="3.5" fill="#CE9178" opacity="0.85"/>
  <rect x="88" y="290" width="80" height="7" rx="3.5" fill="#D4D8E3" opacity="0.85"/>
  <rect x="76" y="307" width="50" height="7" rx="3.5" fill="#DCDCAA" opacity="0.85"/>
  <rect x="64" y="324" width="24" height="7" rx="3.5" fill="#D4D8E3" opacity="0.85"/>
  <text class="dn" x="48" y="384" data-fit="208">Una base de código</text>
  <text class="dd" x="48" y="404" data-fit="208">Flutter · Dart</text>
  <path d="M264,248 H296" fill="none" stroke="#4453C9" stroke-width="2" marker-end="url(#feLugares-arrow)"/>
  <path d="M308,152 V344" stroke="#4453C9" stroke-width="2" stroke-linecap="round"/>
  <rect x="328" y="152" width="96" height="192" rx="16" fill="#1F2430"/>
  <rect x="334" y="162" width="84" height="172" rx="10" fill="#FFFFFF"/>
  <path d="M334,172 A10,10 0 0 1 344,162 H408 A10,10 0 0 1 418,172 V184 H334 Z" fill="#EADDFF"/>
  <circle cx="345" cy="201" r="5" fill="#C9A6EE"/>
  <rect x="355" y="197" width="52" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="355" y="205" width="34" height="4" rx="2" fill="#EDEFF3"/>
  <circle cx="345" cy="227" r="5" fill="#86D3CA"/>
  <rect x="355" y="223" width="49" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="355" y="231" width="36" height="4" rx="2" fill="#EDEFF3"/>
  <circle cx="345" cy="253" r="5" fill="#F0C572"/>
  <rect x="355" y="249" width="46" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="355" y="257" width="38" height="4" rx="2" fill="#EDEFF3"/>
  <circle cx="345" cy="279" r="5" fill="#A9B4F2"/>
  <rect x="355" y="275" width="43" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="355" y="283" width="40" height="4" rx="2" fill="#EDEFF3"/>
  <circle cx="345" cy="305" r="5" fill="#F3A3B2"/>
  <rect x="355" y="301" width="40" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="355" y="309" width="42" height="4" rx="2" fill="#EDEFF3"/>
  <rect x="456" y="144" width="160" height="208" rx="16" fill="#1F2430"/>
  <rect x="464" y="154" width="144" height="188" rx="10" fill="#FFFFFF"/>
  <path d="M464,164 A10,10 0 0 1 474,154 H598 A10,10 0 0 1 608,164 V178 H464 Z" fill="#EADDFF"/>
  <rect x="472" y="190" width="60" height="62" rx="6" fill="#F7F4FD" stroke="#E4D8F8"/>
  <rect x="472" y="190" width="60" height="26" rx="6" fill="#C9A6EE" opacity="0.7"/>
  <rect x="478" y="224" width="40" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="478" y="234" width="28" height="4" rx="2" fill="#EDEFF3"/>
  <rect x="540" y="190" width="60" height="62" rx="6" fill="#F7F4FD" stroke="#E4D8F8"/>
  <rect x="540" y="190" width="60" height="26" rx="6" fill="#86D3CA" opacity="0.7"/>
  <rect x="546" y="224" width="40" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="546" y="234" width="28" height="4" rx="2" fill="#EDEFF3"/>
  <rect x="472" y="262" width="60" height="62" rx="6" fill="#F7F4FD" stroke="#E4D8F8"/>
  <rect x="472" y="262" width="60" height="26" rx="6" fill="#F0C572" opacity="0.7"/>
  <rect x="478" y="296" width="40" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="478" y="306" width="28" height="4" rx="2" fill="#EDEFF3"/>
  <rect x="540" y="262" width="60" height="62" rx="6" fill="#F7F4FD" stroke="#E4D8F8"/>
  <rect x="540" y="262" width="60" height="26" rx="6" fill="#A9B4F2" opacity="0.7"/>
  <rect x="546" y="296" width="40" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="546" y="306" width="28" height="4" rx="2" fill="#EDEFF3"/>
  <rect x="648" y="144" width="264" height="208" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M648,154 A10,10 0 0 1 658,144 H902 A10,10 0 0 1 912,154 V170 H648 Z" fill="#E8EAEF"/>
  <circle cx="660" cy="157" r="3.5" fill="#F14C4C"/><circle cx="672" cy="157" r="3.5" fill="#E5C07B"/><circle cx="684" cy="157" r="3.5" fill="#6BCB77"/>
  <rect x="700" y="150" width="200" height="14" rx="7" fill="#FFFFFF"/>
  <rect x="649" y="170" width="46" height="181" fill="#F4EBFF"/>
  <rect x="662" y="186" width="20" height="14" rx="4" fill="#7439B8"/>
  <rect x="662" y="214" width="20" height="14" rx="4" fill="#C9A6EE"/>
  <rect x="662" y="242" width="20" height="14" rx="4" fill="#C9A6EE"/>
  <rect x="662" y="270" width="20" height="14" rx="4" fill="#C9A6EE"/>
  <path d="M695,170 H911 V190 H695 Z" fill="#EADDFF"/>
  <rect x="705" y="202" width="60" height="62" rx="6" fill="#F7F4FD" stroke="#E4D8F8"/>
  <rect x="705" y="202" width="60" height="26" rx="6" fill="#C9A6EE" opacity="0.7"/>
  <rect x="711" y="236" width="40" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="711" y="246" width="28" height="4" rx="2" fill="#EDEFF3"/>
  <rect x="773" y="202" width="60" height="62" rx="6" fill="#F7F4FD" stroke="#E4D8F8"/>
  <rect x="773" y="202" width="60" height="26" rx="6" fill="#86D3CA" opacity="0.7"/>
  <rect x="779" y="236" width="40" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="779" y="246" width="28" height="4" rx="2" fill="#EDEFF3"/>
  <rect x="841" y="202" width="60" height="62" rx="6" fill="#F7F4FD" stroke="#E4D8F8"/>
  <rect x="841" y="202" width="60" height="26" rx="6" fill="#F0C572" opacity="0.7"/>
  <rect x="847" y="236" width="40" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="847" y="246" width="28" height="4" rx="2" fill="#EDEFF3"/>
  <rect x="705" y="274" width="60" height="62" rx="6" fill="#F7F4FD" stroke="#E4D8F8"/>
  <rect x="705" y="274" width="60" height="26" rx="6" fill="#A9B4F2" opacity="0.7"/>
  <rect x="711" y="308" width="40" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="711" y="318" width="28" height="4" rx="2" fill="#EDEFF3"/>
  <rect x="773" y="274" width="60" height="62" rx="6" fill="#F7F4FD" stroke="#E4D8F8"/>
  <rect x="773" y="274" width="60" height="26" rx="6" fill="#F3A3B2" opacity="0.7"/>
  <rect x="779" y="308" width="40" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="779" y="318" width="28" height="4" rx="2" fill="#EDEFF3"/>
  <rect x="841" y="274" width="60" height="62" rx="6" fill="#F7F4FD" stroke="#E4D8F8"/>
  <rect x="841" y="274" width="60" height="26" rx="6" fill="#C9A6EE" opacity="0.7"/>
  <rect x="847" y="308" width="40" height="5" rx="2.5" fill="#D9DEE8"/>
  <rect x="847" y="318" width="28" height="4" rx="2" fill="#EDEFF3"/>
  <text class="dn" x="376" y="384" text-anchor="middle" data-fit="200">Celular</text>
  <text class="dd" x="376" y="406" text-anchor="middle" data-fit="150">pantalla chica,</text>
  <text class="dd" x="376" y="424" text-anchor="middle" data-fit="150">se usa con el dedo</text>
  <text class="dn" x="536" y="384" text-anchor="middle" data-fit="200">Tablet</text>
  <text class="dd" x="536" y="406" text-anchor="middle" data-fit="150">más espacio,</text>
  <text class="dd" x="536" y="424" text-anchor="middle" data-fit="150">otra distribución</text>
  <text class="dn" x="780" y="384" text-anchor="middle" data-fit="200">Navegador</text>
  <text class="dd" x="780" y="406" text-anchor="middle" data-fit="250">mouse y teclado, en una</text>
  <text class="dd" x="780" y="424" text-anchor="middle" data-fit="250">ventana que cambia de tamaño</text>
</svg>
```

Con Flutter escribes la app una sola vez y corre en celular, tablet y navegador. Pero una pantalla chica no se usa igual que una ventana de escritorio: cada una pide su propia distribución, y resolverlo es parte del trabajo.

## La idea que guía el curso

En el frontend moderno la pantalla no se modifica a mano: **se describe a partir del estado**.

> **interfaz = f(estado)**

Cuando el estado cambia (llegaron los datos, falló la red, el usuario tocó un botón), la interfaz se vuelve a dibujar sola. Sobre esa idea están construidas las próximas sesiones: componentes, pantallas, estado y navegación.
