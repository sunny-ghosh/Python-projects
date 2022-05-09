# W.A.P in Python to find the factorial of a given number. # 

n = int(input("Enter the number : "))
fact=1
for i in range(1,n+1) :
    fact = fact*i
print("The factorial of",n,"is",fact)