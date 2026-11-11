# El CRUD con el SDK de Supabase

<!-- tags: from('tracks'), select(), insert(), update(), delete(), eq('id', id), .select().single(), PostgrestException, DELETE requires a WHERE clause, null value in column violates not-null constraint, CRUD -->

Toda operación sobre una tabla empieza igual: el cliente de Supabase, el nombre de la tabla y la operación. El resultado llega con `await`, porque es un `Future`.

```dart
final SupabaseClient _client = Supabase.instance.client;

await _client.from('tracks').select();
```

## Pruébalo

Elige una operación, cámbiale los datos y pulsa *Ejecutar*. Mira qué filas de la tabla cambian y qué devuelve el `await`. La tabla recuerda lo que hiciste hasta que pulses *Reiniciar tabla*.

```interactive
crud
```

## Listar: select

```dart
final rows = await _client.from('tracks').select();
```

Trae todas las filas. `rows` es una `List<Map<String, dynamic>>`: un Map por fila, con las columnas como llaves. Para traer solo algunas columnas, se nombran: `select('name, artist_name')`.

## Crear: insert

```dart
await _client.from('tracks').insert({
  'name': 'Viva la Vida',
  'artist_name': 'Coldplay',
});
```

Se manda un Map con las columnas, sin el `id`: lo genera la base de datos. Una columna que no se manda, como `image_url`, queda en `null`.

Así solo, el `await` no devuelve nada y la app no se entera del `id`. Para recibir la fila guardada, se encadena `.select().single()`:

```dart
final row = await _client
    .from('tracks')
    .insert({'name': 'Viva la Vida', 'artist_name': 'Coldplay'})
    .select()
    .single();
```

## Editar: update

```dart
await _client
    .from('tracks')
    .update({'name': 'Paradise'})
    .eq('id', id);
```

`update` recibe solo las columnas que cambian. `eq('id', id)` dice **cuál fila**: solo la que tiene ese `id`.

## Borrar: delete

```dart
await _client.from('tracks').delete().eq('id', id);
```

Sin el `eq`, el delete borraría la tabla entera. Supabase no lo deja: responde `DELETE requires a WHERE clause` y no borra nada.

## Si algo falla

Los errores llegan como `PostgrestException` en el `await`:

- `null value in column "name" violates not-null constraint`: el insert no mandó una columna obligatoria.
- `DELETE requires a WHERE clause`: falta el `.eq(...)` del delete.
- `permission denied for table tracks`: a la tabla le falta el `grant` de su migración.
