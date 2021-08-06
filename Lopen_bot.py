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
                kaladin_quotes = [
                    "[WOR spoilers] >!Honor is dead. But I'll see what I can do.!<",
                    "The only time you seem honest is when you’re insulting someone!",
                    "I fell face-first, sir, and fortunately, I’m particularly hard-headed.",
                    "[WOR spoilers] >!Fleet couldn't win, but he kept running. And when the storm caught him, it didn't matter that he’d died, because he’d run for all he had.!<",
                    "[WOR spoilers] >!We all die in the end, you see, so I guess what truly matters is just how well you've run. And Elhokar, you've kept running since your father was killed, even if you screw up all the storming time.!<",
                    "It would be more beautiful if it hadn't tried to eat me.",
                    "If you’re only now learning that, then you haven’t been paying attention.",
                    "I've never been an optimist. I see the world as it is, or try to. That's a problem, though, when the truth I see is so terrible.",
                    "I see good lots of days. Trouble is, on the bad days, that is hard to remember. At those times, for some reason, it feels like I have always been in that darkness, and always would be.",
                    "I’d rather walk these chasms with a compulsive murderer than you. At least then, when the conversation got tedious, I’d have an easy way out.",
                    "Is it really this hard for you to let me win one single argument?",
                    "*Grunt*",
                    "**Scowls**",
                    "**Glowers**",
                    "Scared to go onward, but terrified to go back to what you were",
                    "[WOR spoilers] >!I will protect even those I hate, so long as it is right.!<",
                    "[WOK spoilers] >!I will protect those who cannot protect themselves.!<",
                    "[WOR spoilers] >!The Knights Radiant... have returned.!<",
                    "[WOR spoilers] >!The sky and the winds are mine. I claim them, as I now claim your life.!<",
                    "Authority doesn't come from a rank. It come from the men who give it to you. That's the only way to get it.",
                    "[WOK spoilers] >!You were not shocked when a child knew how to breathe. You were not shocked when a skyeel took flight for the first time. You should not be shocked when you hand Kaladin Stormblessed a spear and he knows how to use it.!<",
                    "If the afterlife really is a big war, then I hope I end up in Damnation. At least there I might be able to get a wink or two of sleep.",
                    "[WOR spoilers] >!What else could he do? Explain to Adolin? Yes, princeling. I let your betrothed wander off alone in the darkness to get eaten by a chasmfiend. No, I didn't go with her. Yes, I'm a coward.!<",
                    "It's horribly unfair you managed that on your first try. It took me forever.",
                    "There had been something more they could do to me. One final torment the world had reserved just for Kaladin. And it was called Bridge Four.",
                    "My father used to say that there are two kinds of people in the world. He said there are those who take lives. And there are those who save lives.",
                    "There are people who exist to be saved or to be killed. The group in the middle. The ones who can't do anything but die or be protected. The victims. That's all I am.",
                    "It's horribly unfair you managed that on your first try. It took me forever.",
                    "Doesn't that bother you? That you might be a creation of human perception?",
                    "Madness is worse than normal. It really just depends on the people around you. How different are you from them? The person that stands out is mad, I guess.",
                    "[WOK spoilers] >!The world just changed, Gaz. I died down at that chasm. Now you've got my vengeful spirit to deal with.!<",
                    "We exist to be killed. If we're not dead already.",
                    "Combat begins with the legs. I don't care how fast you are with a jab, how accurate you are with a thrust. If your opponent can trip you, or make you stumble, you'll lose. Losing means dying.",
                    "Amaram and Sadeas. Two men in my life who would, at some point, need to pay for the things they'd done.",
                    "Some people - like a festering finger or a leg shattered beyond repair - just needed to be removed.",
                    "Breath. A man's breath was his life. Exhaled, bit by bit, back into the world.",
                    "Giving up all pretense of obeying natural laws again, I see.",
                    "I won't stand there and watch while men die behind me. We have to be better than that! We can't look away like the lighteyes, pretending we don't see. This man is one of us.",
                    "The lighteyes talk about honor. They spout empty claims about their nobility. Well, I've only known one man in my life who was a true man of honor. He was a surgeon who would help anyone, even those who hated him. Especially those who hated him.",
                    "There was no sin greater than the betrayal of one's allies in battle. Except, perhaps, for the betrayal of one's own men - of murdering them after they risked their lives to protect you",
                    "The Almighty was supposed to be able to see all and know all. So why did he need a prayer to be burned before he would do anything? Why did he need people to fight for him in the first place?",
                    "I hoped for something else. Hoped. Yes, I'd discovered that I could still hope. A spear in my hands. An enemy to face. I could live like that.",
                    "[OB spoilers] >!Ten spears go to battle, and nine shatter. Did the war forge the one that remained? No, Amaran. All the war did was identify the spear that would not break.!<"
                ]

                mess = random.choice(["\n\n^(These words of Kaladin's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Kaladin, brought by Lopen's cousins)",
                "\n\n^(Speak further to Kaladin by mentioning !Kaladin in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(kaladin_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

            elif lms_key == "!shallan":
                shallan_quotes = [
                    "The only honest things I can say to you are insults.",
                    "Words are where most change begins.",
                    "Funny. I thought I'd run straight into sarcasm, screaming at the top of my lungs.",
                    "Remind me to try to kill you once in a while. If I succeed, it will make me feel better, and if I fail, it will make you feel better. Everyone wins!",
                    "The world isn't fair? What a huge revelation! Some people in power abuse those they have power over? Amazing! When did this start happening?",
                    "Expectation isn't just about what people expect of you. It is about what you expectof yourself.",
                    "Are you that afraid of being wrong? One would assume you’d be accustomed to it by now.",
                    "The last thing I’d want to do is accidentally insult you, Vathah. To think that I couldn’t manage it on purpose if I wanted!",
                    "I am offend!",
                    "No apologize! Boots!",
                    "But you could be fire.",
                    "It’s not a lie, if everyone understands and knows what it means.",
                    "I seek the truth. Wherever it may be, whoever may hold it. That’s who I am.",
                    "Ah,the outdoors. I visited that mythical place once. It was so very long ago, I've nearly forgotten it. Tell me, does the sun still shine, or is that just my dreamy recollection?",
                    "Your feet stink. See? Too early. I can’t possibly be witty at this hour. So no arguments [...] Besides, no murderer would agree to accompany you. Everyone needs to have some standards, after all.",
                    "The sensation—it’s not sorrow, but something deeper—of being broken. Of being crushed so often, and so hatefully, that emotion becomes something you can only wish for. If only you could cry, because then you’d feel something. Instead, you feel nothing. Just . . . haze and smoke inside. Like you’re already dead.",
                    "Perhaps I am an insensitive rich woman. That doesn't change the fact that you can be downright mean and offensive, Kaladin Stormblessed.",
                    "It is beautiful because it could have been. It should have been.",
                    "I probably shouldn't mock our family. House Davar is distinctive and enduring. [...] Of course, the same could be said for a wart.",
                    "You aren't what you think yourselves to be.",
                    "I know. I'm ignorant. There's a simple cure for that.",
                    "Practice. I should suspect that is how everyone learns, eventually.",
                    "It frightens me, because we all see the world by some kind of light personal to us, and that light changes perception. I don't see clearly. I want to, but I don't know if I ever truly can.",
                    "I've never actually had someone's tongue on me, clever or not. I'd hazard to consider it an unpleasant experience.",
                    "I don’t want revenge. I want my family.",
                    "Now go to sleep in Chasms deep, with darkness all around you..."
                    ]

                mess = random.choice(["\n\n^(These words of Shallan's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Shallan, brought by Lopen's cousins)",
                "\n\n^(Speak further to Shallan by mentioning !Shallan in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(shallan_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

            elif lms_key == "!adolin":
                adolin_quotes = [
                    "[WOR spoilers] >!Well, there was no need to be barbaric, just because I was incarcerated.!<",
                    "I’m refined, you insolent farmer. Besides, I’ll have you know that I had to use cold water for my baths while here.",
                    "What are you doing here, bridgeboy?",
                    "People think I know a lot about women. The truth is, I know how to get them, how to make them laugh, how to make them interested. I don't know how to keep them. I really want to keep this one.",
                    "Of course. He’s probably their leader now or something. Storming bridgeboy.",
                    "I, Adolin Kholin, cousin to the king, heir to the Kholin princedom, have shat myself in my shardplate. Three times. All on purpose.",
                    "Rudeness doesn't necessarily imply untruth.",
                    "I don't think Shallan is as weak as you say. Weakness doesn't make someone weak, you see. It's the opposite",
                    "Never underestimate the worth of being willing to hold. Your. GROUND.",
                    "If she's so precious, maybe you all could listen to her once in a while.",
                    "Words like 'eternal' and 'forever' aren't as definitive as you all pretend.",
                    "Maybe there are more than two choices in life. Maybe I'm my own brand of wrong.",
                    "[ROW spoilers] >!You're Alethkar's most eligible bachelor. Shardbearer, Radiant, Landed, and single?!<",
                    "You don't have to smile. You don't have to talk. But if you're going to to be miserable, you might as well do it with friends.",
                    "Welcome to the party.",
                    "I owe you my life. That's the only reason I haven't yet thrown you through a window.",
                    "[WOK spoilers] >!We walked right into this We let him take away our bridges. We let him get us onto the plateau before the second wave of Parshendi arrived. We let him control the scouts. We even suggested the attack pattern that would leave us surrounded if he didn't support us!!<",
                    "What you see is not real. Your life now is a rationalization, a way of trying to pretend that what's happening isn't happening. But I'll go to Damnation itself before I'll let you drag the entire house down without speaking my mind on it!",
                    "I know it's hard to accept, but sometimes, people get old. Sometimes, the mind stops working right.",
                    "This might be our last fight together. I appreciate what you've done for me. I know you'd do it for anyone who held you, but I still appreciate it."
                ]

                mess = random.choice(["\n\n^(These words of Adolin's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Adolin, brought by Lopen's cousins)",
                "\n\n^(Speak further to Adolin by mentioning !Adolin in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(adolin_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

            elif lms_key == "!stormfather" or lms_key == "!stormdaddy":
                stormfather_quotes = [
                    "WHY HAVE YOU SUMMONED ME, MORTAL?",
                    "[OB spoilers] >!I AM HIS ... SPREN, YOU MIGHT SAY. NOT HIS SOUL. I AM THE MEMORY MEN CREATE FOR HIM, NOW THAT HE IS GONE. THE PERSONIFICATION OF THE STORMS AND OF THE DIVINE. I AM NO GOD. I AM BUT A SHADOW OF ONE.!<",
                    "I RESPECT ALL OATHS",
                    "There are no foolish oaths. All are the mark of men and true spren over beasts and subspren. The mark of intelligence, free will, and choice.".upper(),
                    "I am that which brings Light and Darkness.".upper(),
                    "I have burned and broken cities myself. I can see … yes, I see a difference now. I see pain now. I did not see it before the bond".upper(),
                    "I am a sliver of the Almighty himself!".upper(),
                    "[OB spoilers] >!I will not be a simple sword to you. I will not come as you call, and you will have to divest yourself of that... monstrosity that you carry. You will be a Radiant with no Shards.!<".upper(),
                    "[OB spoilers] >!During these days, Honor still lived. I was not yet fully myself. More of a storm. Less interested in men.!<".upper(),
                    "Oaths are the soul of righteousness. If you are to survive the coming tempest, oaths must guide you.".upper(),
                    "SON OF HONOR.",
                    "[OB spoilers] >!This is the lot I have chosen. It is you or oblivion.!<".upper(),
                    "[OB spoilers] >!I was bonded to men before. This never happened then.!<".upper(),
                    "Of course Honor's suggestion would work. He spoke it.".upper(),
                    "You have taken her from me. My beloved one.".upper(),
                    "[WOR spoilers] >!A daughter disobeys!<".upper(),
                    "YES?"
                ]

                mess = random.choice(["\n\n^(These words of Stormfather's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Stormfather, brought by Lopen's cousins)",
                "\n\n^(Speak further to Stormfather by mentioning !Stormfather in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(stormfather_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

            elif lms_key == "!taln":
                taln_quotes = [
                    "I am Talenel'Elin, Herald of War. The time of the Return, the Desolation, is near at hand. We must prepare. You will have forgotten much, following the destruction of the times past. Kalak will teach you to cast bronze, if you have forgotten this. We will Soulcast blocks of metal directly for you. I wish we could teach you steel, but casting is so much easier than forging, and you must have something we can produce quickly. Your stone tools will not serve against what is to come. Vedel can train your surgeons, and Jezrien . . . he will teach you leadership. So much is lost between Returns . . . I will train your soldiers. We should have time. Ishar keeps talking about a way to keep information from being lost following Desolations. And you have discovered something unexpected. We will use that. Surgebinders to act as guardians . . . Knights . . . The coming days will be difficult, but with training, humanity will survive. You must bring me to your leaders. The other Heralds should join us soon."
                ]

                mess = random.choice(["\n\n^(These words of Taln's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Taln, brought by Lopen's cousins)",
                "\n\n^(Speak further to Taln by mentioning !Taln in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(taln_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

            elif lms_key == "!syl":
                syl_quotes = [
                    "You don't fly, you fall the wrong way.",
                    "Humans don’t make sense.",
                    "I'm not odd! I'm beautiful and articulate",
                    "[WOR spoilers] >!YOU CANNOT HOLD ME BACK IF HE SPEAKS THE WORDS! THE WORDS, KALADIN! SAY THEM!!<",
                    "Do you like the new dress? I'll have you know, I put a *ton* of thought into it. I spent positively *hours* thinking of just how - Oh! What's that?",
                    "Syl. That’s amusing. It appears that I have a nickname.",
                    "Nonsense! Why would I leave my babies in a drawer? Far too boring. A highprince’s shoe though…",
                    "He hasn't said how amazing I am all morning!",
                    "I am intelligent and articulate. You should compliment me now.",
                    "You worry like a worrier.",
                    "It is my solemn and important duty to bring happiness, light, and joy into your world.",
                    "What is one more try then?",
                    "Aladar's axehounds had puppies. I had no idea how much I needed to see puppies until I flew by them this morning. They are the grossest things on the planet, Kaladin. They're somehow so gross that they're cute. So cute I could have died! Except I can't, because I'm an eternal sliver of God himself, and we have standards about things like that.",
                    "[WOK spoilers] >!I bind things, Kaladin. I am honorspren. Spirit of oaths. Of promises. And of nobility!<",
                    "[WOK spoilers] >!I'm behind what is happening to you. I'm doing it. It's both of us. But without me, nothing would be changing in you. I'm . . . taking something from you. And giving something in return.!<",
                    "It seems that if you're worried about hurting people, you shouldn’t be afraid to help the bridgemen. What more could you do to them?",
                    "Something dangerous is coming.",
                    "[WOR spoilers >!Kaladin! Stretch forth thy hand!!<",
                    "You'd better catch me before I scamper away! Wow! I’m feeling capricious today. I might just vanish again, off to where nobody can find me!",
                    "How can you tell? I don’t think he ever gets excited. Not even when I tell him I have a fun surprise for him.",
                    "I am a god. A little piece of one.",
                    "Everyone is connected, Kaladin. Everything is connected. I didn't know you then, but the winds did, and I am of the winds.",
                    "The winds are of Honor. We are kindred blood",
                    "[WOR spoilers] >! ... I don't smash into things. I am an elegant and graceful weapon, stupid.!<",
                    "I don't know, it just feels wrong to me. I hate it. I'm glad he got rid of it. Makes him a better man."
                    ]

                mess = random.choice(["\n\n^(These words of Syl's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Syl, brought by Lopen's cousins)",
                "\n\n^(Speak further to Syl by mentioning !Syl in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(syl_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

            elif lms_key == "!pattern":
                pattern_quotes = [
                    "Insults in particular will be of great use to my people, as they are truths and lies combined in a quite interesting manner.",
                    "I know ... little of humans. They break. Their minds break. You did not break. Only cracked.",
                    "It is the lies that save you. The lies that drew me.",
                    "I find sleeping very odd. I know that all beings in the Physical Realm engage in it. Do you find it pleasant? You fear nonexistence, but is not unconsciousness the same thing?",
                    "Ah. It is all right, because in the morning, you each return to sentience.",
                    "[WOR spoilers] >!Shallan. I know that you have forgotten much of what once was. Those lies attracted me. But you cannot continue like this; you must admit the truth about me. About what I can do, and what we have done. Mmm ... More, you must know yourself. And remember.!<",
                    "[WOR spoilers] >!You wish to help. You wish to prepare for the Everstorm, the spren of the unnatural one. You must become something. I did not come to you merely to teach you tricks of light.!<",
                    "I came to learn. We became to do something greater.",
                    "[WOR spoilers] >!Mmmm ... Such a deep lie. A deep lie indeed. But still, you must obtain your abilities. Learn again if you have to.!<",
                    "Lightweavers make no oaths beyond the first ... . You must speak truths.",
                    "Mmmmmmmmmmmmmmmmmmmm...",
                    "Mmm... delicious lies.",
                    "NO MATING",
                    "You are not as good with patterns... You are abstract. You think in lies and tell them to yourselves. That is fascinating, but it is not good for patterns.",
                    "My memory is weak. I was dumb so long, nearly dead. Mmm. I could not speak.",
                    "I will not stop vibrating. The wind will not stop blowing. You will not stop drawing.",
                    "Truth is individual. Your truth is what you see. What else could it be? That is the truth that you spoke to me, the truth that brings power.",
                    "Humans can see the world as it is not. It is why your lies can be so strong. You are able to not admit that they are lies.",
                    "I’m sorry that your mystical, godlike powers do not instantly work as you would like them to.",
                    "You live lies. It gives you strength. But the truth . . . Without speaking truths you will not be able to grow, Shallan.",
                    "You were talking about mating! I’m to make sure you don’t accidentally mate, as mating is forbidden by human society until you have first performed appropriate rituals! Yes, yes. Mmmm. Dictates of custom require following certain patterns before you copulate. I’ve been studying this!",
                    "That’s not enough. I must know something true about you. Tell me. The stronger the truth, the more hidden it is, the more powerful the bond. Tell me. Tell me. What are you??",
                    "Terrible destruction to eat!",
                    "Know you nothing of Patterns, old human? Voidbringers have no pattern. Besides, I have read of them in your lore. They speak of spindly arms like bone, and horrific faces. I should think, if you wish to find one, the mirror might be a location where you can begin your search.",
                    "Good lies... True lies... Light makes shadow. Truth makes lies.",
                    "Spren are... power... shattered power. Power given thought by the perceptions of men. Honor, Cultivation, and . . . and another. Fragments broken off.",
                    "Sapience. Thought. Life. These are of humans. We are ideas. Ideas that wish to live.",
                    "Inappropriate? Such as...dividing by zero?",
                    "The fundamental underlying mathematics by which natural phenomena occur. Mmm. Truths that explain the fabric of existence.",
                    "Yes. Seven people. Odd."
                 ]

                mess = random.choice(["\n\n^(These words of Pattern's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Pattern, brought by Lopen's cousins)",
                "\n\n^(Speak further to Pattern by mentioning !Pattern in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(pattern_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

            elif lms_key == "!dalinar" or lms_key == "!dadinar":
                dalinar_quotes = [
                    "Sometimes a hypocrite is nothing more than a man in the process of changing.",
                    "[OB spoilers] >!To love the journey is to accept no such end. I have found, through painful experience, that the most important step a person can take is always the next one.!<",
                    "[OB spoilers] >!The most important step a man can take. It's not the first one, is it? It's the next one. Always the next step, Dalinar!<",
                    "[OB spoilers] >!I will take responsibility for what I have done. If I must fall, I will rise each time a better man.!<",
                    "[OB spoilers] >!The most important words a man can say are, “I will do better.” These are not the most important words any man can say. I am a man, and they are what I needed to say.",
                    "The ancient code of the Knights Radiant says “journey before destination.” Some may call it a simple platitude, but it is far more. A journey will have pain and failure. It is not only the steps forward that we must accept. It is the stumbles. The trials. The knowledge that we will fail. That we will hurt those around us.",
                    "But if we stop, if we accept the person we are when we fall, the journey ends. That failure becomes our destination. To love the journey is to accept no such end. I have found, through painful experience, that the most important step a person can take is always the next one.",
                    "[OB spoilers] >!I’m certain some will feel threatened by this record. Some few may feel liberated. Most will simply feel that it should not exist. I needed to write it anyway.!<",
                    "Yes, I began my journey alone, and I ended it alone. But that does not mean that I walked alone.",
                    "But merely being tradition does not make something worthy, Kadash. We can't just assume that because something is old it is right.",
                    "[OB spoilers] >!YOU CANNOT HAVE MY PAIN!!<",
                    "[OB spoilers] >!I am Unity!<",
                    "A man’s emotions are what define him, control is the hallmark of true strength. To lack feeling is to be dead, but to act on every feeling is to be a child.",
                    "If I should die, then I would do so having lived my life right. It is not the destination that matters, but how one arrives there.",
                    "Sometimes the prize is not worth the costs. The means by which we achieve victory are as important as the victory itself.",
                    "A leader did not slump. A leader was in control. Even when he least felt like he controlled anything. Especially then.",
                    "Something is either right, or it's wrong. The Almighty doesn't come into it.",
                    "[OB spoilers] >!I will unite instead of divide.!<",
                    "I will unite them",
                    "I'm a man of extremes, Navani. I discovered that when I was a youth. I’ve learned, repeatedly, that the only way to control those extremes is to dedicate my life to something.",
                    "I have spent too much of my time worrying about what people think, Navani. When I thought my time had arrived, I realized that all my worrying had been wasted. In the end, I was pleased with how I had lived my life.",
                    "I assumed I was dreaming myself, when I saw the first vision. When they kept happening, I was forced to acknowledge that no dream is this crisp, this logical. In no dream could we be having this conversation.",
                    "We looked at this place here, this kingdom, and we realized, 'Hey, all these people have stuff .' And we figured ... hey, maybe we should have that stuff. So we took it.",
                    "May you have your father’s strength, and at least some of your mother’s compassion, little one",
                    "[OB spoilers] >!I intend to so thoroughly ruin this place that for ten generations, nobody will dare build here for fear of the spirits who will haunt it. We will make a pyre of this city, and there shall be no weeping for its passing, for none will remain to weep.!<",
                    "[WOR spoilers] >!Where is your Honor?!<",
                    "[WOK spoilers] >!Well, you've shown me something today, Sadeas – shown it to me by the very act of trying to remove me. . . You've shown me that I'm still a threat.!<",
                    "[WOK spoilers] >!I'll have us be what we were before, son. A kingdom that can stand through storms, a kingdom that is a light and not a darkness. I will have a truly unified Alethkar, with highprinces who are loyal and just. I'll have more than that. I'm going to refound the Knights Radiant.!<",
                    "[WOR spoilers] >!I will unite instead of divide, Stormfather. I will bring men together.!<",
                    "[OB spoilers] >!Old friend, Honor might be dead, but I have felt … something else. Something beyond. A warmth and a light. It is not that God has died, it is that the Almighty was never God.!<",
                    "[OB spoilers] >!Maybe you're right, and I am a tyrant! Maybe letting my armies into your city is a terrible risk. But maybe you don’t have good options! Maybe all the good men are dead, so all you have is me! Spitting into the storm isn’t going to change that, Fen. You can risk possibly being conquered by the Alethi, or you can definitely fall to the Voidbringer assault alone!!<",
                    "I don’t want your life, son, I don’t want your city or your kingdom. If I’d wanted to conquer Thaylenah, I wouldn’t offer you a smiling face and promises of peace. You should know that much from my reputation.",
                    "[OB spoilers] >!Shardbearers can't hold ground. [...] Fen, I have Radiants, yes—but they, no matter how powerful, won’t win this war. More importantly, I can’t see what I’m missing. That’s why I need you.!<",
                    "Oh, Ruthar, you can't win this fight. Jasnah has thought about the topic far more than you have. It’s a familiar battleground to her.",
                    "This is what you feared, a world that turns not upon force of armies, but upon the concerns of scribes and bureaucrats.",
                    "The enemy brought a very big stick to this battle, Captain. I'm going to take it away.",
                    "[WOK spoilers] >!So today, you and your men sacrificed to buy me twenty-six hundred priceless lives. And all I had to repay you with was a single priceless sword. I call that a bargain.!<",
                    "[WOK spoilers] >!I have been treating the other highprinces and their lighteyes like adults. An adult can take a principle and adapt it to his needs. But we're not ready for that yet. We're children. And when you're teaching a child, you require him to do what is right until he grows old enough to make his own choices.!<",
                 ]

                mess = random.choice(["\n\n^(These words of Dalinar's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Dalinar, brought by Lopen's cousins)",
                "\n\n^(Speak further to Dalinar by mentioning !Dalinar in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(dalinar_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

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

            elif lms_key == "!rock" or lms_key == "!numuhukumakiaki'aialunamor":
                rock_quotes = [
                    "Airsick lowlanders.",
                    "[OB spoilers] >!We take to the skies, Stormblessed.!<",
                    "Rlain, is okay to throw things at Eth.",
                    "Take everything you have, and put him in pot. Don't let anyone airsick touch spices.",
                    "[WOK spoilers] >!Actually, I put this thing in his bread too. And used it as a garnish on the pork steak. And made a chutney out of it for the buttered garams. Chull dung, it has many uses, I found.!<",
                    "I think, your problem is different than you say. You claim you are not the person everyone thinks you are. Maybe you worry, instead, that you are that person.",
                    "It was small tree and very hard head.",
                    "I will fix two things. One for the brave and one for the silly. You may choose between these things.",
                    "Airsick lowlanders. Too much air makes your brain sick.",
                    "You are all still my family, just the dumb ones.",
                    "On top, is water. Beneath, is not. Is something else. Water of life. The place of the gods. This thing is true. I have met a god myself.",
                    "No complaining today. You do this thing too much. Do not make me kick you. I do not like kicking. It hurts my toes.",
                    "What are you doing, crazy man! Lazbo? In drink? That thing is spicy powder, airsick lowlander!",
                    "You are lucky man. I will not kill you today.",
                    "Finding a smile on your face, Kaladin Stormblessed, is like finding lost sphere in your soup.",
                    "This thing we have begun, it is still war. Men will die.",
                    "Today is not day for sad stories. Today is day for laughter, stew, flight. These things.",
                    "[WOR spoilers] >!Truthwatcher! Is good name. More people should watch truth, instead of lies.!<",
                    "Everyone thinks I am loud, insufferable lout! So to be something else would not be bad thing.",
                    "You can admit you act and think differently from your brother, but can learn not to see this as flaw.",
                    "Do not look so self-satisfied. I may still throw you off side of plateau.",
                    "These are wise words. I am not sure why yet. I will have to ponder them.",
                    "[OB spoilers] >!Next son is Rock, but not same kind of Rock as me. This is . . . um . . . smaller Rock.!<",
                    "The last time, we march not toward death, but toward full stomachs and good songs!",

                ]

                mess = random.choice(["\n\n^(These words of Rock's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Rock, brought by Lopen's cousins)",
                "\n\n^(Speak further to Rock by mentioning !Rock in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(rock_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

            elif lms_key == "!jasnah":
                jasnah_quotes = [
                    "Congratulations. Should I need someone to write a treatise on their stuffed pony or give an account of an interesting pebble they discovered, I shall send for you.",
                    "Ignorance is hardly unusual, Miss Davar. The longer I live, the more I come to realize that it is the natural state of the human mind. There are many who will strive to defend its sanctity and then expect you to be impressed with their efforts.",
                    "...a woman's mind is her most precious weapon. It must not be employed clumsily or prematurely. Much like the aforementioned knife to the back, a clever gibe is most effective when it is unanticipated.",
                    "Youthful immaturity is one of the cosmere’s great catalysts for change... To be young is about action. To be a scholar is about informed action.",
                    "Too many scholars think of research as purely a cerebral pursuit. If we do nothing with the knowledge we gain, then we have wasted our study. Books can store information better than we can—what we do that books cannot is interpret. So if one is not going to draw conclusions, then one might as well just leave the information in the texts. ",
                    "I always forgive curiosity, Your Majesty. It strikes me as one of the most genuine of emotions.",
                    "A true scholar must not close her mind on any topic, no matter how certain she may feel. Just because I have not yet found a convincing reason to join one of the devotaries does not mean I never will. Though each time I have a discussion like the one today, my convictions grow firmer.",
                    "When we are young, we want simple answers. There is no greater indication of youth, perhaps, than the desire for everything to be as it should. As it has ever been.",
                    "The older we grow, the more we question. We begin to ask why. And yet, we still want the answers to be simple. We assume that the people around us—adults, leaders—will have those answers. Whatever they give often satisfies us.",
                    "It seems to me that aging, wisdom, and wondering are synonymous. The older we grow, the more likely we are to reject the simple answers. Unless someone gets in our way and demands they be accepted regardless.",
                    "You will find wise men in any religion, Shallan, and good men in every nation. Those who truly seek wisdom are those who will acknowledge the virtue in their adversaries and who will learn from those who disabuse them of error. All others—heretic, Vorin, Ysperist, or Maakian—are equally closed-minded.",
                    "Let the Vorin believe as they wish—the wise among them will find goodness and solace in their faith; the fools would be fools no matter what they believed.",
                    "Power is an illusion of perception...Some kinds of power are real -- power to command armies, power to soulcast. These come into play far less often than you would think.",
                    "Most threats to a dynasty came from within.",
                    "A woman's strength should not be in her role, whatever she chooses to be, but in the power to choose that role.",
                    "You came up on deck,” Jasnah said, “to sketch pictures of young men working without their shirts on. You expected this to help your concentration?",
                    "Control is the basis of all true power. Authority and strength are matters of perception.",
                    "I say that there is no role for women - there is, instead, a role for each woman, and she must make it for herself.",
                    "It is important to be rational at all times, not just when calm.",
                    "Then we shall do an evaluation. Answer truthfully and do not exaggerate, as I will soon discover your lies. Feign no false modesty, either. I haven't the patience for a simperer.",
                    "Does one deserve to have evil done to her by consequence of putting herself where evil can reach her?",
                    "Just because I do not accept the teachings of the devotaries does not mean I’ve discarded a belief in right and wrong.",
                    "Must someone, some unseen thing, declare what is right for it to be right? I believe that my own morality -- which answers only to my heart -- is more sure and true than the morality of those who do right only because they fear retribution.",
                    "A fool is a person who ignored information because it disagreed with desired results.",
                    "United, new beginnings sing: \"Defying truth, love, Truth defy!\" Sing beginnings, new unity.",
                    "*Harsher*",
                    "Sometimes we find it hardest to accept in others that which we cling to in ourselves.",
                    "I know what people say of me. I should hope that I am not as harsh as some say, though a woman could have far worse than a reputation for sternness. It can serve one well.",
                    "All things have three components: the soul, the body, and the mind.",
                    "Unless I were a pig. Then you’d be doubly interested.",
                ]

                mess = random.choice(["\n\n^(These words of Jasnah's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                "\n\n^(-Jasnah, brought by Lopen's cousins)",
                "\n\n^(Speak further to Jasnah by mentioning !Jasnah in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(jasnah_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")


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

            comment.reply(list)

            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
            print("Comment found!")

        if "!function" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
            functions = "Hey, there, Gon, you wanted to know what I can do? Well, here you go!\n\
\n\
1. **Lopen Insult**: Reply to any message which I haven't replied to, and I will arrive to insult the penhito. I am no Wit, but I would bet an arm that I can make them cry!\n\
\n\
2. **Lopen Joke**: Want a nice joke, moolie? Summon me by commenting 'Lopen joke(s)' or 'One armed Herdazian' anywhere on the sub for a good laugh!\n\
\n\
3. **Spoiler tag system**: The Lopen likes surprises. Don't ruin surprises for others by using incorrect spoiler tags, lest you want to face my wrath! [For more information, check out this post](https://www.reddit.com/user/jofwu/comments/eo4rhu/how_to_cover_spoilers_in_posts_and_comments/?utm_source=share&utm_medium=web2x&context=3)\n\
\n\
4. **Quotes and usual summons**: Just say my name to get a quote from the King of Alethkar himself! Nicknames like gancho, penhito and gon work too!\n\
\n\
5. **Lopen Messaging System**: I got my many cousins to agree upon bring you messages from my fellow ganchos! Just type !(character name) to bring out a nice quote, provided by the LMS. For the entire list of characters (*work in progress*) comment '!list'.\n\
\n\
6. **Swear counter**: Call the Lopen with !swear to find out if you have been using crem-filled language lately!\n\
\n\
7. **Do not call me merely Lopen**: I am *the* Lopen, not some mere *a* Lopen. Remember that."

            comment.reply(functions)

            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
            print("Comment found!")


    #Witty stuff
        if "!wit" in comment.body.lower() and comment.id not in comments_replied_to2:
            #Quotes
            if not WholeWord("insult")(comment.body) and comment.author != r.user.me():
                wit_quotes = [
                    "Yes, yes. Aim for the sun. That way if you miss, at least your arrow will fall far away, and the person it kills will likely be someone you don’t know.",
                    "Like a fashionable dress, stupidity can be fetching in youth, but looks particularly bad on the aged. And unique as its properties may be, stupidity is frighteningly common. The sum total of stupid people is somewhere around the population of the planet. Plus one.",
                    "[I know] almost everything. That almost part can be a real kick in the teeth sometimes.",
                    "Two what, Dalinar? Eyes, hands, or spheres? I’d lend you one of the first, but — by definition — a man can only have one I, and if it is given away, who would be Wit then? I’d lend you one of the second, but I fear my simple hands have been digging in the muck far too often to suit one such as you. And if I gave you one of my spheres, what would I spend the remaining one on? I’m quite attached to both of my spheres, you see. Or, well, you can’t see. Would you like to?"
                    "A bunny rabbit and a chick went frolicking in the grass together on a sunny day. [...] Sorry. Let me make it more appropriate for you. A piece of wet slime and a disgusting crab thing with seventeen legs slunk across the rocks together on an insufferably rainy day. Is that better?",
                    "What is it we value? Innovation. Originality. Novelty. But most importantly...timeliness. I fear you may be too late, my confused, unfortunate, friend.",
                    "[Mild ROW spoilers] >!This is a dog. They’re fluffy and loyal and wonderful.!<",
                    "[OB spoilers] >!I have bonded a literal monster!<",
                    "If the Wit is a fool, then it is a sorry state for men. I shall offer you this Sadeas. If you speak, yet say nothing ridiculous, I will leave you alone for the rest of the week.",
                    "What of you, young Prince Renarin? Your father wishes me to leave you alone. Can you speak, yet say nothing ridiculous?",
                    "You’re all of them, Shallan. Why must you be only one emotion? One set of sensations? One role? One life?",
                    "Then be ruled as a king is ruled by his subjects. Make Shallan so strong, the others must bow.",
                    "[ROW spoilers] >!It will [get worse] but then it will get better. Then it will get worse again. Then better. This is life, and I will not lie by saying every day will be sunshine. But there will be sunshine again, and that is a very different thing to say. That is truth. I promise you, Kaladin: You will be warm again.!<",
                    "I like to live every day like it's my last. And by that I mean lying in a puddle of my own urine, calling for the nurse to bring me more pudding.",
                    "Two blind men waited at the end of an era, contemplating beauty. They sat atop the world's highest cliff, overlooking the land and seeing nothing",
                    "I began life as a thought, a concept, words on a page. That was another thing I stole. Myself.",
                    "*Giggles like a child*",
                    "The longer you live, the more you fail. Failure is the mark of a life well lived. In turn, the only way to live without failure is to be of no use to anyone. Trust me, I've practiced.",
                ]

                mess = random.choice(["\n\n^(These words of Wit's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                    "\n\n^(-Wit, brought by Lopen's cousins)",
                    "\n\n^(Speak further to Wit by mentioning ! Wit in your comments. Anytime, anywhere. LMS)"])

                list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                comment.reply(random.choice(wit_quotes) + mess + list_of) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
                print("Comment found!")

            else:
                if WholeWord("lopen")(comment.body):
                    insult_num = random.randint(1, 2)

                else:
                    insult_num = 1

                if insult_num == 1:
                    parent = comment

                    wit_insult = [
                        "The sum total of stupid people is somewhere around the population of the planet. Plus one. You count twice.",
                        "I would never call you an imbecile, because then I would have to explain what that is, and I doubt any of us have the requisite time.",
                        f"You see, {parent.author}, you make it too easy. An uneducated, half-brained serving boy with a hangover could make mock of you. I am left with no need to exert myself, and your very nature makes mockery of my mockery. And so it is that through sheer stupidity you make me look incompetent.",
                        "I needed an objective frame of reference by which to judge the experience of your company. Somewhere between four and five blows, I place it.",
                        f"{parent.author}, I salute you. You are what lesser cretins like AlThorStormblessed aspire to be.",
                        f"I point out truths when I see them, {parent.author}. Each man has his place. Mine is to make insults. Yours is to be in-sluts.",
                        "So, dear sir, when I say that you are the very embodiment of repulsiveness, I am merely looking to improve my art.",
                        "You look so ugly, it seems that someone tried — and failed — to get the warts off your face through aggressive application of sandpaper.",
                        "You are less a human being, and more a lump of dung with aspirations. If someone took a stick and beat you repeatedly, it could only serve to improve your features.",
                        "Your face defies description, but only because it nauseated all the poets. You are what parents use to frighten children into obedience.",
                        "I’d tell you to put a sack over your head, but think of the poor sack!",
                        "Theologians use you as proof that God exists, because such hideousness can only be intentional.",
                        f"Ahh {parent.author}! You remind me of someone very dear to me. My horse.",
                        "You storming personification of a cancerous anal discharge.",
                    ]

                    fail = [
                        "I don't feel like it, so I'll insult you instead!",
                        "You think yourself so clever?",
                        "I am sorry, your stupidity is too attractive to not talk about.",
                        "Does a man take a bite at a mildly dumb rock rather than the extremely juicy stupidity you present?"
                    ]

                    fail_2 = [
                        "I have already insulted them, and who is a Wit who wastes himself on one person?",
                        "I am bored. Ask me later, perhaps.",
                        "Why would I want to insult them? Perhaps you want to be insulted instead?",
                        "I am not into insulting imbeciles; they cry too much, and that's just annoying."
                    ]

                    fail_or_insult = random.randint(1, 3)

                    mess = random.choice(["\n\n^(These words of Wit's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
                        "\n\n^(-Wit, brought by Lopen's cousins)",
                        "\n\n^(Speak further to Wit by mentioning ! Wit in your comments. Anytime, anywhere. LMS)"])

                    list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

                    if fail_or_insult == 1:
                        parent = comment
                        comment.reply(random.choice(fail) + "\n\n" + random.choice(wit_insult) + mess + list_of)

                    else:
                        if parent.id not in comments_replied_to2:
                            parent = comment.parent()
                            parent.reply(random.choice(wit_insult) + mess + list_of) #Chooses a random quote from above list
                            comments_replied_to2.append(parent.id)
                            print("Comment insulted!")

                        else:
                            parent = comment
                            comment.reply(random.choice(fail_2) + mess + list_of) #Chooses a random quote from above list
                            pass

                    comments_replied_to2.append(comment.id)

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
                        "moolie, you have more crem in you then a Highstorm's leavings!",
                        "Wow, Gancho, you are dumber than a bridge of wood and not nearly as useful!",
                        "If your brain exploded, it wouldn't even mess up your hair!",
                        "Hey, penhito, I think the Stormfather is jealous of the amount of crem you just typed out!",
                        "May your armpits be infested with the dung of a thousand chulls!",
                        "Gancho, I have more arms than you have brains.",
                        "People like you are the reason Honor is dead.",
                        "Penhito, your words are so stupid even the Stormfather didn't accept them"
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
                    comment.reply(random.choice(fail_quotes)) #Chooses a random quote from above list
                    pass

                comments_replied_to2.append(comment.id)

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

                comment.reply(random.choice(lopen_quotes)) #Chooses a random quote from above list

                comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

                with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                    f.write(comment.id + "\n")

                print("Comment found!")

    #Swear words
        if "!swear" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
            redditor = comment.author
            comments = "".join([comment.body for comment in list(redditor.comments.new(limit = 1000))]).lower()

            reply = f"\nHey, gancho! You have been using bad Cosmere words, eh? Here are the stats for u/{comment.author}:\n\n\
|Swear words|Occurences|\n\
:--|:--|"
            swear_words = ["storms", "safehand", "femboy", "rusts", "rust and ruin", "merciful domi",\
                        "storming", "shat", "ashes", "starvin", "ash's eyes", "airsick", "nale's nut", "taln's stones",
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

            print("Swear words found!")


    #Good bot
        parent = comment.parent()
        if "good bot" in comment.body.lower() and comment.id not in comments_replied_to2 and parent.author == r.user.me():
            good_bot = [
                "Thanks, gancho!",
                "I do my best, gon!",
                "Why, you are welcome!"
            ]

            comment.reply(random.choice(good_bot)) #Chooses a random quote from above list

            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")

            print("Comment found!")

    #Bad bot
        parent = comment.parent()
        if "bad bot" in comment.body.lower() and comment.id not in comments_replied_to2 and parent.author == r.user.me():
            bad_bot = [
                "**Makes the Lopen gesture!**",
                f"Storm off, {comment.author}!",
                "I am sorry you didn't like me :("
            ]

            comment.reply(random.choice(bad_bot)) #Chooses a random quote from above list

            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again

            with open("comments_replied_to2.txt", "a", encoding='cp1252') as f:
                f.write(comment.id + "\n")

            print("Comment found!")

    #gancho
        for key in ["gancho", "moolie", "gon", "penhito", r.user.me(), "the lopen"]:
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
                    "My other hand? The one that was cut off long ago, eaten by a fearsome beast? It is making a rude gesture toward you right now. I thought you would want to know, so you can prepare to be insulted.",
                    "It is said that you shouldn't bet against a one-armed Herdazian in a drinking contest!",
                    "[OB spoilers] >!Drehy likes other guys. That's like … he wants to be even less around women than the rest of us. It's the opposite of feminine. He is you could say extra manly.!<",
                    "[OB spoilers] >!Do you mean Journey Before Pancakes, gancho?!<",
                    "[OB spoilers] >!Life before Death, Strength Before Weakness, Journey before Pancakes!<",
                    "[OB spoilers] >!NOW? I was saving that for a dramatic moment, you penhito! Why didn't you listen earlier? We were, sure, all about to die and things!!<",
                    "[DS spoilers] >!I'll do it, then. I've got to protect people, you know? Even from myself. Gotta rededicate to being the best Lopen possible. A better, improved, extra-incredible Lopen.!<"
                    "[OB spoilers] >!How hard can it be to learn how to fly? Skyeels do it all the time, and they are ugly and stupid. Most bridgemen are only one of those things.!<",
                    "[OB spoilers] >!Ground, I will still love you. I’m not attracted to anyone the way I am to you. Whenever I leave, I’ll come right back!!<",
                    "[OB spoilers] >!Here it is. I, the Lopen, will now fly. You may applaud as you feel is appropriate.!<",
                ]

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
            if WholeWord(key)(comment.body)  and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
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

    #sad
        for key in ["sad", "depress", "depressed", "trauma", "depression", "not happy", "hurt", "ache",
        "heartache", "sadly", "unfortunate", "unfortunately", "traumatic"]:
            if WholeWord(key)(comment.body) and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
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

    #Stick
        if "you could be fire" in comment.body.lower() and comment.id not in comments_replied_to2 and not comment.author == r.user.me():
            stick_quotes = [
                    "I am stick."
                 ]

            mess = random.choice(["\n\n^(These words of Stick's were brought by the Lopen Messaging Service, by the cousins, for the cousins)",
            "\n\n^(-Stick, brought by Lopen's cousins)",
            "\n\n^(Speak further to Stick by mentioning !Stick in your comments. Anytime, anywhere. LMS)"])

            list_of = "\n\n^(Use !list in your comments to view entire list LMS characters!)"

            comment.reply(random.choice(stick_quotes) + mess + list_of) #Chooses a random quote from above list

            comments_replied_to2.append(comment.id)  #Simply adds the comment.id replied to to a list so the bot doesn't reply to it again
            print("Comment found!")

    #Correction
        for key in ["lopen", "Lopen"]:
            if key in comment.body  and not "The Lopen" in comment.body and comment.id not in comments_replied_to2 and not comment.author == r.user.me() and gancho_num == 2:
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

