# This is part of the Projekt Taskmanager (tama) in wich i build my own taskmanager for the console
# Author: Cesar Andres
# Language Python 3.8
# Date: 2020
# This part deletes the Task identified by the ID and displays it one more time

import sys
import terminalColors as b # colors for the terminal
import taskDesign as tmp

# input
taskToDelete = sys.argv[1]

# new tasks is a list of tasks without the deltet wich gets written into the now empty file
newTasks = []

with open("Taskmanager/tasks.txt", "r") as file:
    tasks = file.readlines() # get the content of the current file

# open in write mode to clear the file
with open("Taskmanager/tasks.txt", "w") as file:
    tmp.form(b)
    for task in tasks: # iterate trough the list of tasks
        chunks = task.split(';')

        if taskToDelete == "done": # deltes all done tasks 
            if chunks[2] != "true":
                newTask = ";".join(chunks) 
                newTasks.append(newTask) # add the not delted tasks to the newTasks list

            else:    
                tmp.displayTask(chunks,b) # print out the delted task
                tmp.form(b)

        else: # deletes the task of the given ID
            if chunks[0] != taskToDelete:
                newTask = ";".join(chunks) 
                newTasks.append(newTask) # add the not delted tasks to the newTasks list

            else:
                tmp.displayTask(chunks,b) # print out the delted task
                tmp.form(b)

    # write the newTasks List to the file
    file.writelines(newTasks)

