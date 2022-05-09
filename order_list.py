# Q: W.A.P. in Python to check a list whether it's in ascending order or not. #

L1 = []         # EMPTY LIST
n = int(input("Enter the total no. of data elements in the list : "))
for i in range(n) : 
    L1.append(input("Enter the data : "))
print(L1)
L2 = L1.copy()             # copy() function is used to copy a list along with its all data items.
L1.sort()
if(L1==L2) :
    print("The list is in ascending order.")
else :
    print("The list is not in ascending order.")