# W.A.P in Python to print all even numbers within a range using 'continue' keyword. #

l = int(input("Enter the lower limit of the range : "))
h = int(input("Enter the upper limit of the range : "))
for i in range(l,h+1) :
    if(i%2!=0) :
        continue          # 'continue' keyword is used to bypass.
    print(i)  