#import random for getting random numbers
import random


#main function for the operation of the Little Professor calculator
def main():
    correct = 0
    n = get_level()
    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        fail = 0
        guess, answer = 0, x + y
        while fail < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess != answer:
                    fail += 1
                    print("EEE")
                else:
                    correct += 1
                    break
                if fail == 3:
                    print(f"{x} + {y} = {answer}")
            except ValueError:
                fail += 1
                print("EEE")
    print(f"Score: {correct}")


#to get number of digits (1-3)
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass

#to get random numbers
def generate_integer(a):
    maxvalue = 10**a - 1
    if a != 1:
        minvalue = 10 ** (a - 1)
    else:
        minvalue = 0
    number = random.randint(minvalue, maxvalue)
    return number


if __name__ == "__main__":
    main()
