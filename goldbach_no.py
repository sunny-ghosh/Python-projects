# W.A.P in Python to check a number whether it's goldbach or not. #

def prime(n) :
    L = []
    for i in range(2,n+1) :
        for j in range(2,i+1) :
            if(i%j==0) :
                break
        if(j==i and i%2!=0) :
            L.append(i)
    return L

n = int(input("Enter the number : "))
if n>0 and n%2==0 :
    list = prime(n)
    flag = False
    print("The pairs of odd prime numbers :-")
    for i in range(len(list)) :
        for j in range(i+1,len(list)) :
            if list[i]+list[j]==n :
                flag = True
                print(list[i],list[j])
    if flag==True :
        print(n,"is a goldbach number.")
    else :
        print("NULL")
        print(n,"is not a goldbach number.")
else :
    print("Invalid Input! The number must be positive and even.")

