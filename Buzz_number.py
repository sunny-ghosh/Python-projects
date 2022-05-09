# W.A.P in Python to check whether a number is buzz or not. #

n = int(input("Enter the number : "))
if (str(n).endswith("7")) or (n%7==0) :      # endswith() function is used to check whether the string is ended with the specified character/'s or not and returns the boolean value.
    print(n,"is a buzz number.")
else :
    print(n,"is not a buzz number.")