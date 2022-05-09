# This is the solution of sample program no.- 6
'''This program is the application of chapter no.- 2.
It's under the basic python lessions.'''
r = input("Enter the value of the radius of a circle : ")   # It's used for taking input from user.
r = int(r)     # It's used to convert the string taken from user to integer value.
a = (3.14*r*r)
p = (2*3.14*r)
print("The area of the circle is",a)
print("The circumference of the circle is",p)
print(type(r),type(a),type(p))