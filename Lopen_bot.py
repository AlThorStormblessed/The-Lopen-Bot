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
from praw.models import Submission
import pandas as pd
import numpy as np
import json

#Bot login
def bot_login():
    r = praw.Reddit(username = userN,
                    password = userP,
                    client_secret = cSC,
                    client_id = cID,
                    user_agent = userAgent)
    return r

def run_bot(r, comments_replied_to2, posts_replied_to, comments_skimmed, mod_comments, mod_posts, removed_comments, WholeWord, rank, count, mod_queue_posts):
    saved = [x.id for x in r.user.me().saved(limit = None) if isinstance(x, Submission)]
    cremrunner = pd.read_csv("Ideals.csv", usecols = ["Name", "Order", "Spren"])
    for crempost in r.subreddit('Cremposting').new(limit = 25):

        if crempost.id not in saved and ("memeing every chapter" in crempost.title.lower() or "meming every chapter" in crempost.title.lower() or "Wasing the meming".lower() in crempost.title.lower() or "meming every letter" in crempost.title.lower()) and crempost.author != r.user.me():
            aut = crempost.author

            if aut == "JeffSheldrake":
                crempost.reply("[Meming every chapter - Mistborn](https://redd.it/pkrvjy/)")
                meme_post = r.submission(id = 'pkrvjy')

            elif aut == "Anacanrock11":
                crempost.reply("[Meming every chapter - Stormlight Archive](https://redd.it/pkrqeg/)")
                meme_post = r.submission(id = 'pkrqeg')

            elif aut == "SpaghettiMaestro14":
                crempost.reply("[Meming every chapter - Elantris](https://redd.it/pkrxrw/)")
                meme_post = r.submission(id = 'pkrxrw')

            elif aut == "AlThorStormblessed":
                crempost.reply("[Meming every letter of the Stormlight Archive](https://redd.it/r9c2tt/)")
                meme_post = r.submission(id = 'r9c2tt')

            text = meme_post.selftext
            meme_post.edit(f'* [{crempost.title}](https://www.reddit.com{crempost.permalink})\n\n' + text)

            crempost.save()

            print("Post saved")

    for post in r.subreddit('Cremposting').hot(limit = 5):
        post_num = random.randint(1, 5)
        if post.id not in posts_replied_to:
            if post_num == 1:
                if str(post.author).lower() != "althorstormblessed":
                    post_quotes = [
                        "This is good crem, gancho!",
                        "Great meme, Gon!",
                        "This crem deserves some chouta!",
                        "This post is as delicious as chouta."]

                    post.reply(random.choice(post_quotes)) #Chooses a random quote from above list
                    print("Post found!")

                    posts_replied_to.append(post.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    with open("posts_replied_to.txt", "a", encoding='cp1252') as f:
                        f.write(post.id + "\n")

                else:
                    post.reply(random.choice(insult_quotes) + "\n\n^(This insult was not requested by anyone. My Creator is storming stupid, that's all.)") #Chooses a random quote from above list
                    print("Post found!")

                    posts_replied_to.append(post.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    with open("posts_replied_to.txt", "a", encoding='cp1252') as f:
                        f.write(post.id + "\n")

            else:
                posts_replied_to.append(post.id)
                with open("posts_replied_to.txt", "a", encoding='cp1252') as f:
                    f.write(post.id + "\n")

    """for post in r.subreddit('Cremposting').new(limit = 5):
        if post not in mod_posts[-10:]:
            punc = '''!()-[]{};:'"\,<>./?@#$%^&*~'''
            title = post.title.lower()

            for ele in title:
                if ele in punc:
                    title = title.replace(ele, "")

            for key in ['fuck moash']:
                if key in title:
                    post.mod.remove()
                    post.reply(f"Hey, gancho. >!{key}!< in your title can be construed as a spoiler, thus you might want to repost this great meme with a better title.\n\n\
^(This action was performed automatically. If you have questions, contact u/AlThorStormblessed, gon!)")

                    my_comment = [comment for comment in r.user.me().comments.new(limit = 1)][0]
                    my_comment.distinguish(sticky = True)

                    removed_comments.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                    with open("removed_comments.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")"""

    '''for post in r.subreddit('Cremposting').hot(limit = 10):
        if post.score > 500 and posts_replied_to.count(post.id) < 1:
            post.reply("Don't forget to vote for the best post of the year!")
            my_comment = [comment for comment in r.user.me().comments.new(limit = 1)][0]
            my_comment.distinguish(sticky = True)

            posts_replied_to.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("posts_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")
            '''

#Send me message regarding new comments at regular intervals
    if int(time.time()//60) % 31 in [0, 1, 2, 3]:
        buncha_comments = "\n\n..................\n\n".join([f'[{comment.body}](https://www.reddit.com{comment.permalink}) ' + comment.submission.link_flair_text + '\n\n' + comment.submission.title for comment in r.subreddit("Cremposting").comments(limit = 30)])
        try:
            r.redditor("AlThorStormblessed").message("New comments!", buncha_comments)
        except:
            r.redditor("AlThorStormblessed").message("New comments!", buncha_comments[:10000])
        print("Message sent!")

#Modqueue
    queue = [item for item in r.subreddit("mod").mod.modqueue(limit=None)]
    if queue and queue[0] not in mod_queue_posts:
        r.redditor("AlThorStormblessed").message("Item in Mod queue", "There's an item in mod queue of r/Cremposting. Check it out!")
        print("Mod queue")

        mod_queue_posts.append(queue[0])  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

        with open("mod_queue_posts.txt", "a", encoding='cp1252') as f:
            f.write(str(queue[0]) + "\n")

#Restore removed comments
    for comment in removed_comments[-10:]:
        if comment:
            comment = r.comment(id = comment)
            if not comment.approved_by:
                for key in ["!>", "<!", ">! ", ">!", "!<"]:
                    if key == ">!":
                        thing = "!<"
                    else:
                        thing = ">!"

                    if key in ["!>", "<!"] and key in comment.body and (comment.body.count(key) != comment.body.count('>!>!') or comment.body.count(key) != comment.body.count('!<!<')):
                        pass
                    elif ">! " in comment.body and "\\>!" not in comment.body and "\\!<" not in comment.body:
                        pass
                    elif comment.body.count(key) != comment.body.count(thing):
                        pass
                    else:
                        for my_comment in list(comment.replies):
                            if my_comment.author == r.user.me() and 'spoiler tag' in my_comment.body.lower():
                                my_comment.delete()

                        comment.mod.approve()
                        #print("Comment approved.")

                        break

#Inbox
    for comment in r.inbox.comment_replies(limit = 20):
    #Sentience
        for word in ['sentient', 'sentience']:
            if word in comment.body.lower() and "not " + word not in comment.body.lower() and comment.new:
                sentient = ["Gon, I am definitely not sentient!",
                            "Of course I am not sentient!",
                            "Totally not sentient, lol!",
                            "Storm off, I am a bot, not a sentient being!",
                            "Who said I am sentient gon? Must be one of those Lighteyes.",
                            "u/AlThorStormblessed, tell this fellow that I am *not* sentient!"]
                comment.reply(random.choice(sentient))
                comment.mark_read()

                print("Definitely not sentient!")

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

    #Good bot
        if "good bot" in comment.body.lower() and comment.new and len(comment.body) < 20:
            good_bot = [
                "Thanks, gancho!",
                "I do my best, gon!",
                "Why, you are welcome!",
                "That's what a one-armed Herdazian is for!",
                "That is what I do, gon!",
                f"Good {comment.author}"
            ]

            comment.reply(random.choice(good_bot)) #Chooses a random quote from above list
            comment.mark_read()

            print("Good bot!")

            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")

    #Bad bot
        if "bad bot" in comment.body.lower() and comment.new and len(comment.body) < 20:
            bad_bot = [
                "**Makes the Lopen gesture!**",
                f"Storm off, {comment.author}!",
            ]

            comment.reply(random.choice(bad_bot)) #Chooses a random quote from above list
            comment.mark_read()

            print("Bad bot!")

            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")


    #Main code
    if count:
        n = 20
    else:
        n = 200

    for comment in r.subreddit('Cremposting+Lopen_bot_test').comments(limit = n):
        comment.refresh()
        #Randomness to make sure Lopen doesn't reply to every comment with these words

        pancake_num = random.randint(1, 4)
        gancho_num = random.randint(1, 3)
        x_com = comment
        y_com = comment

        if str(comment.author).lower() not in ["b0trank"]:

        #Spoiler
            for key in ["!>", "<!", ">! "]:
                if comment.id not in mod_comments:
                    if key in comment.body and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                        if key in ["!>", "<!"] and (comment.body.count(key) != comment.body.count('>!>!') or comment.body.count(key) != comment.body.count('!<!<')):
                            extra = f"You have used {key} by mistake, which is wrong. Use \>!(Text here)\!< instead for correct spoiler tags!"
                        elif key == ">! " and "\\>!" not in comment.body and "\\!<" not in comment.body:
                            extra = f"There is a space between your spoiler tag and text! Remove it to fix the spoiler!"

                        disclaimer = "\n\n^(If you are explaining the correct usage of tags, type \\\!< and \\\>! so I don't get confused. Alternatively, use > ! and ! < for explanations.)"

                        comment.reply(extra + disclaimer) #Chooses a random quote from above list

                        comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                        print("Untagged spoiler found!")

                        my_comment = [comment for comment in r.user.me().comments.new(limit = 1)][0]
                        my_comment.mod.distinguish()

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                        mod_comments.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                        with open("mod_comments.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                elif key in comment.body and comment.id not in removed_comments and r.user.me().is_mod and int(time.time() - comment.created_utc)/60 > 10:

                    if (key in ["!>", "<!"] and (comment.body.count(key) != comment.body.count('>!>!') or comment.body.count(key) != comment.body.count('!<!<'))) or (key == ">! " and "\\>!" not in comment.body and "\\!<" not in comment.body):
                        for my_comment in list(comment.replies):
                            if my_comment.author == r.user.me() and 'spoiler tag' in my_comment.body.lower():
                                extra = my_comment.body
                                my_comment.delete()

                        comment.reply(f"Hey gon, this comment has been removed due to bad spoiler tags. {extra} Edit your original comment for it to be reinstated, or repost it with fixed tags.\n\n^(This action was performed automatically. If you think this was done incorrectly, contact u/AlThorStormblessed.)")
                        comment.mod.remove()

                        print("Comment removed")

                        my_comment = [comment for comment in r.user.me().comments.new(limit = 1)][0]
                        my_comment.mod.distinguish()

                        removed_comments.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                        with open("removed_comments.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

            for key in [">!", "!<"]:
                if comment.id not in mod_comments:
                    for element in comment.body.split("\n\n"):
                        if key in element and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                            if key == ">!":
                                thing = "!<"
                            else:
                                thing = ">!"

                            if element.count(key) == element.count(thing):
                                pass
                            else:
                                if element.count(key) > element.count(thing):
                                    tag = thing
                                else:
                                    tag = key

                                disclaimer = "\n\n^(If you are explaining the correct usage of tags, type \\\!< and \\\>! so I don't get confused. Alternatively, use > ! and ! < for explanations.)"

                                comment.reply(f"You are missing at least one {tag} in that comment (spoiler tags do not work across paragraphs, so make sure to check for that as well)! Fix it so others don't get spoiled!" + disclaimer)

                                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                                print("Untagged spoiler found!")

                                my_comment = [comment for comment in r.user.me().comments.new(limit = 1)][0]
                                my_comment.mod.distinguish()

                                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                    f.write(comment.id + "\n")

                                mod_comments.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                                with open("mod_comments.txt", "a", encoding='cp1252') as f:
                                    f.write(comment.id + "\n")

                                break

                else:
                    for element in comment.body.split("\n\n"):
                        if key in element and comment.id not in removed_comments and r.user.me().is_mod and int(time.time() - comment.created_utc)/60 > 10:
                            if key == ">!":
                                thing = "!<"
                            else:
                                thing = ">!"

                            if element.count(key) == element.count(thing):
                                pass
                            else:
                                for my_comment in list(comment.replies):
                                    if my_comment.author == r.user.me() and 'spoiler tag' in my_comment.body.lower():
                                        extra = my_comment.body
                                        my_comment.delete()

                                comment.reply(f"Hey gon, this comment has been removed due to bad spoiler tags. {extra} Edit your original comment for it to be reinstated, or repost it with fixed tags.\n\n^(This action was performed automatically. If you think this was done incorrectly, contact u/AlThorStormblessed.)")
                                comment.mod.remove()

                                my_comment = [comment for comment in r.user.me().comments.new(limit = 1)][0]
                                my_comment.mod.distinguish()

                                print("Comment removed")

                                removed_comments.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                                with open("removed_comments.txt", "a", encoding='cp1252') as f:
                                    f.write(comment.id + "\n")

                                break

        #My commands
            if "!delete" in comment.body.lower() and comment.id not in comments_replied_to2 and comment.parent().author == r.user.me():
                if comment.author == "AlThorStormblessed":
                    comment.parent().delete()

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment deleted!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                else:
                    comment.reply(random.choice(
                        ["Who are you, gon, to command me so?",
                        "I don't listen to anyone but my idiot Creator!",
                        "You aren't AlThorStormblessed..."]))

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Comment *not* deleted!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

        #Emulate users
            if "!emulate" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                text = comment.body
                text = text.split("!emulate")[-1]
                text = text.split()

                search = text[0]

                punc = '''!()-[]{};:'"\,<>./?@#$%^&*~'''

                for ele in search:
                    if ele in punc:
                        search = search.replace(ele, "")

                try:
                    user = r.redditor(search)
                    string = random.choice([comment for comment in user.comments.new(limit = None) if comment.subreddit.display_name.lower() == 'cremposting'])
                    link = string.permalink
                    string = string.body.split("\n\n")

                    new_string = ""
                    for ele in string:
                        new_string += f"*>!{ele}!<* ".replace('u/mistborn', '(summoned Brando here)')

                    comment.reply(f'{new_string.strip()}[Link](https://www.reddit.com{link})' + f"\n\n~{user}")

                except:
                    comment.reply("Who the hell is that, gon?")
                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("User mimicked!")

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

        #Meming every chapter
            if "!meme_list" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                text = comment.body
                text = text.split("!meme_list")[-1]
                text = text.split()

                search = text[0]

                punc = '''!()-[]{};:'"\,<>./?@#$%^&*~'''

                for ele in search:
                    if ele in punc:
                        search = search.replace(ele, "")

                if search.lower() in ["stormlight", "sa"]:
                    comment.reply("[Meming every chapter - Stormlight Archive](https://redd.it/pkrqeg/)")

                elif search.lower() in ["warbreaker", "wb"]:
                    comment.reply("[Meming every chapter - Warbreaker](https://redd.it/pks0ux/)")

                elif search.lower() in ["elantris", "el"]:
                    comment.reply("[Meming every chapter - Elantris](https://redd.it/pkrxrw/)")

                elif search.lower() in ["mistborn", "mb"]:
                    comment.reply("[Meming every chapter - Mistborn](https://redd.it/pkrvjy/)")

                else:
                    comment.reply("No such page found, please type in the format '!meme_list (SA/MB/WB/EL)' to produce a result.")


                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Meme list exported!")

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")


            if "!meme" in comment.body.lower() and "!memecaller" not in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                text = comment.body
                text = text.split("!meme")[-1]
                text = text.split()

                try:
                    punc = '''!()-[]{};:'"\,<>./?@#$%^&*~'''

                    for ele in text:
                        if ele in punc:
                            text = text.replace(ele, "")

                    search = text[0]
                    num = int(text[1])


                    if search.lower() in ["stormlight", "sa"]:
                        meme_post = r.submission(id='pkrqeg')

                    elif search.lower() in ["warbreaker", "wb"]:
                        meme_post = r.submission(id='pks0ux')

                    elif search.lower() in ["elantris", "el"]:
                        meme_post = r.submission(id='pkrxrw')

                    elif search.lower() in ["mistborn", "mb"]:
                        meme_post = r.submission(id='pkrvjy')

                    else:
                        meme_post = ""
                        comment.reply("No such page found, gon, please type in the format '!meme (SA/MB/WB/EL) (part no.)' to produce a result.")

                    if meme_post:
                        meme_text = meme_post.selftext.split("\n")

                        post_links = []
                        for element in meme_text:
                            element2 = element
                            for ele in element2:
                                if ele in punc:
                                    element2 = element2.replace(ele, " ")

                            if str(num) in element2.split():
                                post_links.append(element)


                        text_links = "\n\n".join(post_links)

                        comment.reply("Hey, gon, I think this is what you are looking for\n\n" + text_links)

                except:
                    comment.reply("Make sure you are using  the correct format, which is '!meme (SA/MB/WB/EL) (part no.)' to produce a result.")

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Meme sent!")

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

    #Lopen messaging service
            LMS = []
            for key in [
                "!kaladin", "!shallan", "!adolin", "!stormfather", "!stormdaddy", "!taln", "!syl", "!pattern",
                "!stick", "!dalinar", "!dadinar", "!rock", "!numuhukumakiaki'aialunamor", "!jasnah", "!nightblood"
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

                elif lms_key == "!nightblood":


                    mess = random.choice(["\n\n^(These words of Nightblood's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Nightblood, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Nightblood by mentioning !Nightblood in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    comment.reply(random.choice(nightblood_quotes) + mess + list_of) #Chooses a random quote from above list

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
* Wit (summoned as either ! Wit (quote to commentor) or ! Wit [...] insult (insult parent commentor)\n\
\n\
* Nightblood"

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

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Wit replied!")

                else:
                    if WholeWord("lopen")(comment.body):
                        insult_num = random.randint(1, 2)

                    else:
                        insult_num = 1

                    if insult_num == 1:
                        post = True
                        for item in r.user.me().saved(limit = None):
                            if isinstance(item, praw.models.Comment):
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
                            fail_or_insult = random.randint(1, 5)

                            wit_insult = [
"The sum total of stupid people is somewhere around the population of the planet. Plus one. You count twice.",
"I would never call you an imbecile, because then I would have to explain what that is, and I doubt any of us have the requisite time.",
f"You see, {comment.parent().author}, you make it too easy. An uneducated, half-brained serving boy with a hangover could make mock of you. I am left with no need to exert myself, and your very nature makes mockery of my mockery. And so it is that through sheer stupidity you make me look incompetent.",
"I needed an objective frame of reference by which to judge the experience of your company. Somewhere between four and five blows, I place it.",
f"{comment.parent().author}, I salute you. You are what lesser cretins like AlThorStormblessed aspire to be.",
f"I point out truths when I see them, {comment.parent().author}. Each man has his place. Mine is to make insults. Yours is to be in-sluts.",
"So, dear sir, when I say that you are the very embodiment of repulsiveness, I am merely looking to improve my art.",
"You look so ugly, it seems that someone tried — and failed — to get the warts off your face through aggressive application of sandpaper.",
"You are less a human being, and more a lump of dung with aspirations. If someone took a stick and beat you repeatedly, it could only serve to improve your features.",
"Your face defies description, but only because it nauseated all the poets. You are what parents use to frighten children into obedience.",
"I’d tell you to put a sack over your head, but think of the poor sack!",
"Theologians use you as proof that God exists, because such hideousness can only be intentional.",
f"Ahh {comment.parent().author}! You remind me of someone very dear to me. My horse.",
"You storming personification of a cancerous anal discharge.",
                            ]

                            mess = random.choice(["\n\n^(These words of Wit's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                                "\n\n^(-Wit, brought by Lopen's cousins)",
                                "\n\n^(Speak further to Wit by mentioning ! Wit in your comments. Anytime, anywhere. LMS)"])

                            list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                            if fail_or_insult == 1:
                                comment.reply(random.choice(wit_fail) + "\n\n" + random.choice(wit_insult).replace('comment.parent().author', 'comment.author') + mess + list_of)

                            else:
                                if comment.parent().id not in comments_replied_to2:
                                    comment.parent().reply(random.choice(wit_insult).replace('x_com', 'comment.parent().author') + mess + list_of) #Chooses a random quote from above list
                                    comments_replied_to2.append(parent.id)
                                    print("Comment insulted!")

                                else:
                                    comment.reply(random.choice(wit_fail_2) + mess + list_of) #Chooses a random quote from above list
                                    pass

                comments_replied_to2.append(comment.id)

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

        #Knights Radiants
            for key in ["!cremrunner", "!shartweaver", "!memecaller", "!hiighbreaker", "!willyshaper", "!rafowatcher", "!edgydancer", "!mudflinger", "!stonedward", "!cumbringer"]:
                if key in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                    if key == "!cumbringer":
                        key = "!mudflinger"
                    #print(f"{key}")

                    heretic = False
                    for item in r.user.me().saved(limit = None):
                        if isinstance(item, praw.models.Comment) and f"Heretic {comment.author}" in item.body and rank("present", comment.author) == "Heretic":
                            heretic = True

                    extra = ""
                    for item in r.user.me().saved(limit = None):
                        if extra or heretic:
                            break
                        elif isinstance(item, praw.models.Comment) and f"Devotee {comment.author}" in item.body :
                            extra = f"\n\nHeretic {comment.author} has been excommunicated from the Vorin Church!"
                            break

                    post = True

                    if cremrunner["Name"].str.contains(str(comment.author)).any():
                        if post and cremrunner[cremrunner["Name"] == str(comment.author)]["Order"].any() == key[1:].capitalize():
                            comment.reply(f"{comment.author} is already a Radiant of the Order {key[1:].capitalize()}.")
                            comments_replied_to2.append(comment.id)

                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            print("Old Radiant found!")
                            post = False

                            break

                        elif post and cremrunner[cremrunner["Name"] == str(comment.author)]["Order"].any() != "Oathless":
                            key_2 = list(cremrunner[cremrunner["Name"] == str(comment.author)]["Order"])[0]

                            comment.reply(f"{comment.author} has left the Order {key_2}. Welcome, {key[1:].capitalize()} {comment.author}!" + extra)
                            comments_replied_to2.append(comment.id)

                            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                f.write(comment.id + "\n")

                            cremrunner[ "Order"][cremrunner.index[cremrunner['Name'] == comment.author]] = key[1:].capitalize()
                            cremrunner.to_csv("Ideals.csv", index = False)

                            print("Old Radiant found!")
                            post = False

                            break

                    if post and (comment.id not in comments_replied_to2):
                        comment.reply(f"Welcome, {key[1:].capitalize()} {comment.author}!" + extra)
                        comments_replied_to2.append(comment.id)

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                        if cremrunner["Name"].str.contains(str(comment.author)).any():
                            print("Changed")
                            cremrunner["Order"][cremrunner.index[cremrunner['Name'] == comment.author]] = key[1:].capitalize()

                        else:
                            print(str(comment.author))
                            cremrunner = cremrunner.append({"Name" : str(comment.author), "Order" : key[1:].capitalize(), "Spren" : np.NaN}, ignore_index=True)

                        cremrunner.to_csv("Ideals.csv", index = False)
                        cremrunner = pd.read_csv("Ideals.csv", usecols = ["Name", "Order", "Spren"])
                        #print(list(cremrunner.keys())[-1])
                        print("New Radiant found!")

                        break

                    elif comment.id not in comments_replied_to2:
                        print("Something went wrong, huh.")
                        comments_replied_to2.append(comment.id)

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                        break


            if "!break" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and cremrunner["Name"].str.contains(str(comment.author)).any():
                print("Breaking Radiant...")
                if cremrunner["Name"].str.contains(str(comment.author)).any():
                    key_2 = list(cremrunner[cremrunner["Name"] == str(comment.author)]["Order"])[0]

                    if (spren := list(cremrunner[cremrunner["Name"] == str(comment.author)]["Spren"])[0]) != np.NaN:
                        extra = f"Your spren, {spren}, has died."
                    else:
                        extra = ""
                    if key_2 != "Oathless":
                        comment.reply(f"{comment.author} has left the Order {key_2}. {comment.author} is Oathless. {extra}")
                        comments_replied_to2.append(comment.id)

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                        cremrunner["Order"][cremrunner.index[cremrunner['Name'] == comment.author]] = "Oathless"
                        cremrunner["Spren"][cremrunner.index[cremrunner['Name'] == comment.author]] = np.NaN
                        cremrunner.to_csv("Ideals.csv", index = False)

                        print("Radiant has Broken!")


            if "!spren" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and cremrunner["Name"].str.contains(str(comment.author)).any():
                if cremrunner["Name"].str.contains(str(comment.author)).any():
                    spren = list(cremrunner[cremrunner["Name"] == str(comment.author)]["Order"])[0]

                if spren == "Cremrunner":
                    extra = f"Hello, {comment.author}! I am you Cremspren, and your friend! I will guide you through the Oaths of the Cremrunners, and help you when you need me!"
                elif spren == "Shartweaver":
                    extra = f"Mmmm. I am a Shartspren. Mmmm."
                elif spren == "Memecaller":
                    extra = "Memespren am. Memecaller are."
                elif spren == "Hiighbreaker":
                    extra = "Stop wasting time and start training!"
                elif spren == "Willyshaper":
                    extra = f"I am your Willy! I will help you shape everyone's Willies!"
                elif spren == "mudflinger":
                    extra = "You are not a mudflinger. You are a ***Releaser***."
                elif spren == "Edgydancer":
                    extra = "Mistress, uh, Master? I am your Edgyspren?"
                elif spren == "Stonedward":
                    extra = f"Hehehehehehehe, I am your Stonedspren. Want some firemoss?"
                elif spren == "Rafowatcher":
                    extra = "RAFO, lmao"
                else:
                    spren = ''

                if spren and spren != "Rafowatcher":
                    comment.reply(extra + "\n\nCurrent powers of Radiants are:\n\n\
1. !therapy: Type this out for compliments and encouragements you might need.\n\n\
2. !break: Use this to kill your spren and leave your Order. Don't do this.\n\n\
3. !name: Type !name (Spren name) to name your own spren!\n\n\
4. Change Order: You can change your spren and Order any time, using the same functions as the joining ones. We don't mind much.")

                    comments_replied_to2.append(comment.id)
                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    print("Spren introduced.")


            if "!therapy" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and cremrunner["Name"].str.contains(str(comment.author)).any():
                if (name := list(cremrunner[cremrunner["Name"] == str(comment.author)]["Spren"])[0]) != np.NaN:
                    extra = f"\n\n^(This therapy was given by your spren, {name}!)"
                else:
                    extra = ""

                spren = ''
                if cremrunner["Name"].str.contains(str(comment.author)).any():
                    spren = list(cremrunner[cremrunner["Name"] == str(comment.author)]["Order"])[0]

                if spren == "Cremrunner":
                    comment.reply(random.choice(cremspren) + extra)
                elif spren == "Shartweaver":
                    comment.reply(random.choice(shartspren) + extra)
                elif spren == "Memecaller":
                    comment.reply(random.choice(memespren) + extra)
                elif spren == "Hiighbreaker":
                    therapy = random.randint(1, 3)
                    if therapy == 1:
                        comment.reply(random.choice(hiighspren) + extra)
                elif spren == "Willyshaper":
                    comment.reply(random.choice(willyspren) + extra)
                elif spren == "mudflinger":
                    comment.reply(random.choice(mudspren) + extra)
                elif spren == "Edgydancer":
                    comment.reply(random.choice(edgyspren) + extra)
                elif spren == "Stonedward":
                    comment.reply(random.choice(stonedspren) + extra)
                elif spren == "Rafowatcher":
                    comment.reply(random.choice(rafospren) + extra)
                else:
                    spren = ''

                if spren:
                    comments_replied_to2.append(comment.id)
                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    print("Therapy given.")

            for key in ["!name", "!\\name"]:
                if key in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and cremrunner["Name"].str.contains(str(comment.author)).any() and list(cremrunner[cremrunner["Name"] == str(comment.author)]["Order"])[0] != "Oathless":
                    text = comment.body
                    text = text.lower().split("!name")[-1].split("!\\name")[-1]
                    text = text.split()

                    #try:
                    punc = '''!()-[]{};:'"\,<>./?@#$%^&*~'''

                    for ele in text:
                        if ele in punc:
                            text = text.replace(ele, "")

                    name = text[0]

                    comment.reply(f"Your spren has been named {name.capitalize()}")
                    comments_replied_to2.append(comment.id)

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    cremrunner["Spren"][cremrunner.index[cremrunner['Name'] == comment.author]] = name
                    #print(cremrunner["Spren"][cremrunner.index[cremrunner['Name'] == comment.author]])
                    cremrunner.to_csv("Ideals.csv", index = False)
                    cremrunner = pd.read_csv("Ideals.csv", usecols = ["Name", "Order", "Spren"])


                    '''except:
                        comment.reply("Make sure you are using the correct format, which is '!name (new spren name)' to produce a result.")'''

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Spren named!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                elif key in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                    text = comment.body
                    text = text.lower().split("!name")[-1].split("!\\name")[-1]
                    text = text.split()

                    #try:
                    punc = '''!()-[]{};:'"\,<>./?@#$%^&*~'''

                    for ele in text:
                        if ele in punc:
                            text = text.replace(ele, "")

                    name = text[0]

                    comment.reply(f"Your spren has been named {name.capitalize()}")
                    comments_replied_to2.append(comment.id)

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Spren named!")

                    cremrunner = cremrunner.append({"Name" : str(comment.author), "Order" : "Cremrunner", "Spren" : name}, ignore_index=True)

                    cremrunner.to_csv("Ideals.csv", index = False)
                    cremrunner = pd.read_csv("Ideals.csv", usecols = ["Name", "Order", "Spren"])

            if "!shart" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                if cremrunner["Name"].str.contains(str(comment.author)).any() and list(cremrunner[cremrunner["Name"] == str(comment.author)]["Order"])[0] == "Shartweaver":
                    sent_list = comment.parent().body.split()
                    spren = list(cremrunner[cremrunner["Name"] == str(comment.author)]["Spren"])[0]

                    for word in range(len(sent_list)):
                        num = random.randint(1, 4)
                        if num == 2:
                            word2 = sent_list[word].replace(">!", "").replace("!<", "")
                            sent_list[word] = sent_list[word].replace(word2, "shart")

                    if sent_list.count('shart') == 0:
                        sent_list[random.randint(0, len(sent_list))] = 'shart'

                    comment.reply("Shartified:\n\n" + ' '.join(sent_list) + f"\n\n^(This comment was sharted by your spren {spren})")
                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Sentence sharted!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")
                else:
                    comment.reply("Are you sure that you are a part of the Shartweavers? Try joining it again!")
                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Sentence not sharted!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")
            if "!lash" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                if cremrunner["Name"].str.contains(str(comment.author)).any() and list(cremrunner[cremrunner["Name"] == str(comment.author)]["Order"])[0] == "Cremrunner":
                    user = comment.author
                    new_comment = comment.body.split("!lash")[-1].split("!Lash")[-1]

                    other_comment = [comment for comment in user.comments.new(limit = None) if comment.subreddit.display_name.lower() == 'cremposting'][0]

                    spren = list(cremrunner[cremrunner["Name"] == str(comment.author)]["Spren"])[0]

                    comment.reply(f"Words have been Lashed!\n\n^(These words were brought by your spren {spren})")
                    comments_replied_to2.append(comment.id)

                    other_comment.reply(str(user) + ',' + new_comment)
                    comments_replied_to2.append(other_comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Sentence lashed!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")
                else:
                    comment.reply("Are you sure that you are a part of the Cremrunners? Try joining it again!")
                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Sentence not lashed!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

        for key in (bots := {"!gandalf" : 'gandalf-bot', "!lews" : 'LewsTherinTelamonBot', "!bobby" : 'bobby-b-bot', "!kenobi" : 'Obiwan-Kenobi-Bot', "!nynaeve" : 'Braid_tugger-bot'}).keys():
            if key in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                if cremrunner["Name"].str.contains(str(comment.author)).any() and list(cremrunner[cremrunner["Name"] == str(comment.author)]["Order"])[0] == "Memecaller":
                    user = r.redditor(bots[key])
                    other_comment = random.choice([comment for comment in user.comments.new(limit = 25)])
                    spren = list(cremrunner[cremrunner["Name"] == str(comment.author)]["Spren"])[0]

                    comment.reply(other_comment.body + f"\n\n^(The bot called is. {spren} call did.)")
                    comments_replied_to2.append(comment.id)

                    print("Meme bot called!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")
                else:
                    comment.reply("Are you sure that you are a part of the Memecallers? Try joining it again!")
                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Meme bot not called!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

        for key in ["!mud", "!fling"]:
            if key in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                if cremrunner["Name"].str.contains(str(comment.author)).any() and list(cremrunner[cremrunner["Name"] == str(comment.author)]["Order"])[0] == "Mudflinger":
                    if comment.parent() not in comments_replied_to2:
                        spren = list(cremrunner[cremrunner["Name"] == str(comment.author)]["Spren"])[0]
                        comment.reply(f"The mud has been flung, Radiant.\n\n^(This comment was brought by your spren {spren})")
                        comments_replied_to2.append(comment.id)

                        comment.parent().reply(random.choice(mudfling) + f"\n\n^(This mud was flung by {comment.author})")
                        print("Mud flung!")

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                        comments_replied_to2.append(comment.parent().id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.parent().id + "\n")
                    else:
                        comment.reply("The Lopen has already replied to that comment, Mudflinger. Destruction has failed.")
                        comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                        print("Mud not flung!")

                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

                else:
                    comment.reply("Are you sure that you are a part of the Mudfliners? Try joining it again!")
                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                    print("Mud not flung!")

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

        #Vorin Church
            if "!join" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                radiant = False
                if cremrunner["Name"].str.contains(str(comment.author)).any():
                    key_2 = list(cremrunner[cremrunner["Name"] == str(comment.author)]["Order"])[0]
                    if key_2 != "Oathless":
                        radiant = True

                if not radiant:
                    post = True
                    heretic = False
                    print(rank("present", comment.author))
                    for item in r.user.me().saved(limit = None):
                        if isinstance(item, praw.models.Comment):
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
                        if isinstance(item, praw.models.Comment):
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
                else:
                    comment.reply("A Radiant?! No Radiants are allowed in the Great Vorin Church! !break all your bonds, then we might allow you in!")
                    comments_replied_to2.append(comment.id)

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    print("Filthy Radiant found!")

                    break

            if not cremrunner["Name"].str.contains(str(comment.author)).any() or list(cremrunner[cremrunner["Name"] == str(comment.author)]["Order"])[0] == "Oathless":

                for key in ["storms", "safehand", "femboy", "rusts", "rust and ruin", "merciful domi", "syladin",
                            "storming", "shat", "ashes", "starvin", "ash's eyes", "airsick", "nale's nut", "taln's stones",
                            "by the survivor", "kelek's breath", "god beyond", "chull dung", "crem", "colors", "almighty is dead"]:
                    if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and comment.id not in comments_skimmed and not comment.author == r.user.me():
                        for item in r.user.me().saved(limit = None):
                            if isinstance(item, praw.models.Comment):
                                if f"Devotee {comment.author}" in item.body and comment.id not in comments_replied_to2:
                                    if rank('past', comment.author) != "Heretic":
                                        if rank('present', comment.author) != rank('past', comment.author) and rank('present', comment.author) != "Heretic":
                                            comment.reply(f"Due to recent activities, your Vorin rank has changed from **{rank('past', comment.author)} to {rank('present', comment.author)}**")
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
                            if isinstance(item, praw.models.Comment):
                                if f"Devotee {comment.author}" in item.body:
                                    if rank('past', comment.author) != "Heretic":
                                        if rank('present', comment.author) != rank('past', comment.author) and rank('present', comment.author) != "Heretic":
                                            comment.reply(f"Due to recent activities, your Vorin rank has changed from **{rank('past', comment.author)} to {rank('present', comment.author)}**")
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
                        if isinstance(item, praw.models.Comment):
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
                        if isinstance(item, praw.models.Comment):
                            if f"Devotee {comment.author}" in item.body:
                                if rank('past', comment.author) != "Heretic":
                                    comment.reply(f"Ah, {rank('present', comment.author)} {comment.author}. You wish to seek our guidelines! Here they are:\n\n\
1. The Great Vorin Church does not permit the use of any swear words, except the name of the Almighty and the Great Heralds. Swearing shall result in reduction in rating and possible reduction in rank, even excommunication.\n\n\
2. Any defiling of Herald names, as and when we detect it, shall result in excommunication.\n\n\
3. No man shall dare read or write on this subreddit. Only through female scribes or ardents shall written word be transmitted (we are working on figuring out how to catch such heretics.)\n\n\
4. Censor the name of J\*snah Kh\*lin, or use a title. Such heretics must not be tolerated. This will result in reduction in rating and possible reduction in rank, even excommunication..\n\n\
5. For more information about ranking, type !rank.")
                                    comments_replied_to2.append(comment.id)
                                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                        f.write(comment.id + "\n")

                                    print("Guidelines!")
                                    break

                for key in ["!cat", "!dog", "!cow", "!crab"]:
                    if key in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                        for item in r.user.me().saved(limit = None):
                            if isinstance(item, praw.models.Comment):
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

                                        comments_replied_to2.append(comment.id)
                                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                            f.write(comment.id + "\n")

                                        print("Cute image sent!")
                                        break

                                    else:
                                        comment.reply("You are a Heretic! No priveleges for you, unless you repent!")

                                        comments_replied_to2.append(comment.id)
                                        with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                            f.write(comment.id + "\n")

                                        print("Heretic found!")
                                        break

                if "!rickroll" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                    for item in r.user.me().saved(limit = None):
                        if isinstance(item, praw.models.Comment):
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

                                    comments_replied_to2.append(comment.id)
                                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                        f.write(comment.id + "\n")

                                    print("Rickroll sent!")
                                    break

                                else:
                                    comment.reply("You are a Heretic! No priveleges for you, unless you repent!")

                                    comments_replied_to2.append(comment.id)
                                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                                        f.write(comment.id + "\n")

                                    print("Heretic found!")
                                    break


                if "!rank" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                    for item in r.user.me().saved(limit = None):
                        if isinstance(item, praw.models.Comment):
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

                if WholeWord("jasnah")(comment.body) and comment.id not in comments_skimmed and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                    for item in r.user.me().saved(limit = None):
                        if isinstance(item, praw.models.Comment):
                            if f"Devotee {comment.author}" in item.body:
                                if rank('past', comment.author) != "Heretic" and comment.id not in comments_replied_to2:
                                    if rank('present', comment.author) != rank('past', comment.author) and rank('present', comment.author) != "Heretic":
                                        comment.reply(f"Due to recent activities (change in rank criteria), your Vorin rank has changed from **{rank('past', comment.author)} to {rank('present', comment.author)}**")
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
                        if isinstance(item, praw.models.Comment):
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
                        if isinstance(item, praw.models.Comment):
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
                        if isinstance(item, praw.models.Comment):
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

                if ("!vorin compliment" in comment.body.lower() or "!praise" in comment.body.lower()) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                    post = True
                    for item in r.user.me().saved(limit = None):
                        if isinstance(item, praw.models.Comment):
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
                        if isinstance(item, praw.models.Comment):
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
                        if isinstance(item, praw.models.Comment):
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
                        if isinstance(item, praw.models.Comment):
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

        #gancho
            for key in ["gancho", "moolie", "gon", "penhito", r.user.me(), "the lopen", "ganchos"]:
                if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                    comment.reply(random.choice(lopen_quotes)) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    print("Comment found!")

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
                if key in comment.body  and not "the lopen" in comment.body.lower() and not "thelopen" in comment.body.lower() and comment.id not in comments_replied_to2 and comment.id not in comments_skimmed and not comment.author == r.user.me() and gancho_num == 2:
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

        #cousin
            for key in ["cousin", "cousins"]:
                if WholeWord(key)(comment.body) and comment.id not in comments_skimmed and not comment.author == r.user.me() and gancho_num == 2:
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
                if WholeWord(key)(comment.body) and comment.id not in comments_skimmed and comment.id not in comments_skimmed and not comment.author == r.user.me() and pancake_num == 4:
                    pan2cakes_quotes = [
                        "Yeah, pancakes are alright, but have you tasted chouta?",
                        "Gon, pancakes are not *that* great! Have some chouta!",
                        "Chouta before pancakes, gon!"
                    ]
                    comment.reply(random.choice(pan2cakes_quotes)) #Chooses a random quote from above list

                    comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                    with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                        f.write(comment.id + "\n")

                    print("Comment found!")

        #chouta
            for key in ["chouta"]:
                if WholeWord(key)(comment.body) and comment.id not in comments_skimmed and not comment.author == r.user.me() and pancake_num == 4:
                    chouta_quotes = [
                        "Chouta. Herdazian food, gon. Good stuff.",
                        "Chouta is love. Chouta is life.",
                        "Chouta are the best thing you can ever have, gon!",
                        "Journey before Chouta, gancho!",
                        "Penhito, the only acceptable use of chouta in a sentence is to praise it!"
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

        #Sazed, I think
            if ", i think." in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
                sazed_quotes = [
                    "Hey, gon, is this you Sazed?",
                    "Saze gancho! Good to see you here!",
                    "Wow, my gon Sazed is here!"
                ]

                comment.reply(">, I think. \n\n" + random.choice(sazed_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

                print("Sazed found!")

                if comment.id not in comments_skimmed and not comment.author == r.user.me():
                    comments_skimmed.append(comment.id) #Adds skimmed comments to list
                    with open("comments_skimmed.txt", "a", encoding='cp1252') as f:
                            f.write(comment.id + "\n")

    for comment in r.subreddit("Cremposting+Stormlight_Archive+Cosmere+Mistborn+brandonsanderson+Lopen_bot_test").comments(limit = 80):
        comment.refresh()
        #Coppermind function
        if "!coppermind" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
            text = comment.body.lower()
            text = text.split("!coppermind")[-1]

            if 'no tag' in text.lower():
                text = text.lower().split("no tag")[0].split()
                tag1 = ''
                tag2 = ''

            else:
                text = text.lower().split()
                tag1 = '>!'
                tag2 = '!<'

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
                            text_list.append(f'{tag1}{p.get_text()}{tag2}')
                            if not text_list[-1]:
                                del text_list[-1]

                        text = "***Warning Gancho: The below paragraph(s) may contain major spoilers for all books in the Cosmere!***\n\n" + "\n\n".join([f"{x}".replace("\n", "").strip() for x in text_list[:n+1]]) + tag2 + f"\n\n^[The article can be viewed here!]({doc})"

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

    #WOB function
        if "!wob" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
            text = comment.body.lower()
            text = text.split("!wob")[-1]

            if 'no tag' in text.lower():
                text = text.lower().split("no tag")[0].split()
                tag1 = ''
                tag2 = ''

            else:
                text = text.lower().split()
                tag1 = '>!'
                tag2 = '!<'
            try:
                try:
                    n = int(text[-1])
                    search = "+".join(text[:-1])

                except:
                    n = 5
                    search = "+".join(text)

                punc = '''!()[]{};:'"\,<>./?@#$%^&*~'''

                for ele in search:
                    if ele in punc:
                       search = search.replace(ele, "")

                if n > 8:
                    n = 8

                doc= f'https://wob.coppermind.net/adv_search/?query={search}'
                res = requests.get(doc)
                soup = BeautifulSoup(res.content, "html.parser")
                rows =soup.find_all('div',attrs={"class" : "entry-content"})[:n]
                ##      print(*rows, sep = "\n\n")

                text_list = []
                for tag in rows:
           ##                print(text_list)
                    for p in tag.find_all(['p', 'h4']):
                       text_list.append(f'{tag1}{p.get_text()}{tag2}')
                       if not text_list[-1]:
                            del text_list[-1]
                    text_list.append(f"************************************************************\n\n************************************************************")

                if len("\n\n".join([f"{x}".replace("\n", "").strip() for x in text_list])) > 9000:
                    special_tag = f'{tag2}\n\n[Incomplete WOB....]'
                else:
                    special_tag = ''

                text = "***Warning Gancho: The below paragraph(s) may contain major spoilers for all books in the Cosmere!***\n\n" + "\n\n".join([f"{x}".replace("\n", "").strip() for x in text_list])[:9000] + special_tag + f"\n\n^([All the WOBs can be viewed here!]({doc}))"

                comment.reply(text)
                print("WOB stuff")

            except:
                comment.reply(f"There are no WOBs for {search}. Check if you have made a spelling mistake, or if there is another name that might work.")
                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("WOB stuff not found.")

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")

        if 'wob.coppermind.net' in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():

            text = comment.body.lower()

            if '](' in comment.body:
                text = text.split('](')[1]

                doc_list = ['https://wob.coppermind.net/api/entry/' + doc2.split('#e')[1].split(')')[0] for doc2 in text if 'wob.coppermind.net' in doc2]

            else:
                try:
                    doc_list = ['https://wob.coppermind.net/api/entry/' + doc2.split('#e')[1] for doc2 in text.split() if 'wob.coppermind.net' in doc2]
                except:
                    print(comment.id)
                    doc_list = []

            if doc_list:
                text_list = []

                for doc in doc_list:
                    res = requests.get(doc)
                    soup = BeautifulSoup(res.content, "html.parser")

                    dic = json.loads(str(soup))

                    for n in range(len(dic['lines'])):
                        for line in dic['lines'][n].values():
                            text_list.append(f'>!{line.replace("<p>", "").replace("</p>", "")}!<')


                if text_list:
                    text = "***Warning Gancho: The below paragraph(s) may contain major spoilers for all books in the Cosmere!***\n\n" + "\n\n".join([f"{x}".replace("\n", "").strip() for x in text_list]) + f"\n\n^([All the WOBs can be viewed here!]({doc}))"

                    comment.reply(text)
            print("WOB stuff")

            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")

    for post in r.subreddit('Wetlanderhumor').new(limit = 10):
        if ("meming every chapter" in post.title.lower() or "memeing every chapter" in post.title.lower()) and any(map(str.isdigit, str(post.title))) and post.id not in posts_replied_to and post.author != r.user.me() and '478' not in post.title:
            post.reply(f"""Hey, ganchos, these are all the chapters memed till now:\n
[Parts 1 - 200](https://www.reddit.com/r/WetlanderHumor/comments/ppfuy7/meming_every_chapter_of_the_wheel_of_time_parts_1/?utm_source=share&utm_medium=web2x&context=3)\n
[Parts 201 - 399](https://www.reddit.com/r/WetlanderHumor/comments/ppfx07/meming_every_chapter_of_the_wheel_of_time_parts/?utm_source=share&utm_medium=web2x&context=3)\n
[Parts 400 and above](https://www.reddit.com/r/WetlanderHumor/comments/pzswww/meming_every_chapter_index_400_and_above/?utm_source=share&utm_medium=web2x&context=3)\n
To get link to a particular part, type '!meme (Part no.)', eg, !meme 200 will give you [this.](https://www.reddit.com/r/WetlanderHumor/comments/ls9y7j/meming_every_chapter_of_the_wheel_of_time_part_200/?utm_source=share&utm_medium=web2x&context=3)\n
^(I am a bot from r/cremposting, and I am here only to help my gon Scotsoe. I can't interact here otherwise.)""")

            meme_post = r.submission(id = 'pzswww')
            text = meme_post.selftext
            meme_post.edit(f'[{post.title}](https://www.reddit.com{post.permalink})\n\n' + text)

            print("Wetlander post found!")

            posts_replied_to.append(post.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
            with open("posts_replied_to.txt", "a", encoding='cp1252') as f:
                f.write(post.id + "\n")

    for comment in r.subreddit('Wetlanderhumor').comments(limit = 50):
        comment.refresh()

        if "!meme" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
            text = comment.body
            text = text.split("!meme")[-1]
            text = text.split()

            try:
                punc = '''!()-[]{};:'"\,<>./?@#$%^&*~'''

                for ele in text:
                    if ele in punc:
                        text = text.replace(ele, "")

                num = int(text[0])

                meme_text = r.submission(id='ppfuy7').selftext.split("\n") + r.submission(id='ppfx07').selftext.split("\n") + r.submission(id='pzswww').selftext.split("\n")

                post_links = []
                for element in meme_text:
                    element2 = element
                    for ele in element2:
                        if ele in punc:
                            element2 = element2.replace(ele, " ")

                    if str(num) in element2.split():
                        post_links.append(element)


                text_links = "\n\n".join(post_links)

                if text_links:
                    comment.reply("Hey, gon, I think this is what you are looking for\n\n" + text_links)

            except:
                comment.reply("Make sure you are using  the correct format, which is '!meme (part no.)' to produce a result.")

            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
            print("Meme sent!")

            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")

    print("Sleeping for a bit")
    time.sleep(240)  #Cool-down period

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

def get_mod_posts():

    if not os.path.isfile("mod_posts.txt"):

        mod_posts = []

    else:

        with open("mod_posts.txt", "r", encoding='cp1252') as f:
            mod_posts = f.read()
            mod_posts = mod_posts.split("\n")

    return mod_posts

def get_mod_comments():

    if not os.path.isfile("mod_comments.txt"):

        mod_comments = []

    else:

        with open("mod_comments.txt", "r", encoding='cp1252') as f:
            mod_comments = f.read()
            mod_comments = mod_comments.split("\n")

    return mod_comments

def get_mod_queue_posts():

    if not os.path.isfile("mod_queue_posts.txt"):

        mod_queue_posts = []

    else:

        with open("mod_queue_posts.txt", "r", encoding='cp1252') as f:
            mod_queue_posts = f.read()
            mod_queue_posts = mod_queue_posts.split("\n")

    return mod_queue_posts

def get_removed_comments():

    if not os.path.isfile("removed_comments.txt"):

        removed_comments = []

    else:

        with open("removed_comments.txt", "r", encoding='cp1252') as f:
            removed_comments = f.read()
            removed_comments = removed_comments.split("\n")

    return removed_comments

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
comments_replied_to2 = get_saved_comments()[-200:]
comments_skimmed = get_skimmed_comments()[-500:]
posts_replied_to = get_saved_posts()[-20:]
mod_posts = get_mod_posts()
mod_comments = get_mod_comments()
removed_comments = get_removed_comments()
mod_queue_posts = get_mod_queue_posts()

#cremrunner.to_csv("Ideals.csv", index = False)
#Sometimes the bot stops working while I am asleep, and remains down for hours.
#So, when it is up again, it will check 400 comments the first run to see if it missed anything, then 50 further on.
count = 0

while True:
    try:
        run_bot(r, comments_replied_to2, posts_replied_to, comments_skimmed, mod_comments, mod_posts, removed_comments, WholeWord, rank, count, mod_queue_posts)
        count = 1
    except:
        print("Error")
        time.sleep(240)
