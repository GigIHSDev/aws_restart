import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)
isGuessRight = False


while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

#While the guess number is not correct or is not equal to true, enter loop
#let them know they guessed wrong and should try gain. Tell them to Try a number between 1 and 10.
#If the customer guesses the correct number between 1 and 10
#The loop will continue until the customer guesses correctly.




