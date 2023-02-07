from TODO_LIST import FAQ


def inputData():
    raw_data = ""
    while len(raw_data) < 1:
        raw_data = input("Add A Todo: ")

    FAQ.append( {"id": len(FAQ) + 1, "data": raw_data})


def editATodo():
    if len(FAQ) <= 0:
        print("The Todo List is empty")
    else:
        user_id = input("Input the ID of the todo: ")
        while True:
            if user_id.isnumeric() and (int(user_id) < len(FAQ) or int(user_id) > 0):
                user_id = int(user_id)
                break
            elif not user_id.isnumeric():
                print("Error use number")
                user_id = input("Input the ID of the todo: ")
            elif int(user_id) > len(FAQ) or int(user_id) <= 0:
                print( f"Todo ID-{user_id} does not exit")
                user_id = input("Input the ID of the todo: ")

        print(f"id: {user_id}, data: {FAQ[user_id - 1]['data']}")
        edit_todo = input(f"Editing todo ID-{user_id} text: ")
        while len(edit_todo) < 1:
            edit_todo = input(f"Editing todo ID-{user_id} text: ")

        FAQ[user_id - 1]["data"] = edit_todo


def deleteATodo():
    if len(FAQ) == 0:
        print("The Todo List is empty")
    else:
        user_id = input("Input the ID of the todo: ")
        while True:
            if user_id.isnumeric() and (int(user_id) < len(FAQ) or int(user_id) > 0):
                user_id = int(user_id)
                break
            elif not user_id.isnumeric():
                print("Error use number")
                user_id = input("Input the ID of the todo: ")
            elif int(user_id) > len(FAQ) or int(user_id) <= 0:
                print(f"Todo ID-{user_id} does not exit")
                user_id = input("Input the ID of the todo: ")

        answer = input(f"Are you sure you want to delete todo ID-{user_id} 😢 (y / n)? ")
        while answer not in ['y', 'yes', "y".upper(), "yes".upper(), "Yes", 'n', 'no', "n".upper(), "no".upper(), "No"]:
            print("Error use yes or no")
            answer = input(f"Are you sure you want to delete todo ID-{user_id} 😢 (y / n)? ")

        if answer in ["y", "yes", "y".upper(), "yes".upper(), "Yes"]:
            FAQ.remove(FAQ[user_id - 1])
        elif answer in ["n", "no", "n".upper(), "no".upper(), "No"]:
            print("Better 😂😍")


def viewAllToDo():
    print(FAQ)


def clearTodo():
    if len(FAQ) <= 0:
        print("The Todo List is empty")
    else:
        answer = input("Are you sure you want to clear all todos😢?(y / n) ")
        while answer not in ['y', 'yes', "y".upper(), "yes".upper(), "Yes", 'n', 'no', "n".upper(), "no".upper(), "No"]:
            print("Error use yes or no")
            answer = input("Are you sure you want to clear all todos😢 (y / n)? ")

        if answer in ["y", "yes", "y".upper(), "yes".upper(), "Yes"]:
            FAQ.clear()
        elif answer in ["n", "no", "n".upper(), "no".upper(), "No"]:
            print("Better 😂😍")
