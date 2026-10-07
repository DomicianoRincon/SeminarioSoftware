# StatelessWidget: tu primer componente

<!-- tags: StatelessWidget, crear un componente, pantalla hecha de piezas, parámetros con nombre, required, widget reutilizable, método build, campos final, lib/components, const en el constructor, The named parameter is required -->

Ya conoces los widgets básicos de Flutter y sabes acomodarlos con `Column` y `Row`. Con ellos se puede armar una pantalla entera, pero el código se vuelve largo y repetido muy rápido. La salida es hacer tus propios widgets: **componentes**.

## Una pantalla está hecha de piezas

Mira esta pantalla de perfil como la ve quien usa la app:

```svg
<svg id="swPantalla" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 866" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="swPantalla-ttl swPantalla-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="swPantalla-ttl">Una pantalla, como la ve quien usa la app</title>
  <desc id="swPantalla-dsc">Maqueta de una pantalla de perfil en un celular: la foto y los datos de la persona, tres indicadores con números, un botón azul Seguir y un botón con borde Enviar mensaje, una fila de cuatro contactos sugeridos y dos conversaciones recientes.</desc>
  <defs>
    <style>
      #swPantalla .title{fill:#161A26;font-size:22px;font-weight:700}
      #swPantalla .sub{fill:#79809A;font-size:13.5px}
      #swPantalla .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #swPantalla .nt{font-size:15px;font-weight:700;fill:#161A26}
      #swPantalla .nb{fill:#454C61;font-size:13px}
      #swPantalla .lbl{fill:#556074;font-size:12px;font-weight:600}
      #swPantalla .foot{fill:#79809A;font-size:12px}
      #swPantalla .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #swPantalla .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#swPantalla-arrow)}
    </style>
    <marker id="swPantalla-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="866" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Una pantalla, como la ve quien usa la app</text>
  <text class="sub" x="48" y="80" data-fit="860">Un perfil con sus datos, sus botones, contactos sugeridos y conversaciones. Parece una sola cosa.</text>
  <clipPath id="swPantalla-scr"><rect width="340" height="676" rx="28"/></clipPath>
  <rect x="300" y="114" width="360" height="696" rx="38" fill="#1F2430"/>
  <g transform="translate(310,124)"><g clip-path="url(#swPantalla-scr)">
    <rect width="340" height="676" fill="#FFFFFF"/>
    <path d="M30,24 H18 M23,19 L18,24 L23,29" fill="none" stroke="#161A26" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="170" y="29" font-size="16" font-weight="700" fill="#161A26" text-anchor="middle">Perfil</text>
    <circle cx="318" cy="17" r="1.9" fill="#161A26"/><circle cx="318" cy="24" r="1.9" fill="#161A26"/><circle cx="318" cy="31" r="1.9" fill="#161A26"/>
    <path d="M0,48 H340" stroke="#EFF1F5" stroke-width="1.5"/>
    <circle cx="170" cy="98" r="34" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><circle cx="170" cy="91.2" r="11.2" fill="#C9A6EE"/><path d="M148.9,123.2 a21.1,19.0 0 0 1 42.2,0 Z" fill="#C9A6EE"/>
    <text x="170" y="156" font-size="17" font-weight="700" fill="#161A26" text-anchor="middle">Mariana Valenzuela</text>
    <text x="170" y="176" font-size="12.5" font-weight="400" fill="#556074" text-anchor="middle">@marianav • Diseñadora de Producto</text>
    <g transform="translate(62,195) scale(.72)"><rect x="-9" y="-7" width="18" height="14" rx="2" fill="none" stroke="#556074" stroke-width="1.75"/><path d="M-9,-6 L0,1 L9,-6" fill="none" stroke="#556074" stroke-width="1.75"/></g><text x="74" y="199" font-size="12" font-weight="400" fill="#556074" text-anchor="start">m.val@estudio.com</text>
    <path d="M212,189 a5,5 0 0 1 10,0 c0,4 -5,9 -5,9 c0,0 -5,-5 -5,-9 Z" fill="none" stroke="#556074" stroke-width="1.4"/><circle cx="217" cy="189" r="1.6" fill="#556074"/><text x="227" y="199" font-size="12" font-weight="400" fill="#556074" text-anchor="start">Madrid, ES</text>
    <rect x="22" y="224" width="88" height="60" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="66" y="250" font-size="18" font-weight="700" fill="#161A26" text-anchor="middle">128</text><text x="66" y="270" font-size="12" font-weight="400" fill="#556074" text-anchor="middle">Publicaciones</text>
    <rect x="126" y="224" width="88" height="60" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="170" y="250" font-size="18" font-weight="700" fill="#161A26" text-anchor="middle">2.4k</text><text x="170" y="270" font-size="12" font-weight="400" fill="#556074" text-anchor="middle">Seguidores</text>
    <rect x="230" y="224" width="88" height="60" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="274" y="250" font-size="18" font-weight="700" fill="#161A26" text-anchor="middle">310</text><text x="274" y="270" font-size="12" font-weight="400" fill="#556074" text-anchor="middle">Seguidos</text>
    <rect x="16" y="302" width="308" height="40" rx="20" fill="#2196F3"/>
    <g transform="translate(136,322)"><circle cx="-2" cy="-4" r="3.5" fill="none" stroke="#FFFFFF" stroke-width="2"/><path d="M-9,8 a7,6 0 0 1 14,0" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/><path d="M7,-5 V1 M4,-2 H10" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/></g>
    <text x="154" y="327" font-size="14.5" font-weight="600" fill="#FFFFFF" text-anchor="start">Seguir</text>
    <rect x="16" y="352" width="308" height="40" rx="20" fill="#FFFFFF" stroke="#2196F3" stroke-width="1.75"/>
    <path d="M103,364 h18 a3,3 0 0 1 3,3 v9 a3,3 0 0 1 -3,3 h-9 l-5,4 v-4 h-4 a3,3 0 0 1 -3,-3 v-9 a3,3 0 0 1 3,-3 Z" fill="none" stroke="#1976D2" stroke-width="1.8" stroke-linejoin="round"/>
    <text x="134" y="377" font-size="14.5" font-weight="600" fill="#1976D2" text-anchor="start">Enviar mensaje</text>
    <text x="16" y="424" font-size="14" font-weight="700" fill="#161A26" text-anchor="start">Contactos sugeridos</text>
    <circle cx="52" cy="458" r="22" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="52" cy="453.6" r="7.3" fill="#A9B4F2"/><path d="M38.4,474.3 a13.6,12.3 0 0 1 27.3,0 Z" fill="#A9B4F2"/><text x="52" y="497" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle">Ana Torres</text><text x="52" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@anatorres</text>
    <circle cx="132" cy="458" r="22" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><circle cx="132" cy="453.6" r="7.3" fill="#86D3CA"/><path d="M118.4,474.3 a13.6,12.3 0 0 1 27.3,0 Z" fill="#86D3CA"/><text x="132" y="497" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle">Luis Peña</text><text x="132" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@luisp</text>
    <circle cx="212" cy="458" r="22" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><circle cx="212" cy="453.6" r="7.3" fill="#F3A3B2"/><path d="M198.4,474.3 a13.6,12.3 0 0 1 27.3,0 Z" fill="#F3A3B2"/><text x="212" y="497" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle">Sofía Ruiz</text><text x="212" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@sofiaruiz</text>
    <circle cx="292" cy="458" r="22" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="292" cy="453.6" r="7.3" fill="#F0C572"/><path d="M278.4,474.3 a13.6,12.3 0 0 1 27.3,0 Z" fill="#F0C572"/><text x="292" y="497" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle">Javier M…</text><text x="292" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@javim</text>
    <text x="16" y="548" font-size="14" font-weight="700" fill="#161A26" text-anchor="start">Últimas conversaciones</text>
    <circle cx="36" cy="584" r="20" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="36" cy="580.0" r="6.6" fill="#F0C572"/><path d="M23.6,598.8 a12.4,11.2 0 0 1 24.8,0 Z" fill="#F0C572"/><text x="66" y="581" font-size="13" font-weight="700" fill="#161A26" text-anchor="start">Javier Montes</text><text x="66" y="598" font-size="12" font-weight="400" fill="#556074" text-anchor="start">¿Te parece si revisamos los…</text><text x="324" y="581" font-size="12" font-weight="400" fill="#79809A" text-anchor="end">10:24 a.m.</text><path d="M306,594 l3,3 l6,-7 M312,597 l1,0 l6,-7" fill="none" stroke="#4453C9" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="36" cy="638" r="20" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><circle cx="36" cy="634.0" r="6.6" fill="#F3A3B2"/><path d="M23.6,652.8 a12.4,11.2 0 0 1 24.8,0 Z" fill="#F3A3B2"/><text x="66" y="635" font-size="13" font-weight="700" fill="#161A26" text-anchor="start">Sofía Ruiz</text><text x="66" y="652" font-size="12" font-weight="400" fill="#556074" text-anchor="start">Listo, ya subí los cambios</text><text x="324" y="635" font-size="12" font-weight="400" fill="#79809A" text-anchor="end">9:02 a.m.</text><path d="M306,648 l3,3 l6,-7 M312,651 l1,0 l6,-7" fill="none" stroke="#A0A8B8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
  </g></g>
  <text class="foot" x="480" y="842" text-anchor="middle" data-fit="860">Antes de seguir, cuenta: ¿cuántos bloques de esta pantalla se parecen entre sí?</text>
</svg>
```

