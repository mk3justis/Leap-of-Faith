from job import Jobs

def apply(player) :
    print(f"This year was challenging and turned out to be more arduous than expected. You are starting to reconsider if you're good enough for a job at {player.dream_job}. However, it is now time for you to submit your applications! Good luck.")
    mental_points = 1 + player.mental
    if mental_points <= 0 :
        mental_points = 0
        print("You are not in the mental state to put energy to into your applications.")
    else :
        print(f"You have {mental_points} energy to put into your applications!")
        for job in player.jobs_list :
            if mental_points == 0 :
                print("You are out of energy.")
                break
            print(f"{job.name}: {job.description}")
            if job == player.dream_job:
                print(f"You have been feeling very insecure this semester and are doubting if have good enough skills for a positiion at {job.name}. It's time to decide if you take the leap of faith and apply.") 
            print(f"How much energy would you like to allocate to {job.name}?")
            amount = input()
            while True :
                if amount.isdigit() :
                    amount = int(amount)
                    if amount <= mental_points and amount >= 0 :
                        break
                    else :
                        print(f"Please enter a number 0-{mental_points}.")
                        amount = input()
                else :
                    print("Please enter a number.")
                    continue
            job.energy += amount
            mental_points -= amount
            print(f"You now have {mental_points} energy left over.")
            if(mental_points > 0):
                continue
            else:
                if player.education < 0 :
                    print("Due to your low GPA, you received no reponses from companies. Not even rejection slips.")
                else:
                    print("Good for you! You finished your applications.")
                    attributes = [player.coding, player.education, player.social, player.mental]
                    exponent = 1
                    while exponent < 4:
                        minimum = min(attributes)
                        attributes.pop(min(attributes))
                        minimum += int(job.energy/pow(2, exponent))
                        exponent += 1
                        
                    energy = player.jobs_list[-1].energy
                    dream_stats = player.dream_job_stats
                    player.jobs_list.pop()
                    dream_company = Jobs(f"{player.dream_job}", "", dream_stats[0], dream_stats[1], dream_stats[2], dream_stats[3], energy)
                    player.jobs_list.append(dream_company)
                    accepted_applications = []
                    for job in player.jobs_list:
                        if job.energy > 0 :
                            check = 0
                            if player.coding >= job.coding :
                                check += 1
                            if player.education >= job.education :
                                check += 1
                            if player.social >= job.social :
                                check += 1
                            if player.mental >= job.mental :
                                check += 1 
                            if check == 4 :
                                if(job == player.jobs_list[4]):
                                    print(f"Whoop-dee-do!!!")
                                print(f"You meet the requirements for an internship at {job}!")
                                accepted_applications.append(job.name)
                    if len(accepted_applications) != 0 :
                        i = 1
                        for internship in accepted_applications :
                            print(f"{i}: {internship}")
                            i+=1
                        choice = input()
                        while True :
                            if choice.isdigit() :
                                choice = int(choice)
                                if 1 <= choice <= len(accepted_applications) :
                                    break
                                else :
                                    print(f"Please enter a number.")
                                    choice = input()
                            else :
                                print("Please enter a number.")
                                amount = input()
                                continue
                        if accepted_applications[i-1] == player.dream_job :
                            print(f"YOU GOT AN INTERNSHIP AT {player.dream_job.upper()}!!! Congratulations, you took the leap of faith and it feels good.")
                        else :
                            print(f"You accepted an intern position at {accepted_applications[i-1]}. Good job! Chase that dream position next year.")