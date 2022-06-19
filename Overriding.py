                                    # Solution of Method Overriding in Python #



class Perfect :
    def check(self) :
        sum=0
        for i in range(1,self.n) :
            if(self.n%i==0) :
                sum=sum+i
        if(self.n==sum) :
            print(self.n,"is a perfect number.")
        else :
            print(self.n,"is not a perfect number.")
class Spy(Perfect) :
    def check(self,n) :
        self.n = n
        super().check()
        temp=self.n
        s=0
        p=1
        while(temp>0) :
            r=temp%10
            s=s+r
            p=p*r
            temp=temp//10
        if s==p :
            print(self.n,"is a spy number.")
        else :
            print(self.n,"is not a spy number.")
ob=Spy()
ob.check(int(input("Enter the number : ")))