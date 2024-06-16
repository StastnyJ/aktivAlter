import threading
from chatbot import Chatbot

def run_scheduled_action(action: str):
    chatbot = Chatbot("1234")
    response = chatbot.send_scheduled_action(action)
    print("< " + response)

def schedule_action(action: str, time: int):
    threading.Timer(time, run_scheduled_action, args=(action,)).start()

def main():
    while True:
        message = input("> ")
        if(message.lower() == "q" or message.lower() == "quit"):
            break
        chatbot = Chatbot("1234")
        response = chatbot.process_message(message, schedule_action)
        print("< " + response)


if __name__ == "__main__":
    main()