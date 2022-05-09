# L = list(("C","C++","Java","Python","HTML","CSS","PHP","SQL","JS"))                      # list() constructor
# print(type(L))
# print(L)
# print(L[0])                       # returns the item value at the specified positive index.
# print(L[-1])                      # returns the item value at the specified negative index.
# print(L[2:5])                     # returns the item values of index no. 2 to 4
# print(L[ :4])                     # returns the item values of index no. 0 to 3
# print(L[3: ])                     # returns the item values of index no. 3 to the end
# print(L[ : ])                     # returns the entire list item values.
# print(L[-4:-1])                   # returns the item values of index no. -4 to -2
# if "Python" in L :                # checking whether the data item is present in the list or not.
#     print(True)
# else :
#     print(False)
# # -----------------------------------------------------------------
# # L[2]=66                    # simple way to change a data item value at the specified index of a list in python.
# # print((L))
# # L[1:3]=["BCA","ECE"]      # It change the all data item values in the list within the specified range with the given values.
# # print((L))
# # L[1:3]=["BCA","ECE","CSE"]      # If more items are inserted here,then the last of them will also be inserted at the specified position of the list and the remaining items will move automatically. 
# # print((L))
# # ---------------------------------------------------------------------------
# L[1:3]=["C#"]               # If less items are inserted here,then they are inserted at the specified position of the list and the remaining items will move accordingly.
# print((L))
# L.insert(2,"Python")
# print(L)
# print(L.count("Python"))     # count() function is used to get number of times the specified value occurs in the list.
# print(L.index("Python"))     # index() function returns the index of the first occurance of the specified value in the list.``
# L.remove("Python")
# print(L)
l = ["c","c++","java","c",22,4,500,122,25]
print(l)
# print(l.count("c"))
# print(l.index("java"))       
# l.remove("c")
# print(l)

for i in range(len(l)) :
    print(i,end=' ')
for i in l :
    print(i)