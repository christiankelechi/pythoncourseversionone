# create bank account
# enter all details for bank creation
import json
import random
atm_details={}
first_name=input("First Name : ")
atm_details['First Name : ']=first_name

last_name=input("Last Name : ")
atm_details['Last Name : ']=last_name

atm_number=random.randint(1000000000000000,100000000000000000)
atm_details['atm_number']=atm_number
pin_password=input("Enter Pin Password : ")
confirm_password=input("Confirm Pin Password : ")

if pin_password==confirm_password:
    atm_details['pin_password']=pin_password
    print("atm cad created successfully")
    
    with open("atm_details.json","w") as file:
        data=atm_details
        json_data=json.dump(data,file)
    file.close()
print(atm_details)
