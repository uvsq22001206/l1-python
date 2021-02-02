# CC du 9/01/2021 11h

import tkinter as tk
root = tk.Tk()
root.title("FETRE Cécile")

HEIGHT, WIDTH = 550, 550
canvas = tk.Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid(row=0)

figure = []


def undo():
    canvas.delete(figure)


redemarrer = tk.Button(root, text="Redémarrer", font=("Helvetica", "30"), command=undo)
redemarrer.grid(row=1)

canvas.create_line((0, HEIGHT/3), (WIDTH, HEIGHT/3), fill="white")
canvas.create_line((0, 2*HEIGHT/3), (WIDTH, 2*HEIGHT/3), fill="white")


def croix(event):
    if event.y < HEIGHT/3:
        figure.append(canvas.create_line(event.x-25, event.y-25, event.x+25, event.y+25, fill="red"))
        figure.append(canvas.create_line(event.x-25, event.y+25, event.x+25, event.y-25, fill="red"))


def carre(event):
    if event.y > HEIGHT/3 and event.y < 2*HEIGHT/3:
        figure.append(canvas.create_rectangle((event.x-25, event.y-25), (event.x+25, event.y+25), fill="red"))


def cercle(event):
    if event.y > 2*HEIGHT/3:
        figure.append(canvas.create_oval((event.x-25, event.y-25), (event.x+25, event.y+25), fill="red"))


canvas.bind("<Button-1>", croix)
canvas.bind("<Button-1>", carre)
canvas.bind("<Button-1>", cercle)

root.mainloop()
