# W.A.P in Python to generate the following pattern-               
''' 
                                                                                     A
                                                                                     B B
                                                                                     C C C
                                                                                     D D D D
'''


n = int(input("Enter the number of lines you want to print : "))
for i in range(n) :
    for j in range(i+1) :
        print(chr(i+65),end=" ")                 # 'chr' is a character datatype in python.
    print("")


