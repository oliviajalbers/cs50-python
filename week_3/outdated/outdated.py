def main():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December" : 12
    }
    while True:
        try:
            user_date = input("date: ")
            date = user_date.split("/")
            if len(date) < 3:
                date = user_date.split(" ")
                month = months[date[0].strip()]
                if "," not in date[1]:
                    raise Exception()
            else:
                month = date[0].strip()

            day = date[1].replace(",", "").strip()
            year = date[2].strip()
            if int(day) <= 31 and int(month) <= 12:
                break
        except (ValueError, Exception):
            pass

    print(year + "-" + f"{int(month):02}" + "-" + f"{int(day):02}")




main()