Parece una sola cosa. Para quien la programa no lo es. Esta es la misma pantalla, con cada pieza marcada:

```svg
<svg id="swPiezas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 866" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="swPiezas-ttl swPiezas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="swPiezas-ttl">La misma pantalla, como la ve quien la programa</title>
  <desc id="swPiezas-dsc">La misma pantalla de perfil con cada componente marcado con un color y su nombre: ProfileInfo, StatsRow que contiene tres StatCard, PrimaryButton, SecondaryButton, cuatro ContactCard y dos ChatItem. Los nombres aparecen como piezas de Lego a los lados.</desc>
  <defs>
    <style>
      #swPiezas .title{fill:#161A26;font-size:22px;font-weight:700}
      #swPiezas .sub{fill:#79809A;font-size:13.5px}
      #swPiezas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #swPiezas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #swPiezas .nb{fill:#454C61;font-size:13px}
      #swPiezas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #swPiezas .foot{fill:#79809A;font-size:12px}
      #swPiezas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #swPiezas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#swPiezas-arrow)}
    </style>
    <marker id="swPiezas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="866" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La misma pantalla, como la ve quien la programa</text>
  <text class="sub" x="48" y="80" data-fit="860">Siete piezas distintas, usadas trece veces. Cada color es una pieza; el número dice cuántas veces aparece.</text>
  <clipPath id="swPiezas-scr"><rect width="340" height="676" rx="28"/></clipPath>
  <rect x="300" y="114" width="360" height="696" rx="38" fill="#1F2430"/>
  <g transform="translate(310,124)"><g clip-path="url(#swPiezas-scr)">
    <rect width="340" height="676" fill="#FFFFFF"/>
    <path d="M30,24 H18 M23,19 L18,24 L23,29" fill="none" stroke="#161A26" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="170" y="29" font-size="16" font-weight="700" fill="#161A26" text-anchor="middle">Perfil</text>
    <circle cx="318" cy="17" r="1.9" fill="#161A26"/><circle cx="318" cy="24" r="1.9" fill="#161A26"/><circle cx="318" cy="31" r="1.9" fill="#161A26"/>
    <path d="M0,48 H340" stroke="#EFF1F5" stroke-width="1.5"/>
    <circle cx="170" cy="98" r="34" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><circle cx="170" cy="91.2" r="11.2" fill="#C9A6EE"/><path d="M148.9,123.2 a21.1,19.0 0 0 1 42.2,0 Z" fill="#C9A6EE"/>
    <text x="170" y="156" font-size="17" font-weight="700" fill="#161A26" text-anchor="middle">Mariana Valenzuela</text>
    <text x="170" y="176" font-size="12.5" font-weight="400" fill="#556074" text-anchor="middle">@marianav • Diseñadora de Producto</text>
    <g transform="translate(62,195) scale(.72)"><rect x="-9" y="-7" width="18" height="14" rx="2" fill="none" stroke="#556074" stroke-width="1.75"/><path d="M-9,-6 L0,1 L9,-6" fill="none" stroke="#556074" stroke-width="1.75"/></g><text x="74" y="199" font-size="12" font-weight="400" fill="#556074" text-anchor="start">m.val@estudio.com</text>
    <path d="M212,189 a5,5 0 0 1 10,0 c0,4 -5,9 -5,9 c0,0 -5,-5 -5,-9 Z" fill="none" stroke="#556074" stroke-width="1.4"/><circle cx="217" cy="189" r="1.6" fill="#556074"/><text x="227" y="199" font-size="12" font-weight="400" fill="#556074" text-anchor="start">Madrid, ES</text>
    <rect x="22" y="224" width="88" height="60" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="66" y="250" font-size="18" font-weight="700" fill="#161A26" text-anchor="middle">128</text><text x="66" y="270" font-size="12" font-weight="400" fill="#556074" text-anchor="middle">Publicaciones</text>
    <rect x="126" y="224" width="88" height="60" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="170" y="250" font-size="18" font-weight="700" fill="#161A26" text-anchor="middle">2.4k</text><text x="170" y="270" font-size="12" font-weight="400" fill="#556074" text-anchor="middle">Seguidores</text>
    <rect x="230" y="224" width="88" height="60" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="274" y="250" font-size="18" font-weight="700" fill="#161A26" text-anchor="middle">310</text><text x="274" y="270" font-size="12" font-weight="400" fill="#556074" text-anchor="middle">Seguidos</text>
    <rect x="16" y="302" width="308" height="40" rx="20" fill="#2196F3"/>
    <g transform="translate(136,322)"><circle cx="-2" cy="-4" r="3.5" fill="none" stroke="#FFFFFF" stroke-width="2"/><path d="M-9,8 a7,6 0 0 1 14,0" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/><path d="M7,-5 V1 M4,-2 H10" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/></g>
    <text x="154" y="327" font-size="14.5" font-weight="600" fill="#FFFFFF" text-anchor="start">Seguir</text>
    <rect x="16" y="352" width="308" height="40" rx="20" fill="#FFFFFF" stroke="#2196F3" stroke-width="1.75"/>
    <path d="M103,364 h18 a3,3 0 0 1 3,3 v9 a3,3 0 0 1 -3,3 h-9 l-5,4 v-4 h-4 a3,3 0 0 1 -3,-3 v-9 a3,3 0 0 1 3,-3 Z" fill="none" stroke="#1976D2" stroke-width="1.8" stroke-linejoin="round"/>
    <text x="134" y="377" font-size="14.5" font-weight="600" fill="#1976D2" text-anchor="start">Enviar mensaje</text>
    <text x="16" y="424" font-size="14" font-weight="700" fill="#161A26" text-anchor="start">Contactos sugeridos</text>
    <circle cx="52" cy="458" r="22" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="52" cy="453.6" r="7.3" fill="#A9B4F2"/><path d="M38.4,474.3 a13.6,12.3 0 0 1 27.3,0 Z" fill="#A9B4F2"/><text x="52" y="497" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle">Ana Torres</text><text x="52" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@anatorres</text>
    <circle cx="132" cy="458" r="22" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/><circle cx="132" cy="453.6" r="7.3" fill="#86D3CA"/><path d="M118.4,474.3 a13.6,12.3 0 0 1 27.3,0 Z" fill="#86D3CA"/><text x="132" y="497" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle">Luis Peña</text><text x="132" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@luisp</text>
    <circle cx="212" cy="458" r="22" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><circle cx="212" cy="453.6" r="7.3" fill="#F3A3B2"/><path d="M198.4,474.3 a13.6,12.3 0 0 1 27.3,0 Z" fill="#F3A3B2"/><text x="212" y="497" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle">Sofía Ruiz</text><text x="212" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@sofiaruiz</text>
    <circle cx="292" cy="458" r="22" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="292" cy="453.6" r="7.3" fill="#F0C572"/><path d="M278.4,474.3 a13.6,12.3 0 0 1 27.3,0 Z" fill="#F0C572"/><text x="292" y="497" font-size="12" font-weight="700" fill="#161A26" text-anchor="middle">Javier M…</text><text x="292" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle">@javim</text>
    <text x="16" y="548" font-size="14" font-weight="700" fill="#161A26" text-anchor="start">Últimas conversaciones</text>
    <circle cx="36" cy="584" r="20" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="36" cy="580.0" r="6.6" fill="#F0C572"/><path d="M23.6,598.8 a12.4,11.2 0 0 1 24.8,0 Z" fill="#F0C572"/><text x="66" y="581" font-size="13" font-weight="700" fill="#161A26" text-anchor="start">Javier Montes</text><text x="66" y="598" font-size="12" font-weight="400" fill="#556074" text-anchor="start">¿Te parece si revisamos los…</text><text x="324" y="581" font-size="12" font-weight="400" fill="#79809A" text-anchor="end">10:24 a.m.</text><path d="M306,594 l3,3 l6,-7 M312,597 l1,0 l6,-7" fill="none" stroke="#4453C9" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="36" cy="638" r="20" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><circle cx="36" cy="634.0" r="6.6" fill="#F3A3B2"/><path d="M23.6,652.8 a12.4,11.2 0 0 1 24.8,0 Z" fill="#F3A3B2"/><text x="66" y="635" font-size="13" font-weight="700" fill="#161A26" text-anchor="start">Sofía Ruiz</text><text x="66" y="652" font-size="12" font-weight="400" fill="#556074" text-anchor="start">Listo, ya subí los cambios</text><text x="324" y="635" font-size="12" font-weight="400" fill="#79809A" text-anchor="end">9:02 a.m.</text><path d="M306,648 l3,3 l6,-7 M312,651 l1,0 l6,-7" fill="none" stroke="#A0A8B8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
  </g></g>
  <rect x="322" y="178" width="316" height="156" rx="10" fill="#4453C9" fill-opacity=".09" stroke="#4453C9" stroke-width="2.25"/>
  <rect x="320" y="340" width="320" height="76" rx="14" fill="#7439B8" fill-opacity=".09" stroke="#7439B8" stroke-width="2.25"/>
  <rect x="329" y="345" width="94" height="66" rx="12" fill="#A96C05" fill-opacity=".09" stroke="#A96C05" stroke-width="2.25"/>
  <rect x="433" y="345" width="94" height="66" rx="12" fill="#A96C05" fill-opacity=".09" stroke="#A96C05" stroke-width="2.25"/>
  <rect x="537" y="345" width="94" height="66" rx="12" fill="#A96C05" fill-opacity=".09" stroke="#A96C05" stroke-width="2.25"/>
  <rect x="322" y="422" width="316" height="48" rx="24" fill="#0F8478" fill-opacity=".09" stroke="#0F8478" stroke-width="2.25"/>
  <rect x="322" y="472" width="316" height="48" rx="24" fill="#3A8235" fill-opacity=".09" stroke="#3A8235" stroke-width="2.25"/>
  <rect x="326" y="556" width="72" height="88" rx="10" fill="#C2354F" fill-opacity=".09" stroke="#C2354F" stroke-width="2.25"/>
  <rect x="406" y="556" width="72" height="88" rx="10" fill="#C2354F" fill-opacity=".09" stroke="#C2354F" stroke-width="2.25"/>
  <rect x="486" y="556" width="72" height="88" rx="10" fill="#C2354F" fill-opacity=".09" stroke="#C2354F" stroke-width="2.25"/>
  <rect x="566" y="556" width="72" height="88" rx="10" fill="#C2354F" fill-opacity=".09" stroke="#C2354F" stroke-width="2.25"/>
  <rect x="320" y="683" width="320" height="50" rx="10" fill="#556074" fill-opacity=".09" stroke="#556074" stroke-width="2.25"/>
  <rect x="320" y="737" width="320" height="50" rx="10" fill="#556074" fill-opacity=".09" stroke="#556074" stroke-width="2.25"/>
  <path d="M638,256 H700" fill="none" stroke="#4453C9" stroke-width="2"/>
  <circle cx="638" cy="256" r="3.5" fill="#4453C9"/>
  <g transform="translate(700,236)">
    <rect x="20" y="-7" width="24" height="10" rx="3" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.75"/>
    <rect x="56" y="-7" width="24" height="10" rx="3" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.75"/>
    <rect x="92" y="-7" width="24" height="10" rx="3" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.75"/>
    <rect width="204" height="40" rx="7" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.75"/>
    <text class="mono" x="16" y="20" dy="0.35em" font-size="14" font-weight="700" fill="#4453C9" data-fit="140">ProfileInfo</text>
  </g>
  <path d="M640,378 H700" fill="none" stroke="#7439B8" stroke-width="2"/>
  <circle cx="640" cy="378" r="3.5" fill="#7439B8"/>
  <g transform="translate(700,358)">
    <rect x="20" y="-7" width="24" height="10" rx="3" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.75"/>
    <rect x="56" y="-7" width="24" height="10" rx="3" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.75"/>
    <rect x="92" y="-7" width="24" height="10" rx="3" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.75"/>
    <rect width="204" height="40" rx="7" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.75"/>
    <text class="mono" x="16" y="20" dy="0.35em" font-size="14" font-weight="700" fill="#7439B8" data-fit="140">StatsRow</text>
  </g>
  <path d="M260,378 H329" fill="none" stroke="#A96C05" stroke-width="2"/>
  <circle cx="329" cy="378" r="3.5" fill="#A96C05"/>
  <g transform="translate(56,358)">
    <rect x="20" y="-7" width="24" height="10" rx="3" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.75"/>
    <rect x="56" y="-7" width="24" height="10" rx="3" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.75"/>
    <rect x="92" y="-7" width="24" height="10" rx="3" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.75"/>
    <rect width="204" height="40" rx="7" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.75"/>
    <text class="mono" x="16" y="20" dy="0.35em" font-size="14" font-weight="700" fill="#A96C05" data-fit="140">StatCard</text>
    <circle cx="180" cy="20" r="13" fill="#A96C05"/>
    <text x="180" y="20" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#FFFFFF">×3</text>
  </g>
  <path d="M638,446 H700" fill="none" stroke="#0F8478" stroke-width="2"/>
  <circle cx="638" cy="446" r="3.5" fill="#0F8478"/>
  <g transform="translate(700,426)">
    <rect x="20" y="-7" width="24" height="10" rx="3" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.75"/>
    <rect x="56" y="-7" width="24" height="10" rx="3" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.75"/>
    <rect x="92" y="-7" width="24" height="10" rx="3" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.75"/>
    <rect width="204" height="40" rx="7" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.75"/>
    <text class="mono" x="16" y="20" dy="0.35em" font-size="14" font-weight="700" fill="#0F8478" data-fit="140">PrimaryButton</text>
  </g>
  <path d="M260,496 H322" fill="none" stroke="#3A8235" stroke-width="2"/>
  <circle cx="322" cy="496" r="3.5" fill="#3A8235"/>
  <g transform="translate(56,476)">
    <rect x="20" y="-7" width="24" height="10" rx="3" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.75"/>
    <rect x="56" y="-7" width="24" height="10" rx="3" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.75"/>
    <rect x="92" y="-7" width="24" height="10" rx="3" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.75"/>
    <rect width="204" height="40" rx="7" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.75"/>
    <text class="mono" x="16" y="20" dy="0.35em" font-size="14" font-weight="700" fill="#3A8235" data-fit="140">SecondaryButton</text>
  </g>
  <path d="M638,600 H700" fill="none" stroke="#C2354F" stroke-width="2"/>
  <circle cx="638" cy="600" r="3.5" fill="#C2354F"/>
  <g transform="translate(700,580)">
    <rect x="20" y="-7" width="24" height="10" rx="3" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.75"/>
    <rect x="56" y="-7" width="24" height="10" rx="3" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.75"/>
    <rect x="92" y="-7" width="24" height="10" rx="3" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.75"/>
    <rect width="204" height="40" rx="7" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.75"/>
    <text class="mono" x="16" y="20" dy="0.35em" font-size="14" font-weight="700" fill="#C2354F" data-fit="140">ContactCard</text>
    <circle cx="180" cy="20" r="13" fill="#C2354F"/>
    <text x="180" y="20" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#FFFFFF">×4</text>
  </g>
  <path d="M260,735 H284 M320,708 H284 V762 H320" fill="none" stroke="#556074" stroke-width="2"/>
  <circle cx="320" cy="708" r="3.5" fill="#556074"/>
  <circle cx="320" cy="762" r="3.5" fill="#556074"/>
  <g transform="translate(56,715)">
    <rect x="20" y="-7" width="24" height="10" rx="3" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.75"/>
    <rect x="56" y="-7" width="24" height="10" rx="3" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.75"/>
    <rect x="92" y="-7" width="24" height="10" rx="3" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.75"/>
    <rect width="204" height="40" rx="7" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.75"/>
    <text class="mono" x="16" y="20" dy="0.35em" font-size="14" font-weight="700" fill="#556074" data-fit="140">ChatItem</text>
    <circle cx="180" cy="20" r="13" fill="#556074"/>
    <text x="180" y="20" dy="0.35em" text-anchor="middle" font-size="12.5" font-weight="700" fill="#FFFFFF">×2</text>
  </g>
  <text class="foot" x="480" y="842" text-anchor="middle" data-fit="860">Lo que no está marcado, como la barra y los títulos, son widgets de Flutter usados directamente.</text>
</svg>
```

