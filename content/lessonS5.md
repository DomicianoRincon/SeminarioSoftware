# Frontend y la nube

<!-- tags: SDK de Supabase, autenticación, base de datos, storage, servicios en la nube, iniciar sesión, subir archivos, supabase.auth, supabase.from, supabase.storage, backend como servicio, librería -->

En este curso no vas a programar el backend. Tu app va a usar **servicios que ya existen en la nube**, los de Supabase, y se va a comunicar con ellos a través de un **SDK**.

```svg
<svg id="fnServicios" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fnServicios-ttl fnServicios-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fnServicios-ttl">Tu app y los servicios de la nube</title>
  <desc id="fnServicios-dsc">Dentro de tu app está el SDK de Supabase, una librería. Tu app le pide cosas al SDK y el SDK habla con tres servicios en la nube: autenticación, que sabe quién es el usuario; base de datos, que guarda y lee información; y storage, que guarda archivos.</desc>
  <defs>
    <style>
      #fnServicios .title{fill:#161A26;font-size:22px;font-weight:700}
      #fnServicios .sub{fill:#79809A;font-size:13.5px}
      #fnServicios .h{font-size:13px;font-weight:700;letter-spacing:.08em}
      #fnServicios .hs{fill:#79809A;font-size:12px}
      #fnServicios .st{font-size:15px;font-weight:700}
      #fnServicios .sd{fill:#454C61;font-size:13px}
      #fnServicios .code{fill:#556074;font-size:11px;font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fnServicios .foot{fill:#454C61;font-size:13px}
    </style>
    <marker id="fnServicios-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="520" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Tu app y los servicios de la nube</text>
  <text class="sub" x="48" y="80" data-fit="860">Tu app no habla directo con la nube: le pide las cosas al SDK, y el SDK se encarga.</text>
  <rect x="48" y="112" width="272" height="352" rx="16" fill="#FAF6FF" stroke="#C9A6EE" stroke-width="1.5" stroke-dasharray="6 5"/>
  <text class="h" x="68" y="142" fill="#7439B8">TU APP</text>
  <text class="hs" x="68" y="160">hecha con Flutter</text>
  <rect x="116" y="176" width="136" height="172" rx="18" fill="#1F2430"/>
  <rect x="124" y="186" width="120" height="152" rx="10" fill="#FFFFFF"/>
  <path d="M124,196 A10,10 0 0 1 134,186 H234 A10,10 0 0 1 244,196 V210 H124 Z" fill="#EADDFF"/>
  <text x="134" y="198" dy="0.35em" fill="#1D1B20" font-size="10.5" font-weight="600">Mi perfil</text>
  <circle cx="184" cy="244" r="20" fill="#EADDFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <circle cx="184" cy="238" r="7" fill="#C9A6EE"/><path d="M171,257 A13,11 0 0 1 197,257" fill="#C9A6EE"/>
  <rect x="154" y="274" width="60" height="7" rx="3.5" fill="#D9DEE8"/>
  <rect x="136" y="294" width="96" height="6" rx="3" fill="#EDEFF3"/><rect x="136" y="308" width="72" height="6" rx="3" fill="#EDEFF3"/>
  <rect x="72" y="366" width="224" height="68" rx="12" fill="#7439B8"/>
  <text x="88" y="392" fill="#FFFFFF" font-size="14" font-weight="700">SDK de Supabase</text>
  <text x="88" y="413" fill="#EADDFF" font-size="12" data-fit="196">una librería dentro de tu app</text>
  <rect x="560" y="112" width="352" height="352" rx="16" fill="#F5F7FA" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="6 5"/>
  <text class="h" x="580" y="142" fill="#556074">LA NUBE</text>
  <text class="hs" x="580" y="160">servicios de Supabase</text>
  <rect x="576" y="168" width="320" height="80" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <circle cx="616" cy="200" r="9" fill="none" stroke="#4453C9" stroke-width="2.25"/>
  <path d="M600,228 A16,14 0 0 1 632,228" fill="none" stroke="#4453C9" stroke-width="2.25"/>
  <text class="st" x="656" y="202" fill="#4453C9" data-fit="220">Autenticación</text>
  <text class="sd" x="656" y="224" data-fit="224">¿quién es el usuario?</text>
  <path d="M432,400 V216 Q432,208 440,208 H568" fill="none" stroke="#7439B8" stroke-width="1.75" marker-end="url(#fnServicios-a)"/>
  <text class="code" x="502" y="200" text-anchor="middle" data-fit="134">supabase.auth</text>
  <rect x="576" y="264" width="320" height="80" rx="12" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <path d="M598,290 A18,6 0 0 1 634,290 V318 A18,6 0 0 1 598,318 Z" fill="#FFFFFF" stroke="#0F8478" stroke-width="2"/>
  <path d="M598,290 A18,6 0 0 0 634,290 M598,304 A18,6 0 0 0 634,304" fill="none" stroke="#0F8478" stroke-width="1.5"/>
  <text class="st" x="656" y="298" fill="#0F8478" data-fit="220">Base de datos</text>
  <text class="sd" x="656" y="320" data-fit="224">guarda y lee información</text>
  <path d="M432,400 V312 Q432,304 440,304 H568" fill="none" stroke="#7439B8" stroke-width="1.75" marker-end="url(#fnServicios-a)"/>
  <text class="code" x="502" y="296" text-anchor="middle" data-fit="134">supabase.from()</text>
  <rect x="576" y="360" width="320" height="80" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <rect x="598" y="382" width="36" height="36" rx="5" fill="#FFFFFF" stroke="#A96C05" stroke-width="2"/>
  <circle cx="624" cy="392" r="4" fill="#A96C05"/>
  <path d="M600,414 L611,400 L620,410 L625,405 L632,414 Z" fill="#A96C05" opacity="0.6"/>
  <text class="st" x="656" y="394" fill="#A96C05" data-fit="220">Storage</text>
  <text class="sd" x="656" y="416" data-fit="224">guarda archivos: fotos, PDF</text>
  <path d="M296,400 H568" fill="none" stroke="#7439B8" stroke-width="1.75" marker-end="url(#fnServicios-a)"/>
  <text class="code" x="502" y="392" text-anchor="middle" data-fit="134">supabase.storage</text>
  <text class="foot" x="48" y="496" data-fit="860">Tu app llama funciones del SDK. Cómo viaja la información por internet es asunto del SDK, no tuyo.</text>
</svg>
```

