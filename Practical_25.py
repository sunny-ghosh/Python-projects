# W.A.P in Python to create a list containing first 20 odd numbers. #

class Number :
    L = []
    def __init__(self,n) :
        for i in range(1,2*n) :
            if i%2==0 :
                continue
            self.L.append(i)
        print("The list of odd numbers :-\n",self.L)
ob = Number(int(input("How many odd numbers you want to display :- ")))


