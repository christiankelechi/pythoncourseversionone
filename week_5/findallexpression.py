import re
#Check if the string starts with "The" and ends with "Spain":

txt = "The rAin in Spain And and and And 012345678 "
x = re.findall("\d",txt)

print(x)