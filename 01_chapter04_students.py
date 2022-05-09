# This is the solution of sample program no.- 1 (see: no.2 in practice list)
'''This program is the application of chapter no.- 4.
It's under the basic python lessions.'''
s1 = int(input("Enter the marks of the first student : "))      # It's used for typecasting the string values to int values.
s2 = int(input("Enter the marks of the second student : "))
s3 = int(input("Enter the marks of the third student : "))
s4 = int(input("Enter the marks of the fourth student : "))
s5 = int(input("Enter the marks of the fifth student : "))
s6 = int(input("Enter the marks of the sixth student : "))
s7 = int(input("Enter the marks of the last student : "))
student_list = [s1,s2,s3,s4,s5,s6,s7]
student_list.sort()                  # Here, the sort method is used in this list to perform sorting values in each of the items in the list in ascending order.    
print(student_list)