import sys
import terminalColors as b
import datetime
import taskDesign as tmp


class Task():

    def __init__(self,name,note,deadline):
        self.name = name
        self.note = note
        self.deadline = deadline
        self.status = "false"  
        self.startDate = datetime.datetime.today().strftime ('%d.%m.%Y')

        
    def createTask(self):
        # creates a Task
        with open("/home/cesar/Projekte/Python/Taskmanager/Taskmanager/taskid.txt","r") as file:
            taskid = file.read()
            taskid = int(taskid) + 1 # incrementing the task id

        with open("/home/cesar/Projekte/Python/Taskmanager/Taskmanager/tasks.txt", "a") as file:
            taskChunks = [str(taskid), self.name, self.status, self.note, self.startDate, self.deadline] # the chunks of the task are collected in this list
            task = ";".join(taskChunks) # the tasks chunks get joind to a list to append it to the file
            file.write(task + "\n")

        with open("/home/cesar/Projekte/Python/Taskmanager/Taskmanager/taskid.txt","w") as file: # the incremented task id gets written to the now empty file
            file.write(str(taskid))     

    
    def deleteTask(self, taskToDelete):
        # new tasks is a list of tasks without the deletet wich gets written into the now empty file
        newTasks = []

        with open("/home/cesar/Projekte/Python/Taskmanager/Taskmanager/tasks.txt", "r") as file:
            tasks = file.readlines() # get the content of the current file

        # open in write mode to clear the file
        with open("/home/cesar/Projekte/Python/Taskmanager/Taskmanager/tasks.txt", "w") as file:
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

    def completeTask(self,completed):
        tasksNew = [] # new tasks are stored in here

        with open("/home/cesar/Projekte/Python/Taskmanager/Taskmanager/tasks.txt", "r") as file: # reads the current context of the file
            tasks = file.readlines()

        with open("/home/cesar/Projekte/Python/Taskmanager/Taskmanager/tasks.txt", "w") as file: # opens the file and wipes it
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

    def searchTask(self):
        searchInput = sys.argv[1] # the serach request

        with open("/home/cesar/Projekte/Python/Taskmanager/Taskmanager/tasks.txt", "r") as file:
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
