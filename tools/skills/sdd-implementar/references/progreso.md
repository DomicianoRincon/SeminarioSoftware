# Cómo se marca una tarea

Antes:

```markdown
- [ ] **T-09** Cambiar la foto desde la galería · CA-1, CA-2 · depende de: ninguna
```

Después:

```markdown
- [x] **T-09** Cambiar la foto desde la galería · CA-1, CA-2 · depende de: ninguna
  - Hecha: 2026-11-18
  - Archivos: `lib/services/storage_service.dart` (nuevo), `lib/screens/profile_screen.dart`
  - Notas: lo que el siguiente debe saber, o nada.
```

- Solo cambia `[ ]` por `[x]` y agrega las tres líneas. No reescribas el título de la tarea.
- *Archivos*: los que tocaste, con `(nuevo)` en los que creaste. Sin contar `pubspec.lock` ni los `generated_plugin*` que escribe `flutter pub add`.
- *Notas*: lo que quedó raro, una decisión que tomaste o algo que la prueba no cubre.
- Arriba del archivo, cambia *Actualizado* por la fecha de hoy y *Hechas* por la cuenta nueva.
