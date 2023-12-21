import sys
import requests


def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    value = btc()
    value = float(value.replace(",", ""))

    amount = value * number

    print(f"${amount:,.4f}")

#to get instant value of bitcoin
def btc():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Request Exception occurred. Exiting...")
    o = response.json()

    value = o["bpi"]["USD"]["rate"]
    return value


if __name__ == "__main__":
    main()