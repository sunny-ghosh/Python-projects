class General :
    def getdata(self,beng,eng) :
        self.beng = beng
        self.eng = eng
    def putdata(self) :
        print("The marks of Bengali :",self.beng)
        print("The marks of English :",self.eng)
class Science :
    def getmarks(self,phys,chem,maths) :
        self.phys = phys
        self.chem = chem
        self.maths = maths
    def showmarks(self) :
        print("The marks of Mathematics :",self.maths)
        print("The marks of Physics :",self.phys)
        print("The marks of Chemistry :",self.chem)
class Result(General,Science) :
    def gettotal(self) :
        total = self.beng + self.eng + self.maths + self.phys + self.chem
        self.total = total
        print("Aggregrate Marks :",total)
    def getaverage(self) :
        avg = self.total/5
        print("Average marks :",avg)
ob = Result()
beng = int(input("Enter the marks of Bengali : "))
eng = int(input("Enter the marks of English : "))
maths = int(input("Enter the marks of Mathematics : "))
phys = int(input("Enter the marks of Physics : "))
chem = int(input("Enter the marks of Chemistry : "))
ob.getdata(beng,eng)
ob.getmarks(phys,chem,maths)
ob.putdata()
ob.showmarks()
ob.gettotal()
ob.getaverage()