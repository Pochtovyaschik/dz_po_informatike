def show(show):
    print("-"*10)
    for i in show:
        print(i)
    print("-"*10)

def confirm(option):
    if option.startswith("y") or option.startswith("Y"):
        return True
    else:
        return False