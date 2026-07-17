#fuel gauge
while True:
    try:
        z=input("Fraction:").split("/")
        x=int(z[0])
        y=int(z[1])
        if x>y:
            continue
        if x<0 or y<0:
            continue
        elif y==0:
            raise ZeroDivisionError
        else:
            break
    except ValueError:
        pass
k=x/y*100
if k<=1:
    print("E")
elif k>=99:
    print("F")
else:
    k=round(k,0)
    k=int(k)
    print(k,"%",sep="")

#Felipes tacqueria
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

#grocery list
items={}
while True:
    try:
        name=input().upper()
        if name in items:
            items[name]+=1
        else:
            items[name]=1
    except EOFError:
        break
    except KeyError:
        break
for item in sorted(items):
    print(items[item],item)

#outdated
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    t=input("Date:")
    if "/" in t:
        t=t.split("/")
        month=int(t[0])
        days=int(t[1])
        year=int(t[2])
        if month>12 or month<1:
            continue
        if days>31 or days<1:
            continue
        else:
            print(f"Date:{year}-{month:02}-{days:02}")
            break

    else:
        t=t.replace(",","").split(" ")
        month=t[0]
        days=int(t[1])
        year=t[2]
        if month not in months:
            continue
        else:
            m=months.index(month)+1
        if m>12 or m<1:
            continue
        if days>31 or days<1:
            continue
        else:
            print(f"Date:{year}-{m:02}-{days:02}")
            break