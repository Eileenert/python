import tkinter as tk
import data
import function as f
import keyboard
import time


class Interface(tk.Frame):
    """main Interface"""

    def __init__(self, **kwargs):
        tk.Frame.__init__(self, **kwargs)

        # design
        self.master.title("2048")
        self.master.geometry('489x473')
        self.master.configure(bg=data.background_color)

        self.grid(sticky="")

        # list with cells information
        self.grid_cells = []
        self.init_grid()

        # positions of labels and numbers
        self.position = f.new_game(data.grid_len)
        self.update_position()

        # after initializing the game we repeat the same functions in self.game_on
        self.game_on()

    def init_grid(self):
        # init the grid

        for i in range(data.grid_len):
            grid_row = []
            for j in range(data.grid_len):
                cell = tk.Frame(self,
                                bg=data.background_color_empty_cell,
                                width=100,
                                height=200)

                cell.grid(row=i,
                          column=j,
                          padx=data.grid_padding,
                          pady=data.grid_padding)

                t = tk.Label(master=cell,
                             text="",
                             bg=data.background_color_empty_cell,
                             justify=tk.CENTER,
                             font=data.font,
                             width=4,
                             height=2,
                             relief="groove")
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    # display the correct number at the correct position
    def update_position(self):
        for i in range(data.grid_len):
            for j in range(data.grid_len):
                new_number = self.position[i][j]

                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="",
                        bg=data.background_color_empty_cell,
                    )
                else:
                    self.grid_cells[i][j].configure(
                        text=new_number,
                        bg=data.background_color_number_dict[new_number],
                        fg=data.cell_number_color_dict[new_number])

    def game_on(self):
        """wait to press a key and do functions according to keys
        observe if the game is won or lost or in progress"""
        done = False

        if keyboard.is_pressed(data.key_up[0]) or keyboard.is_pressed(data.key_up[1]):
            self.position, done = f.key_up_pressed(self.position)

        elif keyboard.is_pressed(data.key_down[0]) or keyboard.is_pressed(data.key_down[1]):
            self.position, done = f.key_down_pressed(self.position)

        elif keyboard.is_pressed(data.key_left[0]) or keyboard.is_pressed(data.key_left[1]):
            self.position, done = f.key_left_pressed(self.position)

        elif keyboard.is_pressed(data.key_right[0]) or keyboard.is_pressed(data.key_right[1]):
            self.position, done = f.key_right_pressed(self.position)

        if done == True:
            self.position = f.add_two(self.position)
            self.update_position()
            game_state = f.game_stat(self.position)
            if game_state == 'win':
                self.grid_cells[1][1].configure(
                    text="You", bg=data.background_color_empty_cell)
                self.grid_cells[1][2].configure(
                    text="Win!", bg=data.background_color_empty_cell)
            if game_state == "lose":
                self.grid_cells[1][1].configure(
                    text="You", bg=data.background_color_empty_cell)
                self.grid_cells[1][2].configure(
                    text="Lose!", bg=data.background_color_empty_cell)
            time.sleep(0.01)

        self.master.after(150, self.game_on)


if __name__ == '__main__':
    # we create our interface
    interface = Interface()
    interface.mainloop()
