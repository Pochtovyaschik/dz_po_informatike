
def save_tasks(task_list):
    name_file = "saves.txt"
    with open(name_file, "w") as f:
        for task in task_list:
            f.writelines(f"{task}\n")

def save_desc(desc_list):
    name_file = "desc_save.txt"
    with open(name_file, "w") as f:
        for desc in desc_list:
            f.writelines(f"{desc}\n")