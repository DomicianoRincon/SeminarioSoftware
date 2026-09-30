# Desarrollar con IA

<!-- tags: human in the lead, agente de IA en consola, tool system, Claude Code, OpenCode, Antigravity CLI, permisos del agente, revisar código generado, entender los conceptos, desarrollo asistido por IA, aprobar a ciegas, ejecutar comandos -->

En este curso vas a programar con un asistente de IA al lado. No para que piense por ti: para que escriba y ejecute mientras **tú diriges**.

## A mano o potenciado con IA

```svg
<svg id="iaManos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 500" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="iaManos-ttl iaManos-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="iaManos-ttl">A mano o potenciado con IA</title>
  <desc id="iaManos-dsc">A mano, tú haces los cuatro pasos: buscar cómo se hace, escribir cada línea, ejecutar y leer errores, y corregir. Con IA, tú decides qué y por qué, la IA escribe y ejecuta, y tú revisas y entiendes. Por eso los conceptos importan más: no puedes revisar lo que no entiendes.</desc>
  <defs>
    <style>
      #iaManos .title{fill:#161A26;font-size:22px;font-weight:700}
      #iaManos .sub{fill:#79809A;font-size:13.5px}
      #iaManos .h{font-size:13px;font-weight:700;letter-spacing:.08em}
      #iaManos .row{fill:#454C61;font-size:13.5px}
      #iaManos .tag{fill:#FFFFFF;font-size:11px;font-weight:700;letter-spacing:.04em}
      #iaManos .cap{fill:#454C61;font-size:13px;font-style:italic}
    </style>
  </defs>
  <rect width="960" height="500" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">A mano o potenciado con IA</text>
  <text class="sub" x="48" y="80" data-fit="860">Cambia quién escribe el código. No cambia quién tiene que entenderlo.</text>
  <rect x="48" y="112" width="408" height="288" rx="16" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="72" y="144" fill="#556074">A MANO</text>
  <rect x="72" y="164" width="360" height="38" rx="10" fill="#EEF1FF"/>
  <rect x="82" y="173" width="36" height="20" rx="10" fill="#4453C9"/>
  <text class="tag" x="100" y="183" dy="0.35em" text-anchor="middle">TÚ</text>
  <text class="row" x="132" y="183" dy="0.35em" data-fit="290">Buscas cómo se hace</text>
  <rect x="72" y="212" width="360" height="38" rx="10" fill="#EEF1FF"/>
  <rect x="82" y="221" width="36" height="20" rx="10" fill="#4453C9"/>
  <text class="tag" x="100" y="231" dy="0.35em" text-anchor="middle">TÚ</text>
  <text class="row" x="132" y="231" dy="0.35em" data-fit="290">Escribes cada línea</text>
  <rect x="72" y="260" width="360" height="38" rx="10" fill="#EEF1FF"/>
  <rect x="82" y="269" width="36" height="20" rx="10" fill="#4453C9"/>
  <text class="tag" x="100" y="279" dy="0.35em" text-anchor="middle">TÚ</text>
  <text class="row" x="132" y="279" dy="0.35em" data-fit="290">Ejecutas y lees los errores</text>
  <rect x="72" y="308" width="360" height="38" rx="10" fill="#EEF1FF"/>
  <rect x="82" y="317" width="36" height="20" rx="10" fill="#4453C9"/>
  <text class="tag" x="100" y="327" dy="0.35em" text-anchor="middle">TÚ</text>
  <text class="row" x="132" y="327" dy="0.35em" data-fit="290">Corriges y vuelves a empezar</text>
  <text class="cap" x="72" y="380" data-fit="360">Tu tiempo se va en escribir.</text>
  <rect x="504" y="112" width="408" height="288" rx="16" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="528" y="144" fill="#7439B8">POTENCIADO CON IA</text>
  <rect x="528" y="164" width="360" height="38" rx="10" fill="#EEF1FF"/>
  <rect x="538" y="173" width="36" height="20" rx="10" fill="#4453C9"/>
  <text class="tag" x="556" y="183" dy="0.35em" text-anchor="middle">TÚ</text>
  <text class="row" x="588" y="183" dy="0.35em" data-fit="290">Decides qué se hace y por qué</text>
  <rect x="528" y="212" width="360" height="38" rx="10" fill="#F4EBFF"/>
  <rect x="538" y="221" width="36" height="20" rx="10" fill="#7439B8"/>
  <text class="tag" x="556" y="231" dy="0.35em" text-anchor="middle">IA</text>
  <text class="row" x="588" y="231" dy="0.35em" data-fit="290">Escribe el código y lo ejecuta</text>
  <rect x="528" y="260" width="360" height="38" rx="10" fill="#EEF1FF"/>
  <rect x="538" y="269" width="36" height="20" rx="10" fill="#4453C9"/>
  <text class="tag" x="556" y="279" dy="0.35em" text-anchor="middle">TÚ</text>
  <text class="row" x="588" y="279" dy="0.35em" data-fit="290">Revisas y entiendes lo que hizo</text>
  <text class="cap" x="528" y="380" data-fit="360">Tu tiempo se va en pensar y en revisar.</text>
  <rect x="48" y="420" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/>
  <text x="68" y="446" dy="0.35em" fill="#7C4F04" font-size="14" data-fit="820"><tspan font-weight="700">Por eso los conceptos importan más, no menos:</tspan> no puedes revisar lo que no entiendes.</text>
</svg>
```

