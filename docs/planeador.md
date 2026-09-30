# Planeador · Seminario de Ingeniería de Software

Plan de curso de las unidades 3 y 4 (sesiones 17 a 32): qué se hace en clase, qué se hace fuera de ella y qué se entrega. Transcrito de la hoja *PlaneadorF* del planeador del departamento.

| | |
|---|---|
| Departamento | Departamento de Computación y Sistemas Inteligentes |
| Curso | Seminario de Ingeniería de Software |
| Créditos | 3 |

## Dedicación

| Concepto | Valor |
|---|---|
| Horas de trabajo directo (en clase) | 32 |
| Horas de estudio independiente (fuera de clase) | 40 |
| Horas de dedicación totales | 72 |
| Créditos reales | 2 |
| Verificación | Créditos subutilizados |

## Entregas

| # | Entrega |
|---|---|
| 1 | Prototipo en Stitch/Figma, base de datos |
| 2 | Prototipo no funcional en Flutter (componentes, pantallas y navegación) |
| 3 | Specs completas de la aplicación |

Momentos evaluativos en clase:

- **Sesión 25** · Entrega parcial 1: maqueta del prototipo de interfaz con pantallas, estado y navegación (3 minutos por equipo).
- **Sesión 30** · Taller evaluativo: pantalla del reto que sube y muestra un archivo.
- **Sesiones 31 y 32** · Entrega final: demostración de la aplicación y sustentación del proceso asistido por IA (equipos 1 a 3 y 4 a 6).

## Calendario

| Sesión | Unidad | Tema | En clase | Fuera de clase |
|---|---|---|---|---|
| 17 | 4 | Entorno y primera aplicación | 2 h | 2 h |
| 18 | 4 | Componentes | 2 h | 2 h |
| 19 | 4 | Pantallas con componentes | 2 h | 2 h |
| 20 | 3 | El agente en consola y el archivo de contexto | 2 h | 2 h |
| 21 | 3 | Skills: extender el agente | 2 h | 4 h |
| 22 | 4 | Stateful widget y setState | 2 h | 2 h |
| 23 | 4 | Elevación de estado y funciones como parámetro | 2 h | 2 h |
| 24 | 4 | Navegación entre pantallas | 2 h | 4 h |
| 25 | 4 | Navegación con bottom navigation bar ⭐ | 2 h | 2 h |
| 26 | 3 | Spec Driven Development | 2 h | 4 h |
| 27 | 3 y 4 | Servicio de base de datos | 2 h | 2 h |
| 28 | 3 y 4 | Servicio de autenticación | 2 h | 2 h |
| 29 | 3 y 4 | Servicio de storage | 2 h | 4 h |
| 30 | 3 y 4 | Funciones como servicio ⭐ | 2 h | 4 h |
| 31 | 3 y 4 | Entrega final I (equipos 1 a 3) ⭐ | 2 h | 2 h |
| 32 | 3 y 4 | Entrega final II (equipos 4 a 6) y cierre ⭐ | 2 h | — |

⭐ = sesión con actividad evaluativa en clase.

## Sesión 17 · Entorno y primera aplicación

*Unidad 4*

### En clase

- Presentación de los profesores y de las unidades 3 y 4.
- Qué es el desarrollo frontend multiplataforma y en qué se diferencia de lo que han visto.
- Instalación del SDK, el editor y el emulador.
- Primera aplicación y ejecución del hola mundo.
- Instalar entorno supabase

`2 h` · RA4 · SO-7 · Formativa · Nivel 1 - Sin IAG · IAG: Ninguna

### Fuera de clase

- Dejar el entorno verificado, corriendo la aplicación de ejemplo en un emulador o dispositivo propio.

`2 h` · RA4 · SO-7 · Formativa · Nivel 1 - Sin IAG · IAG: Ninguna

## Sesión 18 · Componentes

*Unidad 4*

### En clase

- Recorrido por main.dart y por la estructura de carpetas del proyecto.
- Paradigma declarativo frente a imperativo: la interfaz como función del estado.
- Widgets básicos: Text, Image (asset y network) y botones.
- Concepto de componente como pieza reutilizable de interfaz.
- Taller: cada estudiante arma componentes Stateless y los monta en una pantalla para verlos.

`2 h` · RA4 · SO-1 · Formativa · Nivel 1 - Sin IAG · IAG: Ninguna

### Fuera de clase

- Terminar los componentes del taller: son el insumo del taller de la sesión 19.

`2 h` · RA4 · SO-1 · Formativa · Nivel 1 - Sin IAG · IAG: Ninguna

