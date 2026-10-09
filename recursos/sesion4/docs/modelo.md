# Modelo de datos

## categorias

- id (PK)
- nombre
- descripcion

## libros

- id (PK)
- titulo
- autor
- categoria_id (FK a categorias)

## usuarios

- id (PK)
- nombre
- correo

## prestamos

- id (PK)
- libro_id (FK a libros)
- usuario_id (FK a usuarios)
- fecha_prestamo

## Relaciones

- Una categoria tiene muchos libros.
- Un libro tiene muchos prestamos.
- Un usuario tiene muchos prestamos.
