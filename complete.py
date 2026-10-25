def complet_task(tasks):
    for task in tasks :
        print (f". {task}")

    print()
    print("========== COMLETE TASK ==========")
    print()

    copleted = input("whiche one did you coplete ? ")

    tasks[copleted] = True
    print()
    return tasks
