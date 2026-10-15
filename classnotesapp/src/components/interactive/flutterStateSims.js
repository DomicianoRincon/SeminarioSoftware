// Interactive simulators for Flutter state (StatefulWidget, setState, lifecycle).
// Plain DOM, no React: the same file is copied into the session decks, so it must
// not import anything. Every simulator is `mount(element, args) => destroy`.

const STYLE_ID = 'fsim-style';

const CSS = `
.fsim{--fs-bg:#FBFBFD;--fs-ink:#1C1B1F;--fs-muted:#5F6368;--fs-line:#E3E3EA;--fs-accent:#6750A4;
  --fs-accent-soft:#EADDFF;--fs-appbar:#D0BCFF;--fs-flash:#FFE082;--fs-ok:#2E7D32;--fs-err:#C62828;
  background:var(--fs-bg);color:var(--fs-ink);border:1px solid var(--fs-line);border-radius:16px;
  padding:16px;font-family:Roboto,Arial,sans-serif;font-size:14px;line-height:1.4;
  display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start;box-sizing:border-box;max-width:960px;margin:0 auto;overflow:hidden}
@media (max-width:480px){.fsim{padding:12px;gap:12px}}
.fsim *{box-sizing:border-box}
.fsim .fs-col{display:flex;flex-direction:column;gap:12px;align-items:center;flex:0 1 280px;min-width:0;max-width:100%;margin:0 auto}
.fsim .fs-side{flex:1 1 300px;min-width:0;max-width:100%;display:flex;flex-direction:column;gap:12px}
.fsim .fs-phone{width:260px;max-width:100%;height:470px;border:10px solid #1C1B1F;border-radius:32px;background:#FEF7FF;
  overflow:hidden;display:flex;flex-direction:column;position:relative;box-shadow:0 6px 18px rgba(0,0,0,.18)}
.fsim .fs-status{height:20px;font-size:11px;color:#1C1B1F;display:flex;justify-content:space-between;padding:2px 14px 0}
.fsim .fs-appbar{background:var(--fs-appbar);padding:12px 14px;font-size:17px;font-weight:500;min-height:48px;
  display:flex;align-items:center;justify-content:space-between;gap:8px}
.fsim .fs-appbar small{font-size:12px;font-weight:400;color:#49454F}
.fsim .fs-body{flex:1;overflow-y:auto;padding:14px;position:relative}
.fsim .fs-center{height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;gap:8px;color:#49454F}
.fsim .fs-big{font-size:44px;color:var(--fs-ink);font-weight:400}
.fsim .fs-fab{position:absolute;right:14px;bottom:14px;width:52px;height:52px;border-radius:16px;border:0;
  background:var(--fs-accent-soft);color:#21005D;font-size:28px;cursor:pointer;box-shadow:0 3px 8px rgba(0,0,0,.25);
  display:flex;align-items:center;justify-content:center}
.fsim .fs-fab:active{transform:scale(.94)}
.fsim .fs-panel{background:#fff;border:1px solid var(--fs-line);border-radius:12px;padding:10px 12px}
.fsim .fs-panel h4{margin:0 0 6px;font-size:12px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--fs-muted)}
.fsim .fs-row{display:flex;flex-wrap:wrap;justify-content:space-between;gap:2px 12px;padding:3px 6px;border-radius:6px;
  font-family:'JetBrains Mono',Menlo,Consolas,monospace;font-size:13px}
.fsim .fs-row span:last-child{text-align:right;overflow-wrap:anywhere}
.fsim .fs-dark{background:#1E1E2E;color:#CDD6F4;border-radius:12px;padding:10px 0;
  font-family:'JetBrains Mono',Menlo,Consolas,monospace;font-size:12.5px;overflow-x:auto}
.fsim .fs-dark h4{margin:0 12px 6px;font-size:11px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:#7F849C;font-family:Roboto,Arial,sans-serif}
.fsim .fs-code-line{white-space:pre;padding:0 12px;border-left:3px solid transparent;transition:background .4s}
.fsim .fs-code-line.fs-on{background:rgba(249,226,175,.18);border-left-color:#F9E2AF}
.fsim .fs-kw{color:#CBA6F7}.fsim .fs-str{color:#A6E3A1}.fsim .fs-num{color:#FAB387}.fsim .fs-type{color:#89DCEB}
.fsim .fs-ann{color:#F38BA8}
.fsim .fs-log{min-height:96px;max-height:150px;overflow-y:auto;padding:0 12px}
.fsim .fs-log div{white-space:pre-wrap;color:#A6ADC8}
.fsim .fs-log div:last-child{color:#fff}
.fsim .fs-log .fs-log-err{color:#F38BA8!important}
.fsim .fs-log .fs-log-ok{color:#A6E3A1!important}
.fsim .fs-flash{animation:fsimFlash 1s ease-out}
@keyframes fsimFlash{0%{background:var(--fs-flash)}100%{background:transparent}}
.fsim .fs-controls{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
.fsim .fs-btn{border:1px solid var(--fs-accent);background:#fff;color:var(--fs-accent);border-radius:20px;
  padding:6px 14px;font:500 13px Roboto,Arial,sans-serif;cursor:pointer}
.fsim .fs-btn:hover{background:#F6F0FF}
.fsim .fs-btn.fs-solid{background:var(--fs-accent);color:#fff}
.fsim .fs-btn:disabled{opacity:.45;cursor:default}
.fsim .fs-switch{display:flex;align-items:center;gap:8px;font-size:13px;cursor:pointer;user-select:none}
.fsim .fs-switch input{accent-color:var(--fs-accent);width:16px;height:16px}
.fsim .fs-note{font-size:13px;color:var(--fs-muted);min-height:36px;text-align:center;max-width:300px}
.fsim .fs-note.fs-warn{color:var(--fs-err)}
.fsim .fs-field{width:100%;border:1px solid #79747E;border-radius:4px;padding:8px 10px;font:14px Roboto,Arial,sans-serif;
  background:transparent;margin-bottom:8px;color:var(--fs-ink)}
.fsim .fs-field:focus{outline:2px solid var(--fs-accent);border-color:transparent}
.fsim .fs-label{font-size:11px;color:#49454F;margin:0 0 2px 2px}
.fsim .fs-filled{width:100%;border:0;border-radius:20px;padding:10px;background:var(--fs-accent);color:#fff;
  font:500 14px Roboto,Arial,sans-serif;cursor:pointer;margin-bottom:12px}
.fsim .fs-text-item{font-size:14px;padding:2px 0;color:var(--fs-ink)}
.fsim .fs-empty{font-size:13px;color:#79747E;text-align:center;padding:12px 0}
.fsim .fs-card{display:flex;align-items:center;gap:12px;background:#fff;border-radius:16px;padding:10px;margin-bottom:10px;
  box-shadow:0 2px 8px rgba(103,80,164,.16)}
.fsim .fs-cover{width:56px;height:56px;border-radius:12px;overflow:hidden;flex:0 0 56px;
  background:linear-gradient(135deg,#B69DF8,#6750A4)}
.fsim .fs-cover img{width:100%;height:100%;object-fit:cover;display:block}
.fsim .fs-card-text{flex:1;min-width:0}
.fsim .fs-card-title{font-weight:600;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.fsim .fs-card-artist{font-size:12px;color:#625B71;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.fsim .fs-card-icon{color:var(--fs-accent);font-size:20px}
.fsim .fs-tree{list-style:none;margin:0;padding:0 0 0 14px;border-left:1px dashed #C9C5D0}
.fsim .fs-tree-root{border-left:0;padding-left:0}
.fsim .fs-node{display:inline-flex;align-items:center;gap:8px;margin:3px 0;padding:3px 8px;border-radius:8px;
  border:1px solid var(--fs-line);background:#fff;font-family:'JetBrains Mono',Menlo,Consolas,monospace;font-size:12.5px}
.fsim .fs-node b{font-weight:600}
.fsim .fs-node.fs-stateful{border-color:var(--fs-accent)}
.fsim .fs-node.fs-state{background:var(--fs-accent-soft);border-color:var(--fs-accent)}
.fsim .fs-id{font-size:11px;color:#fff;background:#625B71;border-radius:10px;padding:0 7px}
.fsim .fs-node.fs-state .fs-id{background:var(--fs-accent)}
.fsim .fs-pair{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.fsim .fs-link{font-size:11px;color:var(--fs-muted)}
.fsim .fs-steps{display:flex;flex-wrap:wrap;gap:6px}
.fsim .fs-step{font-family:'JetBrains Mono',Menlo,Consolas,monospace;font-size:12px;padding:3px 9px;border-radius:12px;
  border:1px solid var(--fs-line);color:#9E9AA7;background:#fff}
.fsim .fs-step.fs-done{color:var(--fs-ink);border-color:var(--fs-accent);background:var(--fs-accent-soft)}
.fsim .fs-step.fs-dead{color:#fff;border-color:#625B71;background:#625B71}
.fsim .fs-list-title{font-size:13px;font-weight:600;color:#49454F;margin:2px 0 6px}
.fsim .fs-seg{display:inline-flex;border:1px solid var(--fs-accent);border-radius:20px;overflow:hidden}
.fsim .fs-seg button{border:0;background:#fff;color:var(--fs-accent);padding:6px 14px;font:500 13px Roboto,Arial,sans-serif;cursor:pointer}
.fsim .fs-seg button.fs-sel{background:var(--fs-accent);color:#fff}
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

const flash = (node) => {
  if (!node) return;
  node.classList.remove('fs-flash');
  void node.offsetWidth;
  node.classList.add('fs-flash');
};

const DART_KEYWORDS = new Set(['class', 'extends', 'void', 'return', 'final', 'const', 'if', 'for', 'in', 'this', 'super', 'late', 'true', 'false']);
const DART_TYPES = new Set(['int', 'String', 'List', 'Widget', 'State', 'StatefulWidget', 'StatelessWidget', 'BuildContext', 'Scaffold', 'Text', 'TextEditingController', 'Column', 'Song', 'SongCard', 'FloatingActionButton', 'TextField', 'MyHomePage', 'GreetingScreen']);
const DART_TOKEN = /('[^']*')|(@\w+)|(\b\d+\b)|(\b[A-Za-z_]\w*\b)/g;

const escapeHtml = (text) => text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const highlightDart = (line) => {
  let html = '';
  let last = 0;
  line.replace(DART_TOKEN, (match, str, ann, num, word, offset) => {
    html += escapeHtml(line.slice(last, offset));
    last = offset + match.length;
    const kind = str ? 'fs-str' : ann ? 'fs-ann' : num ? 'fs-num' : DART_KEYWORDS.has(word) ? 'fs-kw' : DART_TYPES.has(word) ? 'fs-type' : '';
    html += kind ? `<span class="${kind}">${escapeHtml(match)}</span>` : escapeHtml(match);
    return match;
  });
  return html + escapeHtml(line.slice(last));
};

const codePanel = (title) => {
  const box = el('div', { class: 'fs-dark' }, el('h4', { text: title }));
  const body = el('div');
  box.appendChild(body);
  let lines = [];
  const setCode = (source) => {
    body.replaceChildren();
    lines = source.split('\n').map((line) => {
      const node = el('div', { class: 'fs-code-line' });
      node.innerHTML = highlightDart(line) || ' ';
      body.appendChild(node);
      return node;
    });
  };
  const mark = (...marked) => {
    lines.forEach((node, index) => node.classList.toggle('fs-on', marked.includes(index)));
  };
  return { box, setCode, mark };
};

const consolePanel = (title = 'Consola de depuración') => {
  const log = el('div', { class: 'fs-log' });
  const box = el('div', { class: 'fs-dark' }, el('h4', { text: title }), log);
  const print = (text, kind) => {
    log.appendChild(el('div', { class: kind ? `fs-log-${kind}` : undefined, text }));
    while (log.childNodes.length > 40) log.removeChild(log.firstChild);
    log.scrollTop = log.scrollHeight;
  };
  const clear = () => log.replaceChildren();
  return { box, print, clear };
};

const statePanel = (title) => {
  const heading = el('h4', { text: title });
  const rows = el('div');
  const box = el('div', { class: 'fs-panel' }, heading, rows);
  const known = new Map();
  const set = (entries) => {
    rows.replaceChildren();
    entries.forEach(([name, value]) => {
      const row = el('div', { class: 'fs-row' }, el('span', { text: name }), el('span', { text: value }));
      rows.appendChild(row);
      if (known.has(name) && known.get(name) !== value) flash(row);
      known.set(name, value);
    });
  };
  const setTitle = (text) => {
    heading.textContent = text;
  };
  return { box, set, setTitle };
};

const phone = (title) => {
  const titleNode = el('span', { text: title });
  const extra = el('small');
  const appbar = el('div', { class: 'fs-appbar' }, titleNode, extra);
  const body = el('div', { class: 'fs-body' });
  const frame = el(
    'div',
    { class: 'fs-phone' },
    el('div', { class: 'fs-status' }, el('span', { text: '9:41' }), el('span', { text: '5G' })),
    appbar,
    body
  );
  return {
    frame,
    body,
    appbar,
    setTitle: (text) => {
      titleNode.textContent = text;
    },
    setExtra: (text) => {
      extra.textContent = text;
    },
  };
};

const switchControl = (label, onChange) => {
  const input = el('input', { type: 'checkbox', onchange: (e) => onChange(e.target.checked) });
  return { node: el('label', { class: 'fs-switch' }, input, label), input };
};

const card = (root) => {
  ensureStyle();
  const container = el('div', { class: 'fsim' });
  root.replaceChildren(container);
  return container;
};

// ───────────────────────── state-counter / hot-reload ─────────────────────────

const COUNTER_CODE = `class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    print('build() con _counter = $_counter');
    return Scaffold(
      body: Text('$_counter'),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
      ),
    );
  }
}`;

const COUNTER_CODE_FORGOT = `class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    _counter++;
  }

  @override
  Widget build(BuildContext context) {
    print('build() con _counter = $_counter');
    return Scaffold(
      body: Text('$_counter'),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
      ),
    );
  }
}`;

const mountCounter = (root, args = []) => {
  const withReload = args.includes('reload');
  const withForget = !withReload || args.includes('forget');
  const container = card(root);
  const timers = [];

  let counter = 0;
  let shown = 0;
  let builds = 0;
  let forgot = false;
  let stateId = 1;

  const screen = phone('Flutter Demo Home Page');
  const big = el('div', { class: 'fs-big', 'data-testid': 'counter-text', text: '0' });
  screen.body.appendChild(
    el('div', { class: 'fs-center' }, el('div', { text: 'You have pushed the button this many times:' }), big)
  );
  const fab = el('button', { class: 'fs-fab', 'aria-label': 'Incrementar', text: '+' });
  screen.body.appendChild(fab);

  const note = el('div', { class: 'fs-note' });
  const code = codePanel('lib/main.dart');
  const state = statePanel('Objeto State');
  const logs = consolePanel();

  const renderState = () => {
    state.setTitle(`Objeto State · _MyHomePageState #${stateId}`);
    state.set([
      ['_counter', String(counter)],
      ['en pantalla', String(shown)],
      ['veces que corrió build()', String(builds)],
    ]);
  };

  const build = (reason) => {
    builds += 1;
    shown = counter;
    big.textContent = String(shown);
    flash(big);
    logs.print(`[${reason}] build() con _counter = ${counter}`);
    renderState();
  };

  const later = (fn, ms) => timers.push(setTimeout(fn, ms));

  fab.addEventListener('click', () => {
    if (forgot) {
      counter += 1;
      code.mark(3, 4);
      note.textContent = 'El valor cambió en el objeto State, pero nadie pidió reconstruir: la pantalla sigue igual.';
      note.className = 'fs-note fs-warn';
      renderState();
      return;
    }
    code.mark(4, 5);
    counter += 1;
    note.textContent = 'setState marca el State como sucio y Flutter vuelve a llamar a build().';
    note.className = 'fs-note';
    renderState();
    later(() => {
      code.mark(10, 11, 13);
      build('setState');
    }, 350);
  });

  const controls = el('div', { class: 'fs-controls' });
  if (withForget) {
    const toggle = switchControl('Olvidar setState', (checked) => {
      forgot = checked;
      code.setCode(checked ? COUNTER_CODE_FORGOT : COUNTER_CODE);
      note.textContent = checked
        ? 'Ahora _incrementCounter solo suma. Pulsa + y mira el panel y la pantalla.'
        : '';
      note.className = 'fs-note';
    });
    controls.appendChild(toggle.node);
  }
  if (withReload) {
    controls.appendChild(
      el('button', {
        class: 'fs-btn',
        text: 'Hot reload',
        onclick: () => {
          logs.print('Reloaded 1 of 612 libraries in 210ms.', 'ok');
          code.mark(10, 11);
          note.textContent = 'Hot reload vuelve a correr build() con el mismo objeto State: el contador se conserva.';
          note.className = 'fs-note';
          build('hot reload');
        },
      })
    );
    controls.appendChild(
      el('button', {
        class: 'fs-btn',
        text: 'Hot restart',
        onclick: () => {
          logs.print('Restarted application in 900ms.', 'ok');
          stateId += 1;
          counter = 0;
          code.mark(1);
          note.textContent = 'Hot restart crea la app desde cero: un State nuevo, y _counter vuelve a 0.';
          note.className = 'fs-note';
          build('hot restart');
        },
      })
    );
  }

  code.setCode(COUNTER_CODE);
  container.append(
    el('div', { class: 'fs-col' }, screen.frame, controls, note),
    el('div', { class: 'fs-side' }, state.box, code.box, logs.box)
  );
  build('primer build');

  return () => {
    timers.forEach(clearTimeout);
    root.replaceChildren();
  };
};

