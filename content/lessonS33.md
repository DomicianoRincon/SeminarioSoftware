# Una skill para armar pantallas

<!-- tags: skill flutter-pantallas, paleta de widgets, componentes reutilizables, el agente usa widgets que no hemos visto, ListView no lo hemos visto, plantilla de componente, plantilla de pantalla, auditar una pantalla generada, reutilizar un componente, pantallas sin navegación, widgets.md -->

En el taller armaste una skill que dibuja. Esta es otra, ya escrita, para lo que más vas a pedirle al agente: **armar pantallas**. Hace dos cosas: lo limita a los widgets que has visto y lo obliga a pensar en componentes reutilizables.

## Por qué hace falta

En *El archivo de contexto* el agente armó la pantalla de inicio con `ListView`, y sin contexto usó además `ClipRRect` y una clase privada. Funciona, pero es código que todavía no puedes revisar: no has visto esos widgets. Y nunca aceptas un cambio que no entiendes.

El `AGENTS.md` no es el lugar para una lista de treinta widgets: viaja en cada pedido. Una skill sí: solo se carga cuando pides una pantalla.

## La carpeta

```svg
<svg id="fpCarpeta" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 592" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpCarpeta-ttl fpCarpeta-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpCarpeta-ttl">La segunda skill del proyecto</title>
  <desc id="fpCarpeta-dsc">El árbol de mi_app_1: dentro de .agents y skills, junto a la skill mer-svg que ya existe, la carpeta nueva flutter-pantallas con SKILL.md, que son los pasos; references con widgets.md, que es la paleta; y assets con dos plantillas, component.dart y screen.dart.</desc>
  <defs>
    <style>
      #fpCarpeta .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpCarpeta .sub{fill:#79809A;font-size:13.5px}
      #fpCarpeta .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #fpCarpeta .nt{font-size:15px;font-weight:700;fill:#161A26}
      #fpCarpeta .nb{fill:#454C61;font-size:13px}
      #fpCarpeta .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fpCarpeta .foot{fill:#79809A;font-size:12px}
      #fpCarpeta .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpCarpeta .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fpCarpeta-arrow)}
    </style>
    <marker id="fpCarpeta-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="592" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La segunda skill del proyecto</text>
  <text class="sub" x="48" y="80" data-fit="860">Va junto a mer-svg, en la misma carpeta skills. Cuatro archivos.</text>
  <path d="M64,132 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="98" y="145" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">mi_app_1/</text>
  <path d="M76,150 V180 H98" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M104,172 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="138" y="185" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">.agents/</text>
  <path d="M116,190 V220 H138" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M144,212 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="178" y="225" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">skills/</text>
  <g opacity=".55"><path d="M156,230 V260 H178" fill="none" stroke="#C4CBD8" stroke-width="1.5"/><path d="M184,252 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/><text x="218" y="265" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">mer-svg/</text></g>
  <path d="M156,230 V300 H178" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M184,292 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="218" y="305" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">flutter-pantallas/</text>
  <rect x="470" y="290" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="498" y="305" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M196,310 V340 H218" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M228,331 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="258" y="345" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">SKILL.md</text>
  <rect x="470" y="330" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="498" y="345" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M196,310 V380 H218" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M224,372 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="258" y="385" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">references/</text>
  <rect x="470" y="370" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="498" y="385" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M236,390 V420 H258" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M268,411 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="298" y="425" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">widgets.md</text>
  <rect x="470" y="410" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="498" y="425" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M196,310 V460 H218" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M224,452 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="258" y="465" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" class="mono">assets/</text>
  <rect x="470" y="450" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="498" y="465" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M236,470 V500 H258" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M268,491 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="298" y="505" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">component.dart</text>
  <rect x="470" y="490" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="498" y="505" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M236,470 V540 H258" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M268,531 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/>
  <text x="298" y="545" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">screen.dart</text>
  <rect x="470" y="530" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="498" y="545" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <rect x="552" y="323" width="360" height="34" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="570" y="344.5" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="330"><tspan font-weight="700" fill="#4453C9">Los pasos.</tspan> Cómo se arma una pantalla.</text>
  <rect x="552" y="403" width="360" height="34" rx="10" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="570" y="424.5" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="330"><tspan font-weight="700" fill="#0F8478">La paleta.</tspan> Los únicos widgets permitidos.</text>
  <rect x="552" y="483" width="360" height="34" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="570" y="504.5" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="330"><tspan font-weight="700" fill="#A96C05">Plantilla.</tspan> Cómo se escribe un componente.</text>
  <rect x="552" y="523" width="360" height="34" rx="10" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="570" y="544.5" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="330"><tspan font-weight="700" fill="#A96C05">Plantilla.</tspan> Cómo se escribe una pantalla.</text>
</svg>
```

