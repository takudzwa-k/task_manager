import json #importing JSON module to work with JSON files
import os #operating system

def addTask(): #declaring function to add task
    task = input("Enter the task you want to add: ")
    status = "not done"

    if os.path.exists('tasks.json'): #checking if file exists
        with open('tasks.json', 'r') as f:
            try:
                tasksList = json.load(f) #reading JSON file
            except json.JSONDecodeError:
                tasksList = []
    else:
        tasksList = []

    nextID = max((t['id'] for t in tasksList), default=0) + 1 

    newTask = {
        'id' : nextID,
        'task': task,
        'status' : status,
    }

    tasksList.append(newTask)

    with open('tasks.json', 'w') as f: #overriding old list with new updated list
        json.dump(tasksList, f, indent=2)

    print(f'Task "{task}" added successfully to ID:{nextID}')

def updateTask(): #declaring function to update task
    taskID = int(input("Enter the ID of the task you want to update: "))

    with open('tasks.json', 'r') as f:
        tasksList = json.load(f) #reading JSON file

    taskToUpdate = None #start with no task to update
    for task in tasksList: 
        if task['id'] == taskID:
            taskToUpdate = task
            break

    if taskToUpdate is None:
        print(f'Task ID {taskID} not found.')
        return

    print(f'Current task description: {taskToUpdate["task"]}')
    
    if os.path.exists('tasks.json'): #checking if file exists
        with open('tasks.json', 'r') as f:
            try:
                tasksList = json.load(f) #reading JSON file
            except json.JSONDecodeError:
                print("No tasks found.")
                return
    else:
        print("No tasks found.")
        return

    for task in tasksList: #looping throug json file
        if task['id'] == taskID:
            newTask = input("Enter the new task description: ")
            task['task'] = newTask
            with open('tasks.json', 'w') as f:
                json.dump(tasksList, f, indent=2)
            print(f'Task ID {taskID} updated successfully')
            return

    print(f'Task ID {taskID} not found.')

    
def deleteTask(): #declaring function to delete task
    taskID = int(input("Enter the ID of the task you want to delete: "))

    with open('tasks.json', 'r') as f:
        tasksList = json.load(f)

    taskToDelete = None #start with no task to delete
    for task in tasksList: #looping through the list of tasks
        if task['id'] == taskID: #checking if the task ID matches the input ID
            taskToDelete = task
            break 

    if taskToDelete == None:
        print(f'Task ID {taskID} not found.')
        return

    print(f'Current task description: {taskToDelete["task"]}')

    if os.path.exists('tasks.json'): #checking if file exists
            with open('tasks.json', 'r') as f:
                try:
                    tasksList = json.load(f) #reading JSON file
                except json.JSONDecodeError:
                    print("No tasks found.")
                    return
    else:
        print("No tasks found.")
        return
    
    while True: #looping until valid input is received
        confirmation = input(f"Are you sure you want to delete task ID {taskID}? (y/n): ").lower()
        if confirmation == 'y': #if user confirms deletion
            for task in tasksList:
                    if task['id'] == taskID: #checking if the task ID matches the input ID
                        tasksList.remove(task) #removing the task from the list
                        with open('tasks.json', 'w') as f:
                            json.dump(tasksList, f, indent=2) #writing the updated list back to the JSON file
                            print(f'Task ID {taskID} deleted successfully')
                            return
            break
        elif confirmation == 'n':
            print("Deletion cancelled.")
            return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


    print(f'Task ID {taskID} not found.')

def changeStatus(): #function to change the status of a task
    taskID = int(input("Enter the ID of the task you want to mark as in progress/done: "))

    if not os.path.exists('tasks.json'): #checking if file exists
        print("No tasks found.")
        return

    with open('tasks.json', 'r') as f:
        try:
            tasksList = json.load(f) #reading JSON file
        except json.JSONDecodeError:
            print("No tasks found.")
            return
    
    taskToUpdate = None #start with no task to update
    for task in tasksList: 
        if task['id'] == taskID:
            taskToUpdate = task
            break
    
    if taskToUpdate is None:
        print(f'Task ID {taskID} not found.')
        return
    
    print(f'Current task description: {taskToUpdate["task"]}')

    while True:
        newStatus = int(input("Enter 1 if you want to mark task as 'in progress': "
        "Enter 2 if you want to mark task as 'done': "))
        status1 = "in progress"
        status2 = "done"

        if newStatus == 1:
            task['status'] = status1
        elif newStatus == 2:
            task['status'] = status2
        else:
             print("Invalid input. Please enter '1' or '2'.")

        with open('tasks.json', 'w') as f:
            json.dump(tasksList, f, indent=2)
        print(f'Task ID {taskID} updated to "done" successfully')
        return

