import faculty as fa

class MechanicalEngineering(fa.Faculties):
    def __init__(self, hod, secretary, exam_officer, students):
        self.hod = hod                  # Head of Department
        self.secretary = secretary      # Department Secretary
        self.exam_officer = exam_officer  # Exam Officer
        self.students = students  
        
    def can_administrate(self):
        return f"{self.hod} adminstrate mechanical engineering department"
    
    def can_accept_files(self):
        return f"{self.secretary} can accept students files"
    
    def can_release_result(self):
        return f"{self.exam_officer} releases results every sessions"
    
    def sum_of_all_students(self):
        return f" Total number of {self.students} equal to 500"
    
    def must_be_a_student_or_worker(self):
        return f"Is either one is a student or a worker 2"