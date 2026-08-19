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

addTask()    
