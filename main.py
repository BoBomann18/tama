import tama as tm 
import sys

action = sys.argv[1]


if action == "cre":
    name = sys.argv[2]
    note = sys.argv[3]
    deadline = sys.argv[4]
    tm.Task.createTask(name, note, deadline)

elif action == "del":
    task_id = sys.argv[2]
    tm.Task.deleteTask(task_id)

elif action == "com":
    task_id = sys.argv[2]
    tm.Task.completeTask(task_id)

elif action == "ser":
    search_input = sys.argv[2]
    tm.Task.searchTask(search_input)

else:
    print("Error")