## Sesión 19 · Pantallas con componentes

*Unidad 4*

### En clase

- Scaffold y SafeArea como andamiaje de una pantalla.
- Composición: armar una pantalla a partir de componentes propios.
- Layout con Column, Row, Expanded, Container, Padding y SingleChildScrollView.
- Convención Screen frente a Page: la Screen tiene Scaffold y se navega; la Page la hospeda una Screen.
- Taller: armar dos pantallas del reto con componentes propios y suministrados.

`2 h` · RA4 · SO-1, SO-2 · Formativa · Nivel 1 - Sin IAG · IAG: Ninguna

### Fuera de clase

- Lectura sobre la construcción de archivos de contexto para agentes (CLAUDE.md / AGENTS.md).

`2 h` · RA3 · SO-7 · Formativa · Nivel 1 - Sin IAG · IAG: Ninguna

## Sesión 20 · El agente en consola y el archivo de contexto

*Unidad 3*

### En clase

- Asistentes de IA en consola: qué son y cómo se opera con ellos.
- Modos de operación y niveles de autonomía.
- Gestión del contexto: qué ve el agente y por qué eso determina la calidad de lo que produce.
- Construcción del primer CLAUDE.md/AGENTS.md con /init: propósito, estructura, cómo ejecutar, convenciones y reglas para los agentes.
- El archivo de contexto es un documento vivo: conciso, y se completa a lo largo del curso.
- Introduccion a los 3 servicios basicos: data, storage y auth

`2 h` · RA3 · SO-7 · Formativa en IAG · Nivel 4 - Uso pleno · IAG: Asistente de IA en consola

### Fuera de clase

- Completar el CLAUDE.md del repositorio del equipo con las convenciones acordadas.

`2 h` · RA3 · SO-7 · Formativa en IAG · Nivel 4 - Uso pleno · IAG: Asistente de IA en consola

## Sesión 21 · Skills: extender el agente

*Unidad 3*

### En clase

- Skills: qué son, cómo se instalan y cómo se invocan. Instalación de la skill de Flutter.
- Taller: generar una pantalla asistido por IA y auditarla contra el contrato del CLAUDE.md.
- Qué se corrige a mano y qué se corrige ajustando el contrato.

`2 h` · RA3, RA4 · SO-2, SO-7 · Formativa en IAG · Nivel 4 - Uso pleno · IAG: Asistente de IA en consola, skills

### Fuera de clase

- Propuesta de la aplicación del reto y diseño no funcional en Stitch y Figma, respetando el contrato mínimo común.

`4 h` · RA4 · SO-2, SO-3 · Formativa en IAG · Nivel 5 - Exploración · IAG: Stitch, Figma, asistente de IA en consola

## Sesión 22 · Stateful widget y setState

*Unidad 4*

### En clase

- Stateless frente a Stateful: por qué el estado vive en el objeto State y no en el widget.
- El árbol de widgets y su reconstrucción: qué hace setState y qué subárbol se vuelve a construir (con un print en build para ver cuándo se reconstruye).
- Ciclo de vida: initState y dispose, con el TextEditingController como caso típico.
- Contador hola mundo sobre estados.
- Taller de dos sesiones, parte 1: agenda de contactos no persistente, resuelta como una sola pantalla con todo el estado adentro. Se continúa en la sesión 23.
- Primera interaccion de usuario: funciones

`2 h` · RA4 · SO-1 · Formativa · Nivel 3 - Colaboración · IAG: Asistente de IA en consola

### Fuera de clase

- Dar estado a un formulario de la aplicación del equipo, con su controller y su dispose.

`2 h` · RA4 · SO-1 · Formativa · Nivel 3 - Colaboración · IAG: Asistente de IA en consola

## Sesión 23 · Elevación de estado y funciones como parámetro

*Unidad 4*

### En clase

- Se retoma la agenda de la sesión 22, con todo el estado y toda la interfaz en un solo archivo, y de ahí sale la elevación de estado: el estado sube a la Screen anfitriona y los componentes lo reciben por constructor.
- Funciones como parámetro: el hijo reporta hacia arriba con un callback, sin conocer al padre.
- Prop drilling: qué es, hasta dónde es aceptable y qué señal da cuando empieza a doler.
- Modelos simples con copyWith para mover estado sin mutarlo.
- Taller de dos sesiones, parte 2: refactorizar la agenda separando la lista y el formulario como componentes, con el estado en la Screen y la comunicación por callbacks.

`2 h` · RA4 · SO-1, SO-2 · Formativa · Nivel 3 - Colaboración · IAG: Asistente de IA en consola

