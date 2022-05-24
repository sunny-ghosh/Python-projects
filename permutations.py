# W.A.P in Python to generate all permutations of a list. #

import itertools
import string            # It's a built-in module in python,used to iterate over data structure.
L = []
n = int(input("Enter the total number of items in the list : "))
for i in range(n) :
    L.append(int(input("Enter the data item : ")))
print(list(itertools.permutations(L)))         # permutations() is a function, used to generate the permutations of a specified data structure.