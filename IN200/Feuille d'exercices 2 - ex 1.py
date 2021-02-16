import tkinter as tk

root = tk.Tk()

canevas = tk.Canvas(root, height=400, width=600, bg="black")
demarrer = tk.Button(root, text="Démarrer")
canevas.grid(row=0)
demarrer.grid(row=1)


def creer_balle():
    canevas.create_oval(280, 180, 320, 220, fill="blue")


balle = creer_balle()

root.mainloop()
