# This is part of the Projekt Taskmanager (tama) in wich i build my own taskmanager for the console
# Author: Cesar Andres
# Language Python 3.8
# Date: 2020
# This Part toggles the Status of the given Task and idicates if its done or not

import sys
import terminalColors as b
import taskDesign as tmp

# input
completed = sys.argv[1] # input as id to identify the task

tasksNew = [] # new tasks are stored in here

with open("Taskmanager/tasks.txt", "r") as file: # reads the current context of the file
    tasks = file.readlines()

with open("Taskmanager/tasks.txt", "w") as file: # opens the file and wipes it
    for task in tasks:
        chunks = task.split(';')

        if chunks[0] == completed: # controles if the task has the expected id, if so it toggels between on and of
            if chunks[2] == "true":
                chunks[2] = "false"

            elif chunks[2] == "false":
                chunks[2] = "true"
        
            # print out the delted task
            tmp.form(b)
            tmp.displayTask(chunks,b)
            tmp.form(b)

        task = ";".join(chunks) # if the task is not choosen it gets directly appended to the new taskslist
        tasksNew.append(task) 
        
    file.writelines(tasksNew) # here I write all Tasks to the know emtpy file