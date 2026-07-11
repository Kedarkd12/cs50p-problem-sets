def parity(a):
    #check whether given number is even or odd and print accordingly
    if(a%2==0):
        print("Even")
    else:
        print("Odd")

def main():
    #Ask user for a number
    b=int(input("Enter a number:"))
    parity(b)

main()