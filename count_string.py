# W.A.P in Python to count the total no. of words in a string. #

str = input("Enter the string :- ")
total = 1
for i in range(len(str)) :                      # len() function returns the length of the string.
    if(str[i]==" ") :
        total+=1
print("The total number of words in the string is ",total)







                 # ALTERNATIVE METHOD #



# str = input("Enter the string :- ")
# total = 1
# total = total + str.count(" ")                   # count() function is used to count the total number of occurances of any specified character.
# print("The total number of words in the string is ",total)