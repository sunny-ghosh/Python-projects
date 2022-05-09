# Q: W.A.P. in Python to interchange the first and last element in the list. #

L = []     
n = int(input("Enter the total no. of data elements in the list : "))
for i in range(n) : 
    L.append(input("Enter the data : "))
print("Before interchanging, the list is - ",L)
L[0],L[-1] = L[-1],L[0]   
print("After interchanging, the list is - ",L)         # Interchanging list items within specified indexes.