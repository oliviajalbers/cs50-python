def main():
    import sys
    import random
    from pyfiglet import Figlet
    figlet = Figlet()
    font_list = figlet.getFonts()

    if len(sys.argv) == 1:
        font1 = random.choice(font_list)
        text = input("Input: ")
        figlet.setFont(font=font1)
        print("Output:")
        print(figlet.renderText(text))

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            font1 = sys.argv[2]
            if font1 not in font_list:
                sys.exit("Invalid usage")
            text = input("Input: ")
            figlet.setFont(font=font1)
            print("Output:")
            print(figlet.renderText(text))

        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")



main()
