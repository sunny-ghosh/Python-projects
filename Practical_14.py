# W.A.P in Python to print all armstrong numbers within a given range. # 

l = int(input("Enter the lower limit of the range : "))
h = int(input("Enter the upper limit of the range : "))
print("All armstrong numbers within the given range are :-")
for n in range(l,h+1) :
    temp=n
    s = 0
    while(temp>0) :
        digit = temp%10
        s = s + digit**3     # ** is used to define power of a number.
        temp = temp//10      # // returns only integer value even during division.
    if(s==n) :
        print(n)
