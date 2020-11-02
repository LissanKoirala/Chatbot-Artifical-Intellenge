# This is an normal import to run flask
from flask import Flask, render_template, request

# To search on google if nothing can be done...
from google_search import google_search

# If someone wants a definition for a certain word
from dictionary import define

# These are the known responses that the bot is told to reply for
from known_responses import known_responses

# Coronavirus data
from coronavirus import coronavirus_data
import requests
import threading
import time

# Flask server runner
app = Flask(__name__)
app.static_folder = 'static'

Coronavirus_Updated = False

def update_coronacases():
    while True:
        response = requests.post(f'https://www.parsehub.com/api/v2/projects/tfs3cuE3x4Cf/run', params={"api_key": "tQUqTjHrbqM-"})
        time.sleep(3600)
        




# If the home page is requested it would be served by this...
@app.route("/")
def home():

    # Updating the coronavirus once the user visits, if the first time the application runs
    global Coronavirus_Updated

    if Coronavirus_Updated == False:
        thread = threading.Thread(target=update_coronacases)
        thread.start()
        Coronavirus_Updated = True

    return render_template("index.html")



# If there is an request for a response...
@app.route("/get")
def get_bot_response():

    message = request.args.get('msg') # This is the text that the user inputed

    reply = known_responses(message) # Checking if the message is known to the bot


    if reply == None: # if the bot hasent been told a response for...


        if "coronavirus" in message.lower() or "covid" in message.lower() or "covid19" in message.lower() or "cor" and "virus" in message.lower():
            
            if "update" in message.lower():
                response = requests.post(f'https://www.parsehub.com/api/v2/projects/tfs3cuE3x4Cf/run', params={"api_key": "tQUqTjHrbqM-"})
                return "The Coronavirus data has now been updated!"


            reply = coronavirus_data(message.lower())


            if reply == None:

            	if "define" in message.lower(): # Checking if the user wants a definition...

            		reply = define(message)

            		if reply == None: # If the 


            			reply = google_search(message)

            			return str(reply)

            		else:

            			return str(reply)

            	else:


            		try:

            			reply = google_search(message)
            			return str(reply)

            		except:
            			return "Sorry, I cannot think of a reply for that!"


            else:
                return reply


        else:

            if "define" in message.lower(): # Checking if the user wants a definition...

                reply = define(message)

                if reply == None: # If the 


                    reply = google_search(message)

                    return str(reply)

                else:

                    return str(reply)

            else:


                try:

                    reply = google_search(message)
                    return str(reply)

                except:
                    return "Sorry, I cannot think of a reply for that!"


    else:

    	return str(reply)



# This starts the Flask Server
if __name__ == "__main__":

    app.run(host='0.0.0.0') 


