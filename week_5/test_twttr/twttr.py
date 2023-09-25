def main():
    tweet = input("Tweet: ")
    tweet = shorten(tweet)
    print(tweet)


def shorten(word):
    new_tweet = ""
    for letter in word:
        if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
            continue
        else:
            new_tweet = new_tweet + letter
    return new_tweet


if __name__ == "__main__":
    main()
