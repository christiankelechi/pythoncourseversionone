import asuu as a

class UnnBoardMembers(a.AsuuBody):
    def __init__(self,admissions,records,exams,students_affairs):
        self.admissions=admissions
        self.records=records
        self.exams=exams
        self.students_affairs=students_affairs
        
    def can_admit_student(self):
        return f"{self.admissions} admit students yearly"
    
    def can_store_students_records(self):
        return f"{self.records} stores students records from first year to final year"
    
    def cordinate_exams(self):
        return f"Workers in {self.exams} office helps in keeping track of students examination "
    
    def student_affairs(self):
        return f"{self.student_affairs} maintains students condusiveness and affairs partaining to their stay in the university"