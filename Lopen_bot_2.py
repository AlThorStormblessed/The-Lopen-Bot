#!/usr/bin/python

import praw
from config_lopen import *
import time
from praw.models import Comment, Submission

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

def run_bot(r):
    for crempost in r.subreddit('Cremposting').new(limit = 25):
        saved = [x.id for x in r.user.me().saved(limit = None) if isinstance(x, Submission)]

        if crempost.id not in saved and ("memeing every chapter" in crempost.title.lower() or "meming every chapter" in crempost.title.lower()):
            #Warbreaker
            redditor = r.redditor("AlThorStormblessed")

            posts = {}
            for post in redditor.submissions.new(limit = 1000):
                if "memeing every chapter" in post.title.lower() or "meming every chapter" in post.title.lower() and "Wheel of Time" not in post.title and "lopen friday" not in post.title.lower():
                    posts[post.title] = r.config.reddit_url + post.permalink

            wb_posts = "The list of chapters posted till now are (Some redos and alternate, coz my Creator is an idiot):\n\n"
            for item in posts.items():

                wb_posts += f"* [{item[0]}]({item[1]}) \n\n"

            redditor = r.redditor("The_Lopen_bot")

            for post in redditor.submissions.new(limit = 5):
                if "Meming every chapter list - Warbreaker" in post.title:
                    post.edit(wb_posts)


            #Stormlight Archive
            redditor = r.redditor("Anacanrock11")

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


            #Mistborn
            redditor = r.redditor("JeffSheldrake")

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

            #Elantris
            redditor = r.redditor("SpaghettiMaestro14")

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
                    post.edit(el_posts.replace("Six", '6'))


            aut = crempost.author
            if aut == "AlThorStormblessed":
                crempost.reply("[Meming every chapter - Warbreaker](https://redd.it/pks0ux/)")
            elif aut == "JeffSheldrake":
                crempost.reply("[Meming every chapter - Mistborn](https://redd.it/pkrvjy/)")
            elif aut == "Anacanrock11":
                crempost.reply("[Meming every chapter - Stormlight Archive](https://redd.it/pkrqeg/)")
            elif aut == "SpaghettiMaestro14":
                crempost.reply("[Meming every chapter - Elantris](https://redd.it/pkrxrw/)")

            crempost.save()


    print("Sleeping for a bit")
    time.sleep(600)  #Cool-down period


#Running the functions
r = bot_login()


while True:
    try:
        run_bot(r)
    except:
        print("Error")
        time.sleep(120)
