# W.A.P in Python to check whether a list is empty or not. #

# List = []
# if bool(List) :                                  
#     print("The list is not empty.")
# else :
#     print("The list is empty.")



                                         # ALTERNATIVE METHOD #



# List = []
# if len(List)==0 :
#     print("The list is empty.")
# else :
#     print("The list is not empty.")





                                         # ALTERNATIVE METHOD #




List = []
n = int(input("Enter the total number of items in the list : "))
for x in range(n) :
    List.append(int(input("Enter the data item : ")))
if len(List)==0 :
    print("The list is empty.")
else :
    print("The list is not empty.")