Tres cosas que se ven en la segunda imagen y no en la primera:

- **Son pocas piezas distintas.** Siete, aunque la pantalla tenga más de treinta textos, iconos y fotos.
- **Las piezas se repiten.** Hay cuatro `ContactCard`, tres `StatCard` y dos `ChatItem`. Cada grupo es la misma pieza con datos distintos: otro nombre, otra foto, otro número.
- **Las piezas encajan unas en otras.** `StatsRow` no es una pieza suelta: está armada con tres `StatCard`.

Funciona como un juego de **Lego**. Nadie fabrica un castillo de un solo bloque: hay unas pocas piezas pequeñas, se usan muchas veces y se encajan para formar cosas más grandes. Con las mismas piezas se arma otro castillo.

En Flutter cada pieza se llama **componente**, y trabajar así tiene tres ventajas muy concretas:

| | Qué ganas |
|---|---|
| Se construye por separado | Te concentras en una pieza pequeña, no en la pantalla entera |
| Se prueba sola | La montas en una pantalla vacía y ves si quedó bien, sin depender del resto |
| Se cambia en un solo lugar | Si el diseño de `ContactCard` cambia, lo editas una vez y cambian las cuatro |

En esta lección construyes la primera pieza, `StatCard`. En el taller haces las demás, y en la sesión 3 las encajas para armar esta pantalla.

