# Create a player class with the necessary attributes
class Player :
    def __init__(self, coding, education, social, mental, energy, name, dream_job, university) :
        self.coding = coding
        self.education = education
        self.social = social
        self.mental = mental
        self.energy = energy
        self.name = name
        self.dream_job = dream_job
        self.university = university
    
    # Functions to update the attribute values for the player
    def update_coding(self, points) :
        self.coding += points
            
    def update_education(self, points) :
        self.education += points
        
    def update_social(self, points) :
        self.social += points
        
    def update_mental(self, points) :
        self.mental += points
        
    
    # Private function to convert user input to 0 or 1.
    def __condition_update(self, condition) :
        condition.lower() 
        if condition == 'y' or condition == 'yes' :
            condition = 0
        elif condition == 'n' or condition == 'no' :
            condition = 1
        else :
            raise Exception("Invalid condition.")
    
    # Calls private function and updates stats based on event.
    def event_effects(self, event, condition) :
        self.__condition_update(condition)
        
        if condition == 0 :
            self.update_coding(event.attributes.iloc[0][0])
            self.update_education(event.attributes.iloc[0][1])
            self.update_social(event.attributes.iloc[0][2])
            self.update_mental(event.attributes.iloc[0][3])
            
        elif condition == 1 :
            self.update_coding(event.attributes.iloc[1][0])
            self.update_education(event.attributes.iloc[1][1])
            self.update_social(event.attributes.iloc[1][2])
            self.update_mental(event.attributes.iloc[1][3])
            