Con IA escribes menos código, pero tienes que entender más. Si no sabes qué es un estado o un componente, no puedes saber si lo que hizo la IA está bien.

## De un chat a un agente

```svg
<svg id="iaTools" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 468" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="iaTools-ttl iaTools-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="iaTools-ttl">De un chat a un agente</title>
  <desc id="iaTools-dsc">En un chat en la web la IA solo responde texto y tú copias y pegas en tu proyecto. Un agente en consola tiene un tool system: herramientas para leer archivos, buscar en el código, editar archivos y ejecutar comandos, que usa directamente sobre tu proyecto.</desc>
  <defs>
    <style>
      #iaTools .title{fill:#161A26;font-size:22px;font-weight:700}
      #iaTools .sub{fill:#79809A;font-size:13.5px}
      #iaTools .h{font-size:13px;font-weight:700;letter-spacing:.08em}
      #iaTools .lbl{fill:#556074;font-size:12px;font-weight:600}
      #iaTools .tool{fill:#7439B8;font-size:12.5px;font-weight:600}
      #iaTools .cap{fill:#454C61;font-size:13.5px}
      #iaTools .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
    </style>
    <marker id="iaTools-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
    <marker id="iaTools-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#79809A"/></marker>
  </defs>
  <rect width="960" height="468" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">De un chat a un agente</text>
  <text class="sub" x="48" y="80" data-fit="860">La diferencia no es el modelo de IA: es a qué tiene acceso.</text>
  <rect x="48" y="112" width="408" height="296" rx="16" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="72" y="144" fill="#556074">CHAT EN LA WEB</text>
  <rect x="72" y="164" width="176" height="164" rx="10" fill="#F5F7FA" stroke="#C4CBD8" stroke-width="1.25"/>
  <rect x="140" y="178" width="96" height="22" rx="11" fill="#EEF1FF"/>
  <rect x="152" y="187" width="72" height="5" rx="2.5" fill="#A9B4F2"/>
  <rect x="84" y="212" width="140" height="96" rx="10" fill="#F4EBFF"/>
  <rect x="96" y="226" width="90" height="5" rx="2.5" fill="#C9A6EE"/>
  <rect x="96" y="238" width="110" height="5" rx="2.5" fill="#C9A6EE"/>
  <rect x="96" y="250" width="70" height="5" rx="2.5" fill="#C9A6EE"/>
  <rect x="96" y="264" width="116" height="32" rx="5" fill="#1F2430"/>
  <rect x="104" y="273" width="60" height="4" rx="2" fill="#DCDCAA"/><rect x="104" y="283" width="84" height="4" rx="2" fill="#9AA3B5"/>
  <path d="M256,246 H336" fill="none" stroke="#79809A" stroke-width="1.75" stroke-dasharray="6 5" marker-end="url(#iaTools-g)"/>
  <circle cx="296" cy="246" r="13" fill="#FFFFFF" stroke="#4453C9" stroke-width="1.75"/>
  <circle cx="296" cy="242" r="3.5" fill="#4453C9"/><path d="M289,253 A7,6 0 0 1 303,253" fill="#4453C9"/>
  <text class="lbl" x="296" y="280" text-anchor="middle">tú copias</text><text class="lbl" x="296" y="296" text-anchor="middle">y pegas</text>
  <path d="M348,222 Q348,212 358,212 H374 L382,222 H410 Q420,222 420,232 V264 Q420,274 410,274 H358 Q348,274 348,264 Z" fill="#E3F6F3" stroke="#0F8478" stroke-width="1.75"/>
  <text x="384" y="296" text-anchor="middle" fill="#0F8478" font-size="12.5" font-weight="700">Tu</text>
  <text x="384" y="312" text-anchor="middle" fill="#0F8478" font-size="12.5" font-weight="700">proyecto</text>
  <text class="cap" x="72" y="388" data-fit="360">La IA solo habla. <tspan font-weight="700">Tú haces el resto.</tspan></text>
  <rect x="504" y="112" width="408" height="296" rx="16" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="2"/>
  <text class="h" x="528" y="144" fill="#7439B8">AGENTE EN CONSOLA</text>
  <rect x="528" y="209" width="96" height="84" rx="12" fill="#7439B8"/>
  <text x="576" y="243" text-anchor="middle" fill="#FFFFFF" font-size="14" font-weight="700">Modelo</text>
  <text x="576" y="261" text-anchor="middle" fill="#FFFFFF" font-size="14" font-weight="700">de IA</text>
  <path d="M624,251 L652,188" fill="none" stroke="#C9A6EE" stroke-width="1.5"/>
  <rect x="656" y="172" width="140" height="32" rx="16" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tool" x="726" y="188" dy="0.35em" text-anchor="middle" data-fit="150">Leer archivos</text>
  <path d="M796,188 L812,251" fill="none" stroke="#7439B8" stroke-width="1.5" marker-end="url(#iaTools-a)"/>
  <path d="M624,251 L652,230" fill="none" stroke="#C9A6EE" stroke-width="1.5"/>
  <rect x="656" y="214" width="140" height="32" rx="16" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tool" x="726" y="230" dy="0.35em" text-anchor="middle" data-fit="150">Buscar en el código</text>
  <path d="M796,230 L812,251" fill="none" stroke="#7439B8" stroke-width="1.5" marker-end="url(#iaTools-a)"/>
  <path d="M624,251 L652,272" fill="none" stroke="#C9A6EE" stroke-width="1.5"/>
  <rect x="656" y="256" width="140" height="32" rx="16" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tool" x="726" y="272" dy="0.35em" text-anchor="middle" data-fit="150">Editar archivos</text>
  <path d="M796,272 L812,251" fill="none" stroke="#7439B8" stroke-width="1.5" marker-end="url(#iaTools-a)"/>
  <path d="M624,251 L652,314" fill="none" stroke="#C9A6EE" stroke-width="1.5"/>
  <rect x="656" y="298" width="140" height="32" rx="16" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tool" x="726" y="314" dy="0.35em" text-anchor="middle" data-fit="150">Ejecutar comandos</text>
  <path d="M796,314 L812,251" fill="none" stroke="#7439B8" stroke-width="1.5" marker-end="url(#iaTools-a)"/>
  <path d="M820,230 Q820,220 830,220 H846 L854,230 H882 Q892,230 892,240 V272 Q892,282 882,282 H830 Q820,282 820,272 Z" fill="#E3F6F3" stroke="#0F8478" stroke-width="1.75"/>
  <text x="856" y="304" text-anchor="middle" fill="#0F8478" font-size="12.5" font-weight="700">Tu</text>
  <text x="856" y="320" text-anchor="middle" fill="#0F8478" font-size="12.5" font-weight="700">proyecto</text>
  <rect x="652" y="160" width="148" height="182" rx="12" fill="none" stroke="#C9A6EE" stroke-width="1.25" stroke-dasharray="5 4"/>
  <text x="726" y="358" text-anchor="middle" fill="#7439B8" font-size="12" font-weight="700" letter-spacing=".06em">TOOL SYSTEM</text>
  <text class="cap" x="528" y="388" data-fit="370">La IA lee, edita y <tspan font-weight="700">ejecuta en tu proyecto.</tspan></text>
  <text x="48" y="440" fill="#454C61" font-size="13.5" data-fit="860">Como puede tocar tus archivos y tu terminal, el agente <tspan font-weight="700">pide permiso</tspan> antes de las acciones delicadas.</text>
</svg>
```

