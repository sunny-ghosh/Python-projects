# W.A.P in Python to check whether a number is perfect or not. #
# Ex. :- 6 = (1+2+3)


n = int(input("Enter the number : "))
sum=0
for i in range(1,n) :
    if(n%i==0) :
        sum=sum+i
if(n==sum) :
    print(n,"is a perfect number.")
else :
    print(n,"is not a perfect number.")