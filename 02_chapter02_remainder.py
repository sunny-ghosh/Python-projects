# This is the solution of sample program no.- 2
'''This program is the application of chapter no.- 2.
It's under the basic python lessions.'''
n1 = input("Enter first number : ")   # It's used for taking input from user.
n1 = int(n1)     # It's used to convert the string taken from user to integer value.
n2 = input("Enter second number : ")  # It's used for taking input from user.
n2 = int(n2)     # It's used to convert the string taken from user to integer value.
Rem = (n1%n2)
print("The remainder after dividing first number by second number is",Rem)
print(type(Rem))  # It's used to print the datatype of the variable.
div=(n1/n2)
print(div)
div1 = (n1//n2)
print(div1)
print(type(div1))
print(type(div))
