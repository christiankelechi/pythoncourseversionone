# create bank account
# enter all details for bank creation
import json
import random
details={}
first_name=input("First Name : ")
details['First Name : ']=first_name

last_name=input("Last Name : ")
details['Last Name : ']=last_name

phone=input("Phone Number : ")
details['Phone Number : ']=phone

lga=input("LGA :")
details['LGA : ']=lga

account_number=random.randint(1000000000,10000000000)
details['Account Number : ']=account_number
print(details)
with open("account_details.json","w") as file:
    data=details
    json_data=json.dump(data,file)
file.close()
print(file)
# with open("second_detail.json","w") as secondfile:
#     data=json.load(file)
#     json_data=json.dump(data,secondfile)