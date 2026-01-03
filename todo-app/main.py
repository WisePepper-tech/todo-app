from storage import load_tasks, save_tasks
from todo import Task


def add_task(title: str):
    tasks = load_tasks()
    new_id = len(tasks) + 1
    tasks.append(Task(id=new_id, title=title))
    save_tasks(tasks)
    print("✅ Task added")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return

    for task in tasks:
        status = "✔" if task.completed else "✖"
        print(f"{task.id}. [{status}] {task.title}")


def main():
    print("1. Add task")
    print("2. List tasks")

    choice = input("Choose option: ")

    if choice == "1":
        title = input("Task title: ")
        add_task(title)
    elif choice == "2":
        list_tasks()
    else:
        print("Unknown option")


if __name__ == "__main__":
    main()