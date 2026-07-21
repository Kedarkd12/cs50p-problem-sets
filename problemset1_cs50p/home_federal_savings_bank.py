greet=input("Greeting: ").strip()

if greet.startswith("hello") | greet.startswith("Hello") | greet.startswith("HELLO"):
    print("$0")
elif greet.startswith("h") | greet.startswith("H"):
    print("$20")
else:
    print("$100")