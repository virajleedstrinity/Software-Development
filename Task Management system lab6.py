from idlelib.autocomplete import FORCE

from colorama import init, Fore, Back, Style
init()
#I have created a variable called Task_During_day and Task_during_Month
Tasks_During_Day = {day: [] for day in ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]}
Tasks_During_Month = {month: [] for month in ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER","NOVEMBER","DECEMBER"]}
# I am defining a function called Adding_Task
# to reduces errors in comparing user input to the day and month I am converting the input to upper case
def Adding_Task():
    period = input(Style.RESET_ALL +"Do You Want To Add A Task To A 'Day' Or A 'Month'? ").upper()
    # If statement is checking if user has selected a day it is asking for the day of the week and tasks
    if period =='DAY':
        day = input("Please Enter The Day Of The Week: ").upper()
        task = input("Please Enter The Task: ").upper()
        # If statement is checking if the statement is true it will append the task to the task list
        if day in Tasks_During_Day:
            Tasks_During_Day[day].append(task)
            print(Fore.GREEN + f"Has Been added to\n {day}.")
            #else function is used to say if the condition is not true then do this
        else:
            print(Fore.RED + "Invalid Day Of The Week.")
            # The Elif statement  is used to check more that one conditions at the same time
    elif period == 'MONTH':
        month = input(Style.RESET_ALL + "Please Enter The Month: ").upper()
        task = input("Please Enter The Task: ").upper()
        # If statement is checking if the statement is true
        if month in Tasks_During_Month:
            Tasks_During_Month[month].append(task)
            print(Fore.GREEN + f"Task Has Been Added To {month}.")
            # Else function is used to say if the condition is not true then do this
        else:
            print(Fore.RED + "Invalid Month.\n")
            # Else function is used to say if the condition is not true then do this
    else:
        print(Fore.RED + "Invalid choice. Please Choose 'Day' Or 'Month'.")

#def is used to define the function seeing_task
def Seeing_Tasks():
    period = input("Do You Want To View Tasks For A 'Day' Or A 'Month'? ").upper()
    # If statement is checking if the statement is true
    if period == 'DAY':
        day = input("Please Enter The Day Of The Week: ").upper()
        # If statement is checking if the statement is true
        if day in Tasks_During_Day:
            print(f"Tasks For {day}: {Tasks_During_Day[day]}")
            # Else function is used to say if the condition is not true then do this using .upper()
        else:
            print(Fore.RED + "Invalid Day Of The Week.")
    elif period == 'MONTH':
        month = input(Style.RESET_ALL + "Please Enter The Month: ").upper()
        # If statement is checking if the statement is true
        if month in Tasks_During_Month:
            print(f"Tasks For {month}: {Tasks_During_Month[month]}")
            # Else function is used to say if the condition is not true then do this
        else:
            print(Fore.RED + "Invalid Month.")
            # Else function is used to say if the condition is not true then do this
    else:
        print(Fore.RED + "Invalid Choice. Please Choose 'Day' Or 'Month'.")

#def is used to define the function Remove_task
def Remove_Task():
    period = input(Style.RESET_ALL + "Are You Sure You Want To Delete A Task From A 'Day' Or A 'Month'? ").upper()
    # If statement is checking if the statement is true
    if period == 'DAY':
        day = input("Please Enter The Day Of The Week: ").upper()
        # If statement is checking if the statement is true
        if day in Tasks_During_Day:
            task = input("Please Enter The Task To Delete: ").upper()
            # If statement is checking if the statement is true
            if task in Tasks_During_Day[day]:
                Tasks_During_Day[day].remove(task)
                print(Fore.GREEN + f"Task Has Been Removed From {day}.")
                # Else function is used to say if the condition is not true then do this
            else:
                print(Fore.RED + "Task Has Not Been Found.")
                # Else function is used to say if the condition is not true then do this
        else:
            print(Fore.RED + "Invalid Day Of the Week.")
            # The Elif statement  is used to check more that one conditions at the same time
    elif period == 'MONTH':
        month = input(Style.RESET_ALL + "Enter The Month: ").upper()
        # If statement is checking if the statement is true
        if month in Tasks_During_Month:
            task = input("Enter The Task To Delete: ").upper()
            # If statement is checking if the statement is true
            if task in Tasks_During_Month[month]:
                Tasks_During_Month[month].remove(task)
                print(Fore.GREEN + f"Task Has Been Removed from {month}.")
                # Else function is used to say if the condition is not true then do this
            else:
                print(Fore.RED + "Task Has Not Been Found.")
                # Else function is used to say if the condition is not true then do this
        else:
            print(Fore.RED + "Invalid month.")
            # Else function is used to say if the condition is not true then do this
    else:
        print(Fore.RED + "Invalid choice. Please Choose 'Day' or 'Month'.")

# While true is a forever loop until condition is not meat
while True:
    print(Style.RESET_ALL + "Please Select An Option From The Task Management System Menu\n")
    print("1: Add a Task")
    print("2: View Tasks")
    print("3: Delete a Task")
    print("4: Exit")

    choice = input("Please Choose an option from the menu: ")
    # If statement is checking if the statement is true
    if choice == '1':
        Adding_Task()
        # The Elif statement  is used to check more that one conditions at the same time
    elif choice == '2':
        Seeing_Tasks()
        # The Elif statement  is used to check more that one conditions at the same time
    elif choice == '3':
        Remove_Task()
        # The Elif statement  is used to check more that one conditions at the same time
    elif choice == '4':
        print("You Are Exiting the program. Goodbye!")
        break
        # Else function is used to say if the condition is not true then do this
    else:
        print("Invalid input. Please choose a valid option.")

