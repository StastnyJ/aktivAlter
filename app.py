from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' in incoming_msg:
        msg.body('Hi there! How can I help you today?')
    else:
        msg.body('I am a bot, and I can only understand "hello".')

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)

