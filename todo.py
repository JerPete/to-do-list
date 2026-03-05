TASK_FILE = "task.txt"


def list_empty(tasks: list) -> bool:
    return not tasks

def print_list(tasks: list[str]) -> None:
    for index, item in enumerate(tasks, start=1):
        print(f"{index}, {item}")

def add_task() -> None:
    user_task = input("Please input a task: ").strip()
    if user_task:
        tasks.append(user_task)
        print("Task added.")
    else:
        print("Task cannot be empty.")

def view_task() -> None:
    if list_empty(tasks):
        print("List empty! ")
        return
    print_list(tasks)

def remove_task() -> None:
    if list_empty(tasks):
        print("List empty! ")
        return
            
        
    print_list(tasks)
        
    try:
        task_number_to_remove = int(input("Which number task do you wish to remove: "))
        if task_number_to_remove < 1 or task_number_to_remove > len(tasks):
            print("Please select a valid option!")
            return
                
        del tasks[task_number_to_remove - 1]
        print(f"Removed number {task_number_to_remove} task successfully!")

        print_list(tasks)

    except ValueError:
        print("Please enter a valid number!")


def save_file() -> None:

    with open(TASK_FILE, "w") as file:
        for entry in tasks:
            file.write(f"{entry}\n")
            

def load_file() -> None:
    try:
        with open(TASK_FILE, "r") as file:
            new_task = [item.strip()for item in file]
            tasks.extend(new_task)
            

    except FileNotFoundError:
        pass



def main() -> None:
    while True:

        print("What would you like to do? ")

        user_choice = input(" A = Add task \n V = View task \n R = Remove task \n Q = Quit \n S = Save task \n").strip().upper()

        if user_choice == "Q":
            return

        if user_choice not in user_options:
            print("Please type a valid option! ")
            continue
    
    
        user_options[user_choice]()


user_options = { "A": add_task, "V" : view_task, "R" : remove_task, "S" : save_file}

tasks = []
load_file()
if __name__ == "__main__":
    main()

    



    
        





        

