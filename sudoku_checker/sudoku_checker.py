import tkinter as tk
import function as f


class Interface(tk.Frame):
    """main Interface"""

    def __init__(self, **kwargs):
        tk.Frame.__init__(self, **kwargs)

        # design
        self.master.title("sudoku resolution")
        self.master.configure(bg=f.background_color)
        self.configure(bg=f.background_color)
        self.grid(sticky="")

        # list if the number variable of each little cell
        self.number_var_list = []
        # same list but with the data of each variable
        self.number_position_list = []
        self.init_grid()

        self.large_box_list = []
        self.row_list = []
        self.column_list = []

        self.ok_button = tk.Button(self, text="Ok", font=(
            "Helvetica Neue Arial sans-serif", 30, "bold"), command=self.check)
        self.ok_button.grid(column=1, row=3, pady=10)

        # label with the instructions
        self.instruction_label = tk.Label(self, text="enter the numbers\n of your sudoku to check\n if it is correct", font=(
            "Helvetica Neue Arial sans-serif", 15, "bold"), bg=f.background_color, fg="#f2f2f2")
        self.instruction_label.grid(column=0, row=3, pady=10)

        # display if there is an error
        self.error_label = tk.Label(self, text="Error", font=(
            "Helvetica Neue Arial sans-serif", 30, "bold"), fg="#ff0000", bg=f.background_color)

        # label to know if the sudoku is complete or not
        self.finished_label = tk.Label(self, text="Not complete", font=(
            "Helvetica Neue Arial sans-serif", 23, "bold"), fg="#ff0000", bg=f.background_color)

    def init_grid(self):
        """initialization of an empty sudoku grid
        we create menu options to add the numbers where we want
        we save the variable of each small box in nbr_var_list (all the variables of one big cell)
        and then we save nbr_var_list in self.number_var_list

        we'll have something like this :
        [[var0, var1, var2,         [var9, var10, var11,        [var18, var19, var20,
          var3, var4, var5,         var12, var13, var14,        var21, var22, var23,
          var6, var7, var8],        var15, var16, var17],       var24, var25, var26],

         [var27, var28, var29,      [var36, var37, var38,       [var45, var46, var47,
          var30, var31, var32,       var39, var40, var41,        var48, var49, var50,
          var33, var34, var35],      var42, var43, var44],       var51, var52, var53],

         [var54, var55, var56,      [var63, var64, var65,       [var72, var73, var74,
          var57, var58, var59,       var66, var67, var68,        var75, var76, var77,
          var60, var61, var62],      var69, var70, var71],       var78, var79, var80],
        """

        for i in range(3):
            for j in range(3):

                # creation of a big cell
                big_cell = tk.Frame(
                    self, width=500, height=500, borderwidth=1, bg=f.background_color)
                big_cell.grid(row=i, column=j, padx=4, pady=4)

                nbr_var_list = []
                for k in range(3):
                    for l in range(3):

                        # add little cells inside the big cell
                        little_cell = tk.Frame(
                            big_cell, width=30, height=30)
                        little_cell.grid(
                            row=k, column=l, padx=4, pady=4)

                        # add an OptionMenu in each little cells
                        number_var = tk.StringVar()
                        number_var.set("")
                        number = tk.OptionMenu(
                            little_cell, number_var, "", *f.number)
                        number.grid(ipadx=10, ipady=10, padx=3, pady=3)

                        # add the OptionMenu's variable inside nbr_var_list
                        nbr_var_list.append(number_var)

                # add nbr_var_list inside number_var_list
                self.number_var_list.append(nbr_var_list)

    def check(self):
        """When the button Ok is pressed
        check if the table got errors
        check if the table is complete
        """

        self.large_box_list, self.row_list, self.column_list = f.get_lists(
            self.number_var_list)
        error = f.check_if_error(self.large_box_list,
                                 self.row_list, self.column_list)

        self.instruction_label.grid_forget()
        if error:
            self.error_label.grid(column=0, row=3, pady=10)
        elif not error:
            self.error_label.grid_forget()

            finished = f.is_finished(self.large_box_list)

            if not finished:
                self.finished_label["fg"] = "#ff0000"
                self.finished_label["text"] = "not complete"
                self.finished_label.grid(column=2, row=3, pady=10)
            elif finished:
                self.finished_label["fg"] = "#00ff00"
                self.finished_label["text"] = "complete with success"
                self.finished_label.grid(column=2, row=3, pady=8)


if __name__ == '__main__':
    # we create our interface
    interface = Interface()
    interface.mainloop()
