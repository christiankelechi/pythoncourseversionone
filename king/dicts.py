numbers = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
}
# print(numbers)
# print(len(numbers))

# #changing items of dictionaries
# numbers["four"] = 6
# print(numbers) 

# numbers.update({"one": 100})
print(numbers)
print(numbers["one"])
print(numbers["four"])
numbers["two"]=200
print(numbers)
numbers.update({"four":400})
print(numbers)

del numbers["four"]
print(numbers)