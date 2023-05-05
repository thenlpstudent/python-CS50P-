import requests
import sys

BITCOIN_PRICE_INDEX_URL = "https://api.coindesk.com/v1/bpi/currentprice.json";


def main(args):
    if not len(args) >= 2:
        exit_program("Missing command-line argument")

    print(format_price(get_bitcoin_price() * get_qty(args[1])))


def get_qty(num):
    try:
        f = float(num)
        if f <= 0:
            raise ValueError
        return f
    except ValueError:
        exit_program("Command-line argument is not a valid number")


def get_bitcoin_price():
    try:
        r = requests.get(BITCOIN_PRICE_INDEX_URL)
        return float(r.json()["bpi"]["USD"]["rate_float"])
    except requests.RequestException:
        exit_program("Internal error occurred when sending a request, please check your connection!")
    except KeyError:
        exit_program("JSON formatted incorrect!")
    except ValueError:
        exit_program("Error in parsing bitcoin price!")


def format_price(price):
    return f"${price:,.4f}";


def exit_program(message):
    print(message)
    sys.exit()


if __name__ == "__main__":
    main(sys.argv)
