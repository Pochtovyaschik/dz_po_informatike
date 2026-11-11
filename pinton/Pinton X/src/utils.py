
import sys
import os

def check_confirm(action: str):
    confirm = input("Are you sure? (Y/N): ").strip().lower()  
    if confirm == "y" or confirm == "Y":
        print(action)
        return True
    else:
        print("отмена")
        return False

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def insure_save_file(name_file: str):
    if not os.path.exists(name_file):
        with open(name_file, "w") as f:
            f.write("")