## Tres servicios

- **Autenticación:** registrarse, iniciar y cerrar sesión. Sabe quién es cada usuario.
- **Base de datos:** guarda la información en tablas, como las que ya conoces.
- **Storage:** guarda archivos: fotos, documentos, videos.

## ¿Qué es el SDK?

Es una **librería** que agregas a tu app. Para usar un servicio no tienes que saber cómo viaja la información por internet: llamas una función del SDK, como `supabase.auth` para la autenticación, y el SDK se encarga del resto.

## Un ejemplo con los tres

```svg
<svg id="fnEjemplo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 400" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fnEjemplo-ttl fnEjemplo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fnEjemplo-ttl">Un ejemplo: cambiar la foto de perfil</title>
  <desc id="fnEjemplo-dsc">Cuatro pasos. Uno, la persona inicia sesión y autenticación confirma quién es. Dos, la app sube la foto y storage la guarda y devuelve un enlace. Tres, la app guarda ese enlace en la fila del perfil en la base de datos. Cuatro, la pantalla muestra la foto nueva.</desc>
  <defs>
    <style>
      #fnEjemplo .title{fill:#161A26;font-size:22px;font-weight:700}
      #fnEjemplo .sub{fill:#79809A;font-size:13.5px}
      #fnEjemplo .bt{font-size:13.5px;font-weight:700}
      #fnEjemplo .tx{fill:#454C61;font-size:13px}
      #fnEjemplo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
    </style>
    <marker id="fnEjemplo-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/></marker>
  </defs>
  <rect width="960" height="400" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Un ejemplo: cambiar la foto de perfil</text>
  <text class="sub" x="48" y="80" data-fit="860">Cada servicio hace una sola cosa. Tu app los combina.</text>
  <rect x="48" y="112" width="192" height="248" rx="14" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.5"/>
  <path d="M48,126 A14,14 0 0 1 62,112 H226 A14,14 0 0 1 240,126 V152 H48 Z" fill="#EEF1FF"/>
  <circle cx="70" cy="132" r="11" fill="#4453C9"/>
  <text x="70" y="132" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="12" font-weight="700">1</text>
  <text class="bt" x="90" y="132" dy="0.35em" fill="#4453C9" data-fit="140">Autenticación</text>
  <rect x="64" y="166" width="160" height="96" rx="10" fill="#F7F8FA"/>
  <rect x="80" y="180" width="128" height="18" rx="5" fill="#FFFFFF" stroke="#C4CBD8"/>
  <text x="88" y="189" dy="0.35em" fill="#79809A" font-size="10">ana@correo.com</text>
  <rect x="80" y="204" width="128" height="18" rx="5" fill="#FFFFFF" stroke="#C4CBD8"/>
  <text x="88" y="213" dy="0.35em" fill="#79809A" font-size="10">••••••••</text>
  <rect x="80" y="230" width="128" height="20" rx="10" fill="#4453C9"/>
  <text x="144" y="240" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="10.5" font-weight="700">Entrar</text>
  <text class="tx" x="64" y="292" data-fit="168">La persona inicia</text>
  <text class="tx" x="64" y="311" data-fit="168">sesión y Auth</text>
  <text class="tx" x="64" y="330" data-fit="168">confirma quién es.</text>
  <path d="M246,236 H266" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#fnEjemplo-a)"/>
  <rect x="272" y="112" width="192" height="248" rx="14" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/>
  <path d="M272,126 A14,14 0 0 1 286,112 H450 A14,14 0 0 1 464,126 V152 H272 Z" fill="#FFF3DC"/>
  <circle cx="294" cy="132" r="11" fill="#A96C05"/>
  <text x="294" y="132" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="12" font-weight="700">2</text>
  <text class="bt" x="314" y="132" dy="0.35em" fill="#A96C05" data-fit="140">Storage</text>
  <rect x="288" y="166" width="160" height="96" rx="10" fill="#F7F8FA"/>
  <rect x="342" y="178" width="52" height="44" rx="6" fill="#FFFFFF" stroke="#A96C05" stroke-width="1.75"/>
  <circle cx="380" cy="190" r="5" fill="#A96C05"/>
  <path d="M345,218 L360,200 L372,212 L379,206 L391,218 Z" fill="#A96C05" opacity="0.55"/>
  <rect x="304" y="236" width="128" height="7" rx="3.5" fill="#EDEFF3"/>
  <rect x="304" y="236" width="96" height="7" rx="3.5" fill="#A96C05"/>
  <text class="tx" x="288" y="292" data-fit="168">La app sube la foto.</text>
  <text class="tx" x="288" y="311" data-fit="168">Storage la guarda y</text>
  <text class="tx" x="288" y="330" data-fit="168">devuelve un enlace.</text>
  <path d="M470,236 H490" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#fnEjemplo-a)"/>
  <rect x="496" y="112" width="192" height="248" rx="14" fill="#FFFFFF" stroke="#86D3CA" stroke-width="1.5"/>
  <path d="M496,126 A14,14 0 0 1 510,112 H674 A14,14 0 0 1 688,126 V152 H496 Z" fill="#E3F6F3"/>
  <circle cx="518" cy="132" r="11" fill="#0F8478"/>
  <text x="518" y="132" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="12" font-weight="700">3</text>
  <text class="bt" x="538" y="132" dy="0.35em" fill="#0F8478" data-fit="140">Base de datos</text>
  <rect x="512" y="166" width="160" height="96" rx="10" fill="#F7F8FA"/>
  <rect x="522" y="178" width="140" height="20" rx="5" fill="#0F8478"/>
  <text x="530" y="188" dy="0.35em" fill="#FFFFFF" font-size="10.5" font-weight="700" class="mono">perfiles</text>
  <text x="530" y="212" dy="0.35em" fill="#79809A" font-size="10" class="mono">nombre</text>
  <text x="586" y="212" dy="0.35em" fill="#79809A" font-size="10" class="mono">foto</text>
  <rect x="522" y="226" width="140" height="22" rx="4" fill="#E3F6F3" stroke="#86D3CA"/>
  <text x="530" y="237" dy="0.35em" fill="#1D1B20" font-size="10" class="mono">Ana</text>
  <text x="586" y="237" dy="0.35em" fill="#0F8478" font-size="10" font-weight="700" class="mono">ana.jpg</text>
  <text class="tx" x="512" y="292" data-fit="168">La app guarda ese</text>
  <text class="tx" x="512" y="311" data-fit="168">enlace en la fila</text>
  <text class="tx" x="512" y="330" data-fit="168">de su perfil.</text>
  <path d="M694,236 H714" fill="none" stroke="#556074" stroke-width="1.75" marker-end="url(#fnEjemplo-a)"/>
  <rect x="720" y="112" width="192" height="248" rx="14" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <path d="M720,126 A14,14 0 0 1 734,112 H898 A14,14 0 0 1 912,126 V152 H720 Z" fill="#F4EBFF"/>
  <circle cx="742" cy="132" r="11" fill="#7439B8"/>
  <text x="742" y="132" dy="0.35em" text-anchor="middle" fill="#FFFFFF" font-size="12" font-weight="700">4</text>
  <text class="bt" x="762" y="132" dy="0.35em" fill="#7439B8" data-fit="140">Tu app</text>
  <rect x="736" y="166" width="160" height="96" rx="10" fill="#F7F8FA"/>
  <circle cx="816" cy="202" r="24" fill="#FFF3DC" stroke="#7439B8" stroke-width="2"/>
  <circle cx="825" cy="192" r="5" fill="#A96C05"/>
  <path d="M798,216 L812,198 L824,210 L829,205 L835,214 A24,24 0 0 1 798,216 Z" fill="#A96C05" opacity="0.55"/>
  <rect x="788" y="236" width="56" height="7" rx="3.5" fill="#D9DEE8"/>
  <text class="tx" x="736" y="292" data-fit="168">La pantalla</text>
  <text class="tx" x="736" y="311" data-fit="168">muestra la foto</text>
  <text class="tx" x="736" y="330" data-fit="168">nueva.</text>
</svg>
```

Casi todo lo que hace una app se arma así: una pantalla que combina, a través del SDK, lo que le piden a varios servicios. Cada uno lo verás a fondo más adelante en el curso.
