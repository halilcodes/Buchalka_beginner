import math
import tkinter as tk


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, -x, y)
        plot(page, x, y)


def circle(page, radius, g, h):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline='red', width=2)
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
    #     print("x: ", x, "y: ", y)
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(palette):
    palette.update()
    x_origin = palette.winfo_width() / 2
    y_origin = palette.winfo_height() / 2
    palette.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    palette.create_line(-x_origin, 0, x_origin, 0, fill='black')
    palette.create_line(0, y_origin, 0, -y_origin, fill='black')


def plot(palette, x_line, y_line):
    palette.create_line(x_line, -y_line, x_line+1, -y_line-1, fill='red', width=2)


window = tk.Tk()

window.title('Parabola')
window.geometry("640x480+2600+50")

canvas = tk.Canvas(window, width=640, height=480)
canvas.grid(row=0, column=0)
draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100)

window.mainloop()
