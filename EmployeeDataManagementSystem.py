# File: EmployeeDataManagementSystem.py
# Author: Jeffrey Bilski
#--------------------------------------------------------

# imports
# import datetime

# Global Variables:
systemState = 0
employeeMasterList = []

#--------------------------------------------------------
# Summary: Takes a string and determines if it is in date format
# Paremeters: dateString = the string being checked as a date 
# Returns: true if dateString is in the correct format,
#           otherwise false

def dateStringIsValid(dateString):
    isValid = False

    #first, determine the size to make sure it is right format
    #
    #should changes this to find where the '/' are and remove them, then check if is numeric
    #there are too many cases to check here, also if the day/month is in the right range
    if len(dateString) == 10:
        if dateString[2] == '/' and dateString[5] == '/':
            isValid = True

    return isValid

#--------------------------------------------------------
# Summary: Prompts the user with "outText", takes input,
#           and validates that input as a string of letters.
# Paremeters: outputText = the string to prompt the user with
# Returns: the string inputed by the user

def getLetterInput(outputText):
    inputString = ""
    isInvalid = True # initialize to true to prime loop

    while isInvalid == True:
        inputString = input(outputText + ": ")
        if not inputString.isalpha():
            print("The value \"" + inputString + "\" is invalid. Please enter a value only containing letters.")
        else:
            isInvalid = False
    
    return inputString

#--------------------------------------------------------
# Summary: Prompts the user with "outText", takes input,
#           and validates that input as a date string.
# Paremeters: outputText = the string to prompt the user with
# Returns: the string inputed by the user

def getDateInput(outputText):
    inputString = ""
    isInvalid = True # initialize to true to prime loop

    while isInvalid == True:
        inputString = input(outputText + " (mm/dd/yyyy): ")
        if not dateStringIsValid(inputString):
            print("The value \"" + inputString + "\" is invalid. Please enter a value in the format (mm/dd/yyyy).")
        else:
            isInvalid = False
    
    return inputString

#--------------------------------------------------------
# Summary: Adds a new entry to the master data list

def addNewEntry():
    print("Enter the employee's info for each prompt. \n\n")
    firstName = ""
    lastName = ""
    birthDate = ""
    position = ""
    newEntry = []

    try:
        firstName = getLetterInput("First name")
        lastName = getLetterInput("Last name")
        birthDate = getDateInput("Birthday")
        position = getLetterInput("Position")
        startDate = getDateInput("Start date")
    except:
        print("Unable to add entry:")
    

    newEntry.append(firstName)
    newEntry.append(lastName)
    newEntry.append(birthDate)
    newEntry.append(position)
    newEntry.append(startDate)

    employeeMasterList.append(newEntry)

#--------------------------------------------------------

def searchByString(menuSelection):
    pass

def searchByDate(menuSelection):
    pass

#--------------------------------------------------------

def queryEntry():
    menuSelection = 0
    
    print("What would you like to search by?")
    print("1.) First name")
    print("2.) Last name")
    print("3.) Birthday name")
    print("4.) Position")
    print("5.) Start date")
    
    menuSelection = input("\nEnter a selection: ")

    if menuSelection == 1 or menuSelection == 2 or menuSelection == 4:
        searchByString(menuSelection)
    elif menuSelection == 3 or menuSelection == 5:
        searchByDate(menuSelection)

#--------------------------------------------------------

def importData():
    pass

#--------------------------------------------------------

def deleteEntry():
    pass

#--------------------------------------------------------
# Outputs the main menu prompt

def outputMainMenu():
    print("\nWhat would you like to do?")
    print("1.) Add a new employee entry")
    print("2.) Query an existing employee")
    print("3.) Import from a text file")
    print("4.) Exit")

#--------------------------------------------------------
# Summary: main function

def runSystem():
    # in python, you have to specify that you're using the global
    # variable first.
    global systemState 
    systemState = 1
    mainMenuSelection = 0

    print("Welcome to Employee Management System.")

    while systemState > 0:
        outputMainMenu()
        mainMenuSelection = input("\nEnter a selection: ")
        
        if mainMenuSelection == "1":
            addNewEntry()
        elif mainMenuSelection == "2":
            queryEntry()
        elif mainMenuSelection == "3":
            importData()
        elif mainMenuSelection == "4":
            print("Goodbye. \n")
            systemState = 0
        else:
            print("You entered: "  + mainMenuSelection + "\n")
            print("This is invalid. Please select an option from the menu. \n")

# program will run by running our script on the command line
if __name__ == "__main__":
	runSystem()
