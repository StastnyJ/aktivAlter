import os
import json 
from typing import Callable, List
from conversation_en import conversation_en # TODO German

EMPTY_STATE = {
    "state":"new", 
    "messages": []
}

class Chatbot:
    def __init__(self, id: str):
        self.id = id
        self.state = self._load_history(id)

    def _load_history(self, id: str) -> List[str]:
        if not os.path.exists("data"):
            os.mkdir("data")
        if not os.path.exists(os.path.join("data", id)):
            os.mkdir(os.path.join("data", id))
        if not os.path.exists(os.path.join("data", id, "messages.json")):
            with open(os.path.join("data", id, "messages.json"), "w") as f:
                f.write("")
            return EMPTY_STATE
        return json.load(open(os.path.join("data", id, "messages.json"), "r"))
    
    def _save_sate(self):
        json.dump(self.state, open(os.path.join("data", self.id, "messages.json"), "w"))
        
    
    def process_message(self, message: str, schedule_action: Callable[[str, int], None]) -> str:
        message = message.lower().strip()
        if message == "!reset":
            self.state = EMPTY_STATE
            self._save_sate()
            return "Message history was removed."
        
        response = ""
        next_state = "new"
        action = None
        possible_responses = conversation_en[self.state["state"]]
        for act in possible_responses:
            if len(response) > 0:
                break
            for keyword in act["keywords"]:
                if keyword in message:
                    response = act["response"]
                    next_state = act["next"]
                    if "action" in act:
                        action = act["action"]
                    break
        
        if action is not None:
            schedule_action(action, 45)

        self.state["state"] = next_state

        self.state["messages"].append({"msg": message, "resp": response})
        self._save_sate()
        return response
    
    def send_scheduled_action(self, action: str) -> str:
        if action == "sendNotification":
            message = conversation_en["notification"]["message"]
            self.state["state"] = conversation_en["notification"]["next"]
            self.state["messages"].append({"msg": "", "resp": message})
            self._save_sate()
            return message
