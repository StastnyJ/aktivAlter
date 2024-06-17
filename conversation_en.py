conversation_en = {
    "new": [
        {
            "keywords": [""],
            "response": "Hi, I am Akivälter and I am gonna help you you with finding amazing events in your neighborhood and connecting you with other people living near you who are interested in the same kind of activities. First, let me ask you a few questions to help me make a better suggestions. First, I would like to ask you, what U-Bahn or S-Bahn station is closest to the place where you live. If you are not comfortable with sharing your location, just tell me, but if you tell me, I could suggest you better events and connect you with people closer to you.",
            "next": "locationAsked"
        }
    ],
    "locationAsked": [
        {
            "keywords": ["no", "not", "don't", "won't", "dont", "wont"],
            "response": "Fine, I understand. Can you briefly explain me, what kind of activities do you like?",
            "next": "activitiesAsked"
        },{
            "keywords": [""],
            "response": "Thank you. Now I would like to ask you, what kind of activities do you like?",
            "next": "activitiesAsked"
        }
    ],
    "activitiesAsked": [
        {
            "keywords": [""],
            "response": "Thanks, now I have all the information I need. I will let you know as soon as I find a new event you might like.",
            "next": "waitingForNotification",
            "action": "sendNotification"
        }
    ],
    "notification": {
        "message": "I have found a new event you might like. Caritas is organizing next Wednesday a board game afternoon near Scheidplatz starting at 14:00. You can find more information at the following website: https://www.caritas-nah-am-naechsten.de/de. Are you interested in this event?",
        "next": "notificationSent"
    },
    "waitingForNotification": [
        {
            "keywords": [""],
            "response": "There are no new events right now. I will let you know as soon as I find a new event you might like.",
            "next": "waitingForNotification"
        }
    ],
    "notificationSent": [
        {
            "keywords": ["no", "not", "don't", "won't", "dont", "wont"],
            "response": "Is it because of the time constraints? Or are you not interested in this kind of events and want me to stop sending notifications about similar events?",
            "next": "eventResolved"
        },
        {
            "keywords": [""],
            "response": "Awesome! I found that 2 other people living near you are planning to go to this particular event:\nPeter Müller +49 1522 343333 and Sarah Grubauer +49 1522 343444.\nFeel free to contact them if you don't won't to travel alone. Also would you like me to share your phone number with other people from your neighborhood?",
            "next": "eventResolved"   
        }
    ],
    "eventResolved": [
        {
            "keywords": [""],
            "response": "Ok, I see. I will let you know as soon as I find a new event you might like.",
            "next": "waitingForNotification"
        }
    ]
}