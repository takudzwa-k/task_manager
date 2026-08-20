import json
import os #operating system

def addTask():
    task = input("Enter the task you want to add: ")

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
    }

    tasksList.append(newTask)

    with open('tasks.json', 'w') as f: #overriding old list with new updated list
        json.dump(tasksList, f, indent=2)

    print(f'Task "{task}" added successfully')

def updateTask():
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

    for task in tasksList:
        if task['id'] == taskID:
            newTask = input("Enter the new task description: ")
            task['task'] = newTask
            with open('tasks.json', 'w') as f:
                json.dump(tasksList, f, indent=2)
            print(f'Task ID {taskID} updated successfully')
            return

    print(f'Task ID {taskID} not found.')

    
def deleteTask():
    taskID = int(input("Enter the ID of the task you want to delete: "))

    with open('tasks.json', 'r') as f:
        tasksList = json.load(f)

    taskToDelete = None
    for task in tasksList:
        if task['id'] == taskID:
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
    
    while True:
        confirmation = input(f"Are you sure you want to delete task ID {taskID}? (y/n): ").lower()
        if confirmation == 'y':
            for task in tasksList:
                    if task['id'] == taskID:
                        tasksList.remove(task)
                        with open('tasks.json', 'w') as f:
                            json.dump(tasksList, f, indent=2)
                            print(f'Task ID {taskID} deleted successfully')
                            return
            break
        elif confirmation == 'n':
            print("Deletion cancelled.")
            return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


    print(f'Task ID {taskID} not found.')
            

deleteTask()
#addTask()
#updateTask()