// ───────────────────────────────── state-tree ─────────────────────────────────

const mountTree = (root) => {
  const container = card(root);
  const timers = [];
  let nextId = 1;
  const newId = () => nextId++;

  let stateless = false;
  let counter = 0;
  let shown = 0;
  let widgetId = newId();
  const stateId = newId();
  const appId = newId();
  const ids = { scaffold: 0, appbar: 0, text: 0, fab: 0 };

  const screen = phone('MyHomePage');
  const big = el('div', { class: 'fs-big', 'data-testid': 'tree-counter', text: '0' });
  screen.body.appendChild(el('div', { class: 'fs-center' }, el('div', { text: 'Contador' }), big));
  const fab = el('button', { class: 'fs-fab', 'aria-label': 'Incrementar', text: '+' });
  screen.body.appendChild(fab);

  const note = el('div', { class: 'fs-note' });
  const tree = el('div', { class: 'fs-panel' });
  const logs = consolePanel('Qué pasó');

  const node = (label, id, kind) =>
    el('span', { class: `fs-node ${kind || ''}` }, el('b', { text: label }), el('span', { class: 'fs-id', text: `#${id}` }));

  const drawTree = (rebuilt) => {
    const app = node('MyApp', appId);
    const page = node(stateless ? 'MyHomePage · Stateless' : 'MyHomePage', widgetId, 'fs-stateful');
    const stateNode = stateless ? null : node('_MyHomePageState', stateId, 'fs-state');
    const children = [
      ['Scaffold', ids.scaffold],
      ['AppBar', ids.appbar],
      [`Text('${shown}')`, ids.text],
      ['FloatingActionButton', ids.fab],
    ];
    const nested = el(
      'ul',
      { class: 'fs-tree' },
      el(
        'li',
        {},
        node(children[0][0], children[0][1]),
        el(
          'ul',
          { class: 'fs-tree' },
          children.slice(1).map(([label, id]) => el('li', {}, node(label, id)))
        )
      )
    );
    const pageRow = el(
      'div',
      { class: 'fs-pair' },
      page,
      stateNode ? el('span', { class: 'fs-link', text: 'createState() →' }) : null,
      stateNode,
      stateless ? el('span', { class: 'fs-link', text: `contador = ${counter}` }) : null
    );
    tree.replaceChildren(
      el('h4', { text: 'Árbol de widgets · #n = número de objeto' }),
      el('ul', { class: 'fs-tree fs-tree-root' }, el('li', {}, app, el('ul', { class: 'fs-tree' }, el('li', {}, pageRow, nested))))
    );
    if (rebuilt.includes('page')) flash(page);
    if (rebuilt.includes('children')) nested.querySelectorAll('.fs-node').forEach(flash);
  };

  const rebuildChildren = () => {
    ids.scaffold = newId();
    ids.appbar = newId();
    ids.text = newId();
    ids.fab = newId();
  };

  const render = (rebuilt) => {
    big.textContent = String(shown);
    flash(big);
    drawTree(rebuilt);
  };

  fab.addEventListener('click', () => {
    counter += 1;
    if (stateless) {
      logs.print(`contador = ${counter} dentro del widget, pero un StatelessWidget no puede pedir build().`);
      note.textContent = 'El número cambió en el objeto widget y la pantalla no se enteró.';
      note.className = 'fs-note fs-warn';
      drawTree([]);
      return;
    }
    shown = counter;
    rebuildChildren();
    logs.print(`setState → _MyHomePageState #${stateId}.build(): widgets hijos nuevos, el State es el mismo.`);
    note.textContent = 'Los widgets hijos son objetos nuevos; el State #' + stateId + ' sigue siendo el mismo.';
    note.className = 'fs-note';
    render(['children']);
  });

  const parentButton = el('button', {
    class: 'fs-btn',
    text: 'Reconstruir MyApp',
    onclick: () => {
      widgetId = newId();
      rebuildChildren();
      if (stateless) {
        counter = 0;
        shown = 0;
        logs.print(`MyApp.build() crea MyHomePage #${widgetId} nuevo: contador vuelve a 0.`, 'err');
        note.textContent = 'El widget se descarta y se crea otro: lo que guardaba se perdió.';
        note.className = 'fs-note fs-warn';
      } else {
        logs.print(`MyApp.build() crea MyHomePage #${widgetId} nuevo; Flutter le conecta el mismo State #${stateId}.`, 'ok');
        note.textContent = `Widget nuevo (#${widgetId}), State de siempre (#${stateId}): el contador sobrevive.`;
        note.className = 'fs-note';
      }
      render(['page', 'children']);
    },
  });

  const toggle = switchControl('Guardar el contador en un StatelessWidget', (checked) => {
    stateless = checked;
    counter = 0;
    shown = 0;
    widgetId = newId();
    rebuildChildren();
    logs.clear();
    logs.print(checked ? 'Ahora el contador es un campo del widget, no del State.' : 'Ahora el contador vive en _MyHomePageState.');
    note.textContent = '';
    render(['page', 'children']);
  });

  rebuildChildren();
  container.append(
    el('div', { class: 'fs-col' }, screen.frame, el('div', { class: 'fs-controls' }, parentButton, toggle.node), note),
    el('div', { class: 'fs-side' }, tree, logs.box)
  );
  logs.print('Pulsa + varias veces y luego «Reconstruir MyApp».');
  render(['page', 'children']);

  return () => {
    timers.forEach(clearTimeout);
    root.replaceChildren();
  };
};

