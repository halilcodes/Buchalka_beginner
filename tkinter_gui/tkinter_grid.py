import tkinter

window = tkinter.Tk()

window.title("Hello World!!")
window.geometry('640x480-8-200')

label = tkinter.Label(window, text='Hello World')
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(window)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(window)
rightFrame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(rightFrame, text='button1', pady=10)
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button3.grid(sticky='ew')

window.mainloop()
