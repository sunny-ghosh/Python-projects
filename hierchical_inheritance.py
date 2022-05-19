class A :
    def getdata(self,n) :
        self.n = n
        print("The number you have entered is",self.n)
class B(A) :
    def odd_even(self) :
        if self.n%2==0 :
            print("The number is even.")
        else :
            print("The number is odd.")
class C(A) :
    def perfect(self) :
        sum = 0
        for i in range(1,self.n) :
            if(self.n%i==0) :
                sum=sum+i
        if(self.n==sum) :
            print(self.n,"is a perfect number.")
        else :
            print(self.n,"is not a perfect number.")
ob = B()
obj = C()
ob.getdata(10)
ob.odd_even()
obj.getdata(6)
obj.perfect()