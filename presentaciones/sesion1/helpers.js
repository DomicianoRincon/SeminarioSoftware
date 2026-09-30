// Íconos propios del deck "Frontend Sesión 1". Estilo de la plantilla: 36x36, círculo de
// color institucional y trazo blanco. Los de sufijo "W" son blancos y sin círculo, para los
// paneles laterales de color. Nunca emoji.
Object.assign(window.H.ICONS, {
  screen: '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="16" fill="#865CF0"/><rect x="12" y="9" width="12" height="19" rx="2.5" stroke="white" stroke-width="1.7"/><line x1="15.5" y1="24.5" x2="20.5" y2="24.5" stroke="white" stroke-width="1.7" stroke-linecap="round"/></svg>',
  map: '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="16" fill="#5454E9"/><rect x="10" y="10" width="7" height="7" rx="1.5" stroke="white" stroke-width="1.6"/><rect x="19" y="10" width="7" height="7" rx="1.5" stroke="white" stroke-width="1.6"/><rect x="10" y="19" width="7" height="7" rx="1.5" stroke="white" stroke-width="1.6"/><rect x="19" y="19" width="7" height="7" rx="1.5" fill="white"/></svg>',
  cloud: '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="16" fill="#4CB979"/><path d="M11 22 Q11 18 15 18 Q15.5 13.5 20 13.5 Q24.5 13.5 25 17.5 Q29 17.8 29 22 Q29 24.5 26 24.5 H13.5 Q11 24.5 11 22Z" stroke="white" stroke-width="1.6"/></svg>',
  ai: '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="16" fill="#865CF0"/><path d="M18 9 L20.2 15.8 L27 18 L20.2 20.2 L18 27 L15.8 20.2 L9 18 L15.8 15.8 Z" fill="white"/></svg>',
  install: '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="16" fill="#E9683B"/><line x1="18" y1="10" x2="18" y2="21" stroke="white" stroke-width="1.9" stroke-linecap="round"/><polyline points="14,17.5 18,21.5 22,17.5" stroke="white" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/><line x1="11.5" y1="25.5" x2="24.5" y2="25.5" stroke="white" stroke-width="1.9" stroke-linecap="round"/></svg>',
  file: '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="16" fill="#393939"/><path d="M13 9 H21 L25 13 V27 H13 Z" stroke="white" stroke-width="1.6" stroke-linejoin="round"/><path d="M21 9 V13 H25" stroke="white" stroke-width="1.6" stroke-linejoin="round"/></svg>',
  edit: '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="16" fill="#5454E9"/><path d="M11 25 L12.5 20 L22 10.5 L25.5 14 L16 23.5 Z" stroke="white" stroke-width="1.6" stroke-linejoin="round"/><line x1="19.5" y1="13" x2="23" y2="16.5" stroke="white" stroke-width="1.6"/></svg>',
  save: '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="16" fill="#4CB979"/><path d="M11 11 H22 L25 14 V25 H11 Z" stroke="white" stroke-width="1.6" stroke-linejoin="round"/><rect x="14" y="11" width="7" height="5" stroke="white" stroke-width="1.4"/><rect x="14" y="19" width="8" height="6" stroke="white" stroke-width="1.4"/></svg>',
  key: '<svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="18" r="16" fill="#E9683B"/><rect x="11" y="12" width="14" height="12" rx="2.5" stroke="white" stroke-width="1.7"/><text x="18" y="21.5" text-anchor="middle" fill="white" font-size="10" font-weight="700" font-family="ui-monospace, Menlo, monospace">r</text></svg>',

  androidW: '<svg width="28" height="28" viewBox="0 0 28 28" fill="none"><rect x="8" y="3" width="12" height="22" rx="2.5" stroke="white" stroke-width="1.8"/><line x1="12" y1="21" x2="16" y2="21" stroke="white" stroke-width="1.8" stroke-linecap="round"/></svg>',
  iosW: '<svg width="28" height="28" viewBox="0 0 28 28" fill="none"><rect x="8" y="3" width="12" height="22" rx="3.5" stroke="white" stroke-width="1.8"/><rect x="12" y="5.5" width="4" height="1.6" rx="0.8" fill="white"/></svg>',
  webW: '<svg width="28" height="28" viewBox="0 0 28 28" fill="none"><rect x="3" y="5" width="22" height="18" rx="2.5" stroke="white" stroke-width="1.8"/><line x1="3" y1="10" x2="25" y2="10" stroke="white" stroke-width="1.6"/><circle cx="6.5" cy="7.5" r="0.9" fill="white"/><circle cx="9.5" cy="7.5" r="0.9" fill="white"/></svg>',
  deskW: '<svg width="28" height="28" viewBox="0 0 28 28" fill="none"><rect x="3" y="4" width="22" height="15" rx="2" stroke="white" stroke-width="1.8"/><path d="M11 19 L10 24 H18 L17 19" stroke="white" stroke-width="1.8" stroke-linejoin="round"/></svg>',
  checkW: '<svg width="28" height="28" viewBox="0 0 28 28" fill="none"><circle cx="14" cy="14" r="11" stroke="white" stroke-width="1.8"/><polyline points="9,14.5 12.5,18 19,10.5" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  phoneW: '<svg width="28" height="28" viewBox="0 0 28 28" fill="none"><rect x="8" y="3" width="12" height="22" rx="2.5" stroke="white" stroke-width="1.8"/><polyline points="11,14 13.5,16.5 17.5,11.5" stroke="white" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  bookW: '<svg width="28" height="28" viewBox="0 0 28 28" fill="none"><path d="M4 6 Q9 4 14 7 Q19 4 24 6 V22 Q19 20 14 23 Q9 20 4 22 Z" stroke="white" stroke-width="1.8" stroke-linejoin="round"/><line x1="14" y1="7" x2="14" y2="23" stroke="white" stroke-width="1.6"/></svg>'
});

