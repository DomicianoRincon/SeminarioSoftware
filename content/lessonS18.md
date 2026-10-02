# Taller · Componentes

<!-- tags: taller de componentes, botón con icono y texto, CircleAvatar, tarjeta de contacto, Expanded, RenderFlex overflowed on the right, ElevatedButton.styleFrom, OutlinedButton.styleFrom, IconData como parámetro, ancho fijo con SizedBox -->

```svg
<svg id="tlTodos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 708" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tlTodos-ttl tlTodos-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tlTodos-ttl">Lo que vas a construir</title>
  <desc id="tlTodos-dsc">Los seis componentes del taller, cada uno con una vista previa: PrimaryButton, un botón azul que dice Iniciar sesión; SecondaryButton, un botón con borde que dice Crear cuenta; StatsRow, una fila de tres tarjetas con números; ChatItem, una fila de chat con foto, nombre, mensaje y hora; ProfileInfo, la cabecera de un perfil con foto, nombre, usuario, correo y ciudad; y ContactCard, una tarjeta pequeña con foto, nombre y usuario.</desc>
  <defs>
    <style>
      #tlTodos .title{fill:#161A26;font-size:22px;font-weight:700}
      #tlTodos .sub{fill:#79809A;font-size:13.5px}
      #tlTodos .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tlTodos .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tlTodos .nb{fill:#454C61;font-size:13px}
      #tlTodos .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tlTodos .foot{fill:#79809A;font-size:12px}
      #tlTodos .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tlTodos .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tlTodos-arrow)}
    </style>
    <marker id="tlTodos-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="708" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Lo que vas a construir</text>
  <text class="sub" x="48" y="80" data-fit="860">Seis componentes, cada uno en su archivo dentro de lib/components/. El número es el apartado del taller donde se arma.</text>
  <g transform="translate(48,112)">
    <rect width="420" height="168" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <rect x="12" y="12" width="396" height="100" rx="10" fill="#F5F6FA"/>
    <g transform="translate(12,12)"><rect x="48" y="28" width="300" height="44" rx="22" fill="#2196F3" stroke="none" stroke-width="1.75"/><g transform="translate(146,50)"><path d="M-9,0 H3 M-1,-4 L3,0 L-1,4" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M2,-8 H8 V8 H2" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g><text x="166" y="50" dy="0.35em" font-size="15" font-weight="600" fill="#FFFFFF" data-fit="170">Iniciar sesión</text></g>
    <circle cx="27" cy="140" r="11" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
    <text x="27" y="140" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="#A96C05">1</text>
    <text class="mono" x="48" y="140" dy="0.35em" font-size="15" font-weight="700" fill="#161A26" data-fit="170">PrimaryButton</text>
    <text class="mono" x="406" y="140" dy="0.35em" text-anchor="end" font-size="12" fill="#79809A" data-fit="180">primary_button.dart</text>
  </g>
  <g transform="translate(492,112)">
    <rect width="420" height="168" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <rect x="12" y="12" width="396" height="100" rx="10" fill="#F5F6FA"/>
    <g transform="translate(12,12)"><rect x="48" y="28" width="300" height="44" rx="22" fill="#FFFFFF" stroke="#2196F3" stroke-width="1.75"/><g transform="translate(150,50)"><circle cx="-2" cy="-4" r="3.5" fill="none" stroke="#1976D2" stroke-width="2"/><path d="M-9,8 a7,6 0 0 1 14,0" fill="none" stroke="#1976D2" stroke-width="2" stroke-linecap="round"/><path d="M7,-5 V1 M4,-2 H10" fill="none" stroke="#1976D2" stroke-width="2" stroke-linecap="round"/></g><text x="170" y="50" dy="0.35em" font-size="15" font-weight="600" fill="#1976D2" data-fit="170">Crear cuenta</text></g>
    <circle cx="27" cy="140" r="11" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
    <text x="27" y="140" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="#A96C05">1</text>
    <text class="mono" x="48" y="140" dy="0.35em" font-size="15" font-weight="700" fill="#161A26" data-fit="170">SecondaryButton</text>
    <text class="mono" x="406" y="140" dy="0.35em" text-anchor="end" font-size="12" fill="#79809A" data-fit="180">secondary_button.dart</text>
  </g>
  <g transform="translate(48,296)">
    <rect width="420" height="168" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <rect x="12" y="12" width="396" height="100" rx="10" fill="#F5F6FA"/>
    <g transform="translate(12,12)"><rect x="30" y="16" width="104" height="68" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="82" y="46" font-size="20" font-weight="700" fill="#161A26" text-anchor="middle">128</text><text x="82" y="68" font-size="12" font-weight="400" fill="#556074" text-anchor="middle" data-fit="96">Publicaciones</text><rect x="146" y="16" width="104" height="68" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="198" y="46" font-size="20" font-weight="700" fill="#161A26" text-anchor="middle">2.4k</text><text x="198" y="68" font-size="12" font-weight="400" fill="#556074" text-anchor="middle" data-fit="96">Seguidores</text><rect x="262" y="16" width="104" height="68" rx="10" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><text x="314" y="46" font-size="20" font-weight="700" fill="#161A26" text-anchor="middle">310</text><text x="314" y="68" font-size="12" font-weight="400" fill="#556074" text-anchor="middle" data-fit="96">Seguidos</text></g>
    <circle cx="27" cy="140" r="11" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
    <text x="27" y="140" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="#A96C05">2</text>
    <text class="mono" x="48" y="140" dy="0.35em" font-size="15" font-weight="700" fill="#161A26" data-fit="170">StatsRow</text>
    <text class="mono" x="406" y="140" dy="0.35em" text-anchor="end" font-size="12" fill="#79809A" data-fit="180">stats_row.dart</text>
  </g>
  <g transform="translate(492,296)">
    <rect width="420" height="168" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <rect x="12" y="12" width="396" height="100" rx="10" fill="#F5F6FA"/>
    <g transform="translate(12,12)"><circle cx="44" cy="50" r="24" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/><circle cx="44" cy="45.2" r="7.9" fill="#F0C572"/><path d="M29.1,67.8 a14.9,13.4 0 0 1 29.8,0 Z" fill="#F0C572"/><text x="80" y="45" font-size="14" font-weight="700" fill="#161A26" text-anchor="start" data-fit="180">Javier Montes</text><text x="80" y="66" font-size="12.5" font-weight="400" fill="#556074" text-anchor="start" data-fit="220">¿Te parece si revisamos los…</text><text x="376" y="45" font-size="12" font-weight="400" fill="#79809A" text-anchor="end" data-fit="80">10:24 a.m.</text><path d="M354,62 l3,3 l6,-7 M360,65 l1,0 l6,-7" fill="none" stroke="#4453C9" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></g>
    <circle cx="27" cy="140" r="11" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
    <text x="27" y="140" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="#A96C05">3</text>
    <text class="mono" x="48" y="140" dy="0.35em" font-size="15" font-weight="700" fill="#161A26" data-fit="170">ChatItem</text>
    <text class="mono" x="406" y="140" dy="0.35em" text-anchor="end" font-size="12" fill="#79809A" data-fit="180">chat_item.dart</text>
  </g>
  <g transform="translate(48,480)">
    <rect width="420" height="168" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <rect x="12" y="12" width="396" height="100" rx="10" fill="#F5F6FA"/>
    <g transform="translate(12,12)"><circle cx="198" cy="22" r="17" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/><circle cx="198" cy="18.6" r="5.6" fill="#C9A6EE"/><path d="M187.5,34.6 a10.5,9.5 0 0 1 21.1,0 Z" fill="#C9A6EE"/><text x="198" y="58" font-size="14" font-weight="700" fill="#161A26" text-anchor="middle" data-fit="240">Mariana Valenzuela</text><text x="198" y="75" font-size="12" font-weight="400" fill="#556074" text-anchor="middle" data-fit="300">@marianav • Diseñadora de Producto</text><g transform="translate(28,-106)"><g transform="translate(62,195) scale(.72)"><rect x="-9" y="-7" width="18" height="14" rx="2" fill="none" stroke="#556074" stroke-width="1.75"/><path d="M-9,-6 L0,1 L9,-6" fill="none" stroke="#556074" stroke-width="1.75"/></g><text x="74" y="199" font-size="12" font-weight="400" fill="#556074" text-anchor="start">m.val@estudio.com</text><path d="M212,189 a5,5 0 0 1 10,0 c0,4 -5,9 -5,9 c0,0 -5,-5 -5,-9 Z" fill="none" stroke="#556074" stroke-width="1.4"/><circle cx="217" cy="189" r="1.6" fill="#556074"/><text x="227" y="199" font-size="12" font-weight="400" fill="#556074" text-anchor="start">Madrid, ES</text></g></g>
    <circle cx="27" cy="140" r="11" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
    <text x="27" y="140" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="#A96C05">4</text>
    <text class="mono" x="48" y="140" dy="0.35em" font-size="15" font-weight="700" fill="#161A26" data-fit="170">ProfileInfo</text>
    <text class="mono" x="406" y="140" dy="0.35em" text-anchor="end" font-size="12" fill="#79809A" data-fit="180">profile_info.dart</text>
  </g>
  <g transform="translate(492,480)">
    <rect width="420" height="168" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
    <rect x="12" y="12" width="396" height="100" rx="10" fill="#F5F6FA"/>
    <g transform="translate(12,12)"><rect x="146" y="4" width="104" height="92" rx="10" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/><circle cx="198" cy="32" r="20" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/><circle cx="198" cy="28.0" r="6.6" fill="#A9B4F2"/><path d="M185.6,46.8 a12.4,11.2 0 0 1 24.8,0 Z" fill="#A9B4F2"/><text x="198" y="70" font-size="13" font-weight="700" fill="#161A26" text-anchor="middle" data-fit="96">Ana Torres</text><text x="198" y="87" font-size="12" font-weight="400" fill="#79809A" text-anchor="middle" data-fit="96">@anatorres</text></g>
    <circle cx="27" cy="140" r="11" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
    <text x="27" y="140" dy="0.35em" text-anchor="middle" font-size="12" font-weight="700" fill="#A96C05">5</text>
    <text class="mono" x="48" y="140" dy="0.35em" font-size="15" font-weight="700" fill="#161A26" data-fit="170">ContactCard</text>
    <text class="mono" x="406" y="140" dy="0.35em" text-anchor="end" font-size="12" fill="#79809A" data-fit="180">contact_card.dart</text>
  </g>
  <text class="foot" x="48" y="680" data-fit="860">En la sesión 3 estas seis piezas se encajan para armar una pantalla de perfil y una de inicio de sesión.</text>
</svg>
```

