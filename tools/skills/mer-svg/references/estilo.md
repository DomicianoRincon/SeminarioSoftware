# Estilo del MER

## Lienzo

- `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 ALTO" role="img">`, con `<title>` y `<desc>`.
- Fondo: `<rect width="960" height="ALTO" rx="16" fill="#FBFBFD"/>`.
- Título en x=32, y=44, 20 px, negrita, color `#161A26`. Subtítulo en x=32, y=66, 13 px, color `#79809A`.
- Fuente del texto: `ui-sans-serif, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif`.
- Fuente de tablas y atributos: `ui-monospace, Menlo, Consolas, monospace`, 13 px, color `#161A26`.

## Rejilla

- Cuatro columnas. La x de cada tabla es 32, 272, 512 o 752. Todas miden 176 de ancho.
- La primera fila de tablas empieza en y=88.
- Si hay más de cuatro tablas, la siguiente fila empieza 64 px debajo de la tabla más alta de la fila anterior.
- ALTO = donde termina la última fila + 48.

## Una tabla

Para una tabla en (X, Y) con N atributos:

- Alto = 40 + 28 × N.
- Caja: `<rect x="X" y="Y" width="176" height="ALTO_TABLA" rx="10" stroke-width="1.5"/>` con el relleno y el borde de su color.
- Nombre: centrado en x = X + 88, y = Y + 21, negrita, 14 px, con el color fuerte.
- Línea bajo el nombre: de (X, Y + 32) a (X + 176, Y + 32), con el color del borde.
- El atributo número i (el primero es 0) va centrado en y = Y + 46 + 28 × i, con `dy="0.35em"`, en x = X + 46.
- Insignia PK o FK, a la izquierda del atributo: `<rect x="X+10" y="centro-9" width="26" height="18" rx="9"/>` y encima el texto `PK` o `FK` en blanco, 10.5 px, negrita, centrado en x = X + 23.
  - PK: relleno con el color fuerte de la tabla.
  - FK: relleno `#556074`.

## Colores

Un color por tabla, en este orden. Si hay más de cuatro tablas, se repiten.

- Azul: relleno `#EEF1FF`, borde `#A9B4F2`, fuerte `#4453C9`.
- Verde: relleno `#E3F6F3`, borde `#86D3CA`, fuerte `#0F8478`.
- Ámbar: relleno `#FFF3DC`, borde `#F0C572`, fuerte `#A96C05`.
- Morado: relleno `#F4EBFF`, borde `#C9A6EE`, fuerte `#7439B8`.

## Relaciones

Todas las líneas: `fill="none" stroke="#556074" stroke-width="1.75"`.

Entre dos tablas vecinas de la misma fila, la línea es horizontal y va a 76 px del borde de arriba (LY = Y + 76). Sea A el borde derecho de la tabla de la izquierda y B el borde izquierdo de la tabla de la derecha (B = A + 64).

- Línea: `M A,LY H B`.
- Lado "uno": una barra vertical a 14 px de la tabla. Si el "uno" está a la izquierda: `M A+14,LY-9 V LY+9`. Si está a la derecha: `M B-14,LY-9 V LY+9`.
- Lado "muchos": una pata de gallo de 24 px que se abre hacia la tabla. Si el "muchos" está a la derecha: `M B-24,LY L B,LY-11 M B-24,LY L B,LY M B-24,LY L B,LY+11`. Si está a la izquierda: `M A+24,LY L A,LY-11 M A+24,LY L A,LY M A+24,LY L A,LY+11`.
- Sobre la línea, a 18 px por encima, un `1` cerca del lado uno y una `N` cerca del lado muchos: 13 px, negrita, color `#556074`.

Entre una tabla y la que está justo debajo, la línea es vertical por el centro de la columna (x = X + 88), desde el borde inferior de la de arriba hasta el borde superior de la de abajo, con la barra y la pata de gallo giradas.

## Pie

Una línea de texto bajo las tablas, 12.5 px, color `#79809A`, que dice cómo se leen las relaciones.