Crea `flutter-pantallas` dentro de `.agents/skills/`, con sus carpetas `references` y `assets`, igual que hiciste con `mer-svg`.

## SKILL.md

```markdown
---
name: flutter-pantallas
description: Construye pantallas y componentes de Flutter con la paleta mínima de widgets del curso y componentes reutilizables. Úsala cuando pidan crear o cambiar una pantalla, una sección o un componente de la app.
---

# Pantallas de Flutter

Armas pantallas estáticas: se ven, pero todavía no navegan ni guardan estado.

## Pasos

1. Lee `references/widgets.md`. Es la paleta: los únicos widgets que puedes usar.
2. Mira qué hay en `lib/components/`. Si un componente ya sirve, úsalo.
3. Divide la pantalla en bloques, de arriba hacia abajo.
4. Lo que se repite, o lo que podría servir en otra pantalla, es un componente: se escribe una vez y recibe sus datos por parámetros.
5. Escribe cada componente nuevo en su archivo de `lib/components/`, a partir de `assets/component.dart`.
6. Escribe la pantalla en `lib/screens/`, a partir de `assets/screen.dart`. La pantalla solo acomoda componentes.
7. Registra la pantalla en `routes` de `lib/main.dart`.
8. Ejecuta `flutter analyze`.

## Reglas

- Solo `StatelessWidget`. Los datos de ejemplo van escritos en el código.
- Los botones no navegan ni cambian nada: `onPressed: () {}`.
- Un componente no conoce la pantalla que lo usa: todo lo que cambia entre un uso y otro llega por el constructor.
- Si lo pedido necesita algo fuera de la paleta, no lo uses: dilo y propón cómo acercarse con la paleta.
```

Los pasos 2 a 4 son el concepto de componente de la sesión 2, escrito como instrucción: primero mirar qué existe, después dividir, y sacar a un componente lo que se repite.

## references/widgets.md

