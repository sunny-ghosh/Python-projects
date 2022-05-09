# W.A.P in Python to check whether a number is armstrong or not. #

n = int(input("Enter the number : "))
temp=n
s=0
while(temp>0) :
        digit = temp%10
        s = s + digit**3  
        temp = temp//10       
if(n==s) :
    print(n,"is an armstrong number.")
else :
    print(n,"is not an armstrong number.")