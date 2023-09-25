def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    left = fraction.split("/")[0]
    right = fraction.split("/")[1]
    try:
        left = int(left)
    except:
        raise ValueError()
    try:
        right = int(right)
    except:
        raise ValueError()

    if right == 0:
        raise ZeroDivisionError()
    if left > right:
        raise ValueError()
    percent = round((left/right)*100)
    return percent

def gauge(percentage):
    if percentage >= 99 and percentage <= 100:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(str(percentage) + "%")

if __name__ == "__main__":
    main()
