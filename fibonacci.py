# W.A.P in Python to print the first n-th terms of the fibonacci series. #

n = int(input("Enter the number of terms :- "))
print("The first n-th terms of the fibonacci series :- ")
f = 0
s = 1
for i in range(0,n) :
    if(i<=1) :
        next = i
        print(next,end='   ')
    else :
        next = f+s
        print(next,end='   ')
        f = s
        s = next
    
