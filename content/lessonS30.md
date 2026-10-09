# El archivo de contexto

<!-- tags: AGENTS.md, archivo de contexto, /init, CLAUDE.md, el agente inventa datos, convenciones del proyecto, reglas para el agente, modelo de datos, docs/modelo.md, el agente no sigue mis convenciones, documento vivo, contexto del agente -->

El agente no sabe nada de tu proyecto hasta que lo lee. Y hay cosas que no puede leer en ninguna parte, porque todavía no están escritas. El **archivo de contexto** es donde las escribes.

## Lo que el agente ve

```svg
<svg id="cxQueVe" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 468" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="cxQueVe-ttl cxQueVe-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="cxQueVe-ttl">Lo que el agente ve y lo que no</title>
  <desc id="cxQueVe-dsc">A la izquierda, lo que el agente ve: tu pedido, los archivos que abre y el archivo AGENTS.md, que llega siempre. Las tres cosas entran al modelo de IA. A la derecha, lo que no ve: de qué trata tu app, qué datos guarda y lo que se acordó en clase. Lo que no ve, lo inventa.</desc>
  <defs>
    <style>
      #cxQueVe .title{fill:#161A26;font-size:22px;font-weight:700}
      #cxQueVe .sub{fill:#79809A;font-size:13.5px}
      #cxQueVe .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #cxQueVe .nt{font-size:15px;font-weight:700;fill:#161A26}
      #cxQueVe .nb{fill:#454C61;font-size:13px}
      #cxQueVe .lbl{fill:#556074;font-size:12px;font-weight:600}
      #cxQueVe .foot{fill:#79809A;font-size:12px}
      #cxQueVe .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #cxQueVe .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#cxQueVe-arrow)}
    </style>
    <marker id="cxQueVe-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="468" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Lo que el agente ve y lo que no</text>
  <text class="sub" x="48" y="80" data-fit="860">El modelo solo trabaja con lo que le llega. Lo demás no existe para él.</text>
  <text x="48" y="124" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" class="h">LO QUE VE</text>
  <text x="612" y="124" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" class="h">LO QUE NO VE</text>
  <rect x="48" y="140" width="300" height="64" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="68" y="167" font-size="14.5" font-weight="700" fill="#4453C9" text-anchor="start" data-fit="260">Tu pedido</text>
  <text x="68" y="188" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="260">Lo que escribes en ese momento.</text>
  <rect x="48" y="216" width="300" height="64" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="68" y="243" font-size="14.5" font-weight="700" fill="#0F8478" text-anchor="start" data-fit="260">Los archivos que abre</text>
  <text x="68" y="264" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="260">Tu código: de ahí copia el estilo.</text>
  <rect x="48" y="292" width="300" height="64" rx="12" fill="#FFF3DC" stroke="#A96C05" stroke-width="2.5"/>
  <text x="68" y="319" font-size="14.5" font-weight="700" fill="#A96C05" text-anchor="start" class="mono" data-fit="260">AGENTS.md</text>
  <text x="68" y="340" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="260">Siempre, en cada pedido.</text>
  <path class="link" d="M348,172 L404,232"/>
  <path class="link" d="M348,248 H404"/>
  <path class="link" d="M348,324 L404,264"/>
  <rect x="412" y="204" width="136" height="88" rx="12" fill="#7439B8"/>
  <text x="480" y="244" font-size="14.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Modelo</text>
  <text x="480" y="263" font-size="14.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">de IA</text>
  <rect x="612" y="140" width="300" height="64" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 4"/>
  <text x="632" y="167" font-size="14.5" font-weight="700" fill="#556074" text-anchor="start" data-fit="260">De qué trata tu app</text>
  <text x="632" y="188" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="260">Biblioteca, tienda, reservas…</text>
  <rect x="612" y="216" width="300" height="64" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 4"/>
  <text x="632" y="243" font-size="14.5" font-weight="700" fill="#556074" text-anchor="start" data-fit="260">Qué datos guarda</text>
  <text x="632" y="264" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="260">Las tablas y sus atributos.</text>
  <rect x="612" y="292" width="300" height="64" rx="12" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 4"/>
  <text x="632" y="319" font-size="14.5" font-weight="700" fill="#556074" text-anchor="start" data-fit="260">Lo que acordaron en clase</text>
  <text x="632" y="340" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="260">Lo que todavía no está en el código.</text>
  <rect x="48" y="388" width="864" height="52" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.25" stroke-dasharray="5 4"/><text x="68" y="414" dy="0.35em" fill="#7C4F04" font-size="13.5" data-fit="820"><tspan font-weight="700">Lo que no ve, lo inventa.</tspan> El archivo de contexto pasa esas tres cosas a la columna de la izquierda.</text>
</svg>
```

