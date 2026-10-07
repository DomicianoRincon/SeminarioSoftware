# Taller · Pantallas

<!-- tags: taller de pantallas, pantalla de perfil, separar la pantalla en secciones, SectionHeader, fila deslizable de contactos, RenderFlex overflowed, extraer un widget a su archivo, StatsRow se desborda en pantalla angosta, crossAxisAlignment stretch, registrar una ruta -->

```svg
<svg id="tpPantallas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 882" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tpPantallas-ttl tpPantallas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tpPantallas-ttl">La pantalla del taller</title>
  <desc id="tpPantallas-dsc">Un celular con la pantalla de perfil, dividida en cuatro bloques numerados de arriba hacia abajo. Uno, la información del perfil y sus tres indicadores. Dos, los botones Seguir y Enviar mensaje. Tres, los contactos sugeridos. Cuatro, las últimas conversaciones. Debajo, el nombre de la clase, ProfileScreen, y su ruta, /profile.</desc>
  <defs>
    <style>
      #tpPantallas .title{fill:#161A26;font-size:22px;font-weight:700}
      #tpPantallas .sub{fill:#79809A;font-size:13.5px}
      #tpPantallas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tpPantallas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tpPantallas .nb{fill:#454C61;font-size:13px}
      #tpPantallas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tpPantallas .foot{fill:#79809A;font-size:12px}
      #tpPantallas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tpPantallas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tpPantallas-arrow)}
    </style>
    <marker id="tpPantallas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="882" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">La pantalla del taller</text>
  <text class="sub" x="48" y="80" data-fit="860">Se arma en cuatro bloques, de arriba hacia abajo, con los componentes de la sesión 2.</text>
  <clipPath id="tpPantallas-scr"><rect width="340" height="676" rx="28"/></clipPath>
  <rect x="300" y="114" width="360" height="696" rx="38" fill="#1F2430"/>
  <g transform="translate(310,124)"><g clip-path="url(#tpPantallas-scr)">
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
  <path d="M672,186 H682 V410 H672" fill="none" stroke="#4453C9" stroke-width="1.75"/>
  <circle cx="712" cy="298" r="14" fill="#4453C9"/>
  <text dy="0.35em" x="712" y="298" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">1</text>
  <text dy="0.35em" x="736" y="298" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="200">La información del perfil</text>
  <path d="M672,422 H682 V520 H672" fill="none" stroke="#4453C9" stroke-width="1.75"/>
  <circle cx="712" cy="471" r="14" fill="#4453C9"/>
  <text dy="0.35em" x="712" y="471" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">2</text>
  <text dy="0.35em" x="736" y="471" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="200">Los botones</text>
  <path d="M672,532 H682 V644 H672" fill="none" stroke="#4453C9" stroke-width="1.75"/>
  <circle cx="712" cy="588" r="14" fill="#4453C9"/>
  <text dy="0.35em" x="712" y="588" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">3</text>
  <text dy="0.35em" x="736" y="588" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="200">Contactos sugeridos</text>
  <path d="M672,656 H682 V788 H672" fill="none" stroke="#4453C9" stroke-width="1.75"/>
  <circle cx="712" cy="722" r="14" fill="#4453C9"/>
  <text dy="0.35em" x="712" y="722" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">4</text>
  <text dy="0.35em" x="736" y="722" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="200">Últimas conversaciones</text>
  <text x="480" y="844" font-size="15" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono">ProfileScreen</text>
  <text x="480" y="864" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" class="mono">'/profile'</text>
</svg>
```

En este taller armas **la pantalla de perfil** con los componentes de la sesión anterior. Va en dos tiempos: primero la armas completa dentro de `ProfileScreen`, bloque por bloque, y después sacas cada bloque a su propio archivo.

Necesitas tus siete componentes terminados en `lib/components/`. Si te falta alguno, termínalo primero con el *Taller · Componentes*.

## Antes de empezar

**Archivo:** `lib/screens/profile_screen.dart` · **Clase:** `ProfileScreen` · **Ruta:** `'/profile'`

La pantalla ya existe y ya abre la app, desde la lección *Scaffold*:

```dart
initialRoute: '/profile',
routes: {
  '/profile': (context) => const ProfileScreen(),
},
```

Tiene el esqueleto de la lección anterior: `Scaffold`, `SafeArea`, `SingleChildScrollView` y una `Column`. Los cuatro bloques son hijos de esa `Column`, de arriba hacia abajo. Ejecuta después de cada uno.

