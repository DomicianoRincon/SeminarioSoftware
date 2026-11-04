# Flutter + Supabase en el curso

## Los tres servicios

- **Auth** (antes GoTrue): crea cuentas, inicia y cierra sesión. Cada usuario tiene un `uuid`.
- **Base de datos** (Postgres, expuesto por PostgREST): las tablas de `docs/modelo.md`. La app lee y escribe filas.
- **Storage**: archivos como fotos o PDF, guardados en buckets.

La app no llama a cada servicio por separado: usa un solo SDK, `supabase_flutter`, que trae los tres.

## Las llaves

- En la app va la **publishable key** del proyecto. Está hecha para ir en el cliente.
- La **secret key** nunca va en la app ni en el repositorio.

## Invariantes que casi siempre aplican

Úsalas como punto de partida y ajústalas al proyecto.

- **Sin backend propio.** La app habla directo con Supabase. *Evita* que alguien monte un servidor aparte para una sola pantalla.
- **Una capa de servicios.** Solo los servicios de la app llaman a Supabase; las pantallas les piden los datos. *Evita* llamadas repetidas y distintas a la misma tabla regadas por las pantallas.
- **El usuario es el de Auth.** Toda fila que pertenece a alguien guarda el `uuid` de Auth. *Evita* dos identidades para la misma persona.
- **Los archivos van en Storage.** La tabla guarda solo la ruta del archivo. *Evita* guardar imágenes dentro de la base de datos.
- **Llaves fuera del código.** La URL y la publishable key se leen de la configuración, no se escriben en cada archivo. *Evita* cambiar de proyecto editando diez archivos.

## Lo que el curso deja por fuera

La app es ligera. Las políticas de seguridad por filas (RLS), las Edge Functions y Realtime no se usan: si aparecen, van en *Diferido*.
