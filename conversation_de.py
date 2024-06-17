conversation_de = {
    "new": [
        {
            "keywords": [""],
            "response": "Hallo, ich bin Akivälter und ich werde dir helfen, großartige Veranstaltungen in deiner Umgebung zu finden und dich mit anderen Menschen zu verbinden, die an den gleichen Aktivitäten interessiert sind. Zuerst möchte ich dir ein paar Fragen stellen, um mir zu helfen, bessere Vorschläge zu machen. Zuerst möchte ich dich fragen, welche U-Bahn- oder S-Bahn-Station deinem Wohnort am nächsten ist. Wenn du deinen Standort nicht teilen möchtest, sag es mir einfach, aber wenn du mir deinen Standort mitteilst, kann ich dir bessere Veranstaltungen vorschlagen und dich mit Menschen in deiner Nähe verbinden.",
            "next": "locationAsked"
        }
    ],
    "locationAsked": [
        {
            "keywords": ["nein", "nicht", "kein", "keine"],
            "response": "In Ordnung, ich verstehe. Kannst du mir kurz erklären, welche Art von Aktivitäten du magst?",
            "next": "activitiesAsked"
        },{
            "keywords": [""],
            "response": "Danke. Nun möchte ich dich fragen, welche Art von Aktivitäten du magst?",
            "next": "activitiesAsked"
        }
    ],
    "activitiesAsked": [
        {
            "keywords": [""],
            "response": "Danke, jetzt habe ich alle Informationen, die ich brauche. Ich werde dich benachrichtigen, sobald ich eine neue Veranstaltung finde, die dir gefallen könnte.",
            "next": "waitingForNotification",
            "action": "sendNotification"
        }
    ],
    "notification": {
        "message": "Ich habe eine neue Veranstaltung gefunden, die dir gefallen könnte. Caritas organisiert nächsten Mittwoch einen Spielenachmittag in der Nähe vom Scheidplatz, beginnend um 14:00 Uhr. Weitere Informationen findest du auf der folgenden Website: https://www.caritas-nah-am-naechsten.de/de. Bist du an dieser Veranstaltung interessiert?",
        "next": "notificationSent"
    },
    "waitingForNotification": [
        {
            "keywords": [""],
            "response": "Derzeit gibt es keine neuen Veranstaltungen. Ich werde dich benachrichtigen, sobald ich eine neue Veranstaltung finde, die dir gefallen könnte.",
            "next": "waitingForNotification"
        }
    ],
    "notificationSent": [
        {
            "keywords": ["nein", "nicht", "kein", "keine"],
            "response": "Liegt es an den Zeitbeschränkungen? Oder bist du an dieser Art von Veranstaltungen nicht interessiert und möchtest, dass ich aufhöre, Benachrichtigungen über ähnliche Veranstaltungen zu senden?",
            "next": "eventResolved"
        },
        {
            "keywords": [""],
            "response": "Super! Ich habe herausgefunden, dass zwei andere Personen in deiner Nähe planen, zu dieser Veranstaltung zu gehen:\nPeter Müller +49 1522 343333 und Sarah Grubauer +49 1522 343444.\nDu kannst sie gerne kontaktieren, wenn du nicht alleine reisen möchtest. Möchtest du auch, dass ich deine Telefonnummer mit anderen Leuten aus deiner Nachbarschaft teile?",
            "next": "eventResolved"   
        }
    ],
    "eventResolved": [
        {
            "keywords": [""],
            "response": "Ok, ich verstehe. Ich werde dich benachrichtigen, sobald ich eine neue Veranstaltung finde, die dir gefallen könnte.",
            "next": "waitingForNotification"
        }
    ]
}