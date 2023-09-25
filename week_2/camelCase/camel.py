def main():
    camel = input("camelCase: ")
    print("snake_case: " + snake_case(camel))

def snake_case(name):
    name1 = ""
    for letter in name:
        if letter.isupper():
            name1 = name1 + "_"
        name1 = name1 + letter
    return name1.lower()


main()
