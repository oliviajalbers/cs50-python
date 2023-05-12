def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")

def convert(t):
    parts = t.split(":")
    hour = int(parts[0])
    minute = int(parts[1])
    fraction = minute / 60
    total_hours = hour + fraction
    return total_hours

if __name__ == "__main__":
    main()