```svg
<svg id="fpPaleta" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 554" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpPaleta-ttl fpPaleta-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpPaleta-ttl">La paleta de widgets</title>
  <desc id="fpPaleta-dsc">Los widgets permitidos, en cinco grupos. Contenido: Text, Icon, Image y CircleAvatar. Botones: ElevatedButton, OutlinedButton, TextButton e IconButton. Entrada: TextField. Acomodar: Column, Row, SizedBox, Expanded, Spacer, Padding, Container, Card, Center y SingleChildScrollView. Estructura: Scaffold, SafeArea, AppBar, BottomNavigationBar y FloatingActionButton. Fuera de la paleta por ahora: ListView, GridView, Stack, ListTile, StatefulWidget, Navigator y cualquier paquete nuevo.</desc>
  <defs>
    <style>
      #fpPaleta .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpPaleta .sub{fill:#79809A;font-size:13.5px}
      #fpPaleta .h{font-size:12px;font-weight:700;letter-spacing:.08em}
      #fpPaleta .nt{font-size:15px;font-weight:700;fill:#161A26}
      #fpPaleta .nb{fill:#454C61;font-size:13px}
      #fpPaleta .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fpPaleta .foot{fill:#79809A;font-size:12px}
      #fpPaleta .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpPaleta .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fpPaleta-arrow)}
    </style>
    <marker id="fpPaleta-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="554" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La paleta de widgets</text>
  <text class="sub" x="48" y="80" data-fit="860">Lo que has visto hasta la sesión 3. El agente arma las pantallas solo con esto.</text>
  <text x="48" y="133" font-size="12" font-weight="700" fill="#4453C9" text-anchor="start" class="h">CONTENIDO</text>
  <rect x="176" y="113" width="58" height="30" rx="15" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="205.0" y="132.5" font-size="13" font-weight="600" fill="#4453C9" text-anchor="middle" class="mono">Text</text>
  <rect x="242" y="113" width="58" height="30" rx="15" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="271.0" y="132.5" font-size="13" font-weight="600" fill="#4453C9" text-anchor="middle" class="mono">Icon</text>
  <rect x="308" y="113" width="66" height="30" rx="15" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="341.0" y="132.5" font-size="13" font-weight="600" fill="#4453C9" text-anchor="middle" class="mono">Image</text>
  <rect x="382" y="113" width="123" height="30" rx="15" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text x="443.5" y="132.5" font-size="13" font-weight="600" fill="#4453C9" text-anchor="middle" class="mono">CircleAvatar</text>
  <text x="48" y="181" font-size="12" font-weight="700" fill="#7439B8" text-anchor="start" class="h">BOTONES</text>
  <rect x="176" y="161" width="139" height="30" rx="15" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="245.5" y="180.5" font-size="13" font-weight="600" fill="#7439B8" text-anchor="middle" class="mono">ElevatedButton</text>
  <rect x="323" y="161" width="139" height="30" rx="15" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="392.5" y="180.5" font-size="13" font-weight="600" fill="#7439B8" text-anchor="middle" class="mono">OutlinedButton</text>
  <rect x="470" y="161" width="107" height="30" rx="15" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="523.5" y="180.5" font-size="13" font-weight="600" fill="#7439B8" text-anchor="middle" class="mono">TextButton</text>
  <rect x="585" y="161" width="107" height="30" rx="15" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text x="638.5" y="180.5" font-size="13" font-weight="600" fill="#7439B8" text-anchor="middle" class="mono">IconButton</text>
  <text x="48" y="229" font-size="12" font-weight="700" fill="#A96C05" text-anchor="start" class="h">ENTRADA</text>
  <rect x="176" y="209" width="99" height="30" rx="15" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text x="225.5" y="228.5" font-size="13" font-weight="600" fill="#A96C05" text-anchor="middle" class="mono">TextField</text>
  <text x="48" y="277" font-size="12" font-weight="700" fill="#0F8478" text-anchor="start" class="h">ACOMODAR</text>
  <rect x="176" y="257" width="75" height="30" rx="15" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="213.5" y="276.5" font-size="13" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">Column</text>
  <rect x="259" y="257" width="50" height="30" rx="15" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="284.0" y="276.5" font-size="13" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">Row</text>
  <rect x="317" y="257" width="91" height="30" rx="15" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="362.5" y="276.5" font-size="13" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">SizedBox</text>
  <rect x="416" y="257" width="91" height="30" rx="15" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="461.5" y="276.5" font-size="13" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">Expanded</text>
  <rect x="515" y="257" width="75" height="30" rx="15" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="552.5" y="276.5" font-size="13" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">Spacer</text>
  <rect x="598" y="257" width="83" height="30" rx="15" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="639.5" y="276.5" font-size="13" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">Padding</text>
  <rect x="689" y="257" width="99" height="30" rx="15" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="738.5" y="276.5" font-size="13" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">Container</text>
  <rect x="796" y="257" width="58" height="30" rx="15" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="825.0" y="276.5" font-size="13" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">Card</text>
  <rect x="176" y="297" width="75" height="30" rx="15" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="213.5" y="316.5" font-size="13" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">Center</text>
  <rect x="259" y="297" width="196" height="30" rx="15" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="357.0" y="316.5" font-size="13" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">SingleChildScrollView</text>
  <text x="48" y="365" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="h">ESTRUCTURA</text>
  <rect x="176" y="345" width="91" height="30" rx="15" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="221.5" y="364.5" font-size="13" font-weight="600" fill="#556074" text-anchor="middle" class="mono">Scaffold</text>
  <rect x="275" y="345" width="91" height="30" rx="15" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="320.5" y="364.5" font-size="13" font-weight="600" fill="#556074" text-anchor="middle" class="mono">SafeArea</text>
  <rect x="374" y="345" width="75" height="30" rx="15" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="411.5" y="364.5" font-size="13" font-weight="600" fill="#556074" text-anchor="middle" class="mono">AppBar</text>
  <rect x="457" y="345" width="180" height="30" rx="15" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="547.0" y="364.5" font-size="13" font-weight="600" fill="#556074" text-anchor="middle" class="mono">BottomNavigationBar</text>
  <rect x="645" y="345" width="188" height="30" rx="15" fill="#EFF1F5" stroke="#C4CBD8" stroke-width="1.5"/>
  <text x="739.0" y="364.5" font-size="13" font-weight="600" fill="#556074" text-anchor="middle" class="mono">FloatingActionButton</text>
  <path d="M48,404 H912" stroke="#D9DEE8" stroke-width="1.5" stroke-dasharray="4 5"/>
  <text x="48" y="435" font-size="12" font-weight="700" fill="#C2354F" text-anchor="start" class="h">FUERA</text>
  <rect x="176" y="415" width="91" height="30" rx="15" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="221.5" y="434.5" font-size="13" font-weight="600" fill="#C2354F" text-anchor="middle" class="mono">ListView</text>
  <rect x="275" y="415" width="91" height="30" rx="15" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="320.5" y="434.5" font-size="13" font-weight="600" fill="#C2354F" text-anchor="middle" class="mono">GridView</text>
  <rect x="374" y="415" width="66" height="30" rx="15" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="407.0" y="434.5" font-size="13" font-weight="600" fill="#C2354F" text-anchor="middle" class="mono">Stack</text>
  <rect x="448" y="415" width="91" height="30" rx="15" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="493.5" y="434.5" font-size="13" font-weight="600" fill="#C2354F" text-anchor="middle" class="mono">ListTile</text>
  <rect x="547" y="415" width="139" height="30" rx="15" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="616.5" y="434.5" font-size="13" font-weight="600" fill="#C2354F" text-anchor="middle" class="mono">StatefulWidget</text>
  <rect x="694" y="415" width="99" height="30" rx="15" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="743.5" y="434.5" font-size="13" font-weight="600" fill="#C2354F" text-anchor="middle" class="mono">Navigator</text>
  <rect x="176" y="455" width="148" height="30" rx="15" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="250.0" y="474.5" font-size="13" font-weight="600" fill="#C2354F" text-anchor="middle">paquetes nuevos</text>
  <text x="48" y="528" font-size="13" font-weight="400" fill="#454C61" text-anchor="start" data-fit="860">Lo de abajo no está prohibido para siempre: entra a la paleta cuando lo veas en clase.</text>
</svg>
```

