#!/usr/bin/python

import praw
from config_lopen import *
import os
import random
import time
import re
import requests
from bs4 import BeautifulSoup, Comment
from quotes import *


#Bot login
def bot_login():
    r = praw.Reddit(username = userN,
                    password = userP,
                    client_secret = cSC,
                    client_id = cID,
                    user_agent = userAgent)
    return r
    print("Logged in")
#    print(r.user.me())

def run_bot(r, comments_replied_to2, posts_replied_to, comments_skimmed, WholeWord, rank):
    for post in r.subreddit('Cremposting').hot(limit = 5):
        post_num = random.randint(1, 3)
        if post.id not in posts_replied_to and post_num == 1:
            mess = random.choice(["\n\n^(These words of Stormfather's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Stormfather, brought by Lopen's cousins)",
                "\n\n^(Speak further to Stormfather by mentioning !Stormfather in your comments. Anytime, anywhere. LMS)"])

            list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

            post_quotes = [
                "This crem is accepted!".upper() + mess + list_of,
                "Great meme, Gon!",
                "This crem deserves some chouta!"]

            post.reply(random.choice(post_quotes)) #Chooses a random quote from above list
            print("Post found!")

            posts_replied_to.append(post.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
            with open("posts_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(post.id + "\n")

        if post.id not in posts_replied_to:
            posts_replied_to.append(post.id)
            with open("posts_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(post.id + "\n")


    #Stormlight Archive
    redditor = r.redditor("Anacanrock11")

    u_comment = r.redditor("Anacanrock11").comments.new(limit=1)

    for user_comment in u_comment:
        if "previous" in user_comment.body.lower() and user_comment.id not in comments_skimmed:

            posts = {}
            for post in redditor.submissions.new(limit = 1000):
                if "memeing every chapter" in post.title.lower() or "meming every chapter" in post.title.lower():
                    posts[post.title] = post.shortlink

            sa_posts = "The list of chapters posted till now are:\n\n"
            for item in posts.items():

                sa_posts += f"* [{item[0]}]({item[1]}) \n\n"

            sa_posts += "* [Meming every chapter of Stormlight Archive till I get bored, part 3](https://redd.it/o3apw6)\n\n"
            sa_posts += "* [Meming every chapter of Stormlight Archive till I get bored, part 2](https://redd.it/o3amnl)\n\n"
            sa_posts += "* [Meming every chapter of Stormlight Archive till I get bored, part 1](https://redd.it/o2mbn2)\n\n"

            redditor = r.redditor("The_Lopen_bot")

            for post in redditor.submissions.new(limit = 5):
                if "Meming every chapter list - Stormlight Archive" in post.title:
                    post.edit(sa_posts)

            comments_skimmed.append(user_comment.id)  #Simply adds the user_comment.id replied to to a list so the bot doesn't reply to it again

            with open("comments_skimmed.txt", "a", encoding='cp1252') as f:
                f.write(user_comment.id + "\n")

    #Mistborn
    redditor = r.redditor("JeffSheldrake")

    u_comment = r.redditor("JeffSheldrake").comments.new(limit=1)

    for user_comment in u_comment:
        if "index" in user_comment.body.lower() and user_comment.id not in comments_skimmed:

            posts = {}
            for post in redditor.submissions.new(limit = 1000):
                if "memeing every chapter" in post.title.lower() or "meming every chapter" in post.title.lower():
                    posts[post.title] = post.shortlink

            mb_posts = "The list of chapters posted till now are:\n\n"
            for item in posts.items():

                mb_posts += f"* [{item[0]}]({item[1]}) \n\n"

            redditor = r.redditor("The_Lopen_bot")

            for post in redditor.submissions.new(limit = 5):
                if "Meming every chapter list - Mistborn" in post.title:
                    post.edit(mb_posts)

            comments_skimmed.append(user_comment.id)  #Simply adds the user_comment.id replied to to a list so the bot doesn't reply to it again

            with open("comments_skimmed.txt", "a", encoding='cp1252') as f:
                f.write(user_comment.id + "\n")

    #Elantris
    redditor = r.redditor("SpaghettiMaestro14")

    u_comment = r.redditor("SpaghettiMaestro14").comments.new(limit=1)

    for user_comment in u_comment:
        if "previous" in user_comment.body.lower() and user_comment.id not in comments_skimmed:

            posts = {}
            for post in redditor.submissions.new(limit = 1000):
                if "memeing every chapter" in post.title.lower() or "meming every chapter" in post.title.lower():
                    posts[post.title] = post.shortlink

            el_posts = "The list of chapters posted till now are:\n\n"
            for item in posts.items():

                el_posts += f"* [{item[0]}]({item[1]}) \n\n"

            redditor = r.redditor("The_Lopen_bot")

            for post in redditor.submissions.new(limit = 5):
                if "Meming every chapter list - Elantris" in post.title:
                    post.edit(el_posts)

            comments_skimmed.append(user_comment.id)  #Simply adds the user_comment.id replied to to a list so the bot doesn't reply to it again

            with open("comments_skimmed.txt", "a", encoding='cp1252') as f:
                f.write(user_comment.id + "\n")

    #Warbreaker
    redditor = r.redditor("AlThorStormblessed")

    u_comment = r.redditor("AlThorStormblessed").comments.new(limit=1)

    for user_comment in u_comment:
        if "previous" in user_comment.body.lower() and user_comment.id not in comments_skimmed:

            posts = {}
            for post in redditor.submissions.new(limit = 1000):
                if "memeing every chapter" in post.title.lower() or "meming every chapter" in post.title.lower() and "Wheel of Time" not in post.title:
                    posts[post.title] = post.shortlink

            wb_posts = "The list of chapters posted till now are (Some redos and alternate, coz my Creator is an idiot):\n\n"
            for item in posts.items():

                wb_posts += f"* [{item[0]}]({item[1]}) \n\n"

            redditor = r.redditor("The_Lopen_bot")

            for post in redditor.submissions.new(limit = 5):
                if "Meming every chapter list - Warbreaker" in post.title:
                    post.edit(wb_posts)

            comments_skimmed.append(user_comment.id)  #Simply adds the user_comment.id replied to to a list so the bot doesn't reply to it again

            with open("comments_skimmed.txt", "a", encoding='cp1252') as f:
                f.write(user_comment.id + "\n")


    #Main code
    for comment in r.subreddit('Cremposting').comments(limit = 100):
        comment.refresh()
        #Randomness to make sure Lopen doesn't reply to every comment with these words

        pancake_num = random.randint(1, 4)
        gancho_num = random.randint(1, 3)
        x_com = comment
        y_com = comment

        if comment.author not in ["b0trank"]:

    #Spoiler
            for key in ["!>", "<!", ">! "]:
                if key in comment.body and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                    spoiler_quotes = [
                            f"Hey moolie, that's a bad spoiler tag. You don't want to ruin the tale for others, do you?",
                            f"That spoiler tag doesn't work! Fix it fast!",
                            f"Gon, I love you and all, but wrong spoiler tags are not very nice. Only storming lighteyes ruin books for others, so correct it!"
                        ]

                    if key in ["!>", "<!"]:
                        extra = f" You have used {key} by mistake, which is wrong. Use \>!(Text here)\!< instead for correct spoiler tags!"
                    elif "\\>!" not in comment.body and "\\!<" not in comment.body:
                        extra = f" There is a space between your spoiler tag and text! Remove it to fix the spoiler!"

                    comment.reply(random.choice(spoiler_quotes) + extra) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Untagged spoiler found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

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
                        print("Spoiler untagged found!")

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")


    #Coppermind function
            if "!coppermind" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                text = comment.body
                text = text.split("!coppermind")[-1]
                text = text.split()

                try:
                    try:
                        n = int(text[-1])
                        search = "_".join(text[:-1])

                    except:
                        n = 5
                        search = text[0]

                    punc = '''!()-[]{};:'"\,<>./?@#$%^&*~'''

                    for ele in search:
                        if ele in punc:
                            search = search.replace(ele, "")

                    if n > 5:
                        n = 5

                    doc= f'https://coppermind.net/wiki/{search}'
                    res = requests.get(doc)
                    soup = BeautifulSoup(res.content, "html.parser")
                    rows =soup.find('div',attrs={"class" : "mw-parser-output"})

                    try:
                        if "disambiguation" in text[0]:
                            comment.reply(f'{search} may refer to multiple pages.\n\n\
Visit {doc} to find what you want.')
                            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                            print("Coppermind tapper found!")

                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                        else:
                            text_list = []
                            for p in rows.find_all('p'):
                                text_list.append(p.get_text())
                                if not text_list[-1]:
                                    del text_list[-1]

                            text = "***Warning Gancho: The below paragraph(s) may contain major spoilers for all books in the Cosmere!***\n\n" + "\n\n".join([f">!{x}!<".replace("\n", "").strip() for x in text_list[:n+1]]) + f"\n\n^[The article can be viewed here!]({doc})"

                            comment.reply(text)
                            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                            print("Coppermind tapper found!")

                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")
                    except:
                        comment.reply(f"The article {search} does not seem to exist. Check if you have made a spelling mistake, or if there is another name that might work.")
                        comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                        print("Coppermind tapper found!")

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                except:
                    comment.reply(f"Gon, u/AlThorStormblessed must have missed something in the code, or your keywords are off, because I couldn't find anything. [How about you take a quick look around Coppermind yourself?](https://coppermind.net/wiki/Coppermind:Welcome)")
                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Coppermind tapper found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")


    #Lopen messaging service
            LMS = []
            for key in [
                "!kaladin", "!shallan", "!adolin", "!stormfather", "!stormdaddy", "!taln", "!syl", "!pattern",
                "!stick", "!dalinar", "!dadinar", "!rock", "!numuhukumakiaki'aialunamor", "!jasnah"
            ]:
                if key in comment.body.lower() and ('>' + key) not in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                    LMS.append(key)

            if LMS:
                lms_key = random.choice(LMS)


                if lms_key == "!kaladin":

                    mess = random.choice(["\n\n^(These words of Kaladin's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Kaladin, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Kaladin by mentioning !Kaladin in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(kaladin_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                elif lms_key == "!shallan":


                    mess = random.choice(["\n\n^(These words of Shallan's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Shallan, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Shallan by mentioning !Shallan in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(shallan_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                elif lms_key == "!adolin":


                    mess = random.choice(["\n\n^(These words of Adolin's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Adolin, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Adolin by mentioning !Adolin in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(adolin_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                elif lms_key == "!stormfather" or lms_key == "!stormdaddy":

                    mess = random.choice(["\n\n^(These words of Stormfather's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Stormfather, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Stormfather by mentioning !Stormfather in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(stormfather_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                elif lms_key == "!taln":


                    mess = random.choice(["\n\n^(These words of Taln's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Taln, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Taln by mentioning !Taln in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(taln_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                elif lms_key == "!syl":

                    mess = random.choice(["\n\n^(These words of Syl's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Syl, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Syl by mentioning !Syl in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(syl_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                elif lms_key == "!pattern":

                    mess = random.choice(["\n\n^(These words of Pattern's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Pattern, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Pattern by mentioning !Pattern in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(pattern_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                elif lms_key == "!dalinar" or lms_key == "!dadinar":

                    mess = random.choice(["\n\n^(These words of Dalinar's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Dalinar, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Dalinar by mentioning !Dalinar in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(dalinar_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                elif lms_key == "!stick":
                    stick_quotes = [
                        "I am a stick."
                     ]

                    mess = random.choice(["\n\n^(These words of Stick's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Stick, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Stick by mentioning !Stick in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(stick_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                elif lms_key == "!rock" or lms_key == "!numuhukumakiaki'aialunamor":

                    mess = random.choice(["\n\n^(These words of Rock's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Rock, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Rock by mentioning !Rock in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(rock_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    print("Comment found!")

                elif lms_key == "!jasnah":

                    mess = random.choice(["\n\n^(These words of Jasnah's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Jasnah, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Jasnah by mentioning !Jasnah in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(jasnah_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")


            if "!list" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                list_of = "Hey, Gancho, these are the people whom you can communicate with through the Lopen Messaging Service as of now!\n\
\n\
* Kaladin\n\
\n\
* Shallan\n\
\n\
* Adolin\n\
\n\
* Stormfather/Stormdaddy (coz why not?)\n\
\n\
* Taln\n\
\n\
* Syl\n\
\n\
* Pattern\n\
\n\
* Dalinar/Dadinar\n\
\n\
* Stick\n\
\n\
* Rock/Numuhukumakiaki'aialunamor\n\
\n\
* Jasnah (no, she isn't going to crush you with her thighs)\n\
\n\
* Wit (summoned as either ! Wit (quote to commentor) or ! Wit [...] insult (insult parent commentor)"

                comment.reply(list_of)

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

            if "!function" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                comment.reply(functions)

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")


        #Witty stuff
            if "!wit" in comment.body.lower() and ">!wit" not in comment.body.lower() and comment.id not in comments_replied_to2:
                #Quotes
                if not WholeWord("insult")(comment.body) and comment.author != r.user.me():

                    mess = random.choice(["\n\n^(These words of Wit's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                        "\n\n^(-Wit, brought by Lopen's cousins)",
                        "\n\n^(Speak further to Wit by mentioning ! Wit in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(wit_quotes) + mess + list_of) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment found!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                else:
                    if WholeWord("lopen")(comment.body):
                        insult_num = random.randint(1, 2)

                    else:
                        insult_num = 1

                    if insult_num == 1:
                        post = True
                        for item in r.user.me().saved(limit = None):
                            if f"Devotee {comment.parent().author}" in item.body:
                                if rank('present', comment.parent().author) != "Heretic":
                                    post = False

                                    Vorin = [
                                        "You dare try to insult a child of the Almighty? Shame!",
                                        "This cr*mposter is protected by the Great Vorin Church. You may not insult them!",
                                        f"Do you not recognise {rank('present', comment.parent().author)} {comment.parent().author}? You shall insult them?"
                                    ]

                                    comment.reply(random.choice(Vorin)) #Chooses a random quote from above list

                                    comments_replied_to2.append(comment.id)
                                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                        f.write(comment.id + "\n")

                        if post:
                            x_com = comment
                            parent = x_com
                            fail_or_insult = random.randint(1, 5)

                            mess = random.choice(["\n\n^(These words of Wit's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                                "\n\n^(-Wit, brought by Lopen's cousins)",
                                "\n\n^(Speak further to Wit by mentioning ! Wit in your comments. Anytime, anywhere. LMS)"])

                            list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                            if fail_or_insult == 1:
                                comment.reply(random.choice(wit_fail) + "\n\n" + random.choice(wit_insult) + mess + list_of)

                            else:
                                if parent.id not in comments_replied_to2:
                                    parent.reply(random.choice(wit_insult).replace(parent.author, comment.parent().author) + mess + list_of) #Chooses a random quote from above list
                                    comments_replied_to2.append(parent.id)
                                    print("Comment insulted!")

                                else:
                                    comment.reply(random.choice(wit_fail_2) + mess + list_of) #Chooses a random quote from above list
                                    pass

                            comments_replied_to2.append(comment.id)

                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

        #Vorin Church
            if "!join" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                post = True
                heretic = False
                print(rank("present", comment.author))
                for item in r.user.me().saved(limit = None):
                    if f"Heretic {comment.author}" in item.body and comment.id not in comments_replied_to2:
                        heretic = True
                        if rank("present", comment.author) == "Heretic":
                            comment.reply(f"Heretic {comment.author} must *not* be allowed into the Holy Vorin Church!")
                            comments_replied_to2.append(comment.id)

                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            print("Heretic found!")

                            post = False

                            break
                        elif comment.id not in comments_replied_to2:
                            comment.reply(f"Your Herecy has been forgiven!\n\n\
Devotee {comment.author} has joined the Great Vorin Church! Your rank, according to your history, has been assigned as {rank('present', comment.author)}!\n\n\
^(We have a strict set of guidelines, which, if not followed, will lead to permanent excommunication from the Vorin Church. Type !guide to read the rules!)\n\n\
^(To find the many different niceties the Vorin Church beings, type out !pros in your comments. We have many nice features!)")
                            comments_replied_to2.append(comment.id)

                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            next(r.redditor("The_Lopen_bot").comments.new(limit=1)).save()

                            print("New member saved")
                            post = False

                            break

                for item in r.user.me().saved(limit = None):
                    if f"Devotee {comment.author}" in item.body and not heretic and comment.id not in comments_replied_to2:
                        comment.reply(f"{rank('present', comment.author)} {comment.author} has already been inducted into the Holy Vorin Church!")
                        comments_replied_to2.append(comment.id)
                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                        print("Devotee found!")

                        post = False
                        break


                if post and comment.id not in comments_replied_to2:
                    if rank('present', comment.author) != "Heretic":
                        comment.reply(f"Devotee {comment.author} has joined the Great Vorin Church! Your rank, according to your history, has been assigned as {rank('present', comment.author)}!\n\n\
^(We have a strict set of guidelines, which, if not followed, will lead to permanent excommunication from the Vorin Church. Type !guide to read the rules!)\n\n\
^(To find the many different niceties the Vorin Church beings, type out !pros in your comments. We have many nice features!)")
                        comments_replied_to2.append(comment.id)

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                        next(r.redditor("The_Lopen_bot").comments.new(limit=1)).save()

                        print("New member saved")

                    elif comment.id not in comments_replied_to2:
                        comment.reply(f"Heretic {comment.author} must *not* be allowed into the Holy Vorin Church!")
                        comments_replied_to2.append(comment.id)

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                        print("Heretic found!")

                        break

            for key in ["storms", "safehand", "femboy", "rusts", "rust and ruin", "merciful domi", "syladin",
                        "storming", "shat", "ashes", "starvin", "ash's eyes", "airsick", "nale's nut", "taln's stones",
                        "by the survivor", "kelek's breath", "god beyond", "chull dung", "crem", "colors", "almighty is dead"]:
                if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and comment.id not in comments_skimmed and not comment.author == r.user.me():
                    for item in r.user.me().saved(limit = None):
                        if f"Devotee {comment.author}" in item.body and comment.id not in comments_replied_to2:
                            if rank('past', comment.author) != "Heretic":
                                if rank('present', comment.author) != rank('past', comment.author) and rank('present', comment.author) != "Heretic":
                                    comment.reply(f"Due to recent activities, your Vorin rank has changed to **{rank('present', comment.author)} from {rank('past', comment.author)}**")
                                    comments_replied_to2.append(comment.id)
                                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                        f.write(comment.id + "\n")

                                    print("Heretic found!")
                                elif rank('present', comment.author) == "Heretic":
                                    comment.reply(f"Due to recent activities, you have been ***excommunicated*** from the Great Vorin Church. Never show your heretic face here again!")
                                    comments_replied_to2.append(comment.id)
                                    next(r.redditor("The_Lopen_bot").comments.new(limit=1)).save()
                                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                        f.write(comment.id + "\n")

                                    print("Heretic found!")


                                break

            for key in ["almighty", "herald", "vorin"]:
                if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and comment.id not in comments_skimmed and not comment.author == r.user.me():
                    for item in r.user.me().saved(limit = None):
                        if f"Devotee {comment.author}" in item.body:
                            if rank('past', comment.author) != "Heretic":
                                if rank('present', comment.author) != rank('past', comment.author) and rank('present', comment.author) != "Heretic":
                                    comment.reply(f"Due to recent activities, your Vorin rank has changed to **{rank('present', comment.author)} from {rank('past', comment.author)}**")
                                    comments_replied_to2.append(comment.id)
                                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                        f.write(comment.id + "\n")
                                elif rank('present', comment.author) == "Heretic":
                                    comment.reply(f"Due to recent activities, you have been ***excommunicated*** from the Great Vorin Church. Never show your heretic face here again!")
                                    comments_replied_to2.append(comment.id)
                                    next(r.redditor("The_Lopen_bot").comments.new(limit=1)).save()
                                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                        f.write(comment.id + "\n")

                                print("Vorin found!")
                                break

            if "!hail" in comment.body.lower() and comment.id not in comments_replied_to2 and comment.id not in comments_skimmed and not comment.author == r.user.me():
                    for item in r.user.me().saved(limit = None):
                        if f"Devotee {comment.author}" in item.body:
                            if rank('past', comment.author) != "Heretic" and comment.id not in comments_replied_to2 and comment.id not in comments_skimmed:
                                if rank('present', comment.author) in ["Holy Emperor", "Herald"]:
                                    comment.reply(f"All hail the glory of the Almighty, the {rank('present', comment.author)} of Stormlight, {comment.author}!")
                                    comments_replied_to2.append(comment.id)
                                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                        f.write(comment.id + "\n")

                                else:
                                    comment.reply("Who are you again??")
                                    comments_replied_to2.append(comment.id)
                                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                        f.write(comment.id + "\n")

                                print("Herald hailed!")
                                break

            if "!guide" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                for item in r.user.me().saved(limit = None):
                    if f"Devotee {comment.author}" in item.body:
                        if rank('past', comment.author) != "Heretic":
                            comment.reply(f"Ah, {rank('present', comment.author)} {comment.author}. You wish to seek our guidelines! Here they are:\n\n\
1. The Great Vorin Church does not permit the use of any swear words, except the name of the Almighty and the Great Heralds. Swearing shall result in reduction in rating and possible reduction in rank, even excommunication.\n\n\
2. Any defiling of Herald names, as and when we detect it, shall result in excommunication.\n\n\
3. No man shall dare read or write on this subreddit. Only through female scribes or ardents shall written word be transmitted (we are working on figuring out how to catch such heretics.)\n\n\
4. Censor the name of J\*snah Kh\*lin, or use a title. Such heretics must not be tolerated. This will result in reduction in rating and possible reduction in rank, even excommunication..\n\n\
5. For more information about ranking, type !rank.")
                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            print("Guidelines!")
                            break

            for key in ["!cat", "!dog", "!cow", "!crab"]:
                if key in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                    for item in r.user.me().saved(limit = None):
                        if f"Devotee {comment.author}" in item.body:
                            if rank('past', comment.author) != "Heretic":
                                if (rank('present', comment.author) in ["Brightness", "High-noble", "Holy Emperor", "Herald"] and len(comment.body.split()) != 2) or rank('present', comment.author) == "Lighteyes":
                                    if key == "!cat":
                                        animal_image = random.choice(cat)
                                    elif key == "!dog":
                                        animal_image = random.choice(dog)
                                    elif key == "!cow":
                                        animal_image = random.choice(cow)
                                    elif key == "!crab":
                                        animal_image = random.choice(crab)
                                    intro = random.choice(intro_list)
                                    comment.reply(f"[{intro}]({animal_image})")

                                elif rank('present', comment.author) in ["Brightness", "High-noble", "Holy Emperor", "Herald"] and len(comment.body.split()) == 2:
                                    author = comment.body.split()[1]
                                    comment = y_com
                                    print(author)
                                    try:
                                        for comment_other in r.redditor(author).comments.new(limit = None):
                                            if author.lower() != "mistborn" and comment_other.subreddit.display_name.lower() == "cremposting" and comment_other.id not in comments_replied_to2:
                                                if key == "!cat":
                                                    animal_image = random.choice(cat)
                                                elif key == "!dog":
                                                    animal_image = random.choice(dog)
                                                elif key == "!cow":
                                                    animal_image = random.choice(cow)

                                                elif key == "!crab":
                                                    animal_image = random.choice(crab)

                                                intro = random.choice(intro_list_2)
                                                comment_other.reply(f"[{intro}]({animal_image})")
                                                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                                    f.write(comment_other.id + "\n")
                                                comment.reply("The image has been sent!")
                                                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                                    f.write(comment.id + "\n")
                                                break
                                            elif author.lower() == "mistborn":
                                                comment.reply(f"We daren't disturb the Almighty, {comment.author}, even for cute images like such.")
                                                break
                                        else:
                                            if comment.id not in comments_replied_to2:
                                                comment.reply("No recent eligible comment found (change in rank criteria). Try someone else instead, or wait for them to make a new comment.")
                                    except:
                                        comment.reply("Image delivery has failed, O Bright One.")

                                else:
                                    comment.reply("You are too lowly ranked to use this function. Be a good Vorin, follow the guidelines and praise the Almighty and the Heralds, and perhaps we will grant you this power!")

                                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                    f.write(comment.id + "\n")

                                print("Cute image sent!")
                                break

                            else:
                                comment.reply("You are a Heretic! No priveleges for you, unless you repent!")

                                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                    f.write(comment.id + "\n")

                                print("Heretic found!")
                                break

            if "!rickroll" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                for item in r.user.me().saved(limit = None):
                    if f"Devotee {comment.author}" in item.body:
                        if rank('past', comment.author) != "Heretic":
                            if (rank('present', comment.author) in ["High-noble", "Holy Emperor", "Herald"] and len(comment.body.split()) != 2):
                                comment.reply("O Bright One, you need to type just '!rickroll [username]' without the u/. Anything else will just confuse us.")
                                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                    f.write(comment.id + "\n")

                            elif rank('present', comment.author) in ["High-noble", "Holy Emperor", "Herald"] and len(comment.body.split()) == 2:
                                author = comment.body.split()[1]
                                comment = y_com
                                try:
                                    for comment_other in r.redditor(author).comments.new(limit = None):
                                        if author.lower() != "mistborn" and comment_other.subreddit.display_name.lower() == "cremposting" and comment_other.id not in comments_replied_to2:

                                            link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

                                            intro = random.choice(intro_list_2)

                                            comment_other.reply(f"[{intro}]({link})")
                                            comments_replied_to2.append(comment_other)
                                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                                f.write(comment_other.id + "\n")
                                            comment.reply("The 'image' has been sent!")
                                            comments_replied_to2.append(comment)
                                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                                f.write(comment.id + "\n")
                                            break
                                        elif author.lower() == "mistborn":
                                            comment.reply(f"You really want to rickroll Brandon Sanderson? The Almighty shall not be disturbed!")

                                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                                f.write(comment.id + "\n")

                                            break
                                    else:
                                        if comment.id not in comments_replied_to2:
                                            comment.reply("No recent eligible comment found. Try someone else instead, or wait for them to make a new comment.")
                                except:
                                    comment.reply("Function has failed, O Bright One.")

                            elif comment.id not in comments_replied_to2:
                                comment.reply("You are too lowly ranked to use this function (change in rank criteria). Be a good Vorin, follow the guidelines and praise the Almighty and the Heralds, and perhaps we will grant you this power!")

                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            print("Rickroll sent!")
                            break

                        else:
                            comment.reply("You are a Heretic! No priveleges for you, unless you repent!")

                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            print("Heretic found!")
                            break


            if "!rank" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                for item in r.user.me().saved(limit = None):
                    if f"Devotee {comment.author}" in item.body:
                        if rank('past', comment.author) != "Heretic":
                            comment.reply(f"The Vorin ranking system is very complex. Devotees gain higher ranks by being good Vorins, and fall in rankings by breaking guidelines. Steep falls can result in excommunication, at least till such behavious is rectified, in which case they may re-join.\n\n\
Your rank for now is ***{rank('present', comment.author)}*** (change in rank criteria)\n\n\
The ranking is as follows:\n\n\
1. Herald: Everything Holy Emperors have\n\n\
2. Holy Emperor: Everything High-nobles have, ability to !hail themselves for all to recognise.\n\n\
3. High-noble: Everything the Bright-lords and -ladies have, ability to send insults to anyone of properly low rank, ability to !rickroll anyone on the sub.\n\n\
4. Brightness: Everything the lower Lighteyes have, protection from all insults, including Vorin insults, ability to send below images to anyone.\n\n\
5. Lighteyes: Everything the Darkborn have, ability to summon !dog, !cat, !crab, and !cow images, for the days you are worse for wear.\n\n\
6. Darkborn: Protected from Lopen and Wit insults, gain access to !Vorin insults and !Vorin compliments\n\n\
7. Heretics: removed from the Church, no priveleges.\n\n\
Powers may not have been unlocked yet, if something doesn't work as expected, please bear patience.")

                            comments_replied_to2.append(comment.id)
                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            print("Guidelines!")
                            break

                        else:
                            comment.reply(f"You are a st*rming heretic!")
                            comments_replied_to2.append(comment.id)
                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")
                            break

            if WholeWord("jasnah")(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                for item in r.user.me().saved(limit = None):
                    if f"Devotee {comment.author}" in item.body:
                        if rank('past', comment.author) != "Heretic" and comment.id not in comments_replied_to2:
                            if rank('present', comment.author) != rank('past', comment.author) and rank('present', comment.author) != "Heretic":
                                comment.reply(f"Due to recent activities (change in rank criteria), your Vorin rank has changed to **{rank('present', comment.author)} from {rank('past', comment.author)}**")
                                comments_replied_to2.append(comment.id)
                                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                    f.write(comment.id + "\n")
                            elif rank('present', comment.author) == "Heretic":
                                comment.reply(f"Due to recent activities (change in rank criteria), you have been ***excommunicated*** from the Great Vorin Church. Never show your heretic face here again!")
                                comments_replied_to2.append(comment.id)
                                next(r.redditor("The_Lopen_bot").comments.new(limit=1)).save()
                                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                    f.write(comment.id + "\n")

                            print("Heretic found!")
                            break

            if "!pros" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                for item in r.user.me().saved(limit = None):
                    if f"Devotee {comment.author}" in item.body:
                        if rank("present", comment.author) != "Heretic":
                            comment.reply(f"Ah, {rank('present', comment.author)} (change in rank criteria) {comment.author}. The features of the Vorin Church are many! There they are:\n\n\
1. No one may insult you, neither the fool Wit, nor the one-armed Herdazian. You will be safe from insults from all but the Church itself.\n\n\
2. You have unlocked the Great Vorin Insult. Type !vorinsult to any heretic or Vorin, and we shall insult them with special, holy insults.\n\n\
3. You can gain or lose rank by praying by the Almighty's name, or by breaking the guidelines respectively. You can reach dizzying heights in the Vorin Church!\n\n\
4. Many new functions shall be granted as you rise in rank!")
                            comments_replied_to2.append(comment.id)
                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            print("Advantages!")
                            break


            if "!cons" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                for item in r.user.me().saved(limit = None):
                    if f"Devotee {comment.author}" in item.body:
                        if rank("present", comment.author) != "Heretic":
                            comment.reply(f"St*rm you. There are no st*rming cons to the Great Vorin Church, so stop asking.")
                            comments_replied_to2.append(comment.id)
                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            print("Advantages!")
                            break

            if ("!vorinsult" in comment.body.lower() or "!vorin insult" in comment.body.lower()) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                post = True
                for item in r.user.me().saved(limit = None):
                    if f"Devotee {comment.author}" in item.body:
                        if rank("present", comment.author) != "Heretic" and rank("present", comment.parent().author) not in ["Brightness", "High-noble", "Holy Emperor", "Herald"]:
                            post = False
                            parent = comment.parent()

                            if parent.id not in comments_replied_to2:
                                extra = f"\n\n ^(This insult was requested by Devotee {comment.author})"
                                parent.reply(random.choice(vorin_insult_quotes) + extra) #Chooses a random quote from above list
                                comments_replied_to2.append(parent.id)
                                print("Comment insulted!")

                                comment.reply(random.choice(vorin_success_quotes)) #Chooses a random quote from above list

                            else:
                                comment.reply(random.choice(vorin_fail_quotes)) #Chooses a random quote from above list

                            comments_replied_to2.append(comment.id)
                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")
                            break

                        elif rank("present", comment.author) != "Heretic":
                            high_quotes = [
                                f"{comment.parent().author} is too highly ranked for even us to insult. You can, however, compliment them.",
                                f"You dare try to insult {rank('present', comment.parent().author)} {comment.parent().author}?",
                                f"Pray, for the insult has not reached them!",
                                f"St*rm off, {comment.author}. We won't insult such a distinguished member of our Church."
                            ]

                            comment.reply(random.choice(high_quotes)) #Chooses a random quote from above list

                            comments_replied_to2.append(comment.id)
                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")
                            post = False
                            break

                if post and comment.id not in comments_replied_to2:
                    comment.reply("Only the members of the Great Vorin Church can use this feature. If you are not a heretic, type !join to be welcomed by us!")
                    comments_replied_to2.append(comment.id)
                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

            if "!vorin compliment" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                post = True
                for item in r.user.me().saved(limit = None):
                    if f"Devotee {comment.author}" in item.body:
                        if rank("present", comment.author) != "Heretic":
                            post = False

                            parent = comment.parent()

                            if parent.id not in comments_replied_to2:
                                extra = f"\n\n ^(This compliment was requested by Devotee {comment.author})"
                                parent.reply(random.choice(vorin_compliment_quotes) + extra) #Chooses a random quote from above list
                                comments_replied_to2.append(parent.id)
                                print("Comment complimented!")

                                comment.reply(random.choice(vorin_success_quotes_2)) #Chooses a random quote from above list

                            else:
                                comment.reply(random.choice(vorin_fail_quotes_2)) #Chooses a random quote from above list

                            comments_replied_to2.append(comment.id)
                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            break

                if post:
                    comment.reply("Only the members of the Great Vorin Church can use this feature. If you are not a heretic, type !join to be welcomed by us!")
                    comments_replied_to2.append(comment.id)
                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

            if "!insult" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                for item in r.user.me().saved(limit = None):
                    if f"Devotee {comment.author}" in item.body:
                        if rank('past', comment.author) != "Heretic":
                            if (rank('present', comment.author) in ["High-noble", "Holy Emperor", "Herald"] and len(comment.body.split()) != 2):
                                comment.reply("O Bright One, you need to type just '!insult [username]' without the u/. Anything else will just confuse us.")
                                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                    f.write(comment.id + "\n")

                            elif rank('present', comment.author) in ["High-noble", "Holy Emperor", "Herald"] and len(comment.body.split()) == 2:
                                author = comment.body.split()[1]
                                try:
                                    for comment_other in r.redditor(author).comments.new(limit = 15):
                                        if author.lower() != "mistborn" and comment_other.subreddit.display_name.lower() == "cremposting" and comment_other.id not in comments_replied_to2:

                                            extra = f"\n\n ^(This insult was requested by {comment.author})"
                                            comment_other.reply(random.choice(vorin_insult_send) + extra)
                                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                                f.write(comment_other.id + "\n")
                                            comment.reply("The insult has been sent!")
                                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                                f.write(comment.id + "\n")
                                            break
                                        elif author.lower() == "mistborn":
                                            comment.reply(f"You really want to insult Brandon Sanderson? The Almighty shall not be disturbed!")
                                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                                f.write(comment.id + "\n")
                                            break
                                    else:
                                        if comment.id not in comments_replied_to2:
                                            comment.reply("No recent eligible comment found. Try someone else instead, or wait for them to make a new comment.")
                                except:
                                    comment.reply("Insult has failed, O Bright One.")
                            elif comment.id not in comments_replied_to2:
                                comment.reply("You are too lowly ranked to use this function (change in rank criteria). Be a good Vorin, follow the guidelines and praise the Almighty and the Heralds, and perhaps we will grant you this power!")

                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            print("Distance insult sent!")
                            break

                        else:
                            comment.reply("You are a Heretic! No priveleges for you, unless you repent!")

                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            print("Heretic found!")
                            break


            for key in ["syladin", "femboy"]:
                if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and comment.id not in comments_skimmed and not comment.author == r.user.me() and random.randint(1, 4) == 2:
                    comment.reply(f'{key.capitalize()}?! This word is not accepted!')
                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    print("Comment found!")

                elif comment.id not in comments_skimmed:
                        comments_skimmed.append(comment.id)

                        with open("comments_skimmed.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

    #Lopen joke
            for key in ["lopen joke", "lopen jokes", "one armed herdazian", "one-armed herdazian", "one-armed-herdazian", "one armed herdaz", "one-armed-herdaz"]:
                if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():

                    comment.reply(random.choice(lopen_joke_quotes)) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")


                    print("Comment found!")

        #Lopen insult
            for key in ["insult", "insults"]:
                if WholeWord(key)(comment.body) and (WholeWord("lopen")(comment.body) or WholeWord("gancho")(comment.body)) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                    post = True
                    for item in r.user.me().saved(limit = None):
                        if"Devotee {comment.author}" in item.body:
                            if rank("present", comment.author) != "Heretic":
                                post = False

                                Vorin = [
                                    "You dare try to insult a child of the Almighty? Shame!",
                                    "This cr*mposter is protected by the Great Vorin Church. You may not insult them!",
                                    f"Do you not recognise Devotee {comment.parent().author}? You shall insult them!"
                                ]

                                comment.reply(random.choice(Vorin)) #Chooses a random quote from above list

                                comments_replied_to2.append(comment.id)
                                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                    f.write(comment.id + "\n")

                                print("Comment not insulted")

                    if post:

                        parent = comment.parent()

                        if parent.id not in comments_replied_to2:
                            extra = f"\n\n ^(This insult was requested by {comment.author})"
                            parent.reply(random.choice(insult_quotes) + extra) #Chooses a random quote from above list
                            comments_replied_to2.append(parent.id)
                            print("Comment insulted!")

                            comment.reply(random.choice(success_quotes)) #Chooses a random quote from above list

                        else:
                            comment.reply(random.choice(fail_quotes)) #Chooses a random quote from above list
                            pass

                        comments_replied_to2.append(comment.id)
                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

        #Questions and answers
            if "!q" in comment.body.lower() and len(comment.body) < 40 and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                questions = {
                    "who is kaladin" : "Our depressed gon, gon!",
                    "what is chouta" : "Chouta, gon. Herdazian food. Good stuff.",
                    "who is dalinar" : "Definitely not a femboy, gancho!",
                    "what is your name" : "The Lopen, King of Alethkar!",
                    "who are you" : "I am your favourite character, gancho! I am the Lopen!",
                    "do you like me?" : "Of course I do, gon! Why wouldn't I?"}
                question = comment.body.replace("!q", "")
                question = comment.body.replace("!Q", "")
                if "!q " not in comment.body.lower():
                    question = question.split()[1:]
                    question = " ".join(question)
                    question.strip()

                for char in ",!.!?!;!:".split("!"):
                    question = question.replace(char, "")

                answer = ""
                for element in questions:
                    element2 = element
                    for char in ",!.!?!;!:".split("!"):
                        element2 = str(element2).replace(char, "")
                    if question.lower() in element2.lower():
                        answer = questions[element]
                        break
                    elif element2.lower() in question.lower():
                        answer = questions[element]
                        break

                if not answer:
                    for item in r.user.me().saved(limit = None):
                        element = item.body
                        element2 = item.body

                        for char in ",!.!?!;!:".split("!"):
                            element2 = element2.replace(char, "")
                            element2.strip()

                        if question.lower() in element2.lower():
                            if "!a" in element:
                                new_ele = element.split("!a")
                            else:
                                new_ele = element.split("!A")
                            new_ele = new_ele[1]
                            new_ele2 = new_ele.split()[:]

                            answer = " ".join(new_ele2)
                            answer.strip()
                            break

                        else:
                            if "!a" in element:
                                new_ele = element2.split("!a")
                            else:
                                new_ele = element2.split("!A")
                            new_ele = new_ele[0]

                            if "!q" in element:
                                new_ele = new_ele.split("!q")
                            else:
                                new_ele = new_ele.split("!Q")
                            if len(new_ele) > 1:
                                element2 = new_ele[1]
                                element2.strip()

                            if element2.lower() in question.lower():
                                if "!a" in element:
                                    new_ele = element.split("!a")
                                else:
                                    new_ele = element.split("!A")
                                new_ele = new_ele[1]
                                new_ele2 = new_ele.split()[:]

                                answer = " ".join(new_ele2)
                                answer.strip()
                                break

                if answer:
                    comment.reply(answer)
                    comments_replied_to2.append(comment.id)

                if not answer:
                    comment.reply("I do not know the answer to that yet, gancho. Could you tell me the answer?\n\n\
You can type out the answer by starting the comment with '!A', then following with a simple, one-lined answer with minimal punctuation and formatting.\n\n\
I'll learn it fast and give you the answer once you ask for it again!")
                    comments_replied_to2.append(comment.id)

                print("Question answered")

            try:
                if "!a" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and "!A" in comment.parent().body and comment.parent().author == r.user.me() and "!q" in comment.parent().parent().body.lower():

                    question = comment.parent().parent().body
                    answer = comment.body

                    comment.reply("The question and answer respectively are: \n\n" + question + "\n\n" + answer)
                    comments_replied_to2.append(comment.id)

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    next(r.redditor("The_Lopen_bot").comments.new(limit=1)).save()

                    print("Answer saved")

            except:
                pass

        #Lopen compliment
            if WholeWord("compliment")(comment.body) and (WholeWord("lopen")(comment.body) or WholeWord("gancho")(comment.body)) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():

                parent = comment.parent()

                if "compliment me" not in comment.body.lower():
                    if parent.id not in comments_replied_to2:
                        extra = f"\n\n ^(This compliment was requested by {comment.author})"
                        parent.reply(random.choice(compliment_quotes) + extra) #Chooses a random quote from above list
                        comments_replied_to2.append(parent.id)
                        print("Comment complimented!")

                        comment.reply(random.choice(comp_success_quotes)) #Chooses a random quote from above list

                    else:
                        comment.reply(random.choice(comp_fail_quotes)) #Chooses a random quote from above list
                        pass

                else:
                    extra = f"\n\n ^(Hope you feel nice, {comment.author}!)"
                    comment.reply(random.choice(compliment_quotes) + extra)
                    print("Comment complimented!")


                comments_replied_to2.append(comment.id)

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

        #What are your thoughts
            for key in [
                "what do you think",
                "what are your thoughts",
                "what do you think about this",
                "what do you think about it"]:
                if key in comment.body.lower() and (WholeWord("lopen")(comment.body) or WholeWord("gancho")(comment.body)) and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and len(comment.body) < 50:
                    thoughts_quotes = [
                        "Seems alright, gancho. Why do you ask?",
                        "**The Lopen gesture**",
                        "I don't like it, gon. Too little chouta.",
                        "Great, gon!",
                        "This has the approval of the King of Alethkar!"]

                    comment.reply(random.choice(thoughts_quotes)) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    print("Comment found!")

        #Random posts
            if "!crem" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                posts = [post for post in r.subreddit("Cremposting").top(limit = 1000)]
                post = random.choice(posts)

                intro = [
                    "Here's a nice post, gon!",
                    "Have a meme!",
                    "This is some crem I found, gancho!",
                    "Why don't you take a while to have a laugh!",
                    "I usually steal laughter, but this is too good to not share!"
                ]

                comment.reply(f"[{random.choice(intro)}]({r.config.reddit_url + post.permalink})")
                comments_replied_to2.append(comment.id)

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

                print("Post linked!")


        #Swear words
            if "!swear" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                redditor = comment.author
                comments = "".join([comment.body for comment in list(redditor.comments.new(limit = 1000))]).lower()

                reply = f"\nHey, gancho! You have been using bad Cosmere words, eh? Here are the stats for u/{comment.author}:\n\n\
|Swear words|Occurences|\n\
:--|:--|"
                swear_words = ["storms", "safehand", "femboy", "rusts", "rust and ruin", "merciful domi",\
                            "storming", "shat", "ashes", "starvin", "ash's eyes", "airsick", "nale's nuts", "taln's stones",
                            "by the survivor", "kelek's breath", "god beyond", "chull dung", "crem", "colors"]
                swear_words.sort()

                for key in swear_words:
                    if key == "colors":
                       count = comments.count(key) + comments.count("colours")
                    else:
                        count = comments.count(key)
                    if count> 0:
                        reply_part = f"|{key}|{count}|"

                        reply += f"\n{reply_part}"
                comment.reply(reply)
                comments_replied_to2.append(comment.id)

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

                print("Swear words found!")


        #Good bot
            parent = comment.parent()
            if "good bot" in comment.body.lower() and comment.id not in comments_replied_to2 and parent.author == r.user.me() and len(comment.body) < 20:
                good_bot = [
                    "Thanks, gancho!",
                    "I do my best, gon!",
                    "Why, you are welcome!",
                    "That's what a one-armed Herdazian is for!",
                    "That is what I do, gon!",
                    f"Good {comment.author}"
                ]

                comment.reply(random.choice(good_bot)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

                print("Comment found!")

        #Bad bot
            parent = comment.parent()
            if "bad bot" in comment.body.lower() and comment.id not in comments_replied_to2 and parent.author == r.user.me() and len(comment.body) < 20:
                bad_bot = [
                    "**Makes the Lopen gesture!**",
                    f"Storm off, {comment.author}!",
                ]

                comment.reply(random.choice(bad_bot)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

                print("Comment found!")

        #gancho
            for key in ["gancho", "moolie", "gon", "penhito", r.user.me(), "the lopen", "ganchos"]:
                if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():


                    comment.reply(random.choice(lopen_quotes)) #Chooses a random quote from above list

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
                if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and comment.id not in comments_skimmed and not comment.author == r.user.me():
                    happy_quotes = [
                        f"{key.capitalize()} is good! For more awesomeness, just ask for \"Lopen Joke\", and I'll give some to you!",
                        f"I have detected '{key}' in your comment, and have come to share the positivity!"
                    ]

                    if (happy_num := random.randint(1, 30)) == 2:
                        comment.reply(random.choice(happy_quotes)) #Chooses a random quote from above list

                        comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                        print("Comment found!")

                    elif comment.id not in comments_skimmed:
                        comments_skimmed.append(comment.id)

                        with open("comments_skimmed.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")
        #sad
            for key in ["sad", "depress", "depressed", "trauma", "depression", "not happy", "hurt", "ache",
            "heartache", "sadly", "unfortunate", "unfortunately", "traumatic"]:
                if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and comment.id not in comments_skimmed and not comment.author == r.user.me():
                    sad_quotes = [
                        f"Hey gancho, you used '{key}' in your comment. If you're sad, want to hear a joke? Just type \"The Lopen Joke\", and I'll give one to you!",
                        f"Gon, you good? I detected '{key}' in your comment."
                    ]

                    if (sad_num := random.randint(1, 30)) == 2:
                        comment.reply(random.choice(sad_quotes)) #Chooses a random quote from above list

                        comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                        print("Comment found!")

                    elif comment.id not in comments_skimmed:
                        comments_skimmed.append(comment.id)

                        with open("comments_skimmed.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

        #Stick
            if "you could be fire" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                stick_quotes = [
                        "I am a stick."
                     ]

                mess = random.choice(["\n\n^(These words of Stick's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Stick, brought by Lopen's cousins)",
                "\n\n^(Speak further to Stick by mentioning !Stick in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(stick_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

                print("Comment found!")

        #Correction
            for key in ["lopen", "Lopen"]:
                if key in comment.body  and not "The Lopen" in comment.body and comment.id not in comments_replied_to2 and comment.id not in comments_skimmed and not comment.author == r.user.me() and gancho_num == 2:
                    correction_quotes = [
                        "That would be *The Lopen* for you, moolie!",
                        f"How dare you disrespect The Lopen, King of Alethkar, by merely calling him '{key}'?",
                        f"{key}? Just {key}? Here, I am giving you the Lopen gesture!"
                    ]
                    comment.reply(random.choice(correction_quotes)) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    print("Comment found!")

                elif comment.id not in comments_skimmed:
                    comments_skimmed.append(comment.id)

                    with open("comments_skimmed.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

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
                if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and comment.id not in comments_skimmed and not comment.author == r.user.me() and pancake_num in (2, 3, 4):
                    pan2cakes_quotes = [
                        "Yeah, pancakes are alright, but have you tasted chouta?"
                    ]
                    comment.reply(random.choice(pan2cakes_quotes)) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    print("Comment found!")

                elif comment.id not in comments_skimmed:
                    comments_skimmed.append(comment.id)

                    with open("comments_skimmed.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

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

            if comment.id not in comments_skimmed and not comment.author == r.user.me():
                comments_skimmed.append(comment.id) #Adds skimmed comments to list
                with open("comments_skimmed.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")


    print("Sleeping for a bit")
    time.sleep(120)  #Cool-down period

#Function to save comments replied to
def get_saved_comments():

    if not os.path.isfile("comments_replied_to2.txt"):

        comments_replied_to2 = []

    else:

        with open("comments_replied_to2.txt", "r", encoding='cp1252') as f:
            comments_replied_to2 = f.read()
            comments_replied_to2 = comments_replied_to2.split("\n")

    return comments_replied_to2

def get_saved_posts():

    if not os.path.isfile("posts_replied_to.txt"):

        posts_replied_to = []

    else:

        with open("posts_replied_to.txt", "r", encoding='cp1252') as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")

    return posts_replied_to

def get_skimmed_comments():

    if not os.path.isfile("comments_skimmed.txt"):

        comments_skimmed = []

    else:

        with open("comments_skimmed.txt", "r", encoding='cp1252') as f:
            comments_skimmed = f.read()
            comments_skimmed = comments_skimmed.split("\n")

    return comments_skimmed

#Splits comment replied to into whole words
def WholeWord(w):

    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def rank(time, author):
    count = 0
    redditor = r.redditor(str(author))

    if time == "present":
        items = " ".join(str(item.body) for item in redditor.comments.new(limit = 100))
    else:
        items = " ".join(str(item.body) for item in list(redditor.comments.new(limit = 100))[1:])
    for key in ["vorin", "almighty", "herald", "nale", "kalak", "kelek", "nalan",
                "taln", "talenelat", "chanarach", "jezrien", "yezrien", "shalash",
                "ishar"]:
        count += items.lower().count(key)*300
    for key in ["storms", "safehand", "femboy", "rusts", "rust and ruin", "merciful domi",\
                    "storming", "shat", "ashes", "starvin", "ash's eyes", "airsick", "nale's nut", "taln's stones",
                    "by the survivor", "kelek's breath", "god beyond", "chull dung", "crem", "colors",
                "colours", "syladin", "almighty is dead"]:
        count -= items.lower().count(key)*50
    count -= items.lower().count("jasnah")*200

    for key in ["nale's nut", "taln's stones", "kelek's breath", "almighty is dead"]:
        count -= items.lower().count(key)*300


    ranks = {
            -100 : "Darkborn",
            50 : "Lighteyes",
            500: "Brightness",
            2000: "High-noble",
            5000: "Holy Emperor",
            10000: "Herald"
            }

    if count < -100:
        Storm_rank = "Heretic"
    else:
        for x in ranks:
            if count >= x:
                Storm_rank = ranks[x]
            else:
                break


    return Storm_rank

#Running the functions
r = bot_login()
comments_replied_to2 = get_saved_comments()
comments_skimmed = get_skimmed_comments()
posts_replied_to = get_saved_posts()


while True:
    try:
        run_bot(r, comments_replied_to2, posts_replied_to, comments_skimmed, WholeWord, rank)
    except:
        print("Error")
        time.sleep(120)