## De copiar y pegar a un componente

Piensa en la fila de indicadores de un perfil: publicaciones, seguidores, seguidos. Son tres bloques idénticos en los que solo cambian dos datos.

```svg
<svg id="swRepetido" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 532" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="swRepetido-ttl swRepetido-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="swRepetido-ttl">Copiar y pegar, o hacer un componente</title>
  <desc id="swRepetido-dsc">A la izquierda, el mismo bloque de widgets copiado tres veces, donde solo cambian dos datos. A la derecha, un componente StatCard definido una vez y usado tres veces con datos distintos.</desc>
  <defs>
    <style>
      #swRepetido .title{fill:#161A26;font-size:22px;font-weight:700}
      #swRepetido .sub{fill:#79809A;font-size:13.5px}
      #swRepetido .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #swRepetido .nt{font-size:15px;font-weight:700;fill:#161A26}
      #swRepetido .nb{fill:#454C61;font-size:13px}
      #swRepetido .lbl{fill:#556074;font-size:12px;font-weight:600}
      #swRepetido .foot{fill:#79809A;font-size:12px}
      #swRepetido .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #swRepetido .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#swRepetido-arrow)}
      #swRepetido .code{font-size:12.5px;fill:#C9CFDA}
      #swRepetido .s{fill:#A8D8A0} #swRepetido .c{fill:#7FD1E8} #swRepetido .d{fill:#7F8AA3}
    </style>
    <marker id="swRepetido-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="532" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Copiar y pegar, o hacer un componente</text>
  <text class="sub" x="48" y="80" data-fit="860">La misma fila de tres indicadores, escrita de dos formas.</text>
  <text class="h" x="48" y="124">SIN COMPONENTE · EL MISMO BLOQUE, TRES VECES</text>
  <rect x="48" y="140" width="408" height="88" rx="10" fill="#1F2430"/>
  <text class="code mono" x="64" y="164" data-fit="376"><tspan class="c">Column</tspan>(children: [</text>
  <text class="code mono" x="80" y="186" data-fit="360"><tspan class="c">Text</tspan>(<tspan class="s">'128'</tspan>, <tspan class="d">style: …</tspan>),</text>
  <text class="code mono" x="80" y="208" data-fit="360"><tspan class="c">Text</tspan>(<tspan class="s">'Publicaciones'</tspan>, <tspan class="d">style: …</tspan>), ])</text>
  <rect x="48" y="240" width="408" height="88" rx="10" fill="#1F2430"/>
  <text class="code mono" x="64" y="264" data-fit="376"><tspan class="c">Column</tspan>(children: [</text>
  <text class="code mono" x="80" y="286" data-fit="360"><tspan class="c">Text</tspan>(<tspan class="s">'2.4k'</tspan>, <tspan class="d">style: …</tspan>),</text>
  <text class="code mono" x="80" y="308" data-fit="360"><tspan class="c">Text</tspan>(<tspan class="s">'Seguidores'</tspan>, <tspan class="d">style: …</tspan>), ])</text>
  <rect x="48" y="340" width="408" height="88" rx="10" fill="#1F2430"/>
  <text class="code mono" x="64" y="364" data-fit="376"><tspan class="c">Column</tspan>(children: [</text>
  <text class="code mono" x="80" y="386" data-fit="360"><tspan class="c">Text</tspan>(<tspan class="s">'310'</tspan>, <tspan class="d">style: …</tspan>),</text>
  <text class="code mono" x="80" y="408" data-fit="360"><tspan class="c">Text</tspan>(<tspan class="s">'Seguidos'</tspan>, <tspan class="d">style: …</tspan>), ])</text>
  <g transform="translate(48,464)">
    <text class="nb" x="0" y="0" font-weight="700" fill="#C2354F" data-fit="408">Cambiar el diseño = editar tres lugares sin equivocarse.</text>
  </g>
  <text class="h" x="504" y="124">CON COMPONENTE · SE ESCRIBE UNA VEZ</text>
  <g transform="translate(504,140)">
    <rect width="408" height="88" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="2.5"/>
    <text class="mono" x="20" y="34" font-size="16" font-weight="700" fill="#4453C9" data-fit="368">StatCard</text>
    <text class="nb" x="20" y="60" data-fit="368">El diseño vive aquí, en lib/components/stat_card.dart</text>
  </g>
  <path class="link" d="M708,228 V252"/>
  <text class="lbl" x="720" y="246" data-fit="180">se usa tres veces</text>
  <rect x="504" y="260" width="408" height="88" rx="10" fill="#1F2430"/>
  <text class="code mono" x="520" y="284" font-size="12" data-fit="380"><tspan class="c">StatCard</tspan>(number: <tspan class="s">'128'</tspan>, label: <tspan class="s">'Publicaciones'</tspan>),</text>
  <text class="code mono" x="520" y="306" font-size="12" data-fit="380"><tspan class="c">StatCard</tspan>(number: <tspan class="s">'2.4k'</tspan>, label: <tspan class="s">'Seguidores'</tspan>),</text>
  <text class="code mono" x="520" y="328" font-size="12" data-fit="380"><tspan class="c">StatCard</tspan>(number: <tspan class="s">'310'</tspan>, label: <tspan class="s">'Seguidos'</tspan>),</text>
  <g transform="translate(504,0)"><g transform="translate(36,364)"><rect width="96" height="72" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="48" y="32" text-anchor="middle" font-size="22" font-weight="700" fill="#161A26">128</text><text x="48" y="54" text-anchor="middle" font-size="11.5" fill="#556074" data-fit="88">Publicaciones</text></g><g transform="translate(156,364)"><rect width="96" height="72" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="48" y="32" text-anchor="middle" font-size="22" font-weight="700" fill="#161A26">2.4k</text><text x="48" y="54" text-anchor="middle" font-size="11.5" fill="#556074" data-fit="88">Seguidores</text></g><g transform="translate(276,364)"><rect width="96" height="72" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="48" y="32" text-anchor="middle" font-size="22" font-weight="700" fill="#161A26">310</text><text x="48" y="54" text-anchor="middle" font-size="11.5" fill="#556074" data-fit="88">Seguidos</text></g></g>
  <text class="nb" x="504" y="464" font-weight="700" fill="#3A8235" data-fit="408">Cambiar el diseño = editar un solo archivo.</text>
  <text class="foot" x="48" y="504" data-fit="860">La señal para crear un componente: estás copiando un bloque y solo le cambias los datos.</text>
</svg>
```

