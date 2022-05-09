# W.A.P in Python to input a list and search for a given element. #

L = []
flag = False
n = int(input("Enter the total number of items in the list : "))
for x in range(n) :
    L.append(int(input("Enter the data item : ")))
item=int(input("Enter the item you want to search in the list :- "))
for i in L :
    if i==item :
        flag = True
        break
if flag==True :
    print("The item is present in the list at index",L.index(item))
else :
    print("The item doesn't exist in the list.")