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