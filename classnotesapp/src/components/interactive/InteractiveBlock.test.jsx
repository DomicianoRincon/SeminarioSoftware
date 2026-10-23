import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { render, screen, fireEvent, act, within } from '@testing-library/react';
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
  const STEP = 1100;
  const nodeId = (container, key) => container.querySelector(`[data-node="${key}"] .fs-id`).textContent;

  it('changes the state first and the screen only at the last step', () => {
    const { container } = renderBlock('state-tree');
    fireEvent.click(screen.getByLabelText('Incrementar'));
    act(() => vi.advanceTimersByTime(STEP));
    expect(screen.getByTestId('var-_counter').textContent).toBe('1');
    expect(screen.getByTestId('tree-counter').textContent).toBe('0');
    expect(screen.getByText('sucio: pide build()')).toBeTruthy();
    act(() => vi.advanceTimersByTime(STEP * 2));
    expect(container.querySelector('[data-node="text"] b').textContent).toBe("Text('1')");
    expect(screen.getByTestId('tree-counter').textContent).toBe('0');
    act(() => vi.advanceTimersByTime(STEP * 2));
    expect(screen.getByTestId('tree-counter').textContent).toBe('1');
    expect(screen.getByText('al día')).toBeTruthy();
    expect(nodeId(container, 'state')).toBe('#3');
  });

  it('never loses a tap made in the middle of an animation', () => {
    renderBlock('state-tree');
    fireEvent.click(screen.getByLabelText('Incrementar'));
    fireEvent.click(screen.getByLabelText('Incrementar'));
    act(() => vi.advanceTimersByTime(STEP * 6));
    expect(screen.getByTestId('var-_counter').textContent).toBe('2');
    expect(screen.getByTestId('tree-counter').textContent).toBe('2');
  });

  it('lights the line that runs in each step and marks where the state is bound', () => {
    const { container } = renderBlock('state-tree bulb');
    const lit = () => [...container.querySelectorAll('.fs-code-line.fs-on')].map((l) => l.textContent.trim());
    const bound = [...container.querySelectorAll('.fs-code-line.fs-bind')].map((l) => l.textContent.trim());
    expect(bound).toContain("Text(_isOn ? 'Encendido' : 'Apagado'),");
    expect(bound).toContain("_isOn ? 'Apagar' : 'Encender',");
    expect(container.querySelectorAll('.fs-sv').length).toBeGreaterThan(4);
    fireEvent.click(screen.getByRole('button', { name: 'Encender' }));
    expect(lit()).toEqual(['onPressed: () => _toggle(),']);
    act(() => vi.advanceTimersByTime(STEP));
    expect(lit()).toEqual(['setState(() {', '_isOn = !_isOn;']);
    act(() => vi.advanceTimersByTime(STEP * 2));
    expect(lit()).toEqual(bound);
  });

  it('switches between the tree and the code without touching the state', () => {
    const { container } = renderBlock('state-tree bulb');
    const treeBox = () => container.querySelector('[data-node="app"]').closest('.fs-panel');
    const codeBox = () => container.querySelector('.fs-code-line').closest('.fs-dark');
    expect(treeBox().hidden).toBe(false);
    expect(codeBox().hidden).toBe(true);
    fireEvent.click(screen.getByRole('button', { name: 'Encender' }));
    act(() => vi.advanceTimersByTime(STEP));
    fireEvent.click(screen.getByRole('button', { name: 'Código' }));
    expect(treeBox().hidden).toBe(true);
    expect(codeBox().hidden).toBe(false);
    expect(screen.getByTestId('var-_isOn').textContent).toBe('true');
    act(() => vi.advanceTimersByTime(STEP * 5));
    expect(screen.getByTestId('bulb-text').textContent).toBe('Encendido');
    fireEvent.click(screen.getByRole('button', { name: 'Árbol de widgets' }));
    expect(container.querySelector('[data-node="text"] b').textContent).toBe("Text('Encendido')");
  });

  it('shows the forgotten setState: the state moves, the screen does not', () => {
    const { container } = renderBlock('state-tree forget');
    fireEvent.click(screen.getByLabelText('Olvidar setState'));
    expect(container.textContent).not.toContain('setState(() {');
    fireEvent.click(screen.getByLabelText('Incrementar'));
    act(() => vi.advanceTimersByTime(STEP * 4));
    fireEvent.click(screen.getByLabelText('Incrementar'));
    act(() => vi.advanceTimersByTime(STEP * 4));
    expect(screen.getByTestId('var-_counter').textContent).toBe('2');
    expect(screen.getByTestId('tree-counter').textContent).toBe('0');
    expect(screen.getByText('Flutter no se enteró')).toBeTruthy();
    fireEvent.click(screen.getByLabelText('Olvidar setState'));
    fireEvent.click(screen.getByLabelText('Incrementar'));
    act(() => vi.advanceTimersByTime(STEP * 6));
    expect(screen.getByTestId('tree-counter').textContent).toBe('3');
    expect(screen.getByText('al día')).toBeTruthy();
  });

  it('waits for Siguiente paso in step-by-step mode', () => {
    renderBlock('state-tree');
    fireEvent.click(screen.getByLabelText('Paso a paso'));
    fireEvent.click(screen.getByLabelText('Incrementar'));
    act(() => vi.advanceTimersByTime(STEP * 5));
    expect(screen.getByTestId('var-_counter').textContent).toBe('0');
    fireEvent.click(screen.getByRole('button', { name: 'Siguiente paso' }));
    expect(screen.getByTestId('var-_counter').textContent).toBe('1');
  });

  it('keeps the State and _isOn when the parent rebuilds (bulb)', () => {
    const { container } = renderBlock('state-tree bulb');
    fireEvent.click(screen.getByRole('button', { name: 'Encender' }));
    act(() => vi.advanceTimersByTime(STEP * 6));
    expect(screen.getByTestId('bulb-text').textContent).toBe('Encendido');
    const widgetBefore = nodeId(container, 'widget');
    const stateBefore = nodeId(container, 'state');
    fireEvent.click(screen.getByRole('button', { name: 'Reconstruir App' }));
    act(() => vi.advanceTimersByTime(STEP * 6));
    expect(nodeId(container, 'widget')).not.toBe(widgetBefore);
    expect(nodeId(container, 'state')).toBe(stateBefore);
    expect(screen.getByTestId('var-_isOn').textContent).toBe('true');
    expect(container.querySelectorAll('.fs-lines .fs-read')).toHaveLength(3);
  });
});

