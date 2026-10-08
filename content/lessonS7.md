# Entrega 1 · Contexto, base de datos y prototipo

<!-- tags: entrega 1, contexto del proyecto, modelo entidad relación, diagrama MER, llave primaria, llave foránea, cardinalidad, prototipo no funcional, Figma, Lovable, Stitch, galería de componentes, componentes reutilizables -->

Primera entrega del proyecto del equipo: el plano de la app antes de escribir código. Son **cuatro cosas**, en este orden, y cada una alimenta a la siguiente.

## Qué se entrega

1. **Contexto del proyecto.** Un párrafo corto (máximo 150 palabras): qué problema resuelve la app, para quién y qué puede hacer el usuario en ella.
2. **Modelo de base de datos.** El diagrama entidad-relación (MER) de la app.
3. **Prototipo no funcional.** Las pantallas de la app en **Figma**, **Lovable** o **Stitch** (la herramienta que el equipo prefiera). No tiene que funcionar: tiene que verse y mostrar el recorrido principal.
4. **Galería de componentes reutilizables.** Sale del prototipo del punto 3: los bloques de interfaz que se repiten en varias pantallas, mostrados juntos.

## El modelo de base de datos (MER)

Un diagrama MER muestra **qué datos guarda la app y cómo se relacionan**. Cada caja es una **entidad** (una futura tabla) y cada línea, una **relación**. Así se ve uno típico:

```svg
<svg id="erEjemplo" viewBox="0 0 960 440" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
<title id="erEjemplo-t">Ejemplo de diagrama entidad-relación</title>
<desc id="erEjemplo-d">Cuatro tablas de una biblioteca: categorias, libros, prestamos y usuarios, con relaciones uno a muchos.</desc>
<style>
#erEjemplo .mono{font-family:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace;font-size:13px;fill:#161A26}
#erEjemplo .nt{font-size:14px;font-weight:700}
#erEjemplo .lk{fill:none;stroke:#556074;stroke-width:1.75}
#erEjemplo .card{stroke-width:1.5}
#erEjemplo .bd{font-size:10.5px;font-weight:700;fill:#fff;letter-spacing:.04em}
#erEjemplo .card-t{font-size:13px;font-weight:700;fill:#161A26}
#erEjemplo .card-b{font-size:12px;fill:#454C61}
#erEjemplo .ca{font-size:13px;font-weight:700;fill:#556074}
</style>
<rect width="960" height="440" rx="16" fill="#FBFBFD"/>
<text x="32" y="44" font-size="20" font-weight="700" fill="#161A26">Ejemplo: biblioteca de préstamos</text>
<text x="32" y="66" font-size="13" fill="#79809A">Cada caja es una tabla; cada línea, una relación entre dos tablas.</text>
<g><rect class="card" x="32" y="88" width="176" height="152" rx="10" fill="#EEF1FF" stroke="#A9B4F2"/>
<path d="M32,120 H208" stroke="#A9B4F2" stroke-width="1.5"/>
<text class="nt mono" x="120" y="109" text-anchor="middle" fill="#4453C9" style="fill:#4453C9;font-size:14px">categorias</text>
<rect x="42" y="125" width="26" height="18" rx="9" fill="#4453C9"/><text class="bd" x="55" y="134" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="78" y="134" dy="0.35em">id</text>
<text class="mono" x="78" y="162" dy="0.35em">nombre</text>
<text class="mono" x="78" y="190" dy="0.35em">descripcion</text>
</g>
<g><rect class="card" x="272" y="88" width="176" height="152" rx="10" fill="#E3F6F3" stroke="#86D3CA"/>
<path d="M272,120 H448" stroke="#86D3CA" stroke-width="1.5"/>
<text class="nt mono" x="360" y="109" text-anchor="middle" fill="#0F8478" style="fill:#0F8478;font-size:14px">libros</text>
<rect x="282" y="125" width="26" height="18" rx="9" fill="#0F8478"/><text class="bd" x="295" y="134" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="318" y="134" dy="0.35em">id</text>
<text class="mono" x="318" y="162" dy="0.35em">titulo</text>
<text class="mono" x="318" y="190" dy="0.35em">autor</text>
<rect x="282" y="209" width="26" height="18" rx="9" fill="#556074"/><text class="bd" x="295" y="218" text-anchor="middle" dy="0.35em">FK</text>
<text class="mono" x="318" y="218" dy="0.35em">categoria_id</text>
</g>
<g><rect class="card" x="512" y="88" width="176" height="152" rx="10" fill="#FFF3DC" stroke="#F0C572"/>
<path d="M512,120 H688" stroke="#F0C572" stroke-width="1.5"/>
<text class="nt mono" x="600" y="109" text-anchor="middle" fill="#A96C05" style="fill:#A96C05;font-size:14px">prestamos</text>
<rect x="522" y="125" width="26" height="18" rx="9" fill="#A96C05"/><text class="bd" x="535" y="134" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="558" y="134" dy="0.35em">id</text>
<rect x="522" y="153" width="26" height="18" rx="9" fill="#556074"/><text class="bd" x="535" y="162" text-anchor="middle" dy="0.35em">FK</text>
<text class="mono" x="558" y="162" dy="0.35em">libro_id</text>
<rect x="522" y="181" width="26" height="18" rx="9" fill="#556074"/><text class="bd" x="535" y="190" text-anchor="middle" dy="0.35em">FK</text>
<text class="mono" x="558" y="190" dy="0.35em">usuario_id</text>
<text class="mono" x="558" y="218" dy="0.35em">fecha_prestamo</text>
</g>
<g><rect class="card" x="752" y="88" width="176" height="152" rx="10" fill="#F4EBFF" stroke="#C9A6EE"/>
<path d="M752,120 H928" stroke="#C9A6EE" stroke-width="1.5"/>
<text class="nt mono" x="840" y="109" text-anchor="middle" fill="#7439B8" style="fill:#7439B8;font-size:14px">usuarios</text>
<rect x="762" y="125" width="26" height="18" rx="9" fill="#7439B8"/><text class="bd" x="775" y="134" text-anchor="middle" dy="0.35em">PK</text>
<text class="mono" x="798" y="134" dy="0.35em">id</text>
<text class="mono" x="798" y="162" dy="0.35em">nombre</text>
<text class="mono" x="798" y="190" dy="0.35em">correo</text>
</g>
<path class="lk" d="M208,164 H272"/><path class="lk" d="M222,155 V173"/><path class="lk" d="M248,164 L272,153 M248,164 L272,164 M248,164 L272,175"/>
<path class="lk" d="M448,164 H512"/><path class="lk" d="M462,155 V173"/><path class="lk" d="M488,164 L512,153 M488,164 L512,164 M488,164 L512,175"/>
<path class="lk" d="M688,164 H752"/><path class="lk" d="M712,164 L688,153 M712,164 L688,164 M712,164 L688,175"/><path class="lk" d="M738,155 V173"/>
<text class="ca" x="220" y="146" text-anchor="middle">1</text>
<text class="ca" x="260" y="146" text-anchor="middle">N</text>
<text class="ca" x="460" y="146" text-anchor="middle">1</text>
<text class="ca" x="500" y="146" text-anchor="middle">N</text>
<text class="ca" x="700" y="146" text-anchor="middle">N</text>
<text class="ca" x="740" y="146" text-anchor="middle">1</text>
<rect class="card" x="32" y="280" width="288" height="112" rx="10" fill="#EEF1FF" stroke="#A9B4F2"/>
<text x="48" y="308" font-size="14" font-weight="700" fill="#4453C9">1  ·  Entidad = tabla</text>
<text class="card-b" x="48" y="332" data-fit="256">Cada caja es algo del que el</text>
<text class="card-b" x="48" y="352" data-fit="256">sistema guarda datos: libros,</text>
<text class="card-b" x="48" y="372" data-fit="256">usuarios…</text>
<rect class="card" x="336" y="280" width="288" height="112" rx="10" fill="#E3F6F3" stroke="#86D3CA"/>
<text x="352" y="308" font-size="14" font-weight="700" fill="#0F8478">2  ·  PK y FK</text>
<text class="card-b" x="352" y="332" data-fit="256">PK identifica cada fila. FK guarda</text>
<text class="card-b" x="352" y="352" data-fit="256">la PK de otra tabla y así se</text>
<text class="card-b" x="352" y="372" data-fit="256">enlazan.</text>
<rect class="card" x="640" y="280" width="288" height="112" rx="10" fill="#FFF3DC" stroke="#F0C572"/>
<text x="656" y="308" font-size="14" font-weight="700" fill="#A96C05">3  ·  Cardinalidad</text>
<text class="card-b" x="656" y="332" data-fit="256">1 = uno, N = muchos (la pata de</text>
<text class="card-b" x="656" y="352" data-fit="256">gallo). Un usuario tiene muchos</text>
<text class="card-b" x="656" y="372" data-fit="256">préstamos.</text>
<text x="32" y="420" font-size="12.5" fill="#79809A">Se lee así: una categoría tiene muchos libros · un libro se presta muchas veces · un usuario hace muchos préstamos.</text>
</svg>
```

