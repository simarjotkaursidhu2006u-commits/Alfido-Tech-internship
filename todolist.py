tasks = []  

while True:
    print("      TO-DO LIST     ")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    
    choice =int(input("Enter your choice between 1-4"))

    if choice == 1:
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task '{task}' added.")
    
    elif choice == 2:
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print("Task not found.")
    
    elif choice == 3:
        if tasks:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        else:
            print("No tasks yet.")
    
    elif choice == 4:
        print("Exiting the list!!")
        break
    
    else:
        print("Invalid choice. Please enter 1-4.")
