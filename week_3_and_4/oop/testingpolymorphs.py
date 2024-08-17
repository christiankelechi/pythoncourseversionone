import faculty
import mechanicalengineering as me
import student

faculty_obj=faculty.Faculties("Engineering","Obi","Mr O","6")
# print(faculty_obj.must_be_a_student_or_worker())



# student_obj=faculty.Faculties("Obi","Ada","Uche","200")

# student_obj.name_of_faculty="Art"
# student_obj.faculty_dean="Eze"
# student_obj.bursar="Obi"
# student_obj.no_of_departments="20"

print(faculty_obj.must_be_a_student_or_worker())