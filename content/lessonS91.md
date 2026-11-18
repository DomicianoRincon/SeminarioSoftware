# Supabase Storage: un bucket público

<!-- tags: Supabase Storage, bucket, bucket público, getPublicUrl, uploadBinary, policy de storage.objects, new row violates row-level security policy, la foto no se actualiza, caché de imágenes, nombre de archivo nuevo -->

La base de datos guarda filas: textos, números, fechas. Una foto no cabe en una fila. Para archivos está **Storage**: guarda bytes y entrega cada archivo por su propia URL. La tabla solo guarda la URL, y la app la sigue con `Image.network`.

## Bucket, ruta y URL

```svg
<svg id="fpRuta" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpRuta-ttl fpRuta-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpRuta-ttl">Bucket, ruta y URL</title>
  <desc id="fpRuta-dsc">Arriba, el bucket público avatars con una carpeta por usuario, 3f9a1c27, y dentro dos fotos con nombre de milisegundos. En el medio, la URL pública partida en cinco tramos de colores: el proyecto, la parte object/public que permite leer sin sesión, el bucket, la carpeta con el id del usuario y el nombre del archivo. Abajo, la fila de profiles de Ana con avatar_url igual a esa URL.</desc>
  <defs>
    <style>
      #fpRuta .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpRuta .sub{fill:#79809A;font-size:13.5px}
      #fpRuta .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #fpRuta .nt{font-size:15px;font-weight:700;fill:#161A26}
      #fpRuta .nb{fill:#454C61;font-size:13px}
      #fpRuta .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fpRuta .foot{fill:#79809A;font-size:12px}
      #fpRuta .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpRuta .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fpRuta-arrow)}
    </style>
    <marker id="fpRuta-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="540" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Bucket, ruta y URL</text>
  <text class="sub" x="48" y="80" data-fit="860">El archivo vive en el bucket. El perfil guarda la URL pública para encontrarlo.</text>
<g><rect x="48" y="116" width="864" height="120" rx="12" fill="#FFF3DC" stroke="#F0C572" stroke-width="1.5"/></g><text x="68" y="146" font-size="12" font-weight="700" fill="#556074" text-anchor="start" data-fit="131">Storage · bucket</text><text x="196" y="146" font-size="13.5" font-weight="700" fill="#A96C05" text-anchor="start" class="mono" data-fit="80">avatars</text><rect x="265.5" y="129" width="69.0" height="24" rx="12" fill="#A96C05" stroke="#A96C05" stroke-width="1.2"/><text x="300" y="145.5" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="71">público</text><path d="M80,172 h7 l3,3 h10 v13 h-20 Z" fill="#F0C572" stroke="#A96C05" stroke-width="1.2"/><text x="108" y="185" font-size="13" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="109">3f9a1c27-…/</text><rect x="300" y="170" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="324" y="184" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="156">1763481200000.jpg</text><rect x="540" y="170" width="15" height="18" rx="2" fill="#FFFFFF" stroke="#79809A" stroke-width="1.2"/><text x="564" y="184" font-size="13" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="156">1763494511000.jpg</text><text x="68" y="218" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="820">Una carpeta por usuario. Cada foto con un nombre nuevo: el momento en que se subió.</text><rect x="48" y="272" width="316.0" height="30" rx="4" fill="#EFF1F5" stroke="#C4CBD8"/><text x="52" y="292" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="312">https://abcdefghijklmnopqrst.supabase.co</text><text x="206.0" y="324" font-size="12" font-weight="600" fill="#556074" text-anchor="middle" data-fit="316.0">tu proyecto</text><rect x="364.0" y="272" width="208.2" height="30" rx="4" fill="#E8F6E3" stroke="#9FD68D"/><text x="368.0" y="292" font-size="12" font-weight="700" fill="#3A8235" text-anchor="start" class="mono" data-fit="211">/storage/v1/object/public/</text><text x="468.1" y="324" font-size="12" font-weight="600" fill="#3A8235" text-anchor="middle" data-fit="208.20000000000002">se lee sin sesión</text><rect x="572.2" y="272" width="61.9" height="30" rx="4" fill="#FFF3DC" stroke="#F0C572"/><text x="576.2" y="292" font-size="12" font-weight="700" fill="#A96C05" text-anchor="start" class="mono" data-fit="74">avatars</text><text x="603.1500000000001" y="324" font-size="12" font-weight="600" fill="#A96C05" text-anchor="middle" data-fit="90">el bucket</text><rect x="634.1" y="272" width="100.4" height="30" rx="4" fill="#F4EBFF" stroke="#C9A6EE"/><text x="638.1" y="292" font-size="12" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="110">/3f9a1c27-…/</text><text x="684.3000000000001" y="324" font-size="12" font-weight="600" fill="#7439B8" text-anchor="middle" data-fit="100.4">id del usuario</text><rect x="734.5" y="272" width="138.9" height="30" rx="4" fill="#EEF1FF" stroke="#A9B4F2"/><text x="738.5" y="292" font-size="12" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="146">1763494511000.jpg</text><text x="803.95" y="324" font-size="12" font-weight="600" fill="#4453C9" text-anchor="middle" data-fit="138.9">el archivo</text><text x="48" y="262" font-size="12.5" font-weight="600" fill="#454C61" text-anchor="start" data-fit="860">getPublicUrl(ruta) arma la URL. No va a internet: solo junta texto.</text><rect x="48" y="356" width="864" height="108" rx="12" fill="#FFFFFF" stroke="#A9B4F2" stroke-width="1.5"/><path d="M48,368 A12,12 0 0 1 60,356 H900 A12,12 0 0 1 912,368 V392 H48 Z" fill="#EEF1FF"/><text x="62" y="380" font-size="13.5" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="844">profiles</text><text x="900" y="380" font-size="12" font-weight="400" fill="#556074" text-anchor="end" data-fit="432.0">la columna nueva</text><text x="62" y="418" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="122">id</text><text x="192" y="418" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="82">name</text><text x="282" y="418" font-size="12" font-weight="700" fill="#556074" text-anchor="start" class="mono" data-fit="636">avatar_url</text><line x1="58" y1="427" x2="902" y2="427" stroke="#C4CBD8"/><text x="62" y="446" font-size="12" font-weight="700" fill="#7439B8" text-anchor="start" class="mono" data-fit="122">3f9a1c27-…</text><text x="192" y="446" font-size="12" font-weight="400" fill="#161A26" text-anchor="start" class="mono" data-fit="82">Ana</text><text x="282" y="446" font-size="12" font-weight="700" fill="#4453C9" text-anchor="start" class="mono" data-fit="636">https://…/object/public/avatars/3f9a1c27-…/1763494511000.jpg</text><text x="48" y="512" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Bucket público: cualquiera con la URL ve la foto. Para subir hace falta una policy, aunque sea público.</text></svg>
```

