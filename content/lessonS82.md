# Dictamen del taller · Spine y specs

<!-- tags: dictamen, architectural spine, sin backend propio, bajo demanda, Diferido, coherencia del PRD y la spine, Edge Function, la spec nombra Supabase, servidor propio, máquina virtual, la llave de Gemini en la app, el rol en los metadatos de Auth -->

Revisé las entregas del [taller de la spine y las specs](https://domicianorincon.github.io/SeminarioSoftware/lesson/S0074) del Grupo 1. Aquí está lo que encontré en cada proyecto y los errores que se repitieron. Léanlo antes de seguir: lo que se corrija ahora en la spine se ahorra en el código.

## Cómo los evalué

Revisé tres cosas, en este orden de importancia:

1. **Que la arquitectura se quede en lo que hemos visto.** La idea de su proyecto viene del caso de su empresa, y eso está bien. Lo que les pido es que la spine use lo del curso: una app Flutter con Screens, Pages, `setState` y rutas nombradas, una capa de servicios, y Supabase con Auth, base de datos y Storage a través de `supabase_flutter`, **sin backend propio**. RLS, Edge Functions y Realtime van en *Diferido*. Si la spine mete algo que no hemos visto (otro frontend, un servidor, una API de IA, pasarelas de pago, mensajería, scraping), resta, salvo que lo hayan dejado **honestamente diferido** y la app se pueda construir sin eso.
2. **El proceso SDD.** Specs funcionales sin tecnología, una por funcionalidad y ligadas a los requisitos; la crítica hecha con la skill `sdd-critica`, las correcciones aplicadas y las specs corregidas en `0.2.0`; el reporte sin rojos.
3. **Que todo cuente la misma app.** `AGENTS.md` (o `CLAUDE.md`), PRD, requisitos, spine y specs tienen que ser consecuentes: lo que el PRD promete lo sostiene la spine, y ninguna spec pide algo que la arquitectura no puede hacer. Cada proyecto cierra con una **Crítica** sobre esto y sobre si la propuesta corresponde a la arquitectura sugerida.

## En general

- **RutaViva**: dentro del curso.
- **Recomendador de eventos Peewah**: dentro del curso en una de sus dos versiones; la otra agrega Gemini.
- **Mercado automotor colombiano**: dentro del curso, con el scraping en exploración.
- **Moneda segura**: dentro del curso, con un detalle en el rol.
- **NevaraFresh**: dentro del curso, con RLS de más.
- **Red Vitalys**: dentro del stack, pero sobrediseñada.
- **Tienda en línea de Tina**: backend acordado para Wompi, pero el frontend está en React.
- **Peewah para agentes de IA**: necesita un backend propio.

El proceso SDD les salió bien a casi todos: specs sin tecnología, todo requisito cubierto y reportes en verde. La diferencia está en la spine. Varios tomaron el patrón del curso y lo adaptaron a su caso; otros dejaron entrar piezas que no hemos visto. Hay dos excepciones que ya acordamos: el equipo del mercado automotor va a explorar si el scraping del portal es viable, y la tienda de Tina puede tener backend propio o Edge Functions para recibir los webhooks de Wompi. Si quieren ver cómo se hace, miren RutaViva: partió de un diseño con data lake y Kafka y lo bajó, diciéndolo explícitamente, a Flutter + Supabase.

Ojo con los reportes "todo en verde": la crítica mide la calidad de las specs, no si la arquitectura es la del curso (la skill tiene la orden de no juzgar la tecnología). Un reporte perfecto puede convivir con una spine que no se puede construir.

## RutaViva

- **Arquitectura.** Es la mejor adaptación del grupo. En el resumen dicen de frente que el caso original usaba data lake y streaming (MQTT/Kafka) y que aquí la telemetría y las predicciones se cargan como filas en Postgres. Su regla de que la predicción de falla es un dato que la app solo lee los libra de construir un motor de ML. El diagrama es el del curso, RLS, Edge Functions y Realtime están en *Diferido* y los servicios tienen nombre (`FleetService`…).
- **SDD.** Seis specs, todas en `0.2.0` después de la crítica. La trazabilidad quedó en amarillo porque la spec de inicio de sesión solo cita un requisito no funcional; lo aceptaron y lo explicaron en el reporte, que es lo correcto.
- **Para mejorar.** Storage aparece en el diagrama y en el stack "sin uso identificado". Si ningún requisito lo pide, déjenlo solo en *Diferido*.

### Crítica

- Es el conjunto más consecuente del grupo. `AGENTS.md` declara el mismo stack que la spine, y lo que el PRD deja por fuera (la integración con los retailers, el ML real, las notificaciones) es justo lo que la spine simula o difiere.
- Lo único que no cuadra: el PRD nombra tecnología cuando dice qué no incluye ("Edge Functions, Realtime o RLS de Supabase") y los requisitos piden "Flutter Web". Las tecnologías se deciden en la spine; el PRD y los requisitos hablan del producto.
- La propuesta corresponde a la arquitectura sugerida: una app Flutter con Auth y base de datos de Supabase.

## Recomendador de eventos Peewah

Este equipo entregó **dos versiones distintas** del mismo proyecto: una sin IA y otra que llama a Gemini desde la app. Un equipo debe tener un solo PRD, una sola spine y un solo juego de specs. Unifiquen, y tomen como base la versión sin IA, porque es la que se ajusta al curso.

### La versión sin IA

- **Arquitectura.** Fiel al curso: solo Auth y base de datos. Encierran las sugerencias en un `RecomendadorService` que hoy lee el conjunto de datos sintético, y dejan la IA y el envío de correos en *Diferido* con la razón correcta: la llave de un modelo no puede ir en la app. Además escribieron reglas propias de su dominio, que es justo lo que se busca: todo se filtra por la organización del usuario, y la apertura de inscripciones y los recordatorios se guardan como días antes del evento.
- **SDD.** Ocho specs. La primera crítica encontró nombres de tecnología en las specs, los corrigieron y cinco specs subieron a `0.2.0`. Reporte en verde.
- **Para mejorar.** Falta `docs/modelo.md`.

### La versión con Gemini

- **Arquitectura.** Agrega la **API de Gemini**, llamada desde la app como si fuera un segundo backend: está en el diagrama y en la mitad de las reglas. Llamar a un modelo de IA desde Flutter no lo hemos visto, y la spine acepta que la llave de Gemini viaje dentro de la app, algo que el curso prohíbe: ningún secreto va en el cliente.
- **Lo bueno.** La regla de que cada organización solo ve lo suyo mientras RLS está diferido, el `docs/modelo.md` y la crítica bien aplicada: la spine y cinco specs en `0.2.0`, con cuatro inconsistencias corregidas.

### Crítica

- En la versión sin IA, `AGENTS.md`, PRD y spine coinciden: las sugerencias salen del conjunto sintético y en ningún documento se promete IA. En la versión con Gemini, PRD y spine están de acuerdo entre sí (el PRD promete sugerencias "integradas con un modelo de IA"), pero los dos se salen del curso, y `AGENTS.md` ni siquiera menciona a Gemini.
- En las dos versiones no cuadra el correo. El PRD lo incluye, los requisitos piden que cada recordatorio salga "dentro de las 24 horas" y hay una spec que dice "llega el día… el sistema envía", pero la spine lo deja en *Diferido* sin ningún servicio que lo haga. Una app Flutter no puede despertarse sola a mandar correos, y todavía no hemos visto cómo montar un backend que lo haga. Háganlo **bajo demanda**: el día del recordatorio la app le muestra al organizador un botón para enviarlo, y al pulsarlo la app llama a un servicio de correo gratuito que se pueda usar directo desde el cliente (EmailJS, por ejemplo). Ajusten el PRD, el requisito de las 24 horas y la spec para que digan eso, y nombren el servicio en la spine.
- En la versión con Gemini, el requisito de mostrar las sugerencias en menos de 10 segundos queda en manos de un servicio externo que ustedes no controlan.
- Sin Gemini y con el correo bajo demanda, la propuesta corresponde a la arquitectura sugerida.

## Mercado automotor colombiano

- **Arquitectura.** El patrón del curso, con buenas reglas de su dominio: un dato que el portal no trae se guarda como ausente, nunca como cero, y cada anuncio guarda de qué portal viene y cuándo se obtuvo.
- **El scraping, en exploración.** Obtener anuncios de un portal externo de forma automática no lo cubre nada del curso. Como acordamos, van a hacer una **exploración** para comprobar si se puede. Mientras tanto está bien que siga en *Diferido*.
- **Una idea para la exploración.** Traer los anuncios cada 24 horas exige algo que corra solo, y eso es un servidor o una máquina virtual aparte. Para evitarlo, prueben traerlos **bajo demanda**: cuando el empleado busca, la app consulta el portal y guarda en la base de datos lo que trae. En la exploración comprueben tres cosas: si el portal tiene una API pública (es mucho más estable que leer el HTML de la página), si sus términos de uso lo permiten y si funciona en web, porque el navegador suele bloquear los pedidos a otro dominio y puede que solo funcione en Android. Si no se puede, carguen los anuncios como datos de ejemplo, como hizo RutaViva.
- **Pendiente.** Que el administrador cree las cuentas de los empleados necesitaría la secret key, que no puede ir en la app. Lo dejaron bien diferido, pero tienen que decidirlo.
- **SDD.** Seis specs y reporte en verde. Las specs corregidas quedaron en `0.1.1`; tras la crítica deben subir a `0.2.0`.

### Crítica

- `CLAUDE.md` está bien alineado con la spine en lo que advierte (la secret key, RLS, los términos de uso del portal), pero dice "plataforma web", mientras la spine dice Android y web con prioridad en celular. Elijan una y que todos los documentos digan lo mismo.
- La obtención automática aparece en el alcance del PRD, en sus objetivos, en dos requisitos (actualizar los anuncios cada 24 horas y tener al menos 1.000) y en su propia spec, pero la spine no tiene ninguna pieza que la haga. Hasta que la exploración dé resultado, márquenlo como condicional en todos esos documentos. Si se quedan con la consulta bajo demanda, el requisito de las 24 horas cambia: los anuncios se actualizan cuando alguien busca. Lo mismo con la creación de cuentas por el administrador: márquenla como pendiente hasta decidir cómo hacerla.
- El visor de anuncios, la búsqueda, la ficha y la comparación corresponden a la arquitectura sugerida. La carga de anuncios depende de lo que salga de la exploración.

## Moneda segura

- **Arquitectura.** Dentro del curso: Auth, base de datos y Storage para los datasets, servicios con nombre, una auditoría a la que solo se le agregan registros y un control por rol para cambiar las reglas de detección. RLS, Edge Functions y Realtime en *Diferido*.
- **Un detalle.** El rol se guarda en los **metadatos de Auth**. En el curso lo hacemos al revés: Auth solo autentica y el rol vive en la tabla de usuarios, unida por el `uuid`.
- **SDD.** Cinco specs y reporte en verde. Las corregidas quedaron en `0.1.1` y `0.1.2`; tras la crítica deben subir a `0.2.0`.

### Crítica

- El conjunto es consecuente. `AGENTS.md`, PRD (solo web de escritorio, datos sintéticos) y spine cuentan la misma app, y Storage tiene un uso que el PRD respalda: los lotes que se exportan desde el histórico.
- Lo único que no cuadra es el rol. La spine valida en la app que el usuario sea administrador antes de cambiar una regla, pero lee ese rol de un dato que el propio usuario podría tocar. Con el rol en la tabla de usuarios, la regla de la spine y la spec de las reglas estáticas quedan bien.
- La propuesta corresponde a la arquitectura sugerida, y usa los tres servicios.

## NevaraFresh

- **Arquitectura.** El patrón del curso, bien escrito, con las imágenes de los productos por URL en vez de Storage, que es una decisión válida y está declarada.
- **Lo que sobra.** Convierten **RLS en una regla fija**. En el curso no lo usamos; debería ir en *Diferido*, con el riesgo anotado. Otra regla baja hasta `main.dart`, que es detalle de código y no va en la spine.
- **SDD.** Ocho specs, tres en `0.2.0`, y reporte en verde. Les faltan las metas numéricas de algunos objetivos, que quedaron como preguntas abiertas del PRD.

### Crítica

- PRD, requisitos y spine coinciden: una app solo para clientes, en celular y sin pasarela de pago.
- `AGENTS.md`, en cambio, cuenta otra app: describe a los usuarios como personal operativo (administradores de tienda, logística, conductores) y pone Storage en el stack, mientras el PRD excluye a los repartidores y la spine no usa Storage. Pónganlo al día con el PRD, porque es lo primero que lee el agente.
- La propuesta corresponde a la arquitectura sugerida, quitando RLS.

## Red Vitalys

- **Arquitectura.** Se quedan en el stack, y lo dicen: `setState`, la navegación de Flutter, solo `supabase_flutter`, sin Storage. RLS y las funciones de base de datos están en *Diferido*, con una explicación del riesgo muy buena.
- **Lo que está por encima del curso.** Piden **repositorios con una interfaz y dos implementaciones** (memoria y Supabase), un único punto de control de acceso con una matriz de permisos y una auditoría que se escribe antes de cada intento. Eso es inversión de dependencias y un diseño de seguridad que no hemos visto. La spine tiene **15 reglas**, bastante más que las dos páginas que pide la skill, y una de ellas trae las reglas de negocio de los indicadores, que van en las specs.
- **SDD.** 23 specs y 219 criterios, muy cuidadas, pero con versiones como `0.6.5` en un solo día: reescribieron los documentos en cada vuelta en vez de cerrarlos. Ese alcance no cabe en las 8 semanas que quedan. Recorten a seis u ocho funcionalidades.

### Crítica

- La coherencia es muy alta: cada versión de la spine dice en qué versión del PRD y de los requisitos se basa, y el requisito de que la entrega 2 funcione con datos en memoria está respaldado por la regla de los repositorios con dos fuentes.
- Lo que no cuadra: que la IP de cada intento la registre el servidor y que los intentos fallidos se cuenten por IP exige funciones dentro de la base de datos, que no son parte de lo que usamos. La spine lo reconoce en *Diferido*, pero las specs del bloqueo del inicio de sesión y del registro de accesos ya lo dan por hecho.
- Les sugiero quitar la IP. El bloqueo tras cinco intentos fallidos lo puede llevar la propia pantalla de inicio de sesión, contando los intentos en su estado, y el evento de auditoría de un intento fallido se guarda en la base de datos con el correo que se intentó, la fecha y la hora, el resultado y la plataforma (web o Android). Del lado del servidor, Supabase Auth ya limita los intentos repetidos de inicio de sesión sin que tengan que programar nada. Así el requisito, la spine y las dos specs quedan dentro de lo que hemos visto.
- Sin la IP, la propuesta corresponde a la arquitectura sugerida. Su problema no es el stack, es el tamaño.

## Tienda en línea de Tina

- **Lo que acordamos.** La app puede ser la de su propia tienda, y para recibir los **webhooks de Wompi** hace falta **backend propio o Edge Functions**. Esa parte de la spine está justificada y no resta. Dos de sus reglas son justo las que esa decisión exige: el comprobante solo se genera cuando Wompi confirma el pago al backend, y las llaves de Wompi viven solo en el backend.
- **Lo que sigue fuera del curso.** El **frontend en React**: la app tiene que ser Flutter. Tampoco aparecen Supabase ni la capa de servicios. El resto del backend (catálogo, carrito, pedidos) no necesita un servidor: puede ser Supabase, como en los demás proyectos, y al backend o a la Edge Function le queda solo lo que exige Wompi (crear el cobro y recibir la confirmación). Correo y WhatsApp no los acordamos: van en *Diferido*.
- **Formato.** La spine no sigue la plantilla de la skill (usa tablas en vez del diagrama, el stack y el *Diferido*), y el lenguaje del backend y el hosting siguen "por definir".
- **SDD.** El reporte dice que la revisión fue **manual, sin la skill `sdd-critica`**, y las specs siguen en `0.1.0`. Las specs sí son funcionales y cubren todos los requisitos.
- **Para rehacer.** Corran `sdd-arquitectura` con Flutter + Supabase y la pieza de Wompi nombrada (backend o Edge Function), con su regla; manden correo y WhatsApp a *Diferido* y vuelvan a correr la crítica.

### Crítica

- Los documentos son coherentes entre sí, pero todos describen una tienda web, no una app Flutter, y `AGENTS.md` no dice con qué se construye.
- Los avisos por correo y WhatsApp son un objetivo del PRD y tienen su spec, pero ningún servicio los cubre. Las fotos de los productos van en una tabla en vez de Storage, y las cuentas de las clientas no usan Auth: la spine solo autentica a las usuarias del panel.
- Hoy la propuesta no corresponde a la arquitectura sugerida, pero casi toda cabe en ella: catálogo y pedidos en la base de datos, fotos en Storage y cuentas en Auth, más la pieza que acordamos para los webhooks de Wompi.

```svg
<svg xmlns="http://www.w3.org/2000/svg" id="tiArq" viewBox="0 0 960 424" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tiArq-ttl tiArq-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tiArq-ttl">La arquitectura que propone tu spine</title>
  <desc id="tiArq-dsc">La clienta y la administradora usan un frontend web en React que habla con un servidor propio, una instancia o máquina virtual aparte. Ese servidor lee y escribe en una base relacional y se conecta con Wompi, un servicio de correo y WhatsApp. El frontend en React y el servidor propio no están en el stack del curso.</desc>
  <defs>
    <style>
      #tiArq .card { stroke-width:1.5; }
      #tiArq .hero { stroke-width:2.5; filter:url(#tiArq-lift); }
      #tiArq .n-rose { fill:#FFEBEF; stroke:#F3A3B2; } #tiArq .t-rose { fill:#C2354F; }
      #tiArq .n-slate { fill:#EFF1F5; stroke:#C4CBD8; } #tiArq .t-slate { fill:#556074; }
      #tiArq .n-violet { fill:#F4EBFF; stroke:#C9A6EE; } #tiArq .t-violet { fill:#7439B8; }
      #tiArq .title { fill:#161A26; font-size:22px; font-weight:700; }
      #tiArq .sub { fill:#79809A; font-size:13.5px; }
      #tiArq .nt { font-size:14px; font-weight:600; }
      #tiArq .nb { fill:#454C61; font-size:12px; }
      #tiArq .link { fill:none; stroke:#556074; stroke-width:1.75; marker-end:url(#tiArq-arrow); }
      #tiArq .bus { fill:none; stroke:#556074; stroke-width:1.75; }
    </style>
    <marker id="tiArq-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <filter id="tiArq-lift" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#0B1020" flood-opacity="0.14"/>
    </filter>
  </defs>

  <rect width="960" height="424" fill="#FBFBFD" rx="16"/>

  <text class="title" x="48" y="56">La arquitectura que propone tu spine</text>
  <text class="sub" x="48" y="80" data-fit="864">En rojo, lo que no está en el stack del curso: el frontend en React y un servidor propio.</text>

  <g transform="translate(48,136)">
    <rect class="card n-violet" width="160" height="64" rx="12"/>
    <text class="nt t-violet" x="16" y="28" data-fit="128">Clienta</text>
    <text class="nb" x="16" y="48" data-fit="128">compra</text>
  </g>
  <g transform="translate(48,264)">
    <rect class="card n-violet" width="160" height="64" rx="12"/>
    <text class="nt t-violet" x="16" y="28" data-fit="128">Administradora</text>
    <text class="nb" x="16" y="48" data-fit="128">gestiona pedidos</text>
  </g>
  <g transform="translate(264,184)">
    <rect class="card n-rose" width="176" height="96" rx="12"/>
    <text class="nt t-rose" x="16" y="36" data-fit="144">Frontend web</text>
    <text class="nb" x="16" y="58" data-fit="144">en React</text>
  </g>
  <g transform="translate(496,184)">
    <rect class="card hero n-rose" width="192" height="96" rx="12"/>
    <text class="nt t-rose" x="16" y="30" data-fit="160">Servidor propio</text>
    <text class="nb" x="16" y="52" data-fit="160">instancia o VM aparte</text>
    <text class="nb" x="16" y="70" data-fit="160">precios, stock, pedidos</text>
  </g>
  <g transform="translate(744,104)">
    <rect class="card n-slate" width="168" height="56" rx="12"/>
    <text class="nt t-slate" x="16" y="24" data-fit="136">Base relacional</text>
    <text class="nb" x="16" y="43" data-fit="136">hosting por definir</text>
  </g>
  <g transform="translate(744,176)">
    <rect class="card n-violet" width="168" height="56" rx="12"/>
    <text class="nt t-violet" x="16" y="24" data-fit="136">Wompi</text>
    <text class="nb" x="16" y="43" data-fit="136">cobro en línea</text>
  </g>
  <g transform="translate(744,248)">
    <rect class="card n-violet" width="168" height="56" rx="12"/>
    <text class="nt t-violet" x="16" y="24" data-fit="136">Correo</text>
    <text class="nb" x="16" y="43" data-fit="136">proveedor por definir</text>
  </g>
  <g transform="translate(744,320)">
    <rect class="card n-violet" width="168" height="56" rx="12"/>
    <text class="nt t-violet" x="16" y="24" data-fit="136">WhatsApp</text>
    <text class="nb" x="16" y="43" data-fit="136">proveedor por definir</text>
  </g>

  <path class="link" d="M208,168 H236 V216 H262"/>
  <path class="link" d="M208,296 H236 V248 H262"/>
  <path class="link" d="M440,232 H494"/>
  <path class="bus" d="M688,232 H716"/>
  <path class="bus" d="M716,132 V348"/>
  <path class="link" d="M716,132 H742"/>
  <path class="link" d="M716,204 H742"/>
  <path class="link" d="M716,276 H742"/>
  <path class="link" d="M716,348 H742"/>
</svg>
```

La sugerida: la tienda y el panel son una sola app Flutter que habla directo con Supabase. Lo único que vive aparte es la pieza que recibe el aviso de Wompi cuando un pago se aprueba y marca el pedido como pagado; las llaves de Wompi viven solo ahí. Los avisos por correo y WhatsApp quedan en *Diferido*.

```svg
<svg xmlns="http://www.w3.org/2000/svg" id="tiSug" viewBox="0 0 960 448" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="tiSug-ttl tiSug-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="tiSug-ttl">Arquitectura sugerida para la tienda de Tina</title>
  <desc id="tiSug-dsc">La clienta y la administradora usan una app Flutter conectada a Auth, la base de datos y Storage de Supabase. La app manda a pagar a Wompi, y una Edge Function o un backend mínimo recibe la confirmación del pago y la escribe en la base de datos.</desc>
  <defs>
    <style>
      #tiSug .card { stroke-width:1.5; }
      #tiSug .hero { stroke-width:2.5; filter:url(#tiSug-lift); }
      #tiSug .n-indigo { fill:#EEF1FF; stroke:#A9B4F2; } #tiSug .t-indigo { fill:#4453C9; }
      #tiSug .n-teal { fill:#E3F6F3; stroke:#86D3CA; } #tiSug .t-teal { fill:#0F8478; }
      #tiSug .n-amber { fill:#FFF3DC; stroke:#F0C572; } #tiSug .t-amber { fill:#A96C05; }
      #tiSug .n-violet { fill:#F4EBFF; stroke:#C9A6EE; } #tiSug .t-violet { fill:#7439B8; }
      #tiSug .title { fill:#161A26; font-size:22px; font-weight:700; }
      #tiSug .sub { fill:#79809A; font-size:13.5px; }
      #tiSug .h { font-size:12px; font-weight:700; letter-spacing:.08em; }
      #tiSug .nt { font-size:14px; font-weight:600; }
      #tiSug .nb { fill:#454C61; font-size:12px; }
      #tiSug .link { fill:none; stroke:#556074; stroke-width:1.75; marker-end:url(#tiSug-arrow); }
    </style>
    <marker id="tiSug-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <filter id="tiSug-lift" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#0B1020" flood-opacity="0.14"/>
    </filter>
  </defs>

  <rect width="960" height="448" fill="#FBFBFD" rx="16"/>

  <text class="title" x="48" y="56">Arquitectura sugerida</text>
  <text class="sub" x="48" y="80" data-fit="864">App Flutter con Auth, base de datos y Storage. En ámbar, lo único aparte: recibir el aviso de pago de Wompi.</text>

  <rect x="704" y="104" width="224" height="272" rx="16" fill="none" stroke="#D9DEE8" stroke-width="1.25" stroke-dasharray="6 5"/>
  <text class="h t-teal" x="720" y="128">SUPABASE</text>

  <g transform="translate(48,136)">
    <rect class="card n-violet" width="160" height="64" rx="12"/>
    <text class="nt t-violet" x="16" y="28" data-fit="128">Clienta</text>
    <text class="nb" x="16" y="48" data-fit="128">compra</text>
  </g>
  <g transform="translate(48,248)">
    <rect class="card n-violet" width="160" height="64" rx="12"/>
    <text class="nt t-violet" x="16" y="28" data-fit="128">Administradora</text>
    <text class="nb" x="16" y="48" data-fit="128">gestiona pedidos</text>
  </g>
  <g transform="translate(264,176)">
    <rect class="card hero n-indigo" width="176" height="96" rx="12"/>
    <text class="nt t-indigo" x="16" y="36" data-fit="144">App Flutter</text>
    <text class="nb" x="16" y="58" data-fit="144">tienda y panel</text>
  </g>
  <g transform="translate(720,144)">
    <rect class="card n-teal" width="192" height="56" rx="12"/>
    <text class="nt t-teal" x="16" y="24" data-fit="160">Auth</text>
    <text class="nb" x="16" y="43" data-fit="160">clientas y panel</text>
  </g>
  <g transform="translate(720,216)">
    <rect class="card n-teal" width="192" height="72" rx="12"/>
    <text class="nt t-teal" x="16" y="26" data-fit="160">Base de datos</text>
    <text class="nb" x="16" y="46" data-fit="160">productos, carrito,</text>
    <text class="nb" x="16" y="61" data-fit="160">pedidos e historial</text>
  </g>
  <g transform="translate(720,304)">
    <rect class="card n-teal" width="192" height="56" rx="12"/>
    <text class="nt t-teal" x="16" y="24" data-fit="160">Storage</text>
    <text class="nb" x="16" y="43" data-fit="160">fotos de productos</text>
  </g>
  <g transform="translate(264,352)">
    <rect class="card n-violet" width="176" height="64" rx="12"/>
    <text class="nt t-violet" x="16" y="28" data-fit="144">Wompi</text>
    <text class="nb" x="16" y="48" data-fit="144">la clienta paga</text>
  </g>
  <g transform="translate(488,352)">
    <rect class="card n-amber" width="176" height="64" rx="12"/>
    <text class="nt t-amber" x="16" y="28" data-fit="144">Edge Function</text>
    <text class="nb" x="16" y="48" data-fit="144">recibe el aviso de pago</text>
  </g>

  <path class="link" d="M208,168 H236 V208 H262"/>
  <path class="link" d="M208,280 H236 V240 H262"/>
  <path class="link" d="M440,224 H702"/>
  <path class="link" d="M352,272 V350"/>
  <path class="link" d="M440,384 H486"/>
  <path class="link" d="M664,384 H688 V264 H718"/>
</svg>
```

## Peewah para agentes de IA

- **Arquitectura.** El producto es una **capa intermedia** que recibe a agentes de IA externos, valida su identidad y sus permisos, retiene operaciones y audita. Eso es un backend o un API gateway, justo lo que el curso descarta cuando dice que la app no tiene backend propio y habla directo con Supabase. Su propio *Diferido* lo confirma al proponer Edge Functions, un microservicio o un API Gateway, y nada de eso lo hemos visto. Además ponen a los agentes como usuarios de Auth, que está pensado para personas.
- **SDD.** Nueve specs bien hechas y reporte en verde, pero describen un sistema que no van a poder implementar este semestre. Al final de esta sección les dejo una arquitectura sugerida para replantear el MVP.
- **Pendiente.** Les faltan las plataformas en las que corre la app.

### Crítica

- Los documentos son coherentes entre sí: todos describen la capa intermedia para agentes. `AGENTS.md`, eso sí, no dice ni con qué se construye ni en qué plataformas corre.
- Casi todo el PRD (registrar agentes, verificar cada solicitud que llega, que un agente cree eventos) exige una API abierta a terceros. De las nueve specs, solo tres son del lado del organizador: gestionar los agentes, resolver las operaciones de alto impacto y consultar la auditoría. El aviso de operaciones pendientes depende de un mecanismo que la spine no define.
- La propuesta no corresponde a la arquitectura sugerida. Solo el panel del organizador cabe en ella.

```svg
<svg xmlns="http://www.w3.org/2000/svg" id="vaArq" viewBox="0 0 960 400" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="vaArq-ttl vaArq-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="vaArq-ttl">La arquitectura que propone su spine</title>
  <desc id="vaArq-dsc">El organizador usa una app Flutter conectada a Supabase. Los agentes de IA externos entran por un servidor propio, una instancia o máquina virtual aparte, que también escribe en Supabase. Ese servidor no está en el stack del curso.</desc>
  <defs>
    <style>
      #vaArq .card { stroke-width:1.5; }
      #vaArq .hero { stroke-width:2.5; filter:url(#vaArq-lift); }
      #vaArq .n-indigo { fill:#EEF1FF; stroke:#A9B4F2; } #vaArq .t-indigo { fill:#4453C9; }
      #vaArq .n-teal { fill:#E3F6F3; stroke:#86D3CA; } #vaArq .t-teal { fill:#0F8478; }
      #vaArq .n-rose { fill:#FFEBEF; stroke:#F3A3B2; } #vaArq .t-rose { fill:#C2354F; }
      #vaArq .n-violet { fill:#F4EBFF; stroke:#C9A6EE; } #vaArq .t-violet { fill:#7439B8; }
      #vaArq .title { fill:#161A26; font-size:22px; font-weight:700; }
      #vaArq .sub { fill:#79809A; font-size:13.5px; }
      #vaArq .h { font-size:12px; font-weight:700; letter-spacing:.08em; }
      #vaArq .nt { font-size:14px; font-weight:600; }
      #vaArq .nb { fill:#454C61; font-size:12px; }
      #vaArq .link { fill:none; stroke:#556074; stroke-width:1.75; marker-end:url(#vaArq-arrow); }
      #vaArq .link-rose { fill:none; stroke:#C2354F; stroke-width:1.75; marker-end:url(#vaArq-arrow-rose); }
    </style>
    <marker id="vaArq-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <marker id="vaArq-arrow-rose" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#C2354F"/>
    </marker>
    <filter id="vaArq-lift" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#0B1020" flood-opacity="0.14"/>
    </filter>
  </defs>

  <rect width="960" height="400" fill="#FBFBFD" rx="16"/>

  <text class="title" x="48" y="56">La arquitectura que propone su spine</text>
  <text class="sub" x="48" y="80" data-fit="864">En rojo, lo que no está en el stack del curso: un servidor propio para recibir a los agentes.</text>

  <rect x="704" y="104" width="224" height="248" rx="16" fill="none" stroke="#D9DEE8" stroke-width="1.25" stroke-dasharray="6 5"/>
  <text class="h t-teal" x="720" y="128">SUPABASE</text>

  <g transform="translate(48,112)">
    <rect class="card n-violet" width="176" height="64" rx="12"/>
    <text class="nt t-violet" x="16" y="28" data-fit="144">Organizador</text>
    <text class="nb" x="16" y="48" data-fit="144">aprueba o rechaza</text>
  </g>
  <g transform="translate(48,272)">
    <rect class="card n-violet" width="176" height="64" rx="12"/>
    <text class="nt t-violet" x="16" y="28" data-fit="144">Agente de IA</text>
    <text class="nb" x="16" y="48" data-fit="144">externo a Peewah</text>
  </g>
  <g transform="translate(328,104)">
    <rect class="card n-indigo" width="200" height="80" rx="12"/>
    <text class="nt t-indigo" x="16" y="32" data-fit="168">App Flutter</text>
    <text class="nb" x="16" y="54" data-fit="168">panel del organizador</text>
  </g>
  <g transform="translate(328,264)">
    <rect class="card hero n-rose" width="200" height="80" rx="12"/>
    <text class="nt t-rose" x="16" y="28" data-fit="168">Servidor propio</text>
    <text class="nb" x="16" y="48" data-fit="168">instancia o VM aparte</text>
    <text class="nb" x="16" y="64" data-fit="168">valida, retiene y audita</text>
  </g>
  <g transform="translate(720,144)">
    <rect class="card n-teal" width="192" height="64" rx="12"/>
    <text class="nt t-teal" x="16" y="28" data-fit="160">Auth</text>
    <text class="nb" x="16" y="48" data-fit="160">personas y agentes</text>
  </g>
  <g transform="translate(720,232)">
    <rect class="card n-teal" width="192" height="104" rx="12"/>
    <text class="nt t-teal" x="16" y="30" data-fit="160">Base de datos</text>
    <text class="nb" x="16" y="52" data-fit="160">eventos, permisos,</text>
    <text class="nb" x="16" y="68" data-fit="160">solicitudes y bitácora</text>
  </g>

  <path class="link" d="M224,144 H326"/>
  <path class="link" d="M528,144 H702"/>
  <path class="link-rose" d="M224,304 H326"/>
  <path class="link-rose" d="M528,304 H702"/>
</svg>
```

Les sugiero darle la vuelta: en lugar de que agentes externos entren a Peewah, el agente vive dentro de la app. El organizador le pide en la app lo que quiere, la app consulta a Gemini, Gemini devuelve una propuesta y la app la guarda en Supabase; las operaciones de alto impacto esperan la aprobación del organizador, como en su PRD. Así conservan la idea (delegar en la IA sin perder el control) y la arquitectura vuelve a ser una app Flutter que habla con Supabase, más la API de Gemini, sin backend propio. Actualicen el PRD, la spine y las specs con este cambio.

```svg
<svg xmlns="http://www.w3.org/2000/svg" id="vaSug" viewBox="0 0 960 408" width="100%" style="max-width:960px;display:block;margin:0 auto" role="img" aria-labelledby="vaSug-ttl vaSug-dsc" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif">
  <title id="vaSug-ttl">Arquitectura sugerida · la app habla con Gemini y con Supabase</title>
  <desc id="vaSug-dsc">El organizador usa una app Flutter que se conecta directamente a la API de Gemini, a Auth y a la base de datos de Supabase. No hay backend propio.</desc>
  <defs>
    <style>
      #vaSug .card { stroke-width:1.5; }
      #vaSug .hero { stroke-width:2.5; filter:url(#vaSug-lift); }
      #vaSug .n-indigo { fill:#EEF1FF; stroke:#A9B4F2; } #vaSug .t-indigo { fill:#4453C9; }
      #vaSug .n-teal { fill:#E3F6F3; stroke:#86D3CA; } #vaSug .t-teal { fill:#0F8478; }
      #vaSug .n-violet { fill:#F4EBFF; stroke:#C9A6EE; } #vaSug .t-violet { fill:#7439B8; }
      #vaSug .title { fill:#161A26; font-size:22px; font-weight:700; }
      #vaSug .sub { fill:#79809A; font-size:13.5px; }
      #vaSug .nt { font-size:14px; font-weight:600; }
      #vaSug .nb { fill:#454C61; font-size:12px; }
      #vaSug .link { fill:none; stroke:#556074; stroke-width:1.75; marker-end:url(#vaSug-arrow); }
    </style>
    <marker id="vaSug-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" markerUnits="strokeWidth" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 L2.4,5 Z" fill="#556074"/>
    </marker>
    <filter id="vaSug-lift" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#0B1020" flood-opacity="0.14"/>
    </filter>
  </defs>

  <rect width="960" height="408" fill="#FBFBFD" rx="16"/>

  <text class="title" x="48" y="56">Arquitectura sugerida</text>
  <text class="sub" x="48" y="80" data-fit="864">La app Flutter habla directo con Gemini y con Supabase. Sin backend propio.</text>

  <g transform="translate(48,196)">
    <rect class="card n-violet" width="176" height="72" rx="12"/>
    <text class="nt t-violet" x="16" y="30" data-fit="144">Organizador</text>
    <text class="nb" x="16" y="52" data-fit="144">pide y aprueba</text>
  </g>
  <g transform="translate(328,188)">
    <rect class="card hero n-indigo" width="200" height="88" rx="12"/>
    <text class="nt t-indigo" x="16" y="34" data-fit="168">App Flutter</text>
    <text class="nb" x="16" y="56" data-fit="168">propone con Gemini,</text>
    <text class="nb" x="16" y="72" data-fit="168">guarda en Supabase</text>
  </g>
  <g transform="translate(712,112)">
    <rect class="card n-violet" width="200" height="64" rx="12"/>
    <text class="nt t-violet" x="16" y="28" data-fit="168">API de Gemini</text>
    <text class="nb" x="16" y="48" data-fit="168">propone operaciones</text>
  </g>
  <g transform="translate(712,200)">
    <rect class="card n-teal" width="200" height="64" rx="12"/>
    <text class="nt t-teal" x="16" y="28" data-fit="168">Auth</text>
    <text class="nb" x="16" y="48" data-fit="168">sesión del organizador</text>
  </g>
  <g transform="translate(712,288)">
    <rect class="card n-teal" width="200" height="72" rx="12"/>
    <text class="nt t-teal" x="16" y="28" data-fit="168">Base de datos</text>
    <text class="nb" x="16" y="48" data-fit="168">eventos, pendientes</text>
    <text class="nb" x="16" y="63" data-fit="168">y bitácora</text>
  </g>

  <path class="link" d="M224,232 H326"/>
  <path class="link" d="M528,212 H620 V144 H710"/>
  <path class="link" d="M528,232 H710"/>
  <path class="link" d="M528,252 H620 V324 H710"/>
</svg>
```

## Errores que se repitieron

- **Meter en la spine lo que no hemos visto** (Gemini, RLS, gateways, repositorios con interfaces). La regla de la skill es: si hace falta, va en *Diferido* y se pregunta.
- **Un MVP que depende de algo diferido.** Si el núcleo de la app no se puede construir con lo del curso, simúlenlo como datos cargados. Si no saben si se puede, exploren primero y actualicen la spine con el resultado.
- **Una excepción se nombra con su razón.** Si algo obliga a salirse del patrón, como los webhooks de Wompi, la spine dice qué pieza lo cubre y solo eso; lo demás sigue siendo Flutter + Supabase.
- **El PRD promete lo que la spine difiere.** Correos programados, scraping, avisos por WhatsApp, una API para agentes. Si la spine lo deja en *Diferido*, el PRD lo saca del alcance o lo marca como condicional, y su spec espera.
- **"Llega el día y el sistema envía"** necesita un proceso que corra solo, es decir, un servidor o una máquina virtual. Una app Flutter no lo tiene, y ninguno de los tres servicios lo da. Mientras no veamos backend, háganlo **bajo demanda**: la app lo hace cuando alguien pulsa un botón o abre una pantalla.
- **Las versiones.** Lo que se corrige después de la crítica sube a `0.2.0`, no a `0.1.1`.
- **El rol vive en la tabla de usuarios**, unido por el `uuid` de Auth, no en los metadatos de Auth.
- **Un equipo, un solo juego de documentos.** Si cada integrante entrega una versión distinta del mismo proyecto, ninguna es la del equipo.
