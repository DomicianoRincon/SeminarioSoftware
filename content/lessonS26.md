# Taller · Pantallas

<!-- tags: taller de pantallas, pantalla de perfil, pantalla de inicio de sesión, SectionHeader, fila deslizable de contactos, pantalla sin AppBar, RenderFlex overflowed, cambiar initialRoute, registrar una ruta, StatsRow se desborda en pantalla angosta -->

```svg
<svg id="tpPantallas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 882" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tpPantallas-ttl tpPantallas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tpPantallas-ttl">Las dos pantallas del taller</title>
  <desc id="tpPantallas-dsc">Dos celulares. El de la izquierda es la pantalla de perfil: barra con el título Perfil, la información de la persona, tres indicadores, dos botones, una fila de contactos sugeridos y las últimas conversaciones. El de la derecha es la pantalla de inicio de sesión, sin barra: un logo, el título Bienvenido, los campos de correo y contraseña, un botón azul Iniciar sesión, un botón con borde Crear cuenta y un enlace.</desc>
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
  <text class="title" x="48" y="56">Las dos pantallas del taller</text>
  <text class="sub" x="48" y="80" data-fit="860">Las dos se arman con los componentes de la sesión 2. Una lleva barra y se desliza; la otra no tiene barra.</text>
  <g transform="translate(-210,0)">
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
  </g>
  <clipPath id="tpPantallas-lg"><rect width="340" height="676" rx="28"/></clipPath>
  <rect x="510" y="114" width="360" height="696" rx="38" fill="#1F2430"/>
  <g transform="translate(520,124)"><g clip-path="url(#tpPantallas-lg)">
    <rect width="340" height="676" fill="#FFFFFF"/>
    <circle cx="170" cy="150" r="40" fill="#E3F2FD" stroke="#2196F3" stroke-width="2"/>
    <path d="M154,150 l11,11 l22,-24" fill="none" stroke="#1976D2" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="170" y="232" font-size="24" font-weight="700" fill="#161A26" text-anchor="middle">Bienvenido</text>
    <text x="170" y="258" font-size="13.5" font-weight="400" fill="#556074" text-anchor="middle">Inicia sesión para continuar</text>
    <rect x="24" y="300" width="292" height="52" rx="6" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5"/>
    <rect x="36" y="292" width="54" height="16" fill="#FFFFFF"/>
    <text x="42" y="304" font-size="12" font-weight="600" fill="#556074" text-anchor="start">Correo</text><text x="42" y="332" font-size="14" font-weight="400" fill="#A0A8B8" text-anchor="start">nombre@icesi.edu.co</text>
    <rect x="24" y="372" width="292" height="52" rx="6" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5"/>
    <rect x="36" y="364" width="82" height="16" fill="#FFFFFF"/>
    <text x="42" y="376" font-size="12" font-weight="600" fill="#556074" text-anchor="start">Contraseña</text><text x="42" y="404" font-size="14" font-weight="400" fill="#A0A8B8" text-anchor="start">••••••••</text>
    <rect x="24" y="456" width="292" height="44" rx="22" fill="#2196F3"/>
    <path d="M108,478 h14 M117,473 l5,5 l-5,5 M124,468 h6 v20 h-6" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="138" y="483" font-size="14.5" font-weight="600" fill="#FFFFFF" text-anchor="start">Iniciar sesión</text>
    <rect x="24" y="512" width="292" height="44" rx="22" fill="#FFFFFF" stroke="#2196F3" stroke-width="1.75"/>
    <g transform="translate(124,534)"><circle cx="-2" cy="-4" r="3.5" fill="none" stroke="#1976D2" stroke-width="2"/><path d="M-9,8 a7,6 0 0 1 14,0" fill="none" stroke="#1976D2" stroke-width="2" stroke-linecap="round"/><path d="M7,-5 V1 M4,-2 H10" fill="none" stroke="#1976D2" stroke-width="2" stroke-linecap="round"/></g>
    <text x="142" y="539" font-size="14.5" font-weight="600" fill="#1976D2" text-anchor="start">Crear cuenta</text>
    <text x="170" y="600" font-size="13" font-weight="400" fill="#556074" text-anchor="middle">¿Olvidaste tu contraseña?</text>
    <text x="16" y="22" font-size="11.5" font-weight="700" fill="#161A26" text-anchor="start">9:41</text><rect x="138.0" y="7" width="64" height="18" rx="9" fill="#1F2430"/><rect x="302" y="11" width="22" height="11" rx="3" fill="none" stroke="#161A26" stroke-width="1.5"/><rect x="304" y="13" width="13" height="7" rx="1.5" fill="#161A26"/><rect x="134.0" y="664" width="72" height="5" rx="2.5" fill="#1F2430"/>
  </g></g>
  <text x="270" y="844" font-size="15" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono">ProfileScreen</text>
  <text x="270" y="864" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" class="mono">'/profile'</text>
  <text x="690" y="844" font-size="15" font-weight="700" fill="#4453C9" text-anchor="middle" class="mono">LoginScreen</text>
  <text x="690" y="864" font-size="13" font-weight="400" fill="#556074" text-anchor="middle" class="mono">'/login'</text>
</svg>
```

