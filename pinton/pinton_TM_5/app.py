
from methods import show
from methods import confirm
from utility import save_tasks
from utility import save_desc

def load_saved_task():
    task_out = []
    name_file = "saves.txt"
    with open(name_file, "r") as f:
        for line in f:
            task_out.append(line.strip())
    return task_out

def load_saved_desc():
    desc_out = []
    name_file = "desc_save.txt"
    with open(name_file, "r") as f:
        for line in f:
            desc_out.append(line.strip())
    return desc_out


tasks = load_saved_task()
tasks_content = load_saved_desc()
choice = 0
task_choice = ""
run_ = True

def main():
    global run_
    while run_:
        print ("Select managing option: \n" \
        "1. View tasks and descriptions \n" \
        "2. Add task and description \n" \
        "3. Rename task \n" \
        "4. Remove task \n" \
        "5. Exit")
        choice = input()
        match choice:
            case "1":
                show(tasks)
                if input("Press ENTER to continue, press Q to view descriptions") == "q":
                    show(tasks_content)
                    input("Press ENTER to continue")
                else:
                    pass
            case "2":
                tasks.append(input("enter task's name: "))
                save_tasks(tasks)
                tasks_content.append(input("enter task's content: "))
                save_desc(tasks_content)
                print("added task: ", tasks[len(tasks)-1], "with description: ", tasks_content[len(tasks_content)-1])
            case "3":
                if (len(tasks) > 0):
                    show(tasks)
                    print(f"\n select task (number 1-{len(tasks)}):")
                    task_choice = int(input())
                    tasks[task_choice - 1] = input("select new name: ")
                    tasks_content[task_choice - 1] = input("select new content: ")
                    save_desc(tasks_content)
                    save_tasks(tasks)
                    task_choice = 0
                else:
                    print("no tasks found!")
            case "4":
                if (len(tasks) > 0):
                    show(tasks)
                    print(f"\n select task (number 1-{len(tasks)}):")
                    task_choice = int(input())
                    if confirm(input("Are you sure? (Y/N)")):
                        tasks.pop(task_choice - 1)
                        tasks_content.pop(task_choice - 1)
                    else:
                        pass
                    task_choice = 0
                    save_tasks(tasks)
                    save_desc(tasks_content)
                else:
                    print("no tasks found!")
            case "5":
                run_ = not(confirm(input("Are you sure? (Y/N)")))
            case _:
                pass
    print("Goodbye")
    