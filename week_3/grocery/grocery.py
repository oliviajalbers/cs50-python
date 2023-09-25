def main():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] = grocery_list[item] + 1
            else:
                grocery_list[item] = 1
        except EOFError:
            break

    grocery_list_keys = sorted(list(grocery_list.keys()))
    for item in grocery_list_keys:
        print(str(grocery_list[item]) + " " + item)



main()
