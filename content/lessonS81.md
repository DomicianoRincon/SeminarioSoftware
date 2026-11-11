# El CRUD con el SDK de Supabase

<!-- tags: from('tabla'), select(), insert(), update(), delete(), eq('id', id), .select().single(), PostgrestException, DELETE requires a WHERE clause, null value in column violates not-null constraint, CRUD -->

Toda operación sobre una tabla empieza igual: el cliente de Supabase, el nombre de la tabla y la operación. El resultado llega con `await`, porque es un `Future`.

```dart
final SupabaseClient _client = Supabase.instance.client;

await _client.from('albums').select();
```

Los ejemplos de abajo usan una tabla `albums` (`id`, `title`, `band`, `year`). El simulador usa la tabla `tracks`.

## Pruébalo

Elige una operación, cámbiale los datos y pulsa *Ejecutar*. Mira qué filas de la tabla cambian y qué devuelve el `await`. La tabla recuerda lo que hiciste hasta que pulses *Reiniciar tabla*.

```interactive
crud
```

## Listar: select

```dart
final albums = await _client.from('albums').select();
```

Trae todas las filas. `albums` es una `List<Map<String, dynamic>>`: un Map por fila, con las columnas como llaves. Para traer solo algunas columnas, se nombran: `select('title, band')`.

## Crear: insert

```dart
await _client.from('albums').insert({
  'title': 'Abbey Road',
  'band': 'The Beatles',
});
```

Se manda un Map con las columnas, sin el `id`: lo genera la base de datos. Una columna que no se manda, como `year`, queda en `null`.

Así solo, el `await` no devuelve nada y la app no se entera del `id`. Para recibir la fila guardada, se encadena `.select().single()`:

```dart
final album = await _client
    .from('albums')
    .insert({'title': 'Abbey Road', 'band': 'The Beatles'})
    .select()
    .single();
```

## Editar: update

```dart
await _client
    .from('albums')
    .update({'year': 1969})
    .eq('id', albumId);
```

`update` recibe solo las columnas que cambian. `eq('id', albumId)` dice **cuál fila**: solo la que tiene ese `id`.

## Borrar: delete

```dart
await _client.from('albums').delete().eq('id', albumId);
```

Sin el `eq`, el delete borraría la tabla entera. Supabase no lo deja: responde `DELETE requires a WHERE clause` y no borra nada.

## Si algo falla

Los errores llegan como `PostgrestException` en el `await`:

- `null value in column "title" violates not-null constraint`: el insert no mandó una columna obligatoria.
- `DELETE requires a WHERE clause`: falta el `.eq(...)` del delete.
- `permission denied for table albums`: a la tabla le falta el `grant` de su migración.
