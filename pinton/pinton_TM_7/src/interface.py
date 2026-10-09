import tkinter as tk

root = tk.Tk()

root.geometry('500x500')
root.iconbitmap('../assets/ssss.ico')
root.title('Pinton TM')

def insert_value():
    pass

def init():
    frame_top = tk.Frame(root, width=100, height=100, background='light blue')
    frame_bottom_left = tk.Frame(root, width=350, height=100, background='blue')
    frame_bottom_right = tk.Frame(root, width=150, height=100, background='light blue')
    return [frame_top.pack(side="top"), frame_bottom_left, frame_bottom_right.pack(side="right")]

def gui():
    frame_bottom_left = init()
    frame_bottom_left[1].pack(side="left", padx=15, pady=15)
    col = 0
    row = 0
    for button in range(10):
        button = tk.Button(frame_bottom_left[1], text=button, command=insert_value, height=5, width=10)
        button.grid(column=col, row=row)
        col += 1
        if col == 3:
            col = 0
            row += 1

gui()


root.mainloop()