def main():
    import sys
    import csv
    from tabulate import tabulate

    # check for correct number of command line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # verify that it is a .csv file
    file_name = sys.argv[1]
    length = len(file_name)
    if file_name[length-1] != "v" or file_name[length-2] != "s" or file_name[length-3] != "c" or file_name[length-4] != ".":
        sys.exit("Not a CSV file")

    #create table
    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            table = []
            headers = []
            headers = next(reader)  
            for row in reader:
                table.append(row)

    except (Exception):
        sys.exit("File does not exist")

    print(tabulate(table, headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
