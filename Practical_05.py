# W.A.P in Python to swap the values of two variables. #
# It's performed without using the third variables.

n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
print("Before swaping, the values of the first and second number are ",n1," and ",n2," respectively.")
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2
print("After swaping, the values of the first and second number are ",n1," and ",n2," respectively.")