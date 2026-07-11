#deep thought
answer=input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip()
match answer:
    case "42" | "forty-two" | "FORTY-TWO" |"FORTY TWO" | "forty two":
        print("Yes")
    case _:
        print("No") 

#home federal savings bank
greet=input("Greeting: ").strip()

if greet.startswith("hello") | greet.startswith("Hello") | greet.startswith("HELLO"):
    print("$0")
elif greet.startswith("h") | greet.startswith("H"):
    print("$20")
else:
    print("$100")

#extensions
extent=input("Enter File name: ").strip()

if extent.endswith(".gif"):
    print("File Type : image/gif")
elif extent.endswith(".jpg"):
    print("File Type : image/jpg")
elif extent.endswith(".jpeg"):
    print("File Type : image/jpeg")
elif extent.endswith(".png"):
    print("File Type : image/png")
elif extent.endswith(".pdf"):
    print("File Type : image/pdf")
elif extent.endswith(".txt"):
    print("File Type : image/txt")
elif extent.endswith(".zip"):
    print("File Type : image/zip")
else:
    print("application/octet-stream")

#math interpreter
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

#mealtime
def main():
    hours,minutes=input("What time is it? ").strip().split(":")
    hours=int(hours)
    minutes=int(minutes)
    convert(hours,minutes)

def convert(x,z):
    if(x==7 and 0<z<60):
        print("Breakfast time")
    elif(x==12 and 00<z<60):
        print("Lunch Time")
    elif(x==18 and 00<z<60):
        print("Dinner Time")

if __name__ == "__main__":
    main()
     