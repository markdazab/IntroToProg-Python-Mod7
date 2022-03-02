# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Build demonstration of Pickling and Error Handling in python
# MDaza,3.1.2022,Created started script

# ---------------------------------------------------------------------------- #

# Picking Demo with Error Handling ------------------------------------ #

import pickle # Import Pickle Module

try: # Handle exceptions for NewTask and New Priority
    NewTask = str(input("Enter the name of your task: ")) # Get user input for task
    if NewTask == "": # Check if the user does not enter a value
        raise Exception ("Forgot to enter task name") # Raise exception if the NewTask is empty
    NewPriority = int(input("Enter the priority [1-5] of your task: ")) # Get user input for priority
    lstTasks = [NewTask, NewPriority] # Add NewTask and NewPriority to list

except Exception as e:
    print("There was an error") # Friendly comment for user
    print(e) # More info on the exception
    print(type(e))
    print(e.__doc__)

try: # Handle exceptions for Pickling
    objFile = open("Demo.dat", "wb")
    pickle.dump(lstTasks, objFile)
    objFile.close()

except Exception as e: # Here to handle any potential exceptions. Very likely if NewPriority is left blank.
    print ("Input error")
    print (e)
    print(type(e))
    print(e.__doc__)

try:
    objFile = open("Demo.dat", "rb")
    objFileData = pickle.load(objFile)
    objFile.close()
    print(objFileData)

except Exception as e:
    print ("Check for more comments below")
    print (e)
    print(type(e))
    print(e.__doc__)

