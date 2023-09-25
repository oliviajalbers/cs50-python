def main():
    while True:
        fraction = input("Fraction: ")
        try:
            left = fraction.split("/")[0]
            right = fraction.split("/")[1]
            percent = round((int(left)/int(right))*100)
        except (ValueError, ZeroDivisionError, IndexError):
            pass
        else:
            if percent >= 99 and percent <= 100:
                print("F")
                break
            elif percent <= 1:
                print("E")
                break
            elif percent > 100:
                pass
            else:
                print(str(percent) + "%")
                break

main()
