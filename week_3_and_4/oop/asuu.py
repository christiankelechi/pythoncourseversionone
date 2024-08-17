import human_being as hb

class AsuuBody(hb.HumanBeing):
    def __init__(self,president,vice_president,secretary):
        super().__init__() 
        self.president=president
        self.vice_president=vice_president
        self.secretary=secretary
        
    def can_declare_strike(self):
        message=self.president+" of Asuu and its body is known for declaring strike since I was born"
        return message
    
    def cordinate_meetings(self):
        message=self.president+" of Asuu and its body is known for cordinating meetings that normally leads to strike"
        return message
    
    def can_foster_schools_budget(self):
        message=self.president+" and its Board Members helps in administrating Universities"
        return message
    
    
    