Copiar el bloque tres veces funciona hoy. El problema llega cuando cambia el diseño: hay que editar tres lugares, y con uno que se olvide la pantalla queda inconsistente. Un componente escribe el diseño **una sola vez** y deja por fuera únicamente lo que cambia.

La señal para crear uno es fácil de reconocer: estás copiando un bloque y solo le cambias los datos.

## Anatomía de un componente

Un componente es una clase que extiende `StatelessWidget`. Crea el archivo `lib/components/stat_card.dart`:

```svg
<svg id="swAnatomia" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 684" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="swAnatomia-ttl swAnatomia-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="swAnatomia-ttl">Anatomía de un componente</title>
  <desc id="swAnatomia-dsc">La clase StatCard anotada: extiende StatelessWidget, declara sus datos como campos final, los recibe en un constructor con parámetros con nombre y describe su aspecto en el método build.</desc>
  <defs>
    <style>
      #swAnatomia .title{fill:#161A26;font-size:22px;font-weight:700}
      #swAnatomia .sub{fill:#79809A;font-size:13.5px}
      #swAnatomia .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #swAnatomia .cl{font-size:13px;fill:#C9CFDA}
      #swAnatomia .s{fill:#A8D8A0} #swAnatomia .n{fill:#F2B880} #swAnatomia .c{fill:#7FD1E8}
      #swAnatomia .p{fill:#D5B8F5} #swAnatomia .k{fill:#F08FB0}
      #swAnatomia .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #swAnatomia .ct{fill:#161A26;font-size:14px;font-weight:700}
      #swAnatomia .cb{fill:#454C61;font-size:13px}
      #swAnatomia .rt{fill:#161A26;font-size:14px} #swAnatomia .rs{fill:#79809A;font-size:12px}
      #swAnatomia .foot{fill:#79809A;font-size:12px}
      #swAnatomia .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #swAnatomia .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #swAnatomia .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#swAnatomia-ar-amber)}
      #swAnatomia .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #swAnatomia .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #swAnatomia .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#swAnatomia-ar-green)}
      #swAnatomia .hl-indigo{fill:#A9B4F2;fill-opacity:.16;stroke:#A9B4F2;stroke-width:1.5}
      #swAnatomia .ld-indigo{fill:none;stroke:#A9B4F2;stroke-width:1.5;stroke-dasharray:3 4}
      #swAnatomia .ar-indigo{fill:none;stroke:#4453C9;stroke-width:1.75;marker-end:url(#swAnatomia-ar-indigo)}
      #swAnatomia .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #swAnatomia .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #swAnatomia .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#swAnatomia-ar-violet)}
    </style>
    <marker id="swAnatomia-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="swAnatomia-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="swAnatomia-ar-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#4453C9"/></marker>
    <marker id="swAnatomia-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="684" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Anatomía de un componente</text>
  <text class="sub" x="48" y="80" data-fit="860">Cuatro partes, siempre en este orden. Todos tus componentes van a tener esta forma.</text>
  <rect x="48" y="112" width="456" height="540" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/components/stat_card.dart</text>
  <rect x="552" y="112" width="360" height="540" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">LAS CUATRO PARTES</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-indigo" x="181.0" y="156" width="187.4" height="22" rx="5"/>
  <rect class="hl-amber" x="79.6" y="180" width="164.0" height="22" rx="5"/>
  <rect class="hl-green" x="79.6" y="252" width="132.8" height="22" rx="5"/>
  <rect class="hl-violet" x="79.6" y="420" width="273.2" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="312.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">class</tspan> <tspan class="c">StatCard</tspan> <tspan class="k">extends</tspan> <tspan class="c">StatelessWidget</tspan> {</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="156.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">final</tspan> <tspan class="c">String</tspan> number;</text>
  <text class="cl mono" font-size="13" x="83.6" y="220" textLength="148.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">final</tspan> <tspan class="c">String</tspan> label;</text>
  <text class="cl mono" font-size="13" x="83.6" y="268" textLength="124.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">const</tspan> <tspan class="c">StatCard</tspan>({</text>
  <text class="cl mono" font-size="13" x="99.2" y="292" textLength="78.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">super</tspan>.key,</text>
  <text class="cl mono" font-size="13" x="99.2" y="316" textLength="163.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">required</tspan> <tspan class="k">this</tspan>.number,</text>
  <text class="cl mono" font-size="13" x="99.2" y="340" textLength="156.0" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">required</tspan> <tspan class="k">this</tspan>.label,</text>
  <text class="cl mono" font-size="13" x="83.6" y="364" textLength="23.4" lengthAdjust="spacingAndGlyphs" data-fit="432">});</text>
  <text class="cl mono" font-size="13" x="83.6" y="412" textLength="70.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">@override</tspan></text>
  <text class="cl mono" font-size="13" x="83.6" y="436" textLength="280.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Widget</tspan> build(<tspan class="c">BuildContext</tspan> context) {</text>
  <text class="cl mono" font-size="13" x="99.2" y="460" textLength="109.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="k">return</tspan> <tspan class="c">Column</tspan>(</text>
  <text class="cl mono" font-size="13" x="114.8" y="484" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">children</tspan>: [</text>
  <text class="cl mono" font-size="13" x="130.4" y="508" textLength="101.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(number),</text>
  <text class="cl mono" font-size="13" x="130.4" y="532" textLength="93.6" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Text</tspan>(label),</text>
  <text class="cl mono" font-size="13" x="114.8" y="556" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="99.2" y="580" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">);</text>
  <text class="cl mono" font-size="13" x="83.6" y="604" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <text class="cl mono" font-size="13" x="68.0" y="628" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">}</text>
  <g transform="translate(552,144)">
<g transform="translate(16,16)"><rect width="328" height="68" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#4453C9" data-fit="300">1 · Es un StatelessWidget</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Un widget sin estado: recibe datos y los</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">muestra. No cambia por su cuenta.</text></g><g transform="translate(16,96)"><rect width="328" height="68" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#A96C05" data-fit="300">2 · Sus datos</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Campos final: llegan de afuera y no se</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">modifican. Son lo que cambia entre usos.</text></g><g transform="translate(16,176)"><rect width="328" height="68" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#3A8235" data-fit="300">3 · El constructor</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Así se le entregan los datos, por nombre.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">required obliga a pasarlos.</text></g><g transform="translate(16,256)"><rect width="328" height="68" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="14" y="23" font-size="13.5" font-weight="700" fill="#7439B8" data-fit="300">4 · build</text><text x="14" y="43" font-size="12.5" fill="#454C61" data-fit="300">Describe cómo se ve, usando sus datos.</text><text x="14" y="60" font-size="12.5" fill="#454C61" data-fit="300">Devuelve otros widgets.</text></g>
  </g>
  <path class="ld-indigo" d="M386.0,167 H504"/>
  <path class="ar-indigo" d="M504,167 H532 V194 H568"/>
  <path class="ld-amber" d="M245.6,191 H504"/>
  <path class="ar-amber" d="M504,191 H523 V274 H568"/>
  <path class="ld-green" d="M214.4,263 H504"/>
  <path class="ar-green" d="M504,263 H514 V354 H568"/>
  <path class="ld-violet" d="M370.4,431 H504"/>
  <path class="ar-violet" d="M504,431 H514 V434 H568"/>
</svg>
```

