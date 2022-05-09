class Number :
    def __init__(self,a,b) :
        self.a = a
        self.b = b
    def disp(self) :
        print("1st number :",self.a)
        print("2nd number :",self.b)
    def total(self) :
        return self.a + self.b
num = Number()
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
num = Number(a,b)
num.disp()
print("The sum of two numbers is",num.total())