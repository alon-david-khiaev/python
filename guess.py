import random

number = random.randint(1, 5)
# print("The correct number is:", number)

p = input("Guess a number between 1 and 5: ")
print("You guessed:", p)

for i in range(3):
    if int(p) == number:
        print("You guessed correctly! The number was", number)
        break
    else:
        print("Wrong guess, try again.")
        p = input("Guess a number between 1 and 5: ")