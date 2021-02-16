import tkinter as tk

root = tk.Tk()
root.title("Exercice 1")

canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.grid(row=0)

bouton_recommencer = tk.Button(root, text="Recommencer")
bouton_recommencer.grid(row=1)
cpt = 0


def couleur_rectangle(event):
    global cpt
    if 100 < event.x < 300 and 100 < event.y < 200:
        cpt += 1
        if cpt % 2 == 0:
            canvas.create_rectangle(100, 100, 300, 200, fill="red")
        else:
            canvas.create_rectangle(100, 100, 300, 200, fill="blue")


canvas.create_rectangle(100, 100, 300, 200, fill="red")

canvas.bind("<Button-1>", couleur_rectangle)
root.mainloop()
