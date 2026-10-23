from show_menus import menus
from add_tasks import Add_tasks
from show_tasks import show_tasks
from progress import calculate_progress
from comlete import complet_task
from display_tasks import Display_task
from delete_task import delete

tasks = {}


while True:
        choice = menus()

        if choice == "1":

            Add_tasks(tasks)

            continue
        if choice == "2":
            show_tasks(tasks)

            continue

        if choice == "3":
            complet_task(tasks)

            Display_task(tasks)

            calculate_progress(tasks)

            continue

        if choice == "4":

            delete(tasks)

            continue

        if choice == "5":
             break