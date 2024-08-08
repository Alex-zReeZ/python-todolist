tasks = []
archived_tasks = []

def show_menu():
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Archive task (enter the name of the todo)")
        print("4. see archived tasks")
        print("5. Exit")
        print("------------------")
        print(show_tasks())

        input_value = input("Choose an option: ").strip()

        if input_value == "1":
            add_task()
        elif input_value == "2":
            delete_task()
        elif input_value == "3":
            archive_task()
        elif input_value == "4":
            see_archived_tasks()
        elif input_value == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")


def show_tasks():
    print("Task list:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task():
    new_task = input("Enter your new task: ")
    tasks.append(new_task)
    print("Task added successfully")


def delete_task():
    task_index = int(input("Enter the number of the task you want to delete : ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Tâche '{removed_task}' supprimée avec succès")
    else:
        print("invalide number")


def archive_task():
    tasks_index = int(input("Entrez l'index de la tâche à archiver: ")) - 1
    if 0 <= tasks_index < len(tasks):
        task_to_archive = tasks.pop(tasks_index)
        archived_tasks.append(task_to_archive)
        print(f"Tâche '{task_to_archive}' archivée avec succès")
    else:
        print("Index invalide")


def see_archived_tasks():
    print("Archived tasks:", archived_tasks)


if __name__ == "__main__":
    show_menu()