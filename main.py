from event import Event
from player import Player

office_hours = Event("You do not understand this chapter\’s material. Luckily, your professor has office hours today. But you do not like your professor. He has a hard to understand accent and every conversation with him is just an endless drain. At the same time, this may be the only way to properly wrap your head around the material. Is it worth going? ")
office_hours.yes(0,1,0,-2)
office_hours.no(0,-1,0,0)

# testing
boysie = Player()
condition = int(input(office_hours.blurb))
boysie.event_effects(office_hours, condition)
boysie.event_effects(office_hours, condition)
print(boysie.coding, boysie.education, boysie.social, boysie.mental)