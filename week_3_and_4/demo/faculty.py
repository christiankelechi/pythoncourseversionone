import unn
class Faculties(unn.UnnBoardMembers):
    def __init__(self, name_of_faculty, faculty_dean, bursar, no_of_departments):
        self.name_of_faculty = name_of_faculty
        self.faculty_dean = faculty_dean
        self.bursar = bursar
        self.no_of_departments = no_of_departments
        
    
    def can_conduct_election(self):
        return f"Each faculties can conduct election through the {self.faculty_dean}"
    
    
    
    def can_give_school_fees_receipt(self):
        return f"{self.bursar} can convert school fees receipt"
    
    def can_assign_lecturer(self):
        return f"Each departments have a specific number of lecturers"