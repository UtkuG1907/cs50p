amount = 50
insert = 25

print("Amount Due:",amount)

while amount > 0:
    insert = int(input("Insert Coin: "))
    if insert == 5 or insert == 10 or insert == 25:
        amount -= insert
    if amount > 0:
        print("Amount Due:",amount)

print("Change Owed:",-amount)
