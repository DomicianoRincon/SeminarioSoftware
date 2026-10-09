# Modelo de datos

## sedes

- id (PK)
- nombre
- direccion

## deportes

- id (PK)
- nombre

## canchas

- id (PK)
- nombre
- precio_hora
- sede_id (FK a sedes)
- deporte_id (FK a deportes)

## usuarios

- id (PK)
- nombre
- correo
- telefono

## reservas

- id (PK)
- cancha_id (FK a canchas)
- usuario_id (FK a usuarios)
- fecha
- hora_inicio

## pagos

- id (PK)
- reserva_id (FK a reservas)
- valor
- metodo

## Relaciones

- Una sede tiene muchas canchas.
- Un deporte tiene muchas canchas.
- Una cancha tiene muchas reservas.
- Un usuario tiene muchas reservas.
- Una reserva tiene muchos pagos.
