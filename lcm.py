# W.A.P in Python to calculate G.C.D and L.C.M. of two numbers . #

def g_c_d(n1,n2) : 
    for i in range(n1 if (n1<n2) else n2,0,-1) :                      # In python, '? :' operator is used in this way.
        if (n1%i==0) and (n2%i==0) :
            break
    return i
def l_c_m(n1,n2) :
    for j in range(n1 if (n1>n2) else n2,((n1*n2)+1)) :
        if (j%n1==0) and (j%n2==0) :
            break
    return j
n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
print("The required G.C.D. of ",n1," and ",n2," is ",g_c_d(n1,n2))
print("The required L.C.M. of ",n1," and ",n2," is ",l_c_m(n1,n2))