Entre un bloque y el siguiente va un `SizedBox(height: 24)`. Entre las cosas de un mismo bloque, `8` o `12`. El borde de la pantalla lo pone el `padding` del scroll.

Los botones siguen con su `print`. Pasar de una pantalla a otra al tocarlos es la sesión 8.

### Un componente que te entregamos

Los bloques 3 y 4 empiezan con un título y un enlace a la derecha. Ese encabezado es un componente, y este ya viene hecho. Crea `lib/components/section_header.dart` y copia:

```dart
import 'package:flutter/material.dart';

/// Title of a section, with a link on the right.
class SectionHeader extends StatelessWidget {
  final String title;
  final String actionLabel;

  const SectionHeader({
    super.key,
    required this.title,
    required this.actionLabel,
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Expanded(
          child: Text(
            title,
            style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
          ),
        ),
        TextButton(
          onPressed: () {
            print(actionLabel);
          },
          child: Text(actionLabel),
        ),
      ],
    );
  }
}
```

Léelo antes de usarlo. Lo único que necesitas saber de un componente que no escribiste es qué recibe: `title` y `actionLabel`.

## 1. La información del perfil

```svg
<svg id="tpBloque1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 506.0" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tpBloque1-ttl tpBloque1-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tpBloque1-ttl">Bloque 1 · La información del perfil</title>
  <desc id="tpBloque1-dsc">La parte de arriba de la pantalla de perfil. Primero ProfileInfo, con la foto, el nombre, el usuario, el correo y la ciudad. Debajo StatsRow, con tres indicadores: publicaciones, seguidores y seguidos.</desc>
  <defs>
    <style>
      #tpBloque1 .title{fill:#161A26;font-size:22px;font-weight:700}
      #tpBloque1 .sub{fill:#79809A;font-size:13.5px}
      #tpBloque1 .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tpBloque1 .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tpBloque1 .nb{fill:#454C61;font-size:13px}
      #tpBloque1 .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tpBloque1 .foot{fill:#79809A;font-size:12px}
      #tpBloque1 .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tpBloque1 .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tpBloque1-arrow)}
    </style>
    <marker id="tpBloque1-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="506.0" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Bloque 1 · La información del perfil</text>
  <text class="sub" x="48" y="80" data-fit="860">Dos componentes, uno debajo del otro. Los dos quedan centrados.</text>
  <clipPath id="tpBloque1-crop"><rect x="48" y="112" width="510" height="354" rx="12"/></clipPath>
  <g clip-path="url(#tpBloque1-crop)"><svg x="48" y="112" width="510" height="354" viewBox="310 180 340 236">
  <clipPath id="tpBloque1-scr"><rect width="340" height="676" rx="0"/></clipPath>
  <rect x="300" y="114" width="360" height="696" rx="38" fill="#1F2430"/>
  <g transform="translate(310,124)"><g clip-path="url(#tpBloque1-scr)">
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
  </svg></g>
  <rect x="48" y="112" width="510" height="354" rx="12" fill="none" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect x="54" y="118" width="498" height="225" rx="12" fill="#7439B8" fill-opacity=".08" stroke="#7439B8" stroke-width="2"/>
  <path d="M552,230.5 H596" stroke="#7439B8" stroke-width="1.75"/><circle cx="596" cy="230.5" r="3.5" fill="#7439B8"/>
  <text x="612" y="227.5" font-size="15" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="300">ProfileInfo</text>
  <text x="612" y="247.5" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="300">Foto, nombre, usuario, correo y ciudad.</text>
  <rect x="54" y="355" width="498" height="108" rx="12" fill="#4453C9" fill-opacity=".08" stroke="#4453C9" stroke-width="2"/>
  <path d="M552,409 H596" stroke="#4453C9" stroke-width="1.75"/><circle cx="596" cy="409" r="3.5" fill="#4453C9"/>
  <text x="612" y="406" font-size="15" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="300">StatsRow</text>
  <text x="612" y="426" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="300">Tres StatCard en una fila.</text>
</svg>
```

Este bloque ya lo tienes de la lección anterior: `ProfileInfo` y, debajo, `StatsRow`.

