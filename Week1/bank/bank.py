greeting = input("Greeting: ")

greeting = greeting.split()[0].lower().strip("," "." "!")


if greeting == "hello":
    print("$0")
    quit()

greeting = greeting[0]

if greeting == "h":
    print("$20")

else:
    print("$100")
