def myfunc1():
    y=12
    x = "Jane"
    def myfunc2():
        nonlocal y
        
        x="Ifeanyi"
        y = 16
        print(y)
        print(x)
        
        # return x
    myfunc2()
    return x

print(myfunc1())
