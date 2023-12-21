grocery = {}

while True:
    try:
        item = input().upper().strip()
        if item in grocery:
            grocery[item] = grocery[item] + 1
        else:
            grocery[item] = 1
    except EOFError:
        break

grocery = dict(sorted(grocery.items()))

for item in grocery:
    print(grocery[item], item)
