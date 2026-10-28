# Skills para tu proyecto

<!-- tags: skill, .agents/skills, disenador-bd, tercera forma normal 3FN, normalización, mer-svg, flutter-componentes, flutter-pantallas, la skill no se carga, SKILL.md, docs/modelo.md, el agente no usa la skill -->

En la sesión 4 viste qué es una [skill](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0031) y armaste dos. Aquí tienes cuatro listas para llevar a tu proyecto: dos para la base de datos y dos para la app. Instálalas una vez y pídele las cosas al agente con tus palabras.

## Las cuatro skills

```svg
<svg id="iaSkillsMapa" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 492" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="iaSkillsMapa-ttl iaSkillsMapa-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="iaSkillsMapa-ttl">Las cuatro skills y lo que deja cada una</title>
  <desc id="iaSkillsMapa-dsc">Dos filas. Arriba, la base de datos: disenador-bd te entrevista y deja docs/modelo.md en tercera forma normal; mer-svg lo lee y dibuja docs/mer.svg. Abajo, la app: flutter-pantallas maqueta pantallas estáticas en lib/screens/, y flutter-componentes crea componentes con datos, eventos y el estado en la Screen, en lib/components/.</desc>
  <defs>
    <style>
      #iaSkillsMapa .title{fill:#161A26;font-size:22px;font-weight:700}
      #iaSkillsMapa .sub{fill:#79809A;font-size:13.5px}
      #iaSkillsMapa .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #iaSkillsMapa .nb{fill:#454C61;font-size:13px}
      #iaSkillsMapa .lbl{fill:#556074;font-size:12px;font-weight:600}
      #iaSkillsMapa .foot{fill:#79809A;font-size:12px}
      #iaSkillsMapa .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #iaSkillsMapa .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#iaSkillsMapa-arrow)}
    </style>
    <marker id="iaSkillsMapa-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="492" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Las cuatro skills y lo que deja cada una</text>
  <text class="sub" x="48" y="80">Cada fila va en orden: lo que deja la primera skill es lo que usa la segunda.</text>
  <text class="h" x="48" y="128">LA BASE DE DATOS · TRABAJAN SOBRE docs/</text>
  <rect x="48" y="140" width="200" height="100" rx="14" fill="#EEF1FF" stroke="#A9B4F2" stroke-width="1.5"/>
  <text class="mono" x="64" y="170" font-size="15" font-weight="700" fill="#4453C9">disenador-bd</text>
  <text class="nb" x="64" y="196">Te entrevista y lleva</text>
  <text class="nb" x="64" y="216">el modelo hasta 3FN.</text>
  <path class="link" d="M248,190 H294"/>
  <rect x="296" y="170" width="160" height="40" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>
  <text class="mono" x="376" y="190" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" text-anchor="middle">docs/modelo.md</text>
  <text class="lbl" x="376" y="230" text-anchor="middle">las tablas, en 3FN</text>
  <path class="link" d="M456,190 H502"/>
  <rect x="504" y="140" width="200" height="100" rx="14" fill="#E3F6F3" stroke="#86D3CA" stroke-width="1.5"/>
  <text class="mono" x="520" y="170" font-size="15" font-weight="700" fill="#0F8478">mer-svg</text>
  <text class="nb" x="520" y="196">Dibuja el modelo como</text>
  <text class="nb" x="520" y="216">diagrama en SVG.</text>
  <path class="link" d="M704,190 H750"/>
  <rect x="752" y="170" width="160" height="40" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>
  <text class="mono" x="832" y="190" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" text-anchor="middle">docs/mer.svg</text>
  <text class="lbl" x="832" y="230" text-anchor="middle">el diagrama MER</text>
  <text class="h" x="48" y="300">LA APP · TRABAJAN SOBRE lib/</text>
  <rect x="48" y="312" width="200" height="100" rx="14" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/>
  <text class="mono" x="64" y="342" font-size="15" font-weight="700" fill="#A96C05">flutter-pantallas</text>
  <text class="nb" x="64" y="368">Maqueta pantallas</text>
  <text class="nb" x="64" y="388">estáticas.</text>
  <path class="link" d="M248,362 H294"/>
  <rect x="296" y="342" width="160" height="40" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>
  <text class="mono" x="376" y="362" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" text-anchor="middle">lib/screens/</text>
  <text class="lbl" x="376" y="402" text-anchor="middle">el prototipo</text>
  <path class="link" d="M456,362 H502"/>
  <rect x="504" y="312" width="200" height="100" rx="14" fill="#F4EBFF" stroke="#C9A6EE" stroke-width="1.5"/>
  <text class="mono" x="520" y="342" font-size="15" font-weight="700" fill="#7439B8">flutter-componentes</text>
  <text class="nb" x="520" y="368">Datos, eventos y</text>
  <text class="nb" x="520" y="388">estado en la Screen.</text>
  <path class="link" d="M704,362 H750"/>
  <rect x="752" y="342" width="160" height="40" rx="10" fill="#FFFFFF" stroke="#C4CBD8" stroke-width="1.5"/>
  <text class="mono" x="832" y="362" dy="0.35em" font-size="13" font-weight="700" fill="#161A26" text-anchor="middle">lib/components/</text>
  <text class="lbl" x="832" y="402" text-anchor="middle">con estado y eventos</text>
  <text class="foot" x="48" y="464">Cada skill es una carpeta en .agents/skills/ del proyecto. El agente la carga cuando tu pedido coincide con su description.</text>
</svg>
```