```dart
import 'package:flutter/material.dart';

/// Shows a number with its label.
class StatCard extends StatelessWidget {
  final String number;
  final String label;

  const StatCard({
    super.key,
    required this.number,
    required this.label,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(number),
        Text(label),
      ],
    );
  }
}
```

Las cuatro partes, en el orden en que aparecen:

1. **`extends StatelessWidget`**. *Stateless* significa sin estado: el componente recibe datos y los muestra, y no cambia por su cuenta. Es lo único que necesitas en esta sesión.
2. **Los campos `final`**. Son los datos del componente, lo que va a ser distinto en cada uso. `final` quiere decir que se asignan una vez y no se modifican.
3. **El constructor**. Las llaves `{ }` hacen que los parámetros se pasen **por nombre**, y `required` obliga a entregarlos. `super.key` se copia siempre igual: es un identificador que Flutter usa internamente.
4. **`build`**. Describe cómo se ve el componente a partir de sus campos. Devuelve otros widgets: aquí una `Column`, que pone un `Text` debajo del otro.

El editor escribe casi todo esto por ti: teclea `stless` y acepta la sugerencia.

Ahora dale el aspecto del diseño. Como el diseño vive en un solo lugar, basta con tocar `build`:

```dart
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(
          number,
          style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
        ),
        Text(
          label,
          style: const TextStyle(fontSize: 12, color: Colors.grey),
        ),
      ],
    );
  }
```

