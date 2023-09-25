import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.search(r"^([1-9]|1[0-2]):?([0-5][0-9])? (A|P)M to ([1-9]|1[0-2]):?([0-5][0-9])? (A|P)M$", s)
    if matches:
        result = ""
        start_h = matches.group(1)
        start_m = matches.group(2)
        x = matches.group(3)
        end_h = matches.group(4)
        end_m = matches.group(5)
        y = matches.group(6)

        if x == "A":
            if int(start_h) < 10:
                result = result + "0" + start_h + ":"
            elif start_h == "12":
                result = result + "00:"
            else:
                result = result + start_h + ":"
        else:
            if start_h == "12":
                result = result + start_h + ":"
            else:
                start_h = int(start_h) + 12
                result = result + str(start_h) + ":"

        if start_m:
            result = result + start_m + " to "
        else:
            result = result + "00 to "

        if y == "A":
            if int(end_h) < 10:
                result = result + "0" + end_h + ":"
            elif end_h == "12":
                result = result + "00:"
            else:
                result = result + end_h + ":"
        else:
            if end_h == "12":
                result = result + end_h + ":"
            else:
                end_h = int(end_h) + 12
                result = result + str(end_h) + ":"

        if end_m:
            result = result + end_m
        else:
            result = result + "00"

        return(result)


    else:
        raise ValueError

if __name__ == "__main__":
    main()
