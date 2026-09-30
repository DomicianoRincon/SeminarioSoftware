import React, { createContext, useContext, useState, useMemo, useEffect } from 'react';
import { light, dark, embeddedLight } from './colors';
import { isEmbedded } from './embedded';

const ThemeContext = createContext();

// Dentro de un iframe la preferencia se guarda con otra clave: el iframe comparte
// localStorage con el sitio abierto directamente (mismo origen), y elegir un modo
// en uno no debe cambiar el del otro.
const STORAGE_KEY = 'themeMode';
const EMBEDDED_STORAGE_KEY = 'themeModeEmbedded';

// Un iframe con sandbox puede bloquear localStorage y lanzar al tocarlo.
const readMode = (key) => {
  try {
    return localStorage.getItem(key);
  } catch {
    return null;
  }
};
const writeMode = (key, mode) => {
  try {
    localStorage.setItem(key, mode);
  } catch {
    // Sin almacenamiento el modo dura lo que dure la página.
  }
};

export const ThemeProvider = ({ children }) => {
  const [embedded] = useState(isEmbedded);
  const storageKey = embedded ? EMBEDDED_STORAGE_KEY : STORAGE_KEY;

  // Por defecto: oscuro al abrir el sitio directamente, claro dentro de un iframe.
  const [mode, setMode] = useState(() => readMode(storageKey) || (embedded ? 'light' : 'dark'));

  const theme = useMemo(() => {
    if (mode === 'dark') return dark;
    return embedded ? embeddedLight : light;
  }, [mode, embedded]);

  const toggleTheme = () => {
    setMode((prev) => (prev === 'dark' ? 'light' : 'dark'));
  };

  useEffect(() => {
    document.body.classList.remove('dark', 'light');
    document.body.classList.add(mode);
    document.body.classList.toggle('embedded', embedded);
    writeMode(storageKey, mode);
  }, [mode, embedded, storageKey]);

  return (
    <ThemeContext.Provider value={{ mode, theme, toggleTheme, embedded }}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useThemeMode = () => useContext(ThemeContext);
