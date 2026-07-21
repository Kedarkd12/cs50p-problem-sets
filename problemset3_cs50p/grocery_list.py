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
