todolist = []
import time

while True: #Menu loop
    print("\n---TO DO LIST---")
    print("1: Add Task")
    print("2: Remove Task")
    print("3: View Tasks")
    print("4: Exit")
    print("5: Clear all")
    
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("❌ Invalid input, please enter a number (1-5)")
        continue

    if choice==1:
       task=input("Add your task: ")
       todolist.append(task)
       print("Task succesfully added")
       continue
    
    elif choice==2:
        if not todolist:
            print("⚠️ No tasks to remove")
        else:
            print("Your tasks")
            for i, task in enumerate(todolist, 1):
                print(f"{i}. {task}")
            try:    
                index = int(input("Enter the number of the task to remove: "))
                if 1 <= index <= len(todolist):
                    removed = todolist.pop(index-1)
                    print(f"🗑️ Removed: {removed}")
                else:
                    print("❌ Invalid task number")
            except ValueError:
                print("Invalid option")
                time.sleep(2)
                

    elif choice==3:
        if not todolist:
            print("📭 No tasks yet")
        else:
            print("YOUR TASKS: ")
            for i, task in enumerate(todolist, 1):
                print(f"{i}. {task}")

    elif choice==4:
        print("Goodbye")
        time.sleep(2)
        break
    
    elif choice==5:
        if not todolist:
            print("📭 No tasks to clear")
            
        print("Delete all tasks? y/n")
        delete=input().lower()
    
        if delete=="y":
            todolist.clear()
            print("TO DO LIST Cleared")
            
        elif delete=="n":
            print("Cancelled")
        else:
            print("Invalid option")
            time.sleep(2)
            

    
    else:
        print("Invalid option")
        



    