Lo que tiene que traer el diagrama del equipo:

- Las **entidades** de la app, con sus **atributos** principales.
- La **llave primaria (PK)** de cada entidad.
- Las **llaves foráneas (FK)** que las enlazan.
- La **cardinalidad** de cada relación (1 a N, N a N…).

Basta con que el diagrama sea legible: puede hacerse en draw.io, dbdiagram.io, Figma o a mano y fotografiado.

## El prototipo y su galería de componentes

El prototipo cubre las pantallas del **recorrido principal** de la app (por ejemplo: entrar, ver la lista, abrir un detalle, crear algo). Los datos que se muestran en ellas deben tener sentido con el modelo de base de datos.

Con el prototipo terminado, identifiquen lo que se repite y armen una **galería de componentes**: una sola vista (una página de Figma, una pantalla aparte) con cada componente **una sola vez**, con nombre. Por ejemplo:

- Botones (principal y secundario).
- Campos de texto.
- Tarjetas de un elemento de la lista.
- Barra superior y barra de navegación.
- Cualquier componente propio de su app.

Si un componente cambia de aspecto (deshabilitado, con error, seleccionado), muestren **cada variante** junto a él. Esta galería es la lista de piezas que después van a programar como widgets.

## Cómo se entrega

Un solo envío por equipo con:

- El texto del contexto.
- La imagen del diagrama MER.
- El enlace al prototipo y a la galería de componentes, con permiso de lectura para el profesor.
