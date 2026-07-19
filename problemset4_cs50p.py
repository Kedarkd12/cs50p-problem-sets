#emojize
import emoji

word=input("Text:")
print("Emojize:",emoji.emojize(word,language="alias"))

# frank,ian and glens letters
from pyfiglet import Figlet
import sys
import random

f=Figlet()
fonts=f.getFonts()
if len(sys.argv)>1:
    if sys.argv[1]!="-f" and sys.argv[1]!="--font":
        sys.exit
    else:
        if sys.argv[2] not in fonts:
            sys.exit
        else:
            f.setFont(font=sys.argv[2])
            b=input("Input:")
            print(f.renderText(b))
else:
    a=input("Input:")
    r=random.choice(f.getFonts())
    f.setFont(font=r)
    print(f.renderText(a))

#adieu,adieu,adieu
import inflect

p=inflect.engine()
items=[]
while True:
    try:
        name=input("Name:").title()
        if name not in items:
            items.append(name)
    except EOFError:
        break
    except KeyError:
        break
print("Adieu, Adieu, to",p.join((items),conj="and",sep=", "))

#guessing game
import random

n=int(input("Level: "))

if n>0:
    r=random.randint(1,n)
    while True:
        g=int(input("Guess: "))
        if g>n or g<0:
            print("Please enter a number within level")
        elif g>r:
            print("Too Large!")
        elif g<r:
            print("Too small!")
        else:
            print("Just Right!")
            break
else:
    print("Enter a valid level")

#little professor
import random


def main():
    level=get_level()
    generate_integer(level)

def get_level():
    while True:
        n=int(input("Level: "))
        if n<1 or n>3:
            continue
        else:
            return n

def generate_integer(level):
    match level:
        case 1:
            for _ in range(10):
                x=random.randint(0,10)
                y=random.randint(0,10)
                z=x+y
                print(x,"+",y,"= ",end="")
                z1=int(input())
                if z1==z:
                    continue
                else:
                    print("EEE")

        case 2:
            for _ in range(10):
                x=random.randint(10,100)
                y=random.randint(10,100)
                z=x+y
                print(x,"+",y,"= ",end="")
                z1=int(input())
                if z1==z:
                    continue
                else:
                    print("EEE")

        case 3:
            for _ in range(10):
                x=random.randint(100,1000)
                y=random.randint(100,1000)
                z=x+y
                print(x,"+",y,"= ",end="")
                z1=int(input())
                if z1==z:
                    continue
                else:
                    print("EEE")
        case _:
            raise ValueError


if __name__ == "__main__":
    main()

#bitcoin price index
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
