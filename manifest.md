# Manifest · Seminario de Ingeniería de Software

Qué sesiones del plan de curso ya tienen su contenido en el visor. El plan completo, con lo que se hace en clase, fuera de clase y los entregables, está en [`docs/planeador.md`](docs/planeador.md). Los resultados de aprendizaje y la evaluación están en [`docs/syllabus.md`](docs/syllabus.md).

Este repositorio cubre **las últimas 8 semanas del curso (semanas 9 a 16)**, que según el syllabus son las unidades 3 y 4. El planeador numera sus sesiones de la **17 a la 32**, porque las 16 primeras son de las unidades 1 y 2, que dicta otro docente. Aquí se cuentan como **sesión 1 a 16**: `sesión del visor = sesión del planeador − 16`, con dos sesiones por semana.

**Estados:** ✅ completa en el visor · 🟡 parcial · ⬜ pendiente

## Sesiones

| Sesión | Planeador | Semana | Unidad | Tema | Estado | Lecciones en el visor |
|---|---|---|---|---|---|---|
| 1 | 17 | 9 | 4 | Entorno y primera aplicación | 🟡 | `S0003` ¿Qué es el frontend? · `S0004` Panorama del frontend · `S0005` Frontend y la nube · `S0006` Desarrollar con IA · `S0001` Instalación básica · sección *Instalación avanzada*: `0019`, `0020`, `0021`, `0022` |
| 2 | 18 | 9 | 4 | Componentes | ⬜ | |
| 3 | 19 | 10 | 4 | Pantallas con componentes | ⬜ | |
| 4 | 20 | 10 | 3 | El agente en consola y el archivo de contexto | ⬜ | |
| 5 | 21 | 11 | 3 | Skills: extender el agente | ⬜ | |
| 6 | 22 | 11 | 4 | Stateful widget y setState | ⬜ | |
| 7 | 23 | 12 | 4 | Elevación de estado y funciones como parámetro | ⬜ | |
| 8 | 24 | 12 | 4 | Navegación entre pantallas | ⬜ | |
| 9 | 25 | 13 | 4 | Navegación con bottom navigation bar | ⬜ | |
| 10 | 26 | 13 | 3 | Spec Driven Development | ⬜ | |
| 11 | 27 | 14 | 3 y 4 | Servicio de base de datos | ⬜ | |
| 12 | 28 | 14 | 3 y 4 | Servicio de autenticación | ⬜ | |
| 13 | 29 | 15 | 3 y 4 | Servicio de storage | ⬜ | |
| 14 | 30 | 15 | 3 y 4 | Funciones como servicio | ⬜ | |
| 15 | 31 | 16 | 3 y 4 | Entrega final I (equipos 1 a 3) | ⬜ | |
| 16 | 32 | 16 | 3 y 4 | Entrega final II (equipos 4 a 6) y cierre | ⬜ | |

## Material de apoyo (no atado a una sesión)

| Sección del visor | Lecciones | Origen |
|---|---|---|
| Curso | `S0002` Programa del curso | Propia, hecha a partir de `docs/syllabus.md` |
| Entregables | `S0007`, `S0008`, `S0009`: las tres entregas del proyecto, **solo qué se entrega** | Propias, hechas a partir de la tabla *Entregas* de `docs/planeador.md`. Fechas, sesiones, uso de IA y pesos están ocultos en `docs/entregables.md` hasta que se confirmen |
| Dart | `0001`, `0006` a `0012` | Sección *Dart basics* de Aplicaciones Móviles |

## Detalle por sesión

### Sesión 1 · Entorno y primera aplicación

**Presentación:** `presentaciones/sesion1/` · *Frontend developing*, publicada en
https://domicianorincon.github.io/SeminarioSoftware/presentaciones/1/ y enlazada al inicio de `S0003`.

| Lo que pide el planeador | Dónde está en el visor |
|---|---|
| Presentación de los profesores y de las unidades 3 y 4 | En vivo, sin lección |
| Qué es el desarrollo frontend multiplataforma | `S0003` ¿Qué es el frontend? y `S0004` Panorama del frontend |
| Instalación del SDK, el editor y el emulador | `S0001` Instalación básica (VS Code + Chrome). El emulador está en *Instalación avanzada*: `0019`, `0022` |
| Primera aplicación y hola mundo | `S0001` (crear y ejecutar en Chrome, hot reload) y `0020` Tu primera app Flutter |
| Introducción a los servicios de la nube *(el planeador la pone en la sesión 20; se adelantó)* | `S0005` Frontend y la nube: autenticación, base de datos y storage vía SDK |
| Instalar entorno Supabase | ⬜ **Pendiente.** Móviles tiene `lessonH1.md` (*Instalación de supabase*, `0051`) y `lessonX5.md` (*Self-hosted Supabase*, `0054`) para reutilizar |
| *Fuera de clase:* entorno verificado, corriendo en emulador o dispositivo propio | *Instalación avanzada*: `0021` Ejecutar las apps y `0022` Configurando dispositivos virtuales |

## Lecciones reutilizadas de Aplicaciones Móviles

Son copias de las de `FlutterLearning/content/`, con el **mismo nombre de archivo y el mismo id**. El 2026-09-29 eran idénticas byte a byte al original. Si se corrige una en Móviles, la copia de aquí no cambia sola.

| Archivo | Id | Título | Sección aquí | Sección en Móviles |
|---|---|---|---|---|
| `lessonC1.md` | `0019` | Instalación de Flutter | Instalación avanzada | Flutter · SEMANA 1 |
| `lessonC2.md` | `0020` | Tu primera app Flutter | Instalación avanzada | Flutter · SEMANA 1 |
| `lessonC3.md` | `0021` | Ejecutar las apps | Instalación avanzada | Flutter · SEMANA 1 |
| `lessonC4.md` | `0022` | Configurando dispositivos virtuales | Instalación avanzada | Flutter · SEMANA 1 |
| `lessonA1.md` | `0001` | Primeros pasos con Dart | Dart | Dart basics |
| `lessonA2.md` | `0006` | Operadores numéricos | Dart | Dart basics |
| `lessonA3.md` | `0007` | Trabajando con Strings | Dart | Dart basics |
| `lessonA4.md` | `0008` | Condicionales | Dart | Dart basics |
| `lessonA5.md` | `0009` | Tipos opcionales y null safety | Dart | Dart basics |
| `lessonA6.md` | `0010` | Listas y mapas | Dart | Dart basics |
| `lessonA7.md` | `0011` | Métodos en Dart | Dart | Dart basics |
| `lessonA8.md` | `0012` | Clases y objetos en Dart | Dart | Dart basics |

## Lecciones propias del Seminario

| Archivo | Id | Título | Sesión |
|---|---|---|---|
| `lessonS1.md` | `S0001` | Instalación básica | 1 |
| `lessonS2.md` | `S0002` | Programa del curso | *(apoyo, sección Curso)* |
| `lessonS3.md` | `S0003` | ¿Qué es el frontend? | 1 |
| `lessonS4.md` | `S0004` | Panorama del frontend | 1 |
| `lessonS5.md` | `S0005` | Frontend y la nube | 1 |
| `lessonS6.md` | `S0006` | Desarrollar con IA | 1 |
| `lessonS7.md` | `S0007` | Entrega 1 · Prototipo en Stitch/Figma y base de datos | *(apoyo, sección Entregables)* |
| `lessonS8.md` | `S0008` | Entrega 2 · Prototipo no funcional en Flutter | *(apoyo, sección Entregables)* |
| `lessonS9.md` | `S0009` | Entrega 3 · Aplicación final y exhibición | *(apoyo, sección Entregables)* |
