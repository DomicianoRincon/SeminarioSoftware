import { createContext } from "react";

// La llave con la que TaskCheckbox guarda la marca: el texto del item de tarea
// que lo contiene. ListItem la provee; fuera de una lista de tareas es null.
export const TaskItemContext = createContext(null);

// Texto plano de un nodo hast, para usarlo como llave del item.
export const hastText = (node) => {
  if (!node) return "";
  if (node.type === "text") return node.value;
  return (node.children || []).map(hastText).join("");
};