def listAllTasks(): #list all tasks
    if not os.path.exists('tasks.json'): #checking if file exists
        print("No tasks found.")
        return

    with open('tasks.json', 'r') as f:
        try:
            tasksList = json.load(f) #reading JSON file
        except json.JSONDecodeError: #handling JSON decode error
            print("No tasks found.")
            return

    if not tasksList:
        print("No tasks found.")
        return

    print("All Tasks:")
    for task in tasksList:
        print(f"ID: {task['id']}, Task: {task['task']}, Status: {task.get('status', 'not done')}")

def listDoneTasks(): #list tasks that are done
    if not os.path.exists('tasks.json'): #checking if file exists
        print("No tasks found.")
        return

    with open('tasks.json', 'r') as f:
        try:
            tasksList = json.load(f) #reading JSON file
        except json.JSONDecodeError:
            print("No tasks found.")
            return

    doneTasks = [task for task in tasksList if task.get('status') == 'done'] #only getting tasks that are marked as done

    if not doneTasks:
        print("No done tasks found.")
        return

    print("Done Tasks:")
    for task in doneTasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Status: {task.get('status', 'not done')}")

def listInProgressTasks(): #list tasks that are in progress
    if not os.path.exists('tasks.json'): #checking if file exists
        print("No tasks found.")
        return

    with open('tasks.json', 'r') as f:
        try:
            tasksList = json.load(f) #reading JSON file
        except json.JSONDecodeError:
            print("No tasks found.")
            return

    inProgressTasks = [task for task in tasksList if task.get('status') == 'in progress'] #only getting tasks that are marked as in progress

    if not inProgressTasks:
        print("No in progress tasks found.")
        return

    print("In Progress Tasks:")
    for task in inProgressTasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Status: {task.get('status', 'not done')}")

def listNotDoneTasks(): #lists tasks that are not done
    if not os.path.exists('tasks.json'): #checking if file exists
        print("No tasks found.")
        return

    with open('tasks.json', 'r') as f:
        try:
            tasksList = json.load(f) #reading JSON file
        except json.JSONDecodeError:
            print("No tasks found.")
            return

    notDoneTasks = [task for task in tasksList if task.get('status') == 'not done'] #only getting tasks that are marked as not done

    if not notDoneTasks:
        print("No not done tasks found.")
        return

    print("Not Done Tasks:")
    for task in notDoneTasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Status: {task.get('status', 'not done')}")  

# --- Main Method ---
if __name__ == "__main__":
    ### Loop to run app
    print("Task Tracker") #Welcome Statement

    while True: ## Loops unless otherwise
        print("\n--- Main Menu ---") # New line and header
        print("1. Add new task")
        print("2. Update task")
        print("3. Delete task") 
        print("4. Mark task as in progress or done")
        print("5. List all tasks") 
        print("6. List all tasks that are done")
        print("6. List all tasks that are not done")
        print("7. List all tasks that are in progress")
        print("8. Quit")
        print("-------------------")

        choice = input("Please enter your choice: ") #Prompt

        if choice == "1":
            addTask() # Calling function
        elif choice == "2":
            updateTask()
        elif choice == "3":
            deleteTask() 
        elif choice == "4":
            changeStatus()
        elif choice == "5":
            listAllTasks() 
        elif choice == "6":
            listDoneTasks()
        elif choice == "7":
            listInProgressTasks()
        elif choice == "8":
            break #Closes app 
        else:
            print("Invalid input. Please enter a number between 1 and 8.")
