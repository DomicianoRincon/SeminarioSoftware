import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';

vi.mock('./embedded', () => ({ isEmbedded: () => true }));

import { ThemeProvider, useThemeMode } from './ThemeContext';

const Consumer = () => {
  const { mode, toggleTheme, theme, embedded } = useThemeMode();
  return (
    <div>
      <span data-testid="mode">{mode}</span>
      <span data-testid="embedded">{String(embedded)}</span>
      <span data-testid="bg">{theme.background}</span>
      <span data-testid="appbar">{theme.appBarBg}</span>
      <span data-testid="appbar-title">{theme.appBarTitle}</span>
      <span data-testid="appbar-text">{theme.appBarText}</span>
      <button onClick={toggleTheme}>toggle</button>
    </div>
  );
};

const renderWithProvider = () => render(<ThemeProvider><Consumer /></ThemeProvider>);

describe('ThemeContext dentro de un iframe', () => {
  beforeEach(() => {
    localStorage.clear();
    document.body.className = '';
  });

  it('arranca en modo claro por defecto', () => {
    renderWithProvider();
    expect(screen.getByTestId('mode').textContent).toBe('light');
    expect(screen.getByTestId('embedded').textContent).toBe('true');
  });

  it('usa blanco puro de fondo y en la barra superior', () => {
    renderWithProvider();
    expect(screen.getByTestId('bg').textContent).toBe('#FFFFFF');
    expect(screen.getByTestId('appbar').textContent).toBe('#FFFFFF');
  });

  it('pone el título de la barra en oscuro, pero deja appBarText en blanco para los botones de acento', () => {
    renderWithProvider();
    expect(screen.getByTestId('appbar-title').textContent).toBe('#102840');
    expect(screen.getByTestId('appbar-text').textContent).toBe('#FFFFFF');
  });

  it('marca el body con la clase embedded', () => {
    renderWithProvider();
    expect(document.body.classList.contains('embedded')).toBe(true);
    expect(document.body.classList.contains('light')).toBe(true);
  });

  it('guarda el modo con una clave propia y no toca la del sitio abierto directamente', () => {
    localStorage.setItem('themeMode', 'dark');
    renderWithProvider();
    fireEvent.click(screen.getByText('toggle'));
    expect(screen.getByTestId('mode').textContent).toBe('dark');
    expect(localStorage.getItem('themeModeEmbedded')).toBe('dark');
    expect(localStorage.getItem('themeMode')).toBe('dark');
  });

  it('en modo oscuro usa la paleta oscura normal', () => {
    localStorage.setItem('themeModeEmbedded', 'dark');
    renderWithProvider();
    expect(screen.getByTestId('bg').textContent).toBe('#181C23');
    expect(screen.getByTestId('appbar').textContent).toBe('#102840');
  });
});