Herramientas como **Claude Code**, **OpenCode CLI** o **Antigravity CLI** corren en la consola, dentro de tu proyecto. Su **tool system** es el conjunto de herramientas que el modelo puede usar: leer tus archivos, buscar en el código, editarlos y ejecutar comandos por ti.

## Un agente en acción

```svg
<svg id="iaAgente" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 694" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="iaAgente-ttl iaAgente-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="iaAgente-ttl">Un agente en acción</title>
  <desc id="iaAgente-dsc">Sesión de un agente en consola: la persona pide agregar un botón que reinicie el contador; el agente lee y edita lib/main.dart, pide permiso para ejecutar flutter analyze, lo ejecuta y reporta lo que hizo.</desc>
  <defs>
    <style>
      #iaAgente .title{fill:#161A26;font-size:22px;font-weight:700}
      #iaAgente .sub{fill:#79809A;font-size:13.5px}
      #iaAgente .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #iaAgente .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #iaAgente .pf{fill:#7F8AA3} #iaAgente .cmd{fill:#FFFFFF;font-weight:600}
      #iaAgente .dim{fill:#8A93A6} #iaAgente .okk{fill:#6BCB77;font-weight:600}
      #iaAgente .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #iaAgente .chipc{fill:#F2C069} #iaAgente .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #iaAgente .ct{fill:#161A26;font-size:14px;font-weight:700}
      #iaAgente .cb{fill:#454C61;font-size:13px}
      #iaAgente .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="694" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Un agente en acción</text>
  <text class="sub" x="48" y="80" data-fit="860">Así se ve una sesión en Claude Code, simplificada y en español. En OpenCode o Antigravity CLI el flujo es parecido.</text>
  <rect x="48" y="112" width="864" height="424" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\miapp1</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816"><tspan class="pf">miapp1&gt; </tspan><tspan class="cmd">claude</tspan></text>
  <text class="tl mono" font-size="13" x="72" y="226" data-fit="816">&gt; Agrega un botón que reinicie el contador a cero</text>
  <text class="tl mono" font-size="13" x="72" y="278" data-fit="816">● Leer lib/main.dart</text>
  <text class="tl mono" font-size="13" x="72" y="304" data-fit="816">● Editar lib/main.dart   (+9 −1)</text>
  <text class="tl mono" font-size="13" x="72" y="356" data-fit="816">? ¿Permites ejecutar este comando?  flutter analyze</text>
  <text class="tl mono" font-size="13" x="72" y="382" data-fit="816">  1. Sí    2. Sí, y no volver a preguntar    3. No</text>
  <text class="tl mono" font-size="13" x="72" y="434" data-fit="816">● Ejecutar flutter analyze</text>
  <text class="tl mono dim" font-size="13" x="72" y="460" data-fit="816">  No issues found!</text>
  <text class="tl mono okk" font-size="13" x="72" y="512" data-fit="816">Listo: agregué un botón "Reiniciar" que vuelve el contador a 0.</text>
  <rect class="ring" x="68.0" y="210" width="390.2" height="22" rx="5"/>
  <circle class="chipc" cx="458.2" cy="211" r="8"/>
  <text class="chipt" x="458.2" y="211" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="68.0" y="288" width="179.6" height="22" rx="5"/>
  <circle class="chipc" cx="247.6" cy="289" r="8"/>
  <text class="chipt" x="247.6" y="289" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <rect class="ring" x="83.6" y="366" width="382.4" height="22" rx="5"/>
  <circle class="chipc" cx="466.0" cy="367" r="8"/>
  <text class="chipt" x="466.0" y="367" dy="0.35em" text-anchor="middle" font-size="10.5">3</text>
  <g transform="translate(48.0,560)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">Tú pides</text>
    <text class="cb" x="16" y="60" data-fit="250">En lenguaje natural: qué quieres,</text>
    <text class="cb" x="16" y="79" data-fit="245">no cómo se escribe.</text>
  </g>
  <g transform="translate(341.3,560)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">La IA usa herramientas</text>
    <text class="cb" x="16" y="60" data-fit="245">Lee y edita tus archivos. Cada</text>
    <text class="cb" x="16" y="79" data-fit="245">acción queda a la vista.</text>
  </g>
  <g transform="translate(634.7,560)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">3</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">Tú autorizas</text>
    <text class="cb" x="16" y="60" data-fit="245">Antes de ejecutar un comando</text>
    <text class="cb" x="16" y="79" data-fit="245">pide permiso. Tú decides.</text>
  </g>
</svg>
```

