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
