import re
#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain and and and and "
x = re.sub("\s","2",txt)

print(x)