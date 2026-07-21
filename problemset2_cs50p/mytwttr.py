k=input("Input:")
print("Output:",end="")
for j in k:
    match j:
        case "a" | "A":
            j.replace("a","").replace("A","")
        case "e" | "E":
            j.replace("e","").replace("E","")
        case "i" | "I":
            j.replace("i","").replace("I","")
        case "o" | "O":
            j.replace("o","").replace("O","")
        case "u" | "U":
            j.replace("u","").replace("U","")
        case _:
            print(j,end="")