## Usarlo en una pantalla

Tu componente se usa igual que un `Text` o un `ElevatedButton`: se escribe su nombre y se le entregan sus datos.

```svg
<svg id="swUso" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 396" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="swUso-ttl swUso-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="swUso-ttl">Un componente, tres usos</title>
  <desc id="swUso-dsc">Una Row con tres StatCard, cada una con su number y su label. A la derecha, las tres tarjetas dibujadas, cada una señalada desde la línea de código que la crea.</desc>
  <defs>
    <style>
      #swUso .title{fill:#161A26;font-size:22px;font-weight:700}
      #swUso .sub{fill:#79809A;font-size:13.5px}
      #swUso .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #swUso .cl{font-size:13px;fill:#C9CFDA}
      #swUso .s{fill:#A8D8A0} #swUso .n{fill:#F2B880} #swUso .c{fill:#7FD1E8}
      #swUso .p{fill:#D5B8F5} #swUso .k{fill:#F08FB0}
      #swUso .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #swUso .ct{fill:#161A26;font-size:14px;font-weight:700}
      #swUso .cb{fill:#454C61;font-size:13px}
      #swUso .rt{fill:#161A26;font-size:14px} #swUso .rs{fill:#79809A;font-size:12px}
      #swUso .foot{fill:#79809A;font-size:12px}
      #swUso .hl-amber{fill:#F2C069;fill-opacity:.16;stroke:#F2C069;stroke-width:1.5}
      #swUso .ld-amber{fill:none;stroke:#F2C069;stroke-width:1.5;stroke-dasharray:3 4}
      #swUso .ar-amber{fill:none;stroke:#A96C05;stroke-width:1.75;marker-end:url(#swUso-ar-amber)}
      #swUso .hl-green{fill:#9FD68D;fill-opacity:.16;stroke:#9FD68D;stroke-width:1.5}
      #swUso .ld-green{fill:none;stroke:#9FD68D;stroke-width:1.5;stroke-dasharray:3 4}
      #swUso .ar-green{fill:none;stroke:#3A8235;stroke-width:1.75;marker-end:url(#swUso-ar-green)}
      #swUso .hl-violet{fill:#C9A6EE;fill-opacity:.16;stroke:#C9A6EE;stroke-width:1.5}
      #swUso .ld-violet{fill:none;stroke:#C9A6EE;stroke-width:1.5;stroke-dasharray:3 4}
      #swUso .ar-violet{fill:none;stroke:#7439B8;stroke-width:1.75;marker-end:url(#swUso-ar-violet)}
    </style>
    <marker id="swUso-ar-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#A96C05"/></marker>
    <marker id="swUso-ar-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#3A8235"/></marker>
    <marker id="swUso-ar-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#7439B8"/></marker>
  </defs>
  <rect width="960" height="396" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Un componente, tres usos</text>
  <text class="sub" x="48" y="80" data-fit="860">Tu componente se usa como cualquier widget de Flutter. Cada línea produce una tarjeta distinta.</text>
  <rect x="48" y="112" width="456" height="252" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H492 A12,12 0 0 1 504,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text class="mono" x="276" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12" data-fit="316">lib/screens/home_screen.dart</text>
  <rect x="552" y="112" width="360" height="252" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text class="h" x="568" y="128" dy="0.35em" data-fit="328">RESULTADO</text>
  <path d="M552,144 H912" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect class="hl-amber" x="95.2" y="204" width="374.6" height="22" rx="5"/>
  <rect class="hl-green" x="95.2" y="228" width="359.0" height="22" rx="5"/>
  <rect class="hl-violet" x="95.2" y="252" width="335.6" height="22" rx="5"/>
  <text class="cl mono" font-size="13" x="68.0" y="172" textLength="31.2" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">Row</tspan>(</text>
  <text class="cl mono" font-size="13" x="83.6" y="196" textLength="85.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="p">children</tspan>: [</text>
  <text class="cl mono" font-size="13" x="99.2" y="220" textLength="374.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">StatCard</tspan>(<tspan class="p">number</tspan>: <tspan class="s">'128'</tspan>, <tspan class="p">label</tspan>: <tspan class="s">'Publicaciones'</tspan>),</text>
  <text class="cl mono" font-size="13" x="99.2" y="244" textLength="358.8" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">StatCard</tspan>(<tspan class="p">number</tspan>: <tspan class="s">'2.4k'</tspan>, <tspan class="p">label</tspan>: <tspan class="s">'Seguidores'</tspan>),</text>
  <text class="cl mono" font-size="13" x="99.2" y="268" textLength="335.4" lengthAdjust="spacingAndGlyphs" data-fit="432"><tspan class="c">StatCard</tspan>(<tspan class="p">number</tspan>: <tspan class="s">'310'</tspan>, <tspan class="p">label</tspan>: <tspan class="s">'Seguidos'</tspan>),</text>
  <text class="cl mono" font-size="13" x="83.6" y="292" textLength="15.6" lengthAdjust="spacingAndGlyphs" data-fit="432">],</text>
  <text class="cl mono" font-size="13" x="68.0" y="316" textLength="7.8" lengthAdjust="spacingAndGlyphs" data-fit="432">)</text>
  <g transform="translate(552,144)">
<g transform="translate(24,56)"><rect width="96" height="72" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><text x="48" y="32" text-anchor="middle" font-size="22" font-weight="700" fill="#161A26">128</text><text x="48" y="54" text-anchor="middle" font-size="11.5" fill="#556074" data-fit="88">Publicaciones</text></g><g transform="translate(132,56)"><rect width="96" height="72" rx="10" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="48" y="32" text-anchor="middle" font-size="22" font-weight="700" fill="#161A26">2.4k</text><text x="48" y="54" text-anchor="middle" font-size="11.5" fill="#556074" data-fit="88">Seguidores</text></g><g transform="translate(240,56)"><rect width="96" height="72" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="48" y="32" text-anchor="middle" font-size="22" font-weight="700" fill="#161A26">310</text><text x="48" y="54" text-anchor="middle" font-size="11.5" fill="#556074" data-fit="88">Seguidos</text></g>
  </g>
  <path class="ld-amber" d="M479.6,215 H504"/>
  <path class="ar-amber" d="M504,215 H532 V296 H624 V276 H624"/>
  <path class="ld-green" d="M464.0,239 H504"/>
  <path class="ar-green" d="M504,239 H523 V310 H732 V276 H732"/>
  <path class="ld-violet" d="M440.6,263 H504"/>
  <path class="ar-violet" d="M504,263 H514 V324 H840 V276 H840"/>
</svg>
```