describe('state-lifecycle', () => {
  const STEP = 1000;
  const count = (container, phase) => container.querySelector(`[data-phase="${phase}"] .fs-lc-count`).textContent;

  it('walks createState, initState and build, rebuilds on setState and runs dispose on Cerrar', () => {
    const { container } = renderBlock('state-lifecycle');
    fireEvent.click(screen.getByLabelText('Abrir Saludo'));
    expect(count(container, 'createState')).toBe('×1');
    expect(screen.queryByLabelText('Nombre')).toBeNull();
    act(() => vi.advanceTimersByTime(STEP * 2));
    expect(count(container, 'initState')).toBe('×1');
    type('Nombre', 'Ana');
    expect(screen.getByTestId('lc-greeting').textContent).toBe('Hola');
    expect(count(container, 'build')).toBe('×1');
    fireEvent.click(screen.getByRole('button', { name: 'Saludar' }));
    expect(count(container, 'setState')).toBe('×1');
    expect(screen.getByTestId('lc-greeting').textContent).toBe('Hola');
    act(() => vi.advanceTimersByTime(STEP));
    expect(screen.getByTestId('lc-greeting').textContent).toBe('Hola, Ana');
    expect(count(container, 'build')).toBe('×2');
    fireEvent.click(screen.getByRole('button', { name: 'Cerrar' }));
    expect(count(container, 'dispose')).toBe('×1');
    expect(screen.getByLabelText('Abrir Saludo')).toBeTruthy();
    fireEvent.click(screen.getByLabelText('Abrir Saludo'));
    expect(screen.getByTestId('lc-caption').textContent).toContain('#2');
    act(() => vi.advanceTimersByTime(STEP * 2));
    expect(count(container, 'build')).toBe('×1');
    expect(screen.getByLabelText('Nombre').value).toBe('');
  });
});

