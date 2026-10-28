# La pila de pantallas

<!-- tags: Navigator, pila de pantallas, Route, push y pop, botón atrás, la pantalla de abajo sigue viva, initState no se repite al volver, la app se cierra al volver, flecha atrás del AppBar -->

Hasta ahora la app tenía una sola pantalla. Para tener varias, Flutter usa un objeto que ya viene dentro de `MaterialApp`: el **Navigator**. Hace una sola cosa: guarda las pantallas abiertas, una encima de otra, como una pila de cartas.

Pruébalo: entra, abre una canción y vuelve. A la derecha está la pila.

```interactive
nav-stack
```

## Una encima de otra

```svg
<svg id="plPila" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="plPila-ttl plPila-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="plPila-ttl">La pila de pantallas</title>
  <desc id="plPila-dsc">A la izquierda, un celular con SongDetailScreen de la canción Yellow. A la derecha, la pila con tres tarjetas: arriba la ruta /song con SongDetailScreen, visible; en medio /playlist con PlaylistScreen y abajo / con LoginScreen, las dos marcadas como debajo y vivas. Una flecha azul entra por arriba: pushNamed pone una encima. Una flecha naranja sale por arriba: pop quita la de arriba. Debajo, tres tarjetas: solo se ve la de arriba, las de abajo siguen vivas, y atrás es un pop.</desc>
  <defs>
    <style>
      #plPila .title{fill:#161A26;font-size:22px;font-weight:700}
      #plPila .sub{fill:#79809A;font-size:13.5px}
      #plPila .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #plPila .nt{font-size:15px;font-weight:700;fill:#161A26}
      #plPila .nb{fill:#454C61;font-size:13px}
      #plPila .lbl{fill:#556074;font-size:12px;font-weight:600}
      #plPila .foot{fill:#79809A;font-size:12px}
      #plPila .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #plPila .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#plPila-arrow)}
    </style>
    <marker id="plPila-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="plPila-push" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#2F6FD6"/></marker><marker id="plPila-pop" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C27A0E"/></marker><marker id="plPila-reset" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/></marker>
  </defs>
  <rect width="960" height="520" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La pila de pantallas</text>
  <text class="sub" x="48" y="80" data-fit="860">El Navigator guarda las pantallas abiertas una encima de otra. Solo se ve la de arriba.</text>
  <clipPath id="plPila-p"><rect width="170" height="270" rx="20"/></clipPath><rect x="65" y="113" width="184" height="284" rx="27" fill="#1F2430"/><g transform="translate(72,120)"><g clip-path="url(#plPila-p)"><rect width="170" height="270" rx="20" fill="#FEF7FF"/><rect width="170" height="40.0" fill="#D0BCFF"/><text x="12.0" y="26.0" font-size="15.0" font-weight="600" fill="#161A26" text-anchor="start">←</text><text x="32.0" y="26.0" font-size="13.5" font-weight="600" fill="#161A26" text-anchor="start" data-fit="130.0">Yellow</text><rect x="50.0" y="54" width="70" height="70" rx="14" fill="#9C7FE0"/><text x="85.0" y="142" font-size="13" font-weight="700" fill="#161A26" text-anchor="middle">Yellow</text><text x="85.0" y="158" font-size="11" font-weight="400" fill="#625B71" text-anchor="middle">Coldplay</text><rect x="15.0" y="170" width="140" height="26.0" rx="13.0" fill="#6750A4"/><text x="85.0" y="187.0" font-size="11.5" font-weight="600" fill="#FFFFFF" text-anchor="middle">Volver</text></g></g>
  <text x="404" y="128" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="h">LA PILA DEL NAVIGATOR</text>
  <rect x="404" y="200" width="372" height="52" rx="10" fill="#FFFFFF" stroke="#6750A4" stroke-width="1.5"/><text x="420" y="222" font-size="13" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">'/song'</text><text x="420" y="241" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">SongDetailScreen</text><rect x="696.4" y="215" width="67.6" height="22" rx="11" fill="#E8F6E3"/><text x="730.2" y="230" font-size="11.5" font-weight="600" fill="#3A8235" text-anchor="middle">visible</text>
  <rect x="404" y="262" width="372" height="52" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="420" y="284" font-size="13" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">'/playlist'</text><text x="420" y="303" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">PlaylistScreen</text><rect x="655.6" y="277" width="108.4" height="22" rx="11" fill="#EEF1FF"/><text x="709.8" y="292" font-size="11.5" font-weight="600" fill="#4453C9" text-anchor="middle">debajo · viva</text>
  <rect x="404" y="324" width="372" height="52" rx="10" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="420" y="346" font-size="13" font-weight="700" fill="#6750A4" text-anchor="start" class="mono">'/'</text><text x="420" y="365" font-size="12.5" font-weight="400" fill="#161A26" text-anchor="start" class="mono">LoginScreen</text><rect x="655.6" y="339" width="108.4" height="22" rx="11" fill="#EEF1FF"/><text x="709.8" y="354" font-size="11.5" font-weight="600" fill="#4453C9" text-anchor="middle">debajo · viva</text>
  <path d="M404,390 H776" stroke="#C4CBD8" stroke-width="3"/><text x="590.0" y="408" font-size="11.5" font-weight="500" fill="#79809A" text-anchor="middle">base de la pila</text>
  <path d="M260,226 H390" stroke="#9AA1B2" stroke-width="1.75" stroke-dasharray="5 5"/>
  <path d="M514,140 V190" fill="none" stroke="#2F6FD6" stroke-width="2.25" marker-end="url(#plPila-push)"/>
  <text x="504" y="162" font-size="12.5" font-weight="700" fill="#2F6FD6" text-anchor="end" class="mono">pushNamed</text>
  <text x="504" y="178" font-size="12" font-weight="400" fill="#454C61" text-anchor="end">pone una encima</text>
  <path d="M666,190 V140" fill="none" stroke="#C27A0E" stroke-width="2.25" marker-end="url(#plPila-pop)"/>
  <text x="678" y="162" font-size="12.5" font-weight="700" fill="#C27A0E" text-anchor="start" class="mono">pop</text>
  <text x="678" y="178" font-size="12" font-weight="400" fill="#454C61" text-anchor="start">quita la de arriba</text>
  <rect x="48" y="420" width="272" height="84" rx="12" fill="#FFFFFF" stroke="#C9A6EE" stroke-width="1.5"/><text x="64" y="451" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="244">Solo se ve la de arriba</text><text x="64" y="478" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">La pantalla visible es la última</text><text x="64" y="497" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">que entró a la pila.</text>
  <rect x="344" y="420" width="272" height="84" rx="12" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.5"/><text x="360" y="451" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="244">Las de abajo siguen vivas</text><text x="360" y="478" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">No se destruyen: su State y sus</text><text x="360" y="497" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">datos esperan intactos.</text>
  <rect x="640" y="420" width="272" height="84" rx="12" fill="#FFFFFF" stroke="#F0C572" stroke-width="1.5"/><text x="656" y="451" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" data-fit="244">Atrás es un pop</text><text x="656" y="478" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">La flecha del AppBar y el botón</text><text x="656" y="497" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="240">del sistema sacan la de arriba.</text>
</svg>
```

