class operation:
    def __init__(self,n) :
        self. n = n
    def perfect(self):
        sum=0
        for i in range(1, self.n):
            if self.n%i==0 : 
                sum=sum+1
        if self.n==sum:
            print(self.n,"is perfect number.")
        else:
            print(self.n,"is not perfect number.")
    def palindrome(self):
        temp = self.n
        while(temp>0) :
            digit=(temp%10)
            sum=(sum*10)+digit
            temp=(temp/10);
        if sum==self.n :
            print(self.n,"is a Palindrome Number.")
        else :
            print(self.n,"is not a Palindrome Number.")
    def factorial(self)
num operation(a)
 num perfect()
