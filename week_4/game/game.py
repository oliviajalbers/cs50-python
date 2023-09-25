def main():
    import random
    import sys
    while True:
        level = input("Level: ")
        if level.isnumeric() and int(level)
        > 0:
            break
    answer = random.randint(1, int(level))
    while True:
        guess = input("Guess: ")
        if guess.isnumeric():
            guess = int(guess)
            if guess == answer:
                sys.exit("Just right!")
            elif guess > answer:
                print("Too large!")
            else:
                print("Too small!")


main()
