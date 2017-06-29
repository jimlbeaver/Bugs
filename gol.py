
import pygame
from pygame.locals import *
from pygamehelper import *
from vec2d import *
from random import randrange


class Matrix:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self._data = []

        for i in range(self.w * self.h):
            self._data.append(None)

    def __getitem__(self, i):
        return self._data[i]

    def _index(self, x, y):
        return x + (y * self.w)

    def get(self, x, y):
        return self._data[self._index(x, y)]

    def set(self, x, y, v):
        self._data[self._index(x, y)] = v


class Cell:
    def __init__(self, x, y, w):
        self.x, self.y, self.w = x, y, w
        self.alive = False

    def draw(self, screen):
        color = (255, 255, 0) if self.alive else (100, 100, 100)
        xywh = (self.x * self.w, self.y * self.w, self.w, self.w)
        pygame.draw.rect(screen, color, xywh, 0)
        pygame.draw.rect(screen, (100, 0, 0), xywh, 1)


class GameOfLife(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h))

        self.begin = raw_input('Begin: ') or [3]
        self.begin = [int(x) for x in self.begin]
        self.stay = raw_input('Stay: ') or [3, 2]
        self.stay = [int(x) for x in self.stay]
        self.paused = True
        self.cellw = input('Cell width: ')
        self.cells = Matrix(self.w / self.cellw, self.h / self.cellw)

        random = (raw_input
                  ('Random arrangement of live cells? (y/n) ') == 'y')

        for i in range(self.cells.w):
            for j in range(self.cells.h):
                c = Cell(i, j, self.cellw)
                if random: c.alive = (randrange(2) == 1)
                self.cells.set(i, j, c)

    def neighbours(self, c):
        n = []
        x, y = c.x, c.y
        for i in [1, -1, 0]:
            for j in [1, -1, 0]:
                if i == 0 and j == 0: continue
                if (x + i) < 0: i += self.cells.w
                if (x + i) >= self.cells.w: i -= self.cells.w

                if (y + j) < 0: j += self.cells.h
                if (y + j) >= self.cells.h: j -= self.cells.h

                n.append(self.cells.get(x + i, y + j))

        return n

    def mouseUp(self, pos):
        if not self.paused: return

        x = (pos[0] - (pos[0] % self.cellw)) / self.cellw
        y = (pos[1] - (pos[1] % self.cellw)) / self.cellw
        c = self.cells.get(x, y)
        c.alive = not c.alive

    def keyDown(self, key):
        if key == 275 and self.paused:
            self.paused = False
            self.update()
            self.draw()
            self.paused = True
        else:
            self.paused = not self.paused

    def update(self):
        if self.paused: return

        changed = []
        for c in self.cells:
            neighbours = self.neighbours(c)
            liveneighbours = [n for n in neighbours if n.alive]

            if c.alive:
                if len(liveneighbours) not in self.stay:
                    changed.append(c)

            if not c.alive:
                if len(liveneighbours) in self.begin:
                    changed.append(c)

        for c in changed:
            c.alive = not c.alive

    def draw(self):
        self.screen.fill((0, 0, 0))

        for c in self.cells:
            c.draw(self.screen)

        pygame.display.update()

g = GameOfLife()
g.mainLoop(60)
