
import functions


def menu():
    todos = functions.load_todos()
    while True:
        print("-"*50)
        print("📋To-Do Menu")
        print("-"*50)
        print("1. List")
        print("2. Add")
        print("3. Update")
        print("4. Delete")
        print("5. Toggle Completion")
        print("6. Exit")

        selectedOption = input("Select an option [1-6]: ").strip()
        if selectedOption == "1":
            functions.list_todos(todos)
            input("Press enter to continue...")  # Pause after listing
        elif selectedOption == "2":
            functions.add_todo(todos)
        elif selectedOption == "3":
            functions.update_todo(todos)
        elif selectedOption == "4":
            functions.delete_todo(todos)
        elif selectedOption == "5":
            functions.toggle_todo(todos)
        elif selectedOption == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌Invalid selection!")


if __name__ == "__main__":
    menu()
