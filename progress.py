def calculate_progress(tasks):

    total = 0

    for task in tasks:
        total += 1

    completed_items = 0 

    for task, status in tasks.items():
        if status == True:
            completed_items +=1

    progress = completed_items / total * 100

    print (progress)

    return