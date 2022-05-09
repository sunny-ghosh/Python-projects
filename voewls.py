''' W.A.P in Python to accept a string from user and redisplay the same string after removing vowels from it 
using function & for loop. '''

def vowel(str) :
    print("The modified string is ~ : ",end = '')
    v = ["a","e","i","o","u"]
    for i in str :
        if i.casefold() not in v :                # casefold() function is for caseless matching in a string i.e. it ignores cases while checking but in case of display, it returns an entire string in lowercase.
            print(i,end = '')
str = input("Enter the string :- ")
print("The user-entered string is ~ ",str)
vowel(str)




