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