En este taller construyes **seis componentes**. Solo componentes: ninguna pantalla. En la próxima sesión los vas a usar para armar una pantalla de perfil y una de inicio de sesión, así que tenerlos terminados es la preparación para esa clase.

Los diseños de los componentes de perfil están en el [proyecto de Figma](https://www.figma.com/design/cn5cLhBPnuJC4tvewTtVmq/Aplicaciones-M%C3%B3viles?node-id=2014-421&t=oULdr2bxOVE437ux-1). Ahí puedes medir tamaños, colores y separaciones.

## Cómo trabajar

Cada componente va en su propio archivo dentro de `lib/components/`. Todos los archivos tienen la misma forma. Este es el del primer componente, `lib/components/primary_button.dart`, antes de darle su diseño:

```dart
import 'package:flutter/material.dart';

/// Main action button, with an icon and a label.
class PrimaryButton extends StatelessWidget {
  final String label;
  final IconData icon;

  const PrimaryButton({
    super.key,
    required this.label,
    required this.icon,
  });

  @override
  Widget build(BuildContext context) {
    return Text(label);
  }
}
```

De arriba hacia abajo:

- El `import` de Flutter.
- **Una línea `///`** que dice qué muestra el componente. Es el único comentario del archivo.
- La clase, con el nombre del archivo en mayúsculas iniciales: `primary_button.dart` contiene `PrimaryButton`.
- Un campo `final` por cada dato de la tabla de parámetros del componente.
- El constructor, con esos mismos datos como parámetros con nombre.
- `build`, que por ahora devuelve un `Text` para que el archivo compile. Tu trabajo es reemplazar ese `Text` por el diseño.

Para ver un componente, móntalo en `HomeScreen`, dentro del `Center`, y pásale datos. Cambia esos datos y comprueba que el diseño aguanta.

La prueba de que un componente está bien hecho: **todo lo que cambia entre un uso y otro llega por el constructor**. Si para reutilizarlo tendrías que abrir el archivo y editar un texto, un icono o una imagen, ese dato debería ser un parámetro.

## 1. Botón principal y botón secundario

Dos botones que van juntos: el principal, relleno de azul, para la acción más importante de la pantalla, y el secundario, solo con borde, para la alternativa. Los dos llevan adentro un icono y un texto.

```svg
<svg id="tlBoton" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 292" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tlBoton-ttl tlBoton-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tlBoton-ttl">Botón principal y botón secundario</title>
  <desc id="tlBoton-dsc">Dos botones a todo el ancho con un icono y un texto centrados. El principal, PrimaryButton, es azul con el contenido blanco y dice Iniciar sesión. El secundario, SecondaryButton, es blanco con borde y contenido azules y dice Crear cuenta.</desc>
  <defs>
    <style>
      #tlBoton .title{fill:#161A26;font-size:22px;font-weight:700}
      #tlBoton .sub{fill:#79809A;font-size:13.5px}
      #tlBoton .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tlBoton .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tlBoton .nb{fill:#454C61;font-size:13px}
      #tlBoton .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tlBoton .foot{fill:#79809A;font-size:12px}
      #tlBoton .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tlBoton .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tlBoton-arrow)}
    </style>
    <marker id="tlBoton-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="292" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Botón principal y botón secundario</text>
  <text class="sub" x="48" y="80" data-fit="860">La misma estructura en los dos: un icono y un texto en fila. Cambia el tipo de botón.</text>
  <g transform="translate(48,112)">
    <text class="mono" x="0" y="12" font-size="14" font-weight="700" fill="#161A26" data-fit="408">PrimaryButton</text>
    <rect y="28" width="408" height="84" rx="12" fill="#EFF1F5"/>
    <rect x="24" y="48" width="360" height="44" rx="22" fill="#2196F3" stroke="none" stroke-width="1.75"/>
    <g transform="translate(146,70)"><path d="M-9,0 H3 M-1,-4 L3,0 L-1,4" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M2,-8 H8 V8 H2" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>
    <text x="166" y="70" dy="0.35em" font-size="15" font-weight="600" fill="#FFFFFF" data-fit="200">Iniciar sesión</text>
    <text class="mono" x="0" y="136" font-size="12" fill="#556074" data-fit="408">label: 'Iniciar sesión'</text>
    <text class="mono" x="0" y="156" font-size="12" fill="#556074" data-fit="408">icon: Icons.login</text>
  </g>
  <g transform="translate(504,112)">
    <text class="mono" x="0" y="12" font-size="14" font-weight="700" fill="#161A26" data-fit="408">SecondaryButton</text>
    <rect y="28" width="408" height="84" rx="12" fill="#EFF1F5"/>
    <rect x="24" y="48" width="360" height="44" rx="22" fill="#FFFFFF" stroke="#2196F3" stroke-width="1.75"/>
    <g transform="translate(150,70)"><circle cx="-2" cy="-4" r="3.5" fill="none" stroke="#1976D2" stroke-width="2"/><path d="M-9,8 a7,6 0 0 1 14,0" fill="none" stroke="#1976D2" stroke-width="2" stroke-linecap="round"/><path d="M7,-5 V1 M4,-2 H10" fill="none" stroke="#1976D2" stroke-width="2" stroke-linecap="round"/></g>
    <text x="170" y="70" dy="0.35em" font-size="15" font-weight="600" fill="#1976D2" data-fit="200">Crear cuenta</text>
    <text class="mono" x="0" y="136" font-size="12" fill="#556074" data-fit="408">label: 'Crear cuenta'</text>
    <text class="mono" x="0" y="156" font-size="12" fill="#556074" data-fit="408">icon: Icons.person_add_outlined</text>
  </g>
</svg>
```

| Archivo | Clase | Por dentro es un |
|---|---|---|
| `lib/components/primary_button.dart` | `PrimaryButton` | `ElevatedButton` |
| `lib/components/secondary_button.dart` | `SecondaryButton` | `OutlinedButton` |

Los dos reciben lo mismo:

| Parámetro | Tipo | Ejemplo |
|---|---|---|
| `label` | `String` | `'Iniciar sesión'` |
| `icon` | `IconData` | `Icons.login` |

Un icono también es un dato. `Icons.login` es un valor de tipo `IconData`: el componente lo guarda en un campo `final IconData icon;` y lo dibuja con `Icon(icon)`.

Como todavía no hay nada que hacer al tocarlos, deja en `onPressed` una función con un `print`.

**Pista 1 · el contenido.** El `child` de un botón es un widget cualquiera, así que puede ser una `Row`:

```dart
Row(
  mainAxisAlignment: MainAxisAlignment.center,
  children: [
    Icon(Icons.login),
    SizedBox(width: 8),
    Text('Iniciar sesión'),
  ],
)
```

Una `Row` ocupa todo el ancho que le den, y por eso el botón queda a todo lo ancho. Si lo quisieras del tamaño de su contenido, le pondrías `mainAxisSize: MainAxisSize.min`.

**Pista 2 · el azul del principal.** Los colores de un botón se cambian con `style`. `backgroundColor` es el fondo y `foregroundColor` el color del icono y del texto:

```dart
ElevatedButton(
  style: ElevatedButton.styleFrom(
    backgroundColor: Colors.blue,
    foregroundColor: Colors.white,
  ),
  onPressed: () {
    print('Iniciar sesión');
  },
  child: Text('Iniciar sesión'),
)
```

**Pista 3 · el borde del secundario.** `OutlinedButton` tiene su propio `styleFrom`. No lleva fondo: el color va en el contenido y en el borde, que se define con `side`:

```dart
OutlinedButton(
  style: OutlinedButton.styleFrom(
    foregroundColor: Colors.blue,
    side: BorderSide(color: Colors.blue),
  ),
  onPressed: () {
    print('Crear cuenta');
  },
  child: Text('Crear cuenta'),
)
```

Cuando termines el principal, el secundario es casi una copia. Fíjate en cuánto se repite entre los dos archivos: es la misma señal que viste en la lección anterior.

## 2. Fila de estadísticas

Tu primer **componente compuesto**: uno que está hecho con otro componente tuyo. Es la fila de indicadores de un perfil, armada con tres `StatCard`, el componente de la lección anterior.

```svg
<svg id="tlStats" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 340" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tlStats-ttl tlStats-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tlStats-ttl">Fila de estadísticas</title>
  <desc id="tlStats-dsc">El componente StatsRow: una fila con tres tarjetas StatCard, que muestran 128 publicaciones, 2.4k seguidores y 310 seguidos. Cada tarjeta tiene fondo suave, borde y esquinas redondeadas.</desc>
  <defs>
    <style>
      #tlStats .title{fill:#161A26;font-size:22px;font-weight:700}
      #tlStats .sub{fill:#79809A;font-size:13.5px}
      #tlStats .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tlStats .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tlStats .nb{fill:#454C61;font-size:13px}
      #tlStats .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tlStats .foot{fill:#79809A;font-size:12px}
      #tlStats .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tlStats .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tlStats-arrow)}
    </style>
    <marker id="tlStats-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="340" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Fila de estadísticas</text>
  <text class="sub" x="48" y="80" data-fit="860">Un componente hecho con otro componente: tres StatCard dentro de una Row.</text>
  <rect x="240" y="124" width="480" height="128" rx="14" fill="none" stroke="#C4CBD8" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text class="mono" x="240" y="114" font-size="13" font-weight="700" fill="#161A26" data-fit="200">StatsRow</text>
  <g transform="translate(272,148)">
    <rect width="112" height="80" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="2"/>
    <text x="56" y="36" text-anchor="middle" font-size="24" font-weight="700" fill="#161A26">128</text>
    <text x="56" y="60" text-anchor="middle" font-size="12.5" fill="#556074" data-fit="100">Publicaciones</text>
  </g>
  <text class="mono" x="328" y="276" text-anchor="middle" font-size="12" fill="#556074" data-fit="120">StatCard</text>
  <g transform="translate(424,148)">
    <rect width="112" height="80" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="2"/>
    <text x="56" y="36" text-anchor="middle" font-size="24" font-weight="700" fill="#161A26">2.4k</text>
    <text x="56" y="60" text-anchor="middle" font-size="12.5" fill="#556074" data-fit="100">Seguidores</text>
  </g>
  <text class="mono" x="480" y="276" text-anchor="middle" font-size="12" fill="#556074" data-fit="120">StatCard</text>
  <g transform="translate(576,148)">
    <rect width="112" height="80" rx="12" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="2"/>
    <text x="56" y="36" text-anchor="middle" font-size="24" font-weight="700" fill="#161A26">310</text>
    <text x="56" y="60" text-anchor="middle" font-size="12.5" fill="#556074" data-fit="100">Seguidos</text>
  </g>
  <text class="mono" x="632" y="276" text-anchor="middle" font-size="12" fill="#556074" data-fit="120">StatCard</text>
  <text class="foot" x="48" y="312" data-fit="860">El diseño de la tarjeta vive en StatCard. StatsRow solo decide cuántas hay, en qué orden y cómo se reparten.</text>
</svg>
```

**Archivo:** `lib/components/stats_row.dart` · **Clase:** `StatsRow`

| Parámetro | Tipo | Ejemplo |
|---|---|---|
| `posts` | `String` | `'128'` |
| `followers` | `String` | `'2.4k'` |
| `following` | `String` | `'310'` |

Aquí las etiquetas *Publicaciones*, *Seguidores* y *Seguidos* sí van escritas dentro del componente: son parte de lo que `StatsRow` es. Lo que cambia de un perfil a otro son los tres números, y por eso solo ellos llegan por el constructor.

**Pista 1 · usar tu propio componente.** `StatCard` está en otro archivo de la misma carpeta, así que hay que importarlo. Después se usa como cualquier widget de Flutter:

```dart
import 'package:flutter/material.dart';
import 'stat_card.dart';
```

**Pista 2 · repartir las tres tarjetas.** Es una `Row` con `mainAxisAlignment: MainAxisAlignment.spaceEvenly`.

**Pista 3 · la caja de cada tarjeta.** El fondo, el borde y las esquinas redondeadas se hacen con un `Container`, un widget que envuelve a otro y lo decora. Se ve a fondo en la sesión 3; por ahora basta con este uso:

```dart
Container(
  padding: EdgeInsets.symmetric(horizontal: 16, vertical: 12),
  decoration: BoxDecoration(
    color: Colors.indigo.shade50,
    border: Border.all(color: Colors.indigo.shade200, width: 2),
    borderRadius: BorderRadius.circular(12),
  ),
  child: Text('128'),
)
```

Fíjate en **dónde** va ese `Container`: en `stat_card.dart`, envolviendo la `Column` que ya tenías. No en `stats_row.dart`. Lo escribes una vez y las tres tarjetas cambian, que es justo para lo que sirve un componente.

## 3. Elemento de conversación

La fila de un chat: la foto del contacto, su nombre, la hora del último mensaje, el inicio de ese mensaje y el icono de leído.

![Elemento de conversación](Lab1Item1.png "frame60")

**Archivo:** `lib/components/chat_item.dart` · **Clase:** `ChatItem`

| Parámetro | Tipo | Ejemplo |
|---|---|---|
| `imageUrl` | `String` | `'https://picsum.photos/400'` |
| `name` | `String` | `'Javier Montes'` |
| `time` | `String` | `'10:24 a.m.'` |
| `message` | `String` | `'¿Te parece si revisamos los avances?'` |

Antes de escribir, parte el diseño en cajas: es una `Row` con tres hijos, la foto, una `Column` con los dos textos y otra `Column` con la hora y el icono.

**Pista 1 · la foto circular.** No uses una imagen ya recortada. `CircleAvatar` recorta en círculo cualquier imagen:

```dart
CircleAvatar(
  radius: 28,
  backgroundImage: NetworkImage('https://picsum.photos/400'),
)
```

**Pista 2 · el mensaje largo.** Si el mensaje no cabe, aparece la franja amarilla y negra que viste en *Row*. Envuelve la `Column` de los textos en un `Expanded`, que le da el espacio que sobra en la fila y ni un píxel más. Con eso, `maxLines` y `overflow` ya pueden recortar el texto:

```dart
Expanded(
  child: Column(
    crossAxisAlignment: CrossAxisAlignment.start,
    children: [
      Text('Javier Montes'),
      Text(
        '¿Te parece si revisamos los avances?',
        maxLines: 1,
        overflow: TextOverflow.ellipsis,
      ),
    ],
  ),
)
```

**Pista 3 · el icono de leído.** Es `Icon(Icons.done_all)`, con `color` y `size`.

## 4. Bloque de información de perfil

La cabecera de un perfil: foto, nombre, usuario y rol, una descripción corta, el correo y la ciudad.

![Bloque de información de perfil](Lab1Item2.png "frame60")

**Archivo:** `lib/components/profile_info.dart` · **Clase:** `ProfileInfo`

| Parámetro | Tipo | Ejemplo |
|---|---|---|
| `imageUrl` | `String` | `'https://picsum.photos/400'` |
| `name` | `String` | `'Mariana Valenzuela'` |
| `username` | `String` | `'@marianav'` |
| `role` | `String` | `'Diseñadora de Producto'` |
| `bio` | `String` | `'Creando experiencias digitales enfocadas en el usuario.'` |
| `email` | `String` | `'m.val@estudio.com'` |
| `location` | `String` | `'Madrid, ES'` |

Es una `Column` centrada. La última línea es una `Row` con dos parejas de icono y texto.

- La descripción ocupa varios renglones: céntrala con `textAlign`.
- Usuario y rol van en un solo `Text`. Se unen con interpolación: `'$username • $role'`.
- Los iconos son `Icons.mail_outline` e `Icons.location_on_outlined`.
- `mainAxisSize: MainAxisSize.min` evita que la columna ocupe toda la pantalla.

## 5. Contacto sugerido

Una versión mínima del perfil: la foto, el nombre y el usuario. Es la tarjeta de una sección de *contactos sugeridos*, donde varias se ponen en fila y la persona las desliza hacia los lados.

```svg
<svg id="tlContacto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 372" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tlContacto-ttl tlContacto-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tlContacto-ttl">Contacto sugerido</title>
  <desc id="tlContacto-dsc">Una sección de contactos sugeridos con una fila de tarjetas pequeñas, cada una con una foto circular, un nombre y un usuario. La fila continúa más allá del borde derecho. La primera tarjeta está resaltada: es el componente que se construye.</desc>
  <defs>
    <style>
      #tlContacto .title{fill:#161A26;font-size:22px;font-weight:700}
      #tlContacto .sub{fill:#79809A;font-size:13.5px}
      #tlContacto .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tlContacto .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tlContacto .nb{fill:#454C61;font-size:13px}
      #tlContacto .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tlContacto .foot{fill:#79809A;font-size:12px}
      #tlContacto .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tlContacto .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tlContacto-arrow)}
    </style>
    <marker id="tlContacto-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="372" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Contacto sugerido</text>
  <text class="sub" x="48" y="80" data-fit="860">Tu componente es una sola de estas tarjetas. La fila que se desliza hacia los lados se arma en la sesión 3.</text>
  <clipPath id="tlContacto-clip"><rect x="48" y="112" width="864" height="196" rx="12"/></clipPath>
  <rect x="48" y="112" width="864" height="196" rx="12" fill="#FFFFFF" stroke="#D9DEE8" stroke-width="1.5"/>
  <text x="72" y="146" font-size="16" font-weight="700" fill="#161A26" data-fit="300">Contactos sugeridos</text>
  <g clip-path="url(#tlContacto-clip)">
    <g transform="translate(72,168)">
      <rect x="-6" y="-8" width="108" height="132" rx="10" fill="none" stroke="#F2C069" stroke-width="2.5"/>
      <circle cx="48" cy="32" r="30" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
      <circle cx="48" cy="24" r="10" fill="#A9B4F2"/><path d="M28,54 a20,17 0 0 1 40,0 Z" fill="#A9B4F2"/>
      <text x="48" y="88" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="110">Ana Torres</text>
      <text x="48" y="108" text-anchor="middle" font-size="12" fill="#79809A" data-fit="110">@anatorres</text>
    </g>
    <g transform="translate(188,168)">
      <circle cx="48" cy="32" r="30" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
      <circle cx="48" cy="24" r="10" fill="#86D3CA"/><path d="M28,54 a20,17 0 0 1 40,0 Z" fill="#86D3CA"/>
      <text x="48" y="88" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="110">Luis Peña</text>
      <text x="48" y="108" text-anchor="middle" font-size="12" fill="#79809A" data-fit="110">@luisp</text>
    </g>
    <g transform="translate(304,168)">
      <circle cx="48" cy="32" r="30" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/>
      <circle cx="48" cy="24" r="10" fill="#F3A3B2"/><path d="M28,54 a20,17 0 0 1 40,0 Z" fill="#F3A3B2"/>
      <text x="48" y="88" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="110">Sofía Ruiz</text>
      <text x="48" y="108" text-anchor="middle" font-size="12" fill="#79809A" data-fit="110">@sofiaruiz</text>
    </g>
    <g transform="translate(420,168)">
      <circle cx="48" cy="32" r="30" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
      <circle cx="48" cy="24" r="10" fill="#F0C572"/><path d="M28,54 a20,17 0 0 1 40,0 Z" fill="#F0C572"/>
      <text x="48" y="88" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="110">Javier Montes</text>
      <text x="48" y="108" text-anchor="middle" font-size="12" fill="#79809A" data-fit="110">@javimontes</text>
    </g>
    <g transform="translate(536,168)">
      <circle cx="48" cy="32" r="30" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
      <circle cx="48" cy="24" r="10" fill="#C9A6EE"/><path d="M28,54 a20,17 0 0 1 40,0 Z" fill="#C9A6EE"/>
      <text x="48" y="88" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="110">Mariana Vale…</text>
      <text x="48" y="108" text-anchor="middle" font-size="12" fill="#79809A" data-fit="110">@marianav</text>
    </g>
    <g transform="translate(652,168)">
      <circle cx="48" cy="32" r="30" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/>
      <circle cx="48" cy="24" r="10" fill="#9FD68D"/><path d="M28,54 a20,17 0 0 1 40,0 Z" fill="#9FD68D"/>
      <text x="48" y="88" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="110">Camilo Díaz</text>
      <text x="48" y="108" text-anchor="middle" font-size="12" fill="#79809A" data-fit="110">@camilod</text>
    </g>
    <g transform="translate(768,168)">
      <circle cx="48" cy="32" r="30" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
      <circle cx="48" cy="24" r="10" fill="#A9B4F2"/><path d="M28,54 a20,17 0 0 1 40,0 Z" fill="#A9B4F2"/>
      <text x="48" y="88" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="110">Laura Gómez</text>
      <text x="48" y="108" text-anchor="middle" font-size="12" fill="#79809A" data-fit="110">@laurag</text>
    </g>
    <g transform="translate(884,168)">
      <circle cx="48" cy="32" r="30" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
      <circle cx="48" cy="24" r="10" fill="#86D3CA"/><path d="M28,54 a20,17 0 0 1 40,0 Z" fill="#86D3CA"/>
      <text x="48" y="88" text-anchor="middle" font-size="13" font-weight="700" fill="#161A26" data-fit="110">Pedro Cano</text>
      <text x="48" y="108" text-anchor="middle" font-size="12" fill="#79809A" data-fit="110">@pedroc</text>
    </g>
  </g>
  <path d="M844,146 H884 M876,140 L884,146 L876,152" fill="none" stroke="#79809A" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="832" y="146" dy="0.35em" text-anchor="end" font-size="12" fill="#79809A" data-fit="140">se desliza</text>
  <text class="foot" x="48" y="344" data-fit="860">Todas las tarjetas miden lo mismo de ancho, y un nombre que no cabe termina en puntos suspensivos.</text>
</svg>
```

**Archivo:** `lib/components/contact_card.dart` · **Clase:** `ContactCard`

| Parámetro | Tipo | Ejemplo |
|---|---|---|
| `imageUrl` | `String` | `'https://picsum.photos/400'` |
| `name` | `String` | `'Mariana Valenzuela'` |
| `username` | `String` | `'@marianav'` |

Compárala con el bloque de información de perfil: es la misma persona, contada con menos datos. Es normal que una app tenga dos componentes para lo mismo, uno de detalle y uno de resumen.

Por dentro es una `Column` con un `CircleAvatar` y dos `Text`. Lo nuevo es que tiene que funcionar **al lado de otras iguales**, y eso pide dos cuidados.

**Pista 1 · el ancho fijo.** Una `Column` mide lo que mide su hijo más ancho, así que cada tarjeta saldría de un ancho distinto según el nombre. Envuélvela en un `SizedBox` con `width` para que todas midan igual:

```dart
SizedBox(
  width: 96,
  child: Column(
    children: [
      CircleAvatar(
        radius: 30,
        backgroundImage: NetworkImage('https://picsum.photos/400'),
      ),
      SizedBox(height: 8),
      Text('Mariana Valenzuela'),
      Text('@marianav'),
    ],
  ),
)
```

**Pista 2 · el nombre largo.** Con el ancho fijo, un nombre largo ya no cabe en un renglón. Usa `maxLines: 1` y `overflow: TextOverflow.ellipsis` en los dos textos. Pruébala con *Mariana Valenzuela* y con *Ana*.

Para verla, pon tres o cuatro en una `Row` dentro de `HomeScreen`, con un `SizedBox(width: 12)` entre ellas. Si agregas tantas que no caben, aparece la franja amarilla y negra: es lo esperado. El deslizamiento horizontal es de la sesión 3, y tu componente no cambia cuando llegue.

## Qué debes tener al terminar

- Siete archivos en `lib/components/`: los seis del taller y `stat_card.dart`, cada uno con un componente y con la forma del apartado *Cómo trabajar*.
- Cada componente probado en `HomeScreen` con **al menos dos juegos de datos distintos**: otro nombre, un mensaje más largo, otro icono.
- El proyecto sin errores en el editor.

Si te alcanza el tiempo, prueba qué pasa con datos incómodos: un nombre muy largo, una descripción de cinco renglones, un número de seis cifras. Un componente que solo se ve bien con los datos del diseño todavía no está terminado.

Lo que no alcances en clase se termina por fuera: la sesión 3 empieza armando pantallas con estas seis piezas.
