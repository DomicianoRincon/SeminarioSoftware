# Normalización hasta 3FN

El ejemplo es una tabla de canciones de una playlist. Así llega del borrador:

- canciones: id, titulo, artista, pais_artista, generos, playlist, duenio_playlist

## 1FN · Un solo valor por celda

**Regla:** cada atributo guarda un único valor y no hay grupos que se repiten.

- **Se rompe** si `generos` guarda "rock, pop". Tampoco sirve tener `genero1`, `genero2` y `genero3`.
- **Arreglo:** el valor múltiple sale a su propia tabla. Como un género tiene muchas canciones, se crean `generos` y la tabla intermedia `canciones_generos`.

## 2FN · Todo depende de la llave entera

**Regla:** se cumple 1FN, y cuando la llave tiene dos partes, cada atributo depende de las dos.

- **Se rompe** en `playlists_canciones` (playlist_id, cancion_id, nombre_playlist, fecha_agregada). `nombre_playlist` depende solo de `playlist_id`.
- **Arreglo:** `nombre_playlist` se mueve a `playlists`. En la intermedia queda lo que depende del par, que es `fecha_agregada`.
- Con un `id` simple como llave, la 2FN se cumple sola. Revísala igual en las tablas intermedias.

## 3FN · Nada depende de otro atributo que no es llave

**Regla:** se cumple 2FN, y ningún atributo depende de otro atributo que no sea la llave.

- **Se rompe** en `canciones` con `artista` y `pais_artista`. El país depende del artista, no de la canción: si el artista tiene diez canciones, su país se repite diez veces y puede quedar distinto en una.
- **Arreglo:** se crea `artistas` (id, nombre, pais). En `canciones` queda `artista_id (FK a artistas)`.
- **Pista:** si al cambiar un dato hay que cambiarlo en muchas filas, casi siempre rompe 3FN.

## Resultado del ejemplo

- artistas: id, nombre, pais
- canciones: id, titulo, artista_id
- generos: id, nombre
- canciones_generos: id, cancion_id, genero_id
- usuarios: id, nombre
- playlists: id, nombre, usuario_id
- playlists_canciones: id, playlist_id, cancion_id, fecha_agregada
