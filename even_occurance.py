# W.A.P in Python to get data items from a list appearing even no. of times. #

list = [22,5,20,3,14,1,19,85,8,8,19,69,9,4,20,22,18,19,10,4,6,4,13,4]
L = []
for i in list :
    if list.count(i)%2==0 :
        if str(i) not in L :
            L.append(str(i))
print("All data items in the list appearing even no. of times are :-")
print(", ".join(L))