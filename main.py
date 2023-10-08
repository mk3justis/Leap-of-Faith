'''
This is a text-based game that takes the user through a story of one year at university.
It is full of random events, goals, and emotions.
Enjoy!

Developed by Justis Nazirbage and Matthew Grigg for the FPU Fall '23 Respawn Game Jam event.
'''

from player import Player
from create_events import generate_events
from exams import *
from career_fair import go_to_career_fair
from job_applications import apply
from delayPrint import delay_print
import random


def main():
    event_list = generate_events()
    delay_print("Hi! Just a few questions before we get started...\n")
    name = input("What is your name? ")
    dream_job = input("What is your dream company? ")
    university = input("What university do you attend? ")
    delay_print("Welcome back from summer break! This is your first year at ", university, " and you're hoping that next summer, you can get an internship at ", dream_job, ". But it won't be easy. You'll have to sucessfully balance your coding skills, grades, social life, and mental health in order to get the job. You're sure that this will be easy.\n")
    player = Player([], [], 0, 0, 0, 0, 0, name, dream_job, university)
    focus_rank = 1
    focus_points = 4
    already_chose_focus = []
    while focus_rank <= 3:
        delay_print("What was your number ", str(focus_rank), " focus this summer?\n")
        if player.coding == 0:
            print("1: Working on personal coding projects and learning new technologies.")
        if player.social == 0:
            print("2: Hanging out with friends and spending time with family.")
        if player.education == 0:
            print("3: Studying last semester's notes and learning upcoming course content.")
        if player.mental == 0:
            print("4: Taking time for yourself to relax and finding inner peace.")
        focus = input()
        while True:
            if focus.isdigit():
                focus = int(focus)
            else:
                focus = input("Please enter a number.\n")
                continue
            if focus in already_chose_focus or focus < 1 or focus > 4:
                continue
            else:
                break

        if focus == 1 and player.coding == 0:
            player.update_coding(focus_points)
        elif focus == 2 and player.social == 0:
            player.update_social(focus_points)
        elif focus == 3 and player.education == 0:
            player.update_education(focus_points)
        elif focus == 4 and player.mental == 0:
            player.update_mental(focus_points)
        already_chose_focus.append(focus)
        focus_points -= 1
        focus_rank += 1

    week = 1
    events = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
              27, 28, 29, 30, 31, 32, 33, 34]
    condition = ''
    while week < 32:
        delay_print("Week ", str(week), "\n")
        event_type = 0  # Event type. 1 = Rare, 2-8 = common, 9-10 = none
        event = 0
        if week == 11:
            delay_print("EXAM NEXT WEEK!\n")
            event_type = random.randint(1, 10)
        elif week == 12:
            exam1(player)
            week += 1
            continue  # some code for exam 1 goes here
        elif week == 15:
            delay_print("CAREER FAIR NEXT WEEK!\n")
            event_type = random.randint(1, 10)
        elif week == 16:
            go_to_career_fair(player)
            week += 1
            continue  # some code for the career fair goes here
        elif week == 28:
            delay_print("EXAM NEXT WEEK!\n")
            event_type = random.randint(1, 10)
        elif week == 29:
            exam2(player)
            week += 1
            continue  # some code for exam 2 goes here
        else:
            event_type = random.randint(1, 10)

        if week == 28:
            modifier = 0
            player.dream_job_stats = [player.coding + modifier, player.education + modifier, player.social + modifier, player.mental + modifier]

        if event_type == 1:
            event = random.randint(28, 34)
        elif event_type > 1 and event_type < 9:
            event = random.randint(0, 27)
        elif event_type >= 9:
            delay_print("There doesn't seem to be much going on this week. What would you like to do?\n")
            print("1: Experimenting and developing code")
            print("2: Hanging out with friends")
            print("3: Getting ahead on the material in class")
            print("4: Relaxing and destressing")
            while True:
                choice = input()
                if choice.isdigit():
                    choice = int(choice)
                    break
                else:
                    print("Please enter a number.")
                    continue
            #print(choice)
            if choice == 1:
                player.update_coding(1)
            elif choice == 2:
                player.update_social(1)
            elif choice == 3:
                player.update_education(1)
            elif choice == 4:
                player.update_mental(1)
            week += 1
            continue
        # Generate the event:
        while True:
            if events[event] == -1:
                if event_type == 1:
                    event = random.randint(28, 34)
                elif event_type > 1 and event_type < 9:
                    event = random.randint(0, 27)
                continue
            # This section of code prevents an event from happening twice
            # It uses an array to store the number associated with that event
            # When that event happens, the number becomes 0, ensuring that it will never happen again
            event_object = event_list[events[event]]
            events[event] = -1
            delay_print(event_object.blurb)
            condition = input()
            while True:
                # condition = str(condition)
                condition = condition.lower()
                if condition == 'y' or condition == 'yes':
                    player.event_effects(event_object, 0)
                    break
                elif condition == 'n' or condition == 'no':
                    player.event_effects(event_object, 1)
                    break
                else:
                    condition = input("Please enter Y/N or Yes/No.\n")
                    continue
            break

        week += 1
    apply(player)


main()
delay_print("Created by Matthew Rigg and Jusitis Nazirbage.\n")
delay_print("Credits to Katelyn Bailey for testing the game and ChatGPT for helping us when we were stumped by logical errors :)\n")
