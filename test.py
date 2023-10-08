# office_hours = Event("You do not understand this chapter\’s material. Luckily, your professor has office hours today. But you do not like your professor. He has a hard to understand accent and every conversation with him is just an endless drain. At the same time, this may be the only way to properly wrap your head around the material. Is it worth going? ")
# office_hours.yes(0,1,0,-2)
# office_hours.no(0,-1,0,0)

# # testing
# boysie = Player()
# condition = int(input(office_hours.blurb))
# boysie.event_effects(office_hours, condition)
# boysie.event_effects(office_hours, condition)
# print(boysie.coding, boysie.education, boysie.social, boysie.mental)

from event import Event
from player import Player
from create_events import generate_events
import random

def main():
    event_list = generate_events()
    name = "b"
    dream_job = "o"
    university = "p"
    player = Player(0, 0, 0, 0, 0, name, dream_job, university)
    epoch = 0
    while epoch < 100 :
        print(f"Epoch: {epoch+1}")
        week = 1
        events = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                27, 28, 29, 30, 31, 32, 33, 34]
        while week < 32 :
            event_type = 0  # Event type. 1 = Rare, 2-8 = common, 9-10 = none
            event = 0
            if week == 8 or week == 16 or week == 24 :
                week+=1
                continue  # some code for exam 1 goes here
            else:
                event_type = random.randint(1, 9)
            
            
            if event_type == 1 :
                event = random.randint(28, 34)
            elif event_type > 1 and event_type < 10 :
                event = random.randint(0, 27)
            # Generate the event:
            while True :
                if events[event] == -1 :
                    if event_type == 1 :
                        event = random.randint(28, 34)
                    elif event_type > 1 and event_type < 10 :
                        event = random.randint(0, 27)
                    continue
                # This section of code prevents an event from happening twice
                # It uses an array to store the number associated with that event
                # When that event happens, the number becomes 0, ensuring that it will never happen again
                event_object = event_list[events[event]]
                events[event] = -1
                player.event_effects(event_object, 0)
                break
                
            
                
            week += 1
        epoch += 1
        
    print(f"Coding: {player.coding / 100}, Education: {player.education / 100}, Social: {player.social / 100}, Mental: {player.mental / 100}")

main()