`AGENTS.md` es un archivo de texto en la raíz del proyecto. El agente lo recibe **en cada pedido**, antes de leer tu mensaje. En Claude Code el mismo archivo se llama `CLAUDE.md`.

## El mismo pedido, dos veces

Haz la prueba. Con el proyecto como lo dejaste en el taller, pídele al agente una pantalla de tu app. En el ejemplo, una app de biblioteca:

> Crea la pantalla de detalle de un libro y regístrala en la app

```svg
<svg id="cxAntesDespues" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="cxAntesDespues-ttl cxAntesDespues-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="cxAntesDespues-ttl">El mismo pedido, sin y con contexto</title>
  <desc id="cxAntesDespues-dsc">Dos celulares con la pantalla de detalle de un libro. Sin contexto, el agente copió el estilo del proyecto pero inventó una calificación con reseñas, el género, las páginas, el ISBN y los botones Leer y Favorito. Con AGENTS.md, la pantalla solo muestra autor y categoría, que sí están en el modelo de datos, y el botón Pedir prestado.</desc>
  <defs>
    <style>
      #cxAntesDespues .title{fill:#161A26;font-size:22px;font-weight:700}
      #cxAntesDespues .sub{fill:#79809A;font-size:13.5px}
      #cxAntesDespues .h{font-size:12px;font-weight:700;letter-spacing:.08em}
      #cxAntesDespues .nt{font-size:15px;font-weight:700;fill:#161A26}
      #cxAntesDespues .nb{fill:#454C61;font-size:13px}
      #cxAntesDespues .lbl{fill:#556074;font-size:12px;font-weight:600}
      #cxAntesDespues .foot{fill:#79809A;font-size:12px}
      #cxAntesDespues .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #cxAntesDespues .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#cxAntesDespues-arrow)}
    </style>
    <marker id="cxAntesDespues-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="560" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">El mismo pedido, sin y con contexto</text>
  <text class="sub" x="48" y="80" data-fit="860">Pedido: «Crea la pantalla de detalle de un libro». Resultado real de un modelo gratuito, redibujado.</text>
  <clipPath id="cxAntesDespues-a"><rect width="200" height="340" rx="20"/></clipPath><rect x="57" y="129" width="214" height="354" rx="27" fill="#1F2430"/><g transform="translate(64,136)"><g clip-path="url(#cxAntesDespues-a)"><rect width="200" height="340" rx="20" fill="#FFFFFF"/><rect width="200" height="44" fill="#F1ECF8"/><text x="16" y="27" font-size="14" font-weight="500" fill="#161A26" text-anchor="start">Detalle del libro</text><rect x="70" y="58" width="60" height="80" rx="6" fill="#E3E7EF"/><path d="M88,84 h24 v28 h-24 Z M100,84 v28" fill="none" stroke="#9AA3B5" stroke-width="1.5"/><text x="100" y="160" font-size="14" font-weight="700" fill="#161A26" text-anchor="middle">El gran viaje</text><text x="100" y="178" font-size="12" font-weight="400" fill="#556074" text-anchor="middle">María López</text><text x="100" y="198" font-size="12" font-weight="400" fill="#161A26" text-anchor="middle">★ 4.5 (128 reseñas)</text><text x="20" y="228" font-size="12" font-weight="700" fill="#161A26" text-anchor="start">Género</text><text x="84" y="228" font-size="12" font-weight="400" fill="#556074" text-anchor="start">Novela</text><text x="20" y="248" font-size="12" font-weight="700" fill="#161A26" text-anchor="start">Páginas</text><text x="84" y="248" font-size="12" font-weight="400" fill="#556074" text-anchor="start">320</text><text x="20" y="268" font-size="12" font-weight="700" fill="#161A26" text-anchor="start">ISBN</text><text x="84" y="268" font-size="12" font-weight="400" fill="#556074" text-anchor="start">978-84-1234</text><rect x="14" y="292" width="82" height="32" rx="16" fill="#7439B8"/><text x="55.0" y="312" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">Leer</text><rect x="104" y="292" width="82" height="32" rx="16" fill="#7439B8"/><text x="145.0" y="312" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">Favorito</text><rect x="30" y="185" width="140" height="20" rx="6" fill="#C2354F" fill-opacity=".08" stroke="#C2354F" stroke-width="2"/><rect x="10" y="212" width="180" height="64" rx="8" fill="#C2354F" fill-opacity=".08" stroke="#C2354F" stroke-width="2"/><rect x="10" y="286" width="180" height="44" rx="8" fill="#C2354F" fill-opacity=".08" stroke="#C2354F" stroke-width="2"/></g></g>
  <clipPath id="cxAntesDespues-b"><rect width="200" height="340" rx="20"/></clipPath><rect x="505" y="129" width="214" height="354" rx="27" fill="#1F2430"/><g transform="translate(512,136)"><g clip-path="url(#cxAntesDespues-b)"><rect width="200" height="340" rx="20" fill="#FFFFFF"/><rect width="200" height="44" fill="#F1ECF8"/><text x="16" y="27" font-size="14" font-weight="500" fill="#161A26" text-anchor="start">Detalle del libro</text><rect x="70" y="58" width="60" height="80" rx="6" fill="#E3E7EF"/><path d="M88,84 h24 v28 h-24 Z M100,84 v28" fill="none" stroke="#9AA3B5" stroke-width="1.5"/><text x="100" y="160" font-size="14" font-weight="700" fill="#161A26" text-anchor="middle">Cien años de soledad</text><text x="20" y="196" font-size="12" font-weight="700" fill="#161A26" text-anchor="start">Autor</text><text x="92" y="196" font-size="12" font-weight="400" fill="#556074" text-anchor="start">García Márquez</text><text x="20" y="216" font-size="12" font-weight="700" fill="#161A26" text-anchor="start">Categoría</text><text x="92" y="216" font-size="12" font-weight="400" fill="#556074" text-anchor="start">Novela</text><rect x="14" y="246" width="172" height="32" rx="16" fill="#7439B8"/><text x="100.0" y="266" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">Pedir prestado</text><rect x="10" y="180" width="180" height="44" rx="8" fill="#0F8478" fill-opacity=".08" stroke="#0F8478" stroke-width="2"/><rect x="10" y="240" width="180" height="44" rx="8" fill="#0F8478" fill-opacity=".08" stroke="#0F8478" stroke-width="2"/></g></g>
  <text x="292" y="150" font-size="13" font-weight="700" fill="#C2354F" text-anchor="start" class="h" data-fit="176">SIN CONTEXTO</text>
  <text x="292" y="196" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="176">Copió el estilo</text>
  <text x="292" y="216" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="176">Scaffold, SafeArea, imports.</text>
  <text x="292" y="262" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="176">Inventó los datos</text>
  <text x="292" y="282" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="176">Reseñas, género, ISBN.</text>
  <text x="292" y="328" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="176">Inventó la app</text>
  <text x="292" y="348" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="176">Leer y Favorito.</text>
  <text x="740" y="150" font-size="13" font-weight="700" fill="#0F8478" text-anchor="start" class="h" data-fit="176">CON AGENTS.md</text>
  <text x="740" y="196" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="176">Solo datos del modelo</text>
  <text x="740" y="216" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="176">Autor y categoría.</text>
  <text x="740" y="262" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="176">La acción de la app</text>
  <text x="740" y="282" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="176">Pedir prestado.</text>
  <text x="740" y="328" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="176">Secciones aparte</text>
  <text x="740" y="348" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="176">En lib/components/.</text>
  <path d="M488,128 V488" stroke="#D9DEE8" stroke-width="1.5" stroke-dasharray="4 5"/>
  <text x="48" y="528" font-size="13.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="860">El código le enseñó cómo escribir. De qué trata la app no estaba en ninguna parte.</text>
</svg>
```

