import tkinter as tk


def draw_pixel(event):
    canvas.create_line((event.x, event.y), (event.x+1, event.y), fill="red")


def draw_circle(x, y, ray, color):
    canvas.create_oval(x-ray, y-ray, x+ray, y+ray, fill=color)


def draw_new_circle(event):
    if (event.x < 250):
        draw_circle(event.x, event.y, 50, "blue")
    else:
        draw_circle(event.x, event.y, 50, "red")


racine = tk.Tk()
canvas = tk.Canvas(racine, width=500, height=500, bg="black")
ligne = canvas.create_line((250, 0), (250, 500), fill="white")

canvas.bind("<Button-1>", draw_new_circle)

canvas.grid()

racine.mainloop()
