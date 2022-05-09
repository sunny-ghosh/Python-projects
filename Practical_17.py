# W.A.P in Python to get the largest number from a list without using max() function. #

def max(list) :
    m = list[0]
    for i in list :
        if i>m :
            m=i
    return m
list = []
n = int(input("Enter the total number of items in the list : "))
for x in range(n) :
    list.append(int(input("Enter the data item : ")))
print("The largest number in the list is",max(list))