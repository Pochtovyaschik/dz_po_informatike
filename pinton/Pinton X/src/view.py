from ui.Interface import Interface

def start_app():
    app = Interface()
    app.show_menu()
    app.root.mainloop()
