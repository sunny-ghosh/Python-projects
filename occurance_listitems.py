# Q: W.A.P. in Python to get data items from a list appearing odd no. of times. #

# list = [22,5,20,3,14,1,19,85,8,8,19,69,30,3,20,22,18,19]
# L = []
# for i in list :
#     if list.count(i)%2!=0 :
#         if i not in L :
#             L.append(i)
# print("Data items are :-")
# for i in range(len(L)) :
#     print(L[i],end = ", ")








                                    # ALTERNATIVE METHOD #

list = [22,5,20,3,14,1,19,85,8,8,19,69,30,3,20,22,18,19]
L = []
for i in list :
    if list.count(i)%2!=0 :
        if i not in L :
            L.append(i)
print("Data items are :-")
print(*L)                  #  *  operaator returns all data items present in the list.