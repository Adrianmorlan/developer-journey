# Store all tasks here
tasks = []

#display the main menu
def show_menu():

    print("""
            === task manager ===
            1. Add task
            2. View task
            3. Delete task
            4. Exit
          """)

while True:

    show_menu()

    option = input("Select an option")

    #add a new talks

    if option == "1":

        name= input("task name: ")
        priority = input("priority  (high,medium,low): ")


        while True:
            try:
                hours = int(input("estimated hours: "))

                if hours < 0:

                    print("hours cannot be negative.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number ")

        #create task dictionary

        task = {
                "name": name,
                "priority": priority,
                "hours": hours
            }

        #add task to the list

        tasks.append(task)

        print("task added successfully")

    elif option == "2":

        print("\n===task list ===")

        if len(tasks) == 0:

                print("No tasks registered.")

        else:
            for task in tasks:

                print(f"""
                    name: {task["name"]}
                    priority: {task["priority"]}
                    hours: {task["hours"]}
                    ----------------------
                """)

    # delete task
    elif option == "3":
        print("\n=== DELETE TASK ===")

        task_name = input("Write the task name to delete: ")

        task_found = None

        for task in tasks:
            if task["name"] == task_name:
                task_found = task
                break

        if task_found is not None:
            tasks.remove(task_found)
            print("Task deleted successfully.")
        else:
            print("Task not found.")
            
    #exit program

    elif option == "4":

        print("\nexiting program....")
        break

    else:
        print("Invalid option.")



