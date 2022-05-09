# W.A.P in Python to print all prime numbers within a given range. # 

# l = int(input("Enter the lower limit of the range : "))
# h = int(input("Enter the upper limit of the range : "))
# print("All prime numbers within the given range are :-")
# for n in range(l,h+1) :
#     for i in range(2,n+1) :
#         if(n%i==0) :
#             break
#     if(i==n) :
#         print(n)









                 # Alternative Method #



l = int(input("Enter the lower limit of the range : "))
h = int(input("Enter the upper limit of the range : "))
print("All prime numbers within the given range are :-")
flag=0
for n in range(l,h+1) :
    for i in range(2,n) :
        if(n%i==0) :
            flag = 1
            break
    if(flag==0) :
        print(n)
    flag = 0
          