En este taller armas **dos pantallas** con los componentes de la sesión anterior. No hay componentes nuevos que diseñar: el trabajo es ordenarlos, darles aire y hacer que todo quepa.

Necesitas tus siete componentes terminados en `lib/components/`. Si te falta alguno, termínalo primero con el *Taller · Componentes*.

## Cómo trabajar

Cada pantalla va en su archivo dentro de `lib/screens/` y se registra en `routes`, en `lib/main.dart`. Para ver una u otra, cambia `initialRoute` y reinicia la app:

```dart
initialRoute: '/profile',
routes: {
  '/home': (context) => const HomeScreen(),
  '/login': (context) => const LoginScreen(),
  '/profile': (context) => const ProfileScreen(),
},
```

Las dos pantallas tienen el mismo esqueleto, el de la lección anterior: `Scaffold`, `SafeArea`, `SingleChildScrollView` y una `Column`. Ármalo primero y agrega los bloques de arriba hacia abajo, ejecutando después de cada uno.

Los botones siguen con su `print`. Pasar de una pantalla a otra al tocarlos es la sesión 8.

## 1. Un componente que te entregamos

Las dos secciones del perfil empiezan con un título y un enlace a la derecha. Ese encabezado es un componente, y este ya viene hecho. Crea `lib/components/section_header.dart` y copia:

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

Léelo antes de usarlo. Tiene la forma de todos tus componentes, y el `Expanded` hace lo que viste hoy: el título ocupa lo que sobra y empuja el enlace hasta el borde derecho.

Usar un componente que no escribiste es lo normal en un equipo. Lo único que necesitas saber de él es qué recibe: `title` y `actionLabel`.

## 2. Pantalla de perfil

**Archivo:** `lib/screens/profile_screen.dart` · **Clase:** `ProfileScreen` · **Ruta:** `'/profile'`

Ya tienes la mitad de arriba de la lección anterior: `ProfileInfo` y `StatsRow`. Agrega debajo, en este orden:

1. `PrimaryButton` con *Seguir* y `SecondaryButton` con *Enviar mensaje*, uno debajo del otro.
2. `SectionHeader` con *Contactos sugeridos*, y debajo una fila con al menos seis `ContactCard` que se deslice de lado.
3. `SectionHeader` con *Últimas conversaciones*, y debajo al menos cuatro `ChatItem`.

**Pista 1 · el aire.** Usa dos separaciones y nada más: `SizedBox(height: 24)` entre un bloque y el siguiente, y `8` o `12` entre las cosas de un mismo bloque. El borde de la pantalla lo pone el `padding` del scroll.

**Pista 2 · la fila de contactos.** Es un `SingleChildScrollView` con `scrollDirection: Axis.horizontal` y una `Row` adentro, con un `SizedBox(width: 12)` entre tarjetas. Va como un hijo más de la `Column`.

**Pista 3 · todo a la izquierda o al centro.** Una `Column` centra a sus hijos. `ProfileInfo` se ve bien así, pero la fila de contactos debería empezar en el borde izquierdo. Si no queda donde quieres, revisa `crossAxisAlignment` en la `Column` de la pantalla.

**Pista 4 · la pantalla angosta.** Haz más angosta la ventana de Chrome hasta que mida lo que un teléfono pequeño. Si aparece la franja amarilla y negra en `StatsRow`, las tres tarjetas ya no caben. El arreglo va en el componente, no en la pantalla: en `stats_row.dart`, envuelve cada `StatCard` en un `Expanded` y sepáralas con `SizedBox(width: 8)`.

