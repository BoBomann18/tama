import terminalColors as b

# displays the task of the given chunks 
def displayTask(chunks,b):
    print(f"ID: {chunks[0]}")
    print(f"Task: {chunks[1]}")
    if chunks[2] == "true":
        print(f"Status: {b.bcolors.OKGREEN} {chunks[2]} {b.bcolors.ENDC}")

    else:
        print(f"Status: {b.bcolors.FAIL} {chunks[2]} {b.bcolors.ENDC}")
        
    print(f"Note: {chunks[3]}")
    print(f"Start: {chunks[4]}")
    print(f"End: {chunks[5]}")

# is a simple form that can make the look more readable
def form(b):
    print("")
    print(f"{b.bcolors.OKBLUE} =============================== {b.bcolors.ENDC}")
    print("")