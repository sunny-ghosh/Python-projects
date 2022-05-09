# W.A.P in Python to take an input of an alphanumeric string and seperate the numbers,special characters,letters and sort the numbers in descending order. #

str = input("Enter an alphanumeric string :- ")
L1 = []
L2 = []
L3 = []
for i in range(len(str)) :
    if str[i].isdigit()==True :
        L1.append(str[i])
    elif str[i].isalpha()==True :
        L2.append(str[i]) 
    else :
        L3.append(str[i])
print("All the numbers in the given alphanumeric string are :-")
print(", ".join(L1))                         
print("All the letters in the given alphanumeric string are :-")
print(", ".join(L2))
print("All the special characters in the given alphanumeric string are :-")
print(", ".join(L3))
print("All the numbers sorted in descending order in the given alphanumeric string are :-")
L1.sort(reverse=True)
print(", ".join(L1))