import pandas as pd
class Event:
    def __init__(self, blurb):
        self.blurb = blurb
        attrs = [["yes", "no"],
                 ["coding", "education", "social", "mental"]]
        self.attributes = pd.DataFrame(attrs)

    def yes(self, *values):
        i = 0
        for value in values:
            self.attributes.iloc[0][i] = value
            i += 1

    def no(self, *values):
        i = 0
        for value in values:
            self.attributes.iloc[1][i] = value
            i += 1


def check_event(event, event_object):
    if (event == 1):
        event_object.blurb = "Bad Office Hours - You do not understand this chapter\’s material. Luckily, your professor has office hours today. But you do not like your professor. He has a hard to understand accent and every conversation with him is just an endless drain. At the same time, this may be the only way to properly wrap your head around the material. Is it worth going? "
        event_object.yes(0, 1, 0, -2)
        event_object.no(0, -1, 0, 0)
    elif (event == 2):
        event_object.blurb = "Tutoring Center - You do not understand this chapter’s material. You know that the tutoring center offers free tutoring, and that your class is one of the classes that they tutor. However, you agreed to meet with your friend for lunch after class. Do you go to the tutoring center? "
        event_object.yes(0, 2, -1, 0)
        event_object.no(0, -1, 1, 0)
    elif (event == 3):
        event_object.blurb = "Lots of Homework - Your professors were absolute beasts this week. The workload seems to be never ending. You know you can get it all done, provided you skip going to Church with friends. Which’ll suck, not only because these are your friends, but also, the pastor gives very nice sermons that you’ve learned many good life lessons from. Do you skip Church?"
        event_object.yes(0, 1, 0, 0)
        event_object.no(0, -1, 0, 2)
    elif (event == 4):
        event_object.blurb = "So….Very….Tired - You wake up very tired this morning. You know that you have your hardest class first thing today. You’ve sat through enough lectures of this. Is it even worth getting out of bed today?"
        event_object.yes(0, 1, 0, -1)
        event_object.no(0, -1, 0, 1)
    elif (event == 5):
        event_object.blurb = "That Lecture Sucked - It’s Friday. It’s your last class. You are tired. You are so done with this week and are ready for the weekend. You have one more lecture to get through. But man, that last lecture SUCKED. You want to go back to the dorm and maybe relax for a few minutes before starting work. But, your professors' office hours are right after class. You’re sure that if you stop them and ask, they’d be more than willing to help. But, you are so very tired. Is it worth talking to them?"
        event_object.yes(0, 2, 0, -1)
        event_object.no(0, -1, 0, 2)
    elif (event == 6):
        event_object.blurb = "JavaScript Workshop - The computer club is hosting a JavaScript Workshop this weekend. While you have some knowledge of JavaScript, it has been quite some time since you’ve used it, and could use a tune up. Plus, there are lots of people attending that may have similar interests as you. However, you do have that project due Monday that you are a little behind on. Do you attend the workshop?"
        event_object.yes(1, 0, 1, 0)
        event_object.no(0, 1, -1, 0)
    elif (event == 7):
        event_object.blurb ="Computer Club Meet - Your friend approaches you and suggests that you come with them to the computer club meet this week. This week, they’ll be covering special Python Classes, something that you’ve been looking into yourself. You could even meet some people here. However, you have a lot of work this week. If you really crunch, you might be able to get it all done. Is it worth the crunch?"
        event_object.yes(2, 0, 2, -1)
        event_object.no(0, 1, -1, 0)
    elif (event == 8):
        event_object.blurb = "Free Website - You find a website that teaches coding. For Free! For free, you can access lessons for ALL the different coding languages! And they have activities that you can use to practice your code. This is your dream come true. One problem. In order for this sort of time commitment, you may have to sacrifice hanging out with your friend this weekend. It’s been a bit since you’ve hung out, and your friend might not like delaying this any longer. Do you use the website?"
        event_object.yes(2, 0, -1, 0)
        event_object.no(0, 0, 2, 0)
    elif (event == 9):
        event_object.blurb = "Smart Friend - Your friend has been learning and experimenting with all sorts of random computing languages. One day, they approach you and offer to give you some lessons. This would be a very rare opportunity, however, you do have a lot of work this week. You may need to crunch to get all of this done. Do you take them up on your offer?"
        event_object.yes(2, 0, 1, 0)
        event_object.no(0, 1, -1, 0)
    elif (event == 10):
        event_object.blurb = "Programming Homework - This week’s homework for your programming class is actually quite easy. You’ll be able to get it done quickly, and even gain some good coding experience. But alas, it could take some time, which could eat up into your travel plans with your friends. You were going to go to Ribby's, the famous Barbecue place in the next town.  Do you do the homework?"
        event_object.yes(1, 1, 0, 1)
        event_object.no(0, 0, 2, 1)
    elif (event == 11):
        event_object.blurb = "Parental Visit - Your parents called this week. They’re coming up to visit you this weekend. While your parents coming up is nice, you were hoping that this weekend, you could take a break and work on a little personal project you started this summer, since you don’t really have a lot of work this weekend. This opportunity may never come up again. Do you ask your parents if you can reschedule?"
        event_object.yes(2, 0, 0, 1)
        event_object.no(0, 0, 2, 0)
    elif (event == 12):
        event_object.blurb = "Game Night with the Boys - Every week, you and your friends get together and play Crag Cats 3. Your role in your party is quite vital. However, this week, you have an absolute TON of homework. Your professors were not merciful this week. You’re sure that you could get it all done this weekend, but it’ll be quite the crunch. Do you tell your friends that you may have to cancel this week?"
        event_object.yes(0, 1, -1, 0)
        event_object.no(0, 0, 2, -1)
    elif (event == 13):
        event_object.blurb = "Classmate needs Help - The guy that sits behind you in class comes up to you and says that they noticed you answer the professor’s questions a lot and that you seem to know what you’re doing. They then ask for your help with the homework. While you don’t fully believe them about you knowing what you’re doing, you do know that you at least know enough to maybe help them. And this could be an opportunity to make a friend. But, you are also very tired and not sure if you can handle teaching someone right now. Do you see if you can teach them?"
        event_object.yes(0, 1, 1, -1)
        event_object.no(0, 0, -1, 1)
    elif (event == 14):
        event_object.blurb = "Annoying Friend - Your friend invites you to come to lunch with him and his family this weekend, since he’s a local. It’ll be nice and dandy, but your friend can be a little annoying, especially when it comes to conversation, and a meal involves a LOT of conversation. Do you go to lunch with him?"
        event_object.yes(0, 0, 2, -1)
        event_object.no(0, 0, -1, 2)
    elif (event == 15):
        event_object.blurb = "Faith Crisis - It’s Sunday. That means that it’s time to go to Church. You like Church. The pastor is a good speaker and has taught you many good life lessons. Plus, it’s nice to go with your little group of friends. However, lately, you’ve been having some issues with the Church. Last week’s mass, your pastor went on a rant about something that you really didn’t agree with. This weekend, your friend invites you to come to mass again. Do you go?"
        event_object.yes(0, 0, 2, -2)
        event_object.no(0, 0, -2, 2)
    elif (event == 16):
        event_object.blurb = "Take a Walk - It’s been a long, exhausting week of work. After your final class of the week, you decide that it’d be beneficial for you if you take a walk before dinner. You know that if you don’t get to the cafeteria soon, a long line will form and you'll be stuck there for a while, which could mess up your Friday night study time. But you really need this walk. Do you take the walk?"
        event_object.yes(0, -1, 0, 2)
        event_object.no(0, 1, 0, -1)
    elif (event == 17):
        event_object.blurb = "Hiding  - You are very tired from classes this week. Your last class ends at 4 today. Usually, after your final class, you meet your friend at the cafeteria and get dinner. But you are just so very tired and burnt out. You do not have the mental capacity to maintain a conversation right now. There is a corner in the cafeteria, where you can just eat alone. Do you hide in the corner this time?"
        event_object.yes(0, 0, 1, -1)
        event_object.no(0, 0, -1, 1)
    elif (event == 18):
        event_object.blurb = "TV Break - It’s Friday. It’s been a hard week. You’ve just got back from dinner and you figure you could watch some TV. You have all weekend to do work. You’re sure goofing off tonight will be okay. Do you do it?"
        event_object.yes(0, 0, 0, 1)
        event_object.no(0, 1, 0, 0)
    elif (event == 19):
        event_object.blurb = "Morning Routine - You want to know the best part of the mornings? The routine! Every morning, you get up early, hit the gym, have breakfast, and take a shower. It all allows you to start the day off feeling nice and refreshed. However, you have a lot of work tonight. It’s getting very late. You’re sure that if you power through it all, you might be able to get it done and without compromising your morning routine all that much. Do you power through the work and get up late tomorrow?"
        event_object.yes(0, 1, 0, -2)
        event_object.no(0, 0, 0, 1)
    elif (event == 20):
        event_object.blurb = "The Plant - Your roommate got a plant from their parents. However, they have made no effort to take care of it. But perhaps you could give it a shot. After all, taking care of a plant can be quite therapeutic. However, it could eat up into your study time. Do you ask your roommate for the plant?"
        event_object.yes(0, -1, 0, 2)
        event_object.no(0, 1, 0, -1)
    elif (event == 21):
        event_object.blurb = "Jakie the Star - “The Adventures of Jake StarRaptor 2” has just come out on Steam. You’ve been looking forward to this all year and can not WAIT to start playing! However, you do have quite a lot of work to do this week. You could play the game and crunch the work this week, but this work is quite difficult. You may not do it fully correctly if you crunch. But at the same time, Jake the Star awaits. Do you play the game?"
        event_object.yes(0, -1, 0, 2)
        event_object.no(0, 2, 0, -1)
    elif (event == 22):
        event_object.blurb = "Code Central - You found the website that taught you how to code back in grade school, codecentral.com,  and decide to give it a whack again. For old times sake. However, your professors were annoying and gave a project due Monday. Do you spend the weekend coding?"
        event_object.yes(2, 0, 0, 1)
        event_object.no(0, 1, 0, 0)
    elif (event == 23):
        event_object.blurb = "Home Game Night - One of your roommates decides that you all should have a game night tonight. All of you will get together and play Party Box Central 7. It sounds quite fun, and it’s been some time since you’ve hung out recreationally with your roommates. But alas, you have lots of work this week. Do you join in the game night?"
        event_object.yes(0, -1, 2, 0)
        event_object.no(0, 1, 0, 0)
    elif(event == 24):
        event_object.blurb = "Listening to Music - Work is hard. Really hard. But one of the upsides is that you get to listen to music while you do it. You’re singing along and getting in good with the vibes when you realize all this fun is distracting you from your work. You’re sure you can get it done in time, but it may take longer, delaying you from getting more work done. Do you turn it off?"
        event_object.yes(0, 1, 0, -1)
        event_object.no(0, -1, 0, 1)
    elif(event == 25):
        event_object.blurb = "Code Family - Your programming professor assigned a project that they’re allowing to be done in groups. Group work is fine and all, but you’ve had some bad experiences with group projects in the past. Plus, in order to share code, you all would have to use Code Family, which is a very difficult app to use and deal with. But it’ll get done faster. Is it worth it?"
        event_object.yes(1, 0, 1, -1)
        event_object.no(0, 0, -1, 0)
    elif(event == 26):
        event_object.blurb = "Group Project - Your professor has assigned a project that they’re allowing to be done in groups. You’ve had some bad experiences working in groups before. You always have to get everyone to work together and make sure that everyone does their part. Exhausting. But it’ll get done faster and likely better. Is it worth it?"
        event_object.yes(0, 2, 1, -1)
        event_object.no(0, 1, -1, 1)
    elif(event == 27):
        event_object.blurb = "Stay After Class - Your professor asks you to stay after class. However, your programming class is right after this one and it’s on the other side of campus. If you don’t leave NOW, you will be late and miss the first chunk of class. Do you stay?"
        event_object.yes(-1, 1, 0, 0)
        event_object.no(1, 1, 0, 0)
    elif(event == 28):
        event_object.blurb = "Study Session - Your roommate is struggling with a class that you are very good at. One day, after class, they come up to you and ask if you could do some study sessions with them. You don’t have a lot of teaching experience, and your roommate can be kind of intense sometimes, so this could be more draining for you than actually productive. On the other hand, you two don’t have that much of a connection. Do you help him?"
        event_object.yes(0, 0, 1, -1)
        event_object.no(0, 0, -1, 1)
    elif (event == 29):
        event_object.blurb = "Sister’s Play - Your younger sister is in the school play, and you said that you would go. So this weekend, you make the long drive home and see the performance. You’re quite proud of your sister. She’s growing up right before your eyes, and this play allowed you to really see that. You’re glad you came. As you’re packing your bags to head back, your mom tells you that you can stay the weekend. It’s been a while since you came home, and you are getting sick of dorm food and dorm mattresses. However, you do have early morning classes on Monday, so if you do spend the weekend here, you may come in Sunday all tired. Plus, it’s much easier to study in your dorm than it is in your noisy house. Do you stay?"
        event_object.yes(0, -1, 4, 5)
        event_object.no(0, 2, -4, 0)
    elif (event == 30):
        event_object.blurb = "International Technology Summit - About an hour away from the university, the International Technology Summit is taking place. There will be a lot of speakers from all kinds of companies, each talking about their technologies. And you may meet some people too. However, you do have to miss a couple of classes in order to make it on time, and these classes are difficult. You may have problems understanding the homework if you skip. Is it worth going?"
        event_object.yes(5, -2, 4, 0)
        event_object.no(0, 1, -2, -2)
    elif (event == 31):
        event_object.blurb = "Disaster  - A Natural disaster is heading for your school. Your university announces that classes are canceled for the remainder of the week. This is good, as it allows you to quickly get your work done and maybe even do some coding! However, your parents call and say that they are very uncomfortable with you being there during a disaster. It’s a long and stressful drive, and the roads may be clogged up with other people leaving to go to other places. And you may not be able to code as much as you would if you do the drive. Do you try to make the drive?"
        event_object.yes(2, 2, 4, -3)
        event_object.no(4, 4, -3, 0)
    elif (event == 32):
        event_object.blurb = "Old Friend From High School - Your best friend from high school is coming from his school to visit. It’s been a bit since you’ve seen them, since you spent all summer getting ready for college and have drifted apart a little bit. However, you do have a significant amount of work this weekend. You’re sure you can power through it all if you half ass an assignment or two. Do you hang out with him?"
        event_object.yes(0, -1, 4, 4)
        event_object.no(0, 1, -4, -2)
    elif (event == 33):
        event_object.blurb = "Code Runners Workshop - The software company Code Runners is coming to the university and is hosting a workshop on all sorts of aspects of coding. It would be very beneficial to go. But there is one problem. You have homework. A lot of it. If you go, it would take a lot of crunching to get it all done this weekend, which could be stressful. Do you go?"
        event_object.yes(5, 0, 2, 0)
        event_object.no(0, 1, 0, -2)
    elif (event == 34):
        event_object.blurb = "Code of the Hour - The Programming Club is throwing its annual “Code of the Hour” programming event! This would be a big chance to really show off your skills as a programmer. However, you do have a quiz on Thursday, and you do not understand the material all that much. You should probably study. Do you go to the event?"
        event_object.yes(4, -1, 2, 0)
        event_object.no(0, 2, -1, 0)
    elif (event == 35):
        event_object.blurb = "Wellness Week - It’s Wellness Week! Everywhere on campus is some sort of mental health wellness stand, designed to help you relax and chill for a bit. We’re talking meditation, therapeutic legos, herb care, and a whole lot more! This all sounds quite appealing. It’s been a bit since you’ve had a decent break. However, you know that you have an assignment due the day after tomorrow. It shouldn’t be too difficult, but you fear if you take this break, you may not get it done in time. Do you take this day to relax and take a break?"
        event_object.yes(0, 0, 0, 4)
        event_object.no(0, 1, 0, -2)
