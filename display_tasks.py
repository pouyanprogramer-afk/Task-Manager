def Display_task(tasks):
    for task, status in tasks.items():

        if status == True:
            print ("✓", task)

        if status == False:
            print ("✗", task)

        