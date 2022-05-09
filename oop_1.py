# W.A.P in Python to find the factorial of a number using OOP containing parameterized function along with user inputs.

class F :
    def factorial(self,n) :
        fact=1
        for i in range(1,n+1) :
            fact = fact*i  
        return fact
n = int(input("Enter a number : "))
ob = F()
f = ob.factorial(n)
print("The factorial of",n,"is",f)
