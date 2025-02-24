# Simple To-Do List App

tasks = []  # Empty list to store tasks

while True:
    print("\n📌 To-Do List:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ Task '{task}' added!")

    elif choice == "2":
        print("\n📝 Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    elif choice == "3":
        task_num = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"❌ Removed Task: {removed_task}")
        else:
            print("⚠️ Invalid task number!")

    elif choice == "4":
        print("👋 Exiting... Bye!")
        break
    else:
        print("⚠️ Invalid choice! Try again.")
