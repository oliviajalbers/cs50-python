def main():
    math = input("arithmetic expression: ")
    parts = math.split()
    x = int(parts[0])
    y = parts[1]
    z = int(parts[2])
    if y == "+":
        print(round(float(x + z), 1))
    elif y == "-":
        print(round(float(x - z), 1))
    elif y == "*":
        print(round(float(x * z), 1))
    elif y == "/":
        print(round(float(x / z), 1))
main()
