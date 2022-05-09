list1 = [22,5,3]
list2 = [5,"Sunny"]
L1 = list1 + list2
print(L1)
myList = ["C","JAVA","Python"]
list2.extend(myList)            # extend() function is used to merge the items of two lists in one list. In this case, that list only will update on which the function is applied. The list given as an arguement of the function will remain unchanged.
print(list1)
print(list2)
print(myList)