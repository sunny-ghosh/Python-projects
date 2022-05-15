# W.A.P in Python to check whether a number is perfect and palindrome or not and find its factorial and sum of digits. #

class Operation:
    def __init__(self,n) :
        self. n = n
    def perfect(self):
        sum=0
        for i in range(1, self.n):
            if self.n%i==0 : 
                sum=sum+i
        if self.n==sum:
            print(self.n,"is perfect number.")
        else:
            print(self.n,"is not perfect number.")
    def palindrome(self):
        temp = self.n
        s = 0
        while(temp>0) :
            digit=(temp%10)
            s=(s*10)+digit
            temp=(temp//10)
        if s==self.n :
            print(self.n,"is a Palindrome Number.")
        else :
            print(self.n,"is not a Palindrome Number.")
    def factorial(self) :
        fact = 1
        for x in range(1,self.n+1) :
            fact = fact*x  
        print("The factorial of",self.n,"is",fact)
    def sum_digit(self) :
        carry = self.n
        total = 0
        while(carry>0) :
            r=(carry%10)
            total=(total+r)
            carry=(carry//10)
        print("The sum of the digits of the given number is",total)
num = Operation(int(input("Enter the number : ")))
num.perfect()
num.palindrome()
num.factorial()
num.sum_digit()
