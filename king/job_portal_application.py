no_of_python_developers=3
list_of_applicants={}
import json
for i in range(1,1000):
    if i <=3:
        name=input("What is your name")
        list_of_applicants['name'+str(i)]=name
        describe_your_self=input("Describe your level of experience in python \n")
        list_of_applicants['discription'+str(i)]=describe_your_self
        
    else:
        
        break
    
with open("applicants.json","w") as file:
    data=list_of_applicants
    json.dump(data,file)