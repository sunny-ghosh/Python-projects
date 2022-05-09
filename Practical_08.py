# W.A.P in Python to find the factors of a given number. #

def factors(n) :
    print("Factors of ",n)
    for i in range(1,n+1) :
        if(n%i==0) :
            print(i,end=", ")
k=int(input("Enter the number : "))
factors(k)