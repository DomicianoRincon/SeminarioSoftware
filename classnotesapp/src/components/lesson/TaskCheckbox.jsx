import React, { useContext, useState } from "react";
import { TaskItemContext } from "./taskItem";

// Lo que el estudiante marca en una lista de tareas (`- [ ] ...`) se guarda en
// localStorage, una entrada por lección: `taskChecks:<lessonId>` → { texto: bool }.
// La llave de cada item es su texto, no su posición, para que insertar una meta
// nueva en la lección no le corra las marcas a las de abajo.
const STORAGE_PREFIX = "taskChecks:";

const readChecks = (lessonId) => {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_PREFIX + lessonId) || "{}");
  } catch {
    return {};
  }
};

const writeCheck = (lessonId, itemKey, checked) => {
  const checks = readChecks(lessonId);
  checks[itemKey] = checked;
  try {
    localStorage.setItem(STORAGE_PREFIX + lessonId, JSON.stringify(checks));
  } catch {
    // Sin localStorage (modo privado lleno, por ejemplo) la marca dura lo que la página.
  }
};

const TaskCheckbox = ({ lessonId, defaultChecked }) => {
  const itemKey = useContext(TaskItemContext);
  const persist = Boolean(lessonId && itemKey);
  const [checked, setChecked] = useState(() => {
    if (!persist) return Boolean(defaultChecked);
    const stored = readChecks(lessonId)[itemKey];
    return stored ?? Boolean(defaultChecked);
  });

  const toggle = (e) => {
    setChecked(e.target.checked);
    if (persist) writeCheck(lessonId, itemKey, e.target.checked);
  };

  return (
    <input
      type="checkbox"
      checked={checked}
      onChange={toggle}
      style={{
        width: "1.05em",
        height: "1.05em",
        marginRight: 10,
        cursor: "pointer",
        verticalAlign: "-0.15em",
      }}
    />
  );
};

export default TaskCheckbox;
