#The import function is getting a random number
import random
#print  function is displaying a range of letter which is a string
print("guess a number between 1 and 100.")
randomNum= random.randint(1,100)
guessestaken= 0
#while True:  this allows the program reapet it self untile the function has met it condtions
while True:
    guess = input("please enter your guess:")
    guess = int(guess)
    # if function will run the program in the conditions has been met
    if guess < randomNum:
        print("That was too low.")
        # elif function allows to check multiple conditions
    elif guess > randomNum:
        print("that was too high!")
        # else function is used to find out what to do if the code is false
    else:
        # The break function will break out the loop
        break
        #The print function is print a string
print("well done you guessed correctly")



