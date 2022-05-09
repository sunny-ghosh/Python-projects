# W.A.P in Python to find the sum of all even numbers between 1 to 20. #

s = 0
for i in range(1,21) :
    if(i%2!=0) :
        continue 
    s = s + i
print(s)  