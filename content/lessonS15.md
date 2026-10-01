# StatelessWidget: tu primer componente

<!-- tags: StatelessWidget, crear un componente, parámetros con nombre, required, widget reutilizable, método build, campos final, lib/components, const en el constructor, The named parameter is required -->

Ya conoces los widgets básicos de Flutter y sabes acomodarlos con `Column` y `Row`. Con ellos se puede armar una pantalla entera, pero el código se vuelve largo y repetido muy rápido. La salida es hacer tus propios widgets: **componentes**.

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
import '../components/stat_card.dart';

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

En el *Taller · Componentes* construyes cinco. Los necesitas terminados para la sesión 3, donde se arman las pantallas con ellos.
