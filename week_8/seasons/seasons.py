from datetime import date
import operator
import inflect
import sys
import re

def main():
    bday = input("Date of Birth: ")
    if convert(bday):
        print (convert(bday))
    else:
        sys.exit("Invalid date")

def convert(dob_str):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", dob_str):
        dob_list = dob_str.split("-")
        year = int(dob_list[0])
        month = int(dob_list[1])
        day = int(dob_list[2])
        dob = date(year, month, day)
        today = date.today()
        diff = str(operator.__sub__(today, dob))
        days = int(diff.split(" ")[0])
        minutes = days * 24 * 60
        p = inflect.engine()
        words = p.number_to_words(minutes, andword="")
        words = words.capitalize()
        return (words + " minutes")
    else:
        return None



if __name__ == "__main__":
    main()
