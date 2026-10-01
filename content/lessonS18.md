# Taller · Componentes

<!-- tags: taller de componentes, botón con icono y texto, OutlinedButton.styleFrom, CircleAvatar, Expanded, RenderFlex overflowed on the right, ElevatedButton.styleFrom, IconData como parámetro, foto circular, lib/components -->

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

La prueba de que un componente está bien hecho: **ningún texto, icono ni imagen del diseño está escrito dentro de él**. Todo lo que cambia entre un uso y otro llega por el constructor.

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

## 2. Indicador numérico

Un número grande con su etiqueta debajo, como el contador de publicaciones o de seguidores de un perfil.

![Indicador numérico](Lab1Item3.png "frame60")

**Archivo:** `lib/components/stat_card.dart` · **Clase:** `StatCard`

| Parámetro | Tipo | Ejemplo |
|---|---|---|
| `number` | `String` | `'248'` |
| `label` | `String` | `'Posts'` |

Es el `StatCard` de la lección anterior. Si ya lo tienes, ajusta tamaños y colores hasta que se vea como el diseño.

## 3. Elemento de conversación

La fila de un chat: la foto del contacto, su nombre, la hora del último mensaje, el inicio de ese mensaje y el icono de leído.

![Elemento de conversación](Lab1Item1.png "frame60")

**Archivo:** `lib/components/chat_item.dart` · **Clase:** `ChatItem`

| Parámetro | Tipo | Ejemplo |
|---|---|---|
| `imageUrl` | `String` | `'https://i.pravatar.cc/150?img=12'` |
| `name` | `String` | `'Javier Montes'` |
| `time` | `String` | `'10:24 a.m.'` |
| `message` | `String` | `'¿Te parece si revisamos los avances?'` |

Antes de escribir, parte el diseño en cajas: es una `Row` con tres hijos, la foto, una `Column` con los dos textos y otra `Column` con la hora y el icono.

**Pista 1 · la foto circular.** No uses una imagen ya recortada. `CircleAvatar` recorta en círculo cualquier imagen:

```dart
CircleAvatar(
  radius: 28,
  backgroundImage: NetworkImage('https://i.pravatar.cc/150?img=12'),
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
| `imageUrl` | `String` | `'https://i.pravatar.cc/300?img=47'` |
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

## 5. Campo de formulario

El campo de las pantallas de inicio de sesión y de registro: una etiqueta, un icono a la derecha y una línea debajo.

```svg
<svg id="tlCampo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 300" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tlCampo-ttl tlCampo-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tlCampo-ttl">Campo de formulario</title>
  <desc id="tlCampo-dsc">El componente campo de formulario usado dos veces: uno con la etiqueta Correo electrónico y un icono de sobre, y otro con la etiqueta Contraseña y un icono de candado. Cada uno es una etiqueta a la izquierda, un icono a la derecha y una línea debajo.</desc>
  <defs>
    <style>
      #tlCampo .title{fill:#161A26;font-size:22px;font-weight:700}
      #tlCampo .sub{fill:#79809A;font-size:13.5px}
      #tlCampo .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #tlCampo .nt{font-size:15px;font-weight:700;fill:#161A26}
      #tlCampo .nb{fill:#454C61;font-size:13px}
      #tlCampo .lbl{fill:#556074;font-size:12px;font-weight:600}
      #tlCampo .foot{fill:#79809A;font-size:12px}
      #tlCampo .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #tlCampo .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#tlCampo-arrow)}
    </style>
    <marker id="tlCampo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="300" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Campo de formulario</text>
  <text class="sub" x="48" y="80" data-fit="860">El mismo componente, usado dos veces. Cambian la etiqueta, el icono y si oculta lo que se escribe.</text>
  <g transform="translate(48,112)">
    <rect width="408" height="100" rx="12" fill="#F4E1E6"/>
    <text x="24" y="50" dy="0.35em" font-size="16" fill="#161A26" data-fit="300">Correo electrónico</text>
    <g transform="translate(368,50)"><rect x="-9" y="-7" width="18" height="14" rx="2" fill="none" stroke="#161A26" stroke-width="1.75"/><path d="M-9,-6 L0,1 L9,-6" fill="none" stroke="#161A26" stroke-width="1.75"/></g>
    <path d="M24,76 H384" stroke="#454C61" stroke-width="1.5"/>
    <text class="mono" x="0" y="128" font-size="12" fill="#556074" data-fit="408">label: 'Correo electrónico'</text>
    <text class="mono" x="0" y="148" font-size="12" fill="#556074" data-fit="408">icon: Icons.mail_outline</text>
  </g>
  <g transform="translate(504,112)">
    <rect width="408" height="100" rx="12" fill="#F4E1E6"/>
    <text x="24" y="50" dy="0.35em" font-size="16" fill="#161A26" data-fit="300">Contraseña</text>
    <g transform="translate(368,50)"><rect x="-8" y="-2" width="16" height="12" rx="2" fill="none" stroke="#161A26" stroke-width="1.75"/><path d="M-5,-2 V-6 a5,5 0 0 1 10,0 V-2" fill="none" stroke="#161A26" stroke-width="1.75"/></g>
    <path d="M24,76 H384" stroke="#454C61" stroke-width="1.5"/>
    <text class="mono" x="0" y="128" font-size="12" fill="#556074" data-fit="408">label: 'Contraseña'</text>
    <text class="mono" x="0" y="148" font-size="12" fill="#556074" data-fit="408">icon: Icons.lock_outline · obscure: true</text>
  </g>
</svg>
```

**Archivo:** `lib/components/login_field.dart` · **Clase:** `LoginField`

| Parámetro | Tipo | Ejemplo |
|---|---|---|
| `label` | `String` | `'Correo electrónico'` |
| `icon` | `IconData` | `Icons.mail_outline` |
| `obscure` | `bool` | `true` para la contraseña |

Es un `TextField` con su `InputDecoration`: la etiqueta va en `labelText` y el icono en `suffixIcon`. La línea de abajo es el borde que el campo trae por defecto, así que no hay que pedirla.

Una cosa nueva en el constructor: **un parámetro con valor por defecto**. La mayoría de los campos no ocultan el texto, así que `obscure` no es `required`. En el constructor se escribe `this.obscure = false`, y solo el campo de contraseña lo pasa.

Este componente todavía no puede entregar lo que la persona escribe. Lo completas en la sesión 6, cuando veas estado.

## Qué debes tener al terminar

- Seis archivos en `lib/components/`, cada uno con un componente y con la forma del apartado *Cómo trabajar*.
- Cada componente probado en `HomeScreen` con **al menos dos juegos de datos distintos**: otro nombre, un mensaje más largo, otra etiqueta, otro icono.
- El proyecto sin errores en el editor.

Si te alcanza el tiempo, prueba qué pasa con datos incómodos: un nombre muy largo, una descripción de cinco renglones, un número de seis cifras. Un componente que solo se ve bien con los datos del diseño todavía no está terminado.

Lo que no alcances en clase se termina por fuera: la sesión 3 empieza armando pantallas con estas seis piezas.
