import tkinter as tk

root = tk.Tk()
Height = 500
Width = 500
color = ["blue", "green", "black", "yellow", "magenta", "red"]
canvas = tk.Canvas(root, bg="black", heigh=Height, width=Width)
canvas.grid()

canvas.create_oval((0, 0, Height, Width), fill="blue")
canvas.create_oval((10, 10, Height - 10, Width - 10), fill="green")
root.mainloop()
