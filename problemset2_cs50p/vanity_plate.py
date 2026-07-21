def main():
    plate = input("\nPlate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    n=len(s)
    if n<=6 and n>=2:
        if s.isalnum():
            if s[0].isalpha() and s[1].isalpha():
                if digs(s):
                   if chars(s):
                       return True 

def digs(s):
    for char in s:
        if char.isdigit():
            if char!="0":
                return True
            else:
                return False
        else:
            return True
            
def chars(s):
    number_started=False
    for char in s:
        if char.isdigit():
            number_started=True
        elif char.isalpha() and number_started:
            return False
        return True
        
main()