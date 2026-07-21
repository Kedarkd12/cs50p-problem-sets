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
