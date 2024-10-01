is_true = True
while is_true:
    password=input("enter password \n")
    if (len(password) < 8):
        is_true = True
    else:
        is_true = False
        