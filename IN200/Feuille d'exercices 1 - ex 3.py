import tkinter as tk

root = tk.Tk()
root.title("Exercice 3")

HEIGHT, WIDTH = 500, 500

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
canvas.grid(row=0)

redemarrer = tk.Button(root, text="Redémarrer")
redemarrer.grid(row=1)

canvas.create_line(WIDTH/3, 0, WIDTH/3, HEIGHT, fill="white")
canvas.create_line(2*WIDTH/3, 0, 2*WIDTH/3, HEIGHT, fill="white")


def croix(event):
    if event.x < WIDTH/3:
        canvas.create_line(event.x-25, event.y-25, event.x+25, event.y+25, fill="blue")
        canvas.create_line(event.x-25, event.y+25, event.x+25, event.y-25, fill="blue")


canvas.bind("<Button-1>", croix)


def rectangle(event):
    if WIDTH/3 < event.x < 2*WIDTH/3:
        canvas.create_rectangle(event.x-25, event.y-25, event.x+25, event.y+25, fill="green")


canvas.bind("<Button->", rectangle)
root.mainloop()
