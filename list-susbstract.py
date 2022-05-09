# Q: W.A.P. in Python to substract a list from another list. #

L1 = [8,0,8,19,69]
L2 = [14,0,1,19,85]
print("Two lists are - ",L1, " & ",L2)
L3 = []
for i in L1 :
    if i not in L2 :
        L3.append(i)
print("After substraction of two list, the new list is - ",L3)