El archivo dice, para cada widget, qué propiedades se usan. Y para lo que queda fuera, con qué reemplazarlo:

```markdown
# Paleta de widgets

Solo estos. Entre paréntesis, las propiedades que se usan.

## Contenido

- `Text` (`style`, `maxLines`, `overflow`) con `TextStyle` (`fontSize`, `fontWeight`, `color`). Colores con `Colors.` o `Color(0xFF...)`.
- `Icon` (`size`, `color`).
- `Image.network` e `Image.asset` (`width`, `height`, `fit`). Imagen de ejemplo: `https://picsum.photos/400`.
- `CircleAvatar` (`radius`, `backgroundImage: NetworkImage(...)`).

## Botones

- `ElevatedButton`, `OutlinedButton`, `TextButton` (`onPressed`, `child`, `style` con `styleFrom`) e `IconButton` (`onPressed`, `icon`).

## Entrada

- `TextField`, solo su aspecto: `decoration: InputDecoration(labelText, hintText, prefixIcon, border)`, `obscureText`, `keyboardType`. Sin `controller`.

## Acomodar

- `Column` y `Row` (`mainAxisAlignment`, `crossAxisAlignment`, `mainAxisSize`, `spacing`, `children`).
- `SizedBox` para separar (`width`, `height`).
- `Expanded` (`flex`) y `Spacer`, solo dentro de `Row` o `Column`.
- `Padding` con `EdgeInsets.all`, `symmetric` u `only`.
- `Container` (`width`, `height`, `padding`, `margin`, `decoration: BoxDecoration(color, border, borderRadius)`). Para recortar al hijo, `clipBehavior: Clip.antiAlias`.
- `Card` (`elevation`, `color`, `shape: RoundedRectangleBorder(borderRadius, side)`), para una tarjeta.
- `Center`.
- `SingleChildScrollView` (`padding`, `scrollDirection`). Adentro no van `Expanded` ni `Spacer`.

