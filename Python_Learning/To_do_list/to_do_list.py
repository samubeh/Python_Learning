todolist = []
import time
import os
def list_tasks(tasks):
    if not tasks:
        print("No tasks yet")
    else:
        print("YOUR TASKS: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def ask_int(prompt, min_value=None, max_value=None):
    """Pide un número entero con validación y mensaje personalizado"""
    while True:
        try:
            num = int(input(prompt))
            if min_value is not None and num < min_value:
                print(f"❌ Must be at least {min_value}")
                continue
            if max_value is not None and num > max_value:
                print(f"❌ Must be at most {max_value}")
                continue
            return num
        except ValueError:
            print("❌ Invalid input, please enter a number")

def remove_task(todolist):
    if not todolist:
        print("⚠️ No tasks to remove")
        time.sleep(1)
        return

    list_tasks(todolist)
    index = ask_int(f"Enter the number of the task to remove (1-{len(todolist)}): ",
                    1, len(todolist))
    removed = todolist.pop(index - 1)
    print(f"🗑️ Removed: {removed}")
    time.sleep(1)
   

def add_task(todolist):
    while True:
        
        print("Type return to go to the menu")
        task= input("Enter your task: ").strip()
        if task== "return":
            return
        if not task:
            print("Empty task not added.")
            continue
        else:
            todolist.append(task)
            print(f"{task} added as a task.")
            time.sleep(1)
            break
        

def clear_tasks(todolist):
    if not todolist:
            print("📭 No tasks to clear")
            return
            
    else:  
        delete=input("Delete all tasks? y/n: ").lower().strip()
    
        if delete=="y":
            todolist.clear()
            print("TO DO LIST Cleared")
            time.sleep(1)
            
        elif delete=="n":
            print("Cancelled")
        else:
            print("Invalid option")
            time.sleep(2)

def edit_task(todolist):
    """Editar el texto de una tarea existente."""
    if not todolist:
        print("📭 No tasks to edit")
        time.sleep(1)
        return

    # 1) Mostrar lista numerada
    list_tasks(todolist)

    # 2) Elegir qué tarea editar (valida rango con ask_int)
    index = ask_int(f"Enter the task number to edit (1-{len(todolist)}): ",
                    1, len(todolist))

    old = todolist[index - 1]  # texto actual de la tarea
    print(f"Current text: '{old}'")

    # 3) Pedir nuevo texto (permitimos cancelar con 'return')
    new_text = input("New text (or type 'return' to cancel): ").strip()

    if new_text.lower() == "return":
        print("Cancelled")
        time.sleep(1)
        return
    if not new_text:
        print("⚠️ Empty text not allowed. Task not changed.")
        time.sleep(1)
        return
    if new_text == old:
        print("ℹ️ Same text as before. Task not changed.")
        time.sleep(1)
        return

    # 4) Aplicar el cambio
    todolist[index - 1] = new_text
    print(f"✏️ Updated: '{old}' → '{new_text}'")
    time.sleep(1)


def search_tasks(todolist):

    """Busca tareas por texto (case-insensitive) y muestra coincidencias numeradas."""
    
    if not todolist:
        print("📭 No tasks to search")
        return

    query = input("Search text: ").strip().lower()
    if not query:
        print("⚠️ Empty search. Type something.")
        return

    # Construimos una lista de coincidencias: (posicion_en_lista, texto_tarea)
    matches = [(i, task) for i, task in enumerate(todolist, 1) if query in task.lower()]

    if not matches:
        print("🔍 No matches found")
        time.sleep(2)
        return

    print(f"🔎 Found {len(matches)} match(es):")
    for i, task in matches:
        print(f"{i}. {task}")
        back = input("Tipe return to go back: ").lower()
        if back== "return":
            return




while True: #Menu loop
    os.system("cls" if os.name == "nt" else "clear")
    print("\n---TO DO LIST---")
    print("0: Exit")
    print("1: Add Task")
    print("2: Remove Task")
    print("3: View Tasks")
    print("4: Clear all")
    print("5: Edit Task")
    print("6: Search Tasks")

    
    choice = ask_int("Choose an option: ", 1, 6)


    if choice==1:
       add_task(todolist)

    elif choice==0:
        print("Goodbye")
        time.sleep(2)
        break

    elif choice==2:
        remove_task(todolist)
       
        
    elif choice==3:
       list_tasks(todolist)
    
    elif choice==4:
        clear_tasks(todolist)
            
    elif choice==5:
        edit_task(todolist)

    elif choice==6:
        search_tasks(todolist)
    
    else:
        print("Invalid option")
        



    

