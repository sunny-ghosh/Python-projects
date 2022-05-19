class A :
    def add(self,a,b) :
        self.a = a
        self.b = b
        print("The sum is",(self.a+self.b))
class B(A) :
    def addition(self,c) :
        self.c = c
        print("The sum is",(self.a+self.b+self.c))
ob = B()
ob.add(5,6)
ob.addition(5)
