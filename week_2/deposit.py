print("HI , to Access Bank Limited: ")
import json
deposit_details={}
print("Fill Deposit slip form to deposit money : ")
name_of_depositor=input("Enter the Depositor Name : ")
deposit_details['Full Name : ']=name_of_depositor
amount_to_deposit=int(input("Enter the amount you want to deposit : "))
deposit_details['Amount to Deposit : ']=amount_to_deposit
account_number_to_deposit=int(input(" Enter your account number : "))
deposit_details['Account Number : ']=account_number_to_deposit
with open("balance.json","w") as file:
    data=deposit_details
    json_data=json.load(data,file)
    print(json_data)