# W.A.P in Python to generate the following pattern-               
''' 
                                                                                     *
                                                                                    **
                                                                                   ***
                                                                                  ****
'''


n = int(input("Enter the number of lines you want to print : "))
for i in range(n) :
    for j in range(n-1,i-1,-1) :
        print(" ",end = "")
    for k in range(i+1) :
        print("*",end = "")
    print("")