En el diseño del [proyecto de Figma](https://www.figma.com/design/cn5cLhBPnuJC4tvewTtVmq/Aplicaciones-M%C3%B3viles?node-id=2014-421&t=oULdr2bxOVE437ux-1) la información del perfil y las estadísticas van dentro de una tarjeta blanca con esquinas redondeadas. Si te alcanza el tiempo, hazla: es un `Container` con `padding` y `decoration` que envuelve una `Column` con esos dos componentes, sobre un `Scaffold` con `backgroundColor` gris claro.

## 3. Pantalla de inicio de sesión

**Archivo:** `lib/screens/login_screen.dart` · **Clase:** `LoginScreen` · **Ruta:** `'/login'`

Esta pantalla **no tiene `AppBar`**. De arriba hacia abajo lleva:

1. Un círculo de color con un icono adentro, a modo de logo.
2. El título *Bienvenido* y el texto *Inicia sesión para continuar*.
3. Un `TextField` para el correo y otro para la contraseña.
4. `PrimaryButton` con *Iniciar sesión* y `SecondaryButton` con *Crear cuenta*.
5. Un `TextButton` con *¿Olvidaste tu contraseña?*

**Pista 1 · el logo.** Es un `Container` con `width` y `height` iguales y un `borderRadius` de la mitad de ese tamaño. Su `child` es un `Icon`.

```dart
Container(
  width: 96,
  height: 96,
  decoration: BoxDecoration(
    color: Colors.blue.shade50,
    borderRadius: BorderRadius.circular(48),
  ),
  child: Icon(Icons.check, size: 48, color: Colors.blue),
)
```

**Pista 2 · los campos.** Son los de la lección *TextField*: `labelText` y `border: OutlineInputBorder()` en `decoration`. El de la contraseña lleva `obscureText: true` y el del correo `keyboardType: TextInputType.emailAddress`. Por ahora solo se ven: leer lo que la persona escribe es la sesión 6.

**Pista 3 · bajar el contenido.** Sin barra, el logo queda pegado arriba. Dentro de un scroll no sirven `Spacer` ni `mainAxisAlignment`, así que el espacio se pone con un `SizedBox(height: 48)` como primer hijo de la `Column`.

**Pista 4 · por qué lleva scroll si todo cabe.** En un teléfono, al tocar un campo sube el teclado y tapa media pantalla. Con el `SingleChildScrollView` la persona puede deslizar para ver el botón. Sin él, aparece la franja.

## Qué debes tener al terminar

```svg
<svg id="tpCarpetas" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 492" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tpCarpetas-ttl tpCarpetas-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tpCarpetas-ttl">Tu proyecto al terminar el taller</title>
  <desc id="tpCarpetas-dsc">La carpeta lib con main.dart y dos subcarpetas. En components están los siete componentes de la sesión 2 y uno nuevo, section_header.dart. En screens están home_screen.dart y las dos pantallas nuevas, profile_screen.dart y login_screen.dart.</desc>
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
  <rect width="960" height="492" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Tu proyecto al terminar el taller</text>
  <text class="sub" x="48" y="80" data-fit="860">Los componentes ya los tienes. Hoy agregas uno que te entregamos y dos pantallas.</text>
  <path d="M64,132 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/><text x="98" y="145" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">lib/</text>
  <path d="M104,167 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="130" y="181" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">main.dart</text>
  <path d="M104,210 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/><text x="138" y="223" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">components/</text>
  <path d="M144,243 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="257" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">chat_item.dart</text>
  <path d="M144,271 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="285" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">contact_card.dart</text>
  <path d="M144,299 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="313" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">primary_button.dart</text>
  <path d="M144,327 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="341" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">profile_info.dart</text>
  <path d="M144,355 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="369" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">secondary_button.dart</text>
  <path d="M144,383 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="397" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">section_header.dart</text><rect x="376" y="382" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="404" y="397" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M144,411 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="425" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">stat_card.dart</text>
  <path d="M144,439 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="170" y="453" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">stats_row.dart</text>
  <path d="M536,210 h9 l3,3 h12 v13 h-24 Z" fill="#FFF3DC" stroke="#A96C05" stroke-width="1.5" stroke-linejoin="round"/><text x="570" y="223" font-size="14.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono">screens/</text>
  <path d="M576,243 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#79809A" stroke-width="1.5" stroke-linejoin="round"/><text x="602" y="257" font-size="13.5" font-weight="400" fill="#556074" text-anchor="start" class="mono">home_screen.dart</text>
  <path d="M576,271 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/><text x="602" y="285" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">login_screen.dart</text><rect x="808" y="270" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="836" y="285" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M576,299 h10 l5,5 v13 h-15 Z" fill="#FFFFFF" stroke="#3A8235" stroke-width="1.5" stroke-linejoin="round"/><text x="602" y="313" font-size="13.5" font-weight="700" fill="#3A8235" text-anchor="start" class="mono">profile_screen.dart</text><rect x="808" y="298" width="56" height="22" rx="11" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="836" y="313" font-size="12" font-weight="700" fill="#3A8235" text-anchor="middle">nuevo</text>
  <path d="M76,156 V218 H96 M76,176 H96" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M116,234 V448 M548,234 V308" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
  <path d="M76,198 H508 V218 H528" fill="none" stroke="#C4CBD8" stroke-width="1.5"/>
</svg>
```

- Las dos pantallas registradas en `routes`, y cada una se ve completa al ponerla en `initialRoute`.
- Ningún archivo de `lib/screens/` dibuja algo que ya exista como componente: si copiaste el código de un `ChatItem` dentro de la pantalla, cámbialo por el componente.
- Todos los `import` de archivos propios empiezan por `package:miapp1/`.
- Las dos pantallas aguantan una ventana angosta y una baja, sin franjas.
- El proyecto sin errores en el editor.

Lo que no alcances en clase se termina por fuera. Estas dos pantallas son la base del prototipo de tu equipo.
