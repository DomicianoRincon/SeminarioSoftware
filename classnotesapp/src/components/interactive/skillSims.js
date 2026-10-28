// Interactive skill browser, ported from "Skills en Antigravity CLI" (Computación en Internet II).
// Here it shows the course skills of the IA section (S0063).
// Plain DOM, no React and no imports, same contract as the other simulators:
// every simulator is `mount(element, args) => destroy`.
// The file contents come from tools/skills/ — regenerate with `python3 tools/skills_data.py`.

const STYLE_ID = 'ksim-style';

const CSS = `
.ksim{background:#FBFBFD;color:#161A26;border:1px solid #D9DEE8;border-radius:16px;padding:16px;box-sizing:border-box;
  font-family:Roboto,Arial,sans-serif;font-size:14px;line-height:1.4;max-width:960px;margin:0 auto;container-type:inline-size}
.ksim *{box-sizing:border-box}
.ksim .ks-title{font-size:17px;font-weight:700;margin:0 0 2px}
.ksim .ks-sub{font-size:12.5px;color:#79809A;margin:0 0 12px}
.ksim .ks-tabs{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px}
.ksim .ks-tab{border:1.5px solid #C4CBD8;background:#fff;color:#556074;border-radius:18px;padding:6px 16px;cursor:pointer;
  font:700 13px 'JetBrains Mono',Menlo,Consolas,monospace}
.ksim .ks-tab:hover{box-shadow:0 0 0 3px #E3E7EF}
.ksim .ks-tab.ks-sel{background:var(--c);border-color:var(--c);color:#fff}
.ksim .ks-summary{background:#fff;border:1.5px solid #D9DEE8;border-left:5px solid var(--c);border-radius:12px;padding:10px 14px;
  margin-bottom:12px;font-size:13.5px;line-height:1.5}
.ksim .ks-body{display:flex;gap:12px;align-items:stretch}
.ksim .ks-tree{flex:0 0 230px;min-width:0;background:#fff;border:1.5px solid #D9DEE8;border-radius:12px;padding:10px;
  display:flex;flex-direction:column;gap:4px}
.ksim .ks-head{font-size:11.5px;font-weight:700;letter-spacing:.08em;color:#556074;margin-bottom:4px}
.ksim .ks-dir,.ksim .ks-file{font:12.5px 'JetBrains Mono',Menlo,Consolas,monospace;overflow-wrap:anywhere;text-align:left}
.ksim .ks-dir{color:#A96C05;font-weight:700;padding:3px 0}
.ksim .ks-dir::before{content:'▸ ';color:#C4CBD8}
.ksim .ks-file{border:1.5px solid transparent;background:none;border-radius:8px;padding:4px 8px;cursor:pointer;color:#161A26}
.ksim .ks-file:hover{background:#F3F5F9}
.ksim .ks-file.ks-sel{border-color:var(--c);background:var(--soft);font-weight:700}
.ksim .ks-file.ks-main{font-weight:700}
.ksim .ks-viewer{flex:1 1 0;min-width:0;background:#1F2430;border-radius:12px;display:flex;flex-direction:column;overflow:hidden}
.ksim .ks-bar{display:flex;justify-content:space-between;align-items:center;gap:8px;background:#2A3040;padding:6px 10px}
.ksim .ks-path{font:12px 'JetBrains Mono',Menlo,Consolas,monospace;color:#9AA3B5;overflow-wrap:anywhere;min-width:0}
.ksim .ks-copy{border:1px solid #556074;background:#1F2430;color:#E6EAF2;border-radius:8px;padding:3px 12px;cursor:pointer;
  font:600 12px Roboto,Arial,sans-serif;white-space:nowrap}
.ksim .ks-copy.ks-done{border-color:#3FB37F;color:#7FD9A8}
.ksim .ks-code{margin:0;padding:12px 14px;font:12px/1.55 'JetBrains Mono',Menlo,Consolas,monospace;color:#E6EAF2;
  white-space:pre-wrap;overflow-wrap:anywhere;overflow-y:auto;max-height:440px}
.ksim .ks-use{display:flex;flex-direction:column;gap:6px;margin-top:12px;font-size:13px}
.ksim .ks-use b{font-size:11.5px;letter-spacing:.06em;color:#556074;margin-right:6px}
.ksim .ks-prompt{display:inline-block;background:#F4EBFF;border:1.5px solid #C9A6EE;border-radius:10px;padding:3px 10px;margin:2px 4px 2px 0}
.ksim .ks-out{display:inline-block;font:12px 'JetBrains Mono',Menlo,Consolas,monospace;background:#EFF1F5;border-radius:6px;
  padding:1px 6px;margin:2px 4px 2px 0}
@container (max-width:640px){
  .ksim .ks-body{flex-direction:column}
  .ksim .ks-tree{flex-basis:auto}
  .ksim .ks-viewer{flex:0 0 auto}
  .ksim .ks-code{max-height:360px}
}
`;

const ensureStyle = () => {
  if (typeof document === 'undefined' || document.getElementById(STYLE_ID)) return;
  const style = document.createElement('style');
  style.id = STYLE_ID;
  style.textContent = CSS;
  document.head.appendChild(style);
};

const el = (tag, attrs = {}, ...children) => {
  const node = document.createElement(tag);
  Object.entries(attrs).forEach(([key, value]) => {
    if (value === undefined || value === null || value === false) return;
    if (key === 'class') node.className = value;
    else if (key === 'text') node.textContent = value;
    else if (key.startsWith('on')) node.addEventListener(key.slice(2), value);
    else node.setAttribute(key, value === true ? '' : value);
  });
  children.flat().forEach((child) => {
    if (child === null || child === undefined || child === false) return;
    node.appendChild(typeof child === 'string' ? document.createTextNode(child) : child);
  });
  return node;
};

