# Modelo de datos

## artistas

- id (PK)
- nombre
- pais

## canciones

- id (PK)
- titulo
- artista_id (FK a artistas)

## playlists

- id (PK)
- nombre
- creada_en

## playlists_canciones

- id (PK)
- playlist_id (FK a playlists)
- cancion_id (FK a canciones)
- fecha_agregada

## Relaciones

- Un artista tiene muchas canciones.
- Una playlist tiene muchas canciones, y una canción está en muchas playlists, a través de playlists_canciones.
