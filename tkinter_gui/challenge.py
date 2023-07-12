# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter as tk
import tkinter.messagebox


def btn_click(char):
    if char == "=":
        if resultBox.get():
            try:
                answer = (str(eval(resultBox.get())))
            except SyntaxError:
                tk.messagebox.showerror("Error", "Invalid calculation. ")
            except ZeroDivisionError:
                tk.messagebox.showerror("Error", "Cannot divide by zero. ")
            else:
                resultBox.delete(0, tk.END)
                resultBox.insert(0, answer)
    if char == 'C':
        resultBox.delete(0, tk.END)
    elif char == "CE":
        resultBox.delete(len(resultBox.get()) - 1, tk.END)
    else:
        resultBox.insert(tk.END, char)


window = tk.Tk()
window.geometry('250x250')
window.title('Calculator')
window.minsize(width=200, height=200)
window['padx'] = 10
window['pady'] = 10

# result box
resultBox = tk.Entry(window, width=25)
resultBox.grid(row=0, column=0, columnspan=4, sticky='nsew')

# C and CE
cButton = tk.Button(window, text='C')
ceButton = tk.Button(window, text='CE')
cButton.grid(row=1, column=0, sticky='ew')
ceButton.grid(row=1, column=1, sticky='ew')

# numbers and buttons
zeroButton = tk.Button(window, text='0')
zeroButton.grid(row=5, column=0, sticky='ew')
num = 1
for row in range(4, 1, -1):
    for col in range(0, 3):
        print(row, col)
        numButton = tk.Button(window, text=str(num), command=lambda char=str(num): btn_click(char))
        numButton.grid(row=row, column=col, sticky='ew')
        num += 1

eqButton = tk.Button(window, text='=')
eqButton.grid(row=5, column=1, columnspan=2, sticky='ew')

for row, sign in enumerate(["+", "-", "*", "/"]):
    print(row, sign)
    signButton = tk.Button(window, text=sign)
    signButton.grid(row=row+2, column=3, sticky='ew')


window.mainloop()