// <skills-data>
export const SKILLS = [
  {
    "name": "disenador-bd",
    "color": "#4453C9",
    "soft": "#EEF1FF",
    "summary": "Te entrevista sobre la app, arma un borrador de tablas y lo normaliza paso a paso: 1FN, 2FN y 3FN, mostrando qué rompe cada regla y pidiendo tu visto bueno antes de seguir.",
    "prompts": [
      "Ayúdame a diseñar la base de datos de mi app",
      "Lleva docs/modelo.md a tercera forma normal"
    ],
    "writes": [
      "docs/modelo.md"
    ],
    "files": [
      {
        "path": "SKILL.md",
        "content": "---\nname: disenador-bd\ndescription: Diseña la base de datos de la app entrevistando al usuario y la normaliza paso a paso hasta la tercera forma normal (3FN). Deja el modelo en docs/modelo.md. Úsala cuando pidan diseñar la base de datos, armar el modelo de datos, decidir qué tablas hacen falta, normalizar o llevar un modelo a primera, segunda o tercera forma normal.\n---\n\n# Diseñador de base de datos\n\nNo inventas el modelo: lo sacas de las respuestas del usuario y le muestras cada cambio.\n\n## Pasos\n\n1. Si ya existe `docs/modelo.md`, léelo y pregunta si se parte de él o de cero.\n2. **Entrevista.** Haz las preguntas de `references/preguntas.md` en rondas de máximo cuatro, y espera las respuestas antes de seguir. Si una respuesta deja una duda, pregunta otra vez. No supongas.\n3. **Borrador.** Con las respuestas, escribe una lista de entidades con sus atributos, sin normalizar todavía. Muéstrala y pregunta si falta algo.\n4. **Normaliza.** Sigue `references/normalizacion.md`, una forma normal a la vez: 1FN, luego 2FN y luego 3FN. En cada una:\n   - di qué regla revisas;\n   - señala qué atributo o tabla la rompe y por qué, con un dato de ejemplo;\n   - muestra el cambio, que puede ser una tabla nueva, un atributo que se mueve o una llave nueva;\n   - pregunta si el usuario está de acuerdo antes de pasar a la siguiente.\n\n   Si una forma normal ya se cumple, dilo y explica por qué.\n5. **Relaciones.** Para cada FK, pregunta la cardinalidad si no quedó clara: uno a uno, uno a muchos o muchos a muchos. Una relación muchos a muchos se resuelve con una tabla intermedia.\n6. Escribe el resultado en `docs/modelo.md` con el formato de `assets/modelo.md`.\n7. Termina con un resumen: cuántas tablas quedaron, qué cambió en cada forma normal y qué le preguntarías al cliente si hubiera dudas. Sugiere dibujarlo con la skill `mer-svg`.\n\n## Reglas\n\n- Las tablas van en plural y en `snake_case`, igual que sus atributos: `canciones`, `fecha_creacion`.\n- Cada tabla tiene `id (PK)`. Una FK se escribe `<tabla_en_singular>_id (FK a <tabla>)`.\n- No agregues tablas ni atributos que el usuario no haya mencionado. Si crees que falta algo, pregúntalo.\n- No escribas SQL ni código: el resultado es `docs/modelo.md`.\n"
      },
      {
        "path": "assets/modelo.md",
        "content": "# Modelo de datos\n\n## artistas\n\n- id (PK)\n- nombre\n- pais\n\n## canciones\n\n- id (PK)\n- titulo\n- artista_id (FK a artistas)\n\n## playlists\n\n- id (PK)\n- nombre\n- creada_en\n\n## playlists_canciones\n\n- id (PK)\n- playlist_id (FK a playlists)\n- cancion_id (FK a canciones)\n- fecha_agregada\n\n## Relaciones\n\n- Un artista tiene muchas canciones.\n- Una playlist tiene muchas canciones, y una canción está en muchas playlists, a través de playlists_canciones.\n"
      },
      {
        "path": "references/normalizacion.md",
        "content": "# Normalización hasta 3FN\n\nEl ejemplo es una tabla de canciones de una playlist. Así llega del borrador:\n\n- canciones: id, titulo, artista, pais_artista, generos, playlist, duenio_playlist\n\n## 1FN · Un solo valor por celda\n\n**Regla:** cada atributo guarda un único valor y no hay grupos que se repiten.\n\n- **Se rompe** si `generos` guarda \"rock, pop\". Tampoco sirve tener `genero1`, `genero2` y `genero3`.\n- **Arreglo:** el valor múltiple sale a su propia tabla. Como un género tiene muchas canciones, se crean `generos` y la tabla intermedia `canciones_generos`.\n\n## 2FN · Todo depende de la llave entera\n\n**Regla:** se cumple 1FN, y cuando la llave tiene dos partes, cada atributo depende de las dos.\n\n- **Se rompe** en `playlists_canciones` (playlist_id, cancion_id, nombre_playlist, fecha_agregada). `nombre_playlist` depende solo de `playlist_id`.\n- **Arreglo:** `nombre_playlist` se mueve a `playlists`. En la intermedia queda lo que depende del par, que es `fecha_agregada`.\n- Con un `id` simple como llave, la 2FN se cumple sola. Revísala igual en las tablas intermedias.\n\n## 3FN · Nada depende de otro atributo que no es llave\n\n**Regla:** se cumple 2FN, y ningún atributo depende de otro atributo que no sea la llave.\n\n- **Se rompe** en `canciones` con `artista` y `pais_artista`. El país depende del artista, no de la canción: si el artista tiene diez canciones, su país se repite diez veces y puede quedar distinto en una.\n- **Arreglo:** se crea `artistas` (id, nombre, pais). En `canciones` queda `artista_id (FK a artistas)`.\n- **Pista:** si al cambiar un dato hay que cambiarlo en muchas filas, casi siempre rompe 3FN.\n\n## Resultado del ejemplo\n\n- artistas: id, nombre, pais\n- canciones: id, titulo, artista_id\n- generos: id, nombre\n- canciones_generos: id, cancion_id, genero_id\n- usuarios: id, nombre\n- playlists: id, nombre, usuario_id\n- playlists_canciones: id, playlist_id, cancion_id, fecha_agregada\n"
      },
      {
        "path": "references/preguntas.md",
        "content": "# Preguntas de la entrevista\n\nHaz las preguntas de una ronda, espera las respuestas y adapta la ronda siguiente.\n\n## Ronda 1 · La app\n\n- ¿Qué hace la app, en una frase?\n- ¿Quiénes la usan? ¿Hay distintos tipos de usuario?\n- ¿Qué pantallas tiene o va a tener?\n- ¿Qué tiene que recordar la app aunque se cierre?\n\n## Ronda 2 · Las cosas que se guardan\n\nPor cada cosa que mencionó, por ejemplo una canción:\n\n- ¿Qué datos tiene? ¿Cuáles son obligatorios?\n- ¿Qué dato la distingue de las demás?\n- ¿Alguno de sus datos puede tener varios valores, como varios géneros o varios teléfonos?\n- ¿Algún dato se repite igual en muchas filas, como el nombre del artista?\n\n## Ronda 3 · Cómo se relacionan\n\nPor cada par de cosas que se tocan:\n\n- ¿Una A tiene una o muchas B?\n- ¿Una B pertenece a una o a muchas A?\n- ¿La relación tiene datos propios, como la fecha en que se agregó o el orden?\n\n## Ronda 4 · Historia y casos raros\n\n- ¿Hay que guardar el historial o solo el valor actual?\n- ¿Qué pasa con lo relacionado cuando se borra algo?\n- ¿Hay un dato que se calcula a partir de otros, como un total o una edad?\n"
      }
    ]
  },
  {
    "name": "mer-svg",
    "color": "#0F8478",
    "soft": "#E3F6F3",
    "summary": "Dibuja el diagrama entidad-relación de docs/modelo.md como un SVG escrito a mano, con una rejilla, un color por tabla y patas de gallo en las relaciones. La armaste en la sesión 4.",
    "prompts": [
      "Dibuja el MER de la app"
    ],
    "writes": [
      "docs/mer.svg"
    ],
    "files": [
      {
        "path": "SKILL.md",
        "content": "---\nname: mer-svg\ndescription: Dibuja el diagrama entidad-relación (MER) de la app como un archivo SVG, a partir de docs/modelo.md. Úsala cuando pidan el MER, el diagrama de base de datos, el diagrama entidad-relación o \"dibuja el modelo de datos\".\n---\n\n# MER en SVG\n\nEscribes el SVG a mano, como código. No uses Mermaid ni ninguna librería.\n\n## Pasos\n\n1. Lee `docs/modelo.md`. Es la única fuente: no agregues ni quites tablas o atributos.\n2. Lee `references/estilo.md`. Trae las medidas, los colores y cómo se dibuja cada relación.\n3. Lee `assets/ejemplo.svg`. Es un diagrama terminado: el tuyo debe verse igual.\n4. Ordena las tablas para que las que se relacionan queden vecinas.\n5. Calcula la posición de cada tabla con las medidas de `references/estilo.md` antes de escribir.\n6. Escribe el resultado en `docs/mer.svg`.\n7. Revisa: cada tabla y cada atributo de `docs/modelo.md` está en el SVG, y cada relación tiene su línea.\n\n## Reglas\n\n- El texto en SVG no se parte solo: una línea por `<text>`.\n- Fondo claro fijo. Sin modo oscuro, sin imágenes y sin enlaces externos.\n- Los nombres de tablas y atributos van igual que en `docs/modelo.md`.\n- Si una relación no cabe entre tablas vecinas, cambia el orden de las tablas. No cruces líneas sobre una tabla.\n- Una línea solo une las dos tablas de su relación. Si una tabla tiene más de dos relaciones, va en el centro: dos tablas a sus lados y las demás justo debajo, en la misma columna.\n- El pie es una sola línea de máximo 100 caracteres.\n"
      },
      {
        "path": "assets/ejemplo.svg",
        "content": "<svg id=\"merEjemplo\" viewBox=\"0 0 960 560\" role=\"img\" xmlns=\"http://www.w3.org/2000/svg\" font-family=\"ui-sans-serif, -apple-system, 'Segoe UI', Inter, Roboto, Helvetica, Arial, sans-serif\">\n<title id=\"merEjemplo-t\">Ejemplo de diagrama entidad-relación</title>\n<desc id=\"merEjemplo-d\">Seis tablas: sedes, canchas, deportes, usuarios, reservas y pagos, con relaciones uno a muchos.</desc>\n<style>\n#merEjemplo .mono{font-family:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace;font-size:13px;fill:#161A26}\n#merEjemplo .nt{font-size:14px;font-weight:700}\n#merEjemplo .lk{fill:none;stroke:#556074;stroke-width:1.75}\n#merEjemplo .card{stroke-width:1.5}\n#merEjemplo .bd{font-size:10.5px;font-weight:700;fill:#fff;letter-spacing:.04em}\n#merEjemplo .ca{font-size:13px;font-weight:700;fill:#556074}\n</style>\n<rect width=\"960\" height=\"560\" rx=\"16\" fill=\"#FBFBFD\"/>\n<text x=\"32\" y=\"44\" font-size=\"20\" font-weight=\"700\" fill=\"#161A26\">Ejemplo: reserva de canchas</text>\n<text x=\"32\" y=\"66\" font-size=\"13\" fill=\"#79809A\">Cada caja es una tabla; cada línea, una relación entre dos tablas.</text>\n\n<g><rect class=\"card\" x=\"32\" y=\"88\" width=\"176\" height=\"124\" rx=\"10\" fill=\"#EEF1FF\" stroke=\"#A9B4F2\"/>\n<path d=\"M32,120 H208\" stroke=\"#A9B4F2\" stroke-width=\"1.5\"/>\n<text class=\"nt mono\" x=\"120\" y=\"109\" text-anchor=\"middle\" style=\"fill:#4453C9;font-size:14px\">sedes</text>\n<rect x=\"42\" y=\"125\" width=\"26\" height=\"18\" rx=\"9\" fill=\"#4453C9\"/><text class=\"bd\" x=\"55\" y=\"134\" text-anchor=\"middle\" dy=\"0.35em\">PK</text>\n<text class=\"mono\" x=\"78\" y=\"134\" dy=\"0.35em\">id</text>\n<text class=\"mono\" x=\"78\" y=\"162\" dy=\"0.35em\">nombre</text>\n<text class=\"mono\" x=\"78\" y=\"190\" dy=\"0.35em\">direccion</text>\n</g>\n\n<g><rect class=\"card\" x=\"272\" y=\"88\" width=\"176\" height=\"180\" rx=\"10\" fill=\"#E3F6F3\" stroke=\"#86D3CA\"/>\n<path d=\"M272,120 H448\" stroke=\"#86D3CA\" stroke-width=\"1.5\"/>\n<text class=\"nt mono\" x=\"360\" y=\"109\" text-anchor=\"middle\" style=\"fill:#0F8478;font-size:14px\">canchas</text>\n<rect x=\"282\" y=\"125\" width=\"26\" height=\"18\" rx=\"9\" fill=\"#0F8478\"/><text class=\"bd\" x=\"295\" y=\"134\" text-anchor=\"middle\" dy=\"0.35em\">PK</text>\n<text class=\"mono\" x=\"318\" y=\"134\" dy=\"0.35em\">id</text>\n<text class=\"mono\" x=\"318\" y=\"162\" dy=\"0.35em\">nombre</text>\n<text class=\"mono\" x=\"318\" y=\"190\" dy=\"0.35em\">precio_hora</text>\n<rect x=\"282\" y=\"209\" width=\"26\" height=\"18\" rx=\"9\" fill=\"#556074\"/><text class=\"bd\" x=\"295\" y=\"218\" text-anchor=\"middle\" dy=\"0.35em\">FK</text>\n<text class=\"mono\" x=\"318\" y=\"218\" dy=\"0.35em\">sede_id</text>\n<rect x=\"282\" y=\"237\" width=\"26\" height=\"18\" rx=\"9\" fill=\"#556074\"/><text class=\"bd\" x=\"295\" y=\"246\" text-anchor=\"middle\" dy=\"0.35em\">FK</text>\n<text class=\"mono\" x=\"318\" y=\"246\" dy=\"0.35em\">deporte_id</text>\n</g>\n\n<g><rect class=\"card\" x=\"512\" y=\"88\" width=\"176\" height=\"96\" rx=\"10\" fill=\"#FFF3DC\" stroke=\"#F0C572\"/>\n<path d=\"M512,120 H688\" stroke=\"#F0C572\" stroke-width=\"1.5\"/>\n<text class=\"nt mono\" x=\"600\" y=\"109\" text-anchor=\"middle\" style=\"fill:#A96C05;font-size:14px\">deportes</text>\n<rect x=\"522\" y=\"125\" width=\"26\" height=\"18\" rx=\"9\" fill=\"#A96C05\"/><text class=\"bd\" x=\"535\" y=\"134\" text-anchor=\"middle\" dy=\"0.35em\">PK</text>\n<text class=\"mono\" x=\"558\" y=\"134\" dy=\"0.35em\">id</text>\n<text class=\"mono\" x=\"558\" y=\"162\" dy=\"0.35em\">nombre</text>\n</g>\n\n<g><rect class=\"card\" x=\"32\" y=\"332\" width=\"176\" height=\"152\" rx=\"10\" fill=\"#F4EBFF\" stroke=\"#C9A6EE\"/>\n<path d=\"M32,364 H208\" stroke=\"#C9A6EE\" stroke-width=\"1.5\"/>\n<text class=\"nt mono\" x=\"120\" y=\"353\" text-anchor=\"middle\" style=\"fill:#7439B8;font-size:14px\">usuarios</text>\n<rect x=\"42\" y=\"369\" width=\"26\" height=\"18\" rx=\"9\" fill=\"#7439B8\"/><text class=\"bd\" x=\"55\" y=\"378\" text-anchor=\"middle\" dy=\"0.35em\">PK</text>\n<text class=\"mono\" x=\"78\" y=\"378\" dy=\"0.35em\">id</text>\n<text class=\"mono\" x=\"78\" y=\"406\" dy=\"0.35em\">nombre</text>\n<text class=\"mono\" x=\"78\" y=\"434\" dy=\"0.35em\">correo</text>\n<text class=\"mono\" x=\"78\" y=\"462\" dy=\"0.35em\">telefono</text>\n</g>\n\n<g><rect class=\"card\" x=\"272\" y=\"332\" width=\"176\" height=\"180\" rx=\"10\" fill=\"#EEF1FF\" stroke=\"#A9B4F2\"/>\n<path d=\"M272,364 H448\" stroke=\"#A9B4F2\" stroke-width=\"1.5\"/>\n<text class=\"nt mono\" x=\"360\" y=\"353\" text-anchor=\"middle\" style=\"fill:#4453C9;font-size:14px\">reservas</text>\n<rect x=\"282\" y=\"369\" width=\"26\" height=\"18\" rx=\"9\" fill=\"#4453C9\"/><text class=\"bd\" x=\"295\" y=\"378\" text-anchor=\"middle\" dy=\"0.35em\">PK</text>\n<text class=\"mono\" x=\"318\" y=\"378\" dy=\"0.35em\">id</text>\n<rect x=\"282\" y=\"397\" width=\"26\" height=\"18\" rx=\"9\" fill=\"#556074\"/><text class=\"bd\" x=\"295\" y=\"406\" text-anchor=\"middle\" dy=\"0.35em\">FK</text>\n<text class=\"mono\" x=\"318\" y=\"406\" dy=\"0.35em\">cancha_id</text>\n<rect x=\"282\" y=\"425\" width=\"26\" height=\"18\" rx=\"9\" fill=\"#556074\"/><text class=\"bd\" x=\"295\" y=\"434\" text-anchor=\"middle\" dy=\"0.35em\">FK</text>\n<text class=\"mono\" x=\"318\" y=\"434\" dy=\"0.35em\">usuario_id</text>\n<text class=\"mono\" x=\"318\" y=\"462\" dy=\"0.35em\">fecha</text>\n<text class=\"mono\" x=\"318\" y=\"490\" dy=\"0.35em\">hora_inicio</text>\n</g>\n\n<g><rect class=\"card\" x=\"512\" y=\"332\" width=\"176\" height=\"152\" rx=\"10\" fill=\"#E3F6F3\" stroke=\"#86D3CA\"/>\n<path d=\"M512,364 H688\" stroke=\"#86D3CA\" stroke-width=\"1.5\"/>\n<text class=\"nt mono\" x=\"600\" y=\"353\" text-anchor=\"middle\" style=\"fill:#0F8478;font-size:14px\">pagos</text>\n<rect x=\"522\" y=\"369\" width=\"26\" height=\"18\" rx=\"9\" fill=\"#0F8478\"/><text class=\"bd\" x=\"535\" y=\"378\" text-anchor=\"middle\" dy=\"0.35em\">PK</text>\n<text class=\"mono\" x=\"558\" y=\"378\" dy=\"0.35em\">id</text>\n<rect x=\"522\" y=\"397\" width=\"26\" height=\"18\" rx=\"9\" fill=\"#556074\"/><text class=\"bd\" x=\"535\" y=\"406\" text-anchor=\"middle\" dy=\"0.35em\">FK</text>\n<text class=\"mono\" x=\"558\" y=\"406\" dy=\"0.35em\">reserva_id</text>\n<text class=\"mono\" x=\"558\" y=\"434\" dy=\"0.35em\">valor</text>\n<text class=\"mono\" x=\"558\" y=\"462\" dy=\"0.35em\">metodo</text>\n</g>\n\n<path class=\"lk\" d=\"M208,164 H272\"/><path class=\"lk\" d=\"M222,155 V173\"/><path class=\"lk\" d=\"M248,164 L272,153 M248,164 L272,164 M248,164 L272,175\"/>\n<text class=\"ca\" x=\"220\" y=\"146\" text-anchor=\"middle\">1</text>\n<text class=\"ca\" x=\"260\" y=\"146\" text-anchor=\"middle\">N</text>\n\n<path class=\"lk\" d=\"M448,164 H512\"/><path class=\"lk\" d=\"M498,155 V173\"/><path class=\"lk\" d=\"M472,164 L448,153 M472,164 L448,164 M472,164 L448,175\"/>\n<text class=\"ca\" x=\"500\" y=\"146\" text-anchor=\"middle\">1</text>\n<text class=\"ca\" x=\"460\" y=\"146\" text-anchor=\"middle\">N</text>\n\n<path class=\"lk\" d=\"M360,268 V332\"/><path class=\"lk\" d=\"M351,282 H369\"/><path class=\"lk\" d=\"M360,308 L349,332 M360,308 L360,332 M360,308 L371,332\"/>\n<text class=\"ca\" x=\"378\" y=\"287\" text-anchor=\"middle\">1</text>\n<text class=\"ca\" x=\"378\" y=\"326\" text-anchor=\"middle\">N</text>\n\n<path class=\"lk\" d=\"M208,408 H272\"/><path class=\"lk\" d=\"M222,399 V417\"/><path class=\"lk\" d=\"M248,408 L272,397 M248,408 L272,408 M248,408 L272,419\"/>\n<text class=\"ca\" x=\"220\" y=\"390\" text-anchor=\"middle\">1</text>\n<text class=\"ca\" x=\"260\" y=\"390\" text-anchor=\"middle\">N</text>\n\n<path class=\"lk\" d=\"M448,408 H512\"/><path class=\"lk\" d=\"M462,399 V417\"/><path class=\"lk\" d=\"M488,408 L512,397 M488,408 L512,408 M488,408 L512,419\"/>\n<text class=\"ca\" x=\"460\" y=\"390\" text-anchor=\"middle\">1</text>\n<text class=\"ca\" x=\"500\" y=\"390\" text-anchor=\"middle\">N</text>\n\n<text x=\"32\" y=\"544\" font-size=\"12.5\" fill=\"#79809A\">Se lee así: sede→canchas, deporte→canchas, cancha→reservas, usuario→reservas y reserva→pagos; siempre del uno a los muchos.</text>\n</svg>\n"
      },
      {
        "path": "references/estilo.md",
        "content": "# Estilo del MER\n\n## Lienzo\n\n- `<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 960 ALTO\" role=\"img\">`, con `<title>` y `<desc>`.\n- Fondo: `<rect width=\"960\" height=\"ALTO\" rx=\"16\" fill=\"#FBFBFD\"/>`.\n- Título en x=32, y=44, 20 px, negrita, color `#161A26`. Subtítulo en x=32, y=66, 13 px, color `#79809A`.\n- Fuente del texto: `ui-sans-serif, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif`.\n- Fuente de tablas y atributos: `ui-monospace, Menlo, Consolas, monospace`, 13 px, color `#161A26`.\n\n## Rejilla\n\n- Cuatro columnas. La x de cada tabla es 32, 272, 512 o 752. Todas miden 176 de ancho.\n- La primera fila de tablas empieza en y=88.\n- Si hay más de cuatro tablas, la siguiente fila empieza 64 px debajo de la tabla más alta de la fila anterior.\n- ALTO = donde termina la última fila + 48.\n\n## Una tabla\n\nPara una tabla en (X, Y) con N atributos:\n\n- Alto = 40 + 28 × N.\n- Caja: `<rect x=\"X\" y=\"Y\" width=\"176\" height=\"ALTO_TABLA\" rx=\"10\" stroke-width=\"1.5\"/>` con el relleno y el borde de su color.\n- Nombre: centrado en x = X + 88, y = Y + 21, negrita, 14 px, con el color fuerte.\n- Línea bajo el nombre: de (X, Y + 32) a (X + 176, Y + 32), con el color del borde.\n- El atributo número i (el primero es 0) va centrado en y = Y + 46 + 28 × i, con `dy=\"0.35em\"`, en x = X + 46.\n- Insignia PK o FK, a la izquierda del atributo: `<rect x=\"X+10\" y=\"centro-9\" width=\"26\" height=\"18\" rx=\"9\"/>` y encima el texto `PK` o `FK` en blanco, 10.5 px, negrita, centrado en x = X + 23.\n  - PK: relleno con el color fuerte de la tabla.\n  - FK: relleno `#556074`.\n\n## Colores\n\nUn color por tabla, en este orden. Si hay más de cuatro tablas, se repiten.\n\n- Azul: relleno `#EEF1FF`, borde `#A9B4F2`, fuerte `#4453C9`.\n- Verde: relleno `#E3F6F3`, borde `#86D3CA`, fuerte `#0F8478`.\n- Ámbar: relleno `#FFF3DC`, borde `#F0C572`, fuerte `#A96C05`.\n- Morado: relleno `#F4EBFF`, borde `#C9A6EE`, fuerte `#7439B8`.\n\n## Relaciones\n\nTodas las líneas: `fill=\"none\" stroke=\"#556074\" stroke-width=\"1.75\"`.\n\nEntre dos tablas vecinas de la misma fila, la línea es horizontal y va a 76 px del borde de arriba (LY = Y + 76). Sea A el borde derecho de la tabla de la izquierda y B el borde izquierdo de la tabla de la derecha (B = A + 64).\n\n- Línea: `M A,LY H B`.\n- Lado \"uno\": una barra vertical a 14 px de la tabla. Si el \"uno\" está a la izquierda: `M A+14,LY-9 V LY+9`. Si está a la derecha: `M B-14,LY-9 V LY+9`.\n- Lado \"muchos\": una pata de gallo de 24 px que se abre hacia la tabla. Si el \"muchos\" está a la derecha: `M B-24,LY L B,LY-11 M B-24,LY L B,LY M B-24,LY L B,LY+11`. Si está a la izquierda: `M A+24,LY L A,LY-11 M A+24,LY L A,LY M A+24,LY L A,LY+11`.\n- Sobre la línea, a 18 px por encima, un `1` cerca del lado uno y una `N` cerca del lado muchos: 13 px, negrita, color `#556074`.\n\nEntre una tabla y la que está justo debajo, la línea es vertical por el centro de la columna (x = X + 88), desde el borde inferior de la de arriba hasta el borde superior de la de abajo, con la barra y la pata de gallo giradas.\n\n## Pie\n\nUna línea de texto bajo las tablas, 12.5 px, color `#79809A`, que dice cómo se leen las relaciones.\n"
      }
    ]
  },
  {
    "name": "flutter-pantallas",
    "color": "#A96C05",
    "soft": "#FFF3DC",
    "summary": "Maqueta pantallas estáticas con la paleta mínima de widgets y componentes reutilizables. Sin estado ni navegación: sirve para el prototipo. La viste en la sesión 4.",
    "prompts": [
      "Maqueta la pantalla de perfil"
    ],
    "writes": [
      "lib/screens/",
      "lib/components/"
    ],
    "files": [
      {
        "path": "SKILL.md",
        "content": "---\nname: flutter-pantallas\ndescription: Maqueta pantallas estáticas de Flutter con la paleta mínima de widgets del curso y componentes reutilizables. Úsala cuando pidan crear, maquetar o cambiar el aspecto de una pantalla o de una sección de la app.\n---\n\n# Pantallas de Flutter\n\nArmas pantallas estáticas: se ven, pero todavía no navegan ni guardan estado.\n\n## Pasos\n\n1. Lee `references/widgets.md`. Es la paleta: los únicos widgets que puedes usar.\n2. Mira qué hay en `lib/components/`. Si un componente ya sirve, úsalo.\n3. Divide la pantalla en bloques, de arriba hacia abajo.\n4. Lo que se repite, o lo que podría servir en otra pantalla, es un componente: se escribe una vez y recibe sus datos por parámetros.\n5. Escribe cada componente nuevo en su archivo de `lib/components/`, a partir de `assets/component.dart`.\n6. Escribe la pantalla en `lib/screens/`, a partir de `assets/screen.dart`. La pantalla solo acomoda componentes.\n7. Registra la pantalla en `routes` de `lib/main.dart`.\n8. Ejecuta `flutter analyze`.\n\n## Reglas\n\n- Solo `StatelessWidget`. Los datos de ejemplo van escritos en el código.\n- Los botones no navegan ni cambian nada: `onPressed: () {}`.\n- Un componente no conoce la pantalla que lo usa: todo lo que cambia entre un uso y otro llega por el constructor.\n- Si lo pedido necesita algo fuera de la paleta, no lo uses: dilo y propón cómo acercarse con la paleta.\n"
      },
      {
        "path": "assets/component.dart",
        "content": "import 'package:flutter/material.dart';\n\n/// Card that summarizes a contact.\nclass ContactCard extends StatelessWidget {\n  final String image;\n  final String name;\n  final String username;\n\n  const ContactCard({\n    super.key,\n    required this.image,\n    required this.name,\n    required this.username,\n  });\n\n  @override\n  Widget build(BuildContext context) {\n    return Card(\n      elevation: 8,\n      color: Colors.white,\n      shape: RoundedRectangleBorder(\n        borderRadius: BorderRadius.circular(10),\n        side: const BorderSide(color: Color(0xFFDCDDE6), width: 1.5),\n      ),\n      child: Padding(\n        padding: EdgeInsets.all(8),\n        child: Column(\n          mainAxisSize: MainAxisSize.min,\n          spacing: 4,\n          children: [\n            CircleAvatar(radius: 28, backgroundImage: NetworkImage(image)),\n            Text(\n              name,\n              style: const TextStyle(\n                fontSize: 15,\n                fontWeight: FontWeight.w600,\n                color: Color(0xFF1B1B2A),\n              ),\n            ),\n            Text(\n              '@$username',\n              style: const TextStyle(fontSize: 13, color: Color(0xFF5B5E72)),\n            ),\n          ],\n        ),\n      ),\n    );\n  }\n}\n"
      },
      {
        "path": "assets/screen.dart",
        "content": "import 'package:flutter/material.dart';\nimport 'package:mi_app_1/components/profile_info.dart';\nimport 'package:mi_app_1/components/stats_row.dart';\n\n/// Profile of a person.\nclass ProfileScreen extends StatelessWidget {\n  const ProfileScreen({super.key});\n\n  @override\n  Widget build(BuildContext context) {\n    return Scaffold(\n      appBar: AppBar(title: const Text('Perfil')),\n      body: SafeArea(\n        child: SingleChildScrollView(\n          padding: const EdgeInsets.all(16),\n          child: Column(\n            spacing: 16,\n            children: [\n              ProfileInfo(\n                image: 'https://picsum.photos/400',\n                name: 'Mariana Valenzuela',\n                username: 'marianav',\n                role: 'Diseñadora de Producto',\n                email: 'm.val@estudio.com',\n                location: 'Cali, CO',\n              ),\n              StatsRow(posts: '128', followers: '2.4k', following: '310'),\n            ],\n          ),\n        ),\n      ),\n    );\n  }\n}\n"
      },
      {
        "path": "references/widgets.md",
        "content": "# Paleta de widgets\n\nSolo estos. Entre paréntesis, las propiedades que se usan.\n\n## Contenido\n\n- `Text` (`style`, `maxLines`, `overflow`) con `TextStyle` (`fontSize`, `fontWeight`, `color`). Colores con `Colors.` o `Color(0xFF...)`.\n- `Icon` (`size`, `color`).\n- `Image.network` e `Image.asset` (`width`, `height`, `fit`). Imagen de ejemplo: `https://picsum.photos/400`.\n- `CircleAvatar` (`radius`, `backgroundImage: NetworkImage(...)`).\n\n## Botones\n\n- `ElevatedButton`, `OutlinedButton`, `TextButton` (`onPressed`, `child`, `style` con `styleFrom`) e `IconButton` (`onPressed`, `icon`).\n\n## Entrada\n\n- `TextField`, solo su aspecto: `decoration: InputDecoration(labelText, hintText, prefixIcon, border)`, `obscureText`, `keyboardType`. Sin `controller`.\n\n## Acomodar\n\n- `Column` y `Row` (`mainAxisAlignment`, `crossAxisAlignment`, `mainAxisSize`, `spacing`, `children`).\n- `SizedBox` para separar (`width`, `height`).\n- `Expanded` (`flex`) y `Spacer`, solo dentro de `Row` o `Column`.\n- `Padding` con `EdgeInsets.all`, `symmetric` u `only`.\n- `Container` (`width`, `height`, `padding`, `margin`, `decoration: BoxDecoration(color, border, borderRadius)`). Para recortar al hijo, `clipBehavior: Clip.antiAlias`.\n- `Card` (`elevation`, `color`, `shape: RoundedRectangleBorder(borderRadius, side)`), para una tarjeta.\n- `Center`.\n- `SingleChildScrollView` (`padding`, `scrollDirection`). Adentro no van `Expanded` ni `Spacer`.\n\n## Estructura de la pantalla\n\n- `Scaffold` (`appBar`, `body`, `backgroundColor`, `floatingActionButton`, `bottomNavigationBar`).\n- `SafeArea`: el `body` siempre empieza con uno.\n- `AppBar` (`title`, `leading`, `actions`, `centerTitle`, `backgroundColor`, `foregroundColor`).\n- `BottomNavigationBar` (`items`, `currentIndex` fijo). Solo se ve: no responde al toque.\n- `FloatingActionButton` (`onPressed`, `child`).\n\n## Fuera de la paleta\n\nNo se usan todavía. En su lugar:\n\n- `ListView`, `GridView`: una `Column` o una `Row` dentro de un `SingleChildScrollView`.\n- `ListTile`: una `Row` dentro de un `Card` o de un `Container`.\n- `Stack`, `Positioned`, `Wrap`, `Align`: reorganiza con `Column`, `Row` y `mainAxisAlignment`.\n- `ClipRRect`: `Container` con `clipBehavior`.\n- `GestureDetector`, `InkWell`: un botón de la paleta.\n- `StatefulWidget`, `setState`, `Switch`, `Checkbox`: no hay estado.\n- `Navigator`, `showDialog`, `SnackBar`: no hay navegación.\n- `FutureBuilder`, `StreamBuilder` y cualquier paquete nuevo.\n"
      }
    ]
  },
  {
    "name": "flutter-componentes",
    "color": "#7439B8",
    "soft": "#F4EBFF",
    "summary": "Crea y conecta componentes como en las sesiones 6 a 8: datos por el constructor, eventos con Function(), copyWith en el modelo y el estado y el Navigator solo en la Screen.",
    "prompts": [
      "Saca la tarjeta de producto a un componente",
      "Haz que tocar la card abra el detalle"
    ],
    "writes": [
      "lib/components/",
      "lib/models/"
    ],
    "files": [
      {
        "path": "SKILL.md",
        "content": "---\nname: flutter-componentes\ndescription: Crea y conecta componentes reutilizables de Flutter al estilo del curso. Los datos bajan por el constructor, los eventos suben con funciones y el estado vive en la Screen o en un formulario. Úsala cuando pidan crear un componente, sacar un pedazo de pantalla a un componente, agregarle un evento (onTap, onDelete, onAdd) a una card o a una lista, o conectar un componente con el estado de la pantalla.\n---\n\n# Componentes de Flutter\n\nUn componente no sabe quién lo usa: recibe lo que muestra y avisa lo que pasó.\n\n## Pasos\n\n1. Lee `references/reglas.md`. Dice quién guarda estado, cómo bajan los datos y cómo suben los eventos.\n2. Mira `lib/components/` y `lib/models/`. Si ya hay un componente o un modelo que sirve, úsalo o amplíalo.\n3. Decide el tipo de componente:\n   - Si solo muestra datos y avisa toques, es un `StatelessWidget`. Plantilla: `assets/product_card.dart`.\n   - Si solo reparte una lista entre cards, es un `StatelessWidget` que pasa las funciones. Plantilla: `assets/product_list.dart`.\n   - Si el usuario escribe en él, es un formulario `StatefulWidget`. Plantilla: `assets/product_form.dart`.\n4. Haz la lista de lo que recibe: los datos, como campos `final`, y los eventos, como `Function()` o `Function(Tipo)`.\n5. Si el componente trabaja con un objeto, búscalo o créalo en `lib/models/` con `copyWith`. Plantilla: `assets/product.dart`.\n6. Escribe el componente en su propio archivo de `lib/components/`.\n7. Conéctalo en la Screen, que es la dueña del estado. Plantilla: `assets/shopping_screen.dart`. Cada función que pasa la Screen hace su `setState` o su llamada al `Navigator`.\n8. Ejecuta `flutter analyze` y corrige hasta que no haya avisos.\n9. Termina con un resumen de tres líneas: qué recibe el componente, qué avisa y quién guarda el estado.\n\n## Reglas\n\n- Las plantillas usan `my_app` como paquete. Cámbialo por el `name` de `pubspec.yaml`.\n- Nunca pongas `setState` ni `Navigator` dentro de un componente que no sea la Screen.\n- No agregues paquetes nuevos.\n- Si lo pedido rompe una regla de `references/reglas.md`, no lo hagas: di cuál y propón cómo hacerlo dentro de las reglas.\n"
      },
      {
        "path": "assets/product.dart",
        "content": "/// A product in the shopping list.\nclass Product {\n  final String name;\n  final int quantity;\n  final bool isBought;\n\n  const Product({\n    required this.name,\n    required this.quantity,\n    this.isBought = false,\n  });\n\n  Product copyWith({String? name, int? quantity, bool? isBought}) {\n    return Product(\n      name: name ?? this.name,\n      quantity: quantity ?? this.quantity,\n      isBought: isBought ?? this.isBought,\n    );\n  }\n}\n"
      },
      {
        "path": "assets/product_card.dart",
        "content": "import 'package:flutter/material.dart';\nimport 'package:my_app/models/product.dart';\n\n/// Card for a product: name, quantity and its actions.\nclass ProductCard extends StatelessWidget {\n  final Product product;\n  final Function() onTap;\n  final Function() onToggleBought;\n  final Function() onDelete;\n\n  const ProductCard({\n    super.key,\n    required this.product,\n    required this.onTap,\n    required this.onToggleBought,\n    required this.onDelete,\n  });\n\n  @override\n  Widget build(BuildContext context) {\n    return GestureDetector(\n      onTap: () => onTap(),\n      child: Container(\n        margin: const EdgeInsets.only(bottom: 12),\n        padding: const EdgeInsets.all(12),\n        decoration: BoxDecoration(\n          color: Colors.white,\n          borderRadius: BorderRadius.circular(16),\n          border: Border.all(color: const Color(0xFFDCDDE6)),\n        ),\n        child: Row(\n          children: [\n            Expanded(\n              child: Column(\n                crossAxisAlignment: CrossAxisAlignment.start,\n                children: [\n                  Text(\n                    product.name,\n                    maxLines: 1,\n                    overflow: TextOverflow.ellipsis,\n                    style: const TextStyle(\n                      fontSize: 16,\n                      fontWeight: FontWeight.bold,\n                    ),\n                  ),\n                  Text(\n                    'Cantidad: ${product.quantity}',\n                    style: const TextStyle(color: Colors.black54),\n                  ),\n                ],\n              ),\n            ),\n            IconButton(\n              onPressed: () => onToggleBought(),\n              icon: Icon(\n                product.isBought\n                    ? Icons.check_circle\n                    : Icons.radio_button_unchecked,\n                color: Colors.green,\n              ),\n            ),\n            IconButton(\n              onPressed: () => onDelete(),\n              icon: const Icon(Icons.delete_outline),\n            ),\n          ],\n        ),\n      ),\n    );\n  }\n}\n"
      },
      {
        "path": "assets/product_form.dart",
        "content": "import 'package:flutter/material.dart';\nimport 'package:my_app/models/product.dart';\n\n/// Form that builds a product and hands it to whoever uses it.\nclass ProductForm extends StatefulWidget {\n  final Function(Product) onAdd;\n\n  const ProductForm({super.key, required this.onAdd});\n\n  @override\n  State<ProductForm> createState() => _ProductFormState();\n}\n\nclass _ProductFormState extends State<ProductForm> {\n  final _nameController = TextEditingController();\n  final _quantityController = TextEditingController();\n  bool _showError = false;\n\n  void _submit() {\n    final quantity = int.tryParse(_quantityController.text);\n    if (_nameController.text.isEmpty || quantity == null) {\n      setState(() {\n        _showError = true;\n      });\n      return;\n    }\n    widget.onAdd(Product(name: _nameController.text, quantity: quantity));\n    _nameController.clear();\n    _quantityController.clear();\n    setState(() {\n      _showError = false;\n    });\n  }\n\n  @override\n  Widget build(BuildContext context) {\n    return Column(\n      children: [\n        TextField(\n          controller: _nameController,\n          decoration: const InputDecoration(labelText: 'Producto'),\n        ),\n        TextField(\n          controller: _quantityController,\n          keyboardType: TextInputType.number,\n          decoration: const InputDecoration(labelText: 'Cantidad'),\n        ),\n        if (_showError)\n          const Text(\n            'Escribe el producto y una cantidad',\n            style: TextStyle(color: Colors.red),\n          ),\n        FilledButton(onPressed: () => _submit(), child: const Text('Agregar')),\n      ],\n    );\n  }\n\n  @override\n  void dispose() {\n    _nameController.dispose();\n    _quantityController.dispose();\n    super.dispose();\n  }\n}\n"
      },
      {
        "path": "assets/product_list.dart",
        "content": "import 'package:flutter/material.dart';\nimport 'package:my_app/components/product_card.dart';\nimport 'package:my_app/models/product.dart';\n\n/// List of products, or a message when there are none.\nclass ProductList extends StatelessWidget {\n  final List<Product> products;\n  final Function(Product) onOpen;\n  final Function(Product) onToggleBought;\n  final Function(Product) onDelete;\n\n  const ProductList({\n    super.key,\n    required this.products,\n    required this.onOpen,\n    required this.onToggleBought,\n    required this.onDelete,\n  });\n\n  @override\n  Widget build(BuildContext context) {\n    if (products.isEmpty) {\n      return const Padding(\n        padding: EdgeInsets.all(24),\n        child: Text(\n          'Todavía no hay productos',\n          style: TextStyle(color: Colors.grey),\n        ),\n      );\n    }\n    return Column(\n      children: [\n        for (final product in products)\n          ProductCard(\n            product: product,\n            onTap: () => onOpen(product),\n            onToggleBought: () => onToggleBought(product),\n            onDelete: () => onDelete(product),\n          ),\n      ],\n    );\n  }\n}\n"
      },
      {
        "path": "assets/shopping_screen.dart",
        "content": "import 'package:flutter/material.dart';\nimport 'package:my_app/components/product_form.dart';\nimport 'package:my_app/components/product_list.dart';\nimport 'package:my_app/models/product.dart';\n\n/// Screen that owns the shopping list.\nclass ShoppingScreen extends StatefulWidget {\n  const ShoppingScreen({super.key});\n\n  @override\n  State<ShoppingScreen> createState() => _ShoppingScreenState();\n}\n\nclass _ShoppingScreenState extends State<ShoppingScreen> {\n  final List<Product> _products = [];\n\n  void _addProduct(Product product) {\n    setState(() {\n      _products.add(product);\n    });\n  }\n\n  void _toggleBought(Product product) {\n    setState(() {\n      final index = _products.indexOf(product);\n      _products[index] = product.copyWith(isBought: !product.isBought);\n    });\n  }\n\n  void _deleteProduct(Product product) {\n    setState(() {\n      _products.remove(product);\n    });\n  }\n\n  void _openProduct(Product product) {\n    Navigator.pushNamed(context, '/product', arguments: product);\n  }\n\n  @override\n  Widget build(BuildContext context) {\n    return Scaffold(\n      appBar: AppBar(title: const Text('Lista de compras')),\n      body: SafeArea(\n        child: SingleChildScrollView(\n          padding: const EdgeInsets.all(16),\n          child: Column(\n            children: [\n              ProductForm(onAdd: (product) => _addProduct(product)),\n              ProductList(\n                products: _products,\n                onOpen: (product) => _openProduct(product),\n                onToggleBought: (product) => _toggleBought(product),\n                onDelete: (product) => _deleteProduct(product),\n              ),\n            ],\n          ),\n        ),\n      ),\n    );\n  }\n}\n"
      },
      {
        "path": "references/reglas.md",
        "content": "# Reglas de los componentes\n\n## Quién guarda estado\n\nSolo dos tipos de widget son `StatefulWidget`:\n\n- **La Screen**, dueña de los datos de la pantalla, por ejemplo `List<Product> _products`.\n- **El formulario**, que guarda solo el borrador: sus `TextEditingController` y el aviso de error.\n\nTodo lo demás es `StatelessWidget`: cards, listas, encabezados y botones.\n\n## Los datos bajan\n\n- Llegan por el constructor, en campos `final` con `required`.\n- El componente no los cambia. Para cambiar un objeto, la Screen lo reemplaza con `copyWith`:\n  `_products[index] = product.copyWith(isBought: true)`.\n- Si una lista no usa un dato y solo lo pasa a sus cards, está bien. Si son más de tres niveles, avísalo: es prop drilling.\n\n## Los eventos suben\n\n- Con el tipo función: `Function()` si no lleva datos y `Function(Product)` si lleva el objeto.\n- Nunca uses `VoidCallback` ni `ValueChanged`.\n- Al widget de Flutter se le pasa envuelta: `onPressed: () => onDelete()`.\n- La card avisa sin datos (`onDelete()`) y la lista le agrega el objeto (`onDelete: () => onDelete(product)`).\n- Para tocar una card entera, envuelve su `Container` en un `GestureDetector` con `onTap`.\n- El formulario sube el objeto terminado (`widget.onAdd(product)`), limpia sus campos y no se lo queda.\n\n## Navegación\n\n- Solo la Screen llama al `Navigator`. Un componente avisa con una función, como `onOpen`, y la Screen hace el `pushNamed`.\n- Solo hay rutas nombradas, registradas en `routes:` de `lib/main.dart`.\n- Los datos para la pantalla nueva van en `arguments`.\n\n## Código\n\n- Imports del proyecto con `package:`, nunca relativos.\n- El código va en inglés y los textos que ve el usuario, en español.\n- Sin comentarios, salvo una línea `///` sobre cada clase pública.\n- Un archivo por componente, con el nombre en `snake_case`: `product_card.dart` para `ProductCard`.\n- Para redondear una imagen, usa un `Container` con `borderRadius` y `clipBehavior: Clip.antiAlias`. Nunca uses `ClipRRect`.\n- Si un formulario tiene un `TextEditingController`, debe tener también su `dispose()`.\n"
      }
    ]
  }
];
// </skills-data>

