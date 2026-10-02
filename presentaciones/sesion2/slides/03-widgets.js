// Bloque 2 · Widgets básicos (slides 9 a 18). Fuente: lecciones S0011 a S0014.
(function () {
  'use strict';
  var H = window.H, icesi = window.icesi, FIG = window.FIG;

  // 9 · Divisor
  window.SLIDES.push(icesi.sectionSlideEBlue(
    'Widgets básicos<br><small style="font-size:0.5em;">Text, Image, Button y TextField.</small>'
  ));

  // 10 · Text y su estilo
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Text y su estilo', FIG.txAnatomia),
    'Text muestra una cadena: lo único obligatorio es la cadena. No tiene una propiedad color ni fontSize: todo el aspecto se agrupa en un TextStyle que se entrega en style. ' +
    'Solo se escriben las propiedades que se quieren cambiar; las demás conservan el valor del tema. ' +
    'fontSize se mide en píxeles lógicos: un 16 se lee igual de grande en un celular y en un monitor.'));

  // 11 · Cuando el texto no cabe
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Cuando el texto no cabe', FIG.txLargo),
    'Un Text ocupa todos los renglones que necesite, y en una tarjeta eso descuadra el diseño. ' +
    'maxLines es el máximo de renglones y overflow dice qué hacer con lo que sobra: TextOverflow.ellipsis pone los tres puntos. ' +
    'Las dos propiedades van en el Text, no en el TextStyle. textAlign alinea el texto cuando ocupa varios renglones.'));

  // 12 · Image.network
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Una imagen desde internet', FIG.imNetwork),
    'Lo primero es decidir de dónde sale la imagen. Image.network recibe la dirección y la descarga: tiene que apuntar al archivo, no a la página donde aparece. ' +
    'width y height casi siempre: sin ellos la imagen sale a su tamaño real y, mientras descarga, todo lo que está debajo salta. ' +
    'Sirve para lo que cambia y no se conoce de antemano: la foto de un perfil, la portada de un producto.'));

  // 13 · Image.asset
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Una imagen que viaja con la app', FIG.imAsset),
    'Lo que es parte del diseño, como el logo, se guarda en el proyecto. Tres pasos: crear la carpeta assets al lado de lib, declararla en pubspec.yaml y usarla con la ruta completa. ' +
    'Si falla, la consola dice Unable to load asset. Casi siempre es la sangría de pubspec.yaml (assets con dos espacios y la carpeta con cuatro), ' +
    'el nombre que no coincide en mayúsculas, o que la app sigue corriendo con la configuración vieja: el hot reload no carga assets nuevos.'));

  // 14 · fit
  window.SLIDES.push(H.withNotes(icesi.slideStandard('fit: cuando la forma no coincide', FIG.imFit),
    'Una foto rara vez tiene la proporción del espacio donde va. cover llena y recorta: fotos, portadas y fondos; es el más usado. ' +
    'contain muestra la imagen entera y deja espacio vacío: logos. fill estira y deforma: casi nunca. ' +
    'fit solo tiene efecto cuando la imagen tiene width y height.'));

  // 15 · Button
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Button: onPressed y child', FIG.btAnatomia),
    'Todos los botones se arman con las mismas dos piezas. child es lo que muestra, casi siempre un Text. onPressed es lo que hace y recibe una función: ' +
    'el código entre llaves no se ejecuta al dibujar la pantalla sino cada vez que alguien toca el botón. ' +
    'El print escribe en la consola, no en la pantalla. Que un toque cambie la pantalla exige estado, y eso es la sesión 6. ' +
    'Un botón se deshabilita entregándole null en onPressed: si sale gris sin haberlo pedido, revisar ahí.'));

  // 16 · Los cuatro botones
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Los cuatro botones', FIG.btTipos),
    'Se escriben igual. Lo que cambia es cuánto resaltan, y eso le dice a la persona cuál es la acción importante. ' +
    'IconButton es el único distinto: no tiene child sino icon. Los iconos salen de la clase Icons; el autocompletado los muestra al escribir Icons y un punto. ' +
    'Regla de diseño: un solo ElevatedButton por pantalla, para la acción principal. Si todo resalta, nada resalta.'));

  // 17 · TextField
  window.SLIDES.push(H.withNotes(icesi.slideStandard('TextField e InputDecoration', FIG.tfAnatomia),
    'Hoy el campo solo se dibuja; leer lo que la persona escribió necesita estado y es la sesión 6. ' +
    'Igual que Text agrupa su aspecto en TextStyle, TextField lo agrupa en InputDecoration. ' +
    'labelText dice qué es el campo y siempre queda visible; hintText es un ejemplo y se va en cuanto hay texto. Se confunden mucho. ' +
    'Si aparece No Material widget found, el campo quedó fuera de un Scaffold.'));

  // 18 · Contraseña y teclado
  window.SLIDES.push(H.withNotes(icesi.slideStandard('Contraseña y teclado', FIG.tfTipos),
    'Estas dos propiedades van en el TextField, no en la decoración: no cambian cómo se ve el campo sino cómo se escribe en él. ' +
    'obscureText reemplaza cada letra por un punto. keyboardType elige el teclado que abre el celular. ' +
    'keyboardType solo se nota en un celular o en un emulador: en Chrome no se ve diferencia.'));
})();
