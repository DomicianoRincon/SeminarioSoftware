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
.fsim .fs-list-title{font-size:13px;font-weight:600;color:#49454F;margin:2px 0 6px}
.fsim .fs-seg{display:inline-flex;border:1px solid var(--fs-accent);border-radius:20px;overflow:hidden}
.fsim .fs-seg button{border:0;background:#fff;color:var(--fs-accent);padding:6px 14px;font:500 13px Roboto,Arial,sans-serif;cursor:pointer}
.fsim .fs-seg button.fs-sel{background:var(--fs-accent);color:#fff}
.fsim .fs-lc-svg{width:100%;height:auto;display:block}
.fsim .fs-lc-block rect{fill:#fff;stroke:#E3E6EE;stroke-width:1.5;transition:fill .3s,stroke .3s}
.fsim .fs-lc-block{opacity:.4;transition:opacity .3s}
.fsim .fs-lc-block.fs-seen{opacity:1}
.fsim .fs-lc-name{font:700 16px 'JetBrains Mono',Menlo,Consolas,monospace}
.fsim .fs-lc-desc{font:13px Roboto,Arial,sans-serif;fill:#454C61}
.fsim .fs-lc-count{font:700 13px 'JetBrains Mono',Menlo,Consolas,monospace}
.fsim .fs-lc-arrow{fill:none;stroke:#C4CBD8;stroke-width:2;transition:stroke .3s}
.fsim .fs-lc-arrow.fs-on{stroke-width:2.75;stroke-dasharray:7 5;animation:fsimDash .5s linear infinite}
@keyframes fsimDash{to{stroke-dashoffset:-12}}
.fsim .fs-lc-label{font:600 12px Roboto,Arial,sans-serif;fill:#79809A}
.fsim .fs-body.fs-launcher{background:linear-gradient(160deg,#B69DF8,#6750A4 70%,#381E72)}
.fsim .fs-apps{display:grid;grid-template-columns:repeat(4,1fr);gap:14px 6px;padding-top:12px}
.fsim .fs-app{border:0;background:none;display:flex;flex-direction:column;align-items:center;gap:5px;color:#fff;
  font:500 11px Roboto,Arial,sans-serif;cursor:pointer;padding:0}
.fsim .fs-app-icon{width:44px;height:44px;border-radius:12px;display:flex;align-items:center;justify-content:center;
  font-size:20px;font-weight:700;color:#fff;box-shadow:0 0 0 2px rgba(255,255,255,.85),0 3px 8px rgba(0,0,0,.25)}
.fsim .fs-app-off{opacity:.55;cursor:default}
.fsim .fs-app-off .fs-app-icon{box-shadow:0 3px 8px rgba(0,0,0,.2)}
.fsim .fs-hello{font-size:22px;margin:6px 0 14px;color:var(--fs-ink)}
.fsim .fs-faint{color:#9E9AA7;font-size:13px}
.fsim .fs-lift-tree{overflow:hidden}
.fsim .fs-lift-node{display:flex;flex-wrap:wrap;align-items:center;gap:5px;margin:4px 0;padding:4px 8px;border-radius:8px;
  border:1px solid var(--fs-line);background:#fff;font-family:'JetBrains Mono',Menlo,Consolas,monospace;font-size:12.5px;width:fit-content;max-width:100%}
.fsim .fs-lift-node b{font-weight:600}
.fsim .fs-lift-node.fs-hot{box-shadow:0 0 0 3px #F2C069;border-color:#A96C05}
.fsim .fs-lift-param{font-size:11px;padding:0 7px;border-radius:9px;border:1px solid}
.fsim .fs-lift-param.fs-down{background:#E6F0FF;border-color:#7FA6E8;color:#1F4FA8}
.fsim .fs-lift-param.fs-up{background:#FFF3DC;border-color:#E2B25C;color:#8A5600}
.fsim .fs-lift-param.fs-pass{background:#F1F2F5;border-color:#B8BDC9;border-style:dashed;color:#79809A}
.fsim .fs-lift-builds{font-size:11px;color:#fff;background:#625B71;border-radius:9px;padding:0 7px}
.fsim .fs-lift-holder{margin:2px 0 8px 18px;padding:8px 10px;border-radius:10px;background:#F4EBFF;border:1px solid #C9A6EE}
.fsim .fs-lift-holder-head{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:center;font-size:12px;font-weight:600;color:#7439B8;margin-bottom:4px}
.fsim .fs-lift-var{display:flex;flex-wrap:wrap;align-items:center;gap:6px;font-family:'JetBrains Mono',Menlo,Consolas,monospace;font-size:12.5px;margin:3px 0}
.fsim .fs-lift-val{background:#fff;border:1px solid #C9A6EE;border-radius:6px;padding:0 6px;overflow-wrap:anywhere}
.fsim .fs-lift-songs{display:flex;flex-wrap:wrap;gap:4px;margin:2px 0 4px}
.fsim .fs-lift-song{font-size:11.5px;padding:2px 8px;border-radius:8px;background:#E6F0FF;border:1px solid #7FA6E8;color:#1C2B4A}
.fsim .fs-lift-song b{color:#1F4FA8}
.fsim .fs-lift-song.fs-fav{background:#FFE4EC;border-color:#E58AA5}
.fsim .fs-lift-legend{font-size:12px;color:var(--fs-muted);margin-top:8px}
.fsim .fs-lift-packet{position:absolute;left:0;top:0;z-index:3;font:600 11.5px 'JetBrains Mono',Menlo,Consolas,monospace;
  padding:3px 9px;border-radius:12px;color:#fff;opacity:0;pointer-events:none;transition:transform .9s ease-in-out,opacity .2s;white-space:nowrap}
.fsim .fs-lift-packet.fs-down{opacity:1;background:#2F6FD6}
.fsim .fs-lift-packet.fs-up{opacity:1;background:#D08A12}
.fsim .fs-lift-error{color:var(--fs-err);font-size:12.5px;margin:-6px 0 10px}
.fsim .fs-lift-actions{display:flex;gap:2px}
.fsim .fs-lift-act{border:0;background:none;cursor:pointer;font-size:18px;color:var(--fs-accent);padding:2px 4px}
.fsim .fs-lift-act.fs-on{color:#C2354F}
.fsim .fs-cmp-bar{flex:1 1 100%;display:flex}
.fsim .fs-cmp-tall .fs-phone{height:600px}
.fsim .fs-cmp-state{display:flex;flex-direction:column;gap:8px}
.fsim .fs-cmp-panel{display:flex;flex-direction:column;gap:10px;padding-right:80px}
.fsim .fs-cmp-tree .fs-lift-node{margin:3px 0}
.fsim .fs-lift-node.fs-cmp-holder{background:#F4EBFF;border-color:#C9A6EE}
.fsim .fs-lift-node.fs-cmp-part{background:#EEF1FF;border-color:#A9B4F2}
.fsim .fs-cmp-group{margin:0}
.fsim .fs-lines .fs-cmp-bind{fill:none;stroke-width:1.5}
.fsim .fs-lines .fs-cmp-bind.fs-on{stroke-width:2.75}
.fsim .fs-cmp-var{cursor:pointer;border-radius:6px;padding:1px 4px;margin-left:-4px}
.fsim .fs-cmp-var:hover{background:rgba(255,255,255,.7)}
.fsim .fs-cmp-var.fs-sel{background:#fff;box-shadow:0 0 0 2px var(--fs-cmp-color)}
.fsim .fs-cmp-var:focus{outline:none}
.fsim .fs-cmp-var:focus-visible{outline:2px dashed var(--fs-cmp-color);outline-offset:2px}
.fsim .fs-cmp-var.fs-sel .fs-var-name{color:var(--fs-cmp-color)}
.fsim .fs-cmp-summary{display:flex;align-items:center;justify-content:space-between;font-size:14px;font-weight:500;margin:0 0 8px}
.fsim .fs-cb-levels{display:flex;flex-direction:column;gap:10px}
.fsim .fs-cb-level{transition:box-shadow .3s,border-color .3s}
.fsim .fs-cb-level.fs-hot{border-color:#2F6FD6;box-shadow:0 0 0 2px #2F6FD6}
.fsim .fs-cb-head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:4px 12px;margin-bottom:8px;font-size:14px}
.fsim .fs-cb-head b{font-family:'JetBrains Mono',Menlo,Consolas,monospace;font-size:13px}
.fsim .fs-cb-tag{font-size:12px;font-weight:600;color:#4453C9}
.fsim .fs-cb-statebox{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px;margin-bottom:8px;padding:6px 10px;border-radius:10px;background:#F4EBFF;border:1px solid #C9A6EE}
.fsim .fs-cb-statelabel{font-size:12px;font-weight:600;color:#7439B8}
.fsim .fs-cb-state{margin:0}
.fsim .fs-cb-trash:disabled{opacity:.45;cursor:default}
.fsim .fs-cb-trash.fs-cb-ask{opacity:1;animation:fsimCbAsk 1s ease-in-out infinite}
@keyframes fsimCbAsk{0%,100%{transform:scale(1)}50%{transform:scale(1.3)}}
.fsim .fs-ns-phone{height:510px}
.fsim .fs-ns-screen{flex:1;display:flex;flex-direction:column;min-height:0;position:relative;background:#FEF7FF}
.fsim .fs-ns-screen.fs-ns-closed{background:#1C1B1F;color:#E6E1E5}
.fsim .fs-ns-closed .fs-center{color:#E6E1E5}
.fsim .fs-ns-navbar{height:36px;flex:0 0 36px;display:flex;align-items:center;justify-content:space-around;background:#F3EDF7;color:#79747E;font-size:15px}
.fsim .fs-ns-sysback{border:0;background:none;font-size:18px;color:#1C1B1F;cursor:pointer;padding:2px 16px;border-radius:14px}
.fsim .fs-ns-sysback:hover{background:#E8DEF8}
.fsim .fs-ns-sysback:disabled{opacity:.35;cursor:default;background:none}
.fsim .fs-ns-appbar{justify-content:flex-start}
.fsim .fs-ns-title{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.fsim .fs-ns-icon{border:0;background:none;font-size:18px;line-height:1;cursor:pointer;color:#1C1B1F;padding:4px 6px;border-radius:14px}
.fsim .fs-ns-icon:hover{background:rgba(255,255,255,.55)}
.fsim .fs-ns-songbtn{display:block;width:100%;border:0;background:none;padding:0;text-align:left;cursor:pointer;font:inherit;color:inherit;border-radius:16px}
.fsim .fs-ns-songbtn:hover .fs-card{box-shadow:0 0 0 2px var(--fs-accent-soft),0 2px 8px rgba(103,80,164,.16)}
.fsim .fs-ns-logo{font-size:52px;color:var(--fs-accent);line-height:1}
.fsim .fs-ns-detail{display:flex;flex-direction:column;align-items:center;text-align:center;gap:2px}
.fsim .fs-ns-detail .fs-cover{width:150px;height:150px;flex:0 0 auto;border-radius:20px;margin:6px 0 4px}
.fsim .fs-ns-detail .fs-hello{margin:6px 0 0}
.fsim .fs-ns-btn{border:0;border-radius:20px;padding:9px 22px;background:var(--fs-accent);color:#fff;font:500 14px Roboto,Arial,sans-serif;cursor:pointer;margin-top:12px}
.fsim .fs-ns-btn:disabled{opacity:.6;cursor:default}
.fsim .fs-ns-stack{display:flex;flex-direction:column;gap:6px;min-height:44px}
.fsim .fs-ns-card{display:flex;flex-wrap:wrap;align-items:center;gap:4px 10px;padding:8px 10px;border-radius:10px;border:1px solid #C9A6EE;
  background:#F4EBFF;transition:opacity .4s,transform .4s}
.fsim .fs-ns-card.fs-ns-top{background:#fff;border-color:var(--fs-accent);box-shadow:0 2px 8px rgba(103,80,164,.2)}
.fsim .fs-ns-card.fs-ns-new{animation:fsimDrop .5s ease-out}
@keyframes fsimDrop{0%{transform:translateY(-26px);opacity:0}100%{transform:none;opacity:1}}
.fsim .fs-ns-card.fs-ns-out{opacity:.45;transform:translateX(28px)}
.fsim .fs-ns-card.fs-ns-cross{opacity:.7;border-color:#F3A3B2;background:#FFEBEF}
.fsim .fs-ns-card.fs-ns-cross .fs-ns-sname{text-decoration:line-through}
.fsim .fs-ns-card.fs-ns-wait{border-color:#F0C572;background:#FFF8EA}
.fsim .fs-ns-route{font:600 13px 'JetBrains Mono',Menlo,Consolas,monospace;color:var(--fs-accent)}
.fsim .fs-ns-sname{font:13px 'JetBrains Mono',Menlo,Consolas,monospace;flex:1 1 auto;white-space:nowrap}
.fsim .fs-ns-icon svg{width:20px;height:20px;display:block}
.fsim .fs-ns-arg{flex:1 1 100%;font:12px 'JetBrains Mono',Menlo,Consolas,monospace;color:#1F4FA8}
.fsim .fs-ns-base{margin-top:8px;border-top:3px solid #C4CBD8;font-size:11px;color:var(--fs-muted);text-align:center;padding-top:2px}
.fsim .fs-tag.fs-ns-alive{background:#EEF1FF;color:#4453C9}
.fsim .fs-row.fs-ns-found{background:#EADDFF;font-weight:600}
.fsim .fs-ns-err{flex:1;background:#B3261E;color:#fff;padding:16px;display:flex;flex-direction:column;gap:10px;
  font:12.5px 'JetBrains Mono',Menlo,Consolas,monospace;overflow-wrap:anywhere}
.fsim .fs-nr-wait{font-size:12px;font-weight:600;padding:2px 10px;border-radius:10px;background:#FFF3DC;color:#A96C05}
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

const DART_KEYWORDS = new Set(['class', 'extends', 'void', 'return', 'final', 'const', 'if', 'for', 'in', 'this', 'super', 'late', 'true', 'false', 'async', 'await', 'is', 'as']);
const DART_TYPES = new Set(['int', 'String', 'List', 'Widget', 'State', 'StatefulWidget', 'StatelessWidget', 'BuildContext', 'Scaffold', 'Text', 'TextEditingController', 'Column', 'Song', 'SongCard', 'FloatingActionButton', 'TextField', 'MyHomePage', 'GreetingScreen', 'PlaylistScreen', 'SingleChildScrollView', 'FilledButton', 'AppBar', 'Future', 'Navigator', 'ModalRoute', 'SongForm']);
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
      const empty = !song.title && !song.artist ? ' Con los campos vacíos entra una canción vacía: se arregla en la sesión 7.' : '';
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

// ──────────────────────────────────── lift ────────────────────────────────────

// The playlist after lifting state: PlaylistScreen keeps _songs, SongForm keeps only
// its draft and the rest receive what they show through the constructor. Every step
// moves one packet between two widgets: data goes down, events go up.
// Stages: default = SongList extracted (form still in the Screen); `events` adds
// SongForm with onAdd and onDelete on each card; `fav` adds the favorite and copyWith.

const LIFT_STEP_MS = 1300;

const mountLift = (root, args = []) => {
  const stage = args.includes('fav') ? 2 : args.includes('events') ? 1 : 0;
  const container = card(root);
  const timers = [];
  let nextSongId = 1;
  const draftOwner = stage ? 'form' : 'screen';

  const model = {
    songs: [],
    painted: [],
    draft: { title: '', artist: '', imageUrl: DEFAULT_IMAGE },
    showError: false,
    dirty: false,
    builds: { screen: 1, form: 1, list: 1 },
  };

  // ── phone
  const screen = phone('Mi playlist');
  const fields = {};
  const field = (label, key, placeholder) => {
    const node = el('input', { class: 'fs-field', placeholder, 'aria-label': label });
    node.value = model.draft[key];
    node.addEventListener('input', () => onType(key, node.value));
    node.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') submit();
    });
    fields[key] = node;
    return [el('div', { class: 'fs-label', text: label }), node];
  };
  const addButton = el('button', { class: 'fs-filled', text: 'Agregar', onclick: () => submit() });
  const errorText = el('div', { class: 'fs-lift-error', text: 'Escribe el nombre y el artista' });
  errorText.hidden = true;
  const listBox = el('div', { 'data-testid': 'lift-list' });
  screen.body.append(
    ...field('Nombre de la canción', 'title', 'Yellow'),
    ...field('Artista', 'artist', 'Coldplay'),
    ...field('URL de la imagen', 'imageUrl', DEFAULT_IMAGE),
    addButton,
    errorText,
    listBox
  );

  const phoneCard = (song) => {
    const node = songCard(song);
    const icon = node.querySelector('.fs-card-icon');
    const actions = el('span', { class: 'fs-lift-actions' });
    if (stage >= 2) {
      actions.appendChild(el('button', {
        class: `fs-lift-act${song.isFavorite ? ' fs-on' : ''}`,
        'aria-label': `Favorita ${song.title}`,
        text: song.isFavorite ? '♥' : '♡',
        onclick: () => toggleFavorite(song.id),
      }));
    }
    if (stage >= 1) {
      actions.appendChild(el('button', {
        class: 'fs-lift-act',
        'aria-label': `Quitar ${song.title}`,
        text: '🗑',
        onclick: () => remove(song.id),
      }));
    }
    if (stage >= 1) icon.replaceWith(actions);
    return node;
  };

  const paintPhone = () => {
    const before = listBox.querySelectorAll('.fs-card').length;
    const songs = model.painted;
    listBox.replaceChildren(...(songs.length
      ? songs.map(phoneCard)
      : [el('div', { class: 'fs-empty', text: 'Todavía no hay canciones' })]));
    if (songs.length > before) {
      flash(listBox.lastChild);
      screen.body.scrollTop = screen.body.scrollHeight;
    }
  };
  const paintDraft = () => {
    Object.entries(fields).forEach(([key, node]) => {
      if (node.value !== model.draft[key]) node.value = model.draft[key];
    });
    errorText.hidden = !model.showError;
  };

  // ── tree with the two state holders
  const treePanel = el('div', { class: 'fs-panel fs-rel fs-lift-tree' });
  const packet = el('div', { class: 'fs-lift-packet', 'aria-hidden': 'true' });
  let nodeEls = {};
  let paramEls = {};

  const songBlock = (song) => el('span', { class: `fs-lift-song${song.isFavorite ? ' fs-fav' : ''}`, 'data-song': String(song.id) },
    el('b', { text: `Song #${song.id}` }),
    ` ${shorten(song.title || '—', 12)} · ${shorten(song.artist || '—', 10)}${song.isFavorite ? ' ♥' : ''}`);

  const draftRows = () => [
    ...['title', 'artist', 'imageUrl'].map((key) => el('div', { class: 'fs-lift-var' },
      el('span', { class: 'fs-var-type', text: 'String' }),
      el('span', { class: 'fs-var-name', text: `_${key}Controller.text` }),
      el('span', { class: 'fs-lift-val', 'data-testid': `draft-${key}`, text: `'${shorten(model.draft[key], 18)}'` }))),
    ...(stage ? [el('div', { class: 'fs-lift-var' },
      el('span', { class: 'fs-var-type', text: 'bool' }),
      el('span', { class: 'fs-var-name', text: '_showError' }),
      el('span', { class: 'fs-lift-val', 'data-testid': 'draft-showError', text: String(model.showError) }))] : []),
  ];

  const holder = (title, testid, rows, tag) => el('div', { class: 'fs-lift-holder', 'data-testid': testid },
    el('div', { class: 'fs-lift-holder-head' }, el('span', { text: title }), tag),
    ...rows);

  const screenHolder = () => {
    const tag = el('span', {
      class: `fs-tag${model.dirty ? ' fs-dirty' : ''}`,
      text: model.dirty ? 'sucio: pide build()' : 'al día',
    });
    const songs = el('div', { class: 'fs-lift-songs', 'data-testid': 'lift-songs' },
      ...(model.songs.length ? model.songs.map(songBlock) : [el('span', { class: 'fs-faint', text: '[ ] vacía' })]));
    const rows = [el('div', { class: 'fs-lift-var' },
      el('span', { class: 'fs-var-type', text: 'List<Song>' }),
      el('span', { class: 'fs-var-name', text: '_songs' })), songs];
    if (draftOwner === 'screen') rows.push(...draftRows());
    return holder('Estado · _PlaylistScreenState', 'screen-state', rows, tag);
  };

  const param = (owner, name, kind) => {
    const hint = kind === 'pass' ? 'solo lo pasa' : '';
    const node = el('span', { class: `fs-lift-param fs-${kind}`, title: hint || undefined, text: name });
    paramEls[`${owner}.${name}`] = node;
    return node;
  };

  const nodeRow = (key, depth, name, params = [], builds) => {
    const row = el('div', { class: 'fs-lift-node', 'data-node': key, style: `margin-left:${depth * 18}px` },
      el('b', { text: name }),
      ...params.map(([n, kind]) => param(key, n, kind)),
      builds ? el('span', { class: 'fs-lift-builds', 'data-testid': `builds-${key}`, text: `build ×${model.builds[key]}` }) : null);
    nodeEls[key] = row;
    return row;
  };

  const callbacks = stage >= 2 ? ['onDelete', 'onToggleFavorite'] : stage >= 1 ? ['onDelete'] : [];

  const renderTree = () => {
    nodeEls = {};
    paramEls = {};
    const items = [
      el('h4', { text: 'Árbol · datos ↓ por constructor · eventos ↑ por funciones' }),
      nodeRow('screen', 0, 'PlaylistScreen', [], true),
      screenHolder(),
      nodeRow('appbar', 1, 'AppBar'),
    ];
    if (stage) {
      items.push(nodeRow('form', 1, 'SongForm', [['onAdd', 'up']], true));
      items.push(holder('Borrador · _SongFormState', 'form-state', draftRows()));
    } else {
      items.push(nodeRow('form', 1, 'TextField ×3 · FilledButton'));
    }
    items.push(nodeRow('list', 1, 'SongList', [['songs', 'down'], ...callbacks.map((c) => [c, 'pass'])], true));
    if (model.built?.length) {
      model.built.forEach((song) => items.push(nodeRow(`card-${song.id}`, 2, 'SongCard',
        [[`song #${song.id}`, 'down'], ...callbacks.map((c) => [c, 'up'])])));
    } else {
      items.push(nodeRow('empty', 2, "Text('Todavía no hay canciones')"));
    }
    if (callbacks.length) {
      items.push(el('div', { class: 'fs-lift-legend' },
        el('span', { class: 'fs-lift-param fs-pass', text: 'gris' }),
        ' SongList recibe las funciones solo para pasárselas a SongCard: prop drilling.'));
    }
    treePanel.replaceChildren(...items, packet);
  };
  model.built = [];

  const hot = (...keys) => {
    Object.values(nodeEls).forEach((n) => n.classList.remove('fs-hot'));
    keys.forEach((k) => nodeEls[k]?.classList.add('fs-hot'));
  };
  const box = (node) => {
    const base = treePanel.getBoundingClientRect();
    const r = node.getBoundingClientRect();
    return { x: r.left - base.left, y: r.top - base.top, w: r.width, h: r.height };
  };
  // One packet, one jump: it starts on the sender and slides to the receiver.
  const send = (from, to, label, kind) => {
    const a = nodeEls[from];
    const b = nodeEls[to];
    packet.textContent = label;
    packet.className = `fs-lift-packet fs-${kind}`;
    if (!a || !b) return;
    const pa = box(a);
    const pb = box(b);
    packet.style.transition = 'none';
    packet.style.transform = `translate(${pa.x + pa.w + 8}px, ${pa.y}px)`;
    void packet.offsetWidth;
    packet.style.transition = '';
    packet.style.transform = `translate(${pb.x + pb.w + 8}px, ${pb.y}px)`;
    hot(from, to);
  };
  const hidePacket = () => {
    packet.className = 'fs-lift-packet';
  };
  const pop = (node, kind = 'fs-flash') => {
    if (!node) return;
    node.classList.remove(kind);
    void node.offsetWidth;
    node.classList.add(kind);
  };

  // ── steps panel
  const stepBar = el('div', { class: 'fs-stepbar' });
  const caption = el('div', { class: 'fs-caption', 'data-testid': 'lift-caption' });
  const stepsPanel = el('div', { class: 'fs-panel' }, stepBar, caption);
  const drawBar = (names, current) => {
    stepBar.replaceChildren(...names.map((name, i) => {
      const kind = i === current ? 'fs-cur' : i < current ? 'fs-past' : '';
      return el('span', { class: `fs-sp ${kind}` }, el('b', { text: String(i + 1) }), name);
    }));
  };

  let run = null;
  let stepMode = false;
  const nextButton = el('button', { class: 'fs-btn', text: 'Siguiente paso', disabled: true });
  const clearTimers = () => timers.splice(0).forEach(clearTimeout);
  const settle = () => {
    run = null;
    nextButton.disabled = true;
    hot();
    hidePacket();
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
    caption.textContent = step.caption();
    step.apply?.();
    step.fx?.();
    if (index === run.plan.steps.length - 1) {
      timers.push(setTimeout(() => {
        drawBar(run.plan.names, run.plan.names.length);
        settle();
      }, LIFT_STEP_MS));
      return;
    }
    if (stepMode) {
      nextButton.disabled = false;
      return;
    }
    timers.push(setTimeout(() => play(index + 1), LIFT_STEP_MS));
  };
  const start = (plan) => {
    finishNow();
    run = { plan, index: -1 };
    play(0);
  };
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

  // The Screen changes its list inside setState; the three steps after it are always
  // the same: the Screen builds, SongList builds, the phone paints.
  const downSteps = (change) => [
    {
      name: 'setState',
      caption: change.caption,
      apply: () => {
        change.apply();
        model.dirty = true;
        renderTree();
      },
      fx: () => {
        hidePacket();
        hot('screen');
        flash(treePanel.querySelector('[data-testid="lift-songs"]'));
      },
    },
    {
      name: 'Baja a SongList',
      caption: () => `build() de la Screen crea SongList y le pasa la lista por el constructor: songs, ${model.songs.length === 1 ? '1 canción' : `${model.songs.length} canciones`}.${callbacks.length ? ` También le pasa ${callbacks.join(' y ')}, que SongList no usa.` : ''}${stage ? ' SongForm también se reconstruye, pero su State es el mismo: el borrador no se pierde.' : ''}`,
      apply: () => {
        model.builds.screen += 1;
        if (stage) model.builds.form += 1;
        model.dirty = false;
        renderTree();
      },
      fx: () => {
        send('screen', 'list', `songs${callbacks.length ? ` · ${callbacks.join(' · ')}` : ''}`, 'down');
        pop(paramEls['list.songs']);
        callbacks.forEach((c) => pop(paramEls[`list.${c}`]));
      },
    },
    {
      name: 'Baja a SongCard',
      caption: () => (model.songs.length
        ? `build() de SongList recorre songs y crea una SongCard por canción. Cada una recibe su song${callbacks.length ? ` y ${callbacks.join(' y ')}` : ''}.`
        : 'build() de SongList ve songs vacía: en lugar de tarjetas muestra «Todavía no hay canciones». Decide con lo que recibe.'),
      apply: () => {
        model.builds.list += 1;
        model.built = [...model.songs];
        renderTree();
      },
      fx: () => {
        const first = model.built.length ? `card-${model.built[model.built.length - 1].id}` : 'empty';
        send('list', first, model.built.length ? 'song' : 'songs.isEmpty', 'down');
      },
    },
    {
      name: 'Pantalla',
      caption: () => `Flutter pinta: la pantalla muestra ${model.songs.length === 1 ? '1 canción' : `${model.songs.length} canciones`}. Nadie más que PlaylistScreen tocó _songs.`,
      apply: () => {
        model.painted = [...model.songs];
        paintPhone();
      },
      fx: () => {
        hidePacket();
        hot();
      },
    },
  ];
  const plan = (first, change) => {
    const steps = [first, ...downSteps(change)];
    return { names: steps.map((s) => s.name), steps };
  };

  function submit() {
    const { title, artist, imageUrl } = model.draft;
    if (stage && (!title.trim() || !artist.trim())) {
      finishNow();
      model.showError = true;
      model.builds.form += 1;
      renderTree();
      paintDraft();
      hot('form');
      drawBar(['setState en SongForm'], 0);
      caption.textContent = 'Falta el nombre o el artista: SongForm no llama a onAdd. Su setState prende _showError y solo se reconstruye SongForm. PlaylistScreen ni se entera.';
      timers.push(setTimeout(() => {
        drawBar(['setState en SongForm'], 1);
        hot();
      }, LIFT_STEP_MS));
      return;
    }
    const song = { id: nextSongId++, title, artist, imageUrl: imageUrl || DEFAULT_IMAGE, isFavorite: false };
    const first = stage
      ? {
        name: 'Sube onAdd',
        caption: () => `SongForm arma Song #${song.id} con su borrador y llama widget.onAdd(song): el evento sube a la Screen. SongForm no sabe quién lo recibe. Después limpia su borrador con clear().`,
        apply: () => {
          model.draft = { ...model.draft, title: '', artist: '' };
          model.showError = false;
          model.builds.form += 1;
          renderTree();
          paintDraft();
        },
        fx: () => {
          pop(addButton, 'fs-press');
          send('form', 'screen', 'onAdd(song)', 'up');
        },
      }
      : {
        name: 'Toque',
        caption: () => 'Pulsaste Agregar: onPressed llama a _addSong(). El formulario todavía es parte de la Screen, así que todo pasa en el mismo State.',
        fx: () => {
          pop(addButton, 'fs-press');
          hot('form', 'screen');
        },
      };
    start(plan(first, {
      caption: () => `_addSong(${stage ? 'song' : ''}) corre en la Screen: dentro de setState, Song #${song.id} entra a _songs y el State queda sucio. La pantalla todavía no cambia.`,
      apply: () => {
        model.songs = [...model.songs, song];
      },
    }));
  }

  function remove(id) {
    const song = model.songs.find((s) => s.id === id);
    if (!song) return;
    start(plan({
      name: 'Sube onDelete',
      caption: () => `La SongCard de Song #${id} llama onDelete(). La función la escribió PlaylistScreen al crear la tarjeta, así que corre allá. La tarjeta no sabe qué hace.`,
      fx: () => send(`card-${id}`, 'screen', 'onDelete()', 'up'),
    }, {
      caption: () => `_deleteSong(song) corre en la Screen: dentro de setState, Song #${id} sale de _songs.`,
      apply: () => {
        model.songs = model.songs.filter((s) => s.id !== id);
      },
    }));
  }

  function toggleFavorite(id) {
    const old = model.songs.find((s) => s.id === id);
    if (!old) return;
    const fresh = { ...old, id: nextSongId++, isFavorite: !old.isFavorite };
    start(plan({
      name: 'Sube onToggleFavorite',
      caption: () => `La SongCard de Song #${id} llama onToggleFavorite(): el evento sube a la Screen.`,
      fx: () => send(`card-${id}`, 'screen', 'onToggleFavorite()', 'up'),
    }, {
      caption: () => `Dentro de setState, la Screen no toca Song #${id}: copyWith(isFavorite: ${fresh.isFavorite}) crea Song #${fresh.id}, una copia con un solo campo cambiado, y la pone en su lugar.`,
      apply: () => {
        model.songs = model.songs.map((s) => (s.id === id ? fresh : s));
      },
    }));
  }

  function onType(key, value) {
    model.draft = { ...model.draft, [key]: value };
    renderTree();
    if (run) return;
    hot('form');
    caption.textContent = draftOwner === 'screen'
      ? `Escribir cambia _${key}Controller.text, que vive en el State de la Screen, sin setState: build() no corre.`
      : `Escribir cambia el borrador de SongForm, sin setState. PlaylistScreen no se entera: lo que todavía no se envía no es asunto suyo.`;
  }

  container.append(
    el('div', { class: 'fs-col' }, screen.frame, el('div', { class: 'fs-controls' }, stepToggle.node, nextButton)),
    el('div', { class: 'fs-side' }, treePanel, stepsPanel)
  );
  paintPhone();
  renderTree();
  drawBar(plan({ name: stage ? 'Sube onAdd' : 'Toque' }, {}).names, -1);
  caption.textContent = [
    'Agrega dos o tres canciones y sigue el paquete: la lista vive en la Screen y baja por el constructor, primero a SongList y luego a cada SongCard.',
    'Agrega canciones y quita una. Los datos bajan (azul) y los eventos suben (naranja): ningún componente toca _songs.',
    'Agrega canciones y marca una como favorita: mira el número de la Song antes y después de copyWith.',
  ][stage];

  return () => {
    clearTimers();
    root.replaceChildren();
  };
};

// ─────────────────────────────────── compose ──────────────────────────────────

// Two tabs of the same playlist. "Sin componentes" is where the session starts: one
// Screen that holds every variable and every widget, so state lines reach deep into
// the tree. "Con componentes" is where it ends: named pieces, a Screen whose state only
// touches its direct children, and SongForm holding its own draft.

const COMPOSE_COLORS = ['#7439B8', '#0F8478', '#C2354F', '#A96C05', '#4453C9', '#3A8235'];
const COMPOSE_GRAY = '#B8BDC9';

const mountCompose = (root) => {
  const container = card(root);
  let nextId = 1;
  const model = {
    songs: [],
    onlyFavorites: false,
    draft: { title: '', artist: '', imageUrl: DEFAULT_IMAGE },
    showError: false,
  };
  let tab = 'flat';

  const screen = phone('Mi playlist');
  const treeBox = el('div', { class: 'fs-cmp-tree' });
  const stateBox = el('div', { class: 'fs-cmp-state' });
  const lines = svgEl('svg', { class: 'fs-lines', 'aria-hidden': 'true' });
  const panel = el('div', { class: 'fs-panel fs-rel fs-cmp-panel' }, treeBox, stateBox, lines);
  const caption = el('div', { class: 'fs-caption', 'data-testid': 'compose-caption' });
  let nodeEls = {};
  let varEls = {};
  let bindings = [];
  let selected = null;

  // ── phone
  const field = (label, key, placeholder) => {
    const node = el('input', { class: 'fs-field', placeholder, 'aria-label': label });
    node.value = model.draft[key];
    node.addEventListener('input', () => {
      model.draft = { ...model.draft, [key]: node.value };
      renderState();
    });
    return [el('div', { class: 'fs-label', text: label }), node];
  };

  const add = () => {
    const { title, artist, imageUrl } = model.draft;
    if (tab === 'parts' && (!title.trim() || !artist.trim())) {
      model.showError = true;
      render();
      return;
    }
    model.songs = [...model.songs, { id: nextId++, title, artist, imageUrl: imageUrl || DEFAULT_IMAGE, isFavorite: false }];
    if (tab === 'parts') {
      model.draft = { ...model.draft, title: '', artist: '' };
      model.showError = false;
    }
    render();
  };
  const update = (id, change) => {
    model.songs = model.songs.map((s) => (s.id === id ? { ...s, ...change } : s));
    render();
  };

  const visible = () => (tab === 'parts' && model.onlyFavorites ? model.songs.filter((s) => s.isFavorite) : model.songs);

  const partsCard = (song) => {
    const node = songCard(song);
    node.querySelector('.fs-card-icon').replaceWith(el('span', { class: 'fs-lift-actions' },
      el('button', {
        class: `fs-lift-act${song.isFavorite ? ' fs-on' : ''}`,
        'aria-label': `Favorita ${song.title}`,
        text: song.isFavorite ? '♥' : '♡',
        onclick: () => update(song.id, { isFavorite: !song.isFavorite }),
      }),
      el('button', {
        class: 'fs-lift-act',
        'aria-label': `Quitar ${song.title}`,
        text: '🗑',
        onclick: () => {
          model.songs = model.songs.filter((s) => s.id !== song.id);
          render();
        },
      })));
    return node;
  };

  const renderPhone = () => {
    const top = screen.body.scrollTop;
    const body = [];
    if (tab === 'parts') {
      const count = model.songs.length;
      body.push(el('div', { class: 'fs-cmp-summary' },
        el('span', { text: count === 1 ? '1 canción' : `${count} canciones` }),
        el('button', {
          class: `fs-lift-act${model.onlyFavorites ? ' fs-on' : ''}`,
          'aria-label': 'Solo favoritas',
          text: model.onlyFavorites ? '♥' : '♡',
          onclick: () => {
            model.onlyFavorites = !model.onlyFavorites;
            render();
          },
        })));
    }
    body.push(
      ...field('Nombre de la canción', 'title', 'Yellow'),
      ...field('Artista', 'artist', 'Coldplay'),
      ...field('URL de la imagen', 'imageUrl', DEFAULT_IMAGE),
      el('button', { class: 'fs-filled', text: 'Agregar', onclick: add })
    );
    if (tab === 'parts' && model.showError) body.push(el('div', { class: 'fs-lift-error', text: 'Escribe el nombre y el artista' }));
    const songs = visible();
    const list = el('div', { 'data-testid': 'compose-list' },
      ...(tab === 'parts' && !songs.length
        ? [el('div', { class: 'fs-empty', text: model.onlyFavorites ? 'No tienes favoritas' : 'Todavía no hay canciones' })]
        : songs.map((s) => (tab === 'parts' ? partsCard(s) : songCard(s)))));
    body.push(list);
    screen.body.replaceChildren(...body);
    screen.body.scrollTop = top;
  };

  // ── tree
  const row = (key, depth, name, kind = '') => {
    const node = el('div', { class: `fs-lift-node fs-cmp-${kind || 'plain'}`, 'data-node': key, style: `margin-left:${depth * 16}px` },
      el('b', { text: name }));
    nodeEls[key] = node;
    return node;
  };

  const flatTree = () => {
    const nodes = [
      row('screen', 0, 'PlaylistScreen', 'holder'),
      row('scaffold', 1, 'Scaffold'),
      row('appbar', 2, 'AppBar'),
      row('scroll', 2, 'SingleChildScrollView'),
      row('column', 3, 'Column'),
      row('title', 4, "TextField('Canción')"),
      row('artist', 4, "TextField('Artista')"),
      row('imageUrl', 4, "TextField('URL')"),
      row('button', 4, "FilledButton('Agregar')"),
      ...model.songs.map((s) => row(`card-${s.id}`, 4, `SongCard('${shorten(s.title || '—', 12)}')`, 'part')),
    ];
    bindings = [
      ['_titleController', ['title']],
      ['_artistController', ['artist']],
      ['_imageUrlController', ['imageUrl']],
      ['_songs', model.songs.map((s) => `card-${s.id}`)],
    ];
    return nodes;
  };

  const partsTree = () => {
    const nodes = [
      row('screen', 0, 'PlaylistScreen', 'holder'),
      row('scaffold', 1, 'Scaffold'),
      row('appbar', 2, 'AppBar'),
      row('scroll', 2, 'SingleChildScrollView · Column'),
      row('summary', 3, 'PlaylistSummary', 'part'),
      row('form', 3, 'SongForm', 'holder'),
      row('title', 4, "TextField('Canción')"),
      row('artist', 4, "TextField('Artista')"),
      row('imageUrl', 4, "TextField('URL')"),
      row('button', 4, "FilledButton('Agregar')"),
    ];
    if (model.showError) nodes.push(row('error', 4, "Text('Escribe el nombre…')"));
    nodes.push(row('list', 3, 'SongList', 'part'));
    visible().forEach((s) => nodes.push(row(`card-${s.id}`, 4, `SongCard('${shorten(s.title || '—', 12)}')`, 'part')));
    bindings = [
      ['_songs', ['summary', 'list']],
      ['_onlyFavorites', ['summary', 'list']],
      ['_titleController', ['title']],
      ['_artistController', ['artist']],
      ['_imageUrlController', ['imageUrl']],
      ['_showError', model.showError ? ['error'] : []],
    ];
    return nodes;
  };

  const renderTree = () => {
    nodeEls = {};
    const nodes = tab === 'flat' ? flatTree() : partsTree();
    treeBox.replaceChildren(el('h4', { text: tab === 'flat' ? 'Árbol de widgets' : 'Árbol de componentes' }), ...nodes);
  };

  // ── state groups, under the tree
  const songBlocks = () => el('span', { class: 'fs-lift-songs' },
    ...(model.songs.length
      ? model.songs.map((s) => el('span', { class: `fs-lift-song${s.isFavorite ? ' fs-fav' : ''}` },
        el('b', { text: `#${s.id}` }), ` ${shorten(s.title || '—', 10)}`))
      : [el('span', { class: 'fs-faint', text: '[ ] vacía' })]));

  const variable = (name, type, value) => {
    const val = typeof value === 'string' ? el('span', { class: 'fs-lift-val', text: value }) : value;
    const node = el('div', {
      class: `fs-lift-var fs-cmp-var${selected === name ? ' fs-sel' : ''}`,
      'data-var': name,
      style: `--fs-cmp-color:${colorOf(name)}`,
      role: 'button',
      tabindex: '0',
      'aria-pressed': String(selected === name),
      title: 'Clic para iluminar sus líneas',
      onclick: () => toggleSelected(name),
      onkeydown: (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          toggleSelected(name);
        }
      },
    }, el('span', { class: 'fs-var-type', text: type }), el('span', { class: 'fs-var-name', text: name }), val);
    varEls[name] = node;
    return node;
  };
  const group = (title, vars) => el('div', { class: 'fs-lift-holder fs-cmp-group' },
    el('div', { class: 'fs-lift-holder-head' }, el('span', { text: title })), ...vars);

  const colorOf = (name) => COMPOSE_COLORS[Math.max(0, bindings.findIndex(([n]) => n === name)) % COMPOSE_COLORS.length];

  const toggleSelected = (name) => {
    selected = selected === name ? null : name;
    renderState();
    varEls[name]?.focus();
  };

  const controllers = () => ['title', 'artist', 'imageUrl'].map((key) => variable(`_${key}Controller`, 'TextEditingController', `'${shorten(model.draft[key], 16)}'`));

  const renderState = () => {
    varEls = {};
    const groups = tab === 'flat'
      ? [group('Estado · _PlaylistScreenState', [variable('_songs', 'List<Song>', songBlocks()), ...controllers()])]
      : [
        group('Estado · _PlaylistScreenState', [variable('_songs', 'List<Song>', songBlocks()), variable('_onlyFavorites', 'bool', String(model.onlyFavorites))]),
        group('Estado · _SongFormState', [...controllers(), variable('_showError', 'bool', String(model.showError))]),
      ];
    stateBox.replaceChildren(...groups);
    scheduleLines();
  };

  // ── lines: each variable climbs its own trunk on the right and turns left into
  // every node it is bound to.
  const markers = svgEl('defs');
  const uid = ++treeUid;
  [...COMPOSE_COLORS, COMPOSE_GRAY].forEach((color, i) => {
    const marker = svgEl('marker', {
      id: `fsim-cmp${uid}-${i}`, viewBox: '0 0 10 10', refX: '9', refY: '5',
      markerWidth: '7', markerHeight: '7', orient: 'auto-start-reverse',
    });
    marker.appendChild(svgEl('path', { d: 'M0,0 L10,5 L0,10 L2.4,5 Z', fill: color }));
    markers.appendChild(marker);
  });

  const drawLines = () => {
    lines.replaceChildren(markers);
    const base = panel.getBoundingClientRect();
    const rect = (node) => {
      const r = node.getBoundingClientRect();
      return { l: r.left - base.left, r: r.right - base.left, t: r.top - base.top, b: r.bottom - base.top, cy: (r.top + r.bottom) / 2 - base.top };
    };
    const active = bindings.map((b, i) => [...b, i]).filter(([name, keys]) => varEls[name] && keys.some((k) => nodeEls[k]));
    const arrivals = {};
    const slots = active.map(([, keys]) => Object.fromEntries(keys.map((k) => {
      arrivals[k] = (arrivals[k] || 0) + 1;
      return [k, arrivals[k] - 1];
    })));
    const ordered = active.map((b, j) => [...b, j]).sort((a, b) => (a[0] === selected) - (b[0] === selected));
    ordered.forEach(([name, keys, i, j]) => {
      const on = name === selected;
      const color = on ? COMPOSE_COLORS[i % COMPOSE_COLORS.length] : COMPOSE_GRAY;
      const marker = on ? i % COMPOSE_COLORS.length : COMPOSE_COLORS.length;
      const from = rect(varEls[name]);
      const trunk = base.width - 10 - j * 11;
      keys.filter((k) => nodeEls[k]).forEach((k) => {
        const to = rect(nodeEls[k]);
        const y = to.cy + (slots[j][k] - (arrivals[k] - 1) / 2) * 7;
        lines.appendChild(svgEl('path', {
          class: `fs-cmp-bind${on ? ' fs-on' : ''}`,
          stroke: color,
          d: `M${from.r + 4},${from.cy} H${trunk} V${y} H${to.r + 6}`,
          'marker-end': `url(#fsim-cmp${uid}-${marker})`,
        }));
      });
    });
  };
  let queued = false;
  const frames = new Set();
  const scheduleLines = () => {
    if (queued) return;
    queued = true;
    const id = raf(() => {
      frames.delete(id);
      queued = false;
      drawLines();
    });
    frames.add(id);
  };

  const CAPTIONS = {
    flat: 'Así quedó la sesión 6: un solo State con todas las variables, y un árbol donde todo cuelga de la misma Screen. Agrega canciones y mira cuántas líneas salen del mismo bloque.',
    parts: 'A esto se llega: piezas con nombre. El estado de la Screen solo llega a PlaylistSummary y SongList; el borrador vive dentro de SongForm. Marca favoritas, filtra y quita canciones.',
  };

  const render = () => {
    renderPhone();
    renderTree();
    renderState();
  };

  const flatTab = el('button', { text: 'Sin componentes', class: 'fs-sel' });
  const partsTab = el('button', { text: 'Con componentes' });
  const select = (next) => {
    tab = next;
    flatTab.className = next === 'flat' ? 'fs-sel' : '';
    partsTab.className = next === 'parts' ? 'fs-sel' : '';
    model.showError = false;
    caption.textContent = CAPTIONS[next];
    render();
  };
  flatTab.addEventListener('click', () => select('flat'));
  partsTab.addEventListener('click', () => select('parts'));

  container.append(
    el('div', { class: 'fs-cmp-bar' }, el('div', { class: 'fs-seg', role: 'tablist', 'aria-label': 'Versión' }, flatTab, partsTab)),
    el('div', { class: 'fs-col fs-cmp-tall' }, screen.frame),
    el('div', { class: 'fs-side' }, panel, el('div', { class: 'fs-panel' }, caption))
  );
  select('flat');

  const onResize = () => scheduleLines();
  window.addEventListener('resize', onResize);
  const observer = typeof ResizeObserver === 'function' ? new ResizeObserver(onResize) : null;
  observer?.observe(panel);

  return () => {
    frames.forEach(cancelRaf);
    observer?.disconnect();
    window.removeEventListener('resize', onResize);
    root.replaceChildren();
  };
};

// ────────────────────────────────── callback ──────────────────────────────────

// Where the delete function is born and how it reaches the button. Three levels:
// PlaylistScreen (state + the function), SongList (only hands it down) and SongCard
// (the button). A guided tour builds the path; afterwards each tap on a trash can
// climbs back up, one level per step, until setState removes the song.

const CB_STEPS = [
  {
    name: 'El estado',
    caption: 'Nivel 1: _songs vive en el State de PlaylistScreen. Solo este State puede cambiarla.',
    hot: 'l1',
  },
  {
    name: 'La función',
    caption: 'La función que borra se define aquí, junto al estado: _deleteSong llama a setState y quita la canción de _songs.',
    hot: 'l1',
  },
  {
    name: '¿Y el botón?',
    caption: 'Pero en este nivel no hay ningún botón. La papelera está dentro de cada SongCard, dos niveles más abajo, y todavía no sabe qué hacer.',
    hot: 'l3',
  },
  {
    name: 'Baja a SongList',
    caption: 'La función baja por el constructor: SongList recibe onDelete. No la usa, solo la va a pasar. Es prop drilling.',
    hot: 'l2',
  },
  {
    name: 'Baja a SongCard',
    caption: 'SongList se la entrega a cada SongCard, ya con su canción: onDelete: () => onDelete(song).',
    hot: 'l3',
  },
  {
    name: 'Al botón',
    caption: 'SongCard la conecta al botón: onPressed: () => onDelete(). Listo. Toca la papelera de una canción.',
    hot: 'l3',
  },
];

const CB_CODE = {
  l1: [
    { t: 'final List<Song> _songs = […];', from: 1, key: 'state' },
    { t: '', from: 2 },
    { t: 'void _deleteSong(Song song) {', from: 2, key: 'fn' },
    { t: '  setState(() {', from: 2, key: 'set' },
    { t: '    _songs.remove(song);', from: 2, key: 'remove' },
    { t: '  });', from: 2, key: 'set2' },
    { t: '}', from: 2, key: 'fn2' },
    { t: '', from: 1 },
    { t: 'SongList(songs: _songs),', from: 1, until: 3 },
    { t: 'SongList(', from: 4, key: 'list' },
    { t: '  songs: _songs,', from: 4 },
    { t: '  onDelete: (song) => _deleteSong(song),', from: 4, key: 'pass1' },
    { t: '),', from: 4 },
  ],
  l2: [
    { t: 'final List<Song> songs;', from: 1 },
    { t: 'final Function(Song) onDelete;', from: 4, key: 'field2' },
    { t: '', from: 1 },
    { t: 'for (final song in songs)', from: 1 },
    { t: '  SongCard(song: song),', from: 1, until: 4 },
    { t: '  SongCard(', from: 5, key: 'card' },
    { t: '    song: song,', from: 5 },
    { t: '    onDelete: () => onDelete(song),', from: 5, key: 'pass2' },
    { t: '  ),', from: 5 },
  ],
  l3: [
    { t: 'final Song song;', from: 1 },
    { t: 'final Function() onDelete;', from: 5, key: 'field3' },
    { t: '', from: 1 },
    { t: 'Text(song.title),', from: 1 },
    { t: 'IconButton(onPressed: ¿?),', from: 3, until: 5, key: 'ask' },
    { t: 'IconButton(', from: 6, key: 'btn' },
    { t: '  onPressed: () => onDelete(),', from: 6, key: 'press' },
    { t: '  icon: Icon(Icons.delete_outline),', from: 6 },
    { t: '),', from: 6 },
  ],
};

const CB_LEVELS = [
  { id: 'l1', title: 'Nivel 1 · PlaylistScreen', tag: () => 'aquí vive el estado' },
  { id: 'l2', title: 'Nivel 2 · SongList', tag: (step) => (step >= 4 ? 'solo pasa la función' : 'recibe la lista') },
  { id: 'l3', title: 'Nivel 3 · SongCard', tag: (step) => (step >= 3 ? 'aquí está el botón' : 'muestra una canción') },
];

const CB_SONGS = [
  { title: 'Imagine', artist: 'John Lennon' },
  { title: 'Yellow', artist: 'Coldplay' },
  { title: 'Levitating', artist: 'Dua Lipa' },
];

const mountCallback = (root) => {
  const container = card(root);
  const timers = [];
  let nextId = 1;
  const fresh = () => CB_SONGS.map((s) => ({ ...s, id: nextId++, imageUrl: DEFAULT_IMAGE }));
  let songs = fresh();
  let step = 1;
  let running = false;

  // ── phone
  const screen = phone('Mi playlist');
  const list = el('div', { 'data-testid': 'callback-list' });
  screen.body.append(list);
  const paintPhone = () => {
    list.replaceChildren(...(songs.length
      ? songs.map((song) => {
        const node = songCard(song);
        const trash = el('button', {
          class: `fs-lift-act fs-cb-trash${step === 3 ? ' fs-cb-ask' : ''}`,
          'aria-label': `Quitar ${song.title}`,
          text: '🗑',
          disabled: step < 6 || running,
          onclick: () => remove(song.id),
        });
        node.querySelector('.fs-card-icon').replaceWith(trash);
        return node;
      })
      : [el('div', { class: 'fs-empty', text: 'Todavía no hay canciones' })]));
  };

  // ── the three levels
  const levels = {};
  const chips = el('div', { class: 'fs-lift-songs fs-cb-state' });
  CB_LEVELS.forEach((level) => {
    const tag = el('span', { class: 'fs-cb-tag' });
    const code = codePanel('');
    code.box.querySelector('h4').remove();
    const head = el('div', { class: 'fs-cb-head' }, el('b', { text: level.title }), tag);
    const box = el('div', { class: 'fs-panel fs-cb-level', 'data-level': level.id }, head);
    if (level.id === 'l1') box.append(el('div', { class: 'fs-cb-statebox' }, el('span', { class: 'fs-cb-statelabel', text: 'Estado · _songs' }), chips));
    box.append(code.box);
    levels[level.id] = { box, tag, code, keys: [] };
  });
  const packet = el('div', { class: 'fs-lift-packet', 'aria-hidden': 'true' });
  const levelCol = el('div', { class: 'fs-rel fs-cb-levels' }, ...CB_LEVELS.map((l) => levels[l.id].box), packet);

  const renderChips = () => {
    chips.replaceChildren(...(songs.length
      ? songs.map((s) => el('span', { class: 'fs-lift-song' }, el('b', { text: `#${s.id}` }), ` ${s.title}`))
      : [el('span', { class: 'fs-faint', text: '[ ] vacía' })]));
  };

  const renderCode = (newFrom) => {
    CB_LEVELS.forEach(({ id, tag }) => {
      const lv = levels[id];
      const shown = CB_CODE[id].filter((line) => line.from <= step && (line.until === undefined || step <= line.until));
      lv.keys = shown.map((line) => line.key);
      lv.code.setCode(shown.map((line) => line.t).join('\n'));
      lv.code.mark(...shown.map((line, i) => (line.from === newFrom ? i : -1)).filter((i) => i >= 0));
      lv.tag.textContent = tag(step);
    });
  };
  const markKey = (id, ...keys) => {
    CB_LEVELS.forEach(({ id: other }) => levels[other].code.mark());
    if (id) levels[id].code.mark(...keys.map((k) => levels[id].keys.indexOf(k)).filter((i) => i >= 0));
  };
  const hot = (id) => CB_LEVELS.forEach(({ id: other }) => levels[other].box.classList.toggle('fs-hot', other === id));

  // One packet, one jump, between two levels.
  const send = (from, to, label, kind) => {
    const base = levelCol.getBoundingClientRect();
    packet.textContent = label;
    packet.className = `fs-lift-packet fs-${kind}`;
    const at = (id) => {
      const r = levels[id].box.getBoundingClientRect();
      return { x: r.left - base.left + (r.width - packet.offsetWidth) / 2, y: r.top - base.top - 16 };
    };
    const a = at(from);
    const b = at(to);
    packet.style.transition = 'none';
    packet.style.transform = `translate(${a.x}px, ${a.y}px)`;
    void packet.offsetWidth;
    packet.style.transition = '';
    packet.style.transform = `translate(${b.x}px, ${b.y}px)`;
  };
  const hidePacket = () => {
    packet.className = 'fs-lift-packet';
  };

  // ── guided tour
  const stepBar = el('div', { class: 'fs-stepbar' });
  const caption = el('div', { class: 'fs-caption', 'data-testid': 'callback-caption' });
  const drawBar = (names, current) => {
    stepBar.replaceChildren(...names.map((name, i) => {
      const kind = i === current ? 'fs-cur' : i < current ? 'fs-past' : '';
      return el('span', { class: `fs-sp ${kind}` }, el('b', { text: String(i + 1) }), name);
    }));
  };
  const prevButton = el('button', { class: 'fs-btn', text: 'Anterior' });
  const nextButton = el('button', { class: 'fs-btn fs-solid', text: 'Siguiente' });
  const resetButton = el('button', { class: 'fs-btn', text: 'Reiniciar' });

  const showStep = (next) => {
    step = next;
    const info = CB_STEPS[step - 1];
    renderCode(step);
    hot(info.hot);
    drawBar(CB_STEPS.map((s) => s.name), step - 1);
    caption.textContent = info.caption;
    prevButton.disabled = step === 1;
    nextButton.disabled = step === CB_STEPS.length;
    hidePacket();
    if (step === 4) send('l1', 'l2', 'onDelete', 'up');
    if (step === 5) send('l2', 'l3', 'onDelete', 'up');
    paintPhone();
  };
  prevButton.addEventListener('click', () => !running && step > 1 && showStep(step - 1));
  nextButton.addEventListener('click', () => !running && step < CB_STEPS.length && showStep(step + 1));
  resetButton.addEventListener('click', () => {
    timers.splice(0).forEach(clearTimeout);
    running = false;
    songs = fresh();
    renderChips();
    showStep(1);
  });

  // ── a tap climbs back up, one level per step
  function remove(id) {
    const song = songs.find((s) => s.id === id);
    if (!song || running) return;
    running = true;
    paintPhone();
    const names = ['Toque', 'Sube a SongList', 'Sube a la Screen', 'setState', 'Pantalla'];
    const plan = [
      () => {
        hot('l3');
        markKey('l3', 'press');
        hidePacket();
        caption.textContent = `Tocaste la papelera de ${song.title}: SongCard ejecuta onPressed, que llama onDelete(). SongCard no sabe qué hace esa función.`;
      },
      () => {
        hot('l2');
        markKey('l2', 'pass2');
        send('l3', 'l2', 'onDelete()', 'up');
        caption.textContent = `Esa función se la dio SongList: () => onDelete(song). Le agrega la canción, Song #${id}, y llama la que recibió.`;
      },
      () => {
        hot('l1');
        markKey('l1', 'pass1', 'fn');
        send('l2', 'l1', `onDelete(#${id})`, 'up');
        caption.textContent = 'Y esa la escribió PlaylistScreen: (song) => _deleteSong(song). La llamada llega al nivel donde vive el estado.';
      },
      () => {
        hidePacket();
        markKey('l1', 'set', 'remove', 'set2');
        songs = songs.filter((s) => s.id !== id);
        renderChips();
        flash(chips);
        caption.textContent = `_deleteSong corre en el State: dentro de setState, Song #${id} sale de _songs. Solo este nivel podía hacerlo.`;
      },
      () => {
        hot(null);
        markKey(null);
        paintPhone();
        caption.textContent = 'build() vuelve a correr y la lista baja otra vez, sin esa canción. Toca otra papelera o reinicia.';
      },
    ];
    plan.forEach((fn, i) => timers.push(setTimeout(() => {
      drawBar(names, i);
      fn();
      if (i === plan.length - 1) {
        running = false;
        paintPhone();
      }
    }, i * 1400)));
  }

  container.append(
    el('div', { class: 'fs-col fs-cmp-tall' }, screen.frame,
      el('div', { class: 'fs-controls' }, prevButton, nextButton, resetButton)),
    el('div', { class: 'fs-side' }, el('div', { class: 'fs-panel' }, stepBar, caption), levelCol)
  );
  renderChips();
  showStep(1);

  return () => {
    timers.splice(0).forEach(clearTimeout);
    root.replaceChildren();
  };
};

// ────────────────────────────── state-lifecycle ──────────────────────────────

// The greeting screen on the phone and, next to it, the phases of its State joined by
// arrows. Opening, greeting and going back light the path the State goes through.

const LC_STEP_MS = 1000;
const LC_COLORS = {
  amber: ['#FFF3DC', '#A96C05'],
  green: ['#E8F6E3', '#3A8235'],
  indigo: ['#EEF1FF', '#4453C9'],
  violet: ['#F4EBFF', '#7439B8'],
  rose: ['#FFEBEF', '#C2354F'],
};
const LC_BLOCKS = [
  { key: 'createState', color: 'amber', x: 20, y: 12, w: 210, desc: 'Flutter crea el objeto State' },
  { key: 'initState', color: 'green', x: 20, y: 100, w: 210, desc: 'Prepara lo que necesita' },
  { key: 'build', color: 'indigo', x: 20, y: 188, w: 210, desc: 'Dibuja con los datos actuales' },
  { key: 'setState', color: 'violet', x: 290, y: 188, w: 160, desc: 'Cambia un dato' },
  { key: 'dispose', color: 'rose', x: 20, y: 296, w: 210, desc: 'Libera lo de initState' },
];
const LC_ARROWS = [
  { key: 'open', to: 'initState', d: 'M125,68 V96' },
  { key: 'first', to: 'build', d: 'M125,156 V184' },
  { key: 'event', to: 'setState', d: 'M232,204 H286', label: 'Saludar', lx: 259, ly: 197 },
  { key: 'rebuild', to: 'build', d: 'M288,228 H234', label: 'build()', lx: 261, ly: 244 },
  { key: 'leave', to: 'dispose', d: 'M125,244 V292', label: 'Cerrar', lx: 156, ly: 273 },
];

const mountLifecycle = (root) => {
  const container = card(root);
  const timers = [];
  let queue = [];
  let stateId = 0;
  let text = '';
  let greeting = 'Hola';
  let counts = {};
  let screenName = 'launcher';

  const screen = phone('Saludo');

  const svg = svgEl('svg', { class: 'fs-lc-svg', viewBox: '0 0 462 360', role: 'img', 'aria-label': 'Fases del ciclo de vida' });
  const defs = svgEl('defs');
  svg.appendChild(defs);
  const marker = (id, color) => {
    const m = svgEl('marker', { id, viewBox: '0 0 10 10', refX: '9', refY: '5', markerWidth: '6', markerHeight: '6', orient: 'auto-start-reverse' });
    m.appendChild(svgEl('path', { d: 'M0,0 L10,5 L0,10 L2.4,5 Z', fill: color }));
    defs.appendChild(m);
  };
  const markerBase = `fsim-lc${++treeUid}`;
  marker(`${markerBase}-off`, '#C4CBD8');
  Object.entries(LC_COLORS).forEach(([name, [, strong]]) => marker(`${markerBase}-${name}`, strong));

  const svgText = (attrs, content) => {
    const t = svgEl('text', attrs);
    t.textContent = content;
    return t;
  };

  const arrows = {};
  LC_ARROWS.forEach((a) => {
    const path = svgEl('path', { class: 'fs-lc-arrow', d: a.d, 'marker-end': `url(#${markerBase}-off)` });
    svg.appendChild(path);
    if (a.label) svg.appendChild(svgText({ class: 'fs-lc-label', x: a.lx, y: a.ly, 'text-anchor': 'middle' }, a.label));
    arrows[a.key] = { path, color: LC_BLOCKS.find((b) => b.key === a.to).color };
  });

  const blocks = {};
  LC_BLOCKS.forEach((b) => {
    const [soft, strong] = LC_COLORS[b.color];
    const g = svgEl('g', { class: 'fs-lc-block', 'data-phase': b.key });
    const rect = svgEl('rect', { x: b.x, y: b.y, width: b.w, height: 56, rx: 12 });
    const count = svgText({ class: 'fs-lc-count', x: b.x + b.w - 12, y: b.y + 23, 'text-anchor': 'end', fill: strong }, '');
    g.append(
      rect,
      svgEl('circle', { cx: b.x + 18, cy: b.y + 28, r: 8, fill: soft, stroke: strong, 'stroke-width': 2.5 }),
      svgText({ class: 'fs-lc-name', x: b.x + 34, y: b.y + 24, fill: strong }, b.key),
      svgText({ class: 'fs-lc-desc', x: b.x + 34, y: b.y + 43 }, b.desc),
      count
    );
    svg.appendChild(g);
    blocks[b.key] = { g, rect, count, soft, strong };
  });

  const caption = el('div', { class: 'fs-caption', 'data-testid': 'lc-caption' });
  const flowPanel = el('div', { class: 'fs-panel' }, el('h4', { text: 'Ciclo de vida del State' }), svg, caption);

  const light = (phase, arrow) => {
    Object.entries(blocks).forEach(([key, b]) => {
      const on = key === phase;
      b.rect.style.fill = on ? b.soft : '';
      b.rect.style.stroke = on ? b.strong : '';
      b.rect.style.strokeWidth = on ? '2.5' : '';
      b.g.classList.toggle('fs-seen', Boolean(counts[key]));
      b.count.textContent = counts[key] ? `×${counts[key]}` : '';
    });
    Object.entries(arrows).forEach(([key, a]) => {
      const on = key === arrow;
      a.path.classList.toggle('fs-on', on);
      a.path.style.stroke = on ? LC_COLORS[a.color][1] : '';
      a.path.setAttribute('marker-end', `url(#${markerBase}-${on ? a.color : 'off'})`);
    });
  };

  const appIcon = (name, color, onclick) => el('button', {
    class: `fs-app${onclick ? '' : ' fs-app-off'}`,
    'aria-label': `Abrir ${name}`,
    disabled: !onclick,
    onclick,
  }, el('span', { class: 'fs-app-icon', style: `background:${color}`, text: name[0] }), el('span', { text: name }));

  const drawLauncher = () => {
    screenName = 'launcher';
    screen.appbar.style.display = 'none';
    screen.body.classList.add('fs-launcher');
    screen.body.replaceChildren(el('div', { class: 'fs-apps' },
      appIcon('Saludo', '#6750A4', () => open()),
      appIcon('Fotos', '#C2354F'),
      appIcon('Mapas', '#3A8235'),
      appIcon('Notas', '#A96C05')));
  };

  const drawBlank = () => {
    screenName = 'blank';
    screen.appbar.style.display = '';
    screen.body.classList.remove('fs-launcher');
    screen.body.replaceChildren(
      el('div', { class: 'fs-center' }, el('div', { class: 'fs-faint', text: 'build() todavía no ha corrido: no hay nada que mostrar' })));
  };

  const drawGreeting = () => {
    screenName = 'greeting';
    const field = el('input', { class: 'fs-field', placeholder: 'Escribe tu nombre', 'aria-label': 'Nombre' });
    field.value = text;
    field.addEventListener('input', () => type(field.value));
    field.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') greet();
    });
    screen.body.replaceChildren(
      el('div', { class: 'fs-label', text: 'Nombre' }),
      field,
      el('div', { class: 'fs-hello', 'data-testid': 'lc-greeting', text: greeting }),
      el('div', { class: 'fs-controls' },
        el('button', { class: 'fs-btn fs-solid', text: 'Saludar', onclick: () => greet() }),
        el('button', { class: 'fs-btn', text: 'Cerrar', onclick: () => leave() })));
  };

  const clearTimers = () => timers.splice(0).forEach(clearTimeout);

  const flush = () => {
    clearTimers();
    queue.splice(0).forEach((s) => s.apply?.());
  };

  const play = () => {
    const step = queue.shift();
    if (!step) return;
    step.apply?.();
    light(step.phase, step.arrow);
    caption.textContent = step.caption;
    if (queue.length) timers.push(setTimeout(play, LC_STEP_MS));
  };

  const run = (steps) => {
    flush();
    queue = steps;
    play();
  };

  const bump = (phase) => {
    counts[phase] = (counts[phase] || 0) + 1;
  };

  function open() {
    if (screenName !== 'launcher') return;
    run([
      {
        phase: 'createState',
        caption: `Abriste la app: Flutter crea GreetingScreen y llama a createState(). Nace _GreetingScreenState #${stateId + 1}.`,
        apply: () => {
          stateId += 1;
          counts = {};
          text = '';
          greeting = 'Hola';
          bump('createState');
          drawBlank();
        },
      },
      {
        phase: 'initState',
        arrow: 'open',
        caption: 'initState() corre una sola vez, antes de dibujar nada. Aquí nace _nameController.',
        apply: () => {
          bump('initState');
        },
      },
      {
        phase: 'build',
        arrow: 'first',
        caption: 'build() dibuja la pantalla con los datos actuales: el campo vacío y Hola. Escribe tu nombre y pulsa Saludar.',
        apply: () => {
          bump('build');
          drawGreeting();
        },
      },
    ]);
  }

  function type(value) {
    flush();
    text = value;
    light(null, null);
    caption.textContent = 'Escribir cambia _nameController.text. No es setState: build() no corre y el saludo no cambia.';
  }

  function greet() {
    if (screenName !== 'greeting') return;
    const next = `Hola, ${text}`;
    run([
      {
        phase: 'setState',
        arrow: 'event',
        caption: `Pulsaste Saludar: _greet() cambia _greeting a '${next}' dentro de setState. El State queda sucio; la pantalla todavía no cambia.`,
        apply: () => {
          greeting = next;
          bump('setState');
        },
      },
      {
        phase: 'build',
        arrow: 'rebuild',
        caption: `build() corre otra vez, con el mismo State #${stateId}: el Text muestra '${next}'.`,
        apply: () => {
          bump('build');
          drawGreeting();
        },
      },
    ]);
  }

  function leave() {
    if (screenName === 'launcher') return;
    run([
      {
        phase: 'dispose',
        arrow: 'leave',
        caption: `Cerraste la app: la pantalla sale del árbol y dispose() corre una vez, así que _nameController se libera. El State #${stateId} no vuelve: si abres otra vez, nace uno nuevo.`,
        apply: () => {
          bump('dispose');
          drawLauncher();
        },
      },
    ]);
  }

  drawLauncher();
  light(null, null);
  caption.textContent = 'Toca la app Saludo en el teléfono y mira por qué bloques pasa su State.';
  container.append(
    el('div', { class: 'fs-col' }, screen.frame),
    el('div', { class: 'fs-side' }, flowPanel)
  );

  return () => {
    clearTimers();
    root.replaceChildren();
  };
};

// ─────────────────────────── nav-stack / nav-result ───────────────────────────

// The Navigator's stack next to a phone. A push drops a card on top, a pop takes it
// away, and pushNamedAndRemoveUntil asks every card under the new one whether it stays.

const NAV_STEP_MS = 1100;

const NAV_ROUTES = [
  { name: '/', screen: 'LoginScreen' },
  { name: '/playlist', screen: 'PlaylistScreen' },
  { name: '/song', screen: 'SongDetailScreen' },
  { name: '/add-song', screen: 'AddSongScreen' },
];

const NAV_SONGS = [
  { title: 'Imagine', artist: 'John Lennon' },
  { title: 'Yellow', artist: 'Coldplay' },
  { title: 'Levitating', artist: 'Dua Lipa' },
];

const navScreenOf = (route) => NAV_ROUTES.find((r) => r.name === route).screen;
const navSong = (song) => `Song('${shorten(song.title, 16)}')`;

// Plays a list of steps one after the other, or one per click in step-by-step mode.
const navRunner = ({ stepBar, caption, nextButton, timers, onChange }) => {
  let run = null;
  let stepMode = false;
  const drawBar = (names, current) => {
    stepBar.replaceChildren(...names.map((name, i) => {
      const kind = i === current ? 'fs-cur' : i < current ? 'fs-past' : '';
      return el('span', { class: `fs-sp ${kind}` }, el('b', { text: String(i + 1) }), name);
    }));
  };
  const play = (index) => {
    run.index = index;
    const step = run.steps[index];
    drawBar(run.steps.map((s) => s.name), index);
    caption.textContent = step.caption;
    step.apply?.();
    if (index === run.steps.length - 1) {
      run = null;
      nextButton.disabled = true;
      onChange();
      return;
    }
    if (stepMode) {
      nextButton.disabled = false;
      return;
    }
    timers.push(setTimeout(() => play(index + 1), NAV_STEP_MS));
  };
  nextButton.addEventListener('click', () => {
    if (!run) return;
    nextButton.disabled = true;
    play(run.index + 1);
  });
  return {
    busy: () => Boolean(run),
    start: (steps) => {
      if (run) return;
      run = { steps, index: -1 };
      onChange();
      play(0);
    },
    setStepMode: (on) => {
      stepMode = on;
      if (!on && run && !nextButton.disabled) {
        nextButton.disabled = true;
        play(run.index + 1);
      }
    },
    stop: () => {
      timers.splice(0).forEach(clearTimeout);
      run = null;
      nextButton.disabled = true;
      stepBar.replaceChildren();
    },
  };
};

const navPhone = () => {
  const screenHost = el('div', { class: 'fs-ns-screen', 'data-testid': 'nav-phone' });
  const back = el('button', { class: 'fs-ns-sysback', 'aria-label': 'Atrás del sistema', title: 'Atrás del sistema', text: '◁' });
  const frame = el(
    'div',
    { class: 'fs-phone fs-ns-phone' },
    el('div', { class: 'fs-status' }, el('span', { text: '9:41' }), el('span', { text: '5G' })),
    screenHost,
    el('div', { class: 'fs-ns-navbar' }, back, el('span', { text: '○' }), el('span', { text: '□' }))
  );
  return { frame, screenHost, back };
};

const navAppBar = (title, onBack, ...actions) => el(
  'div',
  { class: 'fs-appbar fs-ns-appbar' },
  onBack ? el('button', { class: 'fs-ns-icon', 'aria-label': 'Atrás', title: 'Atrás', text: '←', onclick: onBack }) : null,
  el('span', { class: 'fs-ns-title', text: title }),
  ...actions
);

const navLogoutIcon = () => {
  const icon = svgEl('svg', { viewBox: '0 0 24 24', 'aria-hidden': 'true' });
  icon.appendChild(svgEl('path', {
    d: 'M10 4H5v16h5M14 8l4 4-4 4M18 12H9',
    fill: 'none',
    stroke: 'currentColor',
    'stroke-width': '2',
    'stroke-linecap': 'round',
    'stroke-linejoin': 'round',
  }));
  return icon;
};

const navTapCard = (song, label, onTap) => {
  const button = el('button', { class: 'fs-ns-songbtn', 'aria-label': label, onclick: onTap });
  button.appendChild(songCard(song));
  return button;
};

const navDetail = (song, onBack) => {
  const cover = el('div', { class: 'fs-cover' });
  const img = el('img', { src: song.imageUrl, alt: '' });
  img.addEventListener('error', () => img.remove());
  cover.appendChild(img);
  return el(
    'div',
    { class: 'fs-body fs-ns-detail' },
    cover,
    el('div', { class: 'fs-hello', text: song.title }),
    el('div', { class: 'fs-card-artist', text: song.artist }),
    el('button', { class: 'fs-ns-btn', text: 'Volver a la lista', onclick: onBack })
  );
};

// Top of the stack first, the base at the bottom.
const navStackPanel = () => {
  const list = el('div', { class: 'fs-ns-stack', 'data-testid': 'nav-stack' });
  const box = el(
    'div',
    { class: 'fs-panel' },
    el('h4', { text: 'Pila del Navigator' }),
    list,
    el('div', { class: 'fs-ns-base', text: 'base de la pila' })
  );
  const TAGS = {
    top: ['visible', ''],
    alive: ['debajo · sigue viva', 'fs-ns-alive'],
    wait: ['esperando en el await', 'fs-dirty'],
    cross: ['(route) => false · sale', 'fs-lost'],
    out: ['dispose()', 'fs-lost'],
  };
  const render = (stack, marks = {}) => {
    if (!stack.length) {
      list.replaceChildren(el('div', { class: 'fs-empty', text: 'Pila vacía: la app se cerró' }));
      return;
    }
    list.replaceChildren(...[...stack].reverse().map((entry, i) => {
      const mark = marks[entry.key];
      const [text, cls] = TAGS[mark === 'new' || !mark ? (i === 0 ? 'top' : 'alive') : mark];
      return el(
        'div',
        { class: `fs-ns-card${i === 0 ? ' fs-ns-top' : ''}${mark ? ` fs-ns-${mark}` : ''}`, 'data-route': entry.route },
        el('span', { class: 'fs-ns-route', text: `'${entry.route}'` }),
        el('span', { class: 'fs-ns-sname', text: entry.label }),
        el('span', { class: `fs-tag ${cls}`, text }),
        entry.arg ? el('span', { class: 'fs-ns-arg', text: `arguments: ${entry.arg}` }) : null
      );
    }));
  };
  return { box, render };
};

const navRoutesPanel = () => {
  const rows = NAV_ROUTES.map((r) => el(
    'div',
    { class: 'fs-row fs-ns-rt', 'data-name': r.name },
    el('span', { text: `'${r.name}'` }),
    el('span', { text: `${r.screen}()` })
  ));
  const box = el('div', { class: 'fs-panel' }, el('h4', { text: 'routes: de MaterialApp' }), ...rows);
  const mark = (name) => rows.forEach((row) => {
    const on = row.dataset.name === name;
    row.classList.toggle('fs-ns-found', on);
    if (on) flash(row);
  });
  return { box, mark };
};

const navControls = (runner, onReset) => {
  const stepToggle = switchControl('Paso a paso', (checked) => runner().setStepMode(checked));
  const nextButton = el('button', { class: 'fs-btn', text: 'Siguiente paso', disabled: true });
  const resetButton = el('button', { class: 'fs-btn', text: 'Reiniciar', onclick: onReset });
  return { nextButton, node: el('div', { class: 'fs-controls' }, stepToggle.node, nextButton, resetButton) };
};

const mountNavStack = (root, args = []) => {
  const resetMode = args.includes('reset');
  const container = card(root);
  const timers = [];
  const songs = NAV_SONGS.map((s) => ({ ...s, imageUrl: DEFAULT_IMAGE }));
  let uid = 1;
  let stack = [];
  let marks = {};

  const entry = (route, song) => ({
    key: uid++,
    route,
    label: song ? `${navScreenOf(route)} · ${song.title}` : navScreenOf(route),
    song,
  });
  const top = () => stack[stack.length - 1];

  const device = navPhone();
  const stackPanel = navStackPanel();
  const routes = navRoutesPanel();
  const code = codePanel('Lo que se ejecutó');
  const stepBar = el('div', { class: 'fs-stepbar' });
  const caption = el('div', { class: 'fs-caption', 'data-testid': 'nav-caption' });
  let runner = null;
  const controls = navControls(() => runner, () => restart());
  runner = navRunner({ stepBar, caption, nextButton: controls.nextButton, timers, onChange: () => paint() });

  const showCode = (text, ...lines) => {
    code.setCode(text);
    code.mark(...(lines.length ? lines : text.split('\n').map((_, i) => i)));
  };

  const PUSH = (route) => `Navigator.pushNamed(context, '${route}')`;
  const POP = 'Navigator.pop(context)';
  const RESET = (route) => `Navigator.pushNamedAndRemoveUntil(\n  context,\n  '${route}',\n  (route) => false,\n)`;

  function push(route, label, song) {
    const below = top().label;
    runner.start([
      {
        name: 'Toque',
        caption: `Tocaste «${label}»: el botón ejecuta pushNamed con el nombre '${route}'.`,
        apply: () => showCode(PUSH(route)),
      },
      {
        name: 'Busca el nombre',
        caption: `El Navigator busca '${route}' en la tabla routes: y encuentra ${navScreenOf(route)}.`,
        apply: () => routes.mark(route),
      },
      {
        name: 'Push',
        caption: `Una ruta nueva cae encima de la pila. ${below} queda debajo: no se destruye y su State sigue vivo.`,
        apply: () => {
          const fresh = entry(route, song);
          stack = [...stack, fresh];
          marks = { [fresh.key]: 'new' };
          paint();
        },
      },
    ]);
  }

  function pop(label) {
    const leaving = top();
    if (stack.length === 1) {
      runner.start([
        {
          name: 'Toque',
          caption: `Tocaste ${label}: eso es un pop, aunque nadie lo haya escrito.`,
          apply: () => showCode(POP),
        },
        {
          name: 'Pila vacía',
          caption: `${leaving.label} era la única ruta. Al sacarla no queda nada que mostrar y la app se cierra.`,
          apply: () => {
            stack = [];
            marks = {};
            paint();
          },
        },
      ]);
      return;
    }
    const below = stack[stack.length - 2].label;
    runner.start([
      {
        name: 'Toque',
        caption: `Tocaste ${label}: se ejecuta Navigator.pop(context).`,
        apply: () => showCode(POP),
      },
      {
        name: 'Pop',
        caption: `La ruta de arriba sale de la pila y su State corre dispose(). ${leaving.label} deja de existir.`,
        apply: () => {
          marks = { [leaving.key]: 'out' };
          paint();
        },
      },
      {
        name: 'La de abajo',
        caption: `Se ve otra vez ${below}, tal como estaba: nunca se destruyó, así que no corre initState de nuevo.`,
        apply: () => {
          stack = stack.slice(0, -1);
          marks = {};
          paint();
        },
      },
    ]);
  }

  function resetTo(route, label) {
    const old = [...stack].reverse();
    const steps = [
      {
        name: 'Toque',
        caption: `Tocaste «${label}»: el botón ejecuta pushNamedAndRemoveUntil hacia '${route}'.`,
        apply: () => showCode(RESET(route)),
      },
      {
        name: 'Busca el nombre',
        caption: `Igual que pushNamed: busca '${route}' en routes: y encuentra ${navScreenOf(route)}.`,
        apply: () => {
          routes.mark(route);
          showCode(RESET(route), 2);
        },
      },
      {
        name: 'Push',
        caption: `Primero empuja ${navScreenOf(route)} encima de todo, como un push normal.`,
        apply: () => {
          const fresh = entry(route);
          stack = [...stack, fresh];
          marks = { [fresh.key]: 'new' };
          paint();
        },
      },
    ];
    old.forEach((item, i) => steps.push({
      name: old.length > 1 ? `¿Se queda? ${i + 1}` : '¿Se queda?',
      caption: `Luego le pregunta al predicado por la ruta de abajo, ${item.label}. (route) => false responde que no, así que sale.`,
      apply: () => {
        stack = stack.filter((s) => marks[s.key] !== 'cross');
        marks = { [item.key]: 'cross' };
        showCode(RESET(route), 3);
        paint();
      },
    }));
    steps.push({
      name: 'Pila nueva',
      caption: `Solo queda ${navScreenOf(route)}. Atrás ya no tiene a dónde volver: con una sola ruta, el AppBar ni siquiera muestra la flecha.`,
      apply: () => {
        stack = stack.filter((s) => marks[s.key] !== 'cross');
        marks = {};
        paint();
      },
    });
    runner.start(steps);
  }

  const busy = () => runner.busy();
  const tap = (fn) => () => {
    if (!busy()) fn();
  };

  const screens = {
    '/': () => [el('div', { class: 'fs-body' }, el(
      'div',
      { class: 'fs-center' },
      el('div', { class: 'fs-ns-logo', text: '♫' }),
      el('div', { class: 'fs-hello', text: 'Mi playlist' }),
      el('button', {
        class: 'fs-ns-btn',
        text: 'Entrar',
        disabled: busy(),
        onclick: tap(() => (resetMode ? resetTo('/playlist', 'Entrar') : push('/playlist', 'Entrar'))),
      })
    ))],
    '/playlist': (canPop) => [
      navAppBar(
        'Mi playlist',
        canPop ? tap(() => pop('la flecha atrás del AppBar')) : null,
        el('button', {
          class: 'fs-ns-icon',
          'aria-label': 'Cerrar sesión',
          title: 'Cerrar sesión',
          onclick: tap(() => (resetMode ? resetTo('/', 'Cerrar sesión') : pop('Cerrar sesión'))),
        }, navLogoutIcon())
      ),
      el(
        'div',
        { class: 'fs-body' },
        ...songs.map((song) => navTapCard(song, `Abrir ${song.title}`, tap(() => push('/song', song.title, song)))),
        el('button', { class: 'fs-fab', 'aria-label': 'Agregar canción', text: '+', onclick: tap(() => push('/add-song', '+')) })
      ),
    ],
    '/song': (canPop, item) => [
      navAppBar(item.song.title, canPop ? tap(() => pop('la flecha atrás del AppBar')) : null),
      navDetail(item.song, tap(() => pop('Volver a la lista'))),
    ],
    '/add-song': (canPop) => [
      navAppBar('Nueva canción', canPop ? tap(() => pop('la flecha atrás del AppBar')) : null),
      el(
        'div',
        { class: 'fs-body' },
        ...['Canción', 'Artista', 'URL de la imagen'].map((label) => el('input', { class: 'fs-field', placeholder: label, 'aria-label': label, disabled: true })),
        el('button', { class: 'fs-filled', text: 'Agregar', onclick: tap(() => pop('Agregar')) }),
        el('div', { class: 'fs-faint', text: 'Por ahora Agregar solo cierra. Devolver la canción es otra lección.' })
      ),
    ],
  };

  const paint = () => {
    const current = top();
    if (current) {
      device.screenHost.className = 'fs-ns-screen';
      device.screenHost.replaceChildren(...screens[current.route](stack.length > 1, current));
    } else {
      device.screenHost.className = 'fs-ns-screen fs-ns-closed';
      device.screenHost.replaceChildren(el(
        'div',
        { class: 'fs-center' },
        el('div', { text: 'La app se cerró' }),
        el('button', { class: 'fs-ns-btn', text: 'Abrir la app', disabled: busy(), onclick: tap(() => open()) })
      ));
    }
    device.back.disabled = !current || busy();
    stackPanel.render(stack, marks);
  };

  function open() {
    stack = [entry('/')];
    marks = {};
    showCode("initialRoute: '/',");
    routes.mark('/');
    caption.textContent = 'La app arranca con una sola ruta en la pila: la de initialRoute, que en la tabla es LoginScreen.';
    paint();
  }

  function restart() {
    runner.stop();
    open();
    caption.textContent = resetMode
      ? 'Entra y luego cierra sesión: mira qué pasa con la pila. Después prueba el botón atrás del sistema.'
      : 'Toca Entrar, abre una canción y vuelve. A la derecha está la pila: la pantalla visible es siempre la de arriba.';
  }

  device.back.addEventListener('click', tap(() => top() && pop('el botón atrás del sistema')));

  container.append(
    el('div', { class: 'fs-col' }, device.frame, controls.node),
    el(
      'div',
      { class: 'fs-side' },
      el('div', { class: 'fs-panel' }, stepBar, caption),
      stackPanel.box,
      el('div', { class: 'fs-row2' }, code.box, routes.box)
    )
  );
  restart();

  return () => {
    timers.splice(0).forEach(clearTimeout);
    root.replaceChildren();
  };
};

const NR_CODE = {
  result: {
    caller: [
      'Future<void> _openAddSong() async {',
      '  final result = await Navigator.pushNamed(',
      '    context,',
      "    '/add-song',",
      '  );',
      '  if (result is Song) {',
      '    _addSong(result);',
      '  }',
      '}',
    ],
    callee: [
      'SongForm(',
      '  onAdd: (song) => Navigator.pop(context, song),',
      '),',
    ],
  },
  args: {
    caller: [
      'void _openSong(Song song) {',
      '  Navigator.pushNamed(',
      '    context,',
      "    '/song',",
      '    arguments: song,',
      '  );',
      '}',
    ],
    callee: [
      'Widget build(BuildContext context) {',
      '  final song = ModalRoute.of(context)!',
      '      .settings.arguments as Song;',
      '  return Scaffold(',
      '    appBar: AppBar(title: Text(song.title)),',
      '  );',
      '}',
    ],
  },
};

const mountNavResult = (root, args = []) => {
  const mode = args.includes('args') ? 'args' : 'result';
  const container = card(root);
  const timers = [];
  let uid = 1;
  let songs = [];
  let stack = [];
  let marks = {};
  let waiting = false;
  let forget = false;
  let failed = false;
  let built = false;
  let draft = { title: '', artist: '' };
  let showError = false;

  const entry = (route, song, arg) => ({ key: uid++, route, label: navScreenOf(route), song, arg });
  const top = () => stack[stack.length - 1];

  const device = navPhone();
  const stackPanel = navStackPanel();
  const vars = statePanel('Variables');
  const stepBar = el('div', { class: 'fs-stepbar' });
  const caption = el('div', { class: 'fs-caption', 'data-testid': 'nav-caption' });
  let runner = null;
  const controls = navControls(() => runner, () => restart());
  runner = navRunner({ stepBar, caption, nextButton: controls.nextButton, timers, onChange: () => paint() });

  // ── the two pieces of code, with the packet that travels between them
  const level = (title, tag) => {
    const tagNode = el('span', { class: 'fs-cb-tag', text: tag });
    const wait = el('span', { class: 'fs-nr-wait', text: '⏳ en pausa en el await' });
    const code = codePanel('');
    code.box.querySelector('h4').remove();
    const box = el('div', { class: 'fs-panel fs-cb-level' }, el('div', { class: 'fs-cb-head' }, el('b', { text: title }), tagNode, wait), code.box);
    return { box, code, wait };
  };
  const caller = level('PlaylistScreen', mode === 'args' ? 'envía la canción' : 'abre y espera');
  const callee = mode === 'args' ? level('SongDetailScreen', 'la recibe') : level('AddSongScreen', 'devuelve la canción');
  callee.wait.remove();
  const packet = el('div', { class: 'fs-lift-packet', 'aria-hidden': 'true' });
  const levelCol = el('div', { class: 'fs-rel fs-cb-levels' }, caller.box, callee.box, packet);

  const callerCode = () => NR_CODE[mode].caller.filter((line) => !(forget && line.includes('arguments')));
  const setCode = () => {
    caller.code.setCode(callerCode().join('\n'));
    callee.code.setCode(NR_CODE[mode].callee.join('\n'));
  };
  const markCode = (side, ...find) => {
    caller.code.mark();
    callee.code.mark();
    if (!side) return;
    const lines = side === caller ? callerCode() : NR_CODE[mode].callee;
    const hit = (line, f) => (f.startsWith('=') ? line.trim() === f.slice(1) : line.includes(f));
    side.code.mark(...lines.map((line, i) => (find.some((f) => hit(line, f)) ? i : -1)).filter((i) => i >= 0));
    caller.box.classList.toggle('fs-hot', side === caller);
    callee.box.classList.toggle('fs-hot', side === callee);
  };
  const send = (from, to, label, kind) => {
    const base = levelCol.getBoundingClientRect();
    packet.textContent = label;
    packet.className = `fs-lift-packet fs-${kind}`;
    const at = (lv) => {
      const r = lv.box.getBoundingClientRect();
      return { x: r.left - base.left + (r.width - packet.offsetWidth) / 2, y: r.top - base.top - 16 };
    };
    const a = at(from);
    const b = at(to);
    packet.style.transition = 'none';
    packet.style.transform = `translate(${a.x}px, ${a.y}px)`;
    void packet.offsetWidth;
    packet.style.transition = '';
    packet.style.transform = `translate(${b.x}px, ${b.y}px)`;
  };
  const hidePacket = () => {
    packet.className = 'fs-lift-packet';
  };

  const showVars = (entries) => vars.set(entries);

  // ── what the user does
  function openAdd() {
    runner.start([
      {
        name: 'Toque',
        caption: 'Tocaste +: corre _openAddSong().',
        apply: () => {
          hidePacket();
          markCode(caller, '_openAddSong');
        },
      },
      {
        name: 'Push y await',
        caption: 'pushNamed abre AddSongScreen y devuelve un Future. El await deja a _openAddSong en pausa en esta línea: lo que sigue no corre hasta que esa pantalla se cierre.',
        apply: () => {
          markCode(caller, 'await', 'context,', "'/add-song'", '=);');
          const fresh = entry('/add-song');
          stack = [...stack, fresh];
          marks = { [stack[0].key]: 'wait', [fresh.key]: 'new' };
          waiting = true;
          draft = { title: '', artist: '' };
          showError = false;
          showVars([['result', '… esperando']]);
          paint();
        },
      },
    ]);
  }

  function closeAdd(song) {
    const value = song ? navSong(song) : 'null';
    const leaving = top();
    runner.start([
      song
        ? {
          name: 'onAdd',
          caption: 'SongForm arma la Song y llama onAdd. AddSongScreen la usa para cerrarse: Navigator.pop(context, song).',
          apply: () => markCode(callee, 'Navigator.pop'),
        }
        : {
          name: 'Atrás',
          caption: 'Atrás también hace pop, pero sin resultado: es Navigator.pop(context), sin segundo argumento.',
          apply: () => markCode(null),
        },
      {
        name: 'Pop',
        caption: `pop saca AddSongScreen de la pila y entrega ${value} como resultado del Future.`,
        apply: () => {
          send(callee, caller, value, 'up');
          marks = { ...marks, [leaving.key]: 'out' };
          paint();
        },
      },
      {
        name: 'Despierta el await',
        caption: `El await termina y result vale ${value}. _openAddSong sigue desde la línea donde se quedó.`,
        apply: () => {
          hidePacket();
          stack = stack.slice(0, -1);
          marks = {};
          waiting = false;
          showVars([['result', value]]);
          markCode(caller, 'await');
          paint();
        },
      },
      song
        ? {
          name: 'if',
          caption: 'result is Song es true: llegó una canción.',
          apply: () => markCode(caller, 'if (result is Song)'),
        }
        : {
          name: 'if',
          caption: 'result is Song es false: la persona volvió sin guardar y no llegó nada. El if evita agregar algo que no existe, y la lista queda igual.',
          apply: () => markCode(caller, 'if (result is Song)'),
        },
      ...(song
        ? [{
          name: 'setState',
          caption: '_addSong la agrega dentro de setState y la lista se dibuja con la canción nueva.',
          apply: () => {
            markCode(caller, '_addSong(result)');
            songs = [...songs, song];
            paint();
          },
        }]
        : []),
    ]);
  }

  function openSong(song) {
    const value = forget ? 'null' : navSong(song);
    runner.start([
      {
        name: 'Toque',
        caption: `Tocaste ${song.title}: SongList avisa con onOpen y la Screen corre _openSong(song).`,
        apply: () => {
          failed = false;
          hidePacket();
          markCode(caller, '_openSong');
        },
      },
      {
        name: 'Empaca',
        caption: forget
          ? 'pushNamed abre /song, pero nadie le dio arguments: la ruta viaja vacía.'
          : 'pushNamed lleva la canción en arguments. Viaja dentro de la ruta nueva, en settings.arguments.',
        apply: () => {
          markCode(caller, 'pushNamed', 'context,', "'/song'", 'arguments', '=);');
          send(caller, callee, value, 'down');
        },
      },
      {
        name: 'Push',
        caption: `SongDetailScreen cae encima de la pila con sus arguments: ${value}.`,
        apply: () => {
          const fresh = entry('/song', song, value);
          built = false;
          stack = [...stack, fresh];
          marks = { [fresh.key]: 'new' };
          paint();
        },
      },
      {
        name: 'Lee arguments',
        caption: forget
          ? 'build lee settings.arguments y encuentra null. El as Song falla: null no es una Song.'
          : 'build lee settings.arguments con ModalRoute.of(context) y lo convierte en Song con as Song.',
        apply: () => {
          hidePacket();
          markCode(callee, 'ModalRoute', '.settings');
          showVars([['settings.arguments', value], ['song', forget ? '✕ error' : value]]);
        },
      },
      {
        name: 'build',
        caption: forget
          ? 'Flutter pinta la pantalla roja del error. Vuelve con atrás y apaga «Olvidar arguments».'
          : `Con la canción en la mano, build dibuja ${song.title}. La pantalla no sabía cuál era hasta este momento.`,
        apply: () => {
          markCode(callee, forget ? '.settings' : 'song.title');
          failed = forget;
          built = true;
          paint();
        },
      },
    ]);
  }

  function closeSong(label) {
    const leaving = top();
    runner.start([
      {
        name: 'Toque',
        caption: `Tocaste ${label}: Navigator.pop(context). Aquí no hace falta devolver nada.`,
        apply: () => {
          hidePacket();
          markCode(null);
        },
      },
      {
        name: 'Pop',
        caption: 'SongDetailScreen sale de la pila y se ve la lista otra vez. Toca otra canción: cada push lleva la suya.',
        apply: () => {
          stack = stack.filter((s) => s.key !== leaving.key);
          marks = {};
          failed = false;
          showVars([]);
          paint();
        },
      },
    ]);
  }

  const busy = () => runner.busy();
  const tap = (fn) => () => {
    if (!busy()) fn();
  };

  function submit() {
    if (!draft.title || !draft.artist) {
      showError = true;
      paint();
      return;
    }
    closeAdd({ ...draft, imageUrl: DEFAULT_IMAGE });
  }

  const back = () => {
    const current = top();
    if (!current || stack.length === 1) return;
    if (current.route === '/add-song') closeAdd(null);
    else closeSong('atrás');
  };

  const playlistScreen = () => [
    navAppBar('Mi playlist', null),
    el(
      'div',
      { class: 'fs-body', 'data-testid': 'nav-list' },
      ...(songs.length
        ? songs.map((song) => (mode === 'args'
          ? navTapCard(song, `Abrir ${song.title}`, tap(() => openSong(song)))
          : songCard(song)))
        : [el('div', { class: 'fs-empty', text: 'Todavía no hay canciones' })]),
      mode === 'result' ? el('button', { class: 'fs-fab', 'aria-label': 'Agregar canción', text: '+', onclick: tap(() => openAdd()) }) : null
    ),
  ];

  const addScreen = () => {
    const field = (key, label) => el('input', {
      class: 'fs-field',
      placeholder: label,
      'aria-label': label,
      value: draft[key],
      oninput: (e) => {
        draft = { ...draft, [key]: e.target.value };
      },
    });
    return [
      navAppBar('Nueva canción', tap(back)),
      el(
        'div',
        { class: 'fs-body' },
        field('title', 'Canción'),
        field('artist', 'Artista'),
        showError ? el('div', { class: 'fs-lift-error', text: 'Escribe el nombre y el artista' }) : null,
        el('button', { class: 'fs-filled', text: 'Agregar', onclick: tap(submit) })
      ),
    ];
  };

  const detailScreen = (item) => {
    if (failed) {
      return [el(
        'div',
        { class: 'fs-ns-err' },
        el('b', { text: 'Exception caught by widgets library' }),
        el('div', { text: "type 'Null' is not a subtype of type 'Song' in type cast" })
      )];
    }
    if (!built) {
      return [navAppBar('', tap(back)), el('div', { class: 'fs-body' })];
    }
    return [navAppBar(item.song.title, tap(back)), navDetail(item.song, tap(() => closeSong('Volver a la lista')))];
  };

  const paint = () => {
    const current = top();
    device.screenHost.className = 'fs-ns-screen';
    const view = current.route === '/playlist' ? playlistScreen()
      : current.route === '/add-song' ? addScreen() : detailScreen(current);
    device.screenHost.replaceChildren(...view);
    device.back.disabled = stack.length < 2 || busy();
    caller.wait.style.display = waiting ? '' : 'none';
    stackPanel.render(stack, marks);
  };

  function restart() {
    runner.stop();
    songs = NAV_SONGS.slice(0, 2).map((s) => ({ ...s, imageUrl: DEFAULT_IMAGE }));
    stack = [entry('/playlist')];
    marks = {};
    waiting = false;
    failed = false;
    showError = false;
    hidePacket();
    setCode();
    markCode(null);
    caller.box.classList.remove('fs-hot');
    callee.box.classList.remove('fs-hot');
    showVars(mode === 'result' ? [['result', '—']] : []);
    caption.textContent = mode === 'result'
      ? 'Toca + para agregar una canción. Prueba también volver con atrás sin guardar.'
      : 'Toca una canción para abrir su detalle. La pantalla nueva no sabe cuál es: hay que mandársela.';
    paint();
  }

  device.back.addEventListener('click', tap(back));

  const sideControls = [];
  if (mode === 'args') {
    const forgetToggle = switchControl('Olvidar arguments', (checked) => {
      forget = checked;
      restart();
    });
    sideControls.push(forgetToggle.node);
  }

  container.append(
    el('div', { class: 'fs-col' }, device.frame, controls.node, ...sideControls),
    el(
      'div',
      { class: 'fs-side' },
      el('div', { class: 'fs-panel' }, stepBar, caption),
      levelCol,
      el('div', { class: 'fs-row2' }, stackPanel.box, vars.box)
    )
  );
  restart();

  return () => {
    timers.splice(0).forEach(clearTimeout);
    root.replaceChildren();
  };
};

export const SIMS = Object.freeze({
  'state-counter': mountCounter,
  'hot-reload': (root, args = []) => mountCounter(root, ['reload', ...args]),
  'state-tree': mountTree,
  'state-lifecycle': mountLifecycle,
  playlist: (root, args = []) => mountTree(root, ['playlist', ...args]),
  lift: mountLift,
  compose: mountCompose,
  callback: mountCallback,
  'nav-stack': mountNavStack,
  'nav-result': mountNavResult,
});

export const parseSpec = (spec) => {
  const [name = '', ...args] = String(spec || '').trim().split(/\s+/);
  return { name, args };
};
