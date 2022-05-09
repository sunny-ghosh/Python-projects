# This is the solution of sample program no.- 2
'''This program is the application of chapter no.- 3.
It's under the basic python lessions.'''
letter = '''To,
<Recipient Name>, 
<Institution's Name>.
<Date of writing>

Respected Sir/Madam,
\t\t   Most respectfully, I beg to state that I can't able to attend the class properly because I was suffering from fever. 

 I'll be highly obliged if you kindly pardon me for the absence from <starting date> to <end date>.


Thanking you,\t\t\t\t\t\t\t\t\tYours sincerely,
\t\t\t\t\t\t\t\t\t\t<Sender's Name>,
\t\t\t\t\t\t\t\t\t\t<Department's name>,
\t\t\t\t\t\t\t\t\t\t<Roll No.> '''
RCPT = input("Enter the name of recipient : ")     # The input() is used to take the inputs from the user.
SNDR = input("Enter your name : ")
inst = input("Enter the name of the institution : ")
dept = input("Enter the name of the department : ")
roll = input("Enter your roll number : ")
date1 = input("Enter the starting date of the absence period : ")
date2 = input("Enter the end date of the absence period : ")
date = input("Enter the date of writing the letter : ")
letter = letter.replace("<Recipient Name>",RCPT)    # This command is used to replace one character in the string by another character.
letter = letter.replace("<Sender's Name>",SNDR)
letter = letter.replace("<Institution's Name>",inst)
letter = letter.replace("<Department's name>",dept)
letter = letter.replace("<Roll No.>",roll)
letter = letter.replace("<Date of writing>",date)
letter = letter.replace("<starting date>",date1)
letter = letter.replace("<end date>",date2)
print(letter)


