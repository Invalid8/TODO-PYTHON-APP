from time import sleep

from todoFunctions import *

not_finished = True

def StartTodoApp():
    AddWaitAnimation(0.5)
    WelcomeMessage()

    while not_finished:
        AddWaitAnimation(0.3)
        WorkOnChoice(ChooseOption())

def EndTodo():
    global not_finished
    not_finished = False

def WelcomeMessage():
    welcome_msg = """
        Welcome to Daniel Todo Python
        Application.

        Functions like:
        1. Add a todo
        2. Edit a todo
        3. Delete a todo
        4. View todos
        5. Clear todos
        6. EXIT
        """
    print(welcome_msg)

def ChooseOption():
    print("""\nYou can:
    1. Add a todo
    2. Edit a todo
    3. Delete a todo
    4. View todos
    5. Clear todos
    6. EXIT
    """)

    user_choice = input("What Do you want to do (1,2,3,4,5,6)? ")
    while user_choice not in ["1","2","3","4", "5", "6"]:
        print("incorrect input")
        user_choice = input("What Do you want to do (1,2,3,4)? ")

    return user_choice

def WorkOnChoice(value):
    if value == "1":
        inputData()
    elif value == "2":
        editATodo()
    elif value == "3":
        deleteATodo()
    elif value == "4":
        viewAllToDo()
    elif value == "5":
        clearTodo()
    else:
        AddWaitAnimation(0.3)
        print("Thanks for using the PYTHON TODO APP")
        EndTodo()

def AddWaitAnimation(secs):
    print("Loading ",end="")
    for i in range(3):
        print(".", end=" ")
        sleep(secs)

    print("\n")
