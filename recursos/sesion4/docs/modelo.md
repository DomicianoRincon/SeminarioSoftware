# Modelo de datos

## usuarios

- id (PK)
- nombre
- usuario
- cargo
- correo
- ciudad
- foto_url

## publicaciones

- id (PK)
- usuario_id (FK a usuarios)
- texto
- fecha

## seguidores

- id (PK)
- seguidor_id (FK a usuarios)
- seguido_id (FK a usuarios)

## mensajes

- id (PK)
- emisor_id (FK a usuarios)
- receptor_id (FK a usuarios)
- texto
- hora

## Relaciones

- Un usuario tiene muchas publicaciones.
- Un usuario tiene muchos seguidores.
- Un usuario tiene muchos mensajes.
