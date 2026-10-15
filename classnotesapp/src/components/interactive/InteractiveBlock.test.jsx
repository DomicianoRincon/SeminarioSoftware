import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { render, screen, fireEvent, act } from '@testing-library/react';
import { ThemeProvider } from '@/theme/ThemeContext';
import InteractiveBlock from './InteractiveBlock';
import { SIMS, parseSpec } from './flutterStateSims';

const renderBlock = (spec) => render(<ThemeProvider><InteractiveBlock spec={spec} /></ThemeProvider>);

const type = (label, value) => {
  const field = screen.getByLabelText(label);
  field.value = value;
  fireEvent.input(field);
};

beforeEach(() => vi.useFakeTimers());
afterEach(() => vi.useRealTimers());

describe('parseSpec', () => {
  it('splits the simulator name from its options', () => {
    expect(parseSpec('playlist cards')).toEqual({ name: 'playlist', args: ['cards'] });
    expect(parseSpec('  state-counter\n')).toEqual({ name: 'state-counter', args: [] });
    expect(parseSpec('')).toEqual({ name: '', args: [] });
  });
});

describe('InteractiveBlock', () => {
  it('shows a visible notice for an unknown simulator instead of a blank block', () => {
    renderBlock('nope');
    expect(screen.getByText(/Diagrama interactivo desconocido/)).toBeTruthy();
  });

  it('mounts every registered simulator and cleans up on unmount', () => {
    Object.keys(SIMS).forEach((name) => {
      const { container, unmount } = renderBlock(name);
      expect(container.querySelector('.fsim')).toBeTruthy();
      unmount();
    });
    expect(document.getElementById('fsim-style')).toBeTruthy();
  });
});

describe('state-counter', () => {
  it('increments _counter and rebuilds the screen through setState', () => {
    renderBlock('state-counter');
    fireEvent.click(screen.getByLabelText('Incrementar'));
    act(() => vi.advanceTimersByTime(400));
    expect(screen.getByTestId('counter-text').textContent).toBe('1');
    expect(screen.getAllByText(/build\(\) con _counter = 1/).length).toBeGreaterThan(0);
  });

  it('leaves the screen stale when setState is forgotten', () => {
    renderBlock('state-counter');
    fireEvent.click(screen.getByLabelText('Olvidar setState'));
    fireEvent.click(screen.getByLabelText('Incrementar'));
    fireEvent.click(screen.getByLabelText('Incrementar'));
    act(() => vi.advanceTimersByTime(400));
    expect(screen.getByTestId('counter-text').textContent).toBe('0');
    expect(screen.getByText(/pero nadie pidió reconstruir/)).toBeTruthy();
  });
});

describe('hot-reload', () => {
  it('keeps the counter on hot reload and resets it on hot restart', () => {
    renderBlock('hot-reload');
    fireEvent.click(screen.getByLabelText('Incrementar'));
    act(() => vi.advanceTimersByTime(400));
    fireEvent.click(screen.getByText('Hot reload'));
    expect(screen.getByTestId('counter-text').textContent).toBe('1');
    fireEvent.click(screen.getByText('Hot restart'));
    expect(screen.getByTestId('counter-text').textContent).toBe('0');
  });
});

describe('state-tree', () => {
  it('keeps the count across a parent rebuild only when it lives in State', () => {
    renderBlock('state-tree');
    fireEvent.click(screen.getByLabelText('Incrementar'));
    fireEvent.click(screen.getByText('Reconstruir MyApp'));
    expect(screen.getByTestId('tree-counter').textContent).toBe('1');

    fireEvent.click(screen.getByLabelText('Guardar el contador en un StatelessWidget'));
    fireEvent.click(screen.getByLabelText('Incrementar'));
    expect(screen.getByTestId('tree-counter').textContent).toBe('0');
    fireEvent.click(screen.getByText('Reconstruir MyApp'));
    expect(screen.getByText(/contador vuelve a 0/)).toBeTruthy();
  });
});

describe('state-lifecycle', () => {
  it('creates the controller in initState, frees it in dispose and flags a late setState', () => {
    renderBlock('state-lifecycle');
    fireEvent.click(screen.getByText('Abrir saludo'));
    act(() => vi.advanceTimersByTime(800));
    expect(screen.getByText('#1 activo')).toBeTruthy();
    type('Nombre', 'Ana');
    expect(screen.getByText('Hola, Ana')).toBeTruthy();
    fireEvent.click(screen.getByText('Guardar (tarda 2 s)'));
    fireEvent.click(screen.getByText('Volver'));
    expect(screen.getByText('#1 liberado')).toBeTruthy();
    act(() => vi.advanceTimersByTime(2100));
    expect(screen.getByText(/setState\(\) called after dispose\(\)/)).toBeTruthy();
  });
});

describe('playlist', () => {
  it('adds whatever the fields hold, like the minimal _addSong of the lesson', () => {
    renderBlock('playlist');
    expect(screen.getByTestId('playlist-list').childNodes).toHaveLength(0);
    type('Nombre de la canción', 'Bohemian Rhapsody');
    type('Artista', 'Queen');
    fireEvent.click(screen.getByText('Agregar'));
    expect(screen.getByTestId('playlist-list').textContent).toBe('Bohemian Rhapsody · Queen');
    expect(screen.getByLabelText('Nombre de la canción').value).toBe('Bohemian Rhapsody');
    type('Nombre de la canción', '');
    type('Artista', '');
    fireEvent.click(screen.getByText('Agregar'));
    expect(screen.getByTestId('playlist-list').childNodes).toHaveLength(2);
    expect(screen.getByText(/canción vacía/)).toBeTruthy();
  });

  it('switches the same state between Text and SongCard views', () => {
    const { container } = renderBlock('playlist cards');
    type('Nombre de la canción', 'Yellow');
    type('Artista', 'Coldplay');
    fireEvent.click(screen.getByText('Agregar'));
    expect(container.querySelectorAll('.fs-card')).toHaveLength(1);
    fireEvent.click(screen.getByRole('button', { name: 'Text' }));
    expect(container.querySelectorAll('.fs-card')).toHaveLength(0);
    expect(screen.getByTestId('playlist-list').textContent).toBe('Yellow · Coldplay');
  });
});
