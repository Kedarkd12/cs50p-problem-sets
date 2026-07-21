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
