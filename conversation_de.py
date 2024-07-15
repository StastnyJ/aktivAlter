conversation_de = {
    "new": [
        {
            "keywords": [""],
            "response": "Hallo, ich bin AktivÄlter und ich werde Ihnen helfen, tolle Veranstaltungen in Ihrer Umgebung zu finden. Zuerst möchte ich Ihnen ein paar Fragen stellen. Ihre Antworten werden mir helfen, Ihnen bessere Vorschläge zu machen. Lassen Sie mich zuerst fragen, an welchem Ort Sie wohnen. Je genauer Ihre Angaben, desto bessere Veranstaltungen kann ich Ihnen vorschlagen. Wenn sie möchten, kann ich Sie außerdem mit Menschen in Ihrer Nähe vernetzen.",
            "next": "locationAsked"
        }
    ],
    "locationAsked": [
        {
            "keywords": ["nein", "nicht", "kein", "keine"],
            "response": "Verstanden! Können Sie mir kurz erklären, welche Aktivitäten Sie mögen?",
            "next": "activitiesAsked"
        },{
            "keywords": [""],
            "response": "Danke. Können Sie mir kurz erzählen, welche Aktivitäten Sie mögen?",
            "next": "activitiesAsked"
        }
    ],
    "activitiesAsked": [
        {
            "keywords": [""],
            "response": "Danke, jetzt habe ich alle Informationen, die ich benötige. Ich werde Sie benachrichtigen, sobald ich eine neue Veranstaltung gefunden habe, die Ihnen gefallen könnte.",
            "next": "waitingForNotification",
            "action": "sendNotification",
            "actionTimeout": 45
        }
    ],
    "notification": {
        "messages": [
            {
                "name": "boardgames",
                "activities": ["schach", "dame", "spiel", "brettspiel", "schafskopf", "karten", "kartenspiel"],
                "resp": "Ich habe eine neue Veranstaltung gefunden, die Ihnen gefallen könnte. Die Caritas organisiert nächsten Mittwoch einen Spielenachmittag in der Nähe vom Scheidplatz, beginnend um 14:00 Uhr. Weitere Informationen findest du auf der folgenden Website: https://www.caritas-nah-am-naechsten.de/de. Sind Sie an dieser Veranstaltung interessiert?"
            },{
                "name": "painting",
                "activities": ["Kunst", "malen", "malerei", "gemälde", "zeichnen", "bild", "portrait", "künstler"],
                "resp": "Ich habe eine neue Veranstaltung gefunden, die Ihnen gefallen könnte. Die Alte Pinakothek organisiert nächsten Donnerstag einen Malerei-Workshop, beginnend um 19:00 Uhr. Weitere Informationen findest du auf der folgenden Website: https://www.pinakothek.de/de/alte-pinakothek. Sind Sie an dieser Veranstaltung interessiert?" 
            },{
                "name": "opera",
                "activities": ["singen", "gesang", "theater", "kultur", "konzert", "oper", "tanz", "schauspiel", "vorführung"],
                "resp": "Ich habe eine neue Veranstaltung gefunden, die Ihnen gefallen könnte. Die Bayrische Staatsoper führt morgen die Premiere der neuen Oper Die Passagierin auf. Die Aufführung beginnt um 20:00 Uhr. Weitere Informationen findest du auf der folgenden Website: https://www.operabase.com/bayerische-staatsoper-o9476/en. Sind Sie an dieser Veranstaltung interessiert?" 
            },{
                "name": "hiking",
                "activities": ["sport", "aktiv", "natur", "Wald", "Berge", "Gehen", "Laufen", "Wandern", "Spazieren", "fit", "walking"],
                "resp": "Ich habe eine neue Veranstaltung gefunden, die Ihnen gefallen könnte. Der deutsche Alpenverein organisiert nächsten Sonntag eine Wanderung am Tegernsee, beginnend um 9 Uhr morgens. Weitere Informationen findest du auf der folgenden Website: https://www.alpenverein-muenchen-oberland.de/seniorengruppe. Sind Sie an dieser Veranstaltung interessiert?"
            },{
                "name": "cafe",
                "activities": [""],
                "resp": "Ich habe eine neue Veranstaltung gefunden, die Ihnen gefallen könnte. Der Treffpunkt unter Hundert organisiert an jedem Tag der Woche außer Mittwochs einen gemeinsamen Kaffeetreff für Senioren. Es wird auch gemeinsam gesungen und getanzt! Wäre das etwas für Sie?"
            }
        ],
        "next": "notificationSent"
    },
    "waitingForNotification": [
        {
            "keywords": [""],
            "response": "Derzeit gibt es keine neuen Veranstaltungen. Ich werde Sie benachrichtigen, sobald ich eine neue Veranstaltung finde, die Ihnen gefallen könnte.",
            "next": "waitingForNotification"
        }
    ],
    "notificationSent": [
        {
            "keywords": ["nein", "nicht", "kein", "keine"],
            "response": "Möchten Sie künftig keine weiteren Benachrichtigungen zu Veranstaltungen wie diesen erhalten?",
            "next": "eventResolved"
        },
        {
            "keywords": [""],
            "response": "Super! Ich habe herausgefunden, dass zwei andere Personen in Ihrer Nähe planen, zu dieser Veranstaltung zu gehen:\nPeter Müller +49 1522 343333 und Sarah Grubauer +49 1522 343444.\nSie können sie gerne kontaktieren, wenn Sie nicht alleine zur Veranstaltung gehen möchten. Bitte lassen Sie mich wissen, ob ich Ihre Telefonnummer mit anderen Leuten aus Ihrer Nachbarschaft teilen darf.",
            "next": "eventAccepted"   
        }
    ],
     "eventAccepted": [
        {
            "keywords": [""],
            "response": "Ok! Benötigst du Hilfe bei der Navigation zum Veranstaltungsort?",
            "next": "directionsAsked"
        }
    ],
    "directionsAsked": [
        {
            "keywords": ["nein", "nicht", "kein", "keine",],
            "response": "Ich werde Sie benachrichtigen, sobald ich eine neue Veranstaltung finde, die Ihnen gefallen könnte. Genießen Sie Ihre Veranstaltung!",
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
            "response": "Ok, ich verstehe. Ich werde Sie benachrichtigen, sobald ich eine neue Veranstaltung finde, die Ihnen gefallen könnte.",
            "next": "waitingForNotification"
        }
    ],
    "locations": {
        "locations": {
            "boardgames": "Am besten kommen Sie zu dieser Veranstaltung, indem Sie die U2, U3 oder U6 zum Scheidplatz nehmen, anschließend können Sie mit der Straßenbahn Nummer 12 zur Karl-Theodor-Strasse nehmen. Das Ohana Cafe, wo das Event stattfindet, befindet sich auf der rechten Seite der Straßenbahnhaltestelle. Um den Ort auf der Karte zu sehen, tippen Sie einfach auf den folgenden Link: \n\n https://www.google.com/maps/dir/Scheidpl.,+80804+M%C3%BCnchen-Schwabing-West,+Germany/Karl-Theodor-Stra%C3%9Fe/@48.1671722,11.570441,17.31z/data=!4m15!4m14!1m5!1m1!1s0x479e75d2171956c1:0xa147859051ddb52e!2m2!1d11.5743336!2d48.1708217!1m5!1m1!1s0x479e75cfd88e2159:0xbbf5edd1d7ff55c9!2m2!1d11.5740019!2d48.1667317!3e3!5i1?entry=ttu",
            "painting": "Am besten kommen Sie zu dieser Veranstaltung, indem Sie U2 zum Königsplatz nehmen und dann durch den Park zur Arcisstrasse laufen. Um den Ort auf der Karte zu sehen, tippen Sie einfach auf den folgenden Link:  \n\n https://www.google.com/maps/place/Karolinenplatz/@48.1470969,11.5650725,18z/data=!3m1!5s0x479e75eefc7e9f19:0x1f838f1d5a41c2a1!4m23!1m16!4m15!1m6!1m2!1s0x479e75e54cf1073b:0x1d910816edf49349!2sK%C3%B6nigsplatz,+Konigsplatz,+Munich,+Germany!2m2!1d11.5652836!2d48.1457089!1m6!1m2!1s0x479e75ee8cc069d7:0x8158244f94d1c0b7!2sAlte+Pinakothek,+Barer+Str.+27,+80333+M%C3%BCnchen,+Germany!2m2!1d11.5699755!2d48.1483311!3e3!3m5!1s0x479e75ee273e378f:0x71c918190c28fd65!8m2!3d48.1454498!4d11.5697769!16s%2Fg%2F1tftvy_r?entry=ttu",
            "opera": "Am besten kommen Sie zu dieser Veranstaltung, indem Sie die U3, U6 oder eine der S-Bahnen zum Marienplatz nehmen und anschließend 400m die Dienerstasse entlanglaufen. Um den Ort auf der Karte zu sehen, tippen Sie einfach auf den folgenden Link:  \n\n https://www.google.com/maps/dir/Marienplatz,+Marienplatz,+Munich,+Germany/Bavarian+State+Opera,+Max-Joseph-Platz+2,+80539+M%C3%BCnchen,+Germany/@48.1384378,11.5762721,18z/data=!4m14!4m13!1m5!1m1!1s0x47a84e248d37632d:0xdead51b35f0e0bb3!2m2!1d11.5754485!2d48.1373932!1m5!1m1!1s0x479e758c0d7f65ad:0x12f23e36ba17ec48!2m2!1d11.5787533!2d48.1397574!3e3?entry=ttu",
            "hiking": "Der Gruppentreff für die Wanderung ist der Hauptbahnhof. Sie können die U1, U2, U4, U5, U7, U8 oder jede S-Bahn zur Station München Hbf nehmen. Um den Ort auf der Karte zu sehen, tippen Sie einfach auf den folgenden Link: \n\n https://www.google.com/maps/search/M%C3%BCnchen+Hauptbahnhof/@48.1402713,11.5579012,17z/data=!3m1!4b1?entry=ttu",
            "cafe": "Am besten kommen Sie zu dieser Veranstaltung, indem Sie die U2, U3 oder U6 zum Scheidplatz nehmen, anschließend können Sie mit der Straßenbahn Nummer 12 zur Karl-Theodor-Strasse nehmen. Das Ohana Cafe, wo das Event stattfindet, befindet sich auf der rechten Seite der Straßenbahnhaltestelle. Um den Ort auf der Karte zu sehen, tippen Sie einfach auf den folgenden Link: \n\n https://www.google.com/maps/dir/Scheidpl.,+80804+M%C3%BCnchen-Schwabing-West,+Germany/Karl-Theodor-Stra%C3%9Fe/@48.1671722,11.570441,17.31z/data=!4m15!4m14!1m5!1m1!1s0x479e75d2171956c1:0xa147859051ddb52e!2m2!1d11.5743336!2d48.1708217!1m5!1m1!1s0x479e75cfd88e2159:0xbbf5edd1d7ff55c9!2m2!1d11.5740019!2d48.1667317!3e3!5i1?entry=ttu"
        },
        "next": "waitingForNotification"
    }
}
