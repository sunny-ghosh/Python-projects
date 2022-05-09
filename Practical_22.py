# W.A.P in Python to take 3 '-ve' numbers as input and find the minimum among them. #

n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
n3 = int(input("Enter the third number : "))
if(n1<0 and n2<0 and n3<0) :
    if(n1<n2 and n1<n3) :
        print("The minimum number is",n1)
    elif(n2<n1 and n2<n3) :
        print("The minimum number is",n2) 
    else :
        print("The minimum number is",n3)
else :
    print("Please enter the valid input.")