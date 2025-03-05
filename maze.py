from tkinter import Tk, BOTH, Canvas
from cell import Cell
from graphics import Window, Line, Point
import time
import random

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
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

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
        time.sleep(.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols -1][self._num_rows -1].has_bottom_wall = False
        self._draw_cell(self._num_cols -1, self._num_rows -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True

        while True:
            to_visit = []
            # Check right cell
            if j+1 < self._num_rows and not self._cells[i][j+1]._visited:
                to_visit.append((i, j+1))
            # Check left cell
            if j-1 >= 0 and not self._cells[i][j-1]._visited:
                to_visit.append((i, j-1))
            # Check top cell
            if i-1 >= 0 and not self._cells[i-1][j]._visited:
                to_visit.append((i-1, j))
            # Check bottom cell
            if i+1 < self._num_cols and not self._cells[i+1][j]._visited:
                to_visit.append((i+1, j))
            if not to_visit:
                self._win.redraw()
                return
            
            selected = random.randrange(len(to_visit))
            to_cell = to_visit[selected]
            print(to_visit)
            print(f'first: {to_cell[0]}, second: {to_cell[1]}')
            
            if to_cell[0] > i:
                self._cells[i][j].has_right_wall = False
                self._cells[to_cell[0]][to_cell[1]].has_left_wall = False
                    # Optional debugging print
                print(f"Breaking right wall at ({i},{j})")
                self._draw_cell(i,j)
                time.sleep(0.05)
            if to_cell[0] < i:
                self._cells[i][j].has_left_wall = False
                self._cells[to_cell[0]][to_cell[1]].has_right_wall = False
                    # Optional debugging print
                print(f"Breaking left wall at ({i},{j})")
                self._draw_cell(i,j)
                time.sleep(0.05)
            if to_cell[1] < j:
                self._cells[i][j].has_top_wall = False
                self._cells[to_cell[0]][to_cell[1]].has_bottom_wall = False
                    # Optional debugging print
                print(f"Breaking top wall at ({i},{j})")
                self._draw_cell(i,j)
                time.sleep(0.05)
            if to_cell[1] > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[to_cell[0]][to_cell[1]].has_top_wall = False
                    # Optional debugging print
                print(f"Breaking bottom wall at ({i},{j})")
                self._draw_cell(i,j)
                time.sleep(0.05)

            self._break_walls_r(to_cell[0], to_cell[1])
