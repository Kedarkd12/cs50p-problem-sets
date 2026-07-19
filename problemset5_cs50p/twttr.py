def main():
    k=input("Input:")
    print("Output:",shorten(k))

def shorten(word):
    result=""
    for j in word:
        match j:
            case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
                pass
            case _:
                result+=j
    return result

if __name__ == "__main__":
    main()