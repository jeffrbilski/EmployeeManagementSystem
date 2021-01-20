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
    if len(dateString) == 10
        if dateString[3] == "/" and dateString[6] == "/"
            isValid == True

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
# Summary: Validates mainMenuSelection is a valid option
# Paremeters: mainMenuSelection = the variable to validate
# Returns: true if mainMenuSelection is in validOptions

def validateMainMenuSelection(mainMenuSelection):
    validOptions = [1,2,3,4]
    returnVal = False

    if mainMenuSelection in validOptions:
        returnVal = True

    return returnVal

#--------------------------------------------------------
# Summary: Adds a new entry to the master data list

def addNewEntry():
    print("Enter the employee's info for each prompt. \n\n")
    firstName = ""
    lastName = ""
    birthdate = ""
    position = ""
    newEntry = []

    firstName = getLetterInput("First name")
    lastName = getLetterInput("Last name")
    birthDate = getDateInput("Birthday")
    position = getLetterInput("Position")
    startDate = getDateInput("Start date")

    newEntry.append(firstName)
    newEntry.append(lastName)
    newEntry.append(birthDate)
    newEntry.append(position)
    newEntry.append(startDate)

    employeeMasterList.append(newEntry)

#--------------------------------------------------------

def queryEntry():
    pass

#--------------------------------------------------------

def importData():
    pass

#--------------------------------------------------------

def deleteEntry():
    pass

#--------------------------------------------------------
# Outputs the main menu prompt

def outputMainMenu():
    print("What would you like to do? \n")
    print("1.) Add a new employee entry \n")
    print("2.) Query an existing employee \n")
    print("3.) Import from a text file \n")
    print("4.) Exit \n")
    print("\n")
    
#--------------------------------------------------------
# Summary: main function

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

