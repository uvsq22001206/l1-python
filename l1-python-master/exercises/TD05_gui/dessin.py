import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 900, 400
root = tk.Tk()
root.title("Mon Dessin")
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black", relief=tk.GROOVE, bd=1)

couleur = "blue"
figure = []


def choix_couleur():
    global couleur
    couleur = input("Choisir une couleur")


def create_button(text, fonction, i, j):
    bouton = tk.Button(text=text, command=fonction, font=("Helvetica", "30"), activeforeground="red", activebackground="black", padx=100)
    bouton.grid(column=i, row=j)
    return bouton


def dessine_cercle():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint(0, CANVAS_HEIGHT-100)
    figure.append(canvas.create_oval(x, y, x + 100, y + 100, fill=couleur))


def dessine_carre():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint(0, CANVAS_HEIGHT-100)
    figure.append(canvas.create_rectangle(x, y, x + 100, y + 100, fill=couleur))


def dessine_croix():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint(0, CANVAS_HEIGHT-100)
    figure.append(canvas.create_line(x, y, x + 100, y + 100, fill=couleur))
    figure.append(canvas.create_line(x+100, y, x, y+100, fill=couleur))


def undo():
    if len(figure) == 0:
        return
    if canvas.type(figure[-1]) == "line":
        canvas.delete(figure[-2])
        del figure[-2]
    canvas.delete(figure[-1])
    del figure[-1]


cercle = create_button("Cercle", dessine_cercle, 0, 1)
carre = create_button("Carré", dessine_carre, 0, 2)
croix = create_button("Croix", dessine_croix, 0, 3)
choix = create_button("Choisir une couleur", choix_couleur, 1, 0)
undo = create_button("Undo", undo, 0, 0)


canvas.grid(column=1, row=1, rowspan=3)
canvas.create_oval(150, 150, 250, 250)
root.mainloop()