### Fuera de clase

- Reorganizar la aplicación del equipo para que el estado viva en la Screen y las Pages reporten con callbacks.

`2 h` · RA4 · SO-1 · Formativa · Nivel 3 - Colaboración · IAG: Asistente de IA en consola

## Sesión 24 · Navegación entre pantallas

*Unidad 4*

### En clase

- Navegación con Navigator y tabla de rutas nombradas en MaterialApp.
- pushNamed para abrir una pantalla y pop para volver.
- pushNamedAndRemoveUntil para rehacer la pila, con el predicado (route) => false.
- Paso de datos a la pantalla nueva y retorno de un resultado al cerrarla.

`2 h` · RA4 · SO-1 · Formativa · Nivel 3 - Colaboración · IAG: Asistente de IA en consola

### Fuera de clase

- Dejar navegable el prototipo del equipo, con datos simulados. Se sustenta en la sesión 25.

`4 h` · RA4 · SO-2 · Formativa en IAG · Nivel 4 - Uso pleno · IAG: Asistente de IA en consola, skills

## Sesión 25 · Navegación con bottom navigation bar

*Unidad 4*

### En clase

- Entrega parcial 1 (aprox. 25 min): (Maqueta) prototipo de interfaz con pantallas, estado y navegación, 3 minutos por equipo.
- Navegación horizontal con BottomNavigationBar: una Screen anfitriona que cambia de Page según un índice guardado en el estado.
- Cambiar de tab es setState y abrir un detalle es push: cuándo usar cada uno.

`2 h` · RA4 · SO-2, SO-3 · Evaluativa en IAG · Nivel 5 - Exploración · IAG: Asistente de IA en consola, skills

### Fuera de clase

- Terminar la navegación por secciones de la aplicación del equipo.

`2 h` · RA4 · SO-1 · Formativa · Nivel 3 - Colaboración · IAG: Asistente de IA en consola

## Sesión 26 · Spec Driven Development

*Unidad 3*

### En clase

- Spec Driven Development en su nivel inicial: la spec como contrato antes del código.
- El sistema de trabajo completo: estructura del proyecto, agentes, skills, servidores MCP y workflows.
- Skills de generación y de crítica de specs.
- Versionamiento de las specs y seguimiento de cuáles están implementadas y cuáles no.

`2 h` · RA3, RA4 · SO-2, SO-7 · Formativa en IAG · Nivel 5 - Exploración · IAG: Asistente de IA en consola, skills, servidores MCP

### Fuera de clase

- El modelo de datos mínimo en diagrama

`4 h` · RA3, RA4 · SO-1, SO-2 · Formativa en IAG · Nivel 5 - Exploración · IAG: Asistente de IA en consola, skills, servidor MCP de Supabase

## Sesión 27 · Servicio de base de datos

*Unidades 3 y 4*

### En clase

- Conexión de la aplicación con Supabase usando el SDK de Supabase para Flutter: llaves y variables de entorno.
- La capa de servicio como frontera entre la interfaz y la base de datos Postgres.
- CRUD por PostgREST: listar, ver el detalle, crear, editar y borrar.
- Estados de la interfaz frente a una operación asíncrona: cargando y error.

`2 h` · RA4 · SO-1, SO-2 · Formativa · Nivel 4 - Uso pleno · IAG: Asistente de IA en consola, skills, servidor MCP de Supabase

### Fuera de clase

- Data ingest con datos inventados

`2 h` · RA4 · SO-1 · Formativa · Nivel 4 - Uso pleno · IAG: Asistente de IA en consola, skills, servidor MCP de Supabase

## Sesión 28 · Servicio de autenticación

*Unidades 3 y 4*

### En clase

- Base datos parte 2

`2 h` · RA4 · SO-1, SO-2 · Formativa · Nivel 4 - Uso pleno · IAG: Asistente de IA en consola, skills, servidor MCP de Supabase

### Fuera de clase

*(Sin actividad definida en el planeador.)*

`2 h` · RA4 · SO-1 · Formativa · Nivel 4 - Uso pleno · IAG: Asistente de IA en consola, skills, servidor MCP de Supabase

## Sesión 29 · Servicio de storage

*Unidades 3 y 4*

### En clase

- Registro, inicio y cierre de sesión con Supabase Auth.
- Sesión persistente: recuperar al usuario al abrir la aplicación.
- Guardas de navegación: qué rutas exigen sesión y a dónde se redirige cuando no la hay.
- Asociar al usuario los datos que crea.
- Hacer registro en base de datos con UUID de Auth

