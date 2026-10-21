// Interactive simulators for Flutter state (StatefulWidget, setState, lifecycle).
// Plain DOM, no React: the same file is copied into the session decks, so it must
// not import anything. Every simulator is `mount(element, args) => destroy`.

const STYLE_ID = 'fsim-style';

const CSS = `
.fsim{--fs-bg:#FBFBFD;--fs-ink:#1C1B1F;--fs-muted:#5F6368;--fs-line:#E3E3EA;--fs-accent:#6750A4;
  --fs-accent-soft:#EADDFF;--fs-appbar:#D0BCFF;--fs-flash:#FFE082;--fs-ok:#2E7D32;--fs-err:#C62828;
  background:var(--fs-bg);color:var(--fs-ink);border:1px solid var(--fs-line);border-radius:16px;
  padding:16px;font-family:Roboto,Arial,sans-serif;font-size:14px;line-height:1.4;
  display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start;box-sizing:border-box;max-width:960px;margin:0 auto;overflow:hidden;
  container-type:inline-size}
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
.fsim .fs-rel{position:relative}
.fsim .fs-lines{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;overflow:visible;z-index:2}
.fsim .fs-lines .fs-read{fill:none;stroke:#9061DB;stroke-width:2;stroke-dasharray:5 5;opacity:.5;transition:opacity .3s}
.fsim .fs-lines .fs-read.fs-active{stroke-dasharray:none;opacity:1;stroke-width:2.5}
.fsim .fs-lines .fs-write{fill:none;stroke:#D08A12;stroke-width:2.5;opacity:0;transition:opacity .3s}
.fsim .fs-lines .fs-write.fs-active{opacity:1}
.fsim .fs-node.fs-reads{border-color:#7439B8;border-style:dashed}
.fsim .fs-node.fs-hot{box-shadow:0 0 0 3px #F2C069;border-color:#A96C05}
.fsim .fs-state-box{background:#F4EBFF;border-color:#C9A6EE}
.fsim .fs-state-head{display:flex;align-items:center;gap:10px}
.fsim .fs-state-head h4{margin:0;color:#7439B8}
.fsim .fs-state-foot{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px;margin-top:8px}
.fsim .fs-state-of{font-size:12px;color:var(--fs-muted);margin:0;font-family:'JetBrains Mono',Menlo,Consolas,monospace}
.fsim .fs-var{display:flex;align-items:center;gap:8px;font-family:'JetBrains Mono',Menlo,Consolas,monospace;font-size:14px;margin:4px 0}
.fsim .fs-var-type{color:#7439B8}
.fsim .fs-var-name{font-weight:600}
.fsim .fs-var-val{min-width:64px;text-align:center;font-size:22px;font-weight:600;background:#fff;border:2px solid #7439B8;
  border-radius:10px;padding:2px 12px;display:inline-block}
.fsim .fs-var.fs-wrap{flex-wrap:wrap}
.fsim .fs-var-val.fs-small{font-size:13px;font-weight:500;padding:2px 8px;text-align:left;overflow-wrap:anywhere;max-width:100%}
.fsim .fs-var-val.fs-list{font-size:12.5px;font-weight:500;padding:4px 8px;text-align:left;min-width:120px;max-width:100%}
.fsim .fs-var-val.fs-list.fs-pop{animation:fsimFlash 1s ease-out}
.fsim .fs-var-val.fs-list div{overflow-wrap:anywhere}
.fsim .fs-var-val.fs-list .fs-more{color:var(--fs-muted)}
.fsim .fs-var-hint{font-size:11px;color:var(--fs-muted);font-family:Roboto,Arial,sans-serif}
.fsim .fs-pop{animation:fsimPop .7s ease-out}
@keyframes fsimPop{0%{transform:scale(1)}35%{transform:scale(1.25);background:#FFE082}100%{transform:scale(1)}}
.fsim .fs-press{animation:fsimPress .6s ease-out}
@keyframes fsimPress{0%{box-shadow:0 0 0 0 rgba(169,108,5,.7)}100%{box-shadow:0 0 0 18px rgba(169,108,5,0)}}
.fsim .fs-tag{font-size:12px;padding:2px 10px;border-radius:10px;background:#E8F6E3;color:#3A8235;font-weight:500}
.fsim .fs-tag.fs-dirty{background:#FFF3DC;color:#A96C05}
.fsim .fs-tag.fs-lost{background:#FFEBEF;color:#C2354F}
.fsim .fs-stepbar{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}
.fsim .fs-sp{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;padding:3px 10px 3px 4px;border-radius:14px;
  border:1px solid var(--fs-line);color:#79747E;background:#fff}
.fsim .fs-sp b{display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:9px;
  background:#E7E0EC;color:#49454F;font-size:11px}
.fsim .fs-sp.fs-past{color:var(--fs-ink);border-color:#C9A6EE}
.fsim .fs-sp.fs-past b{background:#C9A6EE;color:#fff}
.fsim .fs-sp.fs-cur{background:var(--fs-accent);border-color:var(--fs-accent);color:#fff}
.fsim .fs-sp.fs-cur b{background:#fff;color:var(--fs-accent)}
.fsim .fs-view{align-self:flex-start}
.fsim .fs-trig{background:rgba(242,192,105,.22);border-radius:3px;padding:0 2px}
.fsim .fs-row2{flex:1 1 100%;display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start;min-width:0}
.fsim .fs-row2 > .fs-dark{flex:1 1 420px;min-width:0}
.fsim .fs-row2 > .fs-panel{flex:1 1 240px;min-width:0}
.fsim .fs-sv{color:#E9D5FF;font-weight:700;background:rgba(201,166,238,.22);border-radius:3px;padding:0 2px}
.fsim .fs-code-line.fs-bind{border-left-color:rgba(201,166,238,.7)}
.fsim .fs-code-line.fs-bind.fs-on{border-left-color:#F9E2AF}
.fsim .fs-caption{font-size:14px;min-height:42px;color:var(--fs-ink)}
.fsim .fs-steps{display:flex;flex-wrap:wrap;gap:6px}
.fsim .fs-step{font-family:'JetBrains Mono',Menlo,Consolas,monospace;font-size:12px;padding:3px 9px;border-radius:12px;
  border:1px solid var(--fs-line);color:#9E9AA7;background:#fff}
.fsim .fs-step.fs-done{color:var(--fs-ink);border-color:var(--fs-accent);background:var(--fs-accent-soft)}
.fsim .fs-step.fs-dead{color:#fff;border-color:#625B71;background:#625B71}
.fsim .fs-list-title{font-size:13px;font-weight:600;color:#49454F;margin:2px 0 6px}
.fsim .fs-seg{display:inline-flex;border:1px solid var(--fs-accent);border-radius:20px;overflow:hidden}
.fsim .fs-seg button{border:0;background:#fff;color:var(--fs-accent);padding:6px 14px;font:500 13px Roboto,Arial,sans-serif;cursor:pointer}
.fsim .fs-seg button.fs-sel{background:var(--fs-accent);color:#fff}
@container (max-width:780px){.fsim .fs-code-line{font-size:11px}}
@media (max-width:480px){.fsim{padding:12px;gap:12px}.fsim .fs-tree{padding-left:7px}.fsim .fs-node{font-size:11px;padding:2px 6px;gap:5px}.fsim .fs-panel{padding:10px 8px}.fsim .fs-code-line{font-size:9.5px;padding:0 6px}}
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
const DART_TYPES = new Set(['int', 'String', 'List', 'Widget', 'State', 'StatefulWidget', 'StatelessWidget', 'BuildContext', 'Scaffold', 'Text', 'TextEditingController', 'Column', 'Song', 'SongCard', 'FloatingActionButton', 'TextField', 'MyHomePage', 'GreetingScreen', 'PlaylistScreen', 'SingleChildScrollView', 'FilledButton', 'AppBar']);
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
  return { box, setCode, mark, lineNodes: () => lines };
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

// The widget tree next to the State's variables, joined by lines from each variable
// to the widgets that read it. A tap plays the steps of setState one by one.

const STEP_MS = 1100;
const DOT_MS = 700;
let treeUid = 0;

const raf = (fn) => (typeof requestAnimationFrame === 'function' ? requestAnimationFrame(fn) : setTimeout(fn, 16));
const cancelRaf = (id) => (typeof cancelAnimationFrame === 'function' ? cancelAnimationFrame(id) : clearTimeout(id));
const SVG_NS = 'http://www.w3.org/2000/svg';
const svgEl = (tag, attrs = {}) => {
  const node = document.createElementNS(SVG_NS, tag);
  Object.entries(attrs).forEach(([key, value]) => node.setAttribute(key, value));
  return node;
};
const showValue = (value) => (typeof value === 'string' ? `'${value}'` : String(value));
const shorten = (text, max) => (text.length > max ? `${text.slice(0, max - 1)}…` : text);

const DEFAULT_IMAGE = 'https://picsum.photos/400';

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

const songList = (songs) => {
  if (!songs.length) return ['[ ]'];
  const shown = songs.slice(-5);
  const rows = shown.map((s) => el('div', { text: `Song('${shorten(s.title, 14)}', '${shorten(s.artist, 12)}')` }));
  if (songs.length > shown.length) rows.unshift(el('div', { class: 'fs-more', text: `… ${songs.length - shown.length} más arriba` }));
  return rows;
};

const bulbIcon = (on) => {
  const icon = svgEl('svg', { viewBox: '0 0 24 24', width: '96', height: '96' });
  icon.appendChild(svgEl('path', {
    d: 'M9 21h6v-1H9v1zm3-19a7 7 0 0 0-4 12.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26A7 7 0 0 0 12 2z',
    fill: on ? '#F5B800' : 'none',
    stroke: on ? '#B78900' : '#9E9AA7',
    'stroke-width': '1.6',
  }));
  return icon;
};

const TREE_SCENARIOS = {
  counter: {
    app: 'MyApp',
    widget: 'MyHomePage',
    state: '_MyHomePageState',
    vars: [{ name: '_counter', type: 'int', initial: 0 }],
    fn: '_incrementCounter()',
    next: (v) => ({ _counter: v._counter + 1 }),
    nodes: [
      { key: 'scaffold', depth: 0, label: () => 'Scaffold' },
      { key: 'appbar', depth: 1, label: () => 'AppBar' },
      { key: 'text', depth: 1, label: (v) => `Text('${v._counter}')`, reads: '_counter' },
      { key: 'fab', depth: 1, label: () => 'FloatingActionButton', trigger: true },
    ],
    code: `class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Contador')),
      body: Text('$_counter'),
      floatingActionButton: FloatingActionButton(
        onPressed: () => _incrementCounter(),
        child: Icon(Icons.add),
      ),
    );
  }
}`,
    file: 'lib/main.dart',
    forgetCode: `class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    _counter++;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Contador')),
      body: Text('$_counter'),
      floatingActionButton: FloatingActionButton(
        onPressed: () => _incrementCounter(),
        child: Icon(Icons.add),
      ),
    );
  }
}`,
    triggerName: () => '+',
    idle: 'Pulsa + y sigue los pasos: primero cambia el estado y al final la pantalla.',
    read: (v) => `Mientras construye, build() lee _counter: el Text nuevo recibe '${v._counter}'.`,
    paint: (v) => `Flutter pinta los widgets nuevos: la pantalla por fin muestra ${v._counter}.`,
    phone: (screen, onTrigger) => {
      screen.setTitle('Contador');
      const big = el('div', { class: 'fs-big', 'data-testid': 'tree-counter' });
      const fab = el('button', { class: 'fs-fab', 'aria-label': 'Incrementar', text: '+', onclick: onTrigger });
      screen.body.append(el('div', { class: 'fs-center' }, big), fab);
      return {
        trigger: fab,
        paint: (v) => {
          big.textContent = String(v._counter);
          flash(big);
        },
      };
    },
  },
  bulb: {
    app: 'App',
    widget: 'HomeScreen',
    state: '_HomeScreenState',
    vars: [{ name: '_isOn', type: 'bool', initial: false }],
    fn: '_toggle()',
    next: (v) => ({ _isOn: !v._isOn }),
    rebuild: true,
    nodes: [
      { key: 'scaffold', depth: 0, label: () => 'Scaffold' },
      { key: 'appbar', depth: 1, label: () => 'AppBar' },
      { key: 'center', depth: 1, label: () => 'Center' },
      { key: 'column', depth: 2, label: () => 'Column' },
      { key: 'icon', depth: 3, label: (v) => (v._isOn ? 'Icon(lightbulb)' : 'Icon(lightbulb_outline)'), reads: '_isOn' },
      { key: 'text', depth: 3, label: (v) => `Text('${v._isOn ? 'Encendido' : 'Apagado'}')`, reads: '_isOn' },
      { key: 'button', depth: 3, label: (v) => `FilledButton('${v._isOn ? 'Apagar' : 'Encender'}')`, reads: '_isOn', trigger: true },
    ],
    code: `class _HomeScreenState extends State<HomeScreen> {
  bool _isOn = false;

  void _toggle() {
    setState(() {
      _isOn = !_isOn;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Bombillo')),
      body: Center(
        child: Column(
          children: [
            Icon(_isOn
                ? Icons.lightbulb
                : Icons.lightbulb_outline),
            Text(_isOn ? 'Encendido' : 'Apagado'),
            FilledButton(
              onPressed: () => _toggle(),
              child: Text(
                _isOn ? 'Apagar' : 'Encender',
              ),
            ),
          ],
        ),
      ),
    );
  }
}`,
    file: 'lib/screens/home_screen.dart',
    triggerName: (v) => (v._isOn ? 'Apagar' : 'Encender'),
    idle: 'Pulsa Encender y sigue los pasos. Después prueba Reconstruir App.',
    read: () => 'Mientras construye, build() lee _isOn: el Icon, el Text y el FilledButton nuevos lo usan.',
    paint: (v) => `Flutter pinta los widgets nuevos: el bombillo queda ${v._isOn ? 'encendido' : 'apagado'}.`,
    phone: (screen, onTrigger) => {
      screen.setTitle('Bombillo');
      const iconBox = el('div');
      const label = el('div', { 'data-testid': 'bulb-text' });
      const button = el('button', { class: 'fs-btn fs-solid', onclick: onTrigger });
      screen.body.append(el('div', { class: 'fs-center' }, iconBox, label, button));
      return {
        trigger: button,
        paint: (v) => {
          iconBox.replaceChildren(bulbIcon(v._isOn));
          label.textContent = v._isOn ? 'Encendido' : 'Apagado';
          button.textContent = v._isOn ? 'Apagar' : 'Encender';
          flash(iconBox);
        },
      };
    },
  },
  playlist: {
    app: 'App',
    widget: 'PlaylistScreen',
    state: '_PlaylistScreenState',
    main: '_songs',
    vars: [
      { name: '_songs', type: 'List<Song>', initial: [], show: (songs) => songList(songs) },
      { name: '_titleController', label: '_titleController.text', type: 'String', initial: '', input: 'title' },
      { name: '_artistController', label: '_artistController.text', type: 'String', initial: '', input: 'artist' },
      { name: '_imageUrlController', label: '_imageUrlController.text', type: 'String', initial: '', input: 'imageUrl' },
    ],
    fn: '_addSong()',
    next: (v) => ({
      _songs: [...v._songs, { title: v._titleController, artist: v._artistController, imageUrl: v._imageUrlController }],
    }),
    nodes: (v, layout) => [
      { key: 'scaffold', depth: 0, label: () => 'Scaffold' },
      { key: 'appbar', depth: 1, label: () => 'AppBar' },
      { key: 'scroll', depth: 1, label: () => 'SingleChildScrollView' },
      { key: 'column', depth: 2, label: () => 'Column' },
      { key: 'title', depth: 3, label: () => "TextField('Canción')" },
      { key: 'artist', depth: 3, label: () => "TextField('Artista')" },
      { key: 'imageUrl', depth: 3, label: () => "TextField('URL')" },
      { key: 'button', depth: 3, label: () => 'FilledButton', trigger: true },
      ...v._songs.map((song, i) => (layout === 'cards'
        ? { key: `card-${i}`, depth: 3, label: () => `SongCard('${shorten(song.title, 16)}')`, reads: '_songs' }
        : { key: `text-${i}`, depth: 3, label: () => `Text('${shorten(`${song.title} · ${song.artist}`, 20)}')`, reads: '_songs' })),
    ],
    source: (forgot, layout) => `class _PlaylistScreenState extends State<PlaylistScreen> {
  final List<Song> _songs = [];
  final _titleController = TextEditingController();
  final _artistController = TextEditingController();
  final _imageUrlController = TextEditingController();

  void _addSong() {
${forgot ? `    _songs.add(Song(
      title: _titleController.text,
      artist: _artistController.text,
      imageUrl: _imageUrlController.text,
    ));` : `    setState(() {
      _songs.add(Song(
        title: _titleController.text,
        artist: _artistController.text,
        imageUrl: _imageUrlController.text,
      ));
    });`}
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Mi playlist')),
      body: SingleChildScrollView(
        child: Column(
          children: [
            TextField(controller: _titleController),
            TextField(controller: _artistController),
            TextField(controller: _imageUrlController),
            FilledButton(
              onPressed: () => _addSong(),
              child: Text('Agregar'),
            ),
            for (final song in _songs)
              ${layout === 'cards' ? 'SongCard(song: song),' : "Text('${song.title} · ${song.artist}'),"}
          ],
        ),
      ),
    );
  }
}`,
    file: 'lib/screens/playlist_screen.dart',
    triggerName: () => 'Agregar',
    idle: 'Escribe una canción y su artista, pulsa Agregar y sigue los pasos: primero crece _songs y al final la pantalla.',
    setCaption: (before, after) => {
      const song = after._songs[after._songs.length - 1];
      const empty = !song.title && !song.artist ? ' Con los campos vacíos entra una canción vacía: se arregla en el taller.' : '';
      return `Dentro de setState, _songs.add(Song('${song.title}', '${song.artist}')) agrega una canción: _songs pasa de ${before._songs.length} a ${after._songs.length} y el State queda sucio. La pantalla todavía no cambia.${empty}`;
    },
    forgetCaption: (before, after) => `_addSong() agrega la canción a _songs (pasa de ${before._songs.length} a ${after._songs.length}), pero no llama a setState.`,
    staleCaption: (painted) => `Flutter no se enteró: build() no corre y la lista sigue con ${painted._songs.length}. La canción aparecerá con el próximo setState.`,
    read: (v, layout) => (v._songs.length
      ? `Mientras construye, el for recorre _songs: un ${layout === 'cards' ? 'SongCard' : 'Text'} por cada canción, ${v._songs.length} en total.`
      : 'Mientras construye, el for recorre _songs: está vacía, así que no crea ningún widget.'),
    paint: (v) => `Flutter pinta los widgets nuevos: la pantalla muestra ${v._songs.length === 1 ? '1 canción' : `${v._songs.length} canciones`}.`,
    typing: (name) => `Escribir cambia ${name}.text sin setState: el TextField se repinta solo y build() no corre.`,
    phone: (screen, onTrigger, onInput) => {
      screen.setTitle('Mi playlist');
      const field = (label, input, placeholder) => {
        const node = el('input', { class: 'fs-field', placeholder, 'aria-label': label });
        node.addEventListener('input', () => onInput(input, node.value));
        node.addEventListener('focus', () => onInput(input, node.value, true));
        node.addEventListener('keydown', (e) => {
          if (e.key === 'Enter') onTrigger();
        });
        return [el('div', { class: 'fs-label', text: label }), node];
      };
      const button = el('button', { class: 'fs-filled', text: 'Agregar', onclick: onTrigger });
      const list = el('div', { 'data-testid': 'playlist-list' });
      screen.body.append(
        ...field('Nombre de la canción', 'title', 'Yellow'),
        ...field('Artista', 'artist', 'Coldplay'),
        ...field('URL de la imagen', 'imageUrl', DEFAULT_IMAGE),
        button,
        list
      );
      return {
        trigger: button,
        paint: (v, layout) => {
          const before = list.childNodes.length;
          list.replaceChildren(...v._songs.map((song) => (layout === 'cards'
            ? songCard(song)
            : el('div', { class: 'fs-text-item', text: `${song.title} · ${song.artist}` }))));
          if (v._songs.length > before) {
            flash(list.lastChild);
            screen.body.scrollTop = screen.body.scrollHeight;
          }
        },
      };
    },
  },
};

const mountTree = (root, args = []) => {
  const sc = TREE_SCENARIOS[['bulb', 'playlist'].find((name) => args.includes(name)) || 'counter'];
  const uid = ++treeUid;
  const container = card(root);
  const timers = [];
  const frames = new Set();
  let nextId = 1;
  const newId = () => nextId++;

  const main = sc.main || sc.vars[0].name;
  const bound = sc.vars.filter((v) => !v.input).map((v) => v.name);
  const withCards = args.includes('cards');
  const initial = Object.fromEntries(sc.vars.map((v) => [v.name, v.initial]));
  const startLayout = withCards ? 'cards' : 'text';
  const model = {
    vars: { ...initial }, built: { ...initial }, painted: { ...initial }, dirty: false,
    layout: startLayout, builtLayout: startLayout, paintedLayout: startLayout,
  };
  const appId = newId();
  let widgetId = newId();
  const stateId = newId();
  const ids = {};
  const nodesNow = () => (typeof sc.nodes === 'function' ? sc.nodes(model.built, model.builtLayout) : sc.nodes);
  const renewIds = () => nodesNow().forEach((n) => {
    ids[n.key] = newId();
  });
  renewIds();

  const screen = phone('');
  const phoneView = sc.phone(screen, () => start(toggleSteps), (input, value, focusOnly) => onInput(input, value, focusOnly));

  const treePanel = el('div', { class: 'fs-panel' });
  const varBoxes = {};
  const dirtyTag = el('span', { class: 'fs-tag' });
  const stateTitle = el('div', { class: 'fs-state-of' });
  const varRows = sc.vars.map((v) => {
    const size = v.show ? ' fs-list' : v.input ? ' fs-small' : '';
    varBoxes[v.name] = el('span', { class: `fs-var-val${size}`, 'data-testid': `var-${v.name}` });
    return el('div', { class: `fs-var${v.input || v.show ? ' fs-wrap' : ''}` },
      el('span', { class: 'fs-var-type', text: v.type }),
      el('span', { class: 'fs-var-name', text: v.label || v.name }),
      varBoxes[v.name]);
  });
  const statePanel = el('div', { class: 'fs-panel fs-state-box' },
    el('div', { class: 'fs-state-head' }, el('h4', { text: 'Estado' })),
    ...varRows,
    el('div', { class: 'fs-state-foot' }, stateTitle, dirtyTag));
  const stepBar = el('div', { class: 'fs-stepbar' });
  const caption = el('div', { class: 'fs-caption', 'data-testid': 'tree-caption' });
  const stepsPanel = el('div', { class: 'fs-panel' }, stepBar, caption);

  let forgot = false;
  const sourceOf = () => (sc.source ? sc.source(forgot, model.layout) : forgot ? sc.forgetCode : sc.code);
  const code = codePanel(sc.file);
  const varNames = sc.vars.map((v) => v.name);
  const codeLines = {};
  const applyCode = (text) => {
    code.setCode(text);
    const source = text.split('\n');
    const buildAt = source.findIndex((l) => l.includes('Widget build('));
    const findLines = (test) => source.map((l, i) => (test(l, i) ? i : -1)).filter((i) => i >= 0);
    Object.assign(codeLines, {
      trigger: findLines((l) => l.includes('onPressed')),
      set: findLines((l, i) => i < buildAt && (l.includes('setState(') || bound.some((n) => l.trim().startsWith(n)))),
      build: [buildAt],
      reads: findLines((l, i) => i > buildAt && bound.some((n) => new RegExp(`\\b${n}\\b`).test(l))),
    });
    decorateCode();
  };
  const decorateCode = () => code.lineNodes().forEach((line, i) => {
    varNames.forEach((n) => {
      line.innerHTML = line.innerHTML.replace(new RegExp(`\\b${n}\\b`, 'g'), `<span class="fs-sv">${n}</span>`);
    });
    if (codeLines.reads.includes(i)) line.classList.add('fs-bind');
    if (codeLines.trigger.includes(i)) {
      line.innerHTML = line.innerHTML.replace('onPressed', '<span class="fs-trig">onPressed</span>');
    }
  });
  applyCode(sourceOf());

  const codeAt = (key) => code.mark(...(codeLines[key] || []));

  const lines = svgEl('svg', { class: 'fs-lines', 'aria-hidden': 'true' });
  let view = 'tree';
  const treeTab = el('button', { text: 'Árbol de widgets', class: 'fs-sel' });
  const codeTab = el('button', { text: 'Código' });
  const showView = (next) => {
    view = next;
    treeTab.className = next === 'tree' ? 'fs-sel' : '';
    codeTab.className = next === 'code' ? 'fs-sel' : '';
    treePanel.hidden = next !== 'tree';
    code.box.hidden = next !== 'code';
    scheduleLines();
  };
  treeTab.addEventListener('click', () => showView('tree'));
  codeTab.addEventListener('click', () => showView('code'));
  const viewSwitch = el('div', { class: 'fs-seg fs-view', role: 'group', 'aria-label': 'Vista' }, treeTab, codeTab);
  code.box.hidden = true;
  const side = el('div', { class: 'fs-side fs-rel' }, viewSwitch, treePanel, code.box, statePanel, stepsPanel);
  side.appendChild(lines);

  let nodeEls = {};
  const node = (key, label, id, kind) => {
    const n = el('span', { class: `fs-node ${kind || ''}`, 'data-node': key },
      el('b', { text: label }), el('span', { class: 'fs-id', text: `#${id}` }));
    nodeEls[key] = n;
    return n;
  };

  const nest = (items) => {
    const rootList = el('ul', { class: 'fs-tree' });
    const stack = [{ depth: -1, list: rootList }];
    items.forEach(({ depth, content }) => {
      while (stack[stack.length - 1].depth >= depth) stack.pop();
      const item = el('li', {}, content);
      stack[stack.length - 1].list.appendChild(item);
      const sub = el('ul', { class: 'fs-tree' });
      item.appendChild(sub);
      stack.push({ depth, list: sub });
    });
    rootList.querySelectorAll('ul').forEach((u) => {
      if (!u.childNodes.length) u.remove();
    });
    return rootList;
  };

  // Lines: each variable to every widget that reads it, plus the transient write path.
  let paths = {};
  let readers = [];
  const markerId = (name) => `fsim-tree${uid}-${name}`;
  const defs = svgEl('defs');
  [['read', '#9061DB'], ['write', '#D08A12']].forEach(([name, color]) => {
    const marker = svgEl('marker', {
      id: markerId(name), viewBox: '0 0 10 10', refX: '9', refY: '5',
      markerWidth: '7', markerHeight: '7', orient: 'auto-start-reverse',
    });
    marker.appendChild(svgEl('path', { d: 'M0,0 L10,5 L0,10 L2.4,5 Z', fill: color }));
    defs.appendChild(marker);
  });
  lines.appendChild(defs);
  const writePath = svgEl('path', { class: 'fs-write', 'marker-end': `url(#${markerId('write')})` });
  lines.appendChild(writePath);
  const triggerKey = () => nodesNow().find((n) => n.trigger).key;

  const syncPaths = (nodes) => {
    readers = nodes.filter((n) => n.reads);
    const next = { write: writePath };
    readers.forEach((n) => {
      next[n.key] = paths[n.key] || svgEl('path', { class: 'fs-read', 'marker-end': `url(#${markerId('read')})` });
      if (!next[n.key].parentNode) lines.appendChild(next[n.key]);
    });
    Object.entries(paths).forEach(([k, p]) => {
      if (!next[k]) p.remove();
    });
    paths = next;
  };

  const renderTree = () => {
    nodeEls = {};
    const nodes = nodesNow();
    nodes.forEach((n) => {
      if (!ids[n.key]) ids[n.key] = newId();
    });
    syncPaths(nodes);
    const pageRow = el('div', { class: 'fs-pair' },
      node('widget', sc.widget, widgetId, 'fs-stateful'),
      el('span', { class: 'fs-link', text: 'createState() →' }),
      node('state', sc.state, stateId, 'fs-state'));
    const children = nest(nodes.map((n) => ({
      depth: n.depth,
      content: node(n.key, n.label(model.built), ids[n.key], n.reads ? 'fs-reads' : ''),
    })));
    treePanel.replaceChildren(
      el('h4', { text: 'Árbol de widgets · #n = número de objeto' }),
      el('ul', { class: 'fs-tree fs-tree-root' },
        el('li', {}, node('app', sc.app, appId), el('ul', { class: 'fs-tree' }, el('li', {}, pageRow, children)))));
    scheduleLines();
  };

  const renderState = () => {
    stateTitle.textContent = `vive en ${sc.state} #${stateId}`;
    sc.vars.forEach((v) => {
      const value = model.vars[v.name];
      varBoxes[v.name].replaceChildren(...(v.show ? v.show(value) : [showValue(value)]));
    });
    const stale = bound.some((n) => model.vars[n] !== model.painted[n]);
    dirtyTag.textContent = model.dirty ? 'sucio: pide build()' : stale ? 'Flutter no se enteró' : 'al día';
    dirtyTag.className = model.dirty ? 'fs-tag fs-dirty' : stale ? 'fs-tag fs-lost' : 'fs-tag';
    scheduleLines();
  };

  const box = (target, base) => {
    const r = target.getBoundingClientRect();
    return { l: r.left - base.left, r: r.right - base.left, t: r.top - base.top, b: r.bottom - base.top,
      cx: (r.left + r.right) / 2 - base.left, cy: (r.top + r.bottom) / 2 - base.top };
  };

  // Every reader of a variable hangs from one vertical trunk placed right of the widest
  // node it passes by, so the branches never cross each other or a node.
  const drawLines = () => {
    const base = side.getBoundingClientRect();
    const inCode = view === 'code';
    const textBox = (line) => {
      const range = typeof document.createRange === 'function' ? document.createRange() : null;
      if (!range || typeof range.getBoundingClientRect !== 'function') return box(line, base);
      range.selectNodeContents(line);
      const r = range.getBoundingClientRect();
      const lineBox = box(line, base);
      return { ...lineBox, l: r.left - base.left, r: r.right - base.left + 6 };
    };
    const all = inCode
      ? code.lineNodes().map(textBox)
      : Object.values(nodeEls).map((n) => box(n, base));
    const source = sourceOf().split('\n');
    const bindLine = (n) => {
      const mine = codeLines.reads.filter((i) => new RegExp(`\\b${n.reads}\\b`).test(source[i]));
      const index = readers.filter((r) => r.reads === n.reads).indexOf(n);
      return code.lineNodes()[mine[Math.min(index, mine.length - 1)] ?? codeLines.reads[0]];
    };
    sc.vars.forEach((v) => {
      const from = box(varBoxes[v.name], base);
      const mine = readers.filter((n) => n.reads === v.name);
      if (!mine.length) return;
      const targets = mine.map((n) => (inCode ? textBox(bindLine(n)) : box(nodeEls[n.key], base)));
      const top = Math.min(...targets.map((t) => t.cy));
      const passed = all.filter((b) => b.b >= top - 2 && b.t <= from.cy);
      const room = base.width - 6;
      const trunk = Math.min(room, Math.max(from.r, ...passed.map((b) => b.r)) + (room > 520 ? 36 : 14));
      mine.forEach((n, i) => {
        const to = targets[i];
        const r = Math.min(10, Math.abs(from.cy - to.cy) / 2);
        paths[n.key].setAttribute('d',
          `M${from.r},${from.cy} H${trunk - r} Q${trunk},${from.cy} ${trunk},${from.cy - r} `
          + `V${to.cy + r} Q${trunk},${to.cy} ${trunk - r},${to.cy} H${to.r + 4}`);
      });
    });
    const to = box(varBoxes[main], base);
    if (inCode) {
      const from = textBox(code.lineNodes()[codeLines.trigger[0]]);
      const out = Math.min(base.width - 4, Math.max(...all.map((b) => b.r)) + 24);
      writePath.setAttribute('d',
        `M${from.r},${from.cy} H${out} V${to.t - 22} H${to.cx} V${to.t - 4}`);
      return;
    }
    const from = box(nodeEls[triggerKey()], base);
    writePath.setAttribute('d',
      `M${from.cx},${from.b} C${from.cx},${from.b + 40} ${to.cx},${to.t - 40} ${to.cx},${to.t - 4}`);
  };

  let linesQueued = false;
  const scheduleLines = () => {
    if (linesQueued) return;
    linesQueued = true;
    const id = raf(() => {
      frames.delete(id);
      linesQueued = false;
      drawLines();
    });
    frames.add(id);
  };

  const travel = (path, color) => {
    if (typeof path.getTotalLength !== 'function') return;
    const dot = svgEl('circle', { r: '6', fill: color, class: 'fs-dot' });
    lines.appendChild(dot);
    const total = path.getTotalLength();
    const begin = performance.now();
    const tick = (now) => {
      const k = Math.min(1, (now - begin) / DOT_MS);
      const p = path.getPointAtLength(total * k);
      dot.setAttribute('cx', p.x);
      dot.setAttribute('cy', p.y);
      if (k < 1) {
        const id = raf(tick);
        frames.add(id);
      } else {
        dot.remove();
      }
    };
    const id = raf(tick);
    frames.add(id);
  };

  const hot = (...keys) => {
    Object.values(nodeEls).forEach((n) => n.classList.remove('fs-hot'));
    keys.forEach((k) => nodeEls[k]?.classList.add('fs-hot'));
  };
  const activeLines = (keys) => {
    Object.entries(paths).forEach(([k, p]) => p.classList.toggle('fs-active', keys.includes(k)));
  };
  const pop = (target, kind = 'fs-pop') => {
    target.classList.remove(kind);
    void target.offsetWidth;
    target.classList.add(kind);
  };
  const flashNodes = () => nodesNow().forEach((n, i) => timers.push(setTimeout(() => flash(nodeEls[n.key]), i * 90)));
  const readLines = () => {
    hot(...readers.map((n) => n.key));
    codeAt('reads');
    activeLines(readers.map((n) => n.key));
    readers.forEach((n) => travel(paths[n.key], '#9061DB'));
  };
  const paint = () => phoneView.paint(model.painted, model.paintedLayout);

  const tapStep = () => ({
    caption: `Pulsaste ${sc.triggerName(model.painted)}: onPressed llama a ${sc.fn}.`,
    fx: () => {
      pop(phoneView.trigger, 'fs-press');
      hot(triggerKey());
      codeAt('trigger');
      activeLines(['write']);
      travel(writePath, '#D08A12');
    },
  });

  const forgottenSteps = () => {
    const before = { ...model.vars };
    const change = sc.next(before);
    const after = { ...before, ...change };
    return {
      names: ['Toque', `${main} cambia`, 'Sin build()'],
      steps: [
        tapStep(),
        {
          caption: sc.forgetCaption
            ? sc.forgetCaption(before, after)
            : `${sc.fn} cambia ${main} de ${showValue(before[main])} a ${showValue(after[main])}, pero no llama a setState.`,
          apply: () => {
            model.vars = { ...model.vars, ...change };
            renderState();
          },
          fx: () => {
            Object.values(varBoxes).forEach((b) => pop(b));
            hot('state');
            codeAt('set');
          },
        },
        {
          caption: sc.staleCaption
            ? sc.staleCaption(model.painted)
            : `Flutter no se enteró: build() no corre y la pantalla sigue en ${showValue(model.painted[main])}. Sin error, sin aviso.`,
          fx: () => {
            hot();
            codeAt('none');
            activeLines([]);
          },
        },
      ],
    };
  };

  const toggleSteps = () => {
    if (forgot) return forgottenSteps();
    const before = { ...model.vars };
    const change = sc.next(before);
    const after = { ...before, ...change };
    return {
      names: ['Toque', 'setState', 'build()', 'Leer el estado', 'Pantalla'],
      steps: [
        tapStep(),
        {
          caption: sc.setCaption
            ? sc.setCaption(before, after)
            : `Dentro de setState, ${main} pasa de ${showValue(before[main])} a ${showValue(after[main])} y el State queda sucio. La pantalla todavía no cambia.`,
          apply: () => {
            model.vars = { ...model.vars, ...change };
            model.dirty = true;
            renderState();
          },
          fx: () => {
            Object.values(varBoxes).forEach((b) => pop(b));
            hot('state');
            codeAt('set');
          },
        },
        {
          caption: `Flutter llama build() de ${sc.state}: los widgets se crean otra vez, como objetos nuevos (mira los #). El State es el mismo, #${stateId}.`,
          apply: () => {
            renewIds();
            renderTree();
          },
          fx: () => {
            activeLines([]);
            hot('state');
            codeAt('build');
            flashNodes();
          },
        },
        {
          caption: sc.read(after, model.layout),
          apply: () => {
            model.built = { ...model.vars };
            renderTree();
          },
          fx: readLines,
        },
        {
          caption: sc.paint(after),
          apply: () => {
            model.painted = { ...model.built };
            model.dirty = false;
            paint();
            renderState();
          },
          fx: () => {
            hot();
            codeAt('none');
            activeLines([]);
          },
        },
      ],
    };
  };

  const rebuildSteps = () => ({
    names: [`${sc.app}.build()`, 'Mismo State', 'build()', 'Leer el estado', 'Pantalla'],
    steps: [
      {
        caption: `${sc.app} se reconstruye y crea un ${sc.widget} nuevo: el objeto viejo se descarta.`,
        apply: () => {
          widgetId = newId();
          renderTree();
        },
        fx: () => {
          hot('app', 'widget');
          codeAt('none');
          flash(nodeEls.widget);
        },
      },
      {
        caption: `Flutter le conecta al widget nuevo el mismo ${sc.state} #${stateId}, con el estado intacto.`,
        fx: () => {
          hot('widget', 'state');
          codeAt('none');
          Object.values(varBoxes).forEach((b) => pop(b));
        },
      },
      {
        caption: `build() de ${sc.state} vuelve a correr y crea widgets nuevos.`,
        apply: () => {
          renewIds();
          renderTree();
        },
        fx: () => {
          hot('state');
          codeAt('build');
          flashNodes();
        },
      },
      {
        caption: sc.read(model.vars, model.layout),
        fx: readLines,
      },
      {
        caption: 'La pantalla queda igual: el estado no se perdió con el widget viejo.',
        apply: paint,
        fx: () => {
          hot();
          codeAt('none');
          activeLines([]);
        },
      },
    ],
  });

  // Swapping Text for SongCard is a code change: hot reload runs build() with the
  // same State, so the list keeps every song.
  const layoutSteps = (next) => {
    const widget = next === 'cards' ? 'SongCard' : 'Text';
    const other = next === 'cards' ? 'Text' : 'SongCard';
    const count = model.vars[main].length;
    return {
      names: ['Hot reload', 'build()', 'Leer el estado', 'Pantalla'],
      steps: [
        {
          caption: `Cambiaste ${other} por ${widget} en el código y guardaste: hot reload. ${sc.state} #${stateId} y ${main} siguen iguales.`,
          apply: () => {
            model.layout = next;
            applyCode(sourceOf());
          },
          fx: () => {
            hot('state');
            codeAt('reads');
            pop(varBoxes[main]);
          },
        },
        {
          caption: `build() corre con el código nuevo: ahora crea un ${widget} por canción, todos objetos nuevos.`,
          apply: () => {
            model.builtLayout = next;
            renewIds();
            renderTree();
          },
          fx: () => {
            hot('state');
            codeAt('build');
            flashNodes();
          },
        },
        {
          caption: count
            ? `Cada ${widget} recibe su Song de ${main}: los datos son los mismos ${count === 1 ? '' : `${count} `}de antes.`
            : `${main} sigue vacía: no hay ningún ${widget} que crear. Agrega canciones y vuelve a cambiar.`,
          fx: readLines,
        },
        {
          caption: `La pantalla muestra las mismas canciones, ahora con ${widget}. El estado no cambió.`,
          apply: () => {
            model.paintedLayout = next;
            paint();
          },
          fx: () => {
            hot();
            codeAt('none');
            activeLines([]);
          },
        },
      ],
    };
  };

  let run = null;
  let stepMode = false;
  const nextButton = el('button', { class: 'fs-btn', text: 'Siguiente paso', disabled: true });

  const drawBar = (names, current) => {
    stepBar.replaceChildren(...names.map((name, i) => {
      const kind = i === current ? 'fs-cur' : i < current ? 'fs-past' : '';
      return el('span', { class: `fs-sp ${kind}` }, el('b', { text: String(i + 1) }), name);
    }));
  };

  const clearTimers = () => {
    timers.splice(0).forEach(clearTimeout);
    frames.forEach(cancelRaf);
    frames.clear();
    linesQueued = false;
    lines.querySelectorAll('.fs-dot').forEach((d) => d.remove());
  };

  const settle = () => {
    run = null;
    nextButton.disabled = true;
    hot();
    codeAt('none');
    activeLines([]);
    phoneView.trigger.classList.remove('fs-press');
    scheduleLines();
  };

  const finishNow = () => {
    if (!run) return;
    clearTimers();
    run.plan.steps.slice(run.index + 1).forEach((s) => s.apply?.());
    drawBar(run.plan.names, run.plan.names.length);
    settle();
  };

  const play = (index) => {
    run.index = index;
    const step = run.plan.steps[index];
    drawBar(run.plan.names, index);
    caption.textContent = step.caption;
    step.apply?.();
    step.fx?.();
    const last = index === run.plan.steps.length - 1;
    if (last) {
      timers.push(setTimeout(() => {
        drawBar(run.plan.names, run.plan.names.length);
        settle();
      }, STEP_MS));
      return;
    }
    if (stepMode) {
      nextButton.disabled = false;
      return;
    }
    timers.push(setTimeout(() => play(index + 1), STEP_MS));
  };

  function start(makePlan) {
    finishNow();
    run = { plan: makePlan(), index: -1 };
    play(0);
  }

  // Typing changes a controller's text without setState: the TextField repaints
  // itself and build() does not run.
  function onInput(input, value, focusOnly) {
    const v = sc.vars.find((x) => x.input === input);
    if (!focusOnly) {
      model.vars = { ...model.vars, [v.name]: value };
      model.built = { ...model.built, [v.name]: value };
      model.painted = { ...model.painted, [v.name]: value };
      renderState();
    }
    if (run) return;
    hot(input);
    caption.textContent = sc.typing(v.name);
  }

  nextButton.addEventListener('click', () => {
    if (!run || run.index >= run.plan.steps.length - 1) return;
    nextButton.disabled = true;
    play(run.index + 1);
  });

  const stepToggle = switchControl('Paso a paso', (checked) => {
    stepMode = checked;
    if (!checked && run && !nextButton.disabled) {
      nextButton.disabled = true;
      play(run.index + 1);
    }
  });

  const controls = el('div', { class: 'fs-controls' }, stepToggle.node, nextButton);
  if ((sc.forgetCode || sc.source) && args.includes('forget')) {
    const forgetToggle = switchControl('Olvidar setState', (checked) => {
      finishNow();
      forgot = checked;
      applyCode(sourceOf());
      drawBar(toggleSteps().names, -1);
      caption.textContent = checked
        ? `Ahora ${sc.fn} no llama a setState. Pulsa ${sc.triggerName(model.painted)} varias veces.`
        : sc.idle;
      scheduleLines();
    });
    controls.prepend(forgetToggle.node);
  }
  if (sc.rebuild) {
    controls.prepend(el('button', { class: 'fs-btn', text: `Reconstruir ${sc.app}`, onclick: () => start(rebuildSteps) }));
  }
  if (withCards) {
    const textButton = el('button', { text: 'Text' });
    const cardsButton = el('button', { text: 'SongCard', class: 'fs-sel' });
    const select = (next) => {
      if (next === model.layout && !run) return;
      textButton.className = next === 'text' ? 'fs-sel' : '';
      cardsButton.className = next === 'cards' ? 'fs-sel' : '';
      start(() => layoutSteps(next));
    };
    textButton.addEventListener('click', () => select('text'));
    cardsButton.addEventListener('click', () => select('cards'));
    controls.prepend(el('div', { class: 'fs-seg', role: 'group', 'aria-label': 'Widget de cada canción' }, textButton, cardsButton));
  }

  container.append(el('div', { class: 'fs-col' }, screen.frame, controls), side);
  code.box.addEventListener('scroll', () => scheduleLines());
  paint();
  renderTree();
  renderState();
  drawBar(toggleSteps().names, -1);
  caption.textContent = withCards ? `${sc.idle} Después cambia entre Text y SongCard.` : sc.idle;

  const onResize = () => scheduleLines();
  window.addEventListener('resize', onResize);
  const observer = typeof ResizeObserver === 'function' ? new ResizeObserver(onResize) : null;
  observer?.observe(side);

  return () => {
    clearTimers();
    observer?.disconnect();
    window.removeEventListener('resize', onResize);
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

export const SIMS = Object.freeze({
  'state-counter': mountCounter,
  'hot-reload': (root, args = []) => mountCounter(root, ['reload', ...args]),
  'state-tree': mountTree,
  'state-lifecycle': mountLifecycle,
  playlist: (root, args = []) => mountTree(root, ['playlist', ...args]),
});

export const parseSpec = (spec) => {
  const [name = '', ...args] = String(spec || '').trim().split(/\s+/);
  return { name, args };
};
