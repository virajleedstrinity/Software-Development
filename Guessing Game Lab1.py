#The import function is getting a random number
import random
#print  function is displaying a range of letter which is a string
print("guess a number between 1 and 100.\n")
randomNum= random.randint(1,100)

guessestaken= 0
#while True:  this allows the program repeats itself until the function has met it conditions
while True:
    guess = int(input("please enter your guess:"))
    if guess<=100:
        # if function will run the program in the conditions has been met
        if guess < randomNum:
            print("\033[42m`That was too low.\n")
            # elif function allows to check multiple conditions
        elif guess > randomNum:
            print("\033[42m`That was too high!\n")
            # else function is used to find out what to do if the code is false
        else:
            # The break function will break out the loop
            break
            #The print function is print a string
    else:
        print("number out if range")
        continue

print("\033[42m`well done you guessed correctly\n")
