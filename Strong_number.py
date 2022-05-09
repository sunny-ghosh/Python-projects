# W.A.P in Python to check whether a number is strong or not. #

def strong_no(n) :
    temp = n
    s=0
    while(temp>0) :
        r = temp%10
        s = s + factorial(r)
        temp=temp//10
    if(n==s) :
        print(n,"is a strong number.")
    else :
        print(n,"is not a strong number.")
def factorial(r) :
    fact = 1
    for i in range(2,r+1) :
        fact = fact*i
    return fact
n = int(input("Enter the number : "))
strong_no(n)