Revisa lo que hizo con lo que ya sabes:

- **Lo que copió bien.** `Scaffold`, `SafeArea`, imports con `package:`, tus componentes. Lo aprendió leyendo tu código.
- **Lo que inventó.** Datos que tu app no guarda y botones de otra app. De eso no había nada que leer.
- **Lo que hizo distinto a lo acordado.** Clases privadas dentro de la pantalla, en vez de secciones en `lib/components/`.

Deshaz el cambio con `/undo`. Ahora vas a escribir el contexto y a repetir exactamente el mismo pedido.

## Crear el archivo con /init

```svg
<svg id="cxInit" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 538" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="cxInit-ttl cxInit-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="cxInit-ttl">Crear el archivo con /init</title>
  <desc id="cxInit-dsc">Dentro de OpenCode se escribe /init. El agente lee pubspec.yaml y los archivos de lib, y escribe AGENTS.md en la raíz del proyecto.</desc>
  <defs>
    <style>
      #cxInit .title{fill:#161A26;font-size:22px;font-weight:700}
      #cxInit .sub{fill:#79809A;font-size:13.5px}
      #cxInit .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #cxInit .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #cxInit .pf{fill:#7F8AA3} #cxInit .cmd{fill:#FFFFFF;font-weight:600}
      #cxInit .dim{fill:#8A93A6} #cxInit .okk{fill:#6BCB77;font-weight:600}
      #cxInit .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #cxInit .chipc{fill:#F2C069} #cxInit .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #cxInit .ct{fill:#161A26;font-size:14px;font-weight:700}
      #cxInit .cb{fill:#454C61;font-size:13px}
      #cxInit .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="538" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Crear el archivo con <tspan class="mono">/init</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">El agente recorre el proyecto y escribe un primer borrador. Es un punto de partida, no el archivo final.</text>
  <rect x="48" y="112" width="864" height="268" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\miapp1</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816">&gt; /init</text>
  <text class="tl mono dim" font-size="13" x="72" y="226" data-fit="816">→ Read pubspec.yaml</text>
  <text class="tl mono dim" font-size="13" x="72" y="252" data-fit="816">→ Read lib/main.dart</text>
  <text class="tl mono dim" font-size="13" x="72" y="278" data-fit="816">→ Read lib/screens/profile_screen.dart</text>
  <text class="tl mono" font-size="13" x="72" y="304" data-fit="816">← Write AGENTS.md</text>
  <text class="tl mono okk" font-size="13" x="72" y="356" data-fit="816">Creé AGENTS.md con la guía del proyecto.</text>
  <rect class="ring" x="83.6" y="158" width="47.0" height="22" rx="5"/>
  <circle class="chipc" cx="130.6" cy="159" r="8"/>
  <text class="chipt" x="130.6" y="159" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="68.0" y="288" width="140.6" height="22" rx="5"/>
  <circle class="chipc" cx="208.6" cy="289" r="8"/>
  <text class="chipt" x="208.6" y="289" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <g transform="translate(48.0,404)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">Un comando del agente</text>
    <text class="cb" x="16" y="60" data-fit="392">Empieza por <tspan font-weight="700">/</tspan> y se escribe</text>
    <text class="cb" x="16" y="79" data-fit="392">dentro de OpenCode.</text>
  </g>
  <g transform="translate(488.0,404)">
    <rect width="424.0" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="362">En la raíz del proyecto</text>
    <text class="cb" x="16" y="60" data-fit="392">Junto a <tspan font-weight="700">pubspec.yaml</tspan>.</text>
    <text class="cb" x="16" y="79" data-fit="392">Se sube al repositorio.</text>
  </g>
</svg>
```

