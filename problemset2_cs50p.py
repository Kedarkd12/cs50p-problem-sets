# #camelCase
word=input("camelCase: ")
print("snake_case: ",end="")
for letter in word:
    if letter.isupper():
        print("_"+letter.lower(),end="")
    else:
        print(letter,end="")
print()

# #coke machine
amount=50
coin=0
while amount>0:
    print("Amount Due:",amount)
    coin=int(input("Enter Coin:"))
    match coin:
        case 25:
            amount-=25
        case 10:
            amount-=10
        case 5:
            amount-=5
        case _:
            continue
if(amount==0):
    print("Change Owed:",amount)
else:
    print("Change Owed:",abs(amount))

#just setting up my twttr
k=input("Input:")
print("Output:",end="")
for j in k:
    match j:
        case "a" | "A":
            j.replace("a","").replace("A","")
        case "e" | "E":
            j.replace("e","").replace("E","")
        case "i" | "I":
            j.replace("i","").replace("I","")
        case "o" | "O":
            j.replace("o","").replace("O","")
        case "u" | "U":
            j.replace("u","").replace("U","")
        case _:
            print(j,end="")

#vanity plate
def main():
    plate = input("\nPlate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    n=len(s)
    if n<=6 and n>=2:
        if s.isalnum():
            if s[0].isalpha() and s[1].isalpha():
                if digs(s):
                   if chars(s):
                       return True 

def digs(s):
    for char in s:
        if char.isdigit():
            if char!="0":
                return True
            else:
                return False
        else:
            return True
            
def chars(s):
    number_started=False
    for char in s:
        if char.isdigit():
            number_started=True
        elif char.isalpha() and number_started:
            return False
        return True
        
main()

#nutrition table
fruits=[
    {"name":"apple","calories":"130"},
    {"name":"avocado","calories":"50"},
    {"name":"banana","calories":"110"},
    {"name":"cantaloupe","calories":"50"},
    {"name":"grapefruit","calories":"60"},
    {"name":"grapes","calories":"90"},
    {"name":"honeydew melon","calories":"50"},
    {"name":"kiwifruit","calories":"90"},
    {"name":"lemon","calories":"15"},
    {"name":"lime","calories":"20"},
    {"name":"nectarine","calories":"60"},
    {"name":"orange","calories":"80"},
    {"name":"peach","calories":"60"},
    {"name":"pear","calories":"100"},
    {"name":"pineapple","calories":"50"},
    {"name":"plums","calories":"70"},
    {"name":"strawberries","calories":"50"},
    {"name":"sweet cherries","calories":"100"},
    {"name":"tangerine","calories":"50"},
    {"name":"watermelon","calories":"80"},
]
f=input("Item:").lower()
for fruit in fruits:
    if fruit["name"]==f:
        print("Calories:",fruit["calories"])