class HumanBeing:
    def __init__(self,eye,leg,hand,mouth):
        self.eye=eye
        self.leg=leg
        self.hand=hand
        self.mouth=mouth
    
    def can_talk(self):
        return f"{self.mouth} is used for talking "
    
    def can_walk(self):
        return f"{self.leg} is used for walking "
    
    def can_cook(self):
        return f"{self.hand} is used for cooking"
    
    def can_see(self):
        return f"{self.eye} is used for seeing"
    
    