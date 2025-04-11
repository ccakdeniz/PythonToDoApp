import json
import os
import helper_functions

TODO_FILE = "todos.json"


def load_todos():
    # check if file exist
    if not os.path.exists(TODO_FILE):
        # create a new file
        create_file()
        return []

    try:
        file = open(TODO_FILE, "r")
        return json.load(file)
    except:
        print("❗Something went wrong loading the file! New file will be created now.")
        create_file()
        return []


def create_file():
    save_todos([])
    print("✅File created!")


def save_todos(todos: list):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def list_todos(todos: list):
    if not todos:
        print("✅ No tasks! Add something.")
    else:
        for idx, todo in enumerate(todos, start=1):
            print(f"{idx}.", end=" ")
            helper_functions.print_todo(todo)


def add_todo(todos: list):
    todo = input("Todo to add: ").strip()
    try:
        todos.append({"title": todo, "done": False})
        save_todos(todos)
        print("✅Todo added!")
    except:
        print("❌Error while adding the todo")


def update_todo(todos: list):
    list_todos(todos)
    try:
        recToUpdate = int(input("Select record to update: "))-1
        newTitle = input("Enter the new title: ")
        todos[recToUpdate]['title'] = newTitle
        save_todos(todos)
        print(f"✅Todo updated! New title is: {newTitle}")
    except:
        helper_functions.invalid_selection()


def delete_todo(todos: list):
    list_todos(todos)
    try:
        recToDelete = int(input("Select record to delete: "))-1
        removed = todos.pop(recToDelete)
        save_todos(todos)
        print(f"✅Deleted: {removed['title']}")
    except:
        helper_functions.invalid_selection()


def toggle_todo(todos: list):
    list_todos(todos)
    try:
        recToToggle = int(
            input("Select record to toggle Complete/Incomplete: "))-1
        todos[recToToggle]['done'] = not todos[recToToggle]['done']
        save_todos(todos)
        print(f"✅ Toggled:", end=" ")
        helper_functions.print_todo(todos[recToToggle])
    except:
        helper_functions.invalid_selection()