- **`disenador-bd`** te hace preguntas sobre la app antes de proponer tablas. Después normaliza el modelo de a una forma normal, hasta la tercera, y en cada paso te muestra qué cambió y por qué.
- **`mer-svg`** es la del *Taller · Tu primera skill*: dibuja `docs/modelo.md` como un diagrama entidad-relación.
- **`flutter-pantallas`** es la de *Una skill para armar pantallas*: maqueta pantallas sin estado ni navegación, con los widgets que has visto.
- **`flutter-componentes`** sigue lo que viste de la sesión 6 a la 8: la Screen guarda el estado, el componente recibe sus datos por el constructor y avisa con `Function()`, y solo la Screen navega.

## Instálalas

Crea las carpetas desde la raíz del proyecto. En macOS, Linux o Git Bash:

```shell
mkdir -p .agents/skills/disenador-bd/references .agents/skills/disenador-bd/assets
mkdir -p .agents/skills/mer-svg/references .agents/skills/mer-svg/assets
mkdir -p .agents/skills/flutter-pantallas/references
mkdir -p .agents/skills/flutter-pantallas/assets
mkdir -p .agents/skills/flutter-componentes/references
mkdir -p .agents/skills/flutter-componentes/assets
```

En PowerShell, `mkdir` también crea las carpetas intermedias: usa las mismas líneas sin `-p`.

```interactive
skill-files
```

Elige una pestaña y recorre sus archivos. Por cada uno, crea un archivo con ese nombre en esa carpeta, pulsa **Copiar** y pega el contenido. Empieza siempre por `SKILL.md`.

Si ya tienes `mer-svg` y `flutter-pantallas` de la sesión 4, solo reemplaza el `SKILL.md` de `flutter-pantallas`. Su description ya no habla de componentes, para que esos pedidos le lleguen a `flutter-componentes`.

## Úsalas en orden

Cierra el agente si estaba abierto y ábrelo de nuevo en la raíz del proyecto, para que encuentre las skills. Pide las cosas sin nombrar la skill: si la description está bien escrita, el agente elige la correcta.

1. **Diseña la base de datos.** Pide «Ayúdame a diseñar la base de datos de mi app» y responde lo que te pregunte. Antes de pasar a la siguiente forma normal te muestra qué regla se rompe, con un ejemplo, y espera tu visto bueno. Si no entiendes un cambio, pregúntale: no lo aceptes a ciegas.
2. **Dibújala.** Pide «Dibuja el MER de la app». El dibujo sale de `docs/modelo.md`, así que muestra el modelo ya normalizado.
3. **Maqueta las pantallas.** Pide «Maqueta la pantalla de perfil». Sale estática: los botones no hacen nada todavía.
4. **Dale vida.** Pide «Saca la tarjeta de producto a un componente» o «Haz que tocar la card abra el detalle». `flutter-componentes` pone el estado en la Screen y le pasa las funciones al componente.

Las plantillas de `flutter-componentes` son de una lista de compras y usan el paquete `my_app`. El agente las cambia por tu dominio y por el `name` de tu `pubspec.yaml`.

## Si el agente no usa la skill

- **El nombre no coincide.** La carpeta y el `name` del `SKILL.md` deben ser iguales, en minúsculas y con guiones: `disenador-bd`, sin ñ.
- **No reiniciaste el agente.** Las skills se buscan al abrirlo.
- **La description no tiene tus palabras.** Si pides «normaliza mis tablas» y la description no dice normalizar, el agente no las relaciona. Agrégale las palabras con las que lo pides.
- **Usó la que no era.** Si una pantalla sale con estado o una card sale sin funciones, di cuál skill quieres: «usa la skill flutter-componentes».
