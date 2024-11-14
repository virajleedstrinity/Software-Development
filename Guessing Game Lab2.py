#importing the function random
import random
#The function def is used the define guess game
def guessgame():
    number=random.randint(1,100)
    maxattempts=9
    tempscore=10
    score=0
    guess=""
    # The function while true is used to run the function if the condition is true
    while guess!=number or maxattempts!=0:
        #Try function is testing the code for any errors
        try:
            guess=int(input("Guess a number between 1,100: "))
            #The if statement is used to check if the function is true
            if isinstance(guess, float) or guess>100 or guess<0:
                print("Please enter a valid number")
                #The else functions decides what to do if the function is false
            else:
                # The if function is checking if the function is true
                if guess < number:
                    print(f"\033[41m`Your number is less than the number I am thinking of \nYou only have {maxattempts - 1} guess now\n")
                    maxattempts -= 1
                    tempscore -= 1
                    #The elif function is used in a conditional functions to check multiple functions
                elif guess > number:
                    print(f"\033[41m`Your number is larger than the number I am thinking of \nYou only have {maxattempts - 1} guess now\n")
                    maxattempts -= 1
                    tempscore -= 1
                    # The elif function is used in a conditional function to check multiple functions
                elif guess == number:
                    print("\033[41m`Correct\n")
                    maxattempts -= 1
                    tempscore -= 1
                    #The return function ends the execution
                    return tempscore
                # The if function is checking if the function is true
                if maxattempts == 0:
                    print(f"\033[41m`You have run out of guesses \nthe number was {number}\nbetter luck next time \n")
                    # The return function ends the execution
                    return score
                #The except function allows function to take another option if the code fails.
        except ValueError:
            print("\033[41m`You must guess a number first\n")

#def function is used to define the function main
def main():
    scores=[]
    # For i in range 3 means that the function will loop 3 times
    for i in range(3):
        print(f"\033[41m`Round number{i+1}\n")
        score=guessgame()
        scores.append(score)
    totalscore=scores[0]+scores[1]+scores[2]
    # The if function is checking if the function is true
    if totalscore/3>=7:
        print(f"\033[41m`Total score is {totalscore} excellent guessing\n")
        # The elif function is used in a conditional function to check multiple functions
    elif totalscore/3<=6 and totalscore/3>1:
        print(f"\033[41m`Total score is {totalscore} good job\n")
        # The else function decide what to do if the function is false
    else:
        print(f"\033[41m`Total score {totalscore} better luck next time\n")
        return
    again = input("Do you want to play again y/n")
    # The if function is checking if the function is true
    if again.lower()=="n":
        print("\033[41m`Thanks for playing\n")
        # The if function is checking if the function is true
    if again.lower()=="y":
        main()
        # The if function is checking if the function is true
if __name__=="__main__":
    main()