// Flujo de pasos en tamaño de proyección (H.pipeline queda chico con pocas palabras por slide).
// nodes: [{icon, label, sub}, ...]
window.H.bigPipeline = function (nodes) {
  var arrow = '<svg width="40" height="24" viewBox="0 0 40 24"><line x1="2" y1="12" x2="32" y2="12" stroke="#5454E9" stroke-width="2.5"/>' +
    '<polyline points="26,5 35,12 26,19" stroke="#5454E9" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  var parts = [];
  nodes.forEach(function (n, i) {
    parts.push('<div style="display:flex;flex-direction:column;align-items:center;gap:10px;width:190px;text-align:center;">' +
      '<div style="width:88px;height:88px;">' + window.H.resize(n.icon, 88) + '</div>' +
      '<div style="font-size:21px;font-weight:700;color:#393939;line-height:26px;">' + n.label + '</div>' +
      '<div style="font-size:16px;color:#88898C;line-height:21px;">' + n.sub + '</div></div>');
    if (i < nodes.length - 1) parts.push('<div style="padding-top:32px;">' + arrow + '</div>');
  });
  return '<div style="display:flex;align-items:flex-start;justify-content:center;gap:4px;">' + parts.join('') + '</div>';
};

// Figura de lección + explicación a la derecha, para las slides de consola.
// items: [[número, título, texto], ...]
window.H.consoleSlide = function (svg, items) {
  var rows = items.map(function (it) {
    return '<div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:18px;">' +
      '<span style="flex-shrink:0;width:28px;height:28px;border-radius:50%;background:#F2C069;color:#1F2430;' +
      'font-weight:800;font-size:15px;display:flex;align-items:center;justify-content:center;">' + it[0] + '</span>' +
      '<div><div style="font-size:18px;font-weight:700;color:#393939;line-height:24px;">' + it[1] + '</div>' +
      '<div style="font-size:16px;color:#393939;line-height:22px;margin-top:2px;">' + it[2] + '</div></div></div>';
  }).join('');
  return '<div style="display:flex;gap:28px;align-items:center;">' +
    '<div style="flex-shrink:0;">' + svg + '</div>' +
    '<div style="flex:1;">' + rows + '</div></div>';
};
