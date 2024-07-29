import pandas as pd
number_of_courses=int(input("Enter the number of courses you want to calculate: \n"))
course_title_list=[]
course_grade_list=[]
course_unit_list=[]
total_unit_value=0
total_value=0
for iterations in range(number_of_courses):
    course=input("Enter your course title : ")
    course_title_list.append(course)
    course_grade=input("Enter your course grade : ")
    
        
    course_grade_list.append(course_grade)
    course_unit=int(input("Enter your course unit: : "))
    total_unit_value+=course_unit
    course_unit_list.append(course_unit)
    
    if course_grade.lower()=='a':
        total=course_unit*5
        total_value+=total
    if course_grade.lower()=='b':
        total=course_unit*4
        total_value+=total
    if course_grade.lower()=='c':
        total=course_unit*3
        total_value+=total
    if course_grade.lower()=='d':
        total=course_unit*2
        total_value+=total
    if course_grade.lower()=='e':
        total=course_unit*1
        total_value+=total
    if course_grade.lower()=='f':
        total=course_unit*0
        total_value+=total
cgp=total_value/total_unit_value

print(f"cgp equal to {cgp}")