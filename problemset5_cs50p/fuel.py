def main():
    while True:
        try:
            z=input("Fraction:")
            percent=convert(z)
            print(gauge(percent))
        except (ZeroDivisionError,ValueError):
            pass

def convert(fraction):
        x, y=fraction.split("/")
        x=int(x)
        y=int(y)
        if x>y and y!=0:
            raise ValueError
        if x<0 or y<0:
            raise ValueError
        else:
            k=x/y
            return k

def gauge(percentage):
    percentage=percentage*100
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        percentage=round(percentage,0)
        percentage=int(percentage)
        return f"{percentage}%"


if __name__ == "__main__":
    main()
