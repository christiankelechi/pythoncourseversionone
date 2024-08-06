def calculate(n):
    def divide(y):
        return y/2
    return lambda x:(x*n)+divide(x)

first_function_call=calculate(2)
print(first_function_call(4))
