def exam1(player) :
    ready = input("Are you ready for your first exam?\n")
    
    if player.education > 10 :
        player.update_education(5)
        print("Wow! That was no match for you!")
    elif player.education > 7 :
        player.update_education(3)
        print("Good job, not too shabby.")
    elif 4 < player.education < 8 :
        print("Well, C's get degrees.")
    elif 2 < player.education < 5 :
        player.update_education(-3)
        print("Not your best work, but you didn't die.")
    elif player.education < 3 :
        player.update_education(-5)
        print("Oof, maybe STEM isn't for you.")
        
def exam2(player) :
    ready = input("Are you ready for your second exam?\n")
    
    if player.education > 14 :
        player.update_education(5)
        print("Wow! That was no match for you!")
    elif player.education > 11 :
        player.update_education(3)
        print("Good job, not too shabby.")
    elif 8 < player.education < 12 :
        print("Well, C's get degrees.")
    elif 6 < player.education < 9 :
        player.update_education(-3)
        print("Not your best work, but you didn't die.")
    elif player.education < 7 :
        player.update_education(-5)
        print("Oof, maybe STEM isn't for you.")