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
            "action": "sendNotification",
            "actionTimeout": 45
        }
    ],
    "notification": {
        "messages": [
            {
                "name": "boardgames",
                "activities": ["chess", "checkers", "game", "board"],
                "resp": "Ich habe eine neue Veranstaltung gefunden, die dir gefallen könnte. Caritas organisiert nächsten Mittwoch einen Spielenachmittag in der Nähe vom Scheidplatz, beginnend um 14:00 Uhr. Weitere Informationen findest du auf der folgenden Website: https://www.caritas-nah-am-naechsten.de/de. Bist du an dieser Veranstaltung interessiert?"
            },{
                "name": "painting",
                "activities": ["art", "painting", "paint", "drawing", "draw", "picture", "image"],
                "resp": "I have found a new event you might like. The Alte Pinakothek is organizing next Thursday a The Art of Painting workshop starting at 19:00. You can find more information at the following website: https://www.pinakothek.de/de/alte-pinakothek. Are you interested in this event?" 
            },{
                "name": "opera",
                "activities": ["song", "singing", "theater", "culture", "concert"],
                "resp": "I have found a new event you might like. The Bavarian State opera is playing a premier of a new opera called Die Passagierin tomorrow at 20:00. You can find more information at the following website: https://www.operabase.com/bayerische-staatsoper-o9476/en. Are you interested in this event?" 
            },{
                "name": "hiking",
                "activities": ["sport", "active", "nature", "forest", "mountains", "walking", "walk", "hike", "hiking", "fit", "exercise"],
                "resp": "I have found a new event you might like. The group called Die Wanderfreunde des Alters is organizing a hike to the mountains next Sunday. You can find more information at the following website: https://www.wfdesaltes.de. Are you interested in this event?" 
            },{
                "name": "cafe",
                "activities": [""],
                "resp": "TODO - Text for the cafe event" 
            }
        ],
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
            "next": "eventAccepted"   
        }
    ],
     "eventAccepted": [
        {
            "keywords": [""],
            "response": "Ok! Do you want to suggest directions?",
            "next": "directionsAsked"
        }
    ],
    "directionsAsked": [
        {
            "keywords": ["no", "not", "don't", "won't", "dont", "wont"],
            "response": "I will let you know as soon as I find a new event you might like. Enjoy the event!",
            "next": "waitingForNotification"
        }, 
        {
            "keywords": [""],
            "response": "",
            "next": "waitingForNotification",
            "action": "sendLocation",
            "actionTimeout": 0
        }
    ],
    "eventResolved": [
        {
            "keywords": [""],
            "response": "Ok, ich verstehe. Ich werde dich benachrichtigen, sobald ich eine neue Veranstaltung finde, die dir gefallen könnte.",
            "next": "waitingForNotification"
        }
    ],
    "locations": {
        "locations": {
            "boardgames": "The best way to go to this event is going with U2, U3 or U6 to Secheidplatz and then taking a tram number 12 to Karli-Theodor-Strasse. The Ohana Cafe, where the event is hosted is right next to the trams stop. To see a map, you can use the following link: \n\n https://www.google.com/maps/dir/Scheidpl.,+80804+M%C3%BCnchen-Schwabing-West,+Germany/Karl-Theodor-Stra%C3%9Fe/@48.1671722,11.570441,17.31z/data=!4m15!4m14!1m5!1m1!1s0x479e75d2171956c1:0xa147859051ddb52e!2m2!1d11.5743336!2d48.1708217!1m5!1m1!1s0x479e75cfd88e2159:0xbbf5edd1d7ff55c9!2m2!1d11.5740019!2d48.1667317!3e3!5i1?entry=ttu",
            "painting": "The best way to go to this event is with U2 to the Königsplatz and then walk through the park to the along the Arcisstrasse. To see a map, you can use the following link: \n\n https://www.google.com/maps/place/Karolinenplatz/@48.1470969,11.5650725,18z/data=!3m1!5s0x479e75eefc7e9f19:0x1f838f1d5a41c2a1!4m23!1m16!4m15!1m6!1m2!1s0x479e75e54cf1073b:0x1d910816edf49349!2sK%C3%B6nigsplatz,+Konigsplatz,+Munich,+Germany!2m2!1d11.5652836!2d48.1457089!1m6!1m2!1s0x479e75ee8cc069d7:0x8158244f94d1c0b7!2sAlte+Pinakothek,+Barer+Str.+27,+80333+M%C3%BCnchen,+Germany!2m2!1d11.5699755!2d48.1483311!3e3!3m5!1s0x479e75ee273e378f:0x71c918190c28fd65!8m2!3d48.1454498!4d11.5697769!16s%2Fg%2F1tftvy_r?entry=ttu",
            "opera": "The best way to go to this event is with U3, U6 or any S-Bahn to the Marienplatz and than walk 400 m along Dienerstasse. To see a map, you can use the following link: \n\n https://www.google.com/maps/dir/Marienplatz,+Marienplatz,+Munich,+Germany/Bavarian+State+Opera,+Max-Joseph-Platz+2,+80539+M%C3%BCnchen,+Germany/@48.1384378,11.5762721,18z/data=!4m14!4m13!1m5!1m1!1s0x47a84e248d37632d:0xdead51b35f0e0bb3!2m2!1d11.5754485!2d48.1373932!1m5!1m1!1s0x479e758c0d7f65ad:0x12f23e36ba17ec48!2m2!1d11.5787533!2d48.1397574!3e3?entry=ttu",
            "hiking": "The group meet for this event at the main station. You can go there with U1, U2, U4, U5, U7, U8 or any S-Bahn to the station München hbf. To see a map, you cat use the following link: \n\n https://www.google.com/maps/search/M%C3%BCnchen+Hauptbahnhof/@48.1402713,11.5579012,17z/data=!3m1!4b1?entry=ttu",
            "cafe": "The best way to go to this event is going with U2, U3 or U6 to Secheidplatz and then taking a tram number 12 to Karli-Theodor-Strasse. The Ohana Cafe, where the event is hosted is right next to the trams stop. To see a map, you can use the following link: \n\n https://www.google.com/maps/dir/Scheidpl.,+80804+M%C3%BCnchen-Schwabing-West,+Germany/Karl-Theodor-Stra%C3%9Fe/@48.1671722,11.570441,17.31z/data=!4m15!4m14!1m5!1m1!1s0x479e75d2171956c1:0xa147859051ddb52e!2m2!1d11.5743336!2d48.1708217!1m5!1m1!1s0x479e75cfd88e2159:0xbbf5edd1d7ff55c9!2m2!1d11.5740019!2d48.1667317!3e3!5i1?entry=ttu"
        },
        "next": "waitingForNotification"
    }
}