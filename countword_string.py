# W.A.P in Python to count the total no. of words in a string starting with 'A'. #

# str = input("Enter the string :- ")
# total = 0
# word = str.title()                               # title() function is used to capitalize the first letter of each word in a string.
# for i in range(len(word)) :                      # len() function returns the length of the string.
#     if word[i]=="A" :
#         total+=1
# print("The total number of words in the string starting with 'A' is ",total)










                 # Alternative Method #





str = input("Enter the string :- ")
word = str.title()                               # title() function is used to capitalize the first letter of each word in a string.
print("The total number of words in the string starting with 'A' is ",word.count("A"))
