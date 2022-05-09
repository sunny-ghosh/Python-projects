# W.A.P in Python to input three numbers to find the largest/smallest number. #

n1 = int(input("Enter a number : "))
n2 = int(input("Enter another number : "))
n3 = int(input("Enter the last number : "))
if((n1>n2)and(n1>n3)) :
    print(n1," is the largest number.")
elif((n2>n1)and(n2>n3)) :             # elif() function is used instead of the else if() function.
    print(n2," is the largest number.")
elif((n3>n1)and(n3>n2)) :
    print(n3," is the largest number.")
else :
    print("Three numbers are equal to each other.")