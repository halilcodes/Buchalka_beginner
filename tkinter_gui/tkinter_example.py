import os
import tkinter
import tkinter as tk
import os

window = tk.Tk()
window.title('Grid Demo')
window.geometry('760x640-80+150')
window['padx'] = 8

window.columnconfigure(0, weight=100)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1000)
window.columnconfigure(3, weight=600)
window.columnconfigure(4, weight=1000)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=10)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=3)
window.rowconfigure(4, weight=3)

label = tk.Label(text='Tkinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)

# List Box and Scroll Bar
scrollBar = tk.Scrollbar(window, orient='vertical')
listBox = tk.Listbox(window, width=20, height=20, yscrollcommand=scrollBar.set, font=("Helvetica", 12))
scrollBar.config(command=listBox.yview)

listBox.grid(row=1, column=0, rowspan=2, sticky='nsew')
scrollBar.grid(row=1, column=1, rowspan=2, sticky='nsw')
listBox.config(border=2, relief='sunken')
for zone in os.listdir('\\Windows\\System32'):
    listBox.insert(tk.END, zone)

# Frame and creation of Radio Buttons
optionFrame = tk.LabelFrame(window, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tk.IntVar()
rbValue.set(1)  # initial value setting
radio1 = tk.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tk.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3 = tk.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# widget to display the result
resultLabel = tk.Label(window, text='Result')
resultLabel.grid(row=2, column=2, sticky='sw')
result = tk.Entry(window)
result.grid(row=3, column=2, sticky='new')

# frame for the time spinners
timeFrame = tk.LabelFrame(window, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')

# time spinners
hourSpinner = tk.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tk.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tk.Spinbox(timeFrame, width=2, from_=0, to=59)

hourSpinner.grid(row=0, column=0)
tk.Label(timeFrame, text=': ').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tk.Label(timeFrame, text=': ').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

# frame for the date spinners
dateFrame = tk.Frame(window)
dateFrame.grid(row=4, column=0, sticky='new')
# date labels
dayLabel = tk.Label(dateFrame, text='Day')
monthLabel = tk.Label(dateFrame, text='Month')
yearLabel = tk.Label(dateFrame, text='Year')

dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')
# date spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Aug', 'Sep',
                                                        'Oct', 'Nov', 'Dec'))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=1900, to=2050)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# ok and cancel buttons
okButton = tk.Button(window, text='OK')
cancelButton = tk.Button(window, text='Cancel', command=window.quit)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

window.mainloop()

print(rbValue.get())
