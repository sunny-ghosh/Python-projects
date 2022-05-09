# W.A.P in Python to check whether a number is pronic or not. #

n = int(input("Enter the number : "))
flag = False
for i in range(n+1) :
    if(i*(i+1)==n) :
        flag = True
        break
if flag==True :
    print(n,"is a pronic number.")
else :
    print(n,"is not a pronic number.")