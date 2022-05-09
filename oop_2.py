# W.A.P in Python to find a factorial of a number and also check that number is odd or even using constructor and functions. #

class Calculation :
    def __init__(self,n) :
        self.n = n
    def factorial(self) :
        fact=1
        for i in range(1,self.n+1) :
            fact = fact*i  
        return fact
    def odd_even(self) :
        if self.n%2==0 :
            print("The number is even.")
        else :
            print("The number is odd.")
n = int(input("Enter a number : "))
ob = Calculation(n)
print("The factorial of",n,"is",ob.factorial())
ob.odd_even()
