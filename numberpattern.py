# W.A.P in Python to generate the following pattern-               
''' 
                                                                                     1
                                                                                     2 3
                                                                                     4 5 6
                                                                                     7 8 9 10
'''


n = int(input("Enter the number of lines you want to print : "))
k = 1
for i in range(1,n+1) :
    for j in range(1,i+1) :
        print(k,end=" ")
        k+=1
    print("")
