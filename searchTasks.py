# This is part of the Projekt Taskmanager (tama) in wich i build my own taskmanager for the console
# Author: Cesar Andres
# Language Python 3.8
# Date: 2020
# This Part searches and displays the searched Tasks

import sys
import terminalColors as b
import taskDesign as tmp

searchInput = sys.argv[1] # the serach request

with open("Taskmanager/tasks.txt", "r") as file:
        tasks = file.readlines()
        if searchInput != "" or searchInput != " ": # if the search bar is not empty the task names get checked for the search request
            tmp.form(b)

            for task in tasks:
                chunks = task.split(';')

                if searchInput in chunks[1]: # if the searchrequest exists in the name the task gets displayed
                    tmp.displayTask(chunks,b)
                    tmp.form(b)

        else: # all tasks get displayed if no serach request is enterd
            tmp.form(b)
            for task in tasks:
                chunks = task.split(';')
                tmp.displayTask(chunks,b)
                tmp.form(b)