Falta probarlo en una pantalla angosta. Reduce la ventana de Chrome hasta que mida lo que un teléfono pequeño. Si aparece la franja amarilla y negra en `StatsRow`, las tres tarjetas ya no caben. El arreglo va en el componente, no en la pantalla: en `stats_row.dart`, envuelve cada `StatCard` en un `Expanded` y sepáralas con `SizedBox(width: 8)`.

En el diseño del [proyecto de Figma](https://www.figma.com/design/cn5cLhBPnuJC4tvewTtVmq/Aplicaciones-M%C3%B3viles?node-id=2014-421&t=oULdr2bxOVE437ux-1) este bloque va dentro de una tarjeta blanca con esquinas redondeadas. Si te alcanza el tiempo, hazla: es un `Container` con `padding` y `decoration` que envuelve los dos componentes, sobre un `Scaffold` con `backgroundColor` gris claro.

## 2. Los botones

```svg
<svg id="tpBloque2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 317.0" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tpBloque2-ttl tpBloque2-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tpBloque2-ttl">Bloque 2 · Los botones</title>
  <desc id="tpBloque2-dsc">Dos botones. Arriba PrimaryButton, azul, con el texto Seguir. Debajo SecondaryButton, con borde, con el texto Enviar mensaje.</desc>
  <defs>
    <style>
      #tpBloque2 .title{fill:#161A26;font-size:22px;font-weight:700}
      #tpBloque2 .sub{fill:#79809A;font-size:13.5px}
      #tpBloque2 .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tpBloque2 .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tpBloque2 .nb{fill:#454C61;font-size:13px}
      #tpBloque2 .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tpBloque2 .foot{fill:#79809A;font-size:12px}
      #tpBloque2 .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tpBloque2 .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tpBloque2-arrow)}
    </style>
    <marker id="tpBloque2-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="317.0" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Bloque 2 · Los botones</text>
  <text class="sub" x="48" y="80" data-fit="860">Dos botones a todo el ancho, uno debajo del otro.</text>
  <clipPath id="tpBloque2-crop"><rect x="48" y="112" width="510" height="165" rx="12"/></clipPath>
  <g clip-path="url(#tpBloque2-crop)"><svg x="48" y="112" width="510" height="165" viewBox="310 416 340 110">
  <clipPath id="tpBloque2-scr"><rect width="340" height="676" rx="0"/></clipPath>
  <rect x="300" y="114" width="360" height="696" rx="38" fill="#1F2430"/>
  <g transform="translate(310,124)"><g clip-path="url(#tpBloque2-scr)">
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
  </svg></g>
  <rect x="48" y="112" width="510" height="165" rx="12" fill="none" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect x="54" y="118" width="498" height="75" rx="12" fill="#4453C9" fill-opacity=".08" stroke="#4453C9" stroke-width="2"/>
  <path d="M552,155.5 H596" stroke="#4453C9" stroke-width="1.75"/><circle cx="596" cy="155.5" r="3.5" fill="#4453C9"/>
  <text x="612" y="152.5" font-size="15" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="300">PrimaryButton</text>
  <text x="612" y="172.5" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="300">Seguir.</text>
  <rect x="54" y="196" width="498" height="75" rx="12" fill="#0F8478" fill-opacity=".08" stroke="#0F8478" stroke-width="2"/>
  <path d="M552,233.5 H596" stroke="#0F8478" stroke-width="1.75"/><circle cx="596" cy="233.5" r="3.5" fill="#0F8478"/>
  <text x="612" y="230.5" font-size="15" font-weight="700" fill="#0F8478" text-anchor="start" class="mono" data-fit="300">SecondaryButton</text>
  <text x="612" y="250.5" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="300">Enviar mensaje.</text>
</svg>
```

`PrimaryButton` con *Seguir* y, debajo, `SecondaryButton` con *Enviar mensaje*.

Los dos van de borde a borde. Para que cada hijo ocupe todo el ancho, pon `crossAxisAlignment: CrossAxisAlignment.stretch` en la `Column` de la pantalla. `ProfileInfo` sigue viéndose centrado, porque centra su contenido por dentro.

## 3. Contactos sugeridos

```svg
<svg id="tpBloque3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 338.0" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tpBloque3-ttl tpBloque3-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tpBloque3-ttl">Bloque 3 · Contactos sugeridos</title>
  <desc id="tpBloque3-dsc">El título Contactos sugeridos, hecho con SectionHeader. Debajo, una fila de ContactCard con la foto, el nombre y el usuario de cada contacto. La última tarjeta queda cortada: la fila sigue hacia la derecha.</desc>
  <defs>
    <style>
      #tpBloque3 .title{fill:#161A26;font-size:22px;font-weight:700}
      #tpBloque3 .sub{fill:#79809A;font-size:13.5px}
      #tpBloque3 .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tpBloque3 .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tpBloque3 .nb{fill:#454C61;font-size:13px}
      #tpBloque3 .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tpBloque3 .foot{fill:#79809A;font-size:12px}
      #tpBloque3 .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tpBloque3 .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tpBloque3-arrow)}
    </style>
    <marker id="tpBloque3-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="338.0" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Bloque 3 · Contactos sugeridos</text>
  <text class="sub" x="48" y="80" data-fit="860">Un título y, debajo, una fila de tarjetas que se desliza de lado.</text>
  <clipPath id="tpBloque3-crop"><rect x="48" y="112" width="510" height="186" rx="12"/></clipPath>
  <g clip-path="url(#tpBloque3-crop)"><svg x="48" y="112" width="510" height="186" viewBox="310 526 340 124">
  <clipPath id="tpBloque3-scr"><rect width="340" height="676" rx="0"/></clipPath>
  <rect x="300" y="114" width="360" height="696" rx="38" fill="#1F2430"/>
  <g transform="translate(310,124)"><g clip-path="url(#tpBloque3-scr)">
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
  </svg></g>
  <rect x="48" y="112" width="510" height="186" rx="12" fill="none" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect x="54" y="118" width="498" height="39" rx="12" fill="#A96C05" fill-opacity=".08" stroke="#A96C05" stroke-width="2"/>
  <path d="M552,137.5 H596" stroke="#A96C05" stroke-width="1.75"/><circle cx="596" cy="137.5" r="3.5" fill="#A96C05"/>
  <text x="612" y="134.5" font-size="15" font-weight="700" fill="#A96C05" text-anchor="start" class="mono" data-fit="300">SectionHeader</text>
  <text x="612" y="154.5" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="300">El título de la sección.</text>
  <rect x="54" y="160" width="498" height="132" rx="12" fill="#0F8478" fill-opacity=".08" stroke="#0F8478" stroke-width="2"/>
  <path d="M552,226 H596" stroke="#0F8478" stroke-width="1.75"/><circle cx="596" cy="226" r="3.5" fill="#0F8478"/>
  <text x="612" y="223" font-size="15" font-weight="700" fill="#0F8478" text-anchor="start" class="mono" data-fit="300">ContactCard</text>
  <text x="612" y="243" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="300">Seis o más, en una fila que se desliza.</text>
</svg>
```

`SectionHeader` con *Contactos sugeridos* y, debajo, una fila con al menos seis `ContactCard`.

Seis tarjetas no caben a lo ancho, así que la fila se desliza de lado. Es un `SingleChildScrollView` con `scrollDirection: Axis.horizontal` y una `Row` adentro, con un `SizedBox(width: 12)` entre tarjetas. Va como un hijo más de la `Column`.

Si la última tarjeta que se ve queda cortada, está bien: así sabe la persona que hay más.

## 4. Últimas conversaciones

```svg
<svg id="tpBloque4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 368.0" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tpBloque4-ttl tpBloque4-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tpBloque4-ttl">Bloque 4 · Últimas conversaciones</title>
  <desc id="tpBloque4-dsc">El título Últimas conversaciones, hecho con SectionHeader. Debajo, dos ChatItem con la foto, el nombre, el último mensaje y la hora.</desc>
  <defs>
    <style>
      #tpBloque4 .title{fill:#161A26;font-size:22px;font-weight:700}
      #tpBloque4 .sub{fill:#79809A;font-size:13.5px}
      #tpBloque4 .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tpBloque4 .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tpBloque4 .nb{fill:#454C61;font-size:13px}
      #tpBloque4 .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tpBloque4 .foot{fill:#79809A;font-size:12px}
      #tpBloque4 .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tpBloque4 .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tpBloque4-arrow)}
    </style>
    <marker id="tpBloque4-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="368.0" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Bloque 4 · Últimas conversaciones</text>
  <text class="sub" x="48" y="80" data-fit="860">Un título y, debajo, una conversación por renglón.</text>
  <clipPath id="tpBloque4-crop"><rect x="48" y="112" width="510" height="216" rx="12"/></clipPath>
  <g clip-path="url(#tpBloque4-crop)"><svg x="48" y="112" width="510" height="216" viewBox="310 650 340 144">
  <clipPath id="tpBloque4-scr"><rect width="340" height="676" rx="0"/></clipPath>
  <rect x="300" y="114" width="360" height="696" rx="38" fill="#1F2430"/>
  <g transform="translate(310,124)"><g clip-path="url(#tpBloque4-scr)">
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
  </svg></g>
  <rect x="48" y="112" width="510" height="216" rx="12" fill="none" stroke="#D9DEE8" stroke-width="1.5"/>
  <rect x="54" y="118" width="498" height="39" rx="12" fill="#A96C05" fill-opacity=".08" stroke="#A96C05" stroke-width="2"/>
  <path d="M552,137.5 H596" stroke="#A96C05" stroke-width="1.75"/><circle cx="596" cy="137.5" r="3.5" fill="#A96C05"/>
  <text x="612" y="134.5" font-size="15" font-weight="700" fill="#A96C05" text-anchor="start" class="mono" data-fit="300">SectionHeader</text>
  <text x="612" y="154.5" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="300">El título de la sección.</text>
  <rect x="54" y="160" width="498" height="162" rx="12" fill="#C2354F" fill-opacity=".08" stroke="#C2354F" stroke-width="2"/>
  <path d="M552,241 H596" stroke="#C2354F" stroke-width="1.75"/><circle cx="596" cy="241" r="3.5" fill="#C2354F"/>
  <text x="612" y="238" font-size="15" font-weight="700" fill="#C2354F" text-anchor="start" class="mono" data-fit="300">ChatItem</text>
  <text x="612" y="258" font-size="13" font-weight="400" fill="#556074" text-anchor="start" data-fit="300">Cuatro o más, uno debajo del otro.</text>
</svg>
```

`SectionHeader` con *Últimas conversaciones* y, debajo, al menos cuatro `ChatItem`.

Los `ChatItem` van uno debajo del otro, directamente en la `Column` de la pantalla. No necesitan un scroll propio: ya se desliza la pantalla entera.

Con este bloque la pantalla ya no cabe en la ventana. Deslízala hasta el final y revisa que el último `ChatItem` se vea completo.

## Sepáralo en secciones

La pantalla funciona, pero su `build` ya pasa de cien líneas y los cuatro bloques están pegados uno tras otro. Cada bloque tiene nombre y límites claros, así que puede ser un widget.

Una **sección** es un componente que agrupa otros componentes. Va en `lib/components/` y su clase termina en `Section`. Esta es la del primer bloque, `lib/components/profile_summary_section.dart`:

```dart
import 'package:flutter/material.dart';
import 'package:miapp1/components/profile_info.dart';
import 'package:miapp1/components/stats_row.dart';

/// Who the person is and their three numbers.
class ProfileSummarySection extends StatelessWidget {
  const ProfileSummarySection({super.key});

  @override
  Widget build(BuildContext context) {
    return const Column(
      children: [
        ProfileInfo(
          imageUrl: 'https://picsum.photos/400',
          name: 'Mariana Valenzuela',
          username: '@marianav',
          role: 'Diseñadora de Producto',
          bio: 'Creando experiencias digitales enfocadas en el usuario.',
          email: 'm.val@estudio.com',
          location: 'Madrid, ES',
        ),
        SizedBox(height: 24),
        StatsRow(posts: '128', followers: '2.4k', following: '310'),
      ],
    );
  }
}
```

No escribiste nada nuevo: cortaste el bloque de la pantalla y lo pegaste en el `build` de la sección. Como son varios widgets, van dentro de una `Column` propia. Los `import` de esos componentes se mudan con ellos.

Haz lo mismo con los otros tres:

- `ProfileActionsSection`, en `profile_actions_section.dart`: los dos botones.
- `SuggestedContactsSection`, en `suggested_contacts_section.dart`: el encabezado y la fila de contactos.
- `RecentChatsSection`, en `recent_chats_section.dart`: el encabezado y las conversaciones.

Saca una sección, ejecuta, y sigue con la otra. Si la pantalla se ve igual que antes, lo hiciste bien.

Al terminar, la `Column` de `ProfileScreen` queda así:

```dart
child: Column(
  crossAxisAlignment: CrossAxisAlignment.stretch,
  children: [
    ProfileSummarySection(),
    SizedBox(height: 24),
    ProfileActionsSection(),
    SizedBox(height: 24),
    SuggestedContactsSection(),
    SizedBox(height: 24),
    RecentChatsSection(),
  ],
),
```

Ahora la pantalla dice qué bloques tiene y en qué orden, y nada más. Para cambiar los contactos sugeridos abres un archivo de treinta líneas, no uno de ciento veinte.

Por ahora cada sección lleva sus datos escritos adentro. En la sesión 7 los va a recibir por el constructor, como cualquier componente.

## Qué debes tener al terminar

```svg
<svg id="tpCarpetas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 604" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tpCarpetas-ttl tpCarpetas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tpCarpetas-ttl">Tu proyecto al terminar el taller</title>
  <desc id="tpCarpetas-dsc">La carpeta lib con main.dart y dos subcarpetas. En components están los siete componentes de la sesión 2 y cinco archivos nuevos: section_header.dart y las cuatro secciones, profile_summary_section.dart, profile_actions_section.dart, suggested_contacts_section.dart y recent_chats_section.dart. En screens están home_screen.dart y la pantalla nueva, profile_screen.dart.</desc>
  <defs>
    <style>
      #tpCarpetas .title{fill:#161A26;font-size:22px;font-weight:700}
      #tpCarpetas .sub{fill:#79809A;font-size:13.5px}
      #tpCarpetas .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tpCarpetas .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tpCarpetas .nb{fill:#454C61;font-size:13px}
      #tpCarpetas .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tpCarpetas .foot{fill:#79809A;font-size:12px}
      #tpCarpetas .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tpCarpetas .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tpCarpetas-arrow)}
    </style>
    <marker id="tpCarpetas-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="604" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Tu proyecto al terminar el taller</text>
  <text class="sub" x="48" y="80" data-fit="860">Los componentes ya los tienes. Hoy agregas uno que te entregamos, cuatro secciones y una pantalla.</text>
  <path d="M64,132 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/><text x="98" y="145" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">lib/</text>
  <path d="M104,167 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="130" y="181" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">main.dart</text>
  <path d="M104,210 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/><text x="138" y="223" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">components/</text>
  <path d="M144,243 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="257" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">chat_item.dart</text>
  <path d="M144,271 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="285" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">contact_card.dart</text>
  <path d="M144,299 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="313" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">primary_button.dart</text>
  <path d="M144,327 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="341" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">profile_actions_section.dart</text><rect x="444" y="326" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="472" y="341" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M144,355 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="369" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">profile_info.dart</text>
  <path d="M144,383 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="397" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">profile_summary_section.dart</text><rect x="444" y="382" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="472" y="397" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M144,411 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="425" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">recent_chats_section.dart</text><rect x="444" y="410" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="472" y="425" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M144,439 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="453" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">secondary_button.dart</text>
  <path d="M144,467 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="481" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">section_header.dart</text><rect x="444" y="466" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="472" y="481" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M144,495 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="509" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">stat_card.dart</text>
  <path d="M144,523 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="537" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">stats_row.dart</text>
  <path d="M144,551 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="565" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">suggested_contacts_section.dart</text><rect x="444" y="550" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="472" y="565" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M536,210 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/><text x="570" y="223" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">screens/</text>
  <path d="M576,243 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="602" y="257" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">home_screen.dart</text>
  <path d="M576,271 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/><text x="602" y="285" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">profile_screen.dart</text><rect x="808" y="270" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="836" y="285" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M76,156 V218 H96 M76,176 H96" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M116,234 V560 M548,234 V280" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M76,198 H508 V218 H528" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
</svg>
```

- `ProfileScreen` registrada en `routes`, y se ve completa al poner `'/profile'` en `initialRoute`.
- Las cuatro secciones en `lib/components/`, cada una en su archivo.
- `profile_screen.dart` solo importa las cuatro secciones: ya no usa `ProfileInfo`, `ChatItem` ni los demás directamente.
- Todos los `import` de archivos propios empiezan por `package:miapp1/`.
- La pantalla aguanta una ventana angosta y una baja, sin franjas.
- El proyecto sin errores en el editor.

Lo que no alcances en clase se termina por fuera. Esta pantalla es la base del prototipo de tu equipo.
