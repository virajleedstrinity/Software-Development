#i have created a variable called Task_During_day and Task_during_Month
Tasks_During_Day = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}
Tasks_During_Month = {month: [] for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October","November","December"]}

# I am defining a function called Adding_Task
def Adding_Task():
    period = input("Do You Want To Add A Task To A 'Day' Or A 'Month'? ").capitalize()
    # If statement is checking if the statement is true
    if period == 'Day':
        day = input("Please Enter The Day Of The Week: ")
        task = input("Please Enter The Task: ")
        # If statement is checking if the statement is true
        if day in Tasks_During_Day:
            Tasks_During_Day[day].append(task)
            print(f"Task Has Been added to {day}.")
            #Else function is used to say if the condition is not true then do this
        else:
            print("Invalid Day Of The Week.")
            # The Elif statement  is used to check more that one conditions at the same time
    elif period == 'Month':
        month = input("Please Enter The Month: ")
        task = input("Please Enter The Task: ")
        # If statement is checking if the statement is true
        if month in Tasks_During_Month:
            Tasks_During_Month[month].append(task)
            print(f"Task Has Been Added To {month}.")
            # Else function is used to say if the condition is not true then do this
        else:
            print("Invalid Month.")
            # Else function is used to say if the condition is not true then do this
    else:
        print("Invalid choice. Please Choose 'Day' Or 'Month'.")

#def is used to define the function seeing_task
def Seeing_Tasks():
    period = input("Do You Want To View Tasks For A 'Day' Or A 'Month'? ")
    # If statement is checking if the statement is true
    if period == 'day':
        day = input("Please Enter The Day Of The Week: ")
        # If statement is checking if the statement is true
        if day in Tasks_During_Day:
            print(f"Tasks For {day}: {Tasks_During_Day[day]}")
            # Else function is used to say if the condition is not true then do this
        else:
            print("Invalid Day Of The Week.")
    elif period == 'Month':
        month = input("Please Enter The Month: ")
        # If statement is checking if the statement is true
        if month in Tasks_During_Month:
            print(f"Tasks For {month}: {Tasks_During_Month[month]}")
            # Else function is used to say if the condition is not true then do this
        else:
            print("Invalid Month.")
            # Else function is used to say if the condition is not true then do this
    else:
        print("Invalid Choice. Please Choose 'Day' Or 'Month'.")

#def is used to define the function Remove_task
def Remove_Task():
    period = input("Are You Sure You Want To Delete A Task From A 'Day' Or A 'Month'? ")
    # If statement is checking if the statement is true
    if period == 'day':
        day = input("Please Enter The Day Of The Week: ")
        # If statement is checking if the statement is true
        if day in Tasks_During_Day:
            task = input("Please Enter The Task To Delete: ")
            # If statement is checking if the statement is true
            if task in Tasks_During_Day[day]:
                Tasks_During_Day[day].remove(task)
                print(f"Task Has Been Removed From {day}.")
                # Else function is used to say if the condition is not true then do this
            else:
                print("Task Has Not Been Found.")
                # Else function is used to say if the condition is not true then do this
        else:
            print("Invalid Day Of the Week.")
            # The Elif statement  is used to check more that one conditions at the same time
    elif period == 'Month':
        month = input("Enter The Month: ")
        # If statement is checking if the statement is true
        if month in Tasks_During_Month:
            task = input("Enter The Task To Delete: ")
            # If statement is checking if the statement is true
            if task in Tasks_During_Month[month]:
                Tasks_During_Month[month].remove(task)
                print(f"Task Has Been Removed from {month}.")
                # Else function is used to say if the condition is not true then do this
            else:
                print("Task Has Not Been Fund.")
                # Else function is used to say if the condition is not true then do this
        else:
            print("Invalid month.")
            # Else function is used to say if the condition is not true then do this
    else:
        print("Invalid choice. Please Choose 'Day' or 'Month'.")

# While true is a forever loop until condition is not meat
while True:
    print("\nPlease Select An Option From The Task Management System Menu")
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

