# Revisión antes de marcar

- [ ] Solo son `StatefulWidget` las Screens, las Pages y los formularios. Todo lo demás es `StatelessWidget`.
- [ ] El estado nuevo vive en el State de la Screen (o de la Page, si solo ella lo usa) y cambia con `setState`.
- [ ] Los modelos no se mutan: se reemplazan con `copyWith`.
- [ ] Los componentes reciben los datos por el constructor y avisan con `Function()` o `Function(Tipo)`.
- [ ] Solo los servicios usan `Supabase.instance.client`. Las Screens llaman a los servicios.
- [ ] Imports del proyecto con `package:`, ninguno relativo.
- [ ] Código en inglés, textos de la interfaz en español.
- [ ] Sin comentarios, salvo una línea `///` por clase pública.
- [ ] Después de un `await`, `if (!mounted) return;` antes de usar `context` o `setState`.
- [ ] `flutter analyze` sin errores.
