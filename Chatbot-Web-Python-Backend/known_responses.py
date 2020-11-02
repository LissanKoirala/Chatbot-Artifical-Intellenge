import time


def known_responses(mesasge):

    mesasge = mesasge.lower()

    msgText = mesasge.replace(' n','and')# Deleting the excess info
    msgText = msgText.replace(' u','you')# Deleting the excess info
    msgText = msgText.replace('?','')# Deleting the excess info
    msgText = msgText.replace(' ','')# Deleting the excess info
    msgText = msgText.replace('!','')# Deleting the excess info
    msgText = msgText.replace(',','')# Deleting the excess info
    mesasge = msgText.replace('.','')# Deleting the excess info

    
    e = "I am bot created by Lissan to help you more efficiently!"
    a = "Hi, Good to see you here!"
    b = "I am fine, what about you?"
    c = "You're welcome!"
    reply_by_bot = {
	      "whereishe":"He is working now! 👩‍💻",
	      "whoareyou":e,
	      "hi":a,
	      "hello": a,
	      "oi": a,
	      "howareyou":b,
	      "fine":"Good 😃",
	      "i'mfine":"Good 😃",
	      "iamfine":"Good 😃",
	      "i'mfineandyou":"I'm always fine unless there is electricity 😃",
	      "iamfineandyou":"I'm always good until there is Electricity 😃",
	      "wow":"Thanks, Hat's off to Lissan 😜",
	      "that'snice":c,
	      "ok":"Good!",
	      "bye":"See you soon 😜, Hat's off to Lissan for this! 😜", # Creating a responses for Bot!
	      "thanks":c,
	      "thankyou":c,
	      "lol":"LMAO 😃",
	      "haha":"Don't make fun of me 🥺, I have feelings 😜",
	      "nice":c,
	      "fantastic":c,
	      "good":"😃",
	      "yes":"Ok, that's fine!",
	      "no":"Ok, that's fine!",
	      "crazy":"Don't make fun of me 🤪, I have feelings 😂",
	      "hell":"That's where you live 😂",
	      "amazing":c,
	      "keepitup":c,
	      "goodjob":c,
	      "whatdoyoudo":"I work for my god : Lissan Koirala 😇",
	      "howdoyouwork":"With the help of software my Boss created and Electricity 😜",
	      "whatcanyoudo":"I can communicate with you, tell you anything you want to know, I can also give you coronavirus updates!",
	      "takecare":"Thanks 😇",
	      "why":"Because I was created for that 😇",
	      "startit'slissan":"Ok sir, I am active now 😃 , you can do your work now 👨‍💻",
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
        
        time.sleep(1)
        return reply_by_bot[mesasge]

    except:

    	if "what" in mesasge.lower() and "age" in mesasge.lower():
    		return "Just some days, electricity went down and I died!"


    	if "lissan" in mesasge.lower() and "like" in mesasge.lower():
    		return "He is my God! He gave me this great opportunity to think, expolre and understand life!"