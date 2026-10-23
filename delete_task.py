def delete(tasks):
    print("========== DELETE TASK ==========")
    print()

    for task in tasks :
        print (f". {task}")

    deleted = input("which one should i delete ? ")

    tasks.pop(deleted)

    return
