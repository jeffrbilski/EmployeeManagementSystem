# File: EmployeeDataManagementSystem.py
# Author: Jeffrey Bilski
#--------------------------------------------------------

# Global Variables:
systemState = 0
employeeMasterList = []

def outputMainMenu():
    print("What would you like to do? \n")
    print("1.) Add a new employee entry \n")
    print("2.) Query an existing employee \n")
    print("3.) Import from a text file \n")
    print("4.) Exit \n")
    print("\n")

#--------------------------------------------------------

def validateMainMenuSelection(mainMenuSelection):
    validOptions = [1,2,3,4]
    returnVal = False

    if mainMenuSelection in validOptions:
        returnVal = True

    return returnVal

#--------------------------------------------------------

def validateDateString(dateString):
    pass

#--------------------------------------------------------

def addNewEntry():
    print("Enter the employee's info for each prompt. \n\n")
    firstName = input("First name:")
    lastName = input("Last name:")

    birthDate = input("Date of birth (mm/dd/yyyy):")
    validateDateString(birthDate)

    position = input("Position:")

    startDate = input("Start date (mm/dd/yyyy):")
    validateDateString(startDate)

#--------------------------------------------------------

def queryEntry():
    pass

#--------------------------------------------------------

def importData():
    pass

#--------------------------------------------------------

def runSystem():
    # in python, you have to specify that you're using the global
    # variable first.
    global systemState 
    systemState = 1
    mainMenuSelection = 0

    print("Welcome to Employee Management System.\n\n")

    while systemState > 0:
        outputMainMenu()
        mainMenuSelection = input("Enter a selection:")

        if not validateMainMenuSelection(mainMenuSelection):
            print("You entered: "  + mainMenuSelection + "\n")
            print("This is invalid. Please select an option from the menu. \n")
        else:
            if mainMenuSelection == 1:
                addNewEntry()
            elif mainMenuSelection == 2:
                queryEntry()
            elif mainMenuSelection == 3:
                importData()
            elif mainMenuSelection == 4:
                print("Goodbye. \n")
                systemState = 0

