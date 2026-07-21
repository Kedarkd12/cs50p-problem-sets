felipes={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
Total=0
for _ in felipes:
    try:
        name=input("Item:").title()
    except EOFError:
        break
    except KeyError:
        break
    else:
        if name in felipes:
            Total += felipes[name]
            print(f"Total: ${Total:.2f}",sep="")
        else:
            continue
