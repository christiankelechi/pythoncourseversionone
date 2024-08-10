import mechanicalengineering as me

class MechStudents(me.MechanicalEngineering):
    def __init__(self, name, reg_number, level, cgp):
        self.name = name                  
        self.reg_number = reg_number      
        self.level = level                
        self.cgp = cgp  
        
    def can_offer_course(self):
        return "Students in mechanical engineering offers at least 5 courses each semester"
    
    def graduating_with_first_class(self):
        return f"25  students graduated with first class with at cgp of 4.6 in Mechanical engineering"
    
    
    
    