# Qué va en una spec funcional

## Sí va

- Quién la usa y para qué.
- El flujo principal, en pasos numerados, y los flujos alternos.
- Las reglas del negocio: límites, condiciones, quién puede qué.
- Los estados que ve el usuario: cargando, vacío y error.
- Los datos, con las palabras del usuario.
- Criterios de aceptación que se puedan comprobar.
- Lo que queda fuera de alcance y las preguntas abiertas.

## No va

- Código, nombres de widgets, cómo se guarda el estado.
- Tablas, columnas, SQL, nombres de servicios o paquetes.
- Colores, tamaños y posiciones: eso es del prototipo.
- Tareas de implementación: eso es del plan.
- Palabras vagas: fácil, rápido, intuitivo, etc., algunos, adecuado.

## Criterios de aceptación

Forma: **Dado** una situación, **cuando** el usuario hace algo, **entonces** pasa algo que se ve.

- Bien: Dado que no hay conexión, cuando el usuario publica, entonces ve "No se pudo publicar" y su texto se conserva.
- Mal: "La publicación funciona bien".

Al menos uno por flujo y uno por estado de error.

Si el equipo los prefiere en Gherkin, usa sus palabras en español dentro de un bloque `gherkin`:
`Escenario`, `Dado`, `Cuando`, `Entonces`, `Y`. Un escenario por criterio.

## Versiones

- `0.x.y` mientras está en borrador. `1.0.0` cuando el equipo la aprueba.
- Mayor: cambia el comportamiento. Menor: se agrega algo. Parche: solo redacción.

## Estados

`borrador` → `aprobada` → `implementada`. Una que ya no aplica pasa a `obsoleta`.
