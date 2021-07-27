#!/usr/bin/python

import praw
from config_lopen import *
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
    for post in r.subreddit('cremposting').hot(limit = 5):
        post_num = random.randint(1, 3)
        if post.id not in comments_replied_to2 and post_num == 1:
            post_quotes = [
                "This crem is accepted, Gancho!",
                "Great meme, Gon!",
                "Did you hear about the one-armed Herdazian who posted on r/cremposting? The crem was dis-arming!",
                "This crem deserves some chouta!"]

            post.reply(random.choice(post_quotes)) #Chooses a random quote from above list
            print("Post found!")

            comments_replied_to2.append(post.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

        if post.id not in comments_replied_to2:
            comments_replied_to2.append(post.id)


    for comment in r.subreddit('cremposting').comments(limit = 25):
        comment.refresh()

        #Randomness to make sure Lopen doesn't reply to every comment with these words

        pancake_num = random.randint(1, 4)
        gancho_num = random.randint(1, 3)


#Spoiler
        for key in ["!>", "<!", ">! ", " !<"]:
            if key in comment.body and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                spoiler_quotes = [
                        f"Hey muli, that's a bad spoiler tag. You don't want to ruin the tale for others, do you?",
                        f"That spoiler tag doesn't work! Fix it fast!",
                        f"Gon, I love you and all, but wrong spoiler tags are not very nice. Only storming lighteyes ruin books for others, so correct it!"
                    ]

                if key in ["!>", "<!"]:
                    extra = f" You have used {key} by mistake, which is wrong. Use \>!(Text here)\!< instead for correct spoiler tags!"
                else:
                    extra = f" There is a space between your spoiler tag and text! Remove it to fix the spoiler!"

                comment.reply(random.choice(spoiler_quotes) + extra) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

        for key in [">!", "!<"]:
            if key in comment.body and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                if key == ">!":
                    thing = "!<"
                else:
                    thing = ">!"

                if comment.body.count(key) == comment.body.count(thing):
                    pass
                else:
                    if comment.body.count(key) > comment.body.count(thing):
                        tag = thing
                    else:
                        tag = key
                    comment.reply(f"You are missing at least one {tag} in that comment! Fix it so others don't get spoiled!")

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

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

    #Lopen insult
        for key in ["insult", "insults"]:
            if WholeWord(key)(comment.body) and (WholeWord("lopen")(comment.body) or WholeWord("gancho")(comment.body)) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                insult_quotes = [
                        "Behold the Lopen gesture!",
                        "***Makes the Lopen gesture***",
                        "***Makes the double Lopen gesture towards you***",
                        "My other hand?' Lopen said. 'The one that was cut off long ago, eaten by a fearsome beast? It is making a rude gesture toward you right now. I thought you would want to know, so you can prepare to be insulted.",
                        "A one-armed Herdazian is still twice as useful as a no-brained Alethi.",
                        "Hey, Gancho, you're not the dumbest person on the planet, but you sure better hope he doesn't die.",
                        "Muli, you have more crem in you then a Highstorm's leavings!",
                        "Wow, Gancho, you are dumber than a bridge of wood and not nearly as useful!",
                        "If your brain exploded, it wouldn't even mess up your hair!",
                        "Hey, penhito, I think the Stormfather is jealous of the amount of crem you just typed out!",
                        "May your armpits be infested with the dung of a thousand chulls!",
                        "Gancho, I have more arms than you have brains.",
                        "People like you are the reason Honor is dead.",
                        "Penhito, your words are so stupid even"
                        ]
                success_quotes = [
                    "Hey, Gancho, I have insulted the guy who spited you! You may thank me now!",
                    "The insult has been deployed. That Wit fellow would have applauded me for my Wittiness, I think!",
                    "I think I made the fellow cry, Gon. He shouldn't trouble you again, and if he does, you can call me again!"
                    ]
                fail_quotes = [
                    "Sorry, Gancho, but I have already replied to that comment. Can't do that again.",
                    "I already spoke to that guy, and I don't think they need to be insulted.",
                    "The insult has failed. If you want, you can have some chouta!",
                    "Hey, gon, that's rude! Listen to a Lopen joke, instead!"
                    ]
                parent = comment.parent()

                if parent.id not in comments_replied_to2:
                    extra = f"\n\n ^(This insult was requested by {comment.author})"
                    parent.reply(random.choice(insult_quotes) + extra) #Chooses a random quote from above list
                    comments_replied_to2.append(parent.id)
                    print("Comment insulted!")

                    comment.reply(random.choice(success_quotes)) #Chooses a random quote from above list

                else:
                    #comment.reply(random.choice(fail_quotes)) #Chooses a random quote from above list
                    pass

                comments_replied_to2.append(comment.id)

    #What are your thoughts
        for key in [
            "what do you think",
            "what are your thoughts",
            "what do you think about this",
            "what do you think about it"]:
            if key in comment.body and (WholeWord("lopen")(comment.body) or WholeWord("gancho")(comment.body)) and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and len(comment.body) < 50:
                thoughts_quotes = [
                    "Seems alright, gancho. Why do you ask?",
                    "**The Lopen gesture**",
                    "I don't like it, gon. Too little chouta.",
                    "Great, gon!",
                    "This has the approval of the King of Alethkar!"]

                comment.reply(random.choice(lopen_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

                print("Comment found!")


    #gancho
        for key in ["gancho", "muli", "gon", "penhito", r.user.me(), "the lopen"]:
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
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
                    "***Makes the Lopen gesture***",
                    "***Makes the double Lopen gesture towards the sky***",
                    "My other hand?' Lopen said. 'The one that was cut off long ago, eaten by a fearsome beast? It is making a rude gesture toward you right now. I thought you would want to know, so you can prepare to be insulted.",
                    "It is said that you shouldn't bet against a one-armed Herdazian in a drinking contest!",
                    "[OB spoilers] >!Drehy likes other guys. That's like … he wants to be even less around women than the rest of us. It's the opposite of feminine. He is you could say extra manly.!<",
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

    #Curses
        for key in (dict := {
            "fuck" : "storms",
            "fucking" : "storming",
            "damn" : "Damnation",
            "bloody" : "storming",
            "shit" : "crem",
            "bullshit" : "chull dung",
            "depression" : "Kaladin",
            "depressed" : "Kaladin",
            "cum" : "stormblessings",
            "crap" : "crem",
            "bitch" : "axehound",
            "fucker" : "penhito",
            "dear god" : "Almighty",
            "hell" : "Damnation",
            "heck" : "Damnation",
            "asshole" : "chull dung",
            "dammit" : "storm it",
            "dick" : "safehand"}):
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                curse_quotes = [
                    f"Hey, gon, instead of using {key}, why not use {dict[key]}?",
                    f"Gancho, don't you think {dict[key]} is a better word than {key}?",
                    f"I would rather you use {dict[key]} than use that foreign word, {key}, gancho."
                ]
                curse_num = random.randint(1, 3)
                if curse_num == 2:
                    comment.reply(random.choice(curse_quotes)) #Chooses a random quote from above list
                else:
                    pass

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")



    #pancakes
        for key in ["journey before destination"]:
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
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
        for key in ["good", "happy", "awesome", "nice", "happiness", "cool", "fantastic", "sweet",
        "noice", "brilliant", "joy", "awesomeness", "wow", "happily", "great", "nicely", "sweetly",
        "joyous", "greatly", "whoop"]:
            if WholeWord(key)(comment.body) and (WholeWord("lopen")(comment.body) or WholeWord("gancho")(comment.body)) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                happy_quotes = [
                    f"{key.capitalise()} is good! For more awesomeness, just ask for \"Lopen Joke\", and I'll give some to you!"
                ]
                comment.reply(random.choice(happy_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

    #sad
        for key in ["sad", "depress", "depressed", "trauma", "depression", "not happy", "hurt", "ache",
        "heartache", "sadly", "unfortunate", "unfortunately", "down", "traumatic"]:
            if WholeWord(key)(comment.body) and WholeWord("lopen")(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                sad_quotes = [
                    f"Hey gancho, you used '{key}' in your comment. If you're sad, want to hear a joke? Just type \"The Lopen Joke\", and I'll give one to you!",
                    f"Gon, you good? I detected '{key}' in your comment."
                ]
                comment.reply(random.choice(sad_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

    #Correction
        for key in ["lopen", "Lopen"]:
            if key in comment.body  and not "The Lopen" in comment.body and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and gancho_num == 2:
                correction_quotes = [
                    "That would be *The Lopen* for you, muli!",
                    f"How dare you disrespect The Lopen, King of Alethkar, by merely calling him '{key}'?",
                    f"{key}? Just {key}? Here, I am giving you the Lopen gesture!"
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
                    "You can never have enough cousins, gon!",
                    "A man can never have enough cousins!",
                    "My cousin's never failed me.",
                    "You bother one of us, you bother us all!"
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

    #chouta
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

    #Rua
        for key in ["rua"]:
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                rua_quotes = [
                    "***Lopen Gesture***"
                ]
                comment.reply(random.choice(rua_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


                print("Comment found!")

        if comment.id not in comments_replied_to2 and not comment.author == r.user.me():
            comments_replied_to2.append(comment.id) #Adds skimmed comments to list

    print("Sleeping for a bit")
    time.sleep(60)  #Cool-down period

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
    try:
        run_bot(r, comments_replied_to2, WholeWord)
    except:
        print("Error")
        time.sleep(120)

