# W.A.P in Python to take the name of a student and the marks of 5 subjects as input & calculate the average marks and print the grades as follows-
'''average<40 ~ grade-F
   39<average<50 ~ grade-C
   49<average<60 ~ grade-B
   59<average<70 ~ grade-A
   69<average<80 ~ grade-A+
   79<average<90 ~ grade-AA
   average>=90 ~ grade-O'''

s_name = input("Enter the name of the student : ")
print("Student name :",s_name)
sub1 = int(input("Enter the marks of first subject : "))
sub2 = int(input("Enter the marks of second subject : "))
sub3 = int(input("Enter the marks of third subject : "))
sub4 = int(input("Enter the marks of fourth subject : "))
sub5 = int(input("Enter the marks of fifth subject : "))
total = (sub1+sub2+sub3+sub4+sub5)
print("Aggregate Marks :",total)
avg = total//5                      # // is used to get the 'int' value after performing division.
print(type(avg))
if avg<40 :
    print("Grade : F")
elif 39<avg<50 :
    print("Grade : C")
elif 49<avg<60 :
    print("Grade : B")
elif 59<avg<70 :
    print("Grade : A")
elif 69<avg<80 :
    print("Grade : A+")
elif 79<avg<90 :
    print("Grade : AA")
elif 89<avg<=100 :
    print("Grade : O")
else :
    print("Enter the correct input!")
