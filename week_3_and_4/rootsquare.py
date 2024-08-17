print(pow(2,3))
print(2**3)

import math
print(math.sqrt(64))
myvalue=str(math.sin(math.radians(45)))
print(myvalue[:13])
if int(myvalue[12])>=5:
    print(myvalue[:11]+str(int(myvalue[11])+1))
else:
    print(myvalue[:12])
