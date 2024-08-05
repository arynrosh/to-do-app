#TO-DO APP BY ARYAN ROSHAN
# Features: List the basic features the app should have, such as:
# Adding tasks
# Viewing tasks
# Marking tasks as complete
# Deleting tasks

def main_menu():
        print("------------------------------------------------")
        print("What would like to do today?")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")       

def main():
    task = 0
    tasks = []
    print("Welcome to my to-do app! Created by Aryan Roshan")
    while True:
        main_menu()
        print("------------------------------------------------")
        choice = input("Please select an option:\n")
        option = int(choice)
           
        if option == 1:
            print("------------------------------------------------")
            num_task = int(input("How many tasks would you like to add?\n"))
            for i in range(num_task):
                print("------------------------------------------------")
                task = input("What task would you like to add?\n")
                tasks.append({"Task": task, "Done": False})
                print("------------------------------------------------")
                print("Task has been added!")

        elif option == 2:
            print("------------------------------------------------")
            print("Tasks:")
            for index, task in enumerate(tasks):
                if task["Done"]:
                    status = "Done"
                else:
                    status = "Not Done"
                print(f"{index + 1}. {task['Task']} - {status}")

        elif option == 3:
            print("------------------------------------------------")
            print("Tasks:")
            for index, task in enumerate(tasks):
                status = "Not Done"
                if not task["Done"]:
                    print(f"{index + 1}. {task['Task']} - {status}")
            
            print("------------------------------------------------")
            task_to_complete = input("Which task would you like to complete?\n")
            if not task_to_complete.isdigit() or not (1 <= int(task_to_complete) <= len(tasks)):
                print("Invalid task number!")
                continue

            task_to_complete = int(task_to_complete)
            tasks[task_to_complete - 1]["Done"] = True
            print("Task marked as complete!")

        elif option == 4:
            print("------------------------------------------------")
            print("Exiting. Thank you for using my app!")
            print("------------------------------------------------")
            break

        else:
            print("------------------------------------------------")
            print("Invalid input, please enter a valid option.")


if __name__ == "__main__":
    main()