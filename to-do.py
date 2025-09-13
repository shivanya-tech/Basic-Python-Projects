def main():
    tasks = []
    while True:
        print("\n------ TASK MANAGER -----")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Mark task as done")
        print("4. Exit")
        
        choice = input("Enter number: ")
        
        if choice == '1':
            how_many = int(input("How many tasks you want to add? "))
            for i in range(how_many):
                t1 = input("Enter your task: ")
                tasks.append({"task": t1, "status": False})
            print("Tasks added!")

        elif choice == '2':
            if not tasks:
                print("\nNo tasks available. Add some first!")
            else:
                print("\n--- YOUR TASKS ---")
                for idx, task in enumerate(tasks, start=1):
                    status = "✅ Done" if task["status"] else "❌ Not done"
                    print(f"{idx}. {task['task']} [{status}]")
                print("------------------")

        elif choice == '3':
            if not tasks:
                print("No tasks available to mark as done.")
            else:
                task_num = int(input("Enter the task number to mark as done: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["status"] = True
                    print(f"Task '{tasks[task_num - 1]['task']}' marked as done ✅")
                else:
                    print("Invalid task number!")

        elif choice == '4':
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid Number. Please try again.")
            

if __name__ == "__main__":
    main()
