#Ask user details
name=input("Enter your name:")
print(f"Hello \"{name}\",",end=" ")
print("Welcome to a simple calculator\n")

#Ask the user to enter numbers
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

#ask the user the operation to be performed
op=int(input("\nFrom the below list of operations:\n   1.Addition\n   2.Subtraction\n   3.Multiplication\n   4.Division\nEnter the number of the operation you want to perform:"))

#switch case using function
def get_operation_selected(op):
    match op:
        case 1:
            print(f"\n{num1} + {num2} = {num1+num2}")
        case 2:
            print(f"\n{num1} - {num2} = {num1-num2}")
        case 3:
            print(f"\n{num1} * {num2} = {num1*num2}")
        case 4:
            print(f"\n{num1} / {num2} = {num1/num2}")

get_operation_selected(op)
