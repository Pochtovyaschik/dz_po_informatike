import tkinter as tk

x = 0
y = 0
last_x = 0
last_y = 0

def set_vertex(eventorigin):
    global x, y, last_x, last_y
    y = eventorigin.y
    x = eventorigin.x
    line = tk.Canvas.create_line(draw, last_x, last_y, x, y)
    oval = tk.Canvas.create_oval(draw, x-15, y-15, x+15, y+15, fill='red', outline='black')
    last_x = x
    last_y = y
    return oval, line

root = tk.Tk()
draw = tk.Canvas(root, bg="white", width=470, height=470)
draw.pack()
root.geometry("470x470")
root.bind("<Button-1>", set_vertex)
root.mainloop()