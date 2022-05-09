# W.A.P in Python to find a given character within a string and if it's present, display it’s index position. #

str = input("Enter a string : ")
s = input("Enter a character to search in the string : ")
flag = False
for i in str :
    if i.casefold()==s.casefold() :
        flag = True
        break
if flag==True :
    print("The character is present in the string at index",str.index(i))
else :    
    print("The character doesn't exist in the string.")
