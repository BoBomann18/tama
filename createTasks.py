# This is part of the Projekt Taskmanager (tama) in wich i build my own taskmanager for the console
# Author: Cesar Andres
# Language Python 3.8
# Date: 2020
# This Part creates Task based on the user Input

import datetime
import sys

# input
name = sys.argv[1]
note = sys.argv[2]
deadline = sys.argv[3]

status = "false"  
startDate = datetime.datetime.today().strftime ('%d.%m.%Y') # gets the current date as begin date

with open("Taskmanager/taskid.txt","r") as file:
    taskid = file.read()
    taskid = int(taskid) + 1 # incrementing the task id

with open("Taskmanager/tasks.txt", "a") as file:
    taskChunks = [str(taskid), name, status, note, startDate, deadline] # the chunks of the task are collected in this list
    task = ";".join(taskChunks) # the tasks chunks get joind to a list to append it to the file
    file.write(task + "\n")

with open("Taskmanager/taskid.txt","w") as file: # the incremented task id gets written to the now empty file
    file.write(str(taskid))

