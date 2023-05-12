def main():
    text = input()
    print(convert(text))

def convert(original):
    smile = original.replace(":)", "🙂")
    final = smile.replace(":(", "🙁")
    return final

main()
