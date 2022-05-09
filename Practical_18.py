# W.A.P in Python to count the number of strings where the string length is 2 or more and first and last character are same from a given list of strings. #

def String(L) :
    count = 0
    for i in L :
        if len(i)>=2 and i[0]==i[-1] :
            count+=1
    return count
L = []
n = int(input("Enter the total number of items in the list : "))
for x in range(n) :
    L.append(input("Enter the data item : "))
print("As per the given conditions, the total number of strings is",String(L))

