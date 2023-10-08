from job import Jobs
from delayPrint import *

def apply(player):
    energy = player.jobs_list[-1].energy
    dream_stats = player.dream_job_stats
    player.jobs_list.pop()
    dream_company = Jobs(f"{player.dream_job}", "", dream_stats[0], dream_stats[1], dream_stats[2], dream_stats[3], energy)
    player.jobs_list.append(dream_company)
    accepted_applications = []
    delay_print("This year was challenging and turned out to be more arduous than expected. You are starting to reconsider if you're good enough for a job at ", player.dream_job, ". However, it is now time for you to submit your applications! Good luck.\n")
    mental_points = 1 + player.mental
    if mental_points <= 0:
        mental_points = 0
        delay_print("You are not in the mental state to put energy to into your applications.\n")
    else:
        delay_print("You have ", str(mental_points), " energy to put into your applications!\n")
        for job in player.jobs_list:
            if mental_points == 0:
                delay_print("You are out of energy.\n")
                break
            delay_print(job.name, "\n")
            if job == player.jobs_list[4]:
                delay_print("You have been feeling very insecure this semester and are doubting if have good enough skills for a positiion at ", job.name, ". It's time to decide if you take the leap of faith and apply.\n")
            delay_print("How much energy would you like to allocate to ", job.name, "?\n")
            amount = input()
            while True:
                if amount.isdigit():
                    amount = int(amount)
                    if amount <= mental_points and amount >= 0:
                        break
                    else:
                        print(f"Please enter a number 0-{mental_points}.")
                        amount = input()
                else:
                    print("Please enter a number.")
                    continue
            job.energy += amount
            mental_points -= amount
            print(f"You now have {mental_points} energy left over.")
            if mental_points > 0:
                continue
            else:
                break
        if player.education < 0:
            delay_print("Due to your low GPA, you received no responses from companies. Not even rejection slips.\n")
        else:
            delay_print("Good for you! You finished your applications.\n")
            for job in player.jobs_list:
                exponent = 1
                attributes = [player.coding, player.education, player.social, player.mental]
                while exponent < 4:
                    minimum = min(attributes)
                    new_minimum = int(job.energy / pow(2, exponent)) + minimum
                    min_index = attributes.index(minimum)
                    attributes.remove(minimum)
                    attributes.insert(min_index, new_minimum)
                    exponent += 1

                if job.energy > 0:
                    check = 0
                    if attributes[0] >= job.coding:
                        check += 1
                    if attributes[1] >= job.education:
                        check += 1
                    if attributes[2] >= job.social:
                        check += 1
                    if attributes[3] >= job.mental:
                       check += 1
                    if check == 4:
                        if job == player.jobs_list[4]:
                            delay_print_slowest("     \n")
                            delay_print("Whoop-dee-do!!!\n")
                            delay_print_slow("You meet the requirements for an internship at ")
                            delay_print_slowest(job.name, "!\n")
                        else :
                            delay_print("You meet the requirements for an internship at ", job.name, "!\n")
                        accepted_applications.append(job.name)
            if len(accepted_applications) != 0:
                i = 1
                delay_print("Which job do you choose?\n")
                for internship in accepted_applications :
                    delay_print(str(i), ": ", internship, "\n")
                    i += 1
                choice = input("")
                while True:
                    if choice.isdigit():
                        choice = int(choice)
                        if 1 <= choice <= len(accepted_applications):
                            break
                        else:
                            print(f"Please enter a valid number.")
                            choice = input()
                    else:
                        print("Please enter a number.")
                        choice = input()
                        continue
                if accepted_applications[choice - 1] == player.dream_job:
                    delay_print_slow("YOU ACCEPTED ", player.dream_job.upper(), ", YOUR DREAM COMPANY!!! Congratulations, you took the ")
                    delay_print_slowest("leap of faith")
                    delay_print_slow(" and it feels good.\n")
                else:
                    delay_print("You accepted an intern position at ", accepted_applications[choice], ". Good job! Chase that dream position next year.\n")
            else:
                delay_print("Unfornately, your resume impressed no one. You received no responses from companies, not even rejection slips.\n")
                delay_print("Fortunately, You can still apply to King's Chicken Fast Food. Do you want to do that?\n")
                choice = input()
                if(choice.upper() == "YES" or choice.upper() == "Y"):
                    if player.social > 1:
                        delay_print("You got a job at King's Chicken Fast Food. Maybe next year you'll get an internship at ", player.dream_job, ". Until than, enjoy making chicken wings!\n")
                    else:
                        delay_print("You need to get your life together. You can't even get a job at King's.")
                else:
                    delay_print("This summer, you got no job. Maybe you could use this time to sharpen your skills so that maybe next year, you'll get an internship at ", player.dream_job, ".\n")