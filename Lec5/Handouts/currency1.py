import requests

def main():
    res = requests.get("http://data.fixer.io/latest?access_key=e3b4139081204a9123d307e12bdc90e9&symbols=USD,GBP,AUD")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"]["GBP"]
    print(f"1 EUR is equal to {rate} EUR")

if __name__ == "__main__":
    main()
