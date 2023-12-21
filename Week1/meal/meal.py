def main():
    time = input("What time is it? ")


    timedecimal = convert(time)
    if 7 <= timedecimal <= 8:
        print("Breakfast time")
    elif 12 <= timedecimal <= 13:
        print("Lunch time")
    elif 18 <= timedecimal <=19:
        print("Dinner time")
    return


def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    minute /= 60
    timedecimal = float(hour + minute)

    return timedecimal


if __name__ == "__main__":

    main()
