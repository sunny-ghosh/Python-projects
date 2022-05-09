# W.A.P in Python to sum all the items in a list. # 

L = []
n = int(input("Enter the total number of items in the list : "))
for i in range(n) :
    L.append(int(input("Enter the data item : ")))
print("The result of the addition of all items in the list is",sum(L))
