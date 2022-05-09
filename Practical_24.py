# W.A.P in Python to count the occurance of each character in your name and display each character of the string. #

str = input("Enter the name : ")
L = []
for i in str.lower() :
        if i not in L :
                L.append(i)
                print("The total number of occurances of",i,"is",str.count(i))

L1 = list(str)
print(L1)