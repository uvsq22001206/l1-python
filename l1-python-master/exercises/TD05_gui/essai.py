import tkinter as tk
import random


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_drop(x, y, ray=50):
    if ray == 0:
        return
    draw_circle(x, y, ray, get_color(0, 0, 255-ray*5))
    canvas.after(3, lambda: draw_drop(x, y, ray-1))


def draw_circle(x, y, ray, color):
    canvas.create_oval(x-ray, y-ray, x+ray, y+ray, fill=color)


def rain():
    draw_drop(random.randint(0, 500), random.randint(0, 500))
    canvas.after(20, rain)


racine = tk.Tk()
canvas = tk.Canvas(racine, width=500, height=500, bg="black")
canvas.grid()
rain()
racine.mainloop()
