import sys
import os


def save_tasks(task_list):
    name_file = os.path.join(get_dir(), "saves.txt")
    with open(name_file, "w") as f:
        for task in task_list:
            f.writelines(f"{task}\n")

def save_desc(desc_list):
    name_file = os.path.join(get_dir(), "desc_save.txt")
    with open(name_file, "w") as f:
        for desc in desc_list:
            f.writelines(f"{desc}\n")

def get_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def ensure_save_files(file_name: str):
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("")