## Estructura de la pantalla

- `Scaffold` (`appBar`, `body`, `backgroundColor`, `floatingActionButton`, `bottomNavigationBar`).
- `SafeArea`: el `body` siempre empieza con uno.
- `AppBar` (`title`, `leading`, `actions`, `centerTitle`, `backgroundColor`, `foregroundColor`).
- `BottomNavigationBar` (`items`, `currentIndex` fijo). Solo se ve: no responde al toque.
- `FloatingActionButton` (`onPressed`, `child`).

## Fuera de la paleta

No se usan todavía. En su lugar:

- `ListView`, `GridView`: una `Column` o una `Row` dentro de un `SingleChildScrollView`.
- `ListTile`: una `Row` dentro de un `Card` o de un `Container`.
- `Stack`, `Positioned`, `Wrap`, `Align`: reorganiza con `Column`, `Row` y `mainAxisAlignment`.
- `ClipRRect`: `Container` con `clipBehavior`.
- `GestureDetector`, `InkWell`: un botón de la paleta.
- `StatefulWidget`, `setState`, `Switch`, `Checkbox`: no hay estado.
- `Navigator`, `showDialog`, `SnackBar`: no hay navegación.
- `FutureBuilder`, `StreamBuilder` y cualquier paquete nuevo.
```

## assets/component.dart

La plantilla de un componente. Es `ContactCard`, del proyecto: campos `final`, constructor con parámetros por nombre y un `build` que solo usa la paleta.

```dart
import 'package:flutter/material.dart';

/// Card that summarizes a contact.
class ContactCard extends StatelessWidget {
  final String image;
  final String name;
  final String username;

  const ContactCard({
    super.key,
    required this.image,
    required this.name,
    required this.username,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 8,
      color: Colors.white,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(10),
        side: const BorderSide(color: Color(0xFFDCDDE6), width: 1.5),
      ),
      child: Padding(
        padding: EdgeInsets.all(8),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          spacing: 4,
          children: [
            CircleAvatar(radius: 28, backgroundImage: NetworkImage(image)),
            Text(
              name,
              style: const TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w600,
                color: Color(0xFF1B1B2A),
              ),
            ),
            Text(
              '@$username',
              style: const TextStyle(fontSize: 13, color: Color(0xFF5B5E72)),
            ),
          ],
        ),
      ),
    );
  }
}
```

## assets/screen.dart

La plantilla de una pantalla: `Scaffold`, `SafeArea`, scroll y una `Column` que acomoda componentes.

```dart
import 'package:flutter/material.dart';
import 'package:mi_app_1/components/profile_info.dart';
import 'package:mi_app_1/components/stats_row.dart';