describe('playlist', () => {
  const STEP = 1100;
  const list = () => screen.getByTestId('playlist-list');

  it('adds the song to _songs first and paints the list only at the last step', () => {
    const { container } = renderBlock('playlist');
    expect(list().childNodes).toHaveLength(0);
    type('Nombre de la canción', 'Bohemian Rhapsody');
    type('Artista', 'Queen');
    expect(screen.getByTestId('var-_titleController').textContent).toBe("'Bohemian Rhapsody'");
    fireEvent.click(screen.getByText('Agregar'));
    act(() => vi.advanceTimersByTime(STEP));
    expect(screen.getByTestId('var-_songs').textContent).toContain("Song('Bohemian Rhap…', 'Queen')");
    expect(list().childNodes).toHaveLength(0);
    expect(screen.getByText('sucio: pide build()')).toBeTruthy();
    act(() => vi.advanceTimersByTime(STEP * 4));
    expect(list().textContent).toBe('Bohemian Rhapsody · Queen');
    expect(container.querySelector('[data-node="text-0"]')).toBeTruthy();
    expect(screen.getByLabelText('Nombre de la canción').value).toBe('Bohemian Rhapsody');
    type('Nombre de la canción', '');
    type('Artista', '');
    fireEvent.click(screen.getByText('Agregar'));
    act(() => vi.advanceTimersByTime(STEP));
    expect(screen.getByTestId('tree-caption').textContent).toMatch(/canción vacía/);
    act(() => vi.advanceTimersByTime(STEP * 4));
    expect(list().childNodes).toHaveLength(2);
  });

  it('types into the controllers without running build()', () => {
    const { container } = renderBlock('playlist');
    const before = container.querySelector('[data-node="title"] .fs-id').textContent;
    type('Artista', 'Queen');
    expect(screen.getByTestId('var-_artistController').textContent).toBe("'Queen'");
    expect(screen.getByTestId('tree-caption').textContent).toMatch(/sin setState/);
    expect(container.querySelector('[data-node="title"] .fs-id').textContent).toBe(before);
  });

  it('switches Text and SongCard with a hot reload that keeps _songs', () => {
    const { container } = renderBlock('playlist cards');
    type('Nombre de la canción', 'Yellow');
    type('Artista', 'Coldplay');
    fireEvent.click(screen.getByText('Agregar'));
    act(() => vi.advanceTimersByTime(STEP * 6));
    expect(container.querySelectorAll('.fs-card')).toHaveLength(1);
    const songs = screen.getByTestId('var-_songs').textContent;
    fireEvent.click(screen.getByRole('button', { name: 'Text' }));
    expect(container.textContent).toContain("Text('${song.title} · ${song.artist}'),");
    act(() => vi.advanceTimersByTime(STEP * 5));
    expect(container.querySelectorAll('.fs-card')).toHaveLength(0);
    expect(list().textContent).toBe('Yellow · Coldplay');
    expect(container.querySelector('[data-node="text-0"]')).toBeTruthy();
    expect(screen.getByTestId('var-_songs').textContent).toBe(songs);
  });

  it('keeps the list one step behind when setState is forgotten', () => {
    renderBlock('playlist forget');
    fireEvent.click(screen.getByLabelText('Olvidar setState'));
    type('Nombre de la canción', 'Yellow');
    fireEvent.click(screen.getByText('Agregar'));
    act(() => vi.advanceTimersByTime(STEP * 4));
    expect(screen.getByTestId('var-_songs').textContent).toContain('Yellow');
    expect(list().childNodes).toHaveLength(0);
    expect(screen.getByText('Flutter no se enteró')).toBeTruthy();
    fireEvent.click(screen.getByLabelText('Olvidar setState'));
    fireEvent.click(screen.getByText('Agregar'));
    act(() => vi.advanceTimersByTime(STEP * 6));
    expect(list().childNodes).toHaveLength(2);
  });
});

describe('lift', () => {
  const STEP = 1300;
  const list = () => screen.getByTestId('lift-list');
  const songs = () => screen.getByTestId('lift-songs').textContent;
  const add = (title, artist) => {
    type('Nombre de la canción', title);
    type('Artista', artist);
    fireEvent.click(screen.getByText('Agregar'));
  };

  it('keeps _songs in the Screen and passes it down one widget per step', () => {
    const { container } = renderBlock('lift');
    expect(list().textContent).toBe('Todavía no hay canciones');
    type('Artista', 'Queen');
    expect(within(screen.getByTestId('screen-state')).getByTestId('draft-artist').textContent).toBe("'Queen'");
    type('Nombre de la canción', 'Bohemian Rhapsody');
    fireEvent.click(screen.getByText('Agregar'));
    act(() => vi.advanceTimersByTime(STEP));
    expect(songs()).toContain('Song #1');
    expect(screen.getByText('sucio: pide build()')).toBeTruthy();
    expect(container.querySelector('[data-node="card-1"]')).toBeNull();
    act(() => vi.advanceTimersByTime(STEP));
    expect(screen.getByTestId('builds-screen').textContent).toBe('build ×2');
    expect(container.querySelector('[data-node="card-1"]')).toBeNull();
    act(() => vi.advanceTimersByTime(STEP));
    expect(container.querySelector('[data-node="card-1"]')).toBeTruthy();
    expect(list().querySelectorAll('.fs-card')).toHaveLength(0);
    act(() => vi.advanceTimersByTime(STEP * 2));
    expect(list().querySelectorAll('.fs-card')).toHaveLength(1);
  });

  it('sends onAdd up from SongForm, which keeps only the draft', () => {
    const { container } = renderBlock('lift events');
    fireEvent.click(screen.getByText('Agregar'));
    expect(screen.getByTestId('lift-caption').textContent).toMatch(/no llama a onAdd/);
    expect(screen.getByTestId('builds-form').textContent).toBe('build ×2');
    expect(screen.getByTestId('builds-screen').textContent).toBe('build ×1');
    add('Yellow', 'Coldplay');
    expect(within(screen.getByTestId('form-state')).getByTestId('draft-title').textContent).toBe("''");
    expect(container.querySelector('.fs-lift-packet.fs-up').textContent).toBe('onAdd(song)');
    act(() => vi.advanceTimersByTime(STEP * 5));
    expect(list().querySelectorAll('.fs-card')).toHaveLength(1);
    expect(container.querySelectorAll('[data-node="list"] .fs-pass')).toHaveLength(1);
    fireEvent.click(screen.getByLabelText('Quitar Yellow'));
    expect(container.querySelector('.fs-lift-packet.fs-up').textContent).toBe('onDelete()');
    act(() => vi.advanceTimersByTime(STEP * 5));
    expect(list().textContent).toBe('Todavía no hay canciones');
    expect(songs()).toContain('vacía');
  });

  it('replaces the song with a copy when it becomes a favorite', () => {
    renderBlock('lift fav');
    add('Yellow', 'Coldplay');
    act(() => vi.advanceTimersByTime(STEP * 5));
    fireEvent.click(screen.getByLabelText('Favorita Yellow'));
    act(() => vi.advanceTimersByTime(STEP));
    expect(screen.getByTestId('lift-caption').textContent).toMatch(/copyWith/);
    expect(songs()).toContain('Song #2');
    expect(songs()).not.toContain('Song #1');
    act(() => vi.advanceTimersByTime(STEP * 4));
    expect(screen.getByLabelText('Favorita Yellow').textContent).toBe('♥');
  });
});

describe('compose', () => {
  const add = (title, artist) => {
    type('Nombre de la canción', title);
    type('Artista', artist);
    fireEvent.click(screen.getByText('Agregar'));
  };
  const nodes = (container) => [...container.querySelectorAll('[data-node]')].map((n) => n.dataset.node);

  it('starts flat: one State with every variable and the cards hanging from the Screen', () => {
    const { container } = renderBlock('compose');
    add('Yellow', 'Coldplay');
    expect(nodes(container)).toContain('card-1');
    expect(nodes(container)).not.toContain('form');
    expect(container.querySelectorAll('.fs-cmp-group')).toHaveLength(1);
    expect(container.querySelector('[data-var="_titleController"]')).toBeTruthy();
    expect(screen.getByTestId('compose-list').querySelectorAll('.fs-card')).toHaveLength(1);
  });

  it('shows the named components, two state holders and a working app', () => {
    const { container } = renderBlock('compose');
    add('Yellow', 'Coldplay');
    fireEvent.click(screen.getByRole('button', { name: 'Con componentes' }));
    expect(nodes(container)).toEqual(expect.arrayContaining(['summary', 'form', 'list', 'card-1']));
    expect(container.querySelectorAll('.fs-cmp-group')).toHaveLength(2);
    expect(screen.getByText('1 canción')).toBeTruthy();
    type('Artista', '');
    fireEvent.click(screen.getByText('Agregar'));
    expect(nodes(container)).toContain('error');
    fireEvent.click(screen.getByLabelText('Favorita Yellow'));
    expect(container.querySelector('[data-var="_songs"] .fs-fav')).toBeTruthy();
    fireEvent.click(screen.getByLabelText('Favorita Yellow'));
    fireEvent.click(screen.getByLabelText('Solo favoritas'));
    expect(screen.getByTestId('compose-list').textContent).toBe('No tienes favoritas');
    fireEvent.click(screen.getByLabelText('Solo favoritas'));
    fireEvent.click(screen.getByLabelText('Favorita Yellow'));
    fireEvent.click(screen.getByLabelText('Solo favoritas'));
    expect(screen.getByTestId('compose-list').querySelectorAll('.fs-card')).toHaveLength(1);
  });

  it('lights the lines of the variable that is clicked', async () => {
    const { container } = renderBlock('compose');
    const songs = container.querySelector('[data-var="_songs"]');
    fireEvent.click(songs);
    const again = container.querySelector('[data-var="_songs"]');
    expect(again.getAttribute('aria-pressed')).toBe('true');
    await act(async () => vi.advanceTimersByTime(50));
    expect(container.querySelector('[data-var="_songs"]').classList.contains('fs-sel')).toBe(true);
    fireEvent.click(container.querySelector('[data-var="_songs"]'));
    expect(container.querySelector('[data-var="_songs"]').getAttribute('aria-pressed')).toBe('false');
  });
});

describe('callback', () => {
  const next = (n = 1) => {
    for (let i = 0; i < n; i += 1) fireEvent.click(screen.getByRole('button', { name: 'Siguiente' }));
  };

  it('builds the path step by step and only then enables the trash cans', () => {
    const { container } = renderBlock('callback');
    expect(screen.getByLabelText('Quitar Yellow').disabled).toBe(true);
    next();
    expect(container.querySelector('[data-level="l1"]').textContent).toContain('_deleteSong');
    next();
    expect(container.querySelector('[data-level="l3"]').textContent).toContain('¿?');
    next();
    expect(container.querySelector('[data-level="l2"]').textContent).toContain('final Function(Song) onDelete;');
    next(2);
    expect(container.querySelector('[data-level="l3"]').textContent).toContain('onPressed: () => onDelete(),');
    expect(screen.getByLabelText('Quitar Yellow').disabled).toBe(false);
  });

  it('climbs back to the Screen and removes the song with setState', () => {
    renderBlock('callback');
    next(5);
    fireEvent.click(screen.getByLabelText('Quitar Yellow'));
    act(() => vi.advanceTimersByTime(1400 * 2));
    expect(screen.getByTestId('callback-list').textContent).toContain('Yellow');
    act(() => vi.advanceTimersByTime(1400));
    expect(screen.getByTestId('callback-caption').textContent).toMatch(/setState/);
    act(() => vi.advanceTimersByTime(1400));
    expect(screen.getByTestId('callback-list').textContent).not.toContain('Yellow');
    expect(screen.getByTestId('callback-list').querySelectorAll('.fs-card')).toHaveLength(2);
  });
});
