#!/usr/bin/python

import praw
from config import *
import os
import random
import time
import re

#Bot login
def bot_login():
    r = praw.Reddit(username = userN,
                    password = userP,
                    client_secret = cSC,
                    client_id = cID,
                    user_agent = userAgent)
    return r
#    print("Logged in")
#    print(r.user.me())


def run_bot(r, comments_replied_to2, WholeWord):
    for comment in r.subreddit('Elmindreda_bot').comments(limit = 25):
        comment.refresh()

        #Randomness to make sure Lopen doesn't reply to every comment with these words
        pancake_num = random.randint(1, 12)
        gancho_num = random.randint(1, 8)
##        elayne_num = (1, 5)

#Lopen joke
        for key in ["lopen joke", "lopen jokes", "one armed herdazian", "one-armed herdazian", "one-armed-herdazian", "one armed herdaz", "one-armed-herdaz"]:
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                lopen_joke_quotes = [
                    """Oh. Oh. Question for you! What did the one-armed Herdazian do to the man who stuck him to the wall?

Nothing. The Herdazian was 'armless.""",

                    """How do you get a one-armed Herdazian out of a tree?

Wave!""",

                    """How many one-armed Herdazians does it take to screw in a lightbulb?

None. That's what cousins are for!""",

                    """I'd tell you a joke about one-armed Herdazian, but I can't remember. I am stumped.""",

                    """I'd tell you a joke about one-armed Herdazian, but I'm afraid I might sound too off-handed.""",

                    """Why do Herdazian women like One-Armed Herdazian men so much?,

They like them because they find them quite disarming""",

                    "I heard High Prince Sadeas got a one-armed butler. Serves him right!",

                    """You've probably heard of the man who lost his arm and leg.

Despite technically being all right, in reality he's dead. But he wasn't buried.

Because there was nothing left.""",

                    "If your happy and you know it, clap your.... Oh....",

                    "Careful! If you guess one more letter wrong he'll be hanged!",

                    "I heard a joke about a one-armed Herdazian, but I can't share it because I don't have the rights.",

                    """Do you know how to get *two-armed* Herdazians to do what you want?

Take away both their spear!"""                    
                ]
                comment.reply(random.choice(lopen_joke_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

#gancho
        for key in ["gancho", "muli", "gon", "penhito"]:
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and gancho_num == 2:
                lopen_quotes = [
                    "[OB spoilers] >!I must first convince the ground that I am not abandoning her. Like a worried lover, sure, she must be comforted and reassured that I will return following my dramatic and regal ascent to the sky.!<",
                    "[OB spoilers] >!Don't worry, dear one. The Lopen is vast enough to be possessed by many, many forces, both terrestrial and celestial! I must soar to the air, for if I were to remain only on the ground, surely my growing magnitude would cause the land to crack and break.!<",
                    "[WOR spoilers] >!Ha! Hey, Chilinko, come back here, I need to stick you to the wall!!<",
                    "Ain't nothing wrong with being a woman, gancho. Some of my relatives are women.",
                    "[WOR spoilers] >!Yes! Everybody give the Lopen your spheres! I have glowing that needs to be done!!<",
                    "[WOR spoilers] >!Sure, a glowing Lopen is a great Lopen. But even a one-armed Herdazian can part the chasms better than any storming Alethi lighteyes.!<",
                    "Some of my cousins, they call me the Lopen because they haven't ever heard anyone else named that. I've asked around a lot, maybe one hundred...or two hundred...lots of people, sure. And nobody has heard of that name.",
                    "If you’re crazy, you’re a good type, and I like you. Not a killing-people-in-their-sleep type of crazy. Besides, We all follow crazies all the time. Do it every day with lighteyes.",
                    "You can thank me, naco, for inspiring this great advance in your learning. People—and little things made out of nothing too, sure—are often inspired near the Lopen.",
                    "‘Lopen,’ my mother always says, ‘you must learn these to laugh before others do. Then you steal the laughter from them, and have it all for yourself.’ She is a very wise woman.",
                    "[Mild ROW, major OB spoilers] >!...look into the future and find out if I beat Huio at cards tomorrow.!<",
                    "Hey, gancho! Hey! You want me, I think. You can use me. We Herdazians are great fighters, gon. You see, this one time, I was with, sure, three men and they were drunk and all but I still beat them.",
                    "A one-armed Herdazian is still twice as useful as a no-brained Alethi.",
                    "Behold the Lopen gesture!",
                    "***Makes the Lope gesture***",
                    "***Make the double Lopen gesture towards the sky***",
                    "My other hand?' Lopen said. 'The one that was cut off long ago, eaten by a fearsome beast? It is making a rude gesture toward you right now. I thought you would want to know, so you can prepare to be insulted.",
                    "Can you feel it? Something just changed. I believe that's the sound the world makes when it pisses itself.",
                    "It is said that you shouldn't bet against a one-armed Herdazian in a drinking contest!"

                ]
                comment.reply(random.choice(lopen_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")


#pancakes
    for key in ["journey before destination"]:
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and pancake_num == 2:
                lopen_quotes = [
                    "[OB spoilers] >!Do you mean Journey Before Pancakes, gancho?!<",
                    "[OB spoilers] >!Life before Death, Strength Before Weakness, Journey beforePancakes!<",
                    "[OB spoilers] >!NOW? I was saving that for a dramatic moment, you penhito! Why didn't you listen earlier? We were, sure, all about to die and things!!<",
                    "[DS spoilers] >!I'll do it, then. I've got to protect people, you know? Even from myself. Gotta rededicate to being the best Lopen possible. A better, improved, extra-incredible Lopen.!<"
                ]
                comment.reply(random.choice(lopen_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

                
#happy
        for key in ["good", "happy", "awesome", "nice"]:
            if WholeWord(key)(comment.body) and WholeWord("lopen")(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                happy_quotes = [
                    f"{key} is good! For more awesomeness, just ask for \"Lopen Joke\", and I'll give some to you!"
                ]
                comment.reply(random.choicehappy_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

#sad
        for key in ["sad", "depress", "depressed", "trauma", "depression"]:
            if WholeWord(key)(comment.body) and WholeWord("lopen")(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                sad_quotes = [
                    f"Hey gancho, you used {key} in your comment. If you're sad, want to hear a joke? Just type \"The Lopen Joke\", and I'll give one to you!",
                    "Gon, you good? I detected {key} in your comment."
                ]
                comment.reply(random.choice(sad_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

#Correction
        for key in ["lopen", "Lopen"]:
            if key in comment.body  and not "The Lopen" in comment.body and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                correction_quotes = [
                    "That would be *The Lopen* for you, muli!",
                    "How dare you disrespect The Lopen, King of Alethkar, by merely calling him 'lopen'?",
                    "Lopen? Just Lopen? Here, I am giving you the Lopen gesture!"
                ]
                comment.reply(random.choice(correction_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

#cousin
        for key in ["cousin", "cousins"]:
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                cousin_quotes = [
                    "You can never have enough cousins, gon!"
                ]
                comment.reply(random.choice(cousin_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

#pancakes-2
    for key in ["pancake", "pancakes"]:
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and pancake_num in (2, 3, 4):
                pan2cakes_quotes = [
                    "Yeah, pancakes are alright, but have you tasted chouta?"
                ]
                comment.reply(random.choice(pan2cakes_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

#pancakes-2
    for key in ["chouta"]:
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                chouta_quotes = [
                    "Chouta. Herdazian food, gon. Good stuff.",
                    "It's meat. The meaty kind."
                ]
                comment.reply(random.choice(chouta_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

#Spoiler
    for key in ["!>", "<!"]:
        if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
            spoiler_quotes = [
                    "Hey muli, that's a bad spoiler tag. You don't want to ruin the tale for others, do you?",
                    "That spoiler tag doesn't work! Fix it fast!",
                    "Gon, I love you and all, but wrong spoiler tags are not very nice. Only storming lighteyes ruin books for others, so correct it!"
                ]
                comment.reply(random.choice(spoiler_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

    if comment.id not in comments_replied_to2 and not comment.author == r.user.me():
        comments_replied_to2.append(comment.id) #Adds skimmed comments to list

    print("Sleeping for a bit")
    time.sleep(120)  #Two minute cool-down period

#Function to save comments replied to
def get_saved_comments():

    if not os.path.isfile("comments_replied_to2.txt"):

        comments_replied_to2 = []

    else:

        with open("comments_replied_to2.txt", "r", encoding='cp1252') as f:
            comments_replied_to2 = f.read()
            comments_replied_to2 = comments_replied_to2.split("\n")

    return comments_replied_to2

#Splits comment replied to into whole words
def WholeWord(w):

    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

#Running the functions
r = bot_login()
comments_replied_to2 = get_saved_comments()


while True:
    run_bot(r, comments_replied_to2, WholeWord)
