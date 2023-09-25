import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'^<iframe .*src="https?://(?:www\.)?youtube.com/embed/(.+)".*></iframe>$', s):
        x = matches.group(1)
        y = x.split('"')
        new = "https://youtu.be/" + y[0]
        return(new)
    else:
        return None


if __name__ == "__main__":
    main()
