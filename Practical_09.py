# W.A.P in Python to check whether a number prime or not. # 

n=int(input("Enter the number : ")) 
p = 0
for i in range(1,n+1) :
    if(n%i==0) :
        p+=1         # It's used to define p=p+1
if(p==2) :
    print(n,"is a prime number.")
else :
    print(n,"is not a prime number.")