from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

import json

app = Flask(__name__)



@app.route("/sms", methods=['GET', 'POST'])
def sms():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    inb_message = request.values.get('Body').lower()
    resp = MessagingResponse()
    if inb_message != None:
        resp.message("Hello. Welcome to Disaster Links. Please enter area code of your hazardous site.")
        # try:
        # int(inb_message)


        # g = open("data.json", "a")
        # g.write(inb_message)
        # g.close()
        fh = open("index.html", "r")
        lines = fh.readlines()
        lines = lines[:len(lines)-3] + ["<p>", inb_message ,"</p>\n"] + lines[len(lines)-3:]
        fh.close()

        filehandle = open("index.html", "w")
        filehandle.write("".join(lines))
        filehandle.close()

        resp.message('you have a area code')

        # except ValueError:
        #     resp.message('not an area code')

        return(str(resp))


if __name__ == "__main__":
    app.run(debug=True)
