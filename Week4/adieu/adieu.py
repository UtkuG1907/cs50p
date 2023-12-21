import inflect
p = inflect.engine()

names = []

def main():
    name = input("Name: ")
    try:
        while name != "":
            names.append(name)
            name = input("Name: ")
    except EOFError:
        printer(names)

def printer(a):
    formatted_names = p.join(a)
    print("Adieu, adieu, to",formatted_names)

main()
