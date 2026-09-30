// ¿La app se está mostrando dentro de un iframe (por ejemplo, incrustada en la
// plataforma de la universidad)? Así el tema puede adaptarse a la página anfitriona.
//
// Comparar window.self con window.top funciona aunque el anfitrión sea de otro
// origen: comparar referencias está permitido, leer propiedades de window.top no.
// Si el navegador bloquea incluso eso, se asume que sí está incrustada.
export function isEmbedded() {
  try {
    return window.self !== window.top;
  } catch {
    return true;
  }
}
