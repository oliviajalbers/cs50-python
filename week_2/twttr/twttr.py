def main():
    tweet = input("Tweet: ")
    tweet = no_vowels(tweet)
    print(tweet)

def no_vowels(tweet):
    new_tweet = ""
    for letter in tweet:
        if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
            continue
        else:
            new_tweet = new_tweet + letter
    return new_tweet

main()
