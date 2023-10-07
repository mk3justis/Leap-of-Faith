from event import Event
from player import Player
from create_events import generate_events

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
import random

def main():
    event_list = generate_events()
    name = input("What is your name? ")
    dream_job = input("What is your dream company? ")
    university = input("Which university do you attend? ")
    player = Player(0, 0, 0, 0, 0, name, dream_job, university)
    focus_rank = 1
    focus_points = 4

    while focus_rank <= 3:
        print(f"What was your number {focus_rank} focus this summer?")
        if player.coding == 0 :
            print("1 for Coding")
        if player.social == 0:
            print("2 for Social")
        if player.education == 0:
            print("3 for Education")
        if player.mental == 0:
            print("4 for Mental")
        focus = int(input())

        if focus == 1 and player.coding == 0 :
            player.update_coding(focus_points)
        elif focus == 2 and player.social == 0 :
            player.update_social(focus_points)
        elif focus == 3 and player.education == 0 :
            player.update_education(focus_points)
        elif focus == 4 and player.mental == 0 :
            player.update_mental(focus_points)
        focus_points -= 1
        focus_rank += 1
        print(player.coding)

        week = 1
        while week < 32 :
            event_number = 0  # Event type. 1 = Rare, 2-8 = common, 9-10 = none
            event = 0
            if week == 8 :
                pass  # some code for exam 1 goes here
            elif week == 16 :
                pass  # some code for the career fair goes here
            elif week == 24 :
                pass  # some code for exam 2 goes here
            else:
                event_number = random.randint(1, 10)

            # Generate the event:
            if event_number == 1 :
                event = random.randint(28, 34)
            elif event_number > 1 and event_number < 9 :
                event = random.randint(0, 27)
                
            # This section of code prevents an event from happening twice
            # It uses an array to store the number associated with that event
            # When that event happens, the number becomes 0, ensuring that it will never happen again
            events = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                        27, 28, 29, 30, 31, 32, 33, 34]
            event_list[events[event]]
            events[event] = -1

            if event_number >= 9 :  # None
                print("There doesn't seem to be much going on this week. What would you like to do?")
                print("1 for experimenting and developing code")
                print("2 for hanging out with friends")
                print("3 for getting ahead oon the material in class")
                print("4 for relaxing and destressing")
                choice = int(input(""))
                
                if choice == 1 :
                    player.update_coding(1)
                elif choice == 2 :
                    player.update_social(1)
                elif choice == 3 :
                    player.update_education(1)
                elif choice == 4 :
                    player.update_mental(1)
            week = week + 1

main()