```shell
/init
```

Lo que escribe `/init` sale de tu código: comandos, carpetas y poco más. Sirve de base. Lo que falta, que es lo importante, lo pones tú.

## Los seis apartados

```svg
<svg id="cxPartes" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 500" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="cxPartes-ttl cxPartes-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="cxPartes-ttl">Los seis apartados de AGENTS.md</title>
  <desc id="cxPartes-dsc">Un documento con seis apartados y de dónde sale cada uno: Qué es, del párrafo de contexto de la Entrega 1. Cómo se ejecuta y se revisa, de los comandos de la sesión 1. Estructura, de las carpetas de la sesión 2. Convenciones, de lo acordado en las sesiones 2 y 3. Modelo de datos, que apunta a docs/modelo.md de la Entrega 1. Reglas para el agente, que son lo que tú le exiges.</desc>
  <defs>
    <style>
      #cxPartes .title{fill:#161A26;font-size:22px;font-weight:700}
      #cxPartes .sub{fill:#79809A;font-size:13.5px}
      #cxPartes .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #cxPartes .nt{font-size:15px;font-weight:700;fill:#161A26}
      #cxPartes .nb{fill:#454C61;font-size:13px}
      #cxPartes .lbl{fill:#556074;font-size:12px;font-weight:600}
      #cxPartes .foot{fill:#79809A;font-size:12px}
      #cxPartes .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #cxPartes .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#cxPartes-arrow)}
    </style>
    <marker id="cxPartes-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="500" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Los seis apartados de <tspan class="mono">AGENTS.md</tspan></text>
  <text class="sub" x="48" y="80" data-fit="860">Casi todo ya lo tienes escrito o acordado. Solo hay que ponerlo donde el agente lo lea.</text>
  <rect x="48" y="112" width="384" height="356" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <path d="M48,144 H432" stroke="#D9DEE8" stroke-width="1.5"/>
  <text x="64" y="133" font-size="12.5" font-weight="700" fill="#556074" text-anchor="start" class="mono">AGENTS.md</text>
  <text x="72" y="178" font-size="13.5" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="340">## Qué es</text>
  <rect x="72" y="189" width="200" height="6" rx="3" fill="#E3E7EF"/>
  <path d="M432,180 H480" stroke="#A9B4F2" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>
  <rect x="480" y="160" width="432" height="40" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="500" y="184.5" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="396">El párrafo de contexto de la Entrega 1.</text>
  <text x="72" y="230" font-size="13.5" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="340">## Cómo se ejecuta y se revisa</text>
  <rect x="72" y="241" width="120" height="6" rx="3" fill="#E3E7EF"/>
  <path d="M432,232 H480" stroke="#C4CBD8" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>
  <rect x="480" y="212" width="432" height="40" rx="10" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="500" y="236.5" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="396">Los comandos de la sesión 1.</text>
  <text x="72" y="282" font-size="13.5" font-weight="700" fill="#A96C05" text-anchor="start" class="mono" data-fit="340">## Estructura</text>
  <rect x="72" y="293" width="160" height="6" rx="3" fill="#E3E7EF"/>
  <path d="M432,284 H480" stroke="#F0C572" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>
  <rect x="480" y="264" width="432" height="40" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="500" y="288.5" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="396">Las carpetas de la sesión 2.</text>
  <text x="72" y="334" font-size="13.5" font-weight="700" fill="#0F8478" text-anchor="start" class="mono" data-fit="340">## Convenciones</text>
  <rect x="72" y="345" width="240" height="6" rx="3" fill="#E3E7EF"/>
  <path d="M432,336 H480" stroke="#86D3CA" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>
  <rect x="480" y="316" width="432" height="40" rx="10" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="500" y="340.5" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="396">Lo acordado en las sesiones 2 y 3.</text>
  <text x="72" y="386" font-size="13.5" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="340">## Modelo de datos</text>
  <rect x="72" y="397" width="100" height="6" rx="3" fill="#E3E7EF"/>
  <path d="M432,388 H480" stroke="#A9B4F2" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>
  <rect x="480" y="368" width="432" height="40" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="500" y="392.5" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="396">Apunta a docs/modelo.md, de la Entrega 1.</text>
  <text x="72" y="438" font-size="13.5" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="340">## Reglas para el agente</text>
  <rect x="72" y="449" width="180" height="6" rx="3" fill="#E3E7EF"/>
  <path d="M432,440 H480" stroke="#C9A6EE" stroke-width="1.75" stroke-dasharray="4 4" fill="none"/>
  <rect x="480" y="420" width="432" height="40" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="500" y="444.5" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="396">Lo que tú le exiges al agente.</text>
</svg>
```

