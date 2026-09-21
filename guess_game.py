import random

num = random.randint(1, 10)

while True:
    guess_num = int(input("Guess the number between 1 and 10: "))

    if (guess_num == num):
        print("Correct! You guessed the number:", guess_num)
        break
    elif (guess_num < num):
        print("The number is bigger than your guess.")
    else:
        print("The number is smaller than your guess.")
