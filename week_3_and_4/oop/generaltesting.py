import faculty as fa

fac=fa.Faculties(name_of_faculty="Engineering",faculty_dean="Engr ABC",bursar="Engr CAC",no_of_departments="8")
fac.admissions=" Admissions"
print(fac.bursar)
print(fac.no_of_departments)
print(fac.can_admit_student())