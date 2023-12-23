def main():
    fuel_fraction = input("Fraciton: ")
    per = convert(fuel_fraction)
    print(gauge(per))


def convert(fraction):
    fuel, tank = fraction.split("/")
    try:
        fuel = int(fuel)
        tank = int(tank)
    except ValueError:
        raise ValueError
    else:
        if tank == 0:
            raise ZeroDivisionError
        if fuel > tank:
            raise ValueError

        return round(fuel / tank * 100)


def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
