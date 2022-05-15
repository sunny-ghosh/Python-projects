# W.A.P in Python to print all perfect numbers within a range using constructor. #

class Task :
    def __init__(self,l,h) :
        print("All perfect numbers within the given range are :-")
        for i in range(l,h+1) :
            sum = 0
            for j in range(1,i) :
                if(i%j==0) :
                    sum=sum+j
            if(i==sum) :
                print(i)
l = int(input("Enter the lower limit of the range : "))
h = int(input("Enter the upper limit of the range : "))
Task(l,h)