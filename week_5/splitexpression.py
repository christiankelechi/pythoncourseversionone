import re
#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain and me"
x = re.split("\s", txt)
print(x)