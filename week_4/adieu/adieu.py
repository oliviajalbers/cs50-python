def main():
    names = []
    while True:
        try:
            name = input()
            names.append(name)
        except EOFError:
            break
    print("Adieu, adieu, to ", end="")
    length = len(names)
    if length == 1:
        print(names[0])
    elif length == 2:
        print(names[0] + " and " + names[1])
    else:    
        for i in range(length-1):
            print(names[i] + ", ", end="")
        print("and "+ names[length-1])


main()
