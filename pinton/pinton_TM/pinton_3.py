"""
Pinton task manager
ver 2 Alpha

ver 1
- Pinton ceated
- Task viewing added
- Adding tasks added

ver 2
- More task managing options

ver 3
- saving and loading tasks

"""

def show_tasks():
    print("-"*10)
    for i in tasks:
        print(i)
    print("-"*10)

def confirm(option):
    if option.startswith("y") or option.startswith("Y"):
        return True
    else:
        return False

def load_saved_task():
    task_out = []
    name_file = "saves.txt"
    with open(name_file, "r") as f:
        for line in f:
            task_out.append(line.strip())
    return task_out

def save_tasks(task_list):
    name_file = "saves.txt"
    with open(name_file, "w") as f:
        for task in task_list:
            f.writelines(f"{task}\n")

tasks = load_saved_task()
tasks_content = []
choice = 0
task_choice = ""
run_ = True

def main():
    global run_
    while run_:
        print ("Select managing option: \n" \
        "1. View tasks \n" \
        "2. Add task \n" \
        "3. Rename task \n" \
        "4. Remove task \n" \
        "5. Exit")
        choice = input()
        match choice:
            case "1":
                show_tasks()
                input("Press ENTER to continue")
            case "2":
                tasks.append(input("enter task's name: "))
                save_tasks(tasks)
                print("added task: ", tasks[len(tasks)-1])
            case "3":
                if (len(tasks) > 0):
                    show_tasks()
                    print(f"\n select task (number 1-{len(tasks)}):")
                    task_choice = int(input())
                    tasks[task_choice - 1] = input("select new name: ")
                    task_choice = 0
                else:
                    print("no tasks found!")
            case "4":
                if (len(tasks) > 0):
                    show_tasks()
                    print(f"\n select task (number 1-{len(tasks)}):")
                    task_choice = int(input())
                    if confirm(input("Are you sure? (Y/N)")):
                        tasks.pop(task_choice - 1)
                    else:
                        pass
                    task_choice = 0
                    save_tasks(tasks)
                else:
                    print("no tasks found!")
            case "5":
                run_ = not(confirm(input("Are you sure? (Y/N)")))
            case _:
                pass
    print("Goodbye")
    
print("Welcome to Pinton Task Manager")
main()