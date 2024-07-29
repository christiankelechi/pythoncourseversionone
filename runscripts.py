import logging
logger=logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def collatz(number):
    
    if float(number)%2==0:
    
        return float(number)//2
    
    else:
        value=((3*float(number))+1)
        
        return value
for i in range(1000):  
    number=float(input("Enter number"))
    value=collatz(number)
    value=float(value)
    if value==1.0:
        logger.debug('the value is equal to ',value) 
        break
    else:
        logger.debug('the value is equal to ',value) 
        
        