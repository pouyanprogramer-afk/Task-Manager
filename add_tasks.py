def Add_tasks(tasks):
    while True:
        print ("========== ADD TASKS ==========")
        print()
        
        task = input("Enter the task : ")
        print()

        tasks[task] = False

        print (f"The {task} task was successfully registered.")

        print()

        return tasks