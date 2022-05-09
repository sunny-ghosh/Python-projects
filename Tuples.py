T1 = ("JAVA","C","C++")                 # Packing the tuple.
(x1,x2,x3) = T1                         # Unpacking the tuple.
print(x1)
print(x2)
print(x3)
T2 = ("CSS","PYTHON","SQL","PHP","JS")
T1+=T2             # Adding two tuple.
print(T1)
L = list(T1)                  # Typecasting from tuple to list.
L.remove("SQL")
print(tuple(L))               # Typecasting from list to tuple.
(a,*b) = T2                   # Unpacking the tuple. Here, * operator returns the sublist of rest of items into a tuple.
print(a)
print(b)