# Panorama del frontend

<!-- tags: desarrollo web, aplicación de escritorio, app móvil nativa, multiplataforma, nativo vs multiplataforma, React, Angular, Jetpack Compose, SwiftUI, Flutter, React Native, Electron -->

El frontend no es uno solo. Según **dónde corre** la app, cambian el lenguaje, las herramientas y los problemas. Se suelen agrupar en cuatro familias.

```svg
<svg id="pfMapa" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 728" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="pfMapa-ttl pfMapa-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="pfMapa-ttl">Las cuatro familias del frontend</title>
  <desc id="pfMapa-dsc">Web: corre en el navegador, con HTML, CSS y JavaScript; frameworks React, Angular, Vue y Svelte. Escritorio: se instala en Windows, macOS o Linux; WinUI, SwiftUI, Qt, Electron y Tauri. Móvil nativo: una app por sistema, Kotlin con Jetpack Compose en Android y Swift con SwiftUI en iOS. Multiplataforma: un solo código para varios destinos; Flutter, que es el de este curso, React Native, Kotlin Multiplatform y .NET MAUI.</desc>
  <defs>
    <style>
      #pfMapa .title{fill:#161A26;font-size:22px;font-weight:700}
      #pfMapa .sub{fill:#79809A;font-size:13.5px}
      #pfMapa .fn{font-size:17px;font-weight:700}
      #pfMapa .fd{fill:#454C61;font-size:13px}
      #pfMapa .fl{fill:#79809A;font-size:12px;font-weight:700;letter-spacing:.06em}
      #pfMapa .fv{fill:#454C61;font-size:12.5px}
      #pfMapa .ch{font-size:12px;font-weight:600}
    </style>
  </defs>
  <rect width="960" height="728" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las cuatro familias del frontend</text>
  <text class="sub" x="48" y="80" data-fit="860">Se distinguen por dónde corre la app y cuántos códigos hay que escribir para llegar ahí.</text>
  <rect x="48" y="112" width="420" height="280" rx="14" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <rect x="68" y="134" width="64" height="46" rx="6" fill="#FFFFFF" stroke="#4453C9" stroke-width="1.75"/>
  <path d="M68,146 H132" stroke="#4453C9" stroke-width="1.75"/>
  <rect x="86" y="137" width="40" height="6" rx="3" fill="#4453C9" opacity="0.35"/>
  <circle cx="75" cy="140" r="2" fill="#4453C9"/><circle cx="81" cy="140" r="2" fill="#4453C9"/>
  <rect x="76" y="154" width="48" height="5" rx="2.5" fill="#4453C9" opacity="0.3"/><rect x="76" y="164" width="34" height="5" rx="2.5" fill="#4453C9" opacity="0.3"/>
  <text class="fn" x="148" y="152" fill="#4453C9" data-fit="300">Web</text>
  <text class="fd" x="148" y="174" data-fit="320">Corre en un navegador. Se abre con una</text>
  <text class="fd" x="148" y="192" data-fit="320">URL, sin instalar nada.</text>
  <text class="fl" x="68" y="240">LENGUAJES</text>
  <text class="fv" x="68" y="260" data-fit="380">HTML, CSS, JavaScript / TypeScript</text>
  <text class="fl" x="68" y="292">FRAMEWORKS</text>
  <rect x="68" y="306" width="59" height="26" rx="13" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.25"/>
  <text class="ch" x="98" y="319" dy="0.35em" text-anchor="middle" fill="#4453C9">React</text>
  <rect x="135" y="306" width="73" height="26" rx="13" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.25"/>
  <text class="ch" x="172" y="319" dy="0.35em" text-anchor="middle" fill="#4453C9">Angular</text>
  <rect x="216" y="306" width="45" height="26" rx="13" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.25"/>
  <text class="ch" x="238" y="319" dy="0.35em" text-anchor="middle" fill="#4453C9">Vue</text>
  <rect x="269" y="306" width="66" height="26" rx="13" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.25"/>
  <text class="ch" x="302" y="319" dy="0.35em" text-anchor="middle" fill="#4453C9">Svelte</text>
  <rect x="492" y="112" width="420" height="280" rx="14" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <rect x="516" y="134" width="56" height="38" rx="4" fill="#FFFFFF" stroke="#556074" stroke-width="1.75"/>
  <path d="M516,143 H572" stroke="#556074" stroke-width="1.5"/>
  <rect x="522" y="149" width="16" height="17" rx="2" fill="#556074" opacity="0.3"/><rect x="542" y="149" width="24" height="7" rx="2" fill="#556074" opacity="0.3"/>
  <path d="M538,172 L534,180 H554 L550,172" fill="none" stroke="#556074" stroke-width="1.75" stroke-linejoin="round"/>
  <text class="fn" x="592" y="152" fill="#556074" data-fit="300">Escritorio</text>
  <text class="fd" x="592" y="174" data-fit="320">Se instala en Windows, macOS o Linux.</text>
  <text class="fd" x="592" y="192" data-fit="340">Ventanas, mouse, teclado, archivos locales.</text>
  <text class="fl" x="512" y="240">LENGUAJES</text>
  <text class="fv" x="512" y="260" data-fit="380">C#, Swift, C++, JavaScript</text>
  <text class="fl" x="512" y="292">FRAMEWORKS</text>
  <rect x="512" y="306" width="101" height="26" rx="13" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.25"/>
  <text class="ch" x="562" y="319" dy="0.35em" text-anchor="middle" fill="#556074">WinUI / WPF</text>
  <rect x="621" y="306" width="129" height="26" rx="13" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.25"/>
  <text class="ch" x="686" y="319" dy="0.35em" text-anchor="middle" fill="#556074">SwiftUI (macOS)</text>
  <rect x="758" y="306" width="38" height="26" rx="13" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.25"/>
  <text class="ch" x="777" y="319" dy="0.35em" text-anchor="middle" fill="#556074">Qt</text>
  <rect x="804" y="306" width="80" height="26" rx="13" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.25"/>
  <text class="ch" x="844" y="319" dy="0.35em" text-anchor="middle" fill="#556074">Electron</text>
  <rect x="512" y="340" width="59" height="26" rx="13" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.25"/>
  <text class="ch" x="542" y="353" dy="0.35em" text-anchor="middle" fill="#556074">Tauri</text>
  <rect x="48" y="416" width="420" height="280" rx="14" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
  <rect x="86" y="434" width="30" height="52" rx="7" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.75"/>
  <rect x="92" y="444" width="18" height="4" rx="2" fill="#3A8235" opacity="0.35"/><rect x="92" y="452" width="18" height="4" rx="2" fill="#3A8235" opacity="0.35"/><rect x="92" y="460" width="12" height="4" rx="2" fill="#3A8235" opacity="0.35"/>
  <circle cx="101" cy="478" r="2.5" fill="#3A8235"/>
  <text class="fn" x="148" y="456" fill="#3A8235" data-fit="300">Móvil nativo</text>
  <text class="fd" x="148" y="478" data-fit="320">Se instala desde una tienda. Una app por</text>
  <text class="fd" x="148" y="496" data-fit="320">sistema, cada una en su propio lenguaje.</text>
  <text class="fl" x="68" y="544">LENGUAJES</text>
  <text class="fv" x="68" y="564" data-fit="380">Kotlin (Android), Swift (iOS)</text>
  <text class="fl" x="68" y="596">FRAMEWORKS</text>
  <rect x="68" y="610" width="129" height="26" rx="13" fill="#FFFFFF" stroke="#9FD68D" stroke-width="1.25"/>
  <text class="ch" x="132" y="623" dy="0.35em" text-anchor="middle" fill="#3A8235">Jetpack Compose</text>
  <rect x="205" y="610" width="115" height="26" rx="13" fill="#FFFFFF" stroke="#9FD68D" stroke-width="1.25"/>
  <text class="ch" x="262" y="623" dy="0.35em" text-anchor="middle" fill="#3A8235">SwiftUI (iOS)</text>
  <rect x="492" y="416" width="420" height="280" rx="14" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <rect x="512" y="444" width="40" height="30" rx="4" fill="#FFFFFF" stroke="#7439B8" stroke-width="1.5"/>
  <rect x="538" y="434" width="22" height="40" rx="5" fill="#FFFFFF" stroke="#7439B8" stroke-width="1.5"/>
  <rect x="554" y="456" width="24" height="30" rx="4" fill="#FFFFFF" stroke="#7439B8" stroke-width="1.5"/>
  <path d="M554,462 H578" stroke="#7439B8" stroke-width="1.25"/>
  <text class="fn" x="592" y="456" fill="#7439B8" data-fit="300">Multiplataforma</text>
  <text class="fd" x="592" y="478" data-fit="320">Un solo código que corre en varios de los</text>
  <text class="fd" x="592" y="496" data-fit="320">destinos anteriores.</text>
  <text class="fl" x="512" y="544">LENGUAJES</text>
  <text class="fv" x="512" y="564" data-fit="380">Dart, JavaScript, Kotlin, C#</text>
  <text class="fl" x="512" y="596">FRAMEWORKS</text>
  <rect x="512" y="610" width="73" height="26" rx="13" fill="#7439B8"/>
  <text class="ch" x="548" y="623" dy="0.35em" text-anchor="middle" fill="#FFFFFF">Flutter</text>
  <rect x="593" y="610" width="108" height="26" rx="13" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="ch" x="647" y="623" dy="0.35em" text-anchor="middle" fill="#7439B8">React Native</text>
  <rect x="709" y="610" width="164" height="26" rx="13" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="ch" x="791" y="623" dy="0.35em" text-anchor="middle" fill="#7439B8">Kotlin Multiplatform</text>
  <rect x="512" y="644" width="87" height="26" rx="13" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="ch" x="556" y="657" dy="0.35em" text-anchor="middle" fill="#7439B8">.NET MAUI</text>
  <text x="892" y="456" text-anchor="end" fill="#7439B8" font-size="12" font-weight="700">★ el de este curso</text>
</svg>
```

