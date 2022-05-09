# W.A.P in Python to count the total unique word appearances of a string. #

str = input("Enter the string :- ")
total=0
L = str.split()
for i in L :
    if L.count(i.casefold())==1 :
        total+=1
print("The total number of unique word appearances of the string is ",total)