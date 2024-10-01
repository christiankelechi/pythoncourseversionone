numbers={}

for i in range(1,101):
    numbers[str("number")+str(i)]=i
print(numbers)
numbers.clear()
print(type(numbers))