- Un **bucket** es un contenedor de archivos con sus propias reglas, como una tabla lo es de filas.
- Cada archivo tiene una **ruta**: carpetas y nombre. En la app de tracks, la carpeta es el id del usuario y el nombre es el momento en que se subió.
- En un bucket **público**, la URL es fija y cualquiera que la tenga ve el archivo, sin sesión. Sirve para lo que igual se muestra a todos, como una foto de perfil.

## Público no es «cualquiera sube»

Público solo cubre **leer** por la URL. Subir, listar o borrar siempre pasa por las **policies** de la tabla `storage.objects`, aunque la app no use RLS en sus propias tablas. Sin una policy de `INSERT`, la subida falla con:

```text
new row violates row-level security policy
```

En el taller creas dos: `INSERT` para subir y `SELECT` para listar el historial.

## Un nombre nuevo en cada subida

```svg
<svg id="fpMismoNombre" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 470" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="fpMismoNombre-ttl fpMismoNombre-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="fpMismoNombre-ttl">Por qué cada foto lleva un nombre nuevo</title>
  <desc id="fpMismoNombre-dsc">Dos columnas. A la izquierda, en rojo, el mismo nombre avatar.jpg: se sube la foto nueva encima de la vieja, la URL no cambia, y Image.network, el navegador y el CDN responden con la foto vieja que ya tenían. A la derecha, en verde, un nombre por subida: la URL es nueva, ninguna caché la tiene y se descarga la foto nueva; las fotos anteriores siguen en el bucket y son el historial.</desc>
  <defs>
    <style>
      #fpMismoNombre .title{fill:#161A26;font-size:22px;font-weight:700}
      #fpMismoNombre .sub{fill:#79809A;font-size:13.5px}
      #fpMismoNombre .h{font-size:12px;font-weight:700;letter-spacing:.08em;fill:#556074}
      #fpMismoNombre .nt{font-size:15px;font-weight:700;fill:#161A26}
      #fpMismoNombre .nb{fill:#454C61;font-size:13px}
      #fpMismoNombre .lbl{fill:#556074;font-size:12px;font-weight:600}
      #fpMismoNombre .foot{fill:#79809A;font-size:12px}
      #fpMismoNombre .mono{font-family:ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace}
      #fpMismoNombre .link{fill:none;stroke:#556074;stroke-width:1.75;marker-end:url(#fpMismoNombre-arrow)}
    </style>
    <marker id="fpMismoNombre-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
  </defs>
  <rect width="960" height="470" rx="16" fill="#FBFBFD"/>
  <text class="title" x="48" y="56">Por qué cada foto lleva un nombre nuevo</text>
  <text class="sub" x="48" y="80" data-fit="860">Las cachés guardan la imagen por su URL. Una URL nueva no la tiene nadie.</text>
<g><rect x="48" y="120" width="416" height="250" rx="12" fill="#FFEBEF" stroke="#F3A3B2" stroke-width="1.5"/><text x="64" y="152" font-size="14.5" font-weight="700" fill="#C2354F" text-anchor="start" data-fit="392">Mismo nombre</text></g><text x="64" y="182" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="384">avatars/3f9a…/avatar.jpg</text><text x="64" y="222" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="384">Subes la foto nueva encima de la vieja.</text><text x="64" y="248" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="384">La URL es la misma de antes.</text><text x="64" y="274" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="384">Image.network, el navegador y el CDN</text><text x="64" y="300" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="384">ya la tienen guardada: muestran la vieja.</text><rect x="187.9" y="386" width="136.2" height="24" rx="12" fill="#C2354F" stroke="#C2354F" stroke-width="1.2"/><text x="256" y="402.5" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="138">la foto no cambia</text><g><rect x="496" y="120" width="416" height="250" rx="12" fill="#E8F6E3" stroke="#9FD68D" stroke-width="1.5"/><text x="512" y="152" font-size="14.5" font-weight="700" fill="#3A8235" text-anchor="start" data-fit="392">Un nombre por subida</text></g><text x="512" y="182" font-size="12.5" font-weight="700" fill="#161A26" text-anchor="start" class="mono" data-fit="384">avatars/3f9a…/1763494511000.jpg</text><text x="512" y="222" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="384">Subes con el momento como nombre.</text><text x="512" y="248" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="384">La URL es nueva: nadie la tiene.</text><text x="512" y="274" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="384">Se descarga la foto nueva.</text><text x="512" y="300" font-size="12.5" font-weight="400" fill="#454C61" text-anchor="start" data-fit="384">Las anteriores siguen ahí: son el historial.</text><rect x="592.2" y="386" width="223.6" height="24" rx="12" fill="#3A8235" stroke="#3A8235" stroke-width="1.2"/><text x="704" y="402.5" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle" data-fit="225">la foto cambia y hay historial</text><text x="48" y="442" font-size="12" font-weight="400" fill="#79809A" text-anchor="start" data-fit="864">Por eso el taller nunca usa upsert ni borra archivos: cada subida es un archivo nuevo.</text></svg>
```

`Image.network`, el navegador y el CDN de Supabase guardan cada imagen por su URL. Si la foto nueva se sube con el mismo nombre, la URL no cambia y todos siguen mostrando la vieja. Con un nombre nuevo, la URL es nueva y nadie la tiene guardada. Y como nada se borra, las fotos anteriores quedan como historial.

## Las dos llamadas

```dart
final path = '$userId/${DateTime.now().millisecondsSinceEpoch}.jpg';
await _client.storage
    .from('avatars')
    .uploadBinary(
      path,
      bytes,
      fileOptions: const FileOptions(contentType: 'image/jpeg'),
    );
final url = _client.storage.from('avatars').getPublicUrl(path);
```

`uploadBinary` sube los bytes de la foto y lleva `await`. `getPublicUrl` no va a internet: solo arma la URL con la ruta. Este código no lo escribes tú: es lo que la spec técnica le pide al implementador, y es bueno reconocerlo cuando lo revises.
