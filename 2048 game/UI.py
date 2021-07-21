from tkinter import Frame, Label, CENTER

import Logic
import Constant as c


class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.matrix = Logic.start_Game()
        self.grid()
        self.master.title('2048    w - up    s - down    a - left     d - right')
        self.master.bind("<Key>", self.key_down)
        self.commands = {c.KEY_UP: Logic.move_up, c.KEY_DOWN: Logic.move_down,
                         c.KEY_RIGHT: Logic.move_right, c.KEY_LEFT: Logic.move_left}
        # creating a grid
        self.grid_cells = []
        # add the grid cell
        self.init_grid()
        # Start a game and add two 2's
        self.init_matrix()
        # set the number according to color
        self.update_grid_cells()

        # it actually runs the code
        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
        background.grid()
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRIP_PADDING,
                          pady=c.GRIP_PADDING)
                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT,
                          width=5, height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        Logic.add_new_two(self.matrix)
        Logic.add_new_two(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="",
                                                    bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),
                                                    bg=c.BACKGROUND_COLOR_DICT[new_number],
                                                    fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()

    def key_down(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                Logic.add_new_two(self.matrix)
                self.update_grid_cells()
                changed = False
                if Logic.current_state_game(self.matrix) == "Won":
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if Logic.current_state_game(self.matrix) == "Lost":
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lost!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)


gameGrid = Game2048()
