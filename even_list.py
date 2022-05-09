# Q: W.A.P. in Python to find all even no.s from a list. #

L = []         # EMPTY LIST
n = int(input("Enter the total no. of data elements in the list : "))
for i in range(n) : 
    L.append(int(input("Enter the data : ")))
print("Even numbers in the list are :- ")
for j in L :
    if j%2==0 :
        print(j,end=' ')       # end parameter is used to add any string with the output.