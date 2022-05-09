# W.A.P in Python to remove duplicates from a list. #

L = []
n = int(input("Enter the total number of items in the list : "))
for x in range(n) :
    L.append(int(input("Enter the data item : ")))
for i in L :
    if L.count(i)!=1 :
        L.remove(i)
print("The modified list :- ",L)