Se abre desde la carpeta del proyecto, con el comando de cada herramienta. Por ejemplo, con Claude Code:

```shell
claude
```

## Tú al mando

```svg
<svg id="iaMando" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 492" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="iaMando-ttl iaMando-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="iaMando-ttl">Tú al mando: human in the lead</title>
  <desc id="iaMando-dsc">Un ciclo de cuatro pasos: tú defines qué, por qué y con qué reglas; la IA propone y hace los cambios con sus herramientas; tú revisas si entiendes lo que hizo; tú decides si aceptas, corriges o descartas. Tú respondes por el resultado. A diferencia de human in the loop, donde la IA dirige y la persona solo aprueba, en human in the lead la persona dirige.</desc>
  <defs>
    <style>
      #iaMando .title{fill:#161A26;font-size:22px;font-weight:700}
      #iaMando .sub{fill:#79809A;font-size:13.5px}
      #iaMando .nt{font-size:14px;font-weight:700}
      #iaMando .nd{fill:#454C61;font-size:12.5px}
      #iaMando .tag{fill:#FFFFFF;font-size:10.5px;font-weight:700;letter-spacing:.04em}
      #iaMando .h{font-size:12.5px;font-weight:700;letter-spacing:.06em}
      #iaMando .cb{fill:#454C61;font-size:13px}
    </style>
    <marker id="iaMando-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/></marker>
  </defs>
  <rect width="960" height="492" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Tú al mando: <tspan fill="#4453C9">human in the lead</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">La IA hace mucho del trabajo. Las decisiones siguen siendo tuyas.</text>
  <path d="M428,152 Q500,152 500,236" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#iaMando-a)"/>
  <path d="M500,312 Q500,404 436,404" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#iaMando-a)"/>
  <path d="M220,404 Q148,404 148,320" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#iaMando-a)"/>
  <path d="M148,244 Q148,152 212,152" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#iaMando-a)"/>
  <rect x="220" y="118" width="208" height="68" rx="14" fill="#EEF1FF" stroke="#4453C9" stroke-width="2.5"/>
  <rect x="234" y="131" width="34" height="18" rx="9" fill="#4453C9"/>
  <text class="tag" x="251" y="140" dy="0.35em" text-anchor="middle">TÚ</text>
  <text class="nt" x="276" y="140" dy="0.35em" fill="#4453C9" data-fit="144">1 · Defines</text>
  <text class="nd" x="234" y="170" data-fit="224">qué, por qué y con qué reglas</text>
  <rect x="396" y="244" width="208" height="68" rx="14" fill="#F4EBFF" stroke="#7439B8" stroke-width="1.5"/>
  <rect x="410" y="257" width="34" height="18" rx="9" fill="#7439B8"/>
  <text class="tag" x="427" y="266" dy="0.35em" text-anchor="middle">IA</text>
  <text class="nt" x="452" y="266" dy="0.35em" fill="#7439B8" data-fit="144">2 · Propone y hace</text>
  <text class="nd" x="410" y="296" data-fit="204">con sus herramientas</text>
  <rect x="220" y="370" width="208" height="68" rx="14" fill="#EEF1FF" stroke="#4453C9" stroke-width="2.5"/>
  <rect x="234" y="383" width="34" height="18" rx="9" fill="#4453C9"/>
  <text class="tag" x="251" y="392" dy="0.35em" text-anchor="middle">TÚ</text>
  <text class="nt" x="276" y="392" dy="0.35em" fill="#4453C9" data-fit="144">3 · Revisas</text>
  <text class="nd" x="234" y="422" data-fit="204">¿entiendes lo que hizo?</text>
  <rect x="44" y="244" width="208" height="68" rx="14" fill="#EEF1FF" stroke="#4453C9" stroke-width="2.5"/>
  <rect x="58" y="257" width="34" height="18" rx="9" fill="#4453C9"/>
  <text class="tag" x="75" y="266" dy="0.35em" text-anchor="middle">TÚ</text>
  <text class="nt" x="100" y="266" dy="0.35em" fill="#4453C9" data-fit="144">4 · Decides</text>
  <text class="nd" x="58" y="296" data-fit="224">aceptas, corriges o descartas</text>
  <text x="324" y="270" text-anchor="middle" fill="#161A26" font-size="14" font-weight="700">Tú respondes</text>
  <text x="324" y="290" text-anchor="middle" fill="#161A26" font-size="14" font-weight="700">por el resultado</text>
  <rect x="640" y="136" width="272" height="116" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="660" y="164" fill="#556074">HUMAN IN THE LOOP</text>
  <text class="cb" x="660" y="190" data-fit="236">La IA dirige y tú apruebas lo</text>
  <text class="cb" x="660" y="209" data-fit="248">que te muestra. Si no entiendes,</text>
  <text class="cb" x="660" y="228" data-fit="236">apruebas a ciegas.</text>
  <rect x="640" y="272" width="272" height="116" rx="12" fill="#EEF1FF" stroke="#4453C9" stroke-width="2.5"/>
  <text class="h" x="660" y="300" fill="#4453C9">HUMAN IN THE LEAD</text>
  <text class="cb" x="660" y="326" data-fit="236">Tú diriges: decides el objetivo,</text>
  <text class="cb" x="660" y="345" data-fit="236">las reglas y cuándo algo está</text>
  <text class="cb" x="660" y="364" data-fit="236">bien. <tspan font-weight="700" fill="#4453C9">Es lo que buscamos.</tspan></text>
  <text x="48" y="468" fill="#454C61" font-size="13.5" data-fit="860">Si la IA se equivoca y tú lo aceptaste, el error es tuyo. Por eso nunca se acepta un cambio que no entiendes.</text>
</svg>
```

Eso es **human in the lead**: la IA hace buena parte del trabajo, pero el objetivo, las reglas y la última palabra son tuyas. En la unidad 3 del curso vas a aprender a configurar al agente para que trabaje como tú quieres.
