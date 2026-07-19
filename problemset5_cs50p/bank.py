def main():
    greet=input("Greeting: ").strip()
    print("$",value(greet),sep="")

def value(greeting):
    if greeting.startswith("hello") | greeting.startswith("Hello") | greeting.startswith("HELLO"):
        return 0
    elif greeting.startswith("h") | greeting.startswith("H"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
