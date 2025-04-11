def invalid_selection():
    print("❗Invalid selection")


def print_todo(todo):
    print(f"{'✅' if todo['done'] else '⬜'} {todo['title']}")
