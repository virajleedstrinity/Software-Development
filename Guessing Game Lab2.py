#importing the function random
import random
#The function def is used the define guess game
def guessgame():
    number=random.randint(0,100)
    maxattempts=9
    tempscore=10
    score=0
    guess=""
    # The function while true is used to run the function if the condition is true
    while guess!=number or maxattempts!=0:
        #Try function is testing the code for any errors
        try:
            guess=int(input("guess a number between 0,100: "))
            #The if statment is used to check if the function is true
            if isinstance(guess, float):
                print("please only use whole number ")
                #The else fuctions desides what to do if the function is false
            else:
                #The if function is checking if the function is true
                if guess < number:
                    print(f"\033[41m`your number is less than the number i am thinking\nyou only have {maxattempts - 1} guess now\n")
                    maxattempts -= 1
                    tempscore -= 1
                    #The elif function is used in a condtiontal fuction to check multiple functions
                elif guess > number:
                    print(f"\033[41m`your number is larger than the number i am thinking\nyou only have {maxattempts - 1} guess now\n")
                    maxattempts -= 1
                    tempscore -= 1
                    # The elif function is used in a conditional function to check multiple functions
                elif guess == number:
                    print("\033[41m`correct\n")
                    maxattempts -= 1
                    tempscore -= 1
                    #The return function ends the excution
                    return tempscore
                # The if function is checking if the function is true
                if maxattempts == 0:
                    print(f"\033[41m`you have run out of guesses\nthe number was {number}\nbetter luck next time \n")
                    # The return function ends the excution
                    return score
                #The except function allows function to take another option if the code fails.
        except ValueError:
            print("\033[41m`you must guess a number first\n")

#def function is used to define the function main
def main():
    scores=[]
    # For i in range 3 means that the function will loop 3 times
    for i in range(3):
        print(f"\033[41m`round number{i+1}\n")
        score=guessgame()
        scores.append(score)
    totalscore=scores[0]+scores[1]+scores[2]
    # The if function is checking if the function is true
    if totalscore/3>=7:
        print(f"\033[41m`total score is{totalscore}excellent guessing\n")
        # The elif function is used in a conditional function to check multiple functions
    elif totalscore/3<=6 and totalscore/3>1:
        print(f"\033[41m`total score is{totalscore}good job\n")
        # The else function decide what to do if the function is false
    else:
        print(f"\033[41m` total score {totalscore}better luck next time\n")
        return
    again = input("do you want to play again y/n")
    # The if function is checking if the function is true
    if again.lower()=="n":
        print("\033[41m`thanks for playing\n")
        # The if function is checking if the function is true
    if again.lower()=="y":
        main()
        # The if function is checking if the function is true
if __name__=="__main__":
    main()