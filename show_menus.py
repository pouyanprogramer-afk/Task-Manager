
def menus():

    print ("========== TASK MANAGER ==========")

    print("\n")


    menus = [
            "1 . Add Task",
            "2 . Show Tasks",
            "3 . Complete Task",
            "4 . Delete Task ",
            "5 . Exit"
        ]


    for menu in menus:

            print (menu)

    print ()

    choice = input("choice an option : ")

    print()

    return choice