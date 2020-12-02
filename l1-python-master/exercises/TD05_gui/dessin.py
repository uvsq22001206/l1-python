import tkinter as tk
import random


def cercle(x1=random.randint(0, 400), y1=random.randint(0, 400)):
    canvas.create_oval((x1, y1, x1 + 100, y1 + 100), fill="blue")


root = tk.Tk()
root.title("Mon dessin")
button1 = tk.Button(root, text="choisir une couleur", font=("helvetica", "26"))
button2 = tk.Button(root, text="cercle", font=("helvetica", "26"), command=cercle)
button3 = tk.Button(root, text="carré", font=("helvetica", "26"))
button4 = tk.Button(root, text="croix", font=("helvetica", "26"))
button1.grid(column=1, row=0)
button2.grid(column=0, row=1)
button3.grid(column=0, row=2)
button4.grid(column=0, row=3)
canvas = tk.Canvas(root, bg="black", height=500, width=500)  # relief=tk.GROOVE, # bd=10 bordure
canvas.grid(column=1, row=1, rowspan=3)

root.mainloop()
