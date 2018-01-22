toDoFile =

toDoList = ""

toDoItem = input("Enter a to-do list item: ")

while toDoItem != "exit":
    toDoList = toDoList + toDoItem + "\n"
    toDoItem = input("Enter a to-do list item: ")
    
