import requests


def main():
    key = 'e3b4139081204a9123d307e12bdc90e9'
    url = "http://data.fixer.io/latest?access_key=" + key
    symbol = input("Enter the currency you like to exchange from EUR: ")
    res = requests.get(url, params={"symbols": symbol})

    if res.status_code != 200:
        raise Exception("Error: API request unsuccessful.")
    data = res.json()
    rate = data["rates"][symbol]
    print(rate)


if __name__ == '__main__':
    main()
