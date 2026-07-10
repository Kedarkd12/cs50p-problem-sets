#Ask user for a number
num=int(input("Enter a number:"))

if num>0:
    #print table of positive integers
    i=1
    print("Table of",num,"using while loop:")
    while i<=10:
        c=num*i
        print(num,"*",i,"=",c)
        i=i+1

#print table of negative integers
else:
    print("Table of",num,"using for loop:")
    for j in range(1,10):
        j<=10
        d=num*j
        print(num,"*",j,"=",d)
        j+=1
