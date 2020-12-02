import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
root = tk.Tk()
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
x = CANVAS_WIDTH / 2
y1 = CANVAS_HEIGHT
y2 = 0

# canvas.create_line(x0, y, x1, y)
canvas.create_line(x, y1, x, y2)

# canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50)
# canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
canvas.create_oval(x - 50, y2 + 50, x + 50, y2 - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)

# Fin de votre code

canvas.grid()
root.mainloop()