Con una sola pantalla hay poco código, pero ya hay mucho decidido. Este es el archivo completo de la app de biblioteca. Reemplaza el contenido que dejó `/init` por uno así, con los datos de tu app:

```markdown
# Biblioteca de préstamos

## Qué es

App para la biblioteca de un colegio. Quien la usa busca libros por categoría, abre el
detalle de un libro y lo pide prestado. También ve la lista de sus préstamos.
No hay compras, reseñas ni lectura dentro de la app.

## Cómo se ejecuta y se revisa

- Ejecutar: `flutter run -d chrome`
- Revisar: `flutter analyze`. El único aviso aceptado es `avoid_print`.

## Estructura

- `lib/main.dart`: la app y la tabla de rutas.
- `lib/screens/`: una pantalla por archivo, `XxxScreen`.
- `lib/components/`: componentes y secciones reutilizables.
- `docs/modelo.md`: el modelo de datos.

## Convenciones

- Una Screen tiene `Scaffold` y su `body` empieza con `SafeArea`.
- Cada bloque de una pantalla es una sección en `lib/components/`, en su propio archivo. Nada de clases privadas dentro de la pantalla.
- Antes de crear un componente, revisa si ya existe en `lib/components/`.
- Imports propios con `package:miapp1/`.
- Código en inglés, también los nombres que vienen del modelo de datos: `titulo` se escribe `title`. Textos de la interfaz en español.
- Solo `StatelessWidget`. Los botones todavía no hacen nada: `print`.

## Modelo de datos

Está en `docs/modelo.md`. Una pantalla solo muestra datos que existan ahí: no inventes atributos.

## Reglas para el agente

- No agregues paquetes a `pubspec.yaml` sin preguntar.
- No toques archivos fuera de `lib/` y `docs/` sin avisar.
- Al terminar, ejecuta `flutter analyze` y di qué archivos creaste o cambiaste.
```

