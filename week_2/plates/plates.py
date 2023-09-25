def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # verify that the length is between 2 and 6 characters
    length = len(s)
    if length < 2 or length > 6:
        return False
    # verify that the first two characters are letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    # verify that all characters are letters or numbers
    if s.isalnum() == False:
        return False
    # verify that numbers are not in the middle of the plate
    x = 0
    for character in s:
        if character.isnumeric():
            x = 1
        if character.isalpha() and x > 0:
            return False
    # verify that the first number is not 0
    for character in s:
        if character.isnumeric() and character != "0":
            break
        elif character.isnumeric() and character == "0":
            return False
    # plate is valid
    return True


main()