// ────────────────────────────── state-lifecycle ──────────────────────────────

const LIFECYCLE_CODE = `class _GreetingScreenState extends State<GreetingScreen> {
  late TextEditingController _nameController;

  @override
  void initState() {
    super.initState();
    _nameController = TextEditingController();
  }

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: _nameController,
      onChanged: (value) => setState(() {}),
    );
  }

  @override
  void dispose() {
    _nameController.dispose();
    super.dispose();
  }
}`;

const LIFECYCLE_STEPS = ['createState', 'initState', 'build', 'setState', 'dispose'];

const mountLifecycle = (root) => {
  const container = card(root);
  const timers = [];
  let open = false;
  let stateId = 0;
  let controllerId = 0;
  let controllerAlive = false;
  let builds = 0;
  let text = '';
  const done = new Set();

  const screen = phone('Inicio');
  const note = el('div', { class: 'fs-note' });
  const code = codePanel('lib/screens/greeting_screen.dart');
  const state = statePanel('Objeto State');
  const logs = consolePanel();
  const steps = el('div', { class: 'fs-steps' });
  const stepsPanel = el('div', { class: 'fs-panel' }, el('h4', { text: 'Ciclo de vida' }), steps);

  const drawSteps = () => {
    steps.replaceChildren(
      ...LIFECYCLE_STEPS.map((name) => {
        const kind = name === 'dispose' && done.has(name) ? 'fs-dead' : done.has(name) ? 'fs-done' : '';
        return el('span', { class: `fs-step ${kind}`, text: name });
      })
    );
  };

  const renderState = () => {
    if (!stateId) {
      state.setTitle('Objeto State · todavía no existe');
      state.set([['_nameController', '—']]);
      return;
    }
    state.setTitle(`Objeto State · _GreetingScreenState #${stateId}${open ? '' : ' (desmontado)'}`);
    state.set([
      ['_nameController', controllerAlive ? `#${controllerId} activo` : `#${controllerId} liberado`],
      ['_nameController.text', `'${text}'`],
      ['mounted', String(open)],
      ['veces que corrió build()', String(builds)],
    ]);
  };

  const later = (fn, ms) => timers.push(setTimeout(fn, ms));

  const drawHome = () => {
    screen.setTitle('Inicio');
    screen.body.replaceChildren(
      el(
        'div',
        { class: 'fs-center' },
        el('div', { text: 'Pantalla de inicio' }),
        el('button', { class: 'fs-btn fs-solid', text: 'Abrir saludo', onclick: openScreen })
      )
    );
  };

  const greeting = el('div', { class: 'fs-big', style: 'font-size:22px' });
  const field = el('input', { class: 'fs-field', placeholder: 'Escribe tu nombre', 'aria-label': 'Nombre' });

  const build = () => {
    builds += 1;
    greeting.textContent = text ? `Hola, ${text}` : 'Hola';
    done.add('build');
    drawSteps();
    renderState();
  };

  const drawGreeting = () => {
    screen.setTitle('Saludo');
    field.value = '';
    screen.body.replaceChildren(
      el('div', { class: 'fs-label', text: 'Nombre' }),
      field,
      greeting,
      el('div', { style: 'height:16px' }),
      el('button', { class: 'fs-btn', text: 'Guardar (tarda 2 s)', onclick: saveLater }),
      el('div', { style: 'height:8px' }),
      el('button', { class: 'fs-btn fs-solid', text: 'Volver', onclick: closeScreen })
    );
  };

  function openScreen() {
    open = true;
    stateId += 1;
    text = '';
    done.clear();
    done.add('createState');
    logs.print(`createState() → _GreetingScreenState #${stateId}`);
    code.mark(0);
    drawGreeting();
    later(() => {
      controllerId += 1;
      controllerAlive = true;
      done.add('initState');
      code.mark(4, 6);
      logs.print(`initState(): se crea TextEditingController #${controllerId}`);
      renderState();
      drawSteps();
    }, 300);
    later(() => {
      code.mark(10, 11);
      logs.print('build()');
      build();
      note.textContent = 'Escribe en el campo: cada letra llama a setState y vuelve a correr build().';
    }, 700);
    renderState();
    drawSteps();
  }

  function closeScreen() {
    if (!open) return;
    open = false;
    controllerAlive = false;
    done.add('dispose');
    code.mark(18, 19);
    logs.print(`dispose(): se libera TextEditingController #${controllerId}`, 'ok');
    note.textContent = 'La pantalla se cerró: el State se descarta y el controller se libera en dispose().';
    drawHome();
    renderState();
    drawSteps();
  }

  function saveLater() {
    const savedFrom = stateId;
    logs.print('Guardando… en 2 s se llama setState para mostrar «Guardado».');
    later(() => {
      if (open && stateId === savedFrom) {
        code.mark(13);
        logs.print('setState(): Guardado', 'ok');
        build();
        greeting.textContent = `${greeting.textContent} · Guardado`;
        return;
      }
      logs.print(`setState() called after dispose(): _GreetingScreenState#${savedFrom}`, 'err');
      note.textContent = 'El State ya no existe. Antes de llamar a setState tras una espera: if (!mounted) return;';
      note.className = 'fs-note fs-warn';
    }, 2000);
  }

  field.addEventListener('input', () => {
    text = field.value;
    done.add('setState');
    code.mark(13);
    logs.print(`setState() → build() con text = '${text}'`);
    build();
  });

  code.setCode(LIFECYCLE_CODE);
  drawHome();
  drawSteps();
  renderState();
  container.append(
    el('div', { class: 'fs-col' }, screen.frame, note),
    el('div', { class: 'fs-side' }, stepsPanel, state.box, code.box, logs.box)
  );
  note.textContent = 'Abre la pantalla de saludo, escribe y vuelve.';

  return () => {
    timers.forEach(clearTimeout);
    root.replaceChildren();
  };
};

