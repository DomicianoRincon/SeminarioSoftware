# Prompts de Diseño para Google Stitch: Clínica Veterinaria "Patitas & Co."

Colección de prompts estructurados para el lienzo de Google Stitch (`stitch.withgoogle.com`) orientados al prototipado móvil de una clínica veterinaria. Estos prompts definen la atmósfera visual, los contrastes, los campos de entrada y la jerarquía de componentes que Antigravity podrá inspeccionar mediante Stitch MCP.

---

## Pantalla 1: Inicio de Sesión (`LoginScreen`)

Copia y pega este prompt en Stitch para generar la pantalla de acceso de propietarios de mascotas:

```text
Diseña una pantalla móvil moderna y acogedora de inicio de sesión para una app de clínica veterinaria llamada "Patitas & Co.".
- Contexto y atmósfera: Estilo cálido, profesional y amigable para dueños de mascotas. Fondo limpio en blanco cálido (#FDFCFB).
- Cabecera:
  * Icono o ilustración minimalista de una huella de perro/gato estilizada en tono esmeralda (#0F8478).
  * Título tipográfico claro: "Patitas & Co.".
  * Subtítulo cálido: "Cuidamos a quienes más quieres. Ingresa a tu cuenta para gestionar citas y salud de tu mascota".
- Campos del formulario:
  * Campo de texto para Correo Electrónico: icono de correo a la izquierda, borde redondeado suave, placeholder "propietario@ejemplo.com".
  * Campo de texto para Contraseña: icono de candado a la izquierda, icono de ojo a la derecha para ver/ocultar contraseña, placeholder "••••••••".
- Fila de opciones:
  * Casilla de verificación "Recordar sesión".
  * Enlace tipográfico a la derecha: "¿Olvidaste tu contraseña?".
- Acciones:
  * Botón principal de ancho completo en color verde esmeralda (#0F8478) con esquinas redondeadas y texto en blanco en negrita: "Iniciar Sesión".
  * Divisor sutil con texto central: "o continúa con".
  * Botón secundario contorneado (outline) con icono de Google: "Ingresar con Google".
- Pie de pantalla:
  * Texto sutil: "¿Aún no tienes cuenta? Regístrate aquí" (con "Regístrate aquí" resaltado en color esmeralda y negrita).
```

---

## Pantalla 2: Registro de Propietario (`SigninScreen`)

Copia y pega este prompt en Stitch para generar la pantalla de registro de nuevo usuario:

```text
Diseña una pantalla móvil limpia y organizada de registro (Sign In / Register) para la app de la clínica veterinaria "Patitas & Co.".
- Contexto y navegación:
  * Barra superior con botón circular de regreso hacia la izquierda.
  * Título grande: "Crear Cuenta".
  * Subtítulo: "Únete a la familia Patitas y lleva el control médico de tus consentidos".
- Campos del formulario (agrupados con espaciado vertical cómodo):
  * Campo "Nombre completo del tutor": icono de usuario, placeholder "Ej. Mariana Pérez".
  * Campo "Teléfono de contacto / Emergencias": icono de teléfono, selector de prefijo de país, placeholder "300 123 4567".
  * Campo "Correo electrónico": icono de email, placeholder "mariana@correo.com".
  * Campo "Contraseña segura": indicador sutil de fortaleza de contraseña con barra de progreso verde/amarilla.
  * Campo "Nombre de tu primera mascota" (opcional para personalizar el onboarding): icono de huellita, placeholder "Ej. Milo, Luna, Rocky...".
- Términos y privacidad:
  * Casilla marcada para aceptar "Términos del Servicio y Política de Tratamiento de Datos Veterinarios".
- Acción principal:
  * Botón prominente de ancho completo en verde esmeralda (#0F8478) con esquinas redondeadas: "Registrarme".
- Pie de página:
  * Enlace inferior: "¿Ya tienes cuenta registrada? Inicia sesión".
```

---

## Pantalla 3: Tablero Principal de la Mascota (`HomeScreen`)

Copia y pega este prompt en Stitch para generar el dashboard principal tras iniciar sesión:

```text
Diseña el dashboard o pantalla principal móvil (Home) para la app de la clínica veterinaria "Patitas & Co.".
- Barra superior de estado (AppBar):
  * Foto de perfil circular del tutor a la izquierda.
  * Saludo personalizado: "Hola, Mariana 👋" con subtítulo "3 mascotas registradas".
  * Botón de campana de notificaciones con punto rojo indicador a la derecha.
- Tarjeta destacada de la mascota activa (Hero Card):
  * Fondo verde menta suave (#E3F6F3) con borde redondeado pronunciado y sombra ligera.
  * Foto de un perro Golden Retriever sonriente en avatar grande.
  * Datos destacados: "Milo" (Golden Retriever, 2 años y medio, 28 kg).
  * Chip indicador de estado de salud: "Vacunas al día ✓" en verde oscuro.
  * Selector desplegable sutil para cambiar a otra mascota ("Luna - Gato Siamés").
- Banner de Próxima Cita Médica (Appointment Card):
  * Fondo blanco con borde naranja/ámbar cálido (#F0C572).
  * Icono de calendario y hora: "Mañana, 10:30 AM".
  * Detalle: "Control de Vacuna Antirrábica con Dra. Gómez".
  * Botón secundario compacto: "Reprogramar".
- Accesos rápidos a servicios clínicos (Grid de 4 botones circulares con etiquetas):
  * Icono de estetoscopio: "Agendar Cita".
  * Icono de jeringa: "Vacunación".
  * Icono de tijeras: "Peluquería".
  * Icono de ambulancia con alerta roja: "Urgencias 24h".
- Sección de Historial Clínico Reciente:
  * Lista de 2 tarjetas compactas con últimas atenciones:
    - "Desparasitación interna" - 12 de septiembre (Dr. Ramírez).
    - "Limpieza dental preventiva" - 04 de julio (Dra. Gómez).
- Barra de navegación inferior fija (BottomNavigationBar):
  * 4 iconos con etiqueta:
    - Inicio (activo, verde #0F8478).
    - Mascotas.
    - Citas.
    - Perfil / Ajustes.
```
