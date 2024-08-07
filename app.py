from chatbot import Chatbot
from flask import Flask, request, jsonify
import threading
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')
client = Client(account_sid, auth_token)

def run_scheduled_action(action: str, phoneNumber: str):
    chatbot = Chatbot(phoneNumber)
    response = chatbot.send_scheduled_action(action)
    client.messages.create(body=response, from_=twilio_number, to=phoneNumber)

def get_schedule_action(phoneNumber: str):
    def schedule_action(action: str, time: int):
        threading.Timer(time, run_scheduled_action, args=(action,phoneNumber)).start()
    return schedule_action

@app.route('/', methods=['GET'])
def ping():
    return "Aktiv aelter chat bot API"

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    try:
        incoming_msg = request.values.get('Body', '')
        phoneNumber = request.values.get("From")

        response = Chatbot(phoneNumber).process_message(incoming_msg, get_schedule_action(phoneNumber))
        resp = MessagingResponse()
        msg = resp.message()
        msg.body(response)
        return str(resp)
    except:
        return "Unknown error"

if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0', port=8099)

