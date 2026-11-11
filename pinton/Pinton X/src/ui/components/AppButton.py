import tkinter as tk

class AppButton(tk.Button):
    def __init__(self, master, status, text, command):
        super().__init__(master, width=20, height=2, text=text, command=command, font=("Gothic", 10))
        self.status = status
        self.settings()
    def settings(self):
        if self.status == "primary":
            self.configure(background='white', foreground="white")
        elif self.status == "secondary":
            self.configure(background='grey', foreground="white")
