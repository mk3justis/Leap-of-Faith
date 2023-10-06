# Create a player class with the necessary attributes
class Player :
    def __init__(self) :
        self.coding = 0
        self.education = 0
        self.social = 0
        self.mental = 0
        self.energy = 0
    
    # Functions to update the attribute values for the player
    def update_coding(self, points) :
        self.coding += points
            
    def update_education(self, points) :
        self.education += points
        
    def update_social(self, points) :
        self.social += points
        
    def update_mental(self, points) :
        self.mental += points
        
    
    # Would like to make this prettier but will be ugly for now
    def event_effects(self, event, condition) :
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
        
        else :
            raise Exception("Invalid condition. Please pass in 0 for yes or 1 for no.")
            