Fíjate en la última frase de *Qué es*: decir lo que la app **no** hace es lo que evita los botones inventados.

## El modelo de datos, en texto

El apartado *Modelo de datos* apunta a otro archivo. Crea `docs/modelo.md` con las tablas de tu diagrama de la Entrega 1, una lista por tabla:

```markdown
# Modelo de datos

## categorias

- id (PK)
- nombre
- descripcion

## libros

- id (PK)
- titulo
- autor
- categoria_id (FK a categorias)

## usuarios

- id (PK)
- nombre
- correo

## prestamos

- id (PK)
- libro_id (FK a libros)
- usuario_id (FK a usuarios)
- fecha_prestamo

## Relaciones

- Una categoria tiene muchos libros.
- Un libro tiene muchos prestamos.
- Un usuario tiene muchos prestamos.
```

Con los dos archivos guardados, repite el pedido de la pantalla y compara.

## Un documento vivo

El archivo de contexto no se escribe una vez. Se corrige cada vez que el agente se equivoca por algo que tú no habías dicho:

- **Si el error es de una sola vez**, corriges el código o se lo pides de nuevo.
- **Si el error se va a repetir**, agregas una línea al `AGENTS.md`.

Un ejemplo real: con la regla "código en inglés", el agente llamó `titulo` a una variable, porque así se llama en el modelo de datos. La regla era ambigua. Se corrigió la regla, no solo la variable.

Mantenlo corto. Todo lo que escribes ahí viaja en cada pedido: si pasa de una página, el agente empieza a perder de vista lo importante.

## Para tu equipo

Lleva el `AGENTS.md`, el `opencode.json` y `docs/modelo.md` al repositorio del equipo, con el contexto y el modelo de **su** app. A partir de la próxima sesión, todo lo que el agente genere se revisa contra ese archivo.
