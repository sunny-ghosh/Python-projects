# This is the solution of sample program no.- 4
'''This program is the application of chapter no.- 2.
It's under the basic python lessions.'''
n1 = input("Enter the marks of first subject : ")   # It's used for taking input from user.
n1 = int(n1)     # It's used to convert the string taken from user to integer value.
n2 = input("Enter the marks of second subject : ")
n2 = int(n2)
n3 = input("Enter the marks of third subject : ")
n3 = int(n3)
n4 = input("Enter the marks of fourth subject : ")
n4 = int(n4)
n5 = input("Enter the marks of fifth subject : ")
n5 = int(n5)
total = (n1+n2+n3+n4+n5)
avg = total/5
print("The Aggregate Marks is",total)
print("The average of the marks of 5 subjects is",avg)