/// Profile of a person.
class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Perfil')),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            spacing: 16,
            children: [
              ProfileInfo(
                image: 'https://picsum.photos/400',
                name: 'Mariana Valenzuela',
                username: 'marianav',
                role: 'Diseñadora de Producto',
                email: 'm.val@estudio.com',
                location: 'Cali, CO',
              ),
              StatsRow(posts: '128', followers: '2.4k', following: '310'),
            ],
          ),
        ),
      ),
    );
  }
}
```

Las dos plantillas viven en `.agents/`, no en `lib/`: no hacen parte de la app y `flutter analyze` no las revisa.

## Pide una pantalla

Cierra el agente y ábrelo de nuevo. Pídele una pantalla de la red profesional sin nombrar la skill:

```svg
<svg id="fpUso" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 590" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpUso-ttl fpUso-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpUso-ttl">Pedir una pantalla</title>
  <desc id="fpUso-dsc">Se le pide al agente la pantalla de mensajes. El agente lee los componentes que ya existen, carga la skill flutter-pantallas, lee la paleta y las plantillas, escribe la pantalla nueva y edita main.dart para registrarla.</desc>
  <defs>
    <style>
      #fpUso .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpUso .sub{fill:#79809A;font-size:13.5px}
      #fpUso .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpUso .tl{font-size:13px;fill:#C9CFDA;white-space:pre}
      #fpUso .pf{fill:#7F8AA3} #fpUso .cmd{fill:#FFFFFF;font-weight:600}
      #fpUso .dim{fill:#8A93A6} #fpUso .okk{fill:#6BCB77;font-weight:600}
      #fpUso .ring{fill:none;stroke:#F2C069;stroke-width:2}
      #fpUso .chipc{fill:#F2C069} #fpUso .chipt{fill:#1F2430;font-size:11.5px;font-weight:700}
      #fpUso .ct{fill:#161A26;font-size:14px;font-weight:700}
      #fpUso .cb{fill:#454C61;font-size:13px}
      #fpUso .foot{fill:#79809A;font-size:12px}
    </style>
  </defs>
  <rect width="960" height="590" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Pedir una pantalla</text>
  <text class="sub" x="48" y="80" data-fit="860">Una sesión real, recortada. Primero mira lo que ya hay, después carga la skill.</text>
  <rect x="48" y="112" width="864" height="320" rx="12" fill="#1F2430"/>
  <path d="M48,124 A12,12 0 0 1 60,112 H900 A12,12 0 0 1 912,124 V144 H48 Z" fill="#2A3040"/>
  <circle cx="68" cy="128" r="5" fill="#F14C4C"/><circle cx="84" cy="128" r="5" fill="#E5C07B"/><circle cx="100" cy="128" r="5" fill="#6BCB77"/>
  <text x="480" y="128" dy="0.35em" text-anchor="middle" fill="#9AA3B5" font-size="12">Terminal · C:\develop\mi_app_1</text>
  <text class="tl mono" font-size="13" x="72" y="174" data-fit="816">&gt; Crea la pantalla de mensajes con la lista de conversaciones</text>
  <text class="tl mono dim" font-size="13" x="72" y="226" data-fit="816">→ Read lib/components/chat_item.dart</text>
  <text class="tl mono" font-size="13" x="72" y="252" data-fit="816">→ Skill "flutter-pantallas"</text>
  <text class="tl mono dim" font-size="13" x="72" y="278" data-fit="816">→ Read .agents/skills/flutter-pantallas/references/widgets.md</text>
  <text class="tl mono dim" font-size="13" x="72" y="304" data-fit="816">→ Read .agents/skills/flutter-pantallas/assets/screen.dart</text>
  <text class="tl mono" font-size="13" x="72" y="330" data-fit="816">← Write lib/screens/messages_screen.dart</text>
  <text class="tl mono" font-size="13" x="72" y="356" data-fit="816">← Edit lib/main.dart</text>
  <text class="tl mono okk" font-size="13" x="72" y="408" data-fit="816">Listo: MessagesScreen reutiliza ChatItem. Sin errores en lib/.</text>
  <rect class="ring" x="68.0" y="210" width="288.8" height="22" rx="5"/>
  <circle class="chipc" cx="356.8" cy="211" r="8"/>
  <text class="chipt" x="356.8" y="211" dy="0.35em" text-anchor="middle" font-size="10.5">1</text>
  <rect class="ring" x="68.0" y="236" width="218.6" height="22" rx="5"/>
  <circle class="chipc" cx="286.6" cy="237" r="8"/>
  <text class="chipt" x="286.6" y="237" dy="0.35em" text-anchor="middle" font-size="10.5">2</text>
  <rect class="ring" x="68.0" y="314" width="320.0" height="22" rx="5"/>
  <circle class="chipc" cx="388.0" cy="315" r="8"/>
  <text class="chipt" x="388.0" y="315" dy="0.35em" text-anchor="middle" font-size="10.5">3</text>
  <g transform="translate(48.0,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">1</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">Miró lo que ya había</text>
    <text class="cb" x="16" y="60" data-fit="245">Encontró un componente</text>
    <text class="cb" x="16" y="79" data-fit="245">que servía.</text>
  </g>
  <g transform="translate(341.3,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">2</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">Cargó la skill</text>
    <text class="cb" x="16" y="60" data-fit="245">Y con ella, la paleta</text>
    <text class="cb" x="16" y="79" data-fit="245">y las plantillas.</text>
  </g>
  <g transform="translate(634.7,456)">
    <rect width="277.3" height="102" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <circle class="chipc" cx="26" cy="26" r="10"/>
    <text class="chipt" x="26" y="26" dy="0.35em" text-anchor="middle">3</text>
    <text class="ct" x="46" y="26" dy="0.35em" data-fit="215">Un solo archivo nuevo</text>
    <text class="cb" x="16" y="60" data-fit="245">La pantalla. Ningún</text>
    <text class="cb" x="16" y="79" data-fit="245">componente repetido.</text>
  </g>
