# main function getting message from user
def main():
    message = input("Input: ")
    shorted = shorten(message)
    print("Output: ", end="")
    print(shorted)


# remove vowels
def shorten(word):
    vowels = ["a", "e", "i", "u", "o"]
    shortened = []
    for c in word:
        if c.casefold() not in vowels:
            shortened.append(c)
    shortened = str("".join(shortened))
    return shortened


if __name__ == "__main__":
    main()
