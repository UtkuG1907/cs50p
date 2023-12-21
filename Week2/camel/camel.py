nickname = input("camelCase: ")

print("snake_case: " ,end="", sep="")

for w in nickname:
    if w.islower():
        print(w, end="", sep="")
    elif w.isupper():
        w = w.lower()
        print("_"+w,end="", sep="")
print("")
