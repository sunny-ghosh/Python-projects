# W.A.P in Python to input a list of numbers and swap the elements at the even location with the elements at the odd location. #

L = []
n = int(input("Enter the total number of items in the list : "))
for x in range(n) :
    L.append(int(input("Enter the data item : ")))
print("List :- ",L)
for i in range(0,len(L)-1,2) : 
    L[i],L[i+1]=L[i+1],L[i]
print("Modified list :- ",L)