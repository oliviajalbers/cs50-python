def main():
    import sys
    import csv
    from tabulate import tabulate

    # check for correct number of command line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # verify that both command line arguments are .csv files
    old_file = sys.argv[1]
    length = len(old_file)
    if old_file[length-1] != "v" or old_file[length-2] != "s" or old_file[length-3] != "c" or old_file[length-4] != ".":
        sys.exit("Not a CSV file")
    new_file = sys.argv[2]
    length = len(new_file)
    if new_file[length-1] != "v" or new_file[length-2] != "s" or new_file[length-3] != "c" or new_file[length-4] != ".":
        sys.exit("Not a CSV file")


    # create new file and write header
    with open(new_file, "w") as file1:
        writer = csv.DictWriter(file1, fieldnames = ["first", "last", "house"])
        writer.writeheader()
    # write all columns
    try:
        with open(old_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                name1 = name.split(",")
                first = name1[1].strip()
                last = name1[0].strip()
                house = row["house"]
                with open(new_file, "a") as file1:
                    writer = csv.writer(file1)
                    writer.writerow([first, last, house])


    # handle invalid file
    except (Exception):
        sys.exit(f"Could not read {old_file}")

if __name__ == "__main__":
    main()
