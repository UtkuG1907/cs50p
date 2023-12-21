import random
import sys

def getting_level(n):
    try:
        n = int(n)
        a = random.randrange(1, n)
        return a
    except ValueError:
        main()
        return None

def main():
    level = input("Level: ")
    random_number = getting_level(level)
    guess = -1
    while guess != random_number:
        guess = int(input("Guess: "))
        if guess > random_number:
            print("Too large!")
        elif guess < random_number:
            print("Too small!")
    print("Just right!")
    sys.exit()

main()
