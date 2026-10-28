import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { ThemeProvider } from '@/theme/ThemeContext';
import InteractiveBlock from './InteractiveBlock';
import { SKILLS, skillTree } from './skillSims';

const renderBlock = (spec) => render(<ThemeProvider><InteractiveBlock spec={spec} /></ThemeProvider>);
const skillMd = (skill) => skill.files.find((file) => file.path === 'SKILL.md').content;

describe('SKILLS', () => {
  it('has the four course skills, in the order they are used', () => {
    expect(SKILLS.map((skill) => skill.name)).toEqual(['disenador-bd', 'mer-svg', 'flutter-pantallas', 'flutter-componentes']);
  });

  it('opens every skill on its SKILL.md, whose name matches the folder', () => {
    SKILLS.forEach((skill) => {
      expect(skill.files[0].path).toBe('SKILL.md');
      const front = skillMd(skill).match(/^---\n([\s\S]*?)\n---/);
      expect(front, skill.name).toBeTruthy();
      expect(front[1]).toContain(`name: ${skill.name}\n`);
      expect(front[1]).toMatch(/\ndescription: .*Úsala cuando/);
    });
  });

  it('only points to files the student is told to create', () => {
    SKILLS.forEach((skill) => {
      const paths = skill.files.map((file) => file.path);
      const mentioned = [...skillMd(skill).matchAll(/`((?:references|assets|scripts)\/[^`]+)`/g)].map((m) => m[1]);
      mentioned.forEach((path) => expect(paths, `${skill.name}: ${path}`).toContain(path));
      paths.filter((path) => path !== 'SKILL.md').forEach((path) => expect(mentioned, `${skill.name}: ${path}`).toContain(path));
    });
  });

  it('keeps code lines short enough for the viewer', () => {
    SKILLS.forEach((skill) => skill.files.forEach((file) => {
      if (!file.path.endsWith('.dart')) return;
      file.content.split('\n').forEach((line) => expect(line.length, `${skill.name}/${file.path}: ${line}`).toBeLessThanOrEqual(80));
    }));
  });

  it('lists folders before the files they hold', () => {
    const rows = skillTree(SKILLS.find((skill) => skill.name === 'disenador-bd'));
    expect(rows.map((row) => row.name)).toEqual(['SKILL.md', 'assets/', 'modelo.md', 'references/', 'normalizacion.md', 'preguntas.md']);
  });
});

describe('skill-files', () => {
  it('switches skill and file', () => {
    const { container } = renderBlock('skill-files');
    expect(screen.getByTestId('skill-content').textContent).toContain('name: disenador-bd');
    fireEvent.click(screen.getByRole('tab', { name: 'flutter-componentes' }));
    expect(screen.getByTestId('skill-content').textContent).toContain('name: flutter-componentes');
    fireEvent.click(container.querySelector('[data-path="assets/product_card.dart"]'));
    expect(screen.getByTestId('skill-content').textContent).toContain('GestureDetector');
    expect(container.textContent).toContain('.agents/skills/flutter-componentes/assets/product_card.dart');
  });

  it('opens on the skill given as option', () => {
    renderBlock('skill-files mer-svg');
    expect(screen.getByTestId('skill-content').textContent).toContain('name: mer-svg');
  });
});
