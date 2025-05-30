def main():
    tasks = []
    while True:
        print("TO DO LIST")
        print("1.  ADD task")
        print("2.  SHOW tasks")
        print("3.  MARKDOWN as done")
        print("4.  EXIT")
        
        choice = input("Enter your choice: ")       
        
        if choice == "1":
            print()
            n_tasks = int(input("how many tasks do you want to add:"))
            
            for i in range(n_tasks):
                task = input("Enter your task: ") 
                tasks.append({"task": task , "status": False}) #key and value pairs 
                print('Task added !')
                
        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
                
        elif choice == '4':        
            print("Exiting the TO-DO List")
            break
        
        else:
            print('Invalid choice')
            
            
if __name__ == "__main__":

    main()
    