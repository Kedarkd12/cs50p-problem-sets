def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    n=len(s)
    if not 2<=n<=6:
        return False
    if not s.isalnum():
        return False
    if not s[0].isalpha() and s[1].isalpha():
        return False
    number_started=False
    for char in s:
        if char.isdigit():
            if not number_started and char=="0":
                return False
            number_started=True
        elif number_started:
            return False
    return True

if __name__ == "__main__":
    main()

        
    