def main():
    import requests
    import sys
    import json

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    n = sys.argv[1]

    try:
        n = float(n)
    except:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        price = o["bpi"]["USD"]["rate"]
        price = price.replace(",", "")
        total = n * float(price)
        print(f"${total:,.4f}")
    except requests.RequestException:
        sys.exit



if __name__ == "__main__":
    main()