```dart
Row(
  children: [
    StatCard(number: '128', label: 'Publicaciones'),
    StatCard(number: '2.4k', label: 'Seguidores'),
    StatCard(number: '310', label: 'Seguidos'),
  ],
)
```

Dentro de una `Row`, tus tres tarjetas se comportan como cualquier otro hijo: puedes repartirlas con `mainAxisAlignment`, como viste en la lección anterior.

Para verlo, impórtalo en `lib/screens/home_screen.dart`:

```dart
import 'package:flutter/material.dart';
import 'package:miapp1/components/stat_card.dart';

/// First screen of the app.
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Inicio')),
      body: const Center(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            StatCard(number: '128', label: 'Publicaciones'),
            StatCard(number: '2.4k', label: 'Seguidores'),
            StatCard(number: '310', label: 'Seguidos'),
          ],
        ),
      ),
    );
  }
}
```

Si olvidas un dato, el editor lo marca antes de ejecutar: `The named parameter 'label' is required, but there's no corresponding argument`. Ese es el trabajo de `required`.

## Dónde vive y cómo se llama

| | Regla | Ejemplo |
|---|---|---|
| Carpeta | Todos los componentes van en `lib/components/` | `lib/components/stat_card.dart` |
| Archivo | Minúsculas y guion bajo, un componente por archivo | `stat_card.dart` |
| Clase | Cada palabra con mayúscula inicial, sin separadores | `StatCard` |
| Idioma | El código en inglés. Los textos que ve la persona, en español | `label: 'Seguidores'` |

Dos ideas para llevarte al taller:

- **Un componente puede usar otros componentes.** Una fila de estadísticas es un componente hecho con tres `StatCard`, y una tarjeta de perfil puede contener esa fila. Las pantallas se arman así, de lo pequeño a lo grande.
- **Todavía no hay interacción.** Un `StatelessWidget` solo muestra. Si tu componente lleva un botón, déjale un `onPressed` con un `print`. Cómo avisarle a la pantalla que lo tocaron es la sesión 7.

En el *Taller · Componentes* construyes seis. Los necesitas terminados para la sesión 3, donde se arman las pantallas con ellos.

## Ejemplo completo

`StatCard` y la pantalla que lo usa tres veces. Cambia el diseño dentro de `build` y mira cómo cambian las tres tarjetas a la vez.

```dart trycode=07821fc61f162124e3d4060bd48c0be9
import 'package:flutter/material.dart';

void main() {
  runApp(const App());
}

/// Root widget of the app.
class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mi app',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      initialRoute: '/home',
      routes: {'/home': (context) => const HomeScreen()},
    );
  }
}

/// First screen of the app.
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Inicio')),
      body: const Center(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            StatCard(number: '128', label: 'Publicaciones'),
            StatCard(number: '2.4k', label: 'Seguidores'),
            StatCard(number: '310', label: 'Seguidos'),
          ],
        ),
      ),
    );
  }
}

/// Shows a number with its label.
class StatCard extends StatelessWidget {
  final String number;
  final String label;

  const StatCard({
    super.key,
    required this.number,
    required this.label,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(
          number,
          style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
        ),
        Text(
          label,
          style: const TextStyle(fontSize: 12, color: Colors.grey),
        ),
      ],
    );
  }
}
```

Aquí todo va en un solo archivo porque el editor en línea solo tiene uno. En tu proyecto `StatCard` va en `lib/components/stat_card.dart` y la pantalla lo importa.
