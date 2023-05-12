def main():
    greeting = input("Greeting: ")
    greeting = greeting.lower().strip()
    if greeting[0] == "h" and greeting[1] == "e" and greeting[2] == "l" and greeting[3] == "l" and greeting[4] == "o":
        print ("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")

main()