</svg>
```

Esto fue lo que hizo un modelo gratuito con ese pedido:

```svg
<svg id="fpComponentes" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpComponentes-ttl fpComponentes-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpComponentes-ttl">Un componente, cinco usos</title>
  <desc id="fpComponentes-dsc">Un celular con la pantalla Mensajes: cinco filas de conversación, cada una con avatar, nombre, último mensaje y hora. Las cinco salen del mismo componente, ChatItem, que vive en lib/components/chat_item.dart y recibe cuatro datos: image, name, message y time. La pantalla solo las acomoda en una Column.</desc>
  <defs>
    <style>
      #fpComponentes .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpComponentes .sub{fill:#79809A;font-size:13.5px}
      #fpComponentes .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #fpComponentes .nt{font-size:15px;font-weight:700;fill:#161A26}
      #fpComponentes .nb{fill:#454C61;font-size:13px}
      #fpComponentes .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fpComponentes .foot{fill:#79809A;font-size:12px}
      #fpComponentes .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpComponentes .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fpComponentes-arrow)}
    </style>
    <marker id="fpComponentes-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="560" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Un componente, cinco usos</text>
  <text class="sub" x="48" y="80" data-fit="860">La pantalla de mensajes que armó el agente: no escribió nada nuevo para las filas, reutilizó ChatItem.</text>
  <clipPath id="fpComponentes-a"><rect width="220" height="370" rx="20"/></clipPath><rect x="89" y="125" width="234" height="384" rx="27" fill="#1F2430"/><g transform="translate(96,132)"><g clip-path="url(#fpComponentes-a)"><rect width="220" height="370" rx="20" fill="#FFFFFF"/><rect width="220" height="46" fill="#F1ECF8"/><text x="16" y="29" font-size="15" font-weight="500" fill="#161A26" text-anchor="start">Mensajes</text><circle cx="28" cy="84" r="14" fill="#C9A6EE"/><text x="50" y="80" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start">Javier Montes</text><text x="50" y="95" font-size="10" font-weight="400" fill="#556074" text-anchor="start">Perfecto, quedamos mañana…</text><text x="208" y="80" font-size="9.5" font-weight="400" fill="#556074" text-anchor="end">10:24</text><rect x="6" y="62" width="208" height="46" rx="8" fill="#0F8478" fill-opacity=".08" stroke="#0F8478" stroke-width="2"/><circle cx="28" cy="142" r="14" fill="#C9A6EE"/><text x="50" y="138" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start">Mariana Valenzuela</text><text x="50" y="153" font-size="10" font-weight="400" fill="#556074" text-anchor="start">Gracias por los comentarios…</text><text x="208" y="138" font-size="9.5" font-weight="400" fill="#556074" text-anchor="end">9:05</text><rect x="6" y="120" width="208" height="46" rx="8" fill="#0F8478" fill-opacity=".08" stroke="#0F8478" stroke-width="2"/><circle cx="28" cy="200" r="14" fill="#C9A6EE"/><text x="50" y="196" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start">Ana Torres</text><text x="50" y="211" font-size="10" font-weight="400" fill="#556074" text-anchor="start">¿Pudiste revisar el docu…</text><text x="208" y="196" font-size="9.5" font-weight="400" fill="#556074" text-anchor="end">Ayer</text><rect x="6" y="178" width="208" height="46" rx="8" fill="#0F8478" fill-opacity=".08" stroke="#0F8478" stroke-width="2"/><circle cx="28" cy="258" r="14" fill="#C9A6EE"/><text x="50" y="254" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start">Carlos Restrepo</text><text x="50" y="269" font-size="10" font-weight="400" fill="#556074" text-anchor="start">Listo, reviso el presupu…</text><text x="208" y="254" font-size="9.5" font-weight="400" fill="#556074" text-anchor="end">Mar</text><rect x="6" y="236" width="208" height="46" rx="8" fill="#0F8478" fill-opacity=".08" stroke="#0F8478" stroke-width="2"/><circle cx="28" cy="316" r="14" fill="#C9A6EE"/><text x="50" y="312" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start">Lucía Fernández</text><text x="50" y="327" font-size="10" font-weight="400" fill="#556074" text-anchor="start">¡Felicitaciones por el…</text><text x="208" y="312" font-size="9.5" font-weight="400" fill="#556074" text-anchor="end">Lun</text><rect x="6" y="294" width="208" height="46" rx="8" fill="#0F8478" fill-opacity=".08" stroke="#0F8478" stroke-width="2"/></g></g>
  <path d="M324,217 C420,217 440,300 512,300" fill="none" stroke="#86D3CA" stroke-width="1.75"/>
  <path d="M324,275 C420,275 440,300 512,300" fill="none" stroke="#86D3CA" stroke-width="1.75"/>
  <path d="M324,333 C420,333 440,300 512,300" fill="none" stroke="#86D3CA" stroke-width="1.75"/>
  <path d="M324,391 C420,391 440,300 512,300" fill="none" stroke="#86D3CA" stroke-width="1.75"/>
  <path d="M324,449 C420,449 440,300 512,300" fill="none" stroke="#86D3CA" stroke-width="1.75"/>
  <rect x="520" y="172" width="392" height="256" rx="12" fill="#E3F6F3" stroke="#0F8478" stroke-width="2.5"/>
  <text x="544" y="208" font-size="18" font-weight="700" fill="#0F8478" text-anchor="start" class="mono">ChatItem</text>
  <text x="544" y="230" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" class="mono" data-fit="340">lib/components/chat_item.dart</text>
  <text x="544" y="268" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="344">Se escribe una vez. Lo que cambia en cada fila</text>
  <text x="544" y="288" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="344">llega por el constructor:</text>
  <rect x="544" y="308" width="80" height="30" rx="15" fill="#FFFFFF" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="584" y="327.5" font-size="12.5" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">image</text>
  <rect x="632" y="308" width="80" height="30" rx="15" fill="#FFFFFF" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="672" y="327.5" font-size="12.5" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">name</text>
  <rect x="720" y="308" width="80" height="30" rx="15" fill="#FFFFFF" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="760" y="327.5" font-size="12.5" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">message</text>
  <rect x="808" y="308" width="80" height="30" rx="15" fill="#FFFFFF" stroke="#86D3CA" stroke-width="1.5"/>
  <text x="848" y="327.5" font-size="12.5" font-weight="600" fill="#0F8478" text-anchor="middle" class="mono">time</text>
  <text x="544" y="376" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="344">La pantalla no dibuja filas: las acomoda</text>
  <text x="544" y="396" font-size="13.5" font-weight="400" fill="#161A26" text-anchor="start" data-fit="344">en una Column y les pasa sus datos.</text>
</svg>
```

No usó `ListView`: puso una `Column` dentro de un `SingleChildScrollView`, como dice la paleta. Y no creó un componente nuevo, porque `ChatItem` ya servía.

## Audita lo que hizo

Antes de aceptar, revisa el resultado contra tres cosas:

- **La paleta.** ¿Hay algún widget que no conozcas? Si lo hay, pregúntale por qué lo usó y pídele que lo cambie.
- **Los componentes.** ¿Reutilizó los que ya existían? ¿Lo que se repite quedó en un componente, en su propio archivo? ¿Cada componente recibe sus datos por el constructor?
- **El `AGENTS.md` y el modelo.** ¿La pantalla muestra solo datos de `docs/modelo.md`? ¿Tocó algún archivo fuera de `lib/`?

Ejecuta la app con `flutter run -d chrome` y cambia `initialRoute` para ver la pantalla nueva: los botones todavía no navegan.

## La paleta crece contigo

Esta skill también es un documento vivo. Cuando veas un widget nuevo en clase, lo pasas de *Fuera de la paleta* a su grupo. En la sesión 6 entra `StatefulWidget`; en la 8, la navegación. Así el agente nunca escribe algo que tú no puedas revisar.
