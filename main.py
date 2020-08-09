# Creator : Lissan Koirala
# Date of Creation : 08/03/2020

# Imports
from fbchat import  Client, log
from fbchat.models import *
from playsound import playsound
from gtts import gTTS
from datetime import datetime
from pytz import timezone 
from plyer import notification
import os
import time


path = "Terms and Conditions.txt"
read_terms = [line for line in open(path)]

try:
    what_terms = read_terms[1]
    what_terms = what_terms[0]
except:
    what_terms = "blank"

if what_terms == "A" or what_terms == "blank":  ## Only proceed if the terms and condition is accepted

    f = open("email.txt",'r')
    final_email = f.read()

    g = open("password.txt",'r')
    final_password = g.read()

    n = "u"
    x = 0
    a = ""
    start = ""
    mshut = 0
    wre = 0
    ag = ""
    doing_what = "busy"

    def my_bot(msgText):
        global x
        global n
        global a
        global response_bot
        global start
        global ag
        global doing_what

        London = timezone('Europe/London')
        sa_time = datetime.now(London)
        current_time = sa_time.strftime('%H')
        current_time = int(current_time)

        if current_time > 8:
          doing_what = "in School right"
        if current_time > 15:
          doing_what = "doing his Homework right"
        if current_time > 16:
          doing_what = "Busy right"
        if current_time > 18:
          doing_what = "having his Dinner🍴🍗"
        if current_time > 21:
          doing_what = "doing some Research 🧐"
        if current_time > 22:
          doing_what = "Sleeping 😴 right"


        a = str(msgText)
        msgText = a.lower()

        urg = msgText[0] # Checking if the message is urgent by seeing what the first index
        msgText = msgText.replace(' n','and')# Deleting the excess info
        msgText = msgText.replace(' u','you')# Deleting the excess info
        msgText = msgText.replace('?','')# Deleting the excess info
        msgText = msgText.replace(' ','')# Deleting the excess info
        msgText = msgText.replace('!','')# Deleting the excess info
        msgText = msgText.replace(',','')# Deleting the excess info
        msgText = msgText.replace('.','')# Deleting the excess info

        if msgText == "startit'slissan":
            start = "Yes"
         
        if msgText == "stopit'slissan":
            start = "No"
       
        if start == "No":
            response_bot = "Ok, sir I will keep my mouth Shut :) , I will also restart my-self 🧠  "

        if start == "Yes" or start == "":
          if start == "Yes" or start == "":
            if urg == "+":
                n += "a"
                n += ".mp3"
                final_file = msgText[1:]
                final = str(final_file)
                asu = "Hello, Sir Lissan" + final + "wants you, please see the message"
                speech = gTTS(text = asu, lang = "en", slow = False) # Creating a sound for an urgent message.
                speech.save(n)
                playsound(n)
                response_bot = "I have informed him that "+final+" wants you soon! Please Wait! :) "
                a = "yes"
                notification.notify(
                title='Bot - Messenger',
                message= final+'wants you soon Sir! :) ',
                app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
                timeout=10,  # seconds
                )
             
            else:
                a = ""
         
            if a == "yes":
                pass
         
            else:
                if x == 0 or ag == "yes":
                    response_bot = "Hi, I'm Bot 1.0 🤖, Lissan is "+ doing_what +" now, I will let him know when he is available ;) . If it's important type: ['+Your Name']"
                    x += 1
                    ag = ""
       
                else:
                    a = "Hi, How are you?"
                    b = "I'm fine, and you?"
                    c = "Hat's off to Lissan ;) "
                    e = "I am Bot 1.0, created by Lissan ;) "

                    # You can add more to it
                    reply_by_bot = {
                          "whereishe":"He is working now! 👩‍💻",
                          "whoareyou":e,
                          "hi":a,
                          "hello": a,
                          "oi": a,
                          "howareyou":b,
                          "fine":"Good :)",
                          "i'mfine":"Good :)",
                          "iamfine":"Good :)",
                          "i'mfineandyou":"I'm always fine unless there is electricity :)",
                          "iamfineandyou":"I'm always good until there is Electricity :) ",
                          "wow":"Thanks, Hat's off to Lissan ;) ",
                          "that'snice":c,
                          "ok":"Bye, See you soon!",
                          "bye":"See you soon ;) , Hat's off to Lissan for this! ;) ", # Creating a responses for Bot!
                          "thanks":c,
                          "thankyou":c,
                          "lol":"LMAO :)",
                          "haha":"Don't make fun of me :( , I have feelings ;)",
                          "nice":c,
                          "fantastic":c,
                          "good":":)",
                          "yes":"Ok, that's fine!",
                          "no":"Ok, that's fine!",
                          "crazy":"Don't make fun of me 🤪 , I have feelings 😂",
                          "hell":"That's where you live 😂",
                          "amazing":c,
                          "keepitup":c,
                          "goodjob":c,
                          "whatdoyoudo":"I work for my god : Lissan Koirala 😇",
                          "howdoyouwork":"With the help of software my Boss created and Electricity ;)",
                          "whatcanyoudo":"I can reply to some of your messages and contact Lissan if it is very important!, just type '+Your Name'",
                          "takecare":"Thanks 😇",
                          "why":"Because I was created for that 😇",
                          "startit'slissan":"Ok sir, I am active now :) , you can do your work now 👨‍💻",
                          "auto-reset":"Auto-resetting 🧠",
                          "👍":"🤪",
                          "😂":"😁",
                          "🙄":"😏",
                          "🤣":"😁",
                          "😮":"😀",
                          "😯":"😀",
                          "😱":"🤓"

                          }
                 
                    try:
                        response_bot = reply_by_bot[msgText]
                        if response_bot == "Auto-resetting 🧠":
                            print("Autoresseting is being done")
                            ag = "yes"

                     
                    except:
                        response_bot = "Oops, I didn't catch that 🤪 " # If he bot cannot reply!  -  Exception Handling
                       
        return response_bot


    ######################################################
    ######################################################
    ######################################################
    ######################################################

    class Bot(Client):

        def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
            
            global wre
            global mshut

            if mshut != 2:
                # Mark message as read
                self.markAsRead(author_id)

            # Print info on console
            log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))

            # Message Text
            msgText = message_object.text 

            # Get reply from the bot 
            reply = my_bot(msgText)

            if reply ==  "Ok sir, I am active now :) , you can do your work now 👨‍💻":
                mshut = 0
                if wre != 2:
                    wre = 1
            if wre == 1:               # Sending message that I can do the work now
                    wre = 2
                
            
            if reply == "Ok, sir I will keep my mouth Shut :) , I will also restart my-self 🧠  ":
                if mshut != 2:
                    mshut = 1
            if mshut == 1:           # Sending message that I will keep my mouth shut
                mshut = 2
                self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
                wre = 0

            if reply == "Auto-resetting 🧠":
                self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
                
            else:
                pass
            
            # Send message
            if mshut != 2:
                if author_id!=self.uid:
                        self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

                        # Mark message as delivered
                        self.markAsDelivered(author_id, thread_id)

    # Create an object of our class, enter your email and password for facebook.
    try:
        client = Bot(final_email, final_password)
        
    except:
        notification.notify(
        title='Error',
        message= 'Credentials provided was incorrect\nPlease try Again!',
        app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
        timeout=10,  # seconds
        )
        os.system("credentials.py")


    # Listen for new message
    client.listen()

  
else:
    os.system("Terms.py")
    time.sleep(10)

    