const copyText = (text) => {
  if (typeof navigator !== 'undefined' && navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(text);
  }
  const area = el('textarea', { style: 'position:fixed;opacity:0' });
  area.value = text;
  document.body.appendChild(area);
  area.select();
  document.execCommand('copy');
  area.remove();
  return Promise.resolve();
};

// Folder rows and file rows in the order they appear on disk: SKILL.md first, then each folder.
export const skillTree = (skill) => {
  const rows = [];
  const seen = new Set();
  skill.files.forEach((file) => {
    const parts = file.path.split('/');
    parts.slice(0, -1).forEach((dir, index) => {
      const key = parts.slice(0, index + 1).join('/');
      if (!seen.has(key)) {
        seen.add(key);
        rows.push({ kind: 'dir', name: `${dir}/`, depth: index + 1 });
      }
    });
    rows.push({ kind: 'file', name: parts[parts.length - 1], path: file.path, depth: parts.length });
  });
  return rows;
};

const mountSkillFiles = (root, args = []) => {
  ensureStyle();
  const container = el('div', { class: 'ksim', 'data-testid': 'skill-files' });
  root.replaceChildren(container);

  let skill = SKILLS.find((item) => item.name === args[0]) || SKILLS[0];
  let path = skill ? skill.files[0].path : null;

  const tabs = el('div', { class: 'ks-tabs', role: 'tablist' });
  const summary = el('div', { class: 'ks-summary' });
  const tree = el('div', { class: 'ks-tree' });
  const pathLabel = el('span', { class: 'ks-path' });
  const copy = el('button', { class: 'ks-copy', type: 'button', text: 'Copiar' });
  const code = el('pre', { class: 'ks-code', 'data-testid': 'skill-content' });
  const use = el('div', { class: 'ks-use' });

  copy.addEventListener('click', () => {
    const file = skill.files.find((item) => item.path === path);
    copyText(file.content).then(() => {
      copy.textContent = 'Copiado';
      copy.classList.add('ks-done');
    }, () => { copy.textContent = 'No se pudo copiar'; });
  });

  const render = () => {
    container.style.setProperty('--c', skill.color);
    container.style.setProperty('--soft', skill.soft);
    [...tabs.children].forEach((tab) => {
      const on = tab.dataset.skill === skill.name;
      tab.classList.toggle('ks-sel', on);
      tab.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    summary.textContent = skill.summary;
    tree.replaceChildren(el('div', { class: 'ks-head', text: 'CARPETA' }),
      el('div', { class: 'ks-dir', text: `.agents/skills/${skill.name}/` }),
      ...skillTree(skill).map((row) => (row.kind === 'dir'
        ? el('div', { class: 'ks-dir', style: `margin-left:${row.depth * 12}px`, text: row.name })
        : el('button', {
          class: `ks-file${row.path === path ? ' ks-sel' : ''}${row.path === 'SKILL.md' ? ' ks-main' : ''}`,
          style: `margin-left:${row.depth * 12}px`,
          type: 'button',
          'data-path': row.path,
          onclick: () => { path = row.path; render(); },
        }, row.name))));
    const file = skill.files.find((item) => item.path === path);
    pathLabel.textContent = `.agents/skills/${skill.name}/${file.path}`;
    code.textContent = file.content;
    copy.textContent = 'Copiar';
    copy.classList.remove('ks-done');
    use.replaceChildren(
      el('div', {}, el('b', { text: 'PÍDELE' }), skill.prompts.map((text) => el('span', { class: 'ks-prompt', text: `«${text}»` }))),
      el('div', {}, el('b', { text: 'ESCRIBE' }), skill.writes.map((text) => el('span', { class: 'ks-out', text }))));
  };

  SKILLS.forEach((item) => tabs.append(el('button', {
    class: 'ks-tab',
    type: 'button',
    role: 'tab',
    'data-skill': item.name,
    style: `--c:${item.color}`,
    onclick: () => { skill = item; path = item.files[0].path; render(); },
  }, item.name)));

  container.append(
    el('div', { class: 'ks-title', text: 'Las skills del curso, archivo por archivo' }),
    el('div', { class: 'ks-sub', text: 'Elige una skill y un archivo. Créalo con ese nombre en esa carpeta y pega el contenido.' }),
    tabs, summary,
    el('div', { class: 'ks-body' }, tree, el('div', { class: 'ks-viewer' }, el('div', { class: 'ks-bar' }, pathLabel, copy), code)),
    use);
  if (skill) render();
  return () => root.replaceChildren();
};

export const SIMS = Object.freeze({
  'skill-files': mountSkillFiles,
});