// ───────────────────────────────── playlist ─────────────────────────────────

const DEFAULT_IMAGE = 'https://picsum.photos/400';

const PLAYLIST_ADD = `void _addSong() {
  final title = _titleController.text;
  final artist = _artistController.text;
  if (title.isEmpty || artist.isEmpty) return;
  setState(() {
    _songs.add(Song(
      title: title,
      artist: artist,
      imageUrl: _imageUrlController.text,
    ));
  });
  _titleController.clear();
  _artistController.clear();
}`;

const PLAYLIST_TEXT_VIEW = `

Column(
  children: [
    for (final song in _songs)
      Text('\${song.title} · \${song.artist}'),
  ],
)`;

const PLAYLIST_CARD_VIEW = `

Column(
  children: [
    for (final song in _songs)
      SongCard(song: song),
  ],
)`;

const mountPlaylist = (root, args = []) => {
  const withCards = args.includes('cards');
  let view = withCards ? 'cards' : 'text';
  const container = card(root);
  const songs = [];

  const screen = phone('Mi playlist');
  const note = el('div', { class: 'fs-note' });
  const code = codePanel('lib/screens/playlist_screen.dart');
  const state = statePanel('Objeto State · _PlaylistScreenState');
  const logs = consolePanel();

  const titleField = el('input', { class: 'fs-field', placeholder: 'Nombre de la canción', 'aria-label': 'Nombre de la canción' });
  const artistField = el('input', { class: 'fs-field', placeholder: 'Artista', 'aria-label': 'Artista' });
  const imageField = el('input', { class: 'fs-field', 'aria-label': 'URL de la imagen', value: DEFAULT_IMAGE });
  const addButton = el('button', { class: 'fs-filled', text: 'Agregar' });
  const list = el('div', { 'data-testid': 'playlist-list' });

  const songCard = (song) => {
    const cover = el('div', { class: 'fs-cover' });
    if (song.imageUrl) {
      const img = el('img', { src: song.imageUrl, alt: '' });
      img.addEventListener('error', () => img.remove());
      cover.appendChild(img);
    }
    return el(
      'div',
      { class: 'fs-card' },
      cover,
      el(
        'div',
        { class: 'fs-card-text' },
        el('div', { class: 'fs-card-title', text: song.title }),
        el('div', { class: 'fs-card-artist', text: song.artist })
      ),
      el('span', { class: 'fs-card-icon', text: '♪' })
    );
  };

  const renderState = () => {
    const entries = [
      ['_titleController.text', `'${titleField.value}'`],
      ['_artistController.text', `'${artistField.value}'`],
      ['_imageUrlController.text', `'${imageField.value}'`],
      ['_songs.length', String(songs.length)],
    ];
    songs.slice(-4).forEach((song, index) => {
      const position = songs.length - Math.min(4, songs.length) + index;
      entries.push([`_songs[${position}]`, `Song('${song.title}', '${song.artist}')`]);
    });
    state.set(entries);
  };

  const build = () => {
    screen.setExtra(songs.length ? `${songs.length}` : '');
    list.replaceChildren();
    if (songs.length === 0) {
      list.appendChild(el('div', { class: 'fs-empty', text: 'Todavía no hay canciones' }));
    } else {
      songs.forEach((song) => {
        list.appendChild(
          view === 'cards' ? songCard(song) : el('div', { class: 'fs-text-item', text: `${song.title} · ${song.artist}` })
        );
      });
    }
    renderState();
  };

  const setView = (next) => {
    view = next;
    code.setCode(PLAYLIST_ADD + (view === 'cards' ? PLAYLIST_CARD_VIEW : PLAYLIST_TEXT_VIEW));
    logs.print(`build() con la vista ${view === 'cards' ? 'SongCard' : 'Text'}: el estado (_songs) es el mismo.`);
    build();
  };

  const addSong = () => {
    const title = titleField.value.trim();
    const artist = artistField.value.trim();
    if (!title || !artist) {
      code.mark(3);
      logs.print('_addSong(): falta el nombre o el artista, no se agrega nada.', 'err');
      note.textContent = 'Escribe al menos el nombre de la canción y el artista.';
      note.className = 'fs-note fs-warn';
      return;
    }
    songs.push({ title, artist, imageUrl: imageField.value.trim() });
    code.mark(4, 5);
    logs.print(`setState(): _songs.add(Song('${title}', '${artist}')) → build() con ${songs.length} canciones`);
    titleField.value = '';
    artistField.value = '';
    note.textContent = 'La lista del estado creció y build() la volvió a pintar completa.';
    note.className = 'fs-note';
    build();
    const last = list.lastChild;
    flash(last);
    if (last && typeof last.scrollIntoView === 'function') last.scrollIntoView({ block: 'nearest' });
  };

  addButton.addEventListener('click', addSong);
  [titleField, artistField, imageField].forEach((field) => {
    field.addEventListener('input', renderState);
    field.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') addSong();
    });
  });

  screen.body.append(
    el('div', { class: 'fs-label', text: 'Nombre de la canción' }),
    titleField,
    el('div', { class: 'fs-label', text: 'Artista' }),
    artistField,
    el('div', { class: 'fs-label', text: 'URL de la imagen' }),
    imageField,
    addButton,
    el('div', { class: 'fs-list-title', text: 'Canciones' }),
    list
  );

  const controls = el('div', { class: 'fs-controls' });
  if (withCards) {
    const textButton = el('button', { text: 'Text' });
    const cardsButton = el('button', { text: 'SongCard', class: 'fs-sel' });
    const select = (next) => {
      textButton.className = next === 'text' ? 'fs-sel' : '';
      cardsButton.className = next === 'cards' ? 'fs-sel' : '';
      setView(next);
    };
    textButton.addEventListener('click', () => select('text'));
    cardsButton.addEventListener('click', () => select('cards'));
    controls.appendChild(el('div', { class: 'fs-seg', role: 'group', 'aria-label': 'Vista' }, textButton, cardsButton));
  }

  container.append(
    el('div', { class: 'fs-col' }, screen.frame, controls, note),
    el('div', { class: 'fs-side' }, state.box, code.box, logs.box)
  );
  code.setCode(PLAYLIST_ADD + (view === 'cards' ? PLAYLIST_CARD_VIEW : PLAYLIST_TEXT_VIEW));
  note.textContent = 'Escribe una canción y su artista, y pulsa Agregar.';
  build();

  return () => {
    root.replaceChildren();
  };
};

export const SIMS = Object.freeze({
  'state-counter': mountCounter,
  'hot-reload': (root, args = []) => mountCounter(root, ['reload', ...args]),
  'state-tree': mountTree,
  'state-lifecycle': mountLifecycle,
  playlist: mountPlaylist,
});

export const parseSpec = (spec) => {
  const [name = '', ...args] = String(spec || '').trim().split(/\s+/);
  return { name, args };
};
