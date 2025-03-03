from tkinter import Tk, BOTH, Canvas
from cell import Cell
from graphics import Window, Line, Point
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        
        for i in range(0, self._num_cols):
            column = []
            for j in range(0, self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)
        
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x = (i * self._cell_size_x) + self._x1
        y = (j * self._cell_size_y) + self._y1
        x2 = x + self._cell_size_x
        y2 = y + self._cell_size_y


        self._cells[i][j].draw(x,y,x2, y2)

        self._animate()


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(.05)