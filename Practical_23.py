# W.A.P in Python to sort a list of names based on their length.[List should be populated through run time input.] #

L = []
n = int(input("Enter the total number of names in the list : "))
for x in range(n) :
    L.append(input("Enter the name : "))
# L.sort(key=len)                   # It's used to sort the items in the list based on their length.
# print(L)
print("Those names are :-\n",sorted(L,key=len))            # It's used to sort the items in the list based on their length.
''' sorted() function is almost similar like sort() function. It performs the same task just keeping unchanged the original list. 
   Syntax :-  sorted(<list name>,<condition[optional]>)
'''