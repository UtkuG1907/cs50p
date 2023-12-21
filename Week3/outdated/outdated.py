months ={
    "January" : "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

def main():
    date = input("Date: ").strip()
    try:
        month, day, year = date.split("/")
        month, day = int(month), int(day)
        if month >12 or day>31:
            main()
        month, day = str(month), str(day)
        month, day, year= month.zfill(2), day.zfill(2), year.zfill(4)
        print(f"{year}-{month}-{day}")
        quit()
    except ValueError:
        pass
    except EOFError:
        quit()
    try:
        month, day, year= date.split(" ")
        if "," in day:
            day = day.strip(",")
            if month not in months:
                main()
            month = months[month]
            month, day = int(month), int(day)
            if month >12 or day>31:
                main()
            month, day = str(month), str(day)
            month, day, year= month.zfill(2), day.zfill(2), year.zfill(4)
            print(f"{year}-{month}-{day}")
        else:
            main()
    except ValueError:
        main()
main()
