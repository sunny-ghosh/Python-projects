''' W.A.P in Python to perform following OOP program ~ 
class ~ Calculate
Functions ~ i.   getdata() -> To take an input(parameterized)
            ii.  prime() -> To check a number prime or not.
            iii. armstrong() -> To check a number armstrong or not. '''

class Calculate :
    def getdata(self,n) :
        self.n = n
    def prime(self) :
        p = 0
        for i in range(1,self.n+1) :
            if(self.n%i==0) :
                p+=1   
        if(p==2) :
            print(self.n,"is a prime number.")
        else :
            print(self.n,"is not a prime number.")
    def armstrong(self) :
        temp=self.n
        s=0
        while(temp>0) :
            digit = temp%10
            s = s + digit**3  
            temp = temp//10       
        if(n==s) :
            print(self.n,"is an armstrong number.")
        else :
            print(self.n,"is not an armstrong number.")
n = int(input("Enter a number : "))
ob = Calculate()
ob.getdata(n)
ob.prime()
ob.armstrong()
