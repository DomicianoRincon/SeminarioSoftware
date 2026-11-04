# Cómo se escribe un requisito

## Funcional (RF)

Dice algo que el sistema hace. Forma: *El sistema debe permitir que el <usuario> <acción>.*

- Bien: `RF-04` El sistema debe permitir que el usuario siga a otro usuario. (O-02)
- Mal: "Que se pueda seguir gente fácilmente". No dice quién ni qué, y "fácilmente" no se comprueba.

## No funcional (RNF)

Dice cómo de bien lo hace. Siempre con un número o una condición que se pueda revisar.

- Bien: `RNF-02` El feed muestra las primeras publicaciones en menos de 2 segundos con wifi.
- Mal: "La app debe ser rápida".

Categorías que suelen aparecer:

- Plataformas: en qué dispositivos o navegadores funciona.
- Rendimiento: tiempos de carga, tamaño máximo de un archivo.
- Usabilidad: cuántos pasos toma una tarea, idioma de la interfaz.
- Disponibilidad y datos: qué pasa sin conexión, qué se guarda y por cuánto tiempo.

## Palabras que delatan un requisito vago

fácil, rápido, intuitivo, amigable, moderno, etc., y/o, varios, algunos, adecuado, mejor.
Si aparece una, pide un número o un ejemplo.

## Una prueba rápida

Pregúntate: *¿cómo demostraría en la entrega que esto se cumple?* Si no hay respuesta, reescríbelo.