Cada pantalla abierta es una **ruta** (`Route`) de la pila. Abrir una pantalla es ponerla encima: eso se llama **push**. Volver es quitar la de arriba: eso es **pop**. La pantalla que se ve es siempre la de arriba.

## La de abajo sigue viva

Cuando se abre una pantalla encima, la de abajo no se destruye. Su State se queda en memoria con todos sus datos, así que al volver la lista está igual que antes y `initState` no corre otra vez.

La que sí se destruye es la que sale. Al hacer pop, su State corre `dispose()`, igual que en la sesión 6 cuando se cerraba la app del saludo.

## Atrás es un pop

Nadie programa el botón atrás. La flecha que el `AppBar` pone sola y el botón atrás del sistema en Android hacen lo mismo: sacan la ruta de arriba. En iPhone, el gesto de deslizar desde el borde izquierdo también.

El `AppBar` solo pone la flecha cuando hay algo debajo a dónde volver. Si la ruta que sale era la única, no queda nada que mostrar y la app se cierra. Pruébalo en el interactivo: toca atrás en la primera pantalla.

## Qué se apila

Lo que se apila son **Screens**: widgets cuya raíz es un `Scaffold`, cada uno con su barra. Por eso cada pantalla nueva de esta sesión es una clase `XxxScreen` en `screens/`. Cambiar de pestaña dentro de una misma pantalla es otra cosa, y es el tema de la sesión 9.
