import random
def main():
    level = get_level()
    correct = 0
    for problem in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        attempt = 0
        while True:
            user_answer = input(str(x) + " + " + str(y) + " = ")
            if answer == int(user_answer):
                correct += 1
                break
            else:
                attempt += 1
                if attempt < 3:
                    print("EEE")
                if attempt >= 3:
                    print(str(x) + " + " + str(y) + " = " + str(answer))
                    break

    print("Score: " + str(correct))

def get_level():
    while True:
        level = input("Level: ")
        if level == "1" or level == "2" or level == "3":
            return level

def generate_integer(level):
    if level == "1":
        integer = random.randint(0, 9)
        return integer
    elif level == "2":
        integer = random.randint(10, 99)
        return integer
    else:
        integer = random.randint(100, 999)
        return integer

if __name__ == "__main__":
    main()
