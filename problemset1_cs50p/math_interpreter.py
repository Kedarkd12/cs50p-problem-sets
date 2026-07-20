x, y, z=input("Enter an expression:").strip().split(" ")
x=float(x)
z=float(z)
match y:
    case " + " | "+":
        print("Result=",x+z)
    case " - " | "-":
        print("Result=",x-z)
    case " * " | "*":
        print("Result=",x*z)
    case " / " | "/":
        print("Result=",x/z)
    case _:
        print("Invalid expression")
