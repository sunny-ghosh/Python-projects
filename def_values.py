def add(x,y=6):
    print("The sum is",(x+y))
    return(x-y)
a=int(input("Enter the first number : "))
b=int(input("Enter the first number : "))
add(a)
add(a,b)
print("The diffrence between two numbers is ",(a-b))