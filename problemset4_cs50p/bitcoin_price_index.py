import requests
import json
import sys

if len(sys.argv)==1:
    sys.exit("Missing command line argument")
elif len(sys.argv)>2:
    sys.exit("Too many arguments")
try:
    n=float(sys.argv[1])
except ValueError:
    sys.exit("Argument is not a number")

try:
    response=requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=6c4f48a9ee1dfc9ceb4eadfa086349aad9537db56b6da9735affc10bebf65943")
    o=response.json()
    price=float(o["data"]["priceUsd"])
    total=n*price
    print(f"${total:,.4f}")

except requests.RequestException:
    pass
