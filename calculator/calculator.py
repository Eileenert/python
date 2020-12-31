import tkinter as tk


class Interface(tk.Frame):

    def __init__(self, window, **kwargs):
        tk.Frame.__init__(self, window,
                          background="#0d0d0d", borderwidth=5, padx=75, pady=25, **kwargs)

        self.grid(sticky="")

        # display area
        self.expression = ""  # the expression to resolve
        self.var_text = tk.StringVar()  # expression displayed
        self.display_area = tk.Entry(
            self, textvariable=self.var_text, font=("Helvetica", 15))  # display area
        self.display_area.grid(columnspan=6, ipadx=350,
                               ipady=15, pady=10, padx=20)

        # buttons
        # buttons number
        self.button0 = tk.Button(
            self, text=0, height=5, width=15,  font=("Helvetica", "10", "bold"), command=lambda: self.press("0"))
        self.button0.grid(row=4, column=0, pady=5, padx=5)

        self.button1 = tk.Button(
            self, text=1, height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("1"))
        self.button1.grid(row=3, column=0, pady=5, padx=5)

        self.button2 = tk.Button(
            self, text=2, height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("2"))
        self.button2.grid(row=3, column=1, pady=5, padx=5)

        self.button3 = tk.Button(
            self, text=3, height=5, width=15,  font=("Helvetica", "10", "bold"), command=lambda: self.press("3"))
        self.button3.grid(row=3, column=2, pady=5, padx=5)

        self.button4 = tk.Button(
            self, text=4, height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("4"))
        self.button4.grid(row=2, column=0, pady=5, padx=5)

        self.button5 = tk.Button(
            self, text=5, height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("5"))
        self.button5.grid(row=2, column=1, pady=5, padx=5)

        self.button6 = tk.Button(
            self, text=6, height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("6"))
        self.button6.grid(row=2, column=2, pady=5, padx=5)

        self.button7 = tk.Button(
            self, text=7, height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("7"))
        self.button7.grid(row=1, column=0, pady=5, padx=5)

        self.button8 = tk.Button(
            self, text=8, height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("8"))
        self.button8.grid(row=1, column=1, pady=5, padx=5)

        self.button9 = tk.Button(
            self, text=9, height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("9"))
        self.button9.grid(row=1, column=2, pady=5, padx=5)

        # point button
        self.button_point = tk.Button(
            self, text=".", height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("."))
        self.button_point.grid(row=4, column=1, pady=5, padx=5)

        # percent button
        self.button_percent = tk.Button(
            self, text="%", height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("%"))
        self.button_percent.grid(row=1, column=5, pady=5, padx=5)

        # division button
        self.button_division = tk.Button(
            self, text="÷", height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("÷"))
        self.button_division.grid(row=3, column=5, pady=5, padx=5)

        # multiplication button
        self.button_multiplication = tk.Button(
            self, text="×", height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("×"))
        self.button_multiplication.grid(row=4, column=5, pady=5, padx=5)

        # substraction button
        self.button_substraction = tk.Button(
            self, text="-", height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("-"))
        self.button_substraction.grid(row=3, column=4, pady=5, padx=5)

        # addition button
        self.button_addition = tk.Button(
            self, text="+", height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("+"))
        self.button_addition.grid(row=4, column=4, pady=5, padx=5)

        # AC button (clear all)
        self.button_AC = tk.Button(
            self, text="AC", height=5, width=15, font=("Helvetica", "10", "bold"), command=self.clear_all)

        # left parenthesis button
        self.button_left_parenthesis = tk.Button(
            self, text="(", height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press("("))
        self.button_left_parenthesis.grid(row=2, column=4, pady=5, padx=5)

        # right parenthesis button
        self.button_right_parenthesis = tk.Button(
            self, text=")", height=5, width=15, font=("Helvetica", "10", "bold"), command=lambda: self.press(")"))
        self.button_right_parenthesis.grid(row=2, column=5, pady=5)

        # equal button
        self.button_equal = tk.Button(self, text="=", height=5, width=15, font=(
            "Helvetica", "10", "bold"), command=self.equal_press)
        self.button_equal.grid(row=4, column=2, pady=5, padx=5)

        # back button
        self.button_back = tk.Button(
            self, text="<--", height=5, width=15, font=("Helvetica", "10", "bold"), command=self.press_back)
        self.button_back.grid(row=1, column=4, pady=5)

    def press(self, number):
        # When we press a button except the equal, back and the AC
        # we modify the expression and then display it
        self.expression += number
        self.var_text.set(self.expression)

    def equal_press(self):
        # when button_equal is pressed
        # we replace expressions not recognizable by eval
        self.expression = self.expression.replace("÷", "/")
        self.expression = self.expression.replace("%", "/100")
        self.expression = self.expression.replace("×", "*")

        # we remove the back button
        self.button_back.grid_forget()
        # we add the AC button
        self.button_AC.grid(row=1, column=4, pady=5, padx=5)

        try:
            # resolve the expression
            total = str(eval(self.expression))
            # display the total of the expression
            self.var_text.set(total)

        except:
            self.var_text.set("ERROR")

        finally:
            # we reset the expression
            self.expression = ""

    def clear_all(self):
        # When button_AC is pressed
        self.var_text.set("")

        # we remove the AC button
        self.button_AC.grid_forget()
        # we add the back button
        self.button_back.grid(row=1, column=4, pady=5, padx=5)

    def press_back(self):
        # when button_back is pressed

        # we remove the last caractere of our expression
        self.expression = self.expression[:-1]
        self.var_text.set(self.expression)


if __name__ == '__main__':
    # we create our interface
    window = tk.Tk()

    window.configure(bg="#0d0d0d")
    window.title("Calculator")

    interface = Interface(window)

    interface.mainloop()
    interface.destroy()
