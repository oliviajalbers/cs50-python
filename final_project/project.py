import sys
import operator
import tabulate
contact_book = []
def main():
    while True:
        action = input("add, remove, update, or exit: ")
        action = action.lower().strip()
        if action == "add":
            name = input("name: ")
            number = input("number: ")
            dataset = add(name, number)
            print(make_table(dataset))
        elif action == "remove":
            name = input("name: ")
            dataset = remove(name)
            if dataset == 'name not in contacts':
                print(dataset)
            else:
                print(make_table(dataset))
        elif action == "update":
            current_name = input("current name: ")
            new_name = input("new name: ")
            new_number = input("new number: ")
            dataset = update(current_name, new_name, new_number)
            if dataset == 'name not in contacts':
                print(dataset)
            else:
                print(make_table(dataset))
        elif action == "exit":
            sys.exit()
        else:
            print("invalid entry")

def add(name, number):
    person = {"name": name, "number": number}
    contact_book.append(person)
    return sort_book(contact_book)


def remove(name):
    for i in range(len(contact_book)):
        if contact_book[i]["name"] == name:
            del contact_book[i]
            return sort_book(contact_book)
    return('name not in contacts')


def update(current_name, new_name, new_number):
    for i in range(len(contact_book)):
        if contact_book[i]["name"] == current_name:
            contact_book[i] = {"name": new_name, "number": new_number}
            return sort_book(contact_book)
    return('name not in contacts')

def sort_book(b):
    sorted_contact_book = sorted(b, key=operator.itemgetter("name"))
    return sorted_contact_book

def make_table(dataset):
    header = dataset[0].keys()
    rows = [x.values() for x in dataset]
    return(tabulate.tabulate(rows, header))



if __name__ == "__main__":
    main()
