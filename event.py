import pandas as pd

class Event :
    def __init__(self, blurb) :
        self.blurb = blurb
        attrs = [["yes", "no"],
                 ["coding", "education", "social", "mental"]]
        self.attributes = pd.DataFrame(attrs)
    
    def yes(self, *values) :
        i = 0
        for value in values :
            self.attributes.iloc[0][i] = value 
            i+=1
            
    def no(self, *values) :
        i=0
        for value in values :
            self.attributes.iloc[1][i] = value
            i+=1
