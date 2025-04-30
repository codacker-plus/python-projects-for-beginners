todos = []
while True:
    action = input("Add/View/Remove/Quit: ").lower()
    if action == 'add':
        task = input("Enter a task: ")
        todos.append(task)
    elif action == 'view':
        for i, task in enumerate(todos):
            print(f"{i+1}. {task}")
    elif action == 'remove':
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(todos):
            todos.pop(index)
    elif action == 'quit':
        break
