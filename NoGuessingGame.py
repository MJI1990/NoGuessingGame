import random

RandomNumber = random.randrange(1, 10)

while True:
    UserInput = int(input("Enter a number between 1 and 10: "))

    if UserInput > RandomNumber:
        print("You guessed too high")
    elif UserInput < RandomNumber:
        print("You guessed too low")
    else:
        print("You won")
        print(f"The number was {RandomNumber}")
        break
