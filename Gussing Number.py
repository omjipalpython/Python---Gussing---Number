import random

computer = random.randint(1,100)

chance = 3

while chance > 0:

    n = int(input("Choose Number (1-100): "))

    if n == computer:
        print("You Win...")
        break

    elif n > computer:
        print("Very Large ↑")

    else:
        print("Very Low ↓")

    chance -= 1
    print("Chances left:", chance)

if chance == 0:
    print("Game Over ")
    print("Correct Number was:", computer)