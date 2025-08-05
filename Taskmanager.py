print("Welcome to To-Do List")

while True:
    print("\n1. View\n2. Add\n3. Remove\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        f = open("tasks.txt", "r")
        tasks = f.read().splitlines()
        f.close()
        if tasks:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        else:
            print("No tasks.")

    elif choice == "2":
        task = input("New task: ")
        f = open("tasks.txt", "a")
        f.write(task + "\n")
        f.close()
        print("Task added.")

    elif choice == "3":
        f = open("tasks.txt", "r")
        tasks = f.read().splitlines()
        f.close()
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        num = int(input("Task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            f = open("tasks.txt", "w")
            for t in tasks:
                f.write(t + "\n")
            f.close()
            print("Task removed.")
        else:
            print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")