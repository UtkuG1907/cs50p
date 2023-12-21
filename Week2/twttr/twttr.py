message = input("Input: ")
vowels = ["a","A","e","E","I","i","u","U","o","O"]

print("Output: ",end="")

for c in message:
    if c not in vowels:
        print(c, end="")
