# Métricas del conjunto de specs

Cada métrica con su fórmula y su meta.

## Completitud

RF que aparecen en el campo `requisitos` de alguna spec ÷ RF totales (sin los retirados).
Meta: 100 %. Lista los RF que no tienen spec.

## Trazabilidad

Dos sentidos:

- RF que citan un objetivo `O-xx` del PRD ÷ RF totales.
- Specs que citan al menos un RF ÷ specs totales.

Meta: 100 % en los dos. Un RF sin objetivo puede sobrar; una spec sin RF puede ser una idea que nadie pidió.

## Verificabilidad

Criterios de aceptación con la forma Dado / cuando / entonces y un resultado que se ve ÷ criterios totales.
Además, ninguna spec sin criterios. Meta: 100 %.

## Ambigüedad

Palabras vagas encontradas en las specs: fácil, rápido, intuitivo, amigable, adecuado, etc., algunos, varios, y/o.
Cuenta por spec. Meta: 0.

## Consistencia

Contradicciones entre dos specs, o de una spec con la spine o con `docs/modelo.md`. Por ejemplo, una spec dice que la publicación tiene foto y el modelo no la tiene.
Meta: 0.

## Atomicidad

Specs que describen más de una funcionalidad (su título lleva "y", o tienen dos flujos principales que no dependen uno del otro).
Meta: 0.

## Pureza funcional

Specs que nombran tecnología: Supabase, Flutter, widgets, `setState`, tablas, SQL.
Meta: 0.

## Preguntas abiertas

Total de preguntas abiertas en las specs. No es un error: es la deuda de especificación. Debe bajar con cada versión.

## Avance de implementación

Specs `implementada` ÷ specs `aprobada` + `implementada`. Si todo está en borrador, dilo.

## Estabilidad

Por spec, cuántas veces subió la versión mayor según su *Historial*. Una spec que cambia mucho todavía no está madura.

## Semáforo

- Verde: en la meta.
- Amarillo: completitud, trazabilidad o verificabilidad entre 80 % y 99 %, o hasta 2 en las métricas de conteo.
- Rojo: el resto.