## Web

La app corre **dentro de un navegador**. El usuario la abre con una URL, sin instalar nada, y siempre usa la última versión. Sus lenguajes son HTML (estructura), CSS (estilo) y JavaScript o TypeScript (comportamiento).

Frameworks más usados: **React**, **Angular**, **Vue** y **Svelte**.

## Escritorio

La app **se instala** en Windows, macOS o Linux. Trabaja con ventanas, mouse, teclado y archivos del computador.

Frameworks más usados: **WinUI / WPF** (Windows, en C#), **SwiftUI** (macOS), **Qt** (C++), y **Electron** y **Tauri**, que empaquetan una app web como app de escritorio. VS Code, el editor que usas en este curso, está hecho con Electron.

## Móvil nativo

La app se instala desde una tienda (Google Play o App Store) y se escribe **una vez por sistema**, cada una con las herramientas de su fabricante:

- **Android:** Kotlin con **Jetpack Compose**.
- **iOS:** Swift con **SwiftUI**.

## Multiplataforma

**Un solo código** corre en varios de los destinos anteriores: celular, web y escritorio.

Frameworks más usados: **Flutter** (Dart, de Google), **React Native** (JavaScript, de Meta), **Kotlin Multiplatform** (de JetBrains) y **.NET MAUI** (C#, de Microsoft).

## ¿Nativo o multiplataforma?

Es una de las primeras decisiones de ingeniería de un proyecto con app, y no tiene una respuesta única:

```svg
<svg id="pfNativo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 440" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="pfNativo-ttl pfNativo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="pfNativo-ttl">¿Nativo o multiplataforma?</title>
  <desc id="pfNativo-dsc">Nativo: un código en Kotlin para Android y otro en Swift para iOS; acceso completo a cada sistema, pero todo se construye y mantiene dos veces. Multiplataforma: un solo código en Flutter que llega a Android, iOS, web y escritorio; un código y un equipo, pero lo muy propio de cada sistema cuesta más.</desc>
  <defs>
    <style>
      #pfNativo .title{fill:#161A26;font-size:22px;font-weight:700}
      #pfNativo .sub{fill:#79809A;font-size:13.5px}
      #pfNativo .h{font-size:13px;font-weight:700;letter-spacing:.08em}
      #pfNativo .hs{fill:#79809A;font-size:12.5px}
      #pfNativo .ct{font-size:14px;font-weight:700}
      #pfNativo .cs{fill:#454C61;font-size:12.5px}
      #pfNativo .pc{fill:#454C61;font-size:13px}
      #pfNativo .tg{font-size:12.5px;font-weight:600}
    </style>
    <marker id="pfNativo-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/></marker>
  </defs>
  <rect width="960" height="440" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">¿Nativo o multiplataforma?</text>
  <text class="sub" x="48" y="80" data-fit="860">La misma app para Android e iOS, construida de dos maneras.</text>
  <rect x="48" y="112" width="420" height="296" rx="16" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="72" y="142" fill="#3A8235">NATIVO</text><text class="hs" x="136" y="142" data-fit="300">· un código por sistema</text>
  <rect x="72" y="164" width="176" height="64" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
  <text class="ct" x="88" y="191" fill="#3A8235" data-fit="150">Código Android</text>
  <text class="cs" x="88" y="211" data-fit="150">Kotlin + Compose</text>
  <rect x="72" y="252" width="176" height="64" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
  <text class="ct" x="88" y="279" fill="#3A8235" data-fit="150">Código iOS</text>
  <text class="cs" x="88" y="299" data-fit="150">Swift + SwiftUI</text>
  <path d="M248,196 H320" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#pfNativo-a)"/>
  <path d="M248,284 H320" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#pfNativo-a)"/>
  <rect x="328" y="165" width="36" height="62" rx="7" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.75"/>
  <rect x="335" y="175" width="22" height="4" rx="2" fill="#3A8235" opacity="0.4"/><rect x="335" y="183" width="22" height="4" rx="2" fill="#3A8235" opacity="0.4"/><rect x="335" y="191" width="14" height="4" rx="2" fill="#3A8235" opacity="0.4"/>
  <rect x="328" y="253" width="36" height="62" rx="7" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.75"/>
  <rect x="335" y="263" width="22" height="4" rx="2" fill="#3A8235" opacity="0.4"/><rect x="335" y="271" width="22" height="4" rx="2" fill="#3A8235" opacity="0.4"/><rect x="335" y="279" width="14" height="4" rx="2" fill="#3A8235" opacity="0.4"/>
  <text class="tg" x="376" y="200" fill="#3A8235">Android</text>
  <text class="tg" x="376" y="288" fill="#3A8235">iOS</text>
  <text class="pc" x="72" y="358" data-fit="380"><tspan fill="#3A8235" font-weight="700">✓</tspan> Acceso completo a cada sistema</text>
  <text class="pc" x="72" y="382" data-fit="380"><tspan fill="#C2354F" font-weight="700">✗</tspan> Todo se construye y se mantiene dos veces</text>
  <rect x="492" y="112" width="420" height="296" rx="16" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="2"/>
  <text class="h" x="516" y="142" fill="#7439B8">MULTIPLATAFORMA</text><text class="hs" x="680" y="142" data-fit="220">· un código para todos</text>
  <rect x="516" y="190" width="160" height="80" rx="12" fill="#F4EBFF" stroke="#7439B8" stroke-width="2"/>
  <text class="ct" x="532" y="222" fill="#7439B8" data-fit="130">Código Flutter</text>
  <text class="cs" x="532" y="244" data-fit="130">Dart</text>
  <path d="M676,230 L760,177" fill="none" stroke="#556074" stroke-width="1.5" marker-end="url(#pfNativo-a)"/>
  <rect x="768" y="164" width="120" height="26" rx="13" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tg" x="828" y="177" dy="0.35em" text-anchor="middle" fill="#7439B8">Android</text>
  <path d="M676,230 L760,211" fill="none" stroke="#556074" stroke-width="1.5" marker-end="url(#pfNativo-a)"/>
  <rect x="768" y="198" width="120" height="26" rx="13" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tg" x="828" y="211" dy="0.35em" text-anchor="middle" fill="#7439B8">iOS</text>
  <path d="M676,230 L760,245" fill="none" stroke="#556074" stroke-width="1.5" marker-end="url(#pfNativo-a)"/>
  <rect x="768" y="232" width="120" height="26" rx="13" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tg" x="828" y="245" dy="0.35em" text-anchor="middle" fill="#7439B8">Web</text>
  <path d="M676,230 L760,279" fill="none" stroke="#556074" stroke-width="1.5" marker-end="url(#pfNativo-a)"/>
  <rect x="768" y="266" width="120" height="26" rx="13" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.25"/>
  <text class="tg" x="828" y="279" dy="0.35em" text-anchor="middle" fill="#7439B8">Escritorio</text>
  <text class="pc" x="516" y="358" data-fit="380"><tspan fill="#3A8235" font-weight="700">✓</tspan> Un código y un equipo para todo</text>
  <text class="pc" x="516" y="382" data-fit="380"><tspan fill="#C2354F" font-weight="700">✗</tspan> Lo muy propio de cada sistema cuesta más</text>
</svg>
```

Si la app depende mucho de lo propio de un sistema, como el hardware del celular o integraciones muy específicas, lo nativo rinde más. Si hay que llegar a varias plataformas con un solo equipo, multiplataforma ahorra la mitad del trabajo.

## ¿Por qué Flutter en este curso?

Flutter lleva la misma app a Android, iOS, web y escritorio con un solo lenguaje, Dart. Eso te permite empezar hoy probando en **Chrome**, sin emuladores, y llevar después la misma app al celular sin reescribirla.
