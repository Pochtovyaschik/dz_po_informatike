import tkinter as tk

'''
calculator = rabotayet
proizvoditelnost = horoshaya
funkciy = mnogo
polzovateley = mnogo
heyterov = net
'''


root = tk.Tk()

root.geometry('500x500')
root.iconbitmap('../assets/ssss.ico')
root.title('Pinton Calc')

#Спасибо Алимке за отдолженный код

lable = tk.Label(root, width=250, height=5, background="lightblue", anchor="e", font=("Gothic", 14))
lable.pack(padx=10, pady=10)

result = ""


def insert_value(value):
    global result
    operators = ["+", "-", "*", "/", "%"]
    if value == "=":
        maths()
        return
    if len(result) > 0 and result[-1] in operators and value in operators:
        result = result[:-1] + value
    else:
        if len(result) == 0 and value in operators:
            if value == "-":
                result += value
            else:
                return
        else:
            result += value

    lable.config(text=result)
    print(result)


def maths():
    global result
    try:
        out = str(eval(result))
        lable.config(text=out)
        result = out

    except Exception:
        lable.config(text="Ошибка")
        result = ""


def init():
    frame_top = tk.Frame(root, width=350, height=100, background='blue')
    frame_bottom_left = tk.Frame(root, width=300, height=350, background='blue')
    frame_bottom_right = tk.Frame(root, width=100, height=350, background='lightblue')
    return [frame_top, frame_bottom_left, frame_bottom_right]


def gui():
    frames = init()
    frames[1].pack(side="left", padx=10, pady=15)
    frames[2].pack(side="right", padx=10, pady=15)
    col = 0
    row = 0
    for step in range(10):
        button = tk.Button(frames[1], text=step, width=8, height=4, command=lambda value=str(step): insert_value(value))
        button.grid(row=row, column=col)
        col += 1
        if col == 3:
            col = 0
            row += 1
    operations = ["+", "-", "*", "/", "="]
    for step in range(len(operations)):
        op = operations[step]
        button = tk.Button(frames[2], text=op, width=7, height=3, command=lambda value=op: insert_value(value))
        button.grid(row=step, column=1)


gui()



root.mainloop()