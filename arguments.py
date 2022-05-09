def addition(*args) :
    s = 0
    for i in args :
        s+=int(i)
    return s
result = addition(2,3,4)               # 3 arguments are being passed during function call.
print("The result is",result)         