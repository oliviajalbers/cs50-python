def main():
    import sys

    # check for correct number of command line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # verify that it is a .py file
    file_name = sys.argv[1]
    length = len(file_name)
    if file_name[length-1] != "y" or file_name[length-2] != "p" or file_name[length-3] != ".":
        sys.exit("Not a python file")

    #count lines
    counter = 0
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                elif line[0] == "#":
                    continue
                else:
                    counter += 1
    except (Exception):
        sys.exit("File does not exist")
    print(counter)
    return(counter)


if __name__ == "__main__":
    main()
