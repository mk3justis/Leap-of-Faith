from job import Jobs

def generate_jobs() :
    job_list = []
    bigs_marketing = Jobs("Bigs Marketing", "Bigs Marketing is a software company that specializes in sales and marketing software. While the coding for this sort of job is light, you will have to talk to a lot of people and know how to make software that people can interact with.", 0, 0, 10, 0, 0)
    job_list.append(bigs_marketing)
    jameson_simulations = Jobs("Jameson Simulations Internship", "Jameson Simulations is a software company that specializes in making flight simulations for the airforce. They are currently looking for interns to help develop their software. However, you’ve heard of Jameson Simulations. Lots of changes are made to the project on the fly, resulting in a high stress environment. You’ll need good stress management if you want this.", 0, 0, 0, 6, 0)
    job_list.append(jameson_simulations)
    asco_software = Jobs("Asco Software Internship", "ASCO is looking for Software Engineering Interns to bring their products to life. The job entails a lot of coding, but you will mostly be left to your own devices and likely not have to talk to a lot of people.", 15, 0, 0, 0, 0)
    job_list.append(asco_software)
    return job_list
# University Internship: One of the professors at your university is looking for interns to help them with a summer project. However, they are looking for someone with a high GPA, no less than a 3.0.
# Bigs Marketing Internship: Bigs Marketing is a software company that specializes in sales and marketing software. While the coding for this sort of job is light, you will have to talk to a lot of people and know how to make software that people can interact with.
# Jameson Simulations Internship: Jameson Simulations is a software company that specializes in making flight simulations for the airforce. They are currently looking for interns to help develop their software. However, you’ve heard of Jameson Simulations. Lots of changes are made to the project on the fly, resulting in a high stress environment. You’ll need good stress management if you want this.
# ASCO Software Internship: ASCO is looking for Software Engineering Interns to bring their products to life. The job entails a lot of coding, but you will mostly be left to your own devices and likely not have to talk to a lot of people.
# Dream Company Internship: Ah, {Dream company name}, your dream company. Man, it’d be cool to work there. Alas, it appears that they have quite some high standards. A high GPA, someone with both good social and coding skills, and someone who can handle stress. This is going to be harder than you thought.
