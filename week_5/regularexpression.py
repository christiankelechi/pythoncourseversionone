import re
#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("rain", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
print(x)