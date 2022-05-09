cprice = int(input("Enter the cost price : "))
sprice = int(input("Enter the selling price : "))
if sprice>cprice :
    print("Profit has occured.")
    profit = sprice-cprice
    print("The profit amount is ",profit)
else :
    print("The loss has occured.")
    loss = cprice-sprice
    print("The loss amount is ",loss)