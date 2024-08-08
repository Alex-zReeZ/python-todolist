tasks = []
archived_tasks = []

def show_menu():
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Archive task")
        print("4. See tasks")
        print("5. Exit")
        print("------------------")
        print("Current tasks:", tasks)

        input_value = input("Choose an option: ").strip()

        if input_value == "1":
            add_task()
        elif input_value == "2":
            delete_task()
        elif input_value == "3":
            archive_task()
        elif input_value == "4":
            see_tasks()
        elif input_value == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

def add_task():
    new_task = input("Enter your new task: ")
    tasks.append(new_task)
    print("Task added successfully")


def delete_task():
    pass


def archive_task():
    pass


def see_tasks():
    pass


if __name__ == "__main__":
    show_menu()