`2 h` · RA4 · SO-1 · Formativa · Nivel 4 - Uso pleno · IAG: Asistente de IA en consola, skills, servidor MCP de Supabase

### Fuera de clase

- Usuarios pueden registrar y loggearse

`4 h` · RA4 · SO-2, SO-3 · Formativa en IAG · Nivel 5 - Exploración · IAG: Asistente de IA en consola, skills, servidor MCP de Supabase

## Sesión 30 · Funciones como servicio

*Unidades 3 y 4*

### En clase

- Subida de un archivo desde la aplicación a Supabase Storage y visualización del archivo guardado.
- Taller: agregar al reto una pantalla que suba y muestre un archivo.

`2 h` · RA3, RA4 · SO-2, SO-3 · Evaluativa en IAG · Nivel 5 - Exploración · IAG: Asistente de IA en consola, skills, servidor MCP de Supabase

### Fuera de clase

- Preparar la sustentación final: demostración, repositorio, CLAUDE.md, skills y specs, con la evidencia de cómo se dirigió y se auditó al agente.

`4 h` · RA3, RA4 · SO-2, SO-3 · Evaluativa en IAG · Nivel 5 - Exploración · IAG: Asistente de IA en consola, skills, servidor MCP de Supabase

## Sesión 31 · Entrega final I (equipos 1 a 3)

*Unidades 3 y 4*

### En clase

- Entrega final, primera parte: equipos 1 a 3.
- Cada equipo demuestra su aplicación multiplataforma y sustenta el proceso asistido por IA: repositorio, CLAUDE.md, skills, specs y evidencia de cómo dirigió y auditó al agente.
- Aproximadamente 30 minutos por equipo, incluida la retroalimentación.

`2 h` · RA3, RA4 · SO-2, SO-3, SO-7 · Evaluativa en IAG · Nivel 5 - Exploración · IAG: Asistente de IA en consola, skills, servidores MCP

### Fuera de clase

- Preparación de la sustentación de los equipos 4 a 6.

`2 h` · RA3, RA4 · SO-2, SO-3 · Evaluativa en IAG · Nivel 5 - Exploración · IAG: Asistente de IA en consola, skills, servidores MCP

## Sesión 32 · Entrega final II (equipos 4 a 6) y cierre

*Unidades 3 y 4*

### En clase

- Entrega final, segunda parte: equipos 4 a 6, con el mismo formato.
- Cierre del bloque: retroalimentación general y reflexión sobre el uso de IAG a lo largo de las unidades 3 y 4, contrastando el nivel de autonomía inicial con el alcanzado.

`2 h` · RA3, RA4 · SO-2, SO-3, SO-7 · Evaluativa en IAG · Nivel 5 - Exploración · IAG: Asistente de IA en consola, skills, servidores MCP

## Glosario

**Tipo de actividad**

| Tipo | Descripción |
|---|---|
| En clase | Actividades del curso que se desarrollan de manera sincrónica (presencial o virtual) con los estudiantes (trabajo directo). |
| Fuera de clase | Actividades del curso que se desarrollan por fuera del aula de clase (estudio independiente), por ejemplo: actividades de preparación, asignaciones y tareas. |

**Naturaleza de la actividad**

| Naturaleza | Descripción |
|---|---|
| Formativa | Se enseña a los estudiantes a usar, dentro de un contexto profesional específico, herramientas de IAG para potenciar ciertas competencias. No necesariamente implica una nota. |
| Formativa en IAG | Se enseña a los estudiantes a usar herramientas o tecnologías de IAG. No necesariamente implica una nota. |
| Evaluativa | Se mide el desempeño de los estudiantes respecto al nivel de competencia esperado, sin un componente de evaluación sobre el uso de IAG. |
| Evaluativa en IAG | Se mide el desempeño de los estudiantes en el uso de herramientas o tecnologías de IAG; la rúbrica incluye explícitamente ese componente. |

**Nivel de IAG según el AIAS**

| Nivel | Descripción |
|---|---|
| Nivel 1 - Sin IAG | No se permite el uso de IAG en ninguna parte de la actividad formativa o evaluación. |
| Nivel 2 - Planeación | Se permite el uso de IAG solo en la fase de planificación (ideas, esquemas). |
| Nivel 3 - Colaboración | Los estudiantes pueden usar IAG para revisar, editar o mejorar sus borradores o ideas iniciales. |
| Nivel 4 - Uso pleno | La IAG es parte integral del desarrollo de la tarea (uso estratégico durante todo el proceso). |
| Nivel 5 - Exploración | Se incentiva la exploración innovadora de la IAG como parte del producto evaluado. |
