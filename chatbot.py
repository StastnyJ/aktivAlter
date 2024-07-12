import os
import json 
from typing import Callable, List
from conversation_en import conversation_en
from conversation_de import conversation_de
from langdetect import detect_langs, DetectorFactory

DetectorFactory.seed = 0

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
        
        conversation = self.detect_language(message)
        
        response = ""
        next_state = "new"
        action = None
        possible_responses = conversation[self.state["state"]]
        for act in possible_responses:
            if len(response) > 0:
                break
            for keyword in act["keywords"]:
                if keyword in message:
                    response = act["response"]
                    next_state = act["next"]
                    if "action" in act:
                        action = act["action"]
                        timeout = act["actionTimeout"]
                    break
        
        if action is not None:
            schedule_action(action, timeout)

        self.state["state"] = next_state

        self.state["messages"].append({"msg": message, "resp": response})
        self._save_sate()
        return response
    
    def detect_language(self, message: str) -> str:
        german_defaults = ["servus", "hallo", "ja", "nein", "klar"]
        english_defaults = ["hello", "hi", "yes", "no", "sure"]

        is_german_number =  "+49" in self.id

        for d in german_defaults:
            if  d in message.lower():
                return conversation_de
        for d in english_defaults:
            if  d in message.lower():
                return conversation_en
            
        try:
            langs = detect_langs(message)
            german_confidence = 0
            english_confidence = 0
            for lang in langs:
                if lang.lang == "de":
                    german_confidence = lang.prob
                if lang.lang == "en":
                    english_confidence = lang.prob
            if is_german_number:
                german_confidence *= 2
            else:
                english_confidence *= 2

            norm = german_confidence + english_confidence
            german_confidence = german_confidence / norm
            english_confidence = english_confidence / norm

            if german_confidence > english_confidence:
                return conversation_de
            else:
                return conversation_en
        except:
            return conversation_en
    
    def send_scheduled_action(self, action: str) -> str:
        last_message = self.state["messages"][-1]["msg"]
        conversation = self.detect_language(last_message)
        if action == "sendNotification":
            message = ""
            messages = conversation["notification"]["messages"]
            for m in messages:
                if len(message) > 0:
                    break
                for k in m["activities"]:
                    if k in last_message.lower():
                        message = m["resp"]
                        self.state["last_event"] = m["name"]

            self.state["state"] = conversation["notification"]["next"]
            self.state["messages"].append({"msg": "", "resp": message})
            self._save_sate()
            return message
        if action == "sendLocation":
            message = ""
            last_event = self.state["last_event"]

            message = conversation["locations"]["locations"][last_event] 

            self.state["state"] = conversation["locations"]["next"]
            self.state["messages"].append({"msg": "", "resp": message})
            self._save_sate()
            return message
            
