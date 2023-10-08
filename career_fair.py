from job import Jobs
from create_jobs import generate_jobs
from delayPrint import delay_print

def go_to_career_fair(player) :
    jobs = generate_jobs()
    university = Jobs(player.university, f"One of the professors at {player.university} is looking for interns to help them with a summer project. However, they are looking for someone with a high GPA, no less than a 3.0.", 0, 14, 0, 0, 0)
    jobs.append(university)
    dream_company = Jobs(player.dream_job, f"Ah, {player.dream_job}, your dream company. Man, it’d be cool to work there. Alas, it appears that they have quite some high standards. A high GPA, someone with both good social and coding skills, and someone who can handle stress. This is going to be harder than you thought.", 0, 0, 0, 0, 0)
    jobs.append(dream_company)
    player.jobs_list = jobs
    mental_points = 2 + player.mental
    if player.mental < 0 :
        mental_points = 2
    delay_print("Here is the list internship programs at the career fair: \n")
    for company in jobs :
        delay_print(company.name, "\n")
    delay_print("You have ", str(mental_points), " energy to allocate to jobs.\n")
    for job in jobs :
        if mental_points == 0 :
            delay_print("You are out of energy.\n")
            break
        delay_print(job.name,": ", job.description, "\n")
        delay_print("How much energy would you like to allocate to ", job.name,"?\n")
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
                amount = input()
                continue
        job.energy += amount
        mental_points -= amount
        print(f"You now have {mental_points} energy left over.")
    delay_print("Good for you! You finished the Career Fair.\n")