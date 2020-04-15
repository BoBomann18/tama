This Programm is a Taskmanger(= tama) wich should help you help in keeping you accountable!
Tama can create, delete, complete and search tasks. It is also pretty easy to control!
More Features will be added soon!

Content:
- General Info
- Guide to set tama up on Linux
- Guide to use tama

General Info:
- Language: Python 3.8 & Bash
- Date: 2020
- Author: Cesar Andres

Guide to set tama up in Linux:
- First you need to download the folder Taskmanger and move it where you want to
- Next you need to download the bash script tama which you move to your /usr/local/bin/
- Now you need to change every line in the bash script that refers to the location of the folder taskmanger where the python files are located
      and change it to the location your folder is stored

Guide to use tama:
- Creating a Task:
    Command: tama cre "Taskname" "Note" Deadline -> creates a task
    e.g: tama cre "Do Homework" "Draw a picture of an bird" 20.12.2020 -> creates the task with these params
    Info: all params are requierd! If you want no note leave the quotes empty -> ("")
        
- Searching Tasks:
    Command: tama ser -> displays all tasks
    Command: tama ser "Taskname" -> searches tasks with 'userInput' in thier taskname
    e.g: tama ser "Homework" -> searches tasks with Homework in their taskname
    Info: Searches only in the Name of the Task 

- Completing Tasks:
    Command: tama com ID -> completes the task with the given ID
    e.g: tama com 4 -> completes the task with ID 4
    Info: You can toggle the status if you complete a completet task again

- Deleting Tasks:
    Command: tama del ID -> deletes the task with the given ID
    e.g: tama del 7 -> delets the task with the ID 7
    Command: tama del done -> deletes all tasks with the status true
    Info: deleting tasks is not reverseable
 
