while True:
    try:
        fuelfraction = input("Fraciton: ")

        fuel, tank= fuelfraction.split("/")

        fuel = int(fuel)
        tank = int(tank)
    except ValueError:
        pass
    else:
            if fuel<=tank:
                if tank != 0:
                    break

per = fuel / tank * 100
per = round(per)

if per >= 99:
    print("F")
elif per <= 1:
    print("E")
else:
    print(f"{per}%")
