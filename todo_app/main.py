from todo import add_task, view_tasks, mark_done, delete_task

def menu():
    while True:
        print("==== TO-DO LIST APP ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
            print("\nTask added!\n")

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            num = int(input("Enter task number to mark done: ")) - 1
            mark_done(num)

        elif choice == "4":
            view_tasks()
            num = int(input("Enter task number to delete: ")) - 1
            delete_task(num)

        elif choice == "5":
            print("\nGoodbye!\n")
            break

        else:
            print("\nInvalid choice. Try again.\n")

menu()
