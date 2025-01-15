from flask import Flask, render_template, request

app = Flask(__name__)

# Datenstruktur für Empfehlungen
recommendation_data = {
    "E-mail senden und empfangen": {
        "Laptop und Desktop-PC": {
            "bedrohung": {
                "Social Engineering - Phishing": {
                    "kontext": "Phishing ist eine der häufigsten Bedrohungen beim E-Mail-Verkehr. Angreifer versuchen, persönliche Daten zu stehlen, indem sie vorgeben, vertrauenswürdige Absender zu sein. Gefälschte E-Mails enthalten häufig Links oder Anhänge, die auf gefährliche Webseiten führen oder Schadprogramme enthalten. Im Juni 2024 wurden weltweit über 266.000 Phishing-Webseiten entdeckt. Solche Angriffe zielen darauf ab, Nutzer zu täuschen, indem sie bekannte Unternehmen oder Kontakte imitieren.",
                    "beispiel": "Herzlichen Glückwunsch, Sie haben ein iPhone 15 gewonnen! Klicken Sie auf diesen Link und geben Sie Ihre Adressdaten für den Versand ein.",
                    "risiken": [
                        "Das Anklicken des Links führt zu gefälschten Webseiten, die persönliche Informationen wie Passwörter oder Adressdaten abgreifen.",
                        "Das Herunterladen von Anhängen kann Schadsoftware auf Ihrem Gerät installieren, die Ihr Gerät infizieren oder Ihre Daten stehlen."
                    ],
                    "barrieren": "Phishing-E-Mails sind oft täuschend echt gestaltet und schwer von legitimen E-Mails zu unterscheiden. Dies macht es schwierig, authentische von gefälschten E-Mails zu unterscheiden. Bei der Umsetzung der folgenden Empfehlungen minimieren Sie die Wahrscheinlichkeit, Opfer eines Phishing-Angriffs zu werden.",
                    "empfehlungen": {
                        "Aktivieren Sie Spam- und Phishing-Filter.": "Aktivieren Sie Spam- und Phishing-Filter: Nutzen Sie die integrierten Filter Ihrer E-Mail-Software, um verdächtige Nachrichten automatisch auszusortieren.",
                        "Prüfen Sie Absenderadressen.": "Prüfen Sie Absenderadressen: Bewegen Sie den Mauszeiger über den Namen des Absenders, um die tatsächliche E-Mail-Adresse anzuzeigen. Dies hilft, gefälschte Absender zu entlarven.",
                        "Klicken Sie nicht auf verdächtige Links.": "Klicken Sie nicht auf verdächtige Links: Wenn Sie unsicher sind, öffnen Sie keine Links und laden Sie keine Anhänge herunter. Geben Sie niemals persönliche Daten ein, falls Sie versehentlich auf eine gefälschte Webseite weitergeleitet werden.",
                        "Seien Sie skeptisch":"Seien Sie skeptisch: E-Mails mit unrealistischen Angeboten oder auffälligen Fehlern sollten sofort gelöscht werden.",
                        "Seien Sie vorsichtig mit Anhängen in E-Mails.": "Seien Sie vorsichtig mit Anhängen in E-Mails: E-Mails mit unrealistischen Angeboten oder auffälligen Fehlern sollten sofort gelöscht werden.",
                        "Nutzen Sie Sicherheitssoftware.": "Nutzen Sie Sicherheitssoftware: Öffnen Sie keine Anhänge mit ungewöhnlichen oder doppelten Dateiendungen, z. B. .exe, .zip oder .pdf.exe, insbesondere wenn Sie diese nicht erwartet haben."
                    },
                    "umsetzung": {
                        "Apple Mail im Browser": [
                            "Öffnen Sie Apple Mail in Ihrem Browser und gehen Sie links über das Zahnrad in die Einstellungen. Aktivieren Sie unter Datenschutz und Sicherheit 'Mail-Aktivität schützen', um Ihre IP-Adresse zu verbergen und potenziellen Angreifern die Verfolgung Ihrer Mail-Aktivität zu erschweren. ",
                            "Apple Mail erkennt und warnt Sie automatisch bei verdächtigen E-Mails und legt diese in dem Spam-Ordner ab. Falls Sie dennoch eine verdächtige E-Mail in Ihrem Postfach finden, öffnen Sie die E-Mail, klicken Sie auf die drei Punkte und wählen Sie 'In den Ordner 'Spam' verschieben'. Somit wird die E-Mails in den Spam-Ordner verschoben und der Absender für Sie blockiert."
                        ],
                        "Google Mail im Browser": [
                            "Öffnen Sie Google Mail in Ihrem Browser und gehen Sie oben rechts über das Zahnrad in die Einstellungen. Rufen Sie alle Einstellungen auf, scrollen Sie zu 'Bilder' und wählen Sie 'Vor dem Anzeigen externer Bilder fragen' aus.",
                            "Google Mail erkennt und warnt Sie automatisch vor verdächtigen E-Mails und verschiebt diese in den Spam-Ordner. Falls Sie dennoch eine verdächtige E-Mail in Ihrem Postfach finden, öffnen Sie die E-Mail, klicken sie auch die 3 Punkte und wählen Sie je nachdem 'Spam melden' oder 'Phishing melden' aus. Somit wird die E-Mail in den Spam-Ordner verschoben und der Absender für Sie blockiert."
                        ],
                        "Outlook im Browser":[
                            "Öffnen Sie Outlook in Ihrem Browser und gehen Sie oben rechts über das Zahnrad in die Einstellungen. Wählen Sie links 'Allgemein' aus und aktivieren Sie unter 'Datenschutz und Daten' die Einstellung 'Immer den Outlook-Dienst zum Laden von Bildern verwenden' aus. Dies bewirkt, dass ein direkter Download potenziell schadhafter Bilder auf Ihrem Gerät vermieden wird.",
                            "Outlook erkennt und warnt Sie automatisch bei verdächtigen E-Mails und legt diese in dem Spam-Ordner ab. Falls Sie dennoch eine verdächtige E-Mail in Ihrem Postfach finden, öffnen Sie die E-Mail, klicken Sie auf die 3 Punkte und wählen Sie je nachdem 'Phishing melden' oder 'Bedenken melden'. Somit wird die E-Mails in den Spam-Ordner verschoben und der Absender für Sie blockiert."

                        ]
                    }
                },
                "Netzwerk und Verschlüsselung": {
                    "kontext": "Eine Bedrohung für die Netzwerksicherheit beim Versenden und Empfangen von E-Mails ist die Nutzung unzureichender Verschlüsselung oder unsicherer öffentlicher Netzwerke. Unsichere E-Mail-Kommunikation ermöglicht Angreifern, Ihre Nachrichten abzufangen und Inhalte einzusehen oder zu manipulieren. Dies geschieht häufig, wenn E-Mails unverschlüsselt oder mit veralteter Verschlüsselung versendet werden. Angreifer nutzen diese Schwachstellen, um an sensible Informationen wie Passwörter, Kontonummern oder persönliche Daten zu gelangen.",
                    "beispiel": "Sie senden eine vertrauliche E-Mail an Ihre Bank mit persönlichen Informationen, z. B. Ihrer Kontonummer oder einer Anfrage zu einem Geldtransfer. Ohne ausreichende Verschlüsselung könnten Angreifer diese Daten abfangen und missbrauchen.",
                    "risiken": [
                        "Unzureichende Verschlüsselung kann dazu führen, dass Angreifer Ihre Nachrichten abfangen und Ihre sensiblen Daten auslesen.",
                        "In unsicheren Netzwerken können Ihre E-Mails abgefangen, manipuliert oder für spätere Angriffe verwendet werden."
                    ],
                    "barrieren": "Nicht alle E-Mail-Anwendungen verwenden automatisch sichere Verschlüsselungsmethoden. Zudem wissen Verbraucherinnen und Verbraucher häufig nicht, wie man eine sichere Verschlüsselung erkennt. Mit den folgenden Empfehlungen minimieren Sie das Risiko, Opfer von Angriffen in unsicheren Netzwerken zu werden.",
                    "empfehlungen": {
                        "Erkennen Sie sichere Verbindungen": "Erkennen Sie sichere Verbindungen: Wenn Sie eine E-Mail-Anwendung in Ihrem Browser nutzen, achten Sie in der Eingabeleiste darauf, dass https vor der URL steht.",
                        "Nutzen Sie sichere Verschlüsselungsprotokolle": "Nutzen Sie sichere Verschlüsselungsprotokolle: Stellen Sie sicher, dass Ihr E-Mail-Programm moderne Verschlüsselungsprotokolle wie STARTTLS, POP3S, IMAPS oder SMTPS nutzt.",
                        "Verschlüsselung bei sensiblen E-Mails":"Verschlüsselung bei sensiblen E-Mails: Aktivieren Sie die Verschlüsselung in den Einstellungen Ihrer E-Mail-Anwendung und verschlüsseln Sie E-Mails mit sensiblen Inhalten.",
                        "VPN für öffentliche WLAN-Hotspots": "VPN für öffentliche WLAN-Hotspots: Vermeiden Sie die Nutzung von E-Mail-Anwendungen innerhalb öffentlicher WLAN-Hotspots. Wenn sich dies nicht vermeiden lässt, nutzen Sie ein VPN.",
                        "Nutzung von vertrauenswürdigen Netzwerken": "Nutzung von vertrauenswürdigen Netzwerken: Stellen Sie sicher, dass Ihr Gerät automatisch eine Verbindung zu vertrauenswürdigen Netzwerken herstellt und blockieren Sie unsichere WLAN-Verbindungen."
                    },
                    "umsetzung": {
                        "Outlook im Browser": [
                            "Öffnen Sie Outlook in Ihrem Browser und gehen Sie oben rechts über das Zahnrad in die Einstellungen. Klicken Sie links auf 'E-Mail' und wählen Sie 'Junk-E-Mail' aus. Innerhalb dieser Einstellung können Sie Absender blockieren.",
                            "Öffnen Sie Outlook in Ihrem Browser und gehen Sie oben rechts über das Zahnrad in die Einstellungen. Klicken Sie links auf Allgemein und wählen Sie 'Datenschutz und Daten' aus. Scrollen Sie nach unten zu 'Externe Bilder' und deaktivieren Sie die Option, externe Bilder automatisch herunterzuladen. Somit werden potenziell schadhafte Bilder nicht automatisch auf Ihre Gerät heruntergeladen."
                        ],
                        "Google Mail im Browser": [
                            "Öffnen Sie Google Mail in Ihrem Browser und gehen Sie oben rechts über das Zahnrad in die Einstellungen. Wählen Sie 'Alle Einstellungen aufrufen' aus und gehen Sie zu 'Filter und blockierte Adressen'. Innerhalb dieser Einstellung können Sie Absender blockieren.",
                            "Öffnen Sie Google Mail in Ihrem Browser und gehen Sie oben rechts über das Zahnrad in die Einstellungen. Wählen Sie 'Alle Einstellungen aufrufen' aus und gehen Sie zu 'Allgemein'. Unter 'Bilder' aktivieren Sie die Option 'Vor dem Anzeigen externer Bilder fragen'. Somit werden potenziell schadhafte Bilder nicht automatisch auf Ihr Gerät heruntergeladen."
                        ],
                        "Apple Mail im Browser":[
                            "Öffnen Sie Apple Mail in Ihrem Browser und gehen Sie links über das Zahnrad in die Einstellungen. wählen Sie dort 'Datenschutz und Sicherheit' aus und aktivieren Sie die Option 'Mail-Aktivität schützen', um Ihre IP-Adresse zu verbergen und potenziellen Angreifern die Verfolgung Ihrer Mail-Aktivität zu erschweren.",
                            "Apple Mail lädt externe Inhalte standardmäßig nicht automatisch herunter. Somit werden potenziell schadhafte Bilder nicht automatisch auf Ihr Gerät heruntergeladen."
                        ]
                    }
                }
            }
        },

    
    "Smartphone und Tablet": {
        "bedrohung": {
            "Social Engineering - Phishing": {
                "kontext": "Phishing ist eine der häufigsten Bedrohungen beim E-Mail-Verkehr. Angreifer versuchen, persönliche Daten zu stehlen, indem sie vorgeben, vertrauenswürdige Absender zu sein. Gefälschte E-Mails enthalten häufig Links oder Anhänge, die zu gefährlichen Webseiten führen oder Schadprogramme enthalten. Im Juni 2024 wurden weltweit über 266.000 Phishing-Webseiten entdeckt. Solche Angriffe zielen darauf ab, Nutzer zu täuschen, indem sie bekannte Unternehmen oder Kontakte imitieren.",
                    "beispiel": "Herzlichen Glückwunsch, Sie haben ein iPhone 15 gewonnen! Klicken Sie auf diesen Link und geben Sie Ihre Adressdaten für den Versand ein.",
                    "risiken": [
                        "Das Anklicken des Links führt zu gefälschten Webseiten, die persönliche Informationen wie Passwörter oder Adressdaten abgreifen.",
                        "Das Herunterladen von Anhängen kann Schadsoftware auf Ihrem Gerät installieren, die Ihr Gerät infizieren oder Ihre Daten stehlen."
                    ],
                    "barrieren": "Phishing-E-Mails sind oft täuschend echt gestaltet und schwer von legitimen Nachrichten zu unterscheiden. Dadurch wird es schwierig, echte von gefälschten E-Mails zu unterscheiden. Bei der Umsetzung der folgenden Empfehlungen minimieren Sie die Wahrscheinlichkeit, Opfer eines Phishing-Angriffs zu werden.",
                    "empfehlungen": {
                        "Aktivieren Sie Spam- und Phishing-Filter.": "Aktivieren Sie Spam- und Phishing-Filter: Nutzen Sie die integrierten Filter Ihrer E-Mail-Software, um verdächtige Nachrichten automatisch auszusortieren.",
                        "Prüfen Sie Absenderadressen.": "Prüfen Sie Absenderadressen: Bewegen Sie den Mauszeiger über den Namen des Absenders, um die tatsächliche E-Mail-Adresse anzuzeigen. Dies hilft, gefälschte Absender zu entlarven.",
                        "Klicken Sie nicht auf verdächtige Links.": "Öffnen Sie keine verdächtige Links: Wenn Sie unsicher sind, öffnen Sie keine Links und laden Sie keine Anhänge herunter. Geben Sie niemals persönliche Daten ein, falls Sie versehentlich auf eine gefälschte Webseite weitergeleitet werden.",
                        "Seien Sie skeptisch":"Seien Sie skeptisch: E-Mails mit unrealistischen Angeboten oder auffälligen Fehlern sollten sofort gelöscht werden.",
                        "Seien Sie vorsichtig mit Anhängen in E-Mails.": "Seien Sie vorsichtig mit Anhängen in E-Mails: E-Mails mit unrealistischen Angeboten oder auffälligen Fehlern sollten sofort gelöscht werden.",
                        "Nutzen Sie Sicherheitssoftware.": "Nutzen Sie Sicherheitssoftware: Öffnen Sie keine Anhänge mit ungewöhnlichen oder doppelten Dateiendungen, z. B. .exe, .zip oder .pdf.exe, insbesondere wenn Sie diese nicht erwartet haben."
                    },
                "umsetzung": {
                    "Windows": [
                        "Öffnen Sie die Einstellungen und gehen Sie zu 'Netzwerk und Internet'. Öffnen Sie dort 'WLAN' und wählen Sie 'Bekannte Netzwerke verwalten' aus. Klicken Sie auf das verwendete bekannte WLAN und aktivieren Sie 'Automatisch verbinden, wenn in Reichweite', damit Ihr Gerät automatisch eine Verbindung mit Ihrem persönlichen WLAN herstellt.",
                        "Windows warnt automatisch vor unsicheren Verbindungen, wenn das Netzwerk keine Verschlüsselung hat oder es ein schwaches Sicherheitsprotokoll (wie WEP) verwendet."
                    ],
                    "MacOS": [
                        "Öffnen Sie die Systemeinstellungen und gehen Sie zu 'WLAN'. Gehen Sie zu 'Bekannte Netzwerke' und aktivieren Sie unter den drei Punkten die Option 'Automatisch verbinden' für bekannte Netzwerke. Damit stellt Ihr Gerät automatisch eine Verbindung mit Ihrem persönlichen WLAN her.",
                        "MacOS warnt automatisch vor unsicheren Verbindungen, wenn das Netzwerk keine Verschlüsselung hat oder es ein schwaches Sicherheitsprotokoll (wie WEP) verwendet."
                    ]
                }
            },

            "Netzwerk und Verschlüsselung": {
                    "kontext": "Eine Bedrohung beim Versenden und Empfangen von E-Mails im Kontext der Netzwerksicherheit besteht in der Verwendung unzureichender Verschlüsselung oder der Nutzung unsicherer öffentlicher Netzwerke. Unsichere E-Mail-Kommunikation ermöglicht Angreifern, Ihre Nachrichten abzufangen und Inhalte einzusehen oder zu manipulieren. Dies geschieht häufig, wenn E-Mails unverschlüsselt oder mit veralteter Verschlüsselung versendet werden oder wenn Sie in öffentlichen WLAN-Hotspots ohne ein VPN arbeiten. Angreifer nutzen diese Schwachstellen, um an sensible Informationen wie Passwörter, Kontonummern oder persönliche Daten zu gelangen.",
                    "beispiel": "Sie senden eine vertrauliche E-Mail an Ihre Bank mit persönlichen Informationen, z. B. Ihrer Kontonummer oder einer Anfrage zu einem Geldtransfer. Ohne ausreichende Verschlüsselung könnten Angreifer diese Daten abfangen und missbrauchen.",
                    "risiken": [
                        "Unzureichende Verschlüsselung kann dazu führen, dass Angreifer Ihre Nachrichten abfangen und Ihre sensiblen Daten auslesen.",
                        "In unsicheren Netzwerken können Ihre E-Mails abgefangen, manipuliert oder für spätere Angriffe verwendet werden."
                    ],
                    "barrieren": "Nicht alle E-Mail-Anwendungen verwenden automatisch sichere Verschlüsselungsmethoden. Zudem wissen Verbraucherinnen und Verbraucher häufig nicht, wie man eine sichere Verschlüsselung erkennt. Bei der Umsetzung der folgenden Empfehlungen minimieren Sie die Wahrscheinlichkeit, Opfer von Angriffen innerhalb unsicherer Netzwerke zu werden.",
                    "empfehlungen": {
                        "Erkennen Sie sichere Verbindungen": "Erkennen Sie sichere Verbindungen: Wenn Sie eine E-Mail-Anwendung in Ihrem Browser nutzen, achten Sie in der Eingabeleiste darauf, dass https vor der URL steht.",
                        "Nutzen Sie sichere Verschlüsselungsprotokolle": "Nutzen Sie sichere Verschlüsselungsprotokolle: Stellen Sie sicher, dass Ihr E-Mail-Programm moderne Verschlüsselungsprotokolle wie STARTTLS, POP3S, IMAPS oder SMTPS nutzt.",
                        "Verschlüsselung bei sensiblen E-Mails":"Verschlüsselung bei sensiblen E-Mails: Aktivieren Sie die Verschlüsselung in den Einstellungen Ihrer E-Mail-Anwendung und verschlüsseln Sie E-Mails mit sensiblen Inhalten.",
                        "VPN für öffentliche WLAN-Hotspots": "VPN für öffentliche WLAN-Hotspots: Vermeiden Sie die Nutzung von E-Mail-Anwendungen innerhalb öffentlicher WLAN-Hotspots. Wenn sich dies nicht vermeiden lässt, nutzen Sie ein VPN.",
                        "Nutzung von vertrauenswürdigen Netzwerken": "Nutzung von vertrauenswürdigen Netzwerken: Stellen Sie sicher, dass Ihr Gerät automatisch eine Verbindung zu vertrauenswürdigen Netzwerken herstellt und blockieren Sie unsichere WLAN-Verbindungen."
                    },
                    "umsetzung": {
                        "Google Mail App": [
                            "Google Mail bietet einen integrierten Spam- und Phishing-Schutz. Wenn dennoch eine verdächtige E-Mail in Ihrem Postfach erscheint, drücken Sie die E-Mail lange und tippen Sie auf die drei Punkte. Dort können Sie die E-Mail als Spam melden.",
                            "Öffnen Sie oben links das Menü und gehen Sie in die Einstellungen. Wählen Sie 'E-Mail-Einstellungen' aus und aktivieren Sie unter 'Bilder' die Option 'Vor dem Anzeigen externer Bilder fragen'. Dadurch werden potenziell schadhafte Bilder nicht automatisch auf Ihr Gerät heruntergeladen. "
                        ],
                        "Outlook App": [
                            "Outlook warnt Sie standardmäßig vor verdächtigen Phishing-E-Mails und verschiebt diese automatisch in den Spam-Ordner. Falls Sie dennoch eine verdächtige E-Mail in Ihrem Postfach finden, tippen Sie die entsprechende E-Mail an, klicken Sie auf die drei Punkte und wählen Sie “Junk-E-Mail melden” aus.",
                            "Tippen Sie oben links auf Ihr Profil und öffnen Sie unten links die Einstellungen. Gehen Sie unter 'Allgemein' auf 'Datenschutz' und deaktivieren Sie die Option 'Inhalte herunterladen'. Somit werden potenziell schadhafte Bilder nicht automatisch auf Ihr Gerät heruntergeladen."
                        ],
                        "Apple Mail App":[
                            "Apple enthält einen automatischen Spam- und Phishing-Schutz. Verdächtige E-Mails werden mit einer Warnung markiert. Falls Sie dennoch eine verdächtige E-Mail in Ihrem Postfach finden, halten Sie die betreffende E-Mail mit Ihrem Finger gedrückt und verschieben Sie sie in den Spam-Ordner.",
                            "Öffnen Sie die Einstellungen-App auf Ihrem Smartphone und gehen Sie auf 'Apps'. Gehen Sie auf 'Mail' und deaktivieren Sie unter 'Verfassen' die Option 'Remote-Bilder laden'. Somit werden potenziell schadhafte Bilder nicht automatisch auf Ihr Gerät heruntergeladen."
                        ]
                    }
                }
        }
    }
    },









#Surfen
    
    "Surfen im Internet": {
        "Laptop und Desktop-PC": {
            "bedrohung": {
                "Unsichere Webseiten": {
                    "kontext": "Eine große Bedrohung beim Surfen im Internet besteht darin, auf gefälschte Webseiten oder schädliche Inhalte zu stoßen, die persönliche Informationen stehlen oder Schadsoftware auf Ihr Gerät installieren können. Beim Surfen im Internet lauern zahlreiche Gefahren. Gefälschte Webseiten imitieren häufig vertrauenswürdige Plattformen, um Benutzer zur Eingabe sensibler Daten wie Passwörter zu verleiten. Auch das Herunterladen von Software aus unseriösen Quellen birgt erhebliche Risiken, da solche Programme häufig Schadsoftware enthalten. Darüber hinaus können beim Anklicken von Werbung oder Pop-ups unbemerkt Daten abfließen oder Schadprogramme auf das Gerät gelangen. Eine Studie aus dem Jahr 2024 ergab, dass etwa 80 % der Schadsoftware-Infektionen durch unvorsichtiges Surfen entstehen. Cyberkriminelle nutzen dabei gezielte Täuschungen und schädliche Inhalte, um ihre Ziele zu erreichen.",
                    "beispiel": "Sie sind der 1.000. Besucher unserer Webseite! Klicken Sie hier, um Ihren Gutschein über 500 € einzulösen!",
                    "risiken": [
                        "Durch das Anklicken gefälschter Links können Sie auf Webseiten gelangen, die Ihre Zugangsdaten oder persönlichen Informationen stehlen.",
                        "Schadsoftware kann unbemerkt auf Ihr Gerät heruntergeladen werden, was zu Datenverlust oder Systemausfällen führen kann.",
                        "Programme aus unseriösen Quellen enthalten oft Malware, die Ihre Privatsphäre gefährdet und Daten an Dritte überträgt.", 
                        "Werbeanzeigen oder Pop-ups können ebenfalls schädliche Inhalte verbreiten und Sicherheitslücken in Ihrem System ausnutzen."
                    ],
                    "barrieren": "Gefälschte Webseiten und schädliche Inhalte sind oft so gestaltet, dass sie authentisch wirken. Pop-ups und Werbung sind häufig aggressiv und verleiten Nutzerinnen und Nutzer zu unüberlegten Klicks.n. Mit den folgenden Empfehlungen können Sie die Risiken beim Surfen erheblich reduzieren.",
                    "empfehlungen": {
                        "Nutzen Sie einen sicheren Browser": "Nutzen Sie einen sicheren Browser: Verwenden Sie aktuelle Browser-Versionen mit integrierten Sicherheitsfunktionen und aktivieren Sie deren Schutzmaßnahmen (z. B. Warnungen bei unsicheren Webseiten).",
                        "Prüfen Sie Links bevor Sie diese anklicken": "Installieren Sie Software nur aus seriösen Quellen: Laden Sie Programme ausschließlich von offiziellen oder geprüften Anbietern herunter.",
                        "Installieren Sie Software nur aus seriösen Quellen": "Installieren Sie Software nur aus seriösen Quellen: Laden Sie Programme ausschließlich von offiziellen oder geprüften Anbietern herunter.",
                        "Blockieren Sie Pop-ups und Werbungen":"Blockieren Sie Pop-ups und Werbung: Verwenden Sie einen Werbeblocker, um störende Pop-ups und Werbung zu blockieren.",
                        "Nutzen Sie Sicherheitssoftware wie Antivirenprogramme":"Nutzen Sie Sicherheitssoftware: Verwenden Sie ein Anti-Malware-Programm, das schädliche Inhalte erkennt und blockiert.",

                    },
                    "umsetzung": {
                        "Microsoft Edge": [
                            "Klicken Sie oben rechts auf die drei Punkte und öffnen Sie die Einstellungen. Wählen Sie links 'Datenschutz, Suche und Dienste' aus und scrollen Sie zu 'Sicherheit'. Aktivieren Sie dort 'Microsoft Defender Smartscreen' und 'Website-Tippfehlerschutz', um sicherzustellen, dass Sie vor Phishing-Webseiten geschützt sind.",
                            "Klicken Sie oben rechts auf die drei Punkte und öffnen Sie die Einstellungen. Wählen Sie links 'Cookies und gespeicherte Daten' aus und scrollen Sie zu 'Websiteberechtigungen'. deaktivieren Sie 'Pop-ups und Umleitungen' sowie 'Aufdringliche Werbung'., um schadhafte Inhalte zu blockieren."
                        ],
                        "Google Chrome": [
                            "Öffnen Sie Ihren Browser und gehen Sie oben rechts über die drei Punkte in die Einstellungen. Gehen Sie zu 'Datenschutz und Sicherheit' und aktivieren Sie unter 'Safe Browsing' die Option 'Erweitertes Safe Browsing', sodass Sie vor Phishing-Webseiten geschützt sind.",
                            "Öffnen Sie Ihren Browser und gehen Sie oben rechts über die drei Punkte in die Einstellungen. Gehen Sie zu 'Datenschutz und Sicherheit' und öffnen Sie 'Website-Einstellungen'. Scrollen Sie nach unten zu 'Inhalte' und aktivieren Sie die Einstellung 'Pop-ups und Weiterleitungen', um potenziell schadhafte Pop-ups zu blockieren.",
                        ],
                        "Safari":[
                            "Öffnen Sie Ihren Browser und gehen Sie in die Einstellungen. Gehen Sie zu 'Sicherheit' und aktivieren Sie die Option 'Bei betrügerischen Inhalten warnen', um vor Phishing-Webseiten gewarnt zu werden.",
                            "Öffnen Sie Ihren Browser und gehen Sie in die Einstellungen. Gehen Sie zu 'Websites' und deaktivieren Sie unter 'Pop-Up-Fenster' die Anzeige von Pop-ups, um schädliche Inhalte zu blockieren."
                        ]
                    }
                },


                "Unsichere Verbindung":{
                    "kontext": "Unsichere Verschlüsselung beim Surfen im Internet ermöglicht es Dritten, Ihre Aktivitäten einzusehen. Insbesondere in öffentlichen Netzwerken ohne VPN besteht das Risiko, dass Daten abgefangen oder manipuliert werden. Zudem können Cookies, die an Dritte weitergegeben werden, Ihr Browsing-Verhalten offenlegen und Ihre Privatsphäre gefährden. Die Nutzung unsicherer Verschlüsselungstechnologien oder ungeschützter Netzwerke eröffnet Angreifern die Möglichkeit, Ihre Online-Aktivitäten mitzulesen oder zu manipulieren. Öffentliche Netzwerke, wie sie in Cafés oder Hotels verfügbar sind, sind besonders anfällig, da sie häufig keine ausreichende Sicherheit bieten. Zusätzlich ermöglichen Cookies, die von Webseiten gesetzt und mit Dritten geteilt werden, eine detaillierte Analyse Ihres Surfverhaltens, was Ihre Privatsphäre erheblich beeinträchtigen kann. Im Jahr 2024 gingen weltweit über 50 % aller Datenlecks auf unsichere Verbindungen und ungeschützte öffentliche Netzwerke zurück. Angreifer nutzen dabei Schwachstellen in der Verschlüsselung oder sammeln Daten über Cookies.",
                    "beispiel": "Sie verbinden sich mit dem kostenlosen WLAN in einem Café ohne eine Anmeldung. Dabei werden Ihre Online-Aktivitäten unbemerkt überwacht.",
                    "risiken": [
                        "Ohne sichere Verschlüsselung können sensible Daten wie Passwörter oder Kreditkartennummern von Angreifern abgefangen werden.",
                        "In öffentlichen Netzwerken können Angreifer Ihre Daten manipulieren oder Phishing-Seiten einschleusen, die wie echte Webseiten aussehen.",
                        "Cookies, die an Dritte weitergegeben werden, erlauben eine detaillierte Verfolgung Ihrer Online-Aktivitäten und die Erstellung von Nutzerprofilen."
                    ],
                    "barrieren": "Unsichere Verbindungen und Cookies werden oft unbewusst akzeptiert. Die Gefahren sind vielen Nutzern nicht bewusst, da sie nicht direkt sichtbar sind. Mit den folgenden Empfehlungen können Sie sich jedoch effektiv vor diesen Risiken schützen.",
                    "empfehlungen": {
                        "Nutzen Sie sichere Verbindungen:": "Nutzen Sie sichere Verbindungen: Achten Sie darauf, dass die URL der besuchten Webseite mit „https“ beginnt, und vermeiden Sie Seiten ohne Verschlüsselung.",
                        "Vermeiden Sie Eingaben auf unsicheren Webseiten": "Vermeiden Sie Eingaben auf unsicheren Webseiten: Achten Sie auf das „https“ in der URL und ein Schlosssymbol in der Adressleiste, bevor Sie sensible Informationen eingeben.",
                        "Verwenden Sie ein VPN in öffentlichen Netzwerken": "Verwenden Sie ein VPN in öffentlichen Netzwerken: Installieren Sie ein vertrauenswürdiges VPN (Virtual Private Network), um Ihre Daten in öffentlichen WLANs zu verschlüsseln und vor Zugriffen zu schützen.",
                        "Deaktivieren Sie die automatische Verbindung zu WLANs":"Deaktivieren Sie die automatische Verbindung zu WLANs: Stellen Sie sicher, dass Ihr Gerät sich nicht automatisch mit offenen Netzwerken verbindet, ohne dass Sie es bewusst erlauben.",
                        "Beschränken Sie Cookies":"Beschränken Sie Cookies: Verwenden Sie Browser-Einstellungen oder Erweiterungen, um Cookies von Drittanbietern zu blockieren. Löschen Sie regelmäßig Cookies, um Tracking zu minimieren.",
                        "Prüfen Sie WLAN-Verbindungen":"Prüfen Sie WLAN-Verbindungen: Verbinden Sie sich nur mit bekannten Netzwerken und fragen Sie im Zweifel nach, ob das Netzwerk vertrauenswürdig ist."

                    },
                    "umsetzung": {
                        "Microsoft Edge":[
                            "Öffnen Sie Ihren Browser und gehen Sie oben rechts über die drei Punkte in die Einstellungen. Öffnen Sie links auf 'Datenschutz, Suche und Dienste' und scrollen Sie zu 'Sicherheit'. Klicken Sie auf 'Verbessern Sie Ihre Sicherheit im Web' und wählen Sie 'Ausgewogen' oder 'Streng', um erweiterte Sicherheitseinstellungen zu aktivieren.",
                            "Öffnen Sie Ihren Browser und besuchen Sie eine beliebige Webseite. Achten Sie oben in der Suchleiste auf das Verschlüsselungssymbol in Form eines Schlosses vor dem Namen der Webseite. Das Schloss-Symbol zeigt eine verschlüsselte Verbindung an."
                        ],
                        "Google Chrome": [
                            "Öffnen Sie Ihren Browser und gehen Sie oben rechts über die drei Punkte in die Einstellungen. Gehen Sie zu 'Datenschutz und Sicherheit' und wählen Sie unter 'Sicherheit' die Option 'Sichere Verbindungen' aus. Aktivieren Sie 'Immer verschlüsselte Verbindungen verwenden'. Dadurch können potenzielle Angreifer Ihre Internetaktivität nicht ohne Weiteres einsehen.",
                            "Öffnen Sie Ihren Browser und besuchen Sie eine beliebige Webseite. Achten Sie oben in der Suchleiste auf das Verschlüsselungssymbol in Form eines Schlosses vor dem Namen der Webseite. Das Schloss-Symbol zeigt eine verschlüsselte Verbindung an."
                        ],
                        "Safari": [
                            "Öffnen Sie Ihren Browser und gehen Sie in die Einstellungen. Gehen Sie auf 'Sicherheit' und aktivieren Sie die Option 'Vor dem Verbinden mit einer Website über HTTP warnen'. Somit werden Sie bei dem Besuch einer unverschlüsselten Webseite gewarnt.",
                            "Öffnen Sie Ihren Browser und besuchen Sie eine beliebige Webseite. Achten Sie oben in der Suchleiste auf das Verschlüsselungssymbol in Form eines Schlosses vor dem Namen der Webseite. Das Schloss-Symbol zeigt eine verschlüsselte Verbindung an."
                        ]
                    }
                }

            }
        },




        "Smartphone und Tablet": {
            "bedrohung": {
                "Unsichere Webseiten": {
                    "kontext": "Eine große Bedrohung beim Surfen im Internet besteht darin, auf gefälschte Webseiten oder schädliche Inhalte zu stoßen, die persönliche Informationen abgreifen oder Schadsoftware auf das Gerät laden können. Beim Surfen im Internet lauern zahlreiche Gefahren. Gefälschte Webseiten imitieren häufig vertrauenswürdige Plattformen, um Benutzer zur Eingabe sensibler Daten wie Passwörtern zu verleiten. Auch das Herunterladen von Software aus unseriösen Quellen birgt erhebliche Risiken, da solche Programme häufig Schadsoftware enthalten. Darüber hinaus können beim Anklicken von Werbung oder Pop-ups unbemerkt Daten abfließen oder Schadprogramme auf das Gerät gelangen. Eine Studie aus dem Jahr 2024 ergab, dass etwa 80 % der Schadsoftware-Infektionen durch unachtsames Surfen verursacht werden. Cyberkriminelle nutzen dabei gezielte Täuschungen und schädliche Inhalte, um ihre Ziele zu erreichen.",
                    "beispiel": "Sie sind der 1.000. Besucher unserer Webseite! Klicken Sie hier, um Ihren Gutschein über 500 € einzulösen!",
                    "risiken": [
                        "Durch das Anklicken gefälschter Links können Sie auf Webseiten gelangen, die Ihre Zugangsdaten oder persönlichen Informationen stehlen.",
                        "Schadsoftware kann unbemerkt auf Ihr Gerät heruntergeladen werden, was zu Datenverlust oder Systemausfällen führen kann.",
                        "Heruntergeladene Programme aus unseriösen Quellen enthalten oft Malware, die Ihre Privatsphäre gefährdet und Daten an Dritte weiterleitet.", 
                        "Werbeanzeigen oder Pop-ups können ebenfalls schädliche Inhalte verbreiten und Sicherheitslücken in Ihrem System ausnutzen."
                    ],
                    "barrieren": "Viele Nutzerinnen und Nutzer haben Schwierigkeiten, unsichere Webseiten zu erkennen, da Warnhinweise oder Sicherheitsindikatoren wie das Schloss-Symbol in der Adressleiste oft übersehen oder nicht verstanden werden. Zudem fehlt es vielen Verbraucherinnen und Verbrauchern an Wissen darüber, wie sie sicher im Internet surfen können oder welche Sicherheitsmaßnahmen allgemein sinnvoll und notwendig sind. Dieses mangelnde Bewusstsein erhöht das Risiko, auf Phishing-Webseiten hereinzufallen. Mit den folgenden Empfehlungen können Sie sich jedoch effektiv vor diesen Risiken schützen.",
                    "empfehlungen": {
                        "Nutzen Sie einen sicheren Browser": "Nutzen Sie einen sicheren Browser: Verwenden Sie aktuelle Browser-Versionen mit integrierten Sicherheitsfunktionen und aktivieren Sie deren Schutzmaßnahmen (z. B. Warnungen bei unsicheren Webseiten).",
                        "Prüfen Sie Links bevor Sie diese anklicken": "Installieren Sie Software nur aus seriösen Quellen: Laden Sie Programme ausschließlich von offiziellen oder geprüften Anbietern herunter.",
                        "Installieren Sie Software nur aus seriösen Quellen": "Installieren Sie Software nur aus seriösen Quellen: Laden Sie Programme ausschließlich von offiziellen oder geprüften Anbietern herunter.",
                        "Blockieren Sie Pop-ups und Werbungen":"Blockieren Sie Pop-ups und Werbung: Verwenden Sie einen Werbeblocker, um störende Werbung zu blockieren.",
                        "Nutzen Sie Sicherheitssoftware wie Antivirenprogramme":"Nutzen Sie Sicherheitssoftware: Nutzen Sie Anti-Malware-Software, um schädliche Inhalte zu erkennen und zu blockieren.",

                    },
                    "umsetzung": {
                        "Microsoft Edge": [
                            "Öffnen Sie Ihre Browser-App und gehen Sie in die Einstellungen. Aktivieren Sie unter 'Datenschutz und Sicherheit' die Option 'Pop-ups blockieren', um schädliche Inhalte zu blockieren.",
                            "Öffnen Sie Ihre Browser-App und gehen Sie in die Einstellungen. Aktivieren Sie unter 'Datenschutz und Sicherheit' die Option 'Microsoft Defender Smartscreen', um sich vor Phishing-Webseiten zu schützen."
                        ],
                        "Google Chrome": [
                            "Öffnen Sie Ihre Browser-App und gehen Sie in die Einstellungen. Aktivieren Sie unter 'Inhaltseinstellungen' die Option 'Pop-ups blockieren', um schädliche Inhalte zu blockieren.",
                            "Öffnen Sie Ihre Browser-App und gehen Sie in die Einstellungen. Öffnen Sie 'Datenschutz und Sicherheit' und aktivieren Sie unter 'Safe Browsing' die Option 'Erweitertes Safe Browsing', sodass Sie vor Phishing-Webseiten geschützt sind"
                        ],
                        "Safari":[
                            "Öffnen Sie die Einstellungen Ihres Smartphones und gehen Sie auf 'Safari'. Aktivieren Sie unter 'Allgemein' die Option 'Pop-Ups blockieren', um schadhafte Inhalte zu blockieren.",
                            "Öffnen Sie die Einstellungen Ihres Smartphones und gehen Sie auf 'Safari'. Aktivieren Sie unter 'Datenschutz und Sicherheit' die Option 'Betrugwarnungen', um vor Phishing-Webseiten gewarnt zu werden."
                        ]
                    }
                },

                "Unsichere Verbindung":{
                    "kontext": "Beim Surfen im Internet kann eine unsichere Verschlüsselung dazu führen, dass Ihre Aktivitäten von Dritten eingesehen werden. Insbesondere in öffentlichen Netzwerken ohne VPN besteht das Risiko, dass Daten abgefangen oder manipuliert werden. Zudem können Cookies, die an Dritte weitergegeben werden, Ihr Browsing-Verhalten offenlegen und Ihre Privatsphäre gefährden. Die Nutzung unsicherer Verschlüsselungstechnologien oder ungeschützter Netzwerke eröffnet Angreifern die Möglichkeit, Ihre Online-Aktivitäten mitzulesen oder zu manipulieren. Öffentliche Netzwerke, wie sie in Cafés oder Hotels verfügbar sind, sind besonders anfällig, da sie häufig keine ausreichende Sicherheit bieten. Zusätzlich ermöglichen Cookies, die von Webseiten gesetzt und mit Dritten geteilt werden, eine detaillierte Analyse Ihres Surfverhaltens, was Ihre Privatsphäre erheblich beeinträchtigen kann. Im Jahr 2024 wurden weltweit über 50 % aller Datenlecks durch unsichere Verbindungen und mangelnden Schutz in öffentlichen Netzwerken verursacht. Angreifer nutzen dabei Schwachstellen in der Verschlüsselung oder sammeln Daten über Cookies.",
                    "beispiel": "Sie verbinden sich mit dem kostenlosen WLAN in einem Café ohne eine Anmeldung. Dabei werden Ihre Online-Aktivitäten unbemerkt überwacht.",
                    "risiken": [
                        "Ohne sichere Verschlüsselung können sensible Daten wie Passwörter oder Kreditkartennummern von Angreifern abgefangen werden.",
                        "In öffentlichen Netzwerken können Angreifer Ihre Daten manipulieren oder Phishing-Seiten einschleusen, die wie echte Webseiten aussehen.",
                        "Cookies, die an Dritte weitergegeben werden, erlauben eine detaillierte Verfolgung Ihrer Online-Aktivitäten und die Erstellung von Nutzerprofilen."
                    ],
                    "barrieren": "Unsichere Verbindungen und Cookies werden oft unbewusst akzeptiert. Die Gefahren sind vielen Nutzern nicht bewusst, da sie nicht direkt sichtbar sind. Dieses mangelnde Bewusstsein erhöht das Risiko, durch unsichere Verbindungen Opfer von Cyberkriminalität zu werden. Mit den folgenden Empfehlungen können Sie sich jedoch effektiv vor diesen Risiken schützen.",
                    "empfehlungen": {
                        "Nutzen Sie sichere Verbindungen:": "Nutzen Sie sichere Verbindungen: Achten Sie darauf, dass die URL der besuchten Webseite mit „https“ beginnt, und vermeiden Sie Seiten ohne Verschlüsselung.",
                        "Vermeiden Sie Eingaben auf unsicheren Webseiten": "Vermeiden Sie Eingaben auf unsicheren Webseiten: Achten Sie auf das „https“ in der URL und ein Schlosssymbol in der Adressleiste, bevor Sie sensible Informationen eingeben.",
                        "Verwenden Sie ein VPN in öffentlichen Netzwerken": "Verwenden Sie ein VPN in öffentlichen Netzwerken: Installieren Sie ein vertrauenswürdiges VPN (Virtual Private Network), um Ihre Daten in öffentlichen WLANs zu verschlüsseln und vor Zugriffen zu schützen.",
                        "Deaktivieren Sie die automatische Verbindung zu WLANs":"Deaktivieren Sie die automatische Verbindung zu WLANs: Stellen Sie sicher, dass Ihr Gerät sich nicht automatisch mit offenen Netzwerken verbindet, ohne dass Sie es bewusst erlauben.",
                        "Beschränken Sie Cookies":"Beschränken Sie Cookies: Nutzen Sie Browser-Einstellungen oder Erweiterungen, um Cookies von Drittanbietern zu blockieren. Löschen Sie regelmäßig Cookies, um Tracking zu minimieren.",
                        "Prüfen Sie WLAN-Verbindungen":"Prüfen Sie WLAN-Verbindungen: Verbinden Sie sich nur mit bekannten Netzwerken, und fragen Sie im Zweifel nach, ob das Netzwerk vertrauenswürdig ist."

                    },
                    "umsetzung": {
                        "Microsoft Edge": [
                            "Öffnen Sie Ihre Browser-App und besuchen Sie eine beliebige Webseite. Ein Schloss-Symbol in der Adressleiste zeigt an, dass die Webseite verschlüsselt ist. Wenn Sie dieses Symbol sehen, ist die Webseite verschlüsselt"
                        ],
                        "Google Chrome": [
                            "Öffnen Sie Ihre Browser-App und öffnen Sie die Einstellungen. Gehen Sie zu 'Datenschutz und Sicherheit' und aktivieren Sie die Option 'Immer verschlüsselte Verbindungen verwenden', um unverschlüsselte Webseiten zu blockieren.",
                            "Öffnen Sie Ihre Browser-App und besuchen Sie eine beliebige Webseite. Ein Schloss-Symbol in der Adressleiste zeigt an, dass die Webseite verschlüsselt ist. Wenn Sie dieses Symbol sehen, ist die Webseite verschlüsselt"
                        ],
                        "Safari":[
                            "Öffnen Sie die Einstellungen auf Ihrem Smartphone. Gehen Sie auf 'Apps' und wählen Sie 'Safari' aus. Aktivieren Sie unter 'Datenschutz und Sicherheit' die Option 'Warnung vor unsicherer Verbindung', um eine Meldung zu erhalten, falls Sie auf eine Webseite ohne HTTPS gelangen.",
                            "Öffnen Sie Ihre Browser-App und besuchen Sie eine beliebige Webseite. Ein Schloss-Symbol in der Adressleiste zeigt an, dass die Webseite verschlüsselt ist. Wenn Sie dieses Symbol sehen, ist die Webseite verschlüsselt"
                        ]
                    }
                }
            }
        }
    },






#####HIER WITER####


    "Telefonie/ Videotelefonie": {
        "Laptop und Desktop-PC": {
            "bedrohung": {
                "Social Engineering - Phishing": {
                    "kontext": "Unvorsichtiges Annehmen von Anrufen unbekannter Nummern oder die Teilnahme an Videotelefonaten ohne Sicherheitsvorkehrungen können dazu führen, dass persönliche Daten an Angreifer weitergegeben werden. Cyberkriminelle nutzen diese Kanäle, um Vertrauen zu erlangen und sensible Informationen zu erfragen oder Geräte durch schädliche Links zu kompromittieren. Telefonie und Videotelefonie sind beliebte Kommunikationsmittel, werden jedoch häufig von Kriminellen für Betrugszwecke missbraucht. Angreifer nutzen Social Engineering, um sensible Daten wie Passwörter oder Bankinformationen zu stehlen. Bei Videotelefonaten können Angreifer durch Schwachstellen in der Software auf Ihr Gerät zugreifen oder unbefugte Mitschnitte erstellen. Zudem besteht die Gefahr, dass Dritte bei unverschlüsselten Verbindungen die Kommunikation mithören können. Eine Studie aus dem Jahr 2024 zeigte, dass weltweit 70 % der Social-Engineering-Angriffe durch Telefonie oder Videotelefonie initiiert wurden, da viele Nutzer in direkter Kommunikation leichter manipulierbar sind.",
                    "beispiel": "Guten Tag, hier spricht die Sicherheitsabteilung Ihrer Bank. Wir haben verdächtige Aktivitäten auf Ihrem Konto festgestellt. Bitte nennen Sie uns Ihre Zugangsdaten zur Überprüfung.",
                    "risiken": [
                        "Unbekannte Anrufe können betrügerisch sein und persönliche Informationen abgreifen.",
                        "Videotelefonate über unsichere Plattformen können von Dritten mitgehört oder aufgezeichnet werden.",
                        "Das Teilen von Links in Anrufen oder Chats kann Schadsoftware oder Phishing-Webseiten verbreiten.",
                        "Über unverschlüsselte Verbindungen kann die Kommunikation abgefangen werden."
                    ],
                    "barrieren": "Die direkte Kommunikation schafft Vertrauen, das Angreifer gezielt ausnutzen. Viele Nutzer erkennen die Gefahren von Telefon- oder Videoanrufen nicht, da sie mit einer persönlichen Ansprache weniger Misstrauen verbinden. Mit den folgenden Empfehlungen können Sie diese Risiken effektiv minimieren.",
                    "empfehlungen": {
                        "Seien Sie vorsichtig bei unbekannten Nummern": "Seien Sie vorsichtig bei unbekannten Nummern: Nehmen Sie Anrufe von unbekannten Nummern nur an, wenn Sie sie erwarten, und geben Sie keine persönlichen Informationen preis.",
                        "Prüfen Sie die Identität des Anrufers": "Prüfen Sie die Identität des Anrufers: Hinterfragen Sie, ob der Anruf echt ist, und rufen Sie bei Unsicherheiten die offizielle Nummer der Organisation zurück.",
                        "Teilen Sie keine sensiblen Daten": "Teilen Sie keine sensiblen Daten: Geben Sie niemals Passwörter, Bankdaten oder andere vertrauliche Informationen telefonisch oder per Videotelefonie weiter.",
                        "Schützen Sie sich vor Spam-Anrufen": "Schützen Sie sich vor Spam-Anrufen: Nutzen Sie Spam-Filter-Apps oder aktivieren Sie die entsprechenden Funktionen auf Ihrem Smartphone."
                    },
                    "umsetzung": {
                        "Skype im Browser": [
                            "Klicken Sie oben links auf die drei Punkte und navigieren Sie zu den Einstellungen und öffnen Sie 'Datenschutz'. Gehen Sie zu 'Anrufen' und aktivieren Sie dort 'Nur Skype-Anrufe von Kontakten auf diesem Gerät zulassen'."
                        ],
                        "Microsoft Teams im Browser": [
                            "Blockieren Sie verdächtige Kontakte, indem Sie neben dem Kontakt auf die drei Punkte klicken und 'blockieren' auswählen."
                        ],
                        "Zoom im Browser":[
                            "Gehen Sie links auf die Einstellungen und wählen Sie 'Sicherheit' aus. Aktivieren Sie dort die Option, dass alle Meetings mit einer Sicherheitsoption abgesichert werden."
                        ]
                    }
                },
                "Netzwerk und Verschlüsselung": {
                    "kontext": "Telefonate und Videotelefonate, die über unsichere Verschlüsselung oder öffentliche WLAN-Hotspots geführt werden, können von Dritten abgehört oder sogar manipuliert werden. Dies gefährdet nicht nur die Vertraulichkeit der Kommunikation, sondern ermöglicht Angreifern auch, schädliche Inhalte in die Verbindung einzuschleusen. Nicht alle Kommunikationsplattformen bieten denselben Verschlüsselungsschutz. Unsichere oder veraltete Verschlüsselungsmethoden können von Angreifern umgangen werden, sodass vertrauliche Gespräche mitgehört werden können. Die Nutzung öffentlicher WLAN-Hotspots ist besonders riskant, da diese häufig ungesichert sind und von Cyberkriminellen zur Überwachung oder Manipulation von Verbindungen genutzt werden. Laut einem Bericht aus dem Jahr 2024 waren rund 60 % der abgefangenen Kommunikation auf die Nutzung unsicherer Netzwerke oder Verschlüsselungslücken zurückzuführen",
                    "beispiel": "Sie führen ein vertrauliches Telefonat in einem öffentlichen WLAN, während ein Angreifer mithört und die ausgetauschten Informationen aufzeichnet.",
                    "risiken": [
                        "Kommunikation kann von Dritten abgehört werden, was die Vertraulichkeit und Privatsphäre gefährden.",
                        "Angreifer können Gespräche manipulieren, z. B. durch das Einschleusen falscher Informationen.",
                        "Sensible Daten, wie besprochene Passwörter oder Geschäftsgeheimnisse, können von Angreifern abgegriffen werden."
                    ],
                    "barrieren": "Unsichere Verbindungen sind für Nutzer oft nicht sichtbar, da die Kommunikation scheinbar problemlos funktioniert. Öffentliche WLAN-Hotspots werden oft aus Bequemlichkeit oder Unwissenheit genutzt, ohne die Risiken zu bedenken. Mit den folgenden Empfehlungen können Sie sich besser vor diesen Risiken schützen.",
                    "empfehlungen": {
                        "Nutzen Sie Plattformen mit Ende-zu-Ende-Verschlüsselung": "Nutzen Sie Plattformen mit Ende-zu-Ende-Verschlüsselung: Verwenden Sie nur Telefonie- und Videotelefonie-Dienste, die eine sichere Verschlüsselung anbieten.",
                        "Vermeiden Sie öffentliche WLAN-Hotspots": "Vermeiden Sie öffentliche WLAN-Hotspots: Führen Sie vertrauliche Gespräche nicht in öffentlichen Netzwerken, es sei denn, Sie verwenden ein VPN (Virtual Private Network).",
                        "Prüfen Sie Netzwerke": "Prüfen Sie Netzwerke: Verbinden Sie sich nur mit vertrauenswürdigen WLANs und deaktivieren Sie die automatische Verbindung zu offenen Netzwerken.",
                        "Sprechen Sie sensible Themen nur in sicheren Umgebungen an": "Sprechen Sie sensible Themen nur in sicheren Umgebungen an: Vermeiden Sie vertrauliche Gespräche, wenn Sie nicht sicher sind, ob die Verbindung geschützt ist.",
                        "Nutzen Sie Sicherheitsfunktionen": "Nutzen Sie Sicherheitsfunktionen: Aktivieren Sie alle verfügbaren Sicherheitsfunktionen in Ihren Telefonie- und Videotelefonie-Apps, wie z. B. Authentifizierungsmechanismen und Verschlüsselungsprotokolle.",
                        "Nutzen Sie Verschlüsselung":"Nutzen Sie Verschlüsselung: Achten Sie darauf, dass Ihre Kommunikation über verschlüsselte Verbindungen erfolgt."
                    },
                    "umsetzung": {
                        "Skype im Browser": [
                            "Standardanrufe und Nachrichten werden über Skype automatisch mit TLS verschlüsselt, sodass Angreifer Ihre Anrufe und Nachrichten nicht ohne Weiteres mitlesen oder abhören können.",
                            "Klicken Sie auf einen Kontakt und wählen Sie 'Private Unterhaltung beginnen', um eine Ende-zu-Ende-Verschlüsselung zu aktivieren. Somit ist es ausschließlich Ihnen und Ihrem Kontakt möglich, Nachrichten zu lesen und Dateien zu öffnen."
                        ],
                        "Microsoft Teams im Browser": [
                            "Microsoft Teams bietet standardmäßig einen Schutz vor unsicheren Dateien und Inhalten. Durch den Microsoft Defender werden Dateien auf Schadsoftware geprüft",
                            "In Teams werden Anrufe und Nachrichten automatisch mit TLS verschlüsselt, sodass Angreifer weder Ihre Anrufe noch Ihre Nachrichten ohne Weiteres abhören können."
                        ],
                        "Zoom im Browser":[
                            "Öffnen Sie die Einstellungen links innerhalb von Zoom und wählen Sie 'Meetings' aus. Unter 'Sicherheit' können Sie die Ende-zu-Ende-Verschlüsselung aktivieren, sodass nur Sie und Ihr Kontakt Nachrichten lesen oder Dateien öffnen können."
                        ]
                    }
                }    
                    
            }
        },







    "Smartphone und Tablet": {        # Kopierte Struktur
        "bedrohung": {
            "Social Engineering - Phishing": {
                "kontext": "Unvorsichtiges Annehmen von Anrufen unbekannter Nummern oder die Teilnahme an Videotelefonaten ohne Sicherheitsvorkehrungen können dazu führen, dass persönliche Daten an Angreifer weitergegeben werden. Cyberkriminelle nutzen diese Kanäle, um Vertrauen zu erlangen und sensible Informationen zu erfragen oder Geräte durch schädliche Links zu kompromittieren. Telefonie und Videotelefonie sind beliebte Kommunikationsmittel, werden jedoch häufig für Betrugsversuche genutzt. Angreifer nutzen Social Engineering, um durch Manipulation sensible Daten wie Passwörter oder Bankzugangsdaten zu stehlen. Bei Videotelefonaten können Angreifer durch Schwachstellen in der Software auf Ihr Gerät zugreifen oder unbefugte Mitschnitte erstellen. Zudem besteht die Gefahr, dass Dritte bei unverschlüsselten Verbindungen die Kommunikation mithören können. Eine Studie aus dem Jahr 2024 zeigte, dass weltweit 70 % der Social-Engineering-Angriffe durch Telefonie oder Videotelefonie initiiert wurden, da viele Nutzer in direkter Kommunikation leichter manipulierbar sind.",
                    "beispiel": "Guten Tag, hier spricht die Sicherheitsabteilung Ihrer Bank. Wir haben verdächtige Aktivitäten auf Ihrem Konto festgestellt. Bitte nennen Sie uns Ihre Zugangsdaten zur Überprüfung.",
                    "risiken": [
                        "Unbekannte Anrufe können betrügerisch sein und persönliche Informationen abgreifen.",
                        "Videotelefonate über unsichere Plattformen können von Dritten mitgehört oder aufgezeichnet werden.",
                        "Durch das Teilen von Links in Anrufen oder Chats können Schadsoftware und Phishing-Webseiten verbreitet werden.",
                        "Über unverschlüsselte Verbindungen kann die Kommunikation abgefangen werden."
                    ],
                    "barrieren": "Die direkte Kommunikation schafft Vertrauen, das Angreifer gezielt ausnutzen. Viele Nutzer unterschätzen die Risiken von Telefon- oder Videoanrufen, da persönliche Ansprache oft weniger Misstrauen hervorruft. Die folgenden Empfehlungen helfen Ihnen, sich effektiv vor diesen Risiken zu schützen.",
                    "empfehlungen": {
                        "Seien Sie vorsichtig bei unbekannten Nummern": "Seien Sie vorsichtig bei unbekannten Nummern: Nehmen Sie Anrufe von unbekannten Nummern nur an, wenn Sie sie erwarten, und geben Sie keine persönlichen Informationen preis.",
                        "Prüfen Sie die Identität des Anrufers": "Prüfen Sie die Identität des Anrufers: Hinterfragen Sie, ob der Anruf echt ist, und rufen Sie bei Unsicherheiten die offizielle Nummer der Organisation zurück.",
                        "Teilen Sie keine sensiblen Daten": "Teilen Sie keine sensiblen Daten: Geben Sie niemals Passwörter, Bankdaten oder andere vertrauliche Informationen telefonisch oder per Videotelefonie weiter.",
                        "Schützen Sie sich vor Spam-Anrufen": "Schützen Sie sich vor Spam-Anrufen: Nutzen Sie Spam-Filter-Apps oder aktivieren Sie die entsprechenden Funktionen auf Ihrem Smartphone."
                    },
                    "umsetzung": {
                        "iOS": [
                            "Blockieren Sie verdächtige Kontakte, insbesondere bei Anrufen aus dem Ausland, wenn Sie diese nicht erwarten. Tippen Sie in Ihrer Anrufliste auf das 'i' neben der Nummer des Anrufers und wählen Sie 'Anrufer:in blockieren'.",
                            "Öffnen Sie die Einstellungen und gehen Sie auf 'Apps'. Wählen Sie dort die Nachrichten-App aus und aktivieren Sie die Funktion 'Unbekannte Absender filtern', um verdächtige Links von unbekannten Kontakten zu blockieren. Mit dieser Einstellung werden keine Links von unbekannten Kontakten geöffnet."
                        ],
                        "Android": [
                            "Öffnen Sie die Telefon-App und gehen Sie in die Einstellungen. Tippen Sie auf 'Anrufe' und wählen Sie 'Anrufer-ID und Spam' aus. Dort können Sie die Funktion 'Spam-Anrufe filtern' aktivieren.",
                            "Öffnen Sie Ihre Nachrichten-App und gehen Sie in die Einstellungen. Aktivieren Sie dort den Spam-Schutz."
                        ]
                }
            },
            "Netzwerk und Verschlüsselung": {
                    "kontext": "Telefonate und Videotelefonate, die über unsichere Verschlüsselung oder öffentliche WLAN-Hotspots geführt werden, können von Dritten abgehört oder sogar manipuliert werden. Dies gefährdet nicht nur die Vertraulichkeit der Kommunikation, sondern ermöglicht Angreifern auch, schädliche Inhalte in die Verbindung einzuschleusen. Nicht alle Kommunikationsplattformen bieten denselben Verschlüsselungsschutz. Unsichere oder veraltete Verschlüsselungsmethoden können von Angreifern umgangen werden, wodurch vertrauliche Gespräche abgefangen werden können. Besonders riskant ist die Nutzung öffentlicher WLAN-Hotspots, da diese häufig ungesichert sind und von Cyberkriminellen zur Überwachung oder Manipulation von Verbindungen genutzt werden. Laut einem Bericht aus dem Jahr 2024 waren rund 60 % der abgefangenen Kommunikation auf die Nutzung unsicherer Netzwerke oder Verschlüsselungslücken zurückzuführen",
                    "beispiel": "Sie führen ein vertrauliches Telefonat in einem öffentlichen WLAN, während ein Angreifer mithört und die ausgetauschten Informationen aufzeichnet.",
                    "risiken": [
                        "Kommunikation kann von Dritten abgehört werden, was die Vertraulichkeit und Privatsphäre gefährden.",
                        "Angreifer können Gespräche manipulieren, z. B. durch das Einschleusen falscher Informationen.",
                        "Sensible Daten, wie besprochene Passwörter oder Geschäftsgeheimnisse, können von Angreifern abgegriffen werden."
                    ],
                    "barrieren": "Unsichere Verbindungen sind für Nutzer oft nicht sichtbar, da die Kommunikation scheinbar problemlos funktioniert. Öffentliche WLAN-Hotspots werden aus Bequemlichkeit oder Unkenntnis häufig verwendet, ohne die Risiken zu berücksichtigen. Mit den folgenden Empfehlungen können Sie diese Gefahren minimieren.",
                    "empfehlungen": {
                        "Nutzen Sie Plattformen mit Ende-zu-Ende-Verschlüsselung": "Nutzen Sie Plattformen mit Ende-zu-Ende-Verschlüsselung: Verwenden Sie nur Telefonie- und Videotelefonie-Dienste, die eine sichere Verschlüsselung anbieten.",
                        "Vermeiden Sie öffentliche WLAN-Hotspots": "Vermeiden Sie öffentliche WLAN-Hotspots: Führen Sie vertrauliche Gespräche nicht in öffentlichen Netzwerken, es sei denn, Sie verwenden ein VPN (Virtual Private Network).",
                        "Prüfen Sie Netzwerke": "Prüfen Sie Netzwerke: Verbinden Sie sich nur mit vertrauenswürdigen WLANs und deaktivieren Sie die automatische Verbindung zu offenen Netzwerken.",
                        "Sprechen Sie sensible Themen nur in sicheren Umgebungen an": "Sprechen Sie sensible Themen nur in sicheren Umgebungen an: Vermeiden Sie vertrauliche Gespräche, wenn Sie nicht sicher sind, ob die Verbindung geschützt ist.",
                        "Nutzen Sie Sicherheitsfunktionen": "Nutzen Sie Sicherheitsfunktionen: Aktivieren Sie alle verfügbaren Sicherheitsfunktionen in Ihren Telefonie- und Videotelefonie-Apps, wie z. B. Authentifizierungsmechanismen und Verschlüsselungsprotokolle.",
                        "Nutzen Sie Verschlüsselung":"Nutzen Sie Verschlüsselung: Achten Sie darauf, dass Ihre Telefon- und Videokommunikation durch Ende-zu-Ende-Verschlüsselung geschützt ist."
                    },
                    "umsetzung": {
                        "Skype App": [
                            "Öffnen Sie Ihre Skype App und tippen Sie unten rechts auf 'Neue Unterhaltung'. Wählen Sie 'Neue private Unterhaltung' aus und wählen Sie Ihren gewünschten Kontakt aus, um eine Ende-zu-Ende-verschlüsselte Unterhaltung zu starten."
                        ],
                        "Teams App": [
                            "Teams verschlüsselt Anrufe und Nachrichten automatisch mit TLS, sodass Angreifer Ihre Anrufe und Nachrichten nicht ohne Weiteres abhören können."
                        ],
                        "Zoom App":[
                            "Um eine Ende-zu-Ende-Verschlüsselung in der Zoom App zu nutzen, müssen Sie diese Einstellung zuvor in dem Webportal auswählen. Melden Sie sich über Ihren Browser im Zoom-Webportal an, und wählen Sie nach der Anmeldung 'Einstellungen' im Dropdown-Menü aus. Gehen Sie auf 'Meetings' und aktivieren Sie 'End-to-End-Verschlüsselung nutzen' aus. Nun können Sie diese Einstellung auch in Ihrer App nutzen."
                        ]
                    }
                }
            }      
        }
    },









    "Messenger": {
        "Laptop und Desktop-PC": {
            "bedrohung": {
                "Social Engineering - Phishing": {
                    "kontext": "Die Nutzung von Messengern birgt verschiedene Risiken. Unbekannte Kontakte können versuchen, persönliche Daten abzugreifen. Links in empfangenen Nachrichten können zu gefälschten Webseiten führen, die persönliche Informationen stehlen, oder Schadsoftware auf Ihr Gerät übertragen. Ebenso können Dateien, die von Kontakten gesendet werden, Schadsoftware enthalten, die Ihr Gerät infiziert, sobald Sie sie herunterladen. Messenger-Dienste sind ein beliebtes Kommunikationsmittel, aber auch ein Ziel für Cyberkriminelle. Phishing-Angriffe und der Versand von Schadsoftware über Nachrichten und Dateien sind weit verbreitet. Unbekannte Kontakte nutzen Social Engineering, indem sie Vertrauen schaffen, um sensible Informationen zu stehlen. Auch scheinbar harmlose Links und Dateien können erhebliche Sicherheitsrisiken darstellen, wenn sie von Angreifern stammen. Laut einem Bericht aus dem Jahr 2024 war jeder dritte Cyberangriff auf mobile Geräte auf Messenger-Aktivitäten zurückzuführen. Besonders gefährdet sind Nutzer, die unbekannten Kontakten leichtfertig vertrauen oder verdächtige Inhalte öffnen.",
                    "beispiel": "Eine Ihnen unbekannte Person sendet Ihnen eine „wichtige“ Datei, die beim Öffnen Schadsoftware auf Ihr Gerät lädt.",
                    "risiken": [
                        "Persönliche Informationen können durch unbekannte Kontakte oder gefälschte Links abgegriffen werden.",
                        "Schadsoftware kann durch das Herunterladen von Dateien oder Anklicken von Links auf das Gerät gelangen.",
                        "Phishing-Angriffe können Zugangsdaten oder andere sensible Informationen stehlen."
                    ],
                    "barrieren": "Die direkte Kommunikation über Messenger schafft Vertrauen, das Angreifer gezielt ausnutzen. Viele Nutzer öffnen Nachrichten, Links oder Dateien aus Neugier oder in gutem Glauben, ohne die potenziellen Risiken zu bedenken. Die folgenden Empfehlungen helfen Ihnen, diese Gefahren zu minimieren.",
                    "empfehlungen": {
                        "Klicken Sie nicht auf verdächtige Links": "Klicken Sie nicht auf verdächtige Links: Überprüfen Sie Links, bevor Sie sie anklicken, und öffnen Sie sie nur, wenn Sie sicher sind, dass sie von einer vertrauenswürdigen Quelle stammen.",
                        "Prüfen Sie Dateien vor dem Herunterladen": "Prüfen Sie Dateien vor dem Herunterladen: Laden Sie Dateien nur herunter, wenn Sie den Absender kennen und ihm vertrauen. Verwenden Sie ein Antivirenprogramm, um Dateien vor dem Öffnen zu scannen.",
                        "Aktivieren Sie Sicherheitsfunktionen in Messengern": "Aktivieren Sie Sicherheitsfunktionen in Messengern: Nutzen Sie Ende-zu-Ende-Verschlüsselung und andere verfügbare Sicherheitsoptionen in der Messenger-App.",
                        "Geben Sie keine sensiblen Daten weiter": "Geben Sie keine sensiblen Daten weiter: Teilen Sie niemals persönliche Informationen, Passwörter oder Zugangsdaten über Messenger, insbesondere nicht mit unbekannten Kontakten.",
                        "Seien Sie skeptisch bei ungewöhnlichen Nachrichten von bekannten Kontakten":"Seien Sie skeptisch bei ungewöhnlichen Nachrichten von bekannten Kontakten: Wenn eine Nachricht von einem bekannten Kontakt verdächtig erscheint, bestätigen Sie die Echtheit durch eine andere Kommunikationsmethode.",
                        "Schalten Sie den automatischen Download von Dateien aus":"Deaktivieren Sie den automatischen Download von Medien wie Bildern, Videos oder Dokumenten, um das Risiko unerkannt installierter Schadsoftware zu minimieren."
                    },
                    "umsetzung": {
                        "Whatsapp Desktop-App": [
                        "Melden Sie Kontakte, die Ihnen verdächtige Nachrichten wie Phishing-Nachrichten schreiben. Öffnen Sie den Chat des Kontakts, klicken Sie oben auf den Namen/ die Nummer und wählen Sie 'Kontakt melden' aus."
                        ],
                        "Telegram Desktop-App": [
                            "Gehen Sie oben links in die Einstellungen und wählen Sie Privatsphäre und Sicherheit aus. Aktivieren Sie dort, dass nur Anrufe und Nachrichten von Ihren Kontakten getätigt werden dürfen."
                        ],
                        "Signal Desktop-App": [
                            "Öffnen Sie oben Links das Menü und gehen Sie über das Zahnrad unten links in die Einstellungen. Gehen Sie auf 'Anrufe' und aktivieren Sie, dass Anrufe immer indirekt sind, um Ihre IP-Adresse zu verbergen und potenziellen Angreifern die Verfolgung Ihrer Telefonie-Aktivität zu erschweren."
                        ]
                    }
                },
                "Netzwerk und Verschlüsselung": {
                    "kontext": "Die Nutzung von Messengern mit unzureichender Verschlüsselung birgt das Risiko, dass Nachrichten von Dritten eingesehen oder abgefangen werden können. Insbesondere bei der Verwendung öffentlicher WLAN-Hotspots ohne VPN steigt die Gefahr, dass Ihre Kommunikation manipuliert oder überwacht wird. Auch die Nutzung von nicht etablierten Messenger-Diensten kann zu Datenverlust und dem Missbrauch persönlicher Informationen führen. Einige Messenger-Dienste setzen auf schwache oder veraltete Verschlüsselungsmethoden, die von Angreifern umgangen werden können. Öffentliche WLAN-Hotspots, die keine ausreichende Sicherheit bieten, ermöglichen es Cyberkriminellen, Nachrichten mitzulesen oder zu manipulieren. Darüber hinaus können unbekannte oder wenig verbreitete Messenger-Dienste, die keine umfassenden Sicherheitsmaßnahmen implementieren, persönliche Daten stehlen oder an Dritte weitergeben. Im Jahr 2024 wurden 55 % der bekannten Messenger-Sicherheitsvorfälle durch unzureichende Verschlüsselung oder die Nutzung unsicherer Netzwerke ermöglicht. Besonders betroffen sind Nutzer, die auf nicht etablierte oder unsichere Dienste vertrauen.",
                    "beispiel": "Sie sind in einem Café und nutzen den kostenlosen WLAN-Hotspot, während Angreifer im Netzwerk Ihre Nachrichten mitlesen.",
                    "risiken": [
                        "Angreifer können Nachrichten aufgrund unzureichender Verschlüsselung abfangen und einsehen.",
                        "In öffentlichen Netzwerken können Nachrichten manipuliert oder gefälschte Inhalte eingefügt werden.",
                        "Nicht etablierte Messenger-Dienste können persönliche Daten und Nachrichten stehlen oder missbrauchen."
                    ],
                    "barrieren": "Unzureichende Verschlüsselung und unsichere Netzwerke sind für Nutzer oft nicht erkennbar, da die Kommunikation scheinbar normal funktioniert. Viele Nutzer nutzen ungesicherte Netzwerke oder unbekannte Messenger-Dienste, ohne die potenziellen Risiken zu bedenken. Die folgenden Empfehlungen helfen Ihnen, sich vor diesen Gefahren zu schützen.",
                    "empfehlungen": {
                        "Nutzen Sie Messenger mit Ende-zu-Ende-Verschlüsselung": "Nutzen Sie Messenger mit Ende-zu-Ende-Verschlüsselung: Verwenden Sie nur Dienste, die eine starke Verschlüsselung bieten, um Ihre Nachrichten vor dem Zugriff Dritter zu schützen.",
                        "Vermeiden Sie öffentliche WLAN-Hotspots": "Vermeiden Sie öffentliche WLAN-Hotspots: Führen sie den Austausch sensibler Informationen nicht in öffentlichen Netzwerken durch, es sei denn, Sie nutzen ein VPN (Virtual Private Network).",
                        "Verwenden Sie etablierte Messenger-Dienste": "Verwenden Sie etablierte Messenger-Dienste: Nutzen Sie nur bekannte und weit verbreitete Messenger-Apps, die regelmäßig aktualisiert und auf Sicherheitsstandards geprüft werden.",
                        "Achten Sie auf Netzwerk-Sicherheit": "Achten Sie auf Netzwerk-Sicherheit: Deaktivieren Sie die automatische Verbindung zu öffentlichen Netzwerken, um das Risiko ungesicherter Verbindungen zu minimieren.",
                        "Seien Sie vorsichtig mit neuen oder unbekannten Diensten": "Seien Sie vorsichtig mit neuen oder unbekannten Diensten: Vermeiden Sie die Nutzung von Messengern, die keine klaren Informationen zu Sicherheit und Datenschutz bieten."
                    },
                    "umsetzung": {
                        "Whatsapp Desktop-App": [
                            "Whatsapp verwendet automatisch eine Ende-zu-Ende-Verschlüsselung",
                        ],
                        "Telegram Desktop-App": [
                            "Öffnen Sie einen Chat und klicken Sie auf den Namen des Kontakts. Über die drei Punkte können Sie einen geheimen Chat starten für eine Ende-zu-Ende-Verschlüsselung.",
                        ],
                        "Signal Desktop-App":[
                            "Signal bietet standardmäßig Ende-zu-Ende-Verschlüsselung."
                        ]
                    }
                }    
                    
            }
        },

    
    "Smartphone und Tablet": {
        "bedrohung": {
            "Social Engineering - Phishing": {
                "kontext": "Die Nutzung von Messengern birgt verschiedene Risiken. Cyberkriminelle nutzen Social Engineering, um durch manipulative Taktiken Vertrauen aufzubauen und sensible Informationen zu stehlen. Links in empfangenen Nachrichten können zu gefälschten Webseiten führen, die persönliche Informationen stehlen, oder Schadsoftware auf das Gerät laden. Ebenso können Dateien, die von Kontakten gesendet werden, Schadsoftware enthalten, die Ihr Gerät infiziert, sobald Sie sie herunterladen. Messenger-Dienste sind ein beliebtes Kommunikationsmittel, aber auch ein Ziel für Cyberkriminelle. Phishing-Angriffe und der Versand von Schadsoftware über Nachrichten und Dateien sind weit verbreitet. Unbekannte Kontakte nutzen Social Engineering, um Vertrauen aufzubauen und sensible Informationen zu erlangen. Auch scheinbar harmlose Links und Dateien können erhebliche Sicherheitsrisiken darstellen, wenn sie von Angreifern stammen. Laut einem Bericht aus dem Jahr 2024 war jeder dritte Cyberangriff auf mobile Geräte auf Messenger-Aktivitäten zurückzuführen. Besonders gefährdet sind Nutzer, die unbekannten Kontakten leichtfertig vertrauen oder verdächtige Inhalte öffnen.",
                    "beispiel": "Eine Ihnen unbekannte Person sendet Ihnen eine „wichtige“ Datei, die beim Öffnen Schadsoftware auf Ihr Gerät lädt.",
                    "risiken": [
                        "Persönliche Informationen können durch unbekannte Kontakte oder gefälschte Links abgegriffen werden.",
                        "Schadsoftware kann durch das Herunterladen von Dateien oder Anklicken von Links auf das Gerät gelangen.",
                        "Phishing-Angriffe können Zugangsdaten oder andere sensible Informationen stehlen."
                    ],
                    "barrieren": "Die direkte Kommunikation über Messenger schafft Vertrauen, das Angreifer gezielt ausnutzen. Viele Nutzer öffnen Nachrichten, Links oder Dateien aus Neugier oder in gutem Glauben, ohne die potenziellen Risiken zu erkennen. Die folgenden Empfehlungen helfen Ihnen, diese Gefahren zu minimieren.",
                    "empfehlungen": {
                        "Klicken Sie nicht auf verdächtige Links": "Klicken Sie nicht auf verdächtige Links: Überprüfen Sie Links, bevor Sie sie anklicken, und öffnen Sie sie nur, wenn Sie sicher sind, dass sie von einer vertrauenswürdigen Quelle stammen.",
                        "Prüfen Sie Dateien vor dem Herunterladen": "Prüfen Sie Dateien vor dem Herunterladen: Laden Sie Dateien nur herunter, wenn Sie den Absender kennen und ihm vertrauen. Verwenden Sie ein Antivirenprogramm, um Dateien vor dem Öffnen zu scannen.",
                        "Aktivieren Sie Sicherheitsfunktionen in Messengern": "Aktivieren Sie Sicherheitsfunktionen in Messengern: Nutzen Sie Ende-zu-Ende-Verschlüsselung und andere verfügbare Sicherheitsoptionen in der Messenger-App.",
                        "Geben Sie keine sensiblen Daten weiter": "Geben Sie keine sensiblen Daten weiter: Teilen Sie niemals persönliche Informationen, Passwörter oder Zugangsdaten über Messenger, insbesondere nicht mit unbekannten Kontakten.",
                        "Seien Sie skeptisch bei ungewöhnlichen Nachrichten von bekannten Kontakten":"Seien Sie skeptisch bei ungewöhnlichen Nachrichten von bekannten Kontakten: Wenn eine Nachricht von einem bekannten Kontakt verdächtig erscheint, bestätigen Sie die Echtheit durch eine andere Kommunikationsmethode.",
                        "Schalten Sie den automatischen Download von Dateien aus":"Deaktivieren Sie den automatischen Download von Medien wie Bildern, Videos und Dokumenten, um das Risiko unbemerkter Schadsoftware zu minimieren."
                    },
                    "umsetzung": {
                        "Whatsapp App": [
                            "Öffnen Sie unten rechts über das Zahnrad die Einstellungen. Aktivieren Sie unter 'Datenschutz' die Funktion 'Nachrichten von unbekannten Nummern blockieren', um Spam-Nachrichten und potenzielle Phishing-Angriffe zu vermeiden. Dies hat zur Folge, dass Konten, welche Ihnen in kurzer Zeit viele Nachrichten hintereinander senden (spam) automatisch blockiert werden.",
                            "Öffnen Sie unten rechts über das Zahnrad die Einstellungen. Wählen Sie 'Speicher und Daten' und Deaktivieren Sie unter 'Speicher und Daten' den automatischen Download von Medien. Dies minimiert das Risiko Schadsoftware herunterzuladen."
                        ],
                        "Telegram App": [
                            "Gehen Sie unten rechts über das Zahnrad in die Einstellungen. Legen Sie unter 'Privatsphäre' fest, dass nur Ihre Kontakte Ihnen Nachrichten oder Anrufe senden können, um unerwünschte Kontakte zu blockieren.",
                            "Gehen Sie unten rechts über das Zahnrad in die Einstellungen. Wählen Sie 'Daten und Speicher' aus und deaktivieren Sie mit 'Automatischer Medien-Download' das automatische herunterladen sämtlicher Medien. Dies minimiert das Risiko Schadsoftware herunterzuladen."
                        ],
                        "Signal App":[
                            "Tippen Sie oben links auf Ihr Profilbild und öffnen Sie die Einstellungen. Öffnen Sie 'Datennutzung' und deaktivieren Sie unter 'Automatisch herunterladen' das automatische herunterladen sämtlicher Medien. Dies minimiert das Risiko Schadsoftware herunterzuladen.",
                            "Tippen Sie oben links auf Ihr Profilbild und öffnen Sie die Einstellungen. Gehen Sie auf 'Datenschutz' und öffnen Sie 'Weitere Einstellungen'. Aktivieren Sie dort, dass Anrufe immer indirekt sind, um Ihre IP-Adresse zu verbergen und potenziellen Angreifern die Verfolgung Ihrer Telefonie-Aktivität zu erschweren."
                        ]
                }
            },
            "Netzwerk und Verschlüsselung": {
                    "kontext": "Messengerdienste mit unzureichender Verschlüsselung bergen das Risiko, dass Nachrichten von Dritten eingesehen oder abgefangen werden. Insbesondere bei der Verwendung öffentlicher WLAN-Hotspots ohne VPN steigt die Gefahr, dass Ihre Kommunikation manipuliert oder überwacht wird. Auch die Nutzung von nicht etablierten Messenger-Diensten kann zu Datenverlust und dem Missbrauch persönlicher Informationen führen. Einige Messenger-Dienste setzen auf schwache oder veraltete Verschlüsselungsmethoden, die von Angreifern umgangen werden können. Öffentliche WLAN-Hotspots, die keine ausreichende Sicherheit bieten, ermöglichen es Cyberkriminellen, Nachrichten abzufangen, Inhalte zu manipulieren oder Schadsoftware einzuschleusen. Darüber hinaus können unbekannte oder wenig verbreitete Messenger-Dienste, die keine umfassenden Sicherheitsmaßnahmen implementieren, persönliche Daten stehlen oder an Dritte weitergeben. Im Jahr 2024 wurden 55 % der bekannten Messenger-Sicherheitsvorfälle auf unzureichende Verschlüsselung oder die Nutzung unsicherer Netzwerke zurückgeführt. Besonders betroffen sind Nutzer, die auf nicht etablierte oder unsichere Dienste vertrauen.",
                    "beispiel": "Sie sind in einem Café und nutzen den kostenlosen WLAN-Hotspot, während Angreifer im Netzwerk Ihre Nachrichten mitlesen.",
                    "risiken": [
                        "NAngreifer können Nachrichten aufgrund unzureichender Verschlüsselung abfangen und einsehen.",
                        "In öffentlichen Netzwerken können Nachrichten manipuliert oder gefälschte Inhalte eingefügt werden.",
                        "Nicht etablierte Messenger-Dienste können persönliche Daten und Nachrichten stehlen oder missbrauchen."
                    ],
                    "barrieren": "Unzureichende Verschlüsselung und unsichere Netzwerke sind für Nutzer oft nicht erkennbar, da die Kommunikation scheinbar normal funktioniert. Viele Nutzer nutzen ungesicherte Netzwerke oder unbekannte Messenger-Dienste, ohne die potenziellen Risiken zu bedenken. Die folgenden Empfehlungen helfen Ihnen, sich vor diesen Gefahren zu schützen.",
                    "empfehlungen": {
                        "Nutzen Sie Messenger mit Ende-zu-Ende-Verschlüsselung": "Nutzen Sie Messenger mit Ende-zu-Ende-Verschlüsselung: Verwenden Sie nur Dienste, die eine starke Verschlüsselung bieten, um Ihre Nachrichten vor dem Zugriff Dritter zu schützen.",
                        "Vermeiden Sie öffentliche WLAN-Hotspots": "Vermeiden Sie öffentliche WLAN-Hotspots: Führen Sie den Austausch sensibler Informationen nicht in öffentlichen Netzwerken durch, es sei denn, Sie nutzen ein VPN (Virtual Private Network).",
                        "Verwenden Sie etablierte Messenger-Dienste": "Verwenden Sie etablierte Messenger-Dienste: Nutzen Sie nur bekannte und weit verbreitete Messenger-Apps, die regelmäßig aktualisiert und auf Sicherheitsstandards geprüft werden.",
                        "Achten Sie auf Netzwerk-Sicherheit": "Achten Sie auf Netzwerk-Sicherheit: Deaktivieren Sie die automatische Verbindung zu öffentlichen Netzwerken, um das Risiko ungesicherter Verbindungen zu minimieren.",
                        "Seien Sie vorsichtig mit neuen oder unbekannten Diensten": "Seien Sie vorsichtig mit neuen oder unbekannten Diensten: Vermeiden Sie die Nutzung von Messengern, die keine klaren Informationen zu Sicherheit und Datenschutz bieten."
                    },
                    "umsetzung": {
                        "Whatsapp App": [
                            "Whatsapp bietet standardmäßig eine Ende-zu-Ende-Verschlüsselung für alle Chats und Anrufe. Stellen Sie sicher, dass Ihre Kontakte ebenfalls die neueste Version von WhatsApp nutzen, um die Verschlüsselung zu gewährleisten."
                        ],
                        "Telegram App": [
                            "Öffnen Sie einen Chat und klicken Sie auf den Namen des Kontakts. Über die drei Punkte können Sie einen geheimen Chat starten für eine Ende-zu-Ende-Verschlüsselung."
                        ],
                        "Signal App":[
                            "Signal bietet standardmäßig eine Ende-zu-Ende-Verschlüsselung für alle Chats und Anrufe. Stellen Sie sicher, dass Ihre Kontakte ebenfalls die neueste Version von Signal nutzen, um die Verschlüsselung zu gewährleisten."
                        ]
                    }
                }
        }
    }
},






#Banking
    "Online Banking": {
        "Laptop und Desktop-PC": {
            "bedrohung": {
                "Social Engineering - Phishing": {
                    "kontext": "Beim Online-Banking können Verbraucher Opfer von Betrügern werden, die sich als Bankmitarbeiter ausgeben, um sensible Daten wie Kontoinformationen oder TANs (Transaktionsnummern) zu stehlen. Zudem besteht die Gefahr, dass Nutzer durch gefälschte Webseiten oder Apps der Bank ihre Zugangsdaten preisgeben, was zu unbefugtem Zugriff auf ihre Konten führen kann. Angreifer setzen gezielte Social-Engineering-Taktiken ein, um Vertrauen zu gewinnen und Bankdaten wie Passwörter oder TANs zu stehlen. Phishing-E-Mails, gefälschte Webseiten oder Anrufe von „Bankmitarbeitern“ sind gängige Methoden. Erhalten Betrüger Zugriff auf Kontodaten oder TANs, führen Sie unbefugte Transaktionen aus oder räumen Konten leer. Im Jahr 2024 wurden weltweit Millionen von Betrugsfällen durch Phishing und gefälschte Bankseiten gemeldet, die Verbraucher um Milliardenbeträge brachten.",
                    "beispiel": "Sehr geehrter Kunde, Ihr Konto wurde aufgrund verdächtiger Aktivitäten gesperrt. Bitte melden Sie sich unter folgendem Link an, um Ihr Konto zu entsperren.",
                    "risiken": [
                        "Die Weitergabe von Bankdaten oder TANs an Betrüger ermöglicht unbefugte Transaktionen und den Zugriff auf Konten.",
                        "Gefälschte Bankseiten oder Apps können Ihre Zugangsdaten abfangen und missbrauchen.",
                        "Durch den Verlust von Zugangsdaten können erhebliche finanzielle Schäden entstehen. "
                    ],
                    "barrieren": "Betrüger agieren oft geschickt, um Vertrauen zu gewinnen. Viele Nutzer erkennen die Gefahren nicht, da Phishing-Nachrichten oder gefälschte Webseiten täuschend echt gestaltet sind. Die folgenden Empfehlungen helfen Ihnen, diese Gefahren zu minimieren.",
                    "empfehlungen": {
                        "Geben Sie keine sensiblen Daten weiter": "Geben Sie keine sensiblen Daten weiter: Banken werden Sie niemals per E-Mail, SMS oder Anruf nach Ihren Zugangsdaten oder TANs fragen. Geben Sie diese Informationen niemals weiter.",
                        "Prüfen Sie die URL der Webseite": "Prüfen Sie die URL der Webseite: Stellen Sie sicher, dass die Webseite Ihrer Bank mit „https“ beginnt und die korrekte Adresse hat. Achten Sie auch auf das Schlosssymbol in der Adressleiste.",
                        "Nutzen Sie nur die offizielle Banking-App": "Nutzen Sie nur die offizielle Banking-Webseite: Laden Sie Apps ausschließlich aus den offiziellen App-Stores und überprüfen Sie die Entwicklerangaben.",
                        "Seien Sie skeptisch bei unerwarteten Nachrichten": "Seien Sie skeptisch bei unerwarteten Nachrichten: Ignorieren Sie E-Mails oder SMS, die Sie auffordern, persönliche Daten einzugeben, insbesondere wenn diese mit Dringlichkeit oder Drohungen arbeiten.",
                        "Aktivieren Sie Zwei-Faktor-Authentifizierung": "Aktivieren Sie Zwei-Faktor-Authentifizierung: Nutzen Sie Sicherheitsmaßnahmen wie TAN-Generatoren oder Apps mit Zwei-Faktor-Authentifizierung, um Ihre Transaktionen abzusichern. ",
                        "Überprüfen Sie regelmäßig Ihre Kontobewegungen":"Überprüfen Sie regelmäßig Ihre Kontobewegungen: Melden Sie verdächtige Aktivitäten sofort Ihrer Bank."
                    },
                    "umsetzung": {
                        "Einstellung in der jeweiligen Webanwendung Ihrer Bank": [
                            "Aktivieren Sie in den Einstellungen die Zwei-Faktor-Authentifizierung. Auch wenn ein Angreifer Ihr Passwort abgegriffen haben sollte, kann sich dieser durch Ihre Zwei-Faktor-Authentifizierung nicht mit Ihrem Bankkonto anmelden.",
                            "Prüfen Sie die URL Ihrer Bank in Ihrem Browser und speichern Sie diese als Lesezeichen, um versehentliche Besuche auf Phishing-Webseiten zu vermeiden."
                    
                        ]
                    }
                },

                "Netzwerk und Verschlüsselung": {
                    "kontext": "Beim Online-Banking können unsichere Banking-Seiten oder Apps dazu führen, dass Zugangsdaten abgegriffen werden. Angreifer können sich über unsichere Verbindungen in die Kommunikation einschalten und Bankdaten stehlen. Die Nutzung ungeprüfter oder unsicherer Seiten erhöht das Risiko, dass Daten abgefangen werden. Cookies oder offene Sitzungen können Angreifern direkten Zugriff auf Konten oder Informationen über Ihre Online-Banking-Aktivitäten gewähren. Unsichere Verbindungen oder Banking-Seiten ohne ausreichende Sicherheitsmaßnahmen sind ein häufiges Ziel für Angriffe. Angreifer nutzen Schwachstellen, um sich in die Kommunikation einzuklinken oder Daten abzufangen. Nicht gelöschte oder an Dritte weitergegebene Cookies enthalten oft Informationen über Online-Banking-Aktivitäten. Zudem bietet das Nicht-Abmelden von Bankkonten Angreifern eine Gelegenheit, bestehende Sitzungen auszunutzen. Im Jahr 2024 wurden laut einem Bericht 40 % der Cyberangriffe auf Banken und deren Kunden durch unsichere Verbindungen oder Cookies ermöglicht.",
                    "beispiel": "Eine ungesicherte Verbindung zu einer Banking-Seite wird von Angreifern genutzt, um Login-Daten abzufangen.",
                    "risiken": [
                        "Unsichere Seiten oder Verbindungen können dazu führen, dass Angreifer Zugangsdaten abgreifen und Konten kompromittieren.",
                        "Ungeprüfte Seiten oder Apps, die wie Banking-Plattformen aussehen, können sensible Daten stehlen.",
                        "Nicht gelöschte Cookies können Angreifern Zugriff auf Banking-Aktivitäten oder bestehende Sitzungen ermöglichen.",
                        "Das Nicht-Abmelden von Sitzungen kann Angreifern direkten Zugriff auf ein Konto verschaffen."
                    ],
                    "barrieren": "Viele Nutzer erkennen nicht, ob eine Verbindung oder Seite sicher ist. Cookies und offene Sitzungen können Angreifern direkten Zugriff auf Konten oder Informationen über Ihre Online-Banking-Aktivitäten ermöglichen. Mit den folgenden Empfehlungen können Sie sich vor diesen Gefahren schützen.",
                    "empfehlungen": {
                        "Nutzen Sie nur gesicherte Banking-Seiten": "Nutzen Sie nur gesicherte Banking-Seiten: Achten Sie darauf, dass die URL Ihrer Bank mit „https“ beginnt und ein Schlosssymbol angezeigt wird.",
                        "Verwenden Sie die offizielle Banking-App": "Nutzen Sie die offizielle Banking-App: Laden Sie Apps ausschließlich aus offiziellen App-Stores und überprüfen Sie, ob sie von Ihrer Bank bereitgestellt wurden.",
                        "Vermeiden Sie unsichere Verbindungen": "Vermeiden Sie unsichere Verbindungen: Führen Sie Online-Banking nur über gesicherte Netzwerke durch. Vermeiden Sie öffentliche WLAN-Hotspots oder nutzen Sie ein VPN für zusätzlichen Schutz.",
                        "Überprüfen Sie Seiten und Apps": "Überprüfen Sie Seiten und Apps: Nutzen Sie nur von Ihrer Bank offiziell empfohlene Seiten oder Apps. Vermeiden Sie Links aus E-Mails oder Suchmaschinen, die Sie auf Banking-Seiten leiten.",
                        "Löschen Sie Cookies regelmäßig": "Löschen Sie Cookies regelmäßig: Konfigurieren Sie Ihren Browser so, dass Cookies nach jeder Sitzung gelöscht werden. Nutzen Sie Browser-Erweiterungen, um Tracking zu minimieren.",
                        "Melden Sie sich nach jeder Sitzung ab":"Melden Sie sich nach jeder Sitzung ab: Verlassen Sie Ihr Online-Banking vollständig, besonders auf gemeinsam genutzten Geräten.",
                        "Deaktivieren Sie Cookies für Dritte":"Deaktivieren Sie Cookies für Dritte: Konfigurieren Sie Ihren Browser so, dass Dritte nicht auf Ihre Banking-Aktivitäten zugreifen können.",
                        "Aktivieren Sie Zwei-Faktor-Authentifizierung":"Aktivieren Sie Zwei-Faktor-Authentifizierung: Nutzen Sie Sicherheitsmaßnahmen, wie TAN-Generatoren oder Authentifizierungs-Apps, um Ihre Konten zusätzlich zu schützen."
                    },
                    "umsetzung": {
                        "Microsoft Edge": [
                            "Überprüfen Sie die URL der Webanwendung Ihrer Bank. Stellen Sie sicher, dass oben in der URL-Leiste vor der Webseite ein Schloss abgebildet ist und ein 'https' vor der Webseite steht. So überprüfen Sie, ob Ihre Verbindung sicher ist.",
                            "Öffnen Sie über die drei Punkte oben rechts die Einstellungen. Gehen Sie auf 'Cookies und Websiteberechtigungen' und wählen Sie 'Cookies und gespeicherte Daten' aus. Aktivieren Sie unter 'Verwalten und Löschen von Cookies und Websitedaten' die Option 'Cookies von Drittanbietern blockieren', um Webseiten zu untersagen, Ihre Aktivitäten im Web nachzuverfolgen."
                        ],
                        "Google Chrome":[
                            "Überprüfen Sie die URL der Webanwendung Ihrer Bank. Stellen Sie sicher, dass oben in der URL-Leiste vor der Webseite ein Schloss abgebildet ist und ein 'https' vor der Webseite steht. So überprüfen Sie, ob Ihre Verbindung sicher ist.",
                            "Öffnen Sie über die drei Punkte oben rechts die Einstellungen. Wählen Sie 'Datenschutz und Sicherheit' aus und aktivieren Sie unter 'Drittanbieter-Cookies' die Option 'Drittanbieter-Cookies blockieren', um Webseiten zu untersagen, Ihre Aktivitäten im Web nachzuverfolgen."

                        ],
                        "Safari":[
                            "Überprüfen Sie die URL der Webanwendung Ihrer Bank. Stellen Sie sicher, dass oben in der URL-Leiste vor der Webseite ein Schloss abgebildet ist und ein 'https' vor der Webseite steht. So überprüfen Sie, ob Ihre Verbindung sicher ist.",
                            "Öffnen Sie die Einstellungen und wählen Sie 'Datenschutz' aus. Aktivieren Sie unter 'Datenschutz' die Option 'Cross-Site-Tracking verhindern', um Tracking durch Drittanbieter zu blockieren und Ihre Privatsphäre zu schützen."                            
                        ]
                        
                    }
                }    
                    
            }
        },

    
    "Smartphone und Tablet": {
        "bedrohung": {
            "Social Engineering - Phishing": {
                "kontext": "Beim Online-Banking können Verbraucher Opfer von Betrügern werden, die sich als Bankmitarbeiter ausgeben, um sensible Daten wie Kontoinformationen oder TANs (Transaktionsnummern) zu stehlen. Zudem besteht die Gefahr, dass Nutzer durch gefälschte Webseiten oder Apps der Bank ihre Zugangsdaten preisgeben, was zu unbefugtem Zugriff auf ihre Konten führen kann. Cyberkriminelle nutzen häufig Social Engineering, um Vertrauen zu erlangen und sensible Bankdaten von Verbrauchern zu stehlen. Phishing-E-Mails, gefälschte Webseiten oder Anrufe von „Bankmitarbeitern“ sind gängige Methoden. Sobald Betrüger Zugriff auf Kontodaten oder TANs erhalten, können sie unbefugte Transaktionen ausführen oder Konten leerräumen. Im Jahr 2024 wurden weltweit Millionen von Betrugsfällen durch Phishing und gefälschte Bankseiten gemeldet, die Verbraucher um Milliardenbeträge brachten.",
                    "beispiel": "Sehr geehrter Kunde, Ihr Konto wurde aufgrund verdächtiger Aktivitäten gesperrt. Bitte melden Sie sich unter folgendem Link an, um Ihr Konto zu entsperren.",
                    "risiken": [
                        "Die Weitergabe von Bankdaten oder TANs an Betrüger ermöglicht unbefugte Transaktionen und den Zugriff auf Konten.",
                        "Gefälschte Bankseiten oder Apps können Ihre Zugangsdaten abfangen und missbrauchen.",
                        "Durch den Verlust von Zugangsdaten können erhebliche finanzielle Schäden entstehen. "
                    ],
                    "barrieren": "Angreifer setzen gezielte Phishing-Taktiken ein, um Vertrauen zu erlangen. Gefälschte Nachrichten, Anrufe oder Webseiten wirken oft täuschend echt, wodurch viele Nutzer die Gefahren nicht erkennen. Die folgenden Empfehlungen helfen Ihnen, diese Gefahren zu minimieren.",
                    "empfehlungen": {
                        "Geben Sie keine sensiblen Daten weiter": "Geben Sie keine sensiblen Daten weiter: Banken werden Sie niemals per E-Mail, SMS oder Anruf nach Ihren Zugangsdaten oder TANs fragen. Geben Sie diese Informationen niemals weiter.",
                        "Prüfen Sie die URL der Webseite": "Prüfen Sie die URL der Webseite: Stellen Sie sicher, dass die Webseite Ihrer Bank mit „https“ beginnt und die korrekte Adresse hat. Achten Sie auch auf das Schlosssymbol in der Adressleiste.",
                        "Nutzen Sie nur die offizielle Banking-App": "Nutzen Sie nur die offizielle Banking-App: Laden Sie Apps ausschließlich aus den offiziellen App-Stores und überprüfen Sie die Entwicklerangaben.",
                        "Seien Sie skeptisch bei unerwarteten Nachrichten": "Seien Sie skeptisch bei unerwarteten Nachrichten: Ignorieren Sie E-Mails oder SMS, die Sie auffordern, persönliche Daten einzugeben, insbesondere wenn diese mit Dringlichkeit oder Drohungen arbeiten.",
                        "Aktivieren Sie Zwei-Faktor-Authentifizierung": "Aktivieren Sie Zwei-Faktor-Authentifizierung: Nutzen Sie Sicherheitsmaßnahmen wie TAN-Generatoren oder Apps mit Zwei-Faktor-Authentifizierung, um Ihre Transaktionen abzusichern. ",
                        "Überprüfen Sie regelmäßig Ihre Kontobewegungen":"Überprüfen Sie regelmäßig Ihre Kontobewegungen: Melden Sie verdächtige Aktivitäten sofort Ihrer Bank."
                    },
                    "umsetzung": {
                        "Einstellungen innerhalb der jeweiligen Banking-App Ihrer Bank": [
                            "Aktivieren Sie Push-Benachrichtigungen: Überwachen Sie Transaktionen in Echtzeit, indem Sie Benachrichtigungen über Ihre Banking-App aktivieren. So können Sie verdächtige Aktivitäten sofort melden.",
                            "Aktivieren Sie die Zwei-Faktor-Authentifizierung. Auch wenn ein Angreifer Ihr Passwort abgegriffen haben sollte, kann sich dieser durch Ihre 2-Faktor-Authentifizierung nicht mit Ihrem Bankkonto anmelden."
                        ]
                    }
                },
            "Netzwerk und Verschlüsselung": {
                    "kontext": "Beim Online-Banking können unsichere Banking-Seiten oder Apps dazu führen, dass Zugangsdaten abgegriffen werden. Angreifer können sich über unsichere Verbindungen in die Kommunikation einschalten und Bankdaten stehlen. Die Nutzung ungeprüfter oder unsicherer Seiten erhöht das Risiko, dass Daten abgefangen werden. Nicht gelöschte Cookies oder das Nicht-Abmelden von Sitzungen können Angreifern ermöglichen, Online-Banking-Aktivitäten einzusehen oder direkten Zugriff auf Konten zu erhalten. Offene WLAN-Hotspots oder schwach verschlüsselte Netzwerke ermöglichen es Angreifern, auf sensible Banking-Daten zuzugreifen. Nicht gelöschte oder an Dritte weitergegebene Cookies enthalten oft Informationen über Online-Banking-Aktivitäten. Zudem bietet das Nicht-Abmelden von Bankkonten Angreifern eine Gelegenheit, bestehende Sitzungen auszunutzen. Im Jahr 2024 wurden laut einem Bericht 40 % der Cyberangriffe auf Banken und deren Kunden durch unsichere Verbindungen oder Cookies ermöglicht.",
                    "beispiel": "Eine ungesicherte Verbindung zu einer Banking-Seite wird von Angreifern genutzt, um Login-Daten abzufangen.",
                    "risiken": [
                        "Unsichere Seiten oder Verbindungen können dazu führen, dass Angreifer Zugangsdaten abgreifen und Konten kompromittieren.",
                        "Ungeprüfte Seiten oder Apps, die wie Banking-Plattformen aussehen, können sensible Daten stehlen.",
                        "Nicht gelöschte Cookies ermöglichen Angreifern Einblick in Banking-Aktivitäten oder den Zugriff auf bestehende Sitzungen.",
                        "Das Nicht-Abmelden von Sitzungen kann Angreifern direkten Zugriff auf ein Konto verschaffen."
                    ],
                    "barrieren": "Viele Nutzer erkennen nicht, ob eine Verbindung oder Seite sicher ist. Cookies und offene Sitzungen werden oft unbedacht hinterlassen, ohne die potenziellen Risiken zu bedenken. Mit den folgenden Empfehlungen können Sie sich vor diesen Gefahren schützen.",
                    "empfehlungen": {
                        "Nutzen Sie nur gesicherte Banking-Seiten": "Nutzen Sie nur gesicherte Banking-Seiten: Achten Sie darauf, dass die URL Ihrer Bank mit „https“ beginnt und ein Schlosssymbol angezeigt wird.",
                        "Verwenden Sie die offizielle Banking-App": "Nutzen Sie die offizielle Banking-App: Laden Sie Apps ausschließlich aus offiziellen App-Stores und überprüfen Sie, ob sie von Ihrer Bank bereitgestellt wurden.",
                        "Vermeiden Sie unsichere Verbindungen": "Vermeiden Sie unsichere Verbindungen: Führen Sie Online-Banking nur über gesicherte Netzwerke durch. Vermeiden Sie öffentliche WLAN-Hotspots oder nutzen Sie ein VPN für zusätzlichen Schutz.",
                        "Überprüfen Sie Seiten und Apps": "Überprüfen Sie Seiten und Apps: Nutzen Sie nur von Ihrer Bank offiziell empfohlene Seiten oder Apps. Vermeiden Sie Links aus E-Mails oder Suchmaschinen, die Sie auf Banking-Seiten leiten.",
                        "Löschen Sie Cookies regelmäßig": "Löschen Sie Cookies regelmäßig: Konfigurieren Sie Ihren Browser so, dass Cookies nach jeder Sitzung gelöscht werden. Nutzen Sie Browser-Erweiterungen, um Tracking zu minimieren.",
                        "Melden Sie sich nach jeder Sitzung ab":"Melden Sie sich nach jeder Sitzung ab: Stellen Sie sicher, dass Sie sich nach der Nutzung von Online-Banking vollständig abmelden, insbesondere auf gemeinsam genutzten Geräten.",
                        "Deaktivieren Sie Cookies für Dritte":"Deaktivieren Sie Cookies für Dritte: Konfigurieren Sie Ihren Browser so, dass Dritte nicht auf Ihre Banking-Aktivitäten zugreifen können.",
                        "Aktivieren Sie Zwei-Faktor-Authentifizierung":"Aktivieren Sie Zwei-Faktor-Authentifizierung: Nutzen Sie Sicherheitsmaßnahmen, wie TAN-Generatoren oder Authentifizierungs-Apps, um Ihre Konten zusätzlich zu schützen."
                    },
                    "umsetzung": {
                        "iOS": [
                            "Öffnen Sie die Einstellungen und gehen Sie zu 'Mobilfunk'. Wählen Sie unter 'SIMs' Ihre SIM aus und aktivieren Sie unter 'Sprache und Daten' die Nutzung von 5G oder 4G und deaktivieren Sie die Nutzung von 2G. Dies sorgt für eine sichere Verschlüsselung auf Ihrem Smartphone.",
                        ],
                        "Android": [
                            "Öffnen Sie die Einstellungen und gehen Sie zu 'Verbindungen' oder 'Netzwerk und Internet'. Wählen Sie 'Mobile Netzwerke' oder 'Mobilfunknetz' aus und suchen Sie nach der Option 'Netzwerkmodus' oder 'Bevorzugter Netzwerktyp'. Wählen Sie die Option '5G/LTE/3G/2G' aus und aktivieren Sie die Nutzung von 5G oder 4G. Deaktivieren Sie die Nutzung von 2G, um für eine sichere Verschlüsselung auf Ihrem Smartphone zu sorgen.",
                        ]
                    }
                }
        }
    }
},










#Social MEdia
"Soziale Medien": {
        "Laptop und Desktop-PC": {
            "bedrohung": {
                "Social Engineering - Phishing": {
                    "kontext": "Öffentliche Profile liefern Angreifern leicht zugängliche Informationen, die für Identitätsdiebstahl oder Betrugsmaschen genutzt werden können. Besonders gefährlich ist die Kombination von Daten aus mehreren sozialen Netzwerken. Das Preisgeben zahlreicher persönlicher Daten erhöht dieses Risiko zusätzlich. Nicht gelöschte, ungenutzte Konten stellen ebenfalls ein Sicherheitsrisiko dar, da sie von Angreifern übernommen werden können. Zudem kann das Klicken auf Werbung oder Links in sozialen Medien zu gefälschten Webseiten führen, die Schadsoftware verbreiten oder Daten abgreifen. Social-Media-Plattformen liefern Angreifern eine Fülle an Informationen. Öffentliche Profile erlauben es ihnen, persönliche Details wie Wohnort, Arbeitsplatz oder Beziehungsstatus zu ermitteln, was Identitätsdiebstahl erleichtert. Auch alte, ungenutzte Konten können gehackt und missbraucht werden. Werbung und Links in sozialen Netzwerken sind häufig mit Phishing-Seiten oder Schadsoftware verbunden, die Geräte infizieren oder Daten abgreifen. Laut einer Studie aus dem Jahr 2024 war Social Media die Quelle für rund 40 % der Fälle von Identitätsdiebstahl und 30 % der gemeldeten Schadsoftware-Infektionen.",
                    "beispiel": "Ein Angreifer erstellt ein gefälschtes Profil und behauptet, Sie zu sein. Er nutzt Ihre Freunde, um persönliche Daten oder Geld zu erschleichen, indem er sich auf eine vermeintliche Notlage beruft.",
                    "risiken": [
                        "Öffentliche Profile und die Preisgabe persönlicher Informationen erleichtern Identitätsdiebstahl und Betrug.",
                        "Ungenutzte Konten können von Angreifern übernommen und missbraucht werden.",
                        "Werbung und Links in sozialen Netzwerken können zu gefälschten Webseiten führen, die Schadsoftware enthalten."
                    ],
                    "barrieren": "Viele Nutzer unterschätzen die Gefahren öffentlicher Profile und die Menge an Informationen, die sie preisgeben. Unbewusstes Klicken auf Werbung oder Links ist ein weiteres Risiko, das durch mangelnde Vorsicht verstärkt wird. Die folgenden Empfehlungen helfen, diese Gefahren zu minimieren.",
                    "empfehlungen": {
                        "Überprüfen Sie Ihre Profileinstellungen": "Überprüfen Sie Ihre Profileinstellungen: Stellen Sie sicher, dass Ihre Social-Media-Profile privat sind und nur von vertrauenswürdigen Personen eingesehen werden können.",
                        "Teilen Sie keine sensiblen Informationen": "Teilen Sie keine sensiblen Informationen: Vermeiden Sie es, Details wie Adresse, Telefonnummer, Geburtsdatum oder finanzielle Informationen öffentlich preiszugeben.",
                        "Löschen Sie ungenutzte Konten": "Löschen Sie ungenutzte Konten: Schließen Sie alte oder nicht mehr verwendete Social-Media-Accounts, um deren Missbrauch zu verhindern.",
                        "Seien Sie vorsichtig mit Werbung und Links": "Seien Sie vorsichtig mit Werbung und Links: Klicken Sie nur auf Links oder Werbung, wenn Sie sicher sind, dass sie aus einer vertrauenswürdigen Quelle stammen. Nutzen Sie Sicherheitssoftware, um potenziell gefährliche Webseiten zu blockieren.",
                        "Überprüfen Sie Ihre Freundes- und Followerliste": "Überprüfen Sie Ihre Freundes- und Followerliste: Akzeptieren Sie nur Personen, die Sie kennen, und entfernen Sie verdächtige Kontakte.",
                        "Seien Sie skeptisch bei unerwarteten Nachrichten":"Seien Sie skeptisch bei unerwarteten Nachrichten: Öffnen Sie keine Anhänge oder Links aus Nachrichten, die Sie nicht erwarten oder von unbekannten Kontakten stammen."
                    },
                    "umsetzung": {
                        "Facebook im Browser": [
                            "Gehen Sie oben rechts auf Ihr Konto und öffnen Sie 'Einstellungen und Privatsphäre' und klicken Sie anschließend auf 'Einstellungen'. Auf der linken Seite unter 'Meta Kontenübersicht' wählen Sie 'Passwort und Sicherheit' aus. Unter den Kontoeinstellungen klicken Sie nochmal auf 'Passwort und Sicherheit'. Unter der Zweistufigen Authentifizierung wählen Sie Ihr Konto aus und wählen nach der Eingabe Ihres erhaltenen Sicherheitscodes eine Methode für die Zwei-Faktor-Authentifizierung aus. Selbst wenn ein Angreifer Ihr Passwort abgegriffen hat, kann er sich durch die Zwei-Faktor-Authentifizierung nicht in Ihr Bankkonto einloggen.",
                            "Gehen Sie oben rechts auf Ihr Konto und öffnen Sie 'Einstellungen und Privatsphäre' und klicken Sie anschließend auf 'Privatsphäre-Check'. Dort können Sie die Einsicht Ihrer Profilinformationen für die Öffentlichkeit limitieren, damit potenzielle Angreifer keinen Zugriff auf Ihre persönlichen Informationen haben."
                        ],
                        "Instagram im Browser": [
                            "Klicken Sie oben rechts auf Ihr Profilbild und öffnen Sie die Einstellungen. Gehen Sie auf 'Privatsphäre und Sicherheit' und klicken Sie unter 'Zwei-Faktor-Authentifizierung' auf 'Bearbeiten der Zwei-Faktor-Authentifizierung'. Dort können Sie eine beliebige Methode wählen, um Ihr Konto vor Angreifern zu schützen, selbst wenn diese über Ihr Passwort verfügen. ",
                            "Klicken Sie oben rechts auf Ihr Profilbild und öffnen Sie die Einstellungen. Gehen Sie auf 'Privatsphäre und Sicherheit' und wählen Sie 'Privates Konto aktivieren' aus, damit nur noch von Ihnen genehmigte Follower Ihre Beiträge sehen können. Dies sorgt dafür, dass Ihre persönlichen Informationen nicht von potenziellen Angreifern eingesehen werden können."
                        ]
                    }
                },
                "Netzwerk und Verschlüsselung": {
                    "kontext": "Öffentliche WLAN-Hotspots, die ungesichert oder schwach verschlüsselt sind, können leicht von Angreifern ausspioniert werden. Dadurch können Daten wie Anmeldedaten, Nachrichten oder Social-Media-Aktivitäten abgefangen werden. Unsichere Verbindungen können dazu führen, dass Zugangsdaten abgegriffen werden. Nicht gelöschte oder an Dritte weitergegebene Cookies ermöglichen es Angreifern, Einsicht in Social-Media-Aktivitäten zu erhalten und möglicherweise auch die Kontrolle über Konten zu übernehmen. Öffentliche WLAN-Hotspots werden oft ohne Sicherheitsvorkehrungen genutzt, was Angreifern die Möglichkeit gibt, sich unbemerkt in die Verbindung einzuschalten und Daten abzufangen. Schwache oder fehlende Verschlüsselung macht es leicht, sensible Informationen wie Zugangsdaten zu stehlen. Nicht gelöschte oder an Dritte weitergegebene Cookies können detaillierte Informationen über Social-Media-Aktivitäten preisgeben und das Nutzerverhalten nachvollziehbar machen. Eine Untersuchung aus dem Jahr 2024 ergab, dass 60 % der Angriffe auf Social-Media-Konten durch unsichere Verbindungen oder die Nutzung öffentlicher Netzwerke ermöglicht wurden. ",
                    "beispiel": "Nicht gelöschte oder an Dritte weitergegebene Cookies ermöglichen es Angreifern, Einsicht in private Nachrichten oder Aktivitäten zu nehmen.",
                    "risiken": [
                        "Öffentliche Hotspots ermöglichen es Angreifern, Aktivitäten zu überwachen und Nachrichten oder Posts zu manipulieren.",
                        "Unsichere Verbindungen können dazu führen, dass Zugangsdaten abgefangen und missbraucht werden.",
                        "Nicht gelöschte Cookies können Angreifern Informationen über Social-Media-Aktivitäten liefern oder sogar den Zugriff auf Konten ermöglichen."
                    ],
                    "barrieren": "Viele Nutzer erkennen die Gefahren öffentlicher Netzwerke oder unsicherer Verbindungen nicht, da die Nutzung von Social Media scheinbar normal funktioniert. Die Auswirkungen nicht gelöschter Cookies werden oft unterschätzt. Mit den folgenden Empfehlungen können Sie diese Risiken minimieren.",
                    "empfehlungen": {
                        "Vermeiden Sie öffentliche WLAN-Hotspots": "Vermeiden Sie öffentliche WLAN-Hotspots: Nutzen Sie öffentliche Netzwerke nur, wenn es unbedingt erforderlich ist und führen Sie keine sensiblen Aktivitäten wie das Anmelden bei Social-Media-Konten durch.",
                        "Prüfen Sie die Sicherheit der Verbindung": "Prüfen Sie die Sicherheit der Verbindung: Achten Sie darauf, dass die URL mit „https“ beginnt und ein Schlosssymbol in der Adressleiste vorhanden ist.",
                        "Löschen Sie Cookies regelmäßig": "Löschen Sie Cookies regelmäßig: Stellen Sie Ihren Browser so ein, dass Cookies nach jeder Sitzung automatisch gelöscht werden, oder verwenden Sie Erweiterungen, um Tracking zu minimieren.",
                        "Deaktivieren Sie den Zugriff Ihrer Cookies durch Dritte": "Deaktivieren Sie Cookies für Dritte: Konfigurieren Sie Ihren Browser so, dass Dritte nicht auf Ihre Internet-Aktivitäten zugreifen können.",
                        "Melden Sie sich ab": "Melden Sie sich ab: Beenden Sie Social-Media-Sitzungen immer, bevor Sie ein öffentliches Netzwerk verlassen, um den Zugriff durch Dritte zu verhindern.",
                        "Überprüfen Sie Ihre Freundes- und Followerliste":"Überprüfen Sie Ihre Freundes- und Followerliste: Akzeptieren Sie nur Personen, die Sie kennen, und entfernen Sie verdächtige Kontakte.",
                        "Seien Sie vorsichtig mit geteilten Geräten":"Seien Sie vorsichtig mit geteilten Geräten: Wenn Sie Social Media auf fremden Geräten oder in öffentlichen Netzwerken nutzen, stellen Sie sicher, dass Sie sich vollständig abmelden und keine Daten speichern."
                    },
                    "umsetzung": {
                        "Microsoft Edge": [
                            "Öffnen Sie über die drei Punkte oben rechts die Einstellungen. Gehen Sie auf 'Datenschutz, Suche und Dienste' und wählen Sie unter 'Browserdaten löschen' die Option 'Wählen Sie aus, was beim Schließen des Browser gelöscht werden soll' aus. Aktivieren Sie 'Cookies und andere Websitedaten' aus. Das automatische Löschen Ihrer Cookies verhindert, dass Angreifer Ihre Browser-Sitzungen für Identitätsdiebstahl ausnutzen können. ",
                            "Öffnen Sie über die drei Punkte oben rechts die Einstellungen. Gehen Sie auf 'Cookies und Websiteberechtigungen' und gehen Sie unter 'Cookies und gespeicherte Daten' auf 'Verwalten und Löschen von Cookies und Websitedaten'. Aktivieren Sie die Option 'Cookies von Drittanbietern blockieren', um Webseiten zu untersagen, Ihre Aktivitäten im Web nachzuverfolgen."
                        ],
                        "Google Chrome":[
                            "Öffnen Sie über die drei Punkte oben rechts die Einstellungen. Wählen Sie 'Datenschutz und Sicherheit' die Option 'Browserdaten löschen' aus. Wählen Sie einen gewünschten Zeitraum und 'Cookies und andere Websitedaten' aus, und klicken Sie anschließend auf 'Daten löschen'. Das regelmäßige Löschen Ihrer Cookies führt dazu, dass Angreifer nicht Ihre Browser-Sitzungen für Identitätsdiebstahl ausnutzen können.",
                            "Öffnen Sie über die drei Punkte oben rechts die Einstellungen. Wählen Sie 'Datenschutz und Sicherheit'  aus und aktivieren Sie unter 'Drittanbieter-Cookies' die Option 'Drittanbieter-Cookies blockieren', um Webseiten zu untersagen, Ihre Aktivitäten im Web nachzuverfolgen."
                        ],
                        "Safari":[
                            "Öffnen Sie die Einstellungen und wählen Sie 'Datenschutz' aus. Gehen Sie auf 'Websitedaten verwalten' und wählen Sie entweder alle oder einzelne aus und klicken Sie dann auf 'Entfernen' oder 'Alle entfernen', um die Cookies zu löschen. Das regelmäßige Löschen Ihrer Cookies verhindert, dass Angreifer Ihre Browser-Sitzungen für Identitätsdiebstahl ausnutzen können.",
                            "Öffnen Sie die Einstellungen und wählen Sie 'Datenschutz' aus. Aktivieren Sie 'Websites daran hindern, Cross-Site-Tracking durchzuführen', um Webseiten zu untersagen, Ihre Aktivitäten im Web nachzuverfolgen."
                        ]

                    }
                }    
                    
            }
        },

    
    "Smartphone und Tablet": {
        "bedrohung": {
            "Social Engineering - Phishing": {
                "kontext": "Die Nutzung öffentlicher Social-Media-Profile birgt das Risiko, dass Angreifer persönliche Informationen einsehen und für Identitätsdiebstahl oder andere betrügerische Zwecke nutzen. Das Preisgeben zahlreicher persönlicher Daten erhöht dieses Risiko zusätzlich. Nicht gelöschte, ungenutzte Konten stellen ebenfalls ein Sicherheitsrisiko dar, da sie von Angreifern übernommen werden können. Zudem kann das Klicken auf Werbung oder Links in sozialen Medien zu gefälschten Webseiten führen, die Schadsoftware verbreiten oder Daten abgreifen. Social-Media-Plattformen liefern Angreifern eine Fülle an Informationen. Öffentliche Profile erlauben es ihnen, persönliche Details wie Wohnort, Arbeitsplatz oder Beziehungsstatus zu ermitteln, was Identitätsdiebstahl erleichtert. Auch alte, ungenutzte Konten können gehackt und missbraucht werden. Werbung und Links in sozialen Netzwerken sind häufig mit Phishing-Seiten oder Schadsoftware verbunden, die Geräte infizieren oder Daten abgreifen. Laut einer Studie aus dem Jahr 2024 war Social Media die Quelle für rund 40 % der Fälle von Identitätsdiebstahl und 30 % der gemeldeten Schadsoftware-Infektionen.",
                    "beispiel": "Ein Angreifer erstellt ein gefälschtes Profil mit Ihren Daten und kontaktiert Ihre Freunde, um Geld oder weitere Informationen zu erschleichen.",
                    "risiken": [
                        "Öffentliche Profile und die Preisgabe persönlicher Informationen erleichtern Identitätsdiebstahl und Betrug.",
                        "Ungenutzte Konten können von Angreifern übernommen und missbraucht werden.",
                        "Werbung und Links in sozialen Netzwerken können zu gefälschten Webseiten führen, die Schadsoftware enthalten."
                    ],
                    "barrieren": "Viele Nutzer unterschätzen die Gefahren öffentlicher Profile sowie die Menge preisgegebener Informationen. Unbewusstes Klicken auf Werbung oder Links ist ein weiteres Risiko, das durch mangelnde Vorsicht verstärkt wird. Die folgenden Empfehlungen helfen, diese Gefahren zu minimieren.",
                    "empfehlungen": {
                        "Überprüfen Sie Ihre Profileinstellungen": "Überprüfen Sie Ihre Profileinstellungen: Stellen Sie sicher, dass Ihre Social-Media-Profile privat sind und nur von vertrauenswürdigen Personen eingesehen werden können.",
                        "Teilen Sie keine sensiblen Informationen": "Teilen Sie keine sensiblen Informationen: Vermeiden Sie es, Details wie Adresse, Telefonnummer, Geburtsdatum oder finanzielle Informationen öffentlich preiszugeben.",
                        "Löschen Sie ungenutzte Konten": "Löschen Sie ungenutzte Konten: Schließen Sie alte oder nicht mehr verwendete Social-Media-Accounts, um deren Missbrauch zu verhindern.",
                        "Seien Sie vorsichtig mit Werbung und Links": "Seien Sie vorsichtig mit Werbung und Links: Klicken Sie nur auf Links oder Werbung, wenn Sie sicher sind, dass sie aus einer vertrauenswürdigen Quelle stammen. Nutzen Sie Sicherheitssoftware, um potenziell gefährliche Webseiten zu blockieren.",
                        "Überprüfen Sie Ihre Freundes- und Followerliste": "Überprüfen Sie Ihre Freundes- und Followerliste: Akzeptieren Sie nur Anfragen von Personen, die Sie kennen, und entfernen Sie verdächtige Kontakte",
                        "Seien Sie skeptisch bei unerwarteten Nachrichten":"Seien Sie skeptisch bei unerwarteten Nachrichten: Öffnen Sie keine Anhänge oder Links aus Nachrichten, die Sie nicht erwarten oder von unbekannten Kontakten stammen."
                    },
                    "umsetzung": {
                        "Facebook-App": [
                            "Gehen Sie unten rechts in das Menü und öffnen Sie 'Einstellungen und Privatsphäre' und klicken Sie anschließend auf 'Einstellungen'. Unter 'Meta Kontenübersicht' wählen Sie 'Mehr dazu in der Kontenübersicht aus und öffnen 'Passwort und Sicherheit'. Unter 'Zweistufige Authentifizierung' wählen Sie Ihr Konto aus und wählen nach der Eingabe Ihres erhaltenen Sicherheitscodes eine Methode für die Zwei-Faktor-Authentifizierung aus. Somit schützen Sie Ihr Konto vor Angreifern, selbst wenn diese über Ihr Passwort verfügen.",
                            "Gehen Sie unten rechts in das Menü, öffnen Sie 'Einstellungen und Privatsphäre' und wählen Sie anschließend 'Privatsphäre-Check'. Dort können Sie die Einsicht Ihrer Profilinformationen für die Öffentlichkeit limitieren, damit potenzielle Angreifer keinen Zugriff auf Ihre persönlichen Informationen haben."
                        ],
                        "Instagram-App": [
                            "Gehen Sie oben rechts auf Ihr Profilbild und öffnen Sie die Einstellungen. Gehen Sie auf 'Privatsphäre und Sicherheit' und wählen Sie unter 'Zwei-Faktor-Authentifizierung' auf 'Bearbeiten der Zwei-Faktor-Authentifizierung'. Dort können Sie eine beliebige Methode wählen, um Ihr Konto vor Angreifern zu schützen, selbst wenn diese über Ihr Passwort verfügen. ",
                            "Gehen Sie oben rechts auf Ihr Profilbild und öffnen Sie die Einstellungen. Gehen Sie auf 'Privatsphäre und Sicherheit' und wählen Sie 'Privates Konto aktivieren' aus, damit nur noch von Ihnen genehmigte Follower Ihre Beiträge sehen können. Dies sorgt dafür, dass Ihre persönlichen Informationen nicht von potenziellen Angreifern eingesehen werden können."
                        ]
                }
            },
            "Netzwerk und Verschlüsselung": {
                    "kontext": "Die Nutzung öffentlicher Hotspots ohne Schutzmaßnahmen birgt das Risiko, dass Angreifer die Aktivitäten von Nutzern überwachen oder manipulieren. Unsichere Verbindungen können dazu führen, dass Zugangsdaten abgegriffen werden. Nicht gelöschte oder an Dritte weitergegebene Cookies ermöglichen es Angreifern, Einsicht in Social-Media-Aktivitäten zu erhalten und möglicherweise auch die Kontrolle über Konten zu übernehmen. Öffentliche WLAN-Hotspots werden oft ohne Sicherheitsvorkehrungen genutzt, was Angreifern die Möglichkeit gibt, sich unbemerkt in die Verbindung einzuschalten und Daten abzufangen. Schwache oder fehlende Verschlüsselung macht es leicht, sensible Informationen wie Zugangsdaten zu stehlen. Nicht gelöschte oder an Dritte weitergegebene Cookies können detaillierte Informationen über Social-Media-Aktivitäten preisgeben und das Nutzerverhalten nachvollziehbar machen. Eine Untersuchung aus dem Jahr 2024 ergab, dass 60 % der Angriffe auf Social-Media-Konten durch unsichere Verbindungen oder die Nutzung öffentlicher Netzwerke ermöglicht wurden. ",
                    "beispiel": "Nicht gelöschte Cookies geben Angreifern potenziell Zugriff auf private Nachrichten oder Aktivitäten.",
                    "risiken": [
                        "Öffentliche Hotspots ermöglichen es Angreifern, Aktivitäten zu überwachen und Nachrichten oder Posts zu manipulieren.",
                        "Unsichere Verbindungen können dazu führen, dass Zugangsdaten abgefangen und missbraucht werden.",
                        "Nicht gelöschte Cookies können Angreifern Informationen über Social-Media-Aktivitäten liefern oder sogar den Zugriff auf Konten ermöglichen."
                    ],
                    "barrieren": "Viele Nutzer erkennen die Gefahren öffentlicher Netzwerke oder unsicherer Verbindungen nicht, da die Nutzung von Social Media keine Auffälligkeiten zeigt. Die Auswirkungen nicht gelöschter Cookies werden oft unterschätzt. Mit den folgenden Empfehlungen können Sie diese Risiken minimieren.",
                    "empfehlungen": {
                        "Vermeiden Sie öffentliche WLAN-Hotspots": "Vermeiden Sie öffentliche WLAN-Hotspots: Nutzen Sie öffentliche Netzwerke nur, wenn es unbedingt erforderlich ist und führen Sie keine sensiblen Aktivitäten wie das Anmelden bei Social-Media-Konten durch.",
                        "Prüfen Sie die Sicherheit der Verbindung": "Prüfen Sie die Sicherheit der Verbindung: Achten Sie darauf, dass die URL mit „https“ beginnt und ein Schlosssymbol in der Adressleiste vorhanden ist.",
                        "Löschen Sie Cookies regelmäßig": "Löschen Sie Cookies regelmäßig: Konfigurieren Sie Ihren Browser so, dass Cookies nach jeder Sitzung automatisch entfernt werden, oder verwenden Sie Erweiterungen, um Tracking zu verhindern.",
                        "Deaktivieren Sie den Zugriff Ihrer Cookies durch Dritte": "Deaktivieren Sie Cookies für Dritte: Konfigurieren Sie Ihren Browser so, dass Dritte nicht auf Ihre Banking-Aktivitäten zugreifen können.",
                        "Melden Sie sich ab": "Melden Sie sich ab: Beenden Sie Social-Media-Sitzungen immer, bevor Sie ein öffentliches Netzwerk verlassen, um den Zugriff durch Dritte zu verhindern.",
                        "Überprüfen Sie Ihre Freundes- und Followerliste":"Überprüfen Sie Ihre Freundes- und Followerliste: Akzeptieren Sie nur Personen, die Sie kennen, und entfernen Sie verdächtige Kontakte.",
                        "Seien Sie vorsichtig mit geteilten Geräten":"Seien Sie vorsichtig mit geteilten Geräten: Wenn Sie Social Media auf fremden Geräten oder in öffentlichen Netzwerken nutzen, melden Sie sich vollständig ab und speichern Sie keine Daten."
                    },
                    "umsetzung": {
                        "Facebook-App": [
                            "Die Facebook-App verwendet standardmäßig eine HTTPS-Verbindung, somit sind Ihre Daten innerhalb der Facebook-App für Angreifer verschlüsselt, sodass diese Ihre Daten nicht ohne Weiteres einsehen können.",
                            "Gehen Sie unten rechts in das Menü und öffnen Sie 'Einstellungen und Privatsphäre' und klicken Sie anschließend auf 'Einstellungen'. Weiter unten unter 'Deine Aktivitäten und Benachrichtigungen' öffnen Sie 'Apps und Webseiten'. Hier können Sie Apps und Webseiten den Zugriff auf Ihre Daten verbieten, wenn Sie diesen nicht vertrauen."
                        ],
                        "Instagram-App": [
                            "Die Instagram-App verwendet standardmäßig eine HTTPS-Verbindung. Dadurch sind Ihre Daten verschlüsselt, und Angreifer können sie nicht ohne Weiteres einsehen.",
                            "Gehen Sie auf Ihr Profil und öffnen Sie oben rechts das Menü. Öffnen Sie dort die Einstellungen und gehen Sie zu 'Sicherheit'. Unter 'Apps und Webseiten', können Sie Apps und Webseiten den Zugriff auf Ihre Daten verbieten, wenn Sie diesen nicht vertrauen. "
                        ]
                    }
                }
        }
    }
},

 
 




#Ware ein- und verkaufen
"Waren Ein- oder Verkaufen": {
        "Laptop und Desktop-PC": {
            "bedrohung": {
                "Social Engineering - Phishing": {
                    "kontext": "Beim Online-Handel besteht die Gefahr, dass Zahlungen außerhalb der Plattform erfolgen, wodurch der Käuferschutz nicht greift und Sie Betrügern ausgesetzt sein können. Unsichere oder gefälschte Online-Shops können persönliche Daten abgreifen oder Schadsoftware auf Ihr Gerät laden. Das Anklicken von Links in gefälschten oder unsicheren Shops birgt ähnliche Risiken. Zahlungsinformationen sollten niemals über E-Mail, Telefon oder Nachrichten weitergegeben werden, da Angreifer diese für Betrug oder Identitätsdiebstahl nutzen können. Plattformen für Online-Handel bieten oft Schutzmechanismen wie Käuferschutz oder sichere Zahlungsmethoden. Zahlungen außerhalb dieser Systeme setzen Käufer und Verkäufer jedoch einem hohen Risiko aus. Gefälschte Online-Shops oder unsichere Webseiten versuchen, Nutzer zu täuschen, indem sie attraktive Angebote präsentieren, die persönliche Daten oder Zahlungsinformationen abgreifen sollen. Zudem sind Phishing-Links in Nachrichten oder E-Mails eine häufig genutzte Methode, um Malware zu verbreiten oder Daten zu stehlen. Im Jahr 2024 berichteten 45 % der Online-Käufer, dass sie mindestens einmal auf einen gefälschten Online-Shop hereingefallen sind oder Opfer von Zahlungsbetrug wurden. ",
                    "beispiel": "Eine gefälschte Shop-Seite lockt Sie mit unschlagbaren Angeboten und stiehlt Ihre Zahlungsinformationen beim Checkout.",
                    "risiken": [
                        "Zahlungen außerhalb der Plattform setzen Nutzer einem erhöhten Betrugsrisiko aus, da kein Käuferschutz greift.",
                        "Gefälschte Shops können persönliche Daten und Zahlungsinformationen abgreifen oder Schadsoftware verbreiten.",
                        "Die Weitergabe von Zahlungsinformationen über unsichere Kanäle wie E-Mail oder Telefon kann zum Datenmissbrauch führen.",
                        "Phishing-Links in Nachrichten können Schadsoftware installieren oder Daten abgreifen."
                    ],
                    "barrieren": "Attraktive Angebote und direkte Zahlungsaufforderungen schaffen Vertrauen, das Betrüger gezielt ausnutzen. Viele Nutzer sind sich der Gefahren durch unsichere Shops oder Links nicht bewusst. Mit den folgenden Empfehlungen können Sie sich vor diesen Bedrohungen schützen.",
                    "empfehlungen": {
                        "Nutzen Sie die Plattform-Zahlungsmethoden": "Nutzen Sie die Plattform-Zahlungsmethoden: Führen Sie Zahlungen ausschließlich über die offiziellen Zahlungsmethoden der Plattform durch, um von Käuferschutz und Sicherheit zu profitieren.",
                        "Überprüfen Sie Online-Shops sorgfältig": "Überprüfen Sie Online-Shops sorgfältig: Prüfen Sie die URL des Shops auf Rechtschreibfehler oder ungewöhnliche Domain-Endungen. Achten Sie darauf, dass die Seite mit „https“ beginnt und ein Schlosssymbol in der Adressleiste angezeigt wird.",
                        "Klicken Sie keine verdächtigen Links an": "Klicken Sie keine verdächtigen Links an: Öffnen Sie Links zu Shops nur, wenn Sie sicher sind, dass sie aus einer vertrauenswürdigen Quelle stammen.",
                        "Geben Sie keine Zahlungsinformationen über unsichere Kanäle weiter": "Geben Sie keine Zahlungsinformationen über unsichere Kanäle weiter: Vermeiden Sie die Weitergabe von Kreditkartendaten, Bankverbindungen oder anderen Zahlungsinformationen per E-Mail, Telefon oder Nachricht.",
                        "Nutzen Sie sichere Zahlungsmethoden": "Nutzen Sie sichere Zahlungsmethoden: Verwenden Sie Dienste wie PayPal oder Kreditkarten mit Käuferschutz, um Ihre Zahlungen abzusichern.",
                        "Seien Sie skeptisch bei außergewöhnlich günstigen Angeboten":"Seien Sie skeptisch bei außergewöhnlich günstigen Angeboten: Wenn ein Angebot zu gut klingt, um wahr zu sein, ist es wahrscheinlich betrügerisch.",
                        "Speichern Sie keine Zahlungsdaten":"Speichern Sie keine Zahlungsdaten: Verzichten Sie darauf, Ihre Zahlungsinformationen auf Online-Shop-Seiten zu speichern, um deren Missbrauch zu verhindern.",
                        "Überprüfen Sie Bewertungen":"Überprüfen Sie Bewertungen: Recherchieren Sie die Reputation eines Online-Shops oder Verkäufers, bevor Sie dort einkaufen."
                    },
                    "umsetzung": {
                        "Käufe in Onlineshops": [
                            "Wenn Sie sich bei einem Onlineshop nicht sicher sind, ob dieser seriös ist, prüfen Sie die Zahlungsmöglichkeiten des Shops. Wenn Ihnen nur die Möglichkeit der Vorauszahlung angeboten wird, könnte dies ein Anzeichen sein, dass der Shop nicht vertrauenswürdig ist. Prüfen Sie zudem auch immer das Impressum der Seite und prüfen Sie ausschließlich positive Bewertungen des Shops kritisch.",
                            "Wenn Sie online etwas Einkaufen, speichern Sie nach der Eingabe Ihre Zahlungsinformationen diese nicht dauerhaft. Geben Sie diese jedesmal händisch ein."
                        ]
                    }
                },
                "Netzwerk und Verschlüsselung": {
                    "kontext": "Die Nutzung öffentlicher WLAN-Hotspots ohne Schutzmaßnahmen birgt das Risiko, dass Angreifer Aktivitäten wie den Kauf- und Verkaufsprozess überwachen und Zugangsdaten abgreifen oder manipulieren. Unsichere Verbindungen erhöhen die Gefahr, dass Aktivitäten, persönliche Informationen und Zugangsdaten eingesehen oder missbraucht werden. Öffentliche WLAN-Hotspots sind häufig ungesichert und erlauben es Angreifern, sich unbemerkt in die Kommunikation zwischen Nutzern und Online-Plattformen einzuschalten. Dabei können sie nicht nur Zugangsdaten und persönliche Informationen abgreifen, sondern auch Transaktionen manipulieren. Unsichere Verbindungen, die keine ausreichende Verschlüsselung nutzen, bieten ähnliche Angriffsmöglichkeiten, wodurch sensible Daten kompromittiert werden können. Laut einer Studie aus dem Jahr 2024 wurden etwa 50 % der Angriffe auf Online-Shopper durch die Nutzung öffentlicher Netzwerke oder ungesicherter Verbindungen ermöglicht. ",
                    "beispiel": "Eine unsichere Verbindung erlaubt es einem Angreifer, Ihre Zahlungsdaten während einer Transaktion mitzulesen und zu manipulieren.",
                    "risiken": [
                        "Aktivitäten wie das Einloggen oder Bezahlen können über öffentliche WLAN-Hotspots abgegriffen werden.",
                        "Unsichere Verbindungen ermöglichen es Angreifern, persönliche Informationen und Zugangsdaten zu stehlen oder Transaktionen zu manipulieren.",
                        "Gestohlene Daten können für unbefugte Zugriffe oder Betrug genutzt werden."
                    ],
                    "barrieren": "Die Nutzung öffentlicher WLAN-Hotspots oder unsicherer Verbindungen scheint bequem, birgt jedoch erhebliche Risiken. Viele Nutzer unterschätzen die Gefahr, dass ihre Aktivitäten und Daten in solchen Netzwerken überwacht werden können. Die folgenden Empfehlungen helfen Ihnen, diese Risiken zu minimieren.",
                    "empfehlungen": {
                        "Vermeiden Sie öffentliche WLAN-Hotspots": "Vermeiden Sie öffentliche WLAN-Hotspots: Nutzen Sie öffentliche Netzwerke nur, wenn es unbedingt erforderlich ist und führen Sie keine sensiblen Aktivitäten wie Online-Käufe oder -Verkäufe durch.",
                        "Prüfen Sie die Sicherheit der Verbindung": "Prüfen Sie die Sicherheit der Verbindung: Überprüfen Sie, ob die URL des Online-Shops mit „https“ beginnt und ein Schlosssymbol in der Adressleiste vorhanden ist.",
                        "Vermeiden Sie unsichere Verbindungen": "Vermeiden Sie unsichere Verbindungen: Nutzen Sie nur bekannte und sichere Netzwerke, insbesondere bei sensiblen Transaktionen.",
                        "Melden Sie sich ab": "Melden Sie sich ab: Loggen Sie sich nach jeder Transaktion aus Ihrem Online-Shop-Konto aus, um unbefugten Zugriff zu verhindern.",
                        "Löschen Sie Cookies regelmäßig": "Löschen Sie Cookies regelmäßig: Vermeiden Sie das Speichern von Sitzungsdaten, indem Sie Cookies nach jeder Sitzung löschen oder Browser-Erweiterungen verwenden, um Tracking zu minimieren.",
                        "Nutzen Sie sichere Zahlungsmethoden:": "Nutzen Sie sichere Zahlungsmethoden: Bevorzugen Sie Zahlungsmethoden mit integriertem Schutz, wie PayPal oder Kreditkarten mit Zwei-Faktor-Authentifizierung.",
                        "Seien Sie vorsichtig bei ungewöhnlichen Aktivitäten":"Seien Sie vorsichtig bei ungewöhnlichen Aktivitäten: Wenn Sie verdächtige Änderungen an Ihrem Konto bemerken, informieren Sie sofort die Plattform und Ihre Bank."
                    },
                    "umsetzung": {
                        "Microsoft Edge": [
                            "Achten Sie auf eine sichere Verbindung, wenn Sie den Browser nutzen. Prüfen Sie hierfür in der URL-Leiste das Schlosssymbol vor der URL des Onlineshop. Zudem zeigt 'https' an, dass die Verbindung sicher verschlüsselt ist und somit ein Angreifer Ihre Zahlungsinformationen nicht ohne Weiteres abgreifen kann.",
                            "Öffnen Sie über die drei Punkte oben rechts die Einstellungen. Gehen Sie auf 'Cookies und Websiteberechtigungen' und gehen Sie unter 'Cookies und gespeicherte Daten' auf 'Verwalten und Löschen von Cookies und Websitedaten'. Aktivieren Sie die Option 'Cookies von Drittanbietern blockieren', um Webseiten zu untersagen, Ihre Aktivitäten im Web nachzuverfolgen."
                        ],

                        "Google Chrome":[
                            "Achten Sie auf eine sichere Verbindung, wenn Sie den Browser nutzen. Prüfen Sie hierfür in der URL-Leiste das Schlosssymbol vor der URL des Onlineshop. Zudem zeigt 'https' an, dass die Verbindung sicher verschlüsselt ist und somit ein Angreifer Ihre Zahlungsinformationen nicht ohne Weiteres abgreifen kann.",
                            "Öffnen Sie über die drei Punkte oben rechts die Einstellungen. Wählen Sie 'Datenschutz und Sicherheit'  aus und aktivieren Sie unter 'Drittanbieter-Cookies' die Option 'Drittanbieter-Cookies blockieren', um Webseiten daran zu hindern, Ihre Aktivitäten im Web zu verfolgen."
                        ],
                        "Safari":[
                            "Achten Sie auf eine sichere Verbindungen, wenn Sie den Browser nutzen. Prüfen Sie hierfür in der URL-Leiste das Schlosssymbol vor der URL des Onlineshop. Zudem zeigt 'https' an, dass die Verbindung sicher verschlüsselt ist und somit ein Angreifer Ihre Zahlungsinformationen nicht ohne Weiteres abgreifen kann.",
                            "Öffnen Sie die Einstellungen und wählen Sie 'Datenschutz' aus. Aktivieren Sie 'Websites daran hindern, Cross-Site-Tracking durchzuführen', um Webseiten daran zu hindern, Ihre Aktivitäten im Web zu verfolgen."
                        ]

                    }
                }    
                    
            }
        },

    
    "Smartphone und Tablet": {
        "bedrohung": {
            "Social Engineering - Phishing": {
                "kontext": "Beim Online-Handel besteht die Gefahr, dass Zahlungen außerhalb der Plattform erfolgen, wodurch der Käuferschutz nicht greift und Sie Betrügern ausgesetzt sein können. Unsichere oder gefälschte Online-Shops können persönliche Daten abgreifen oder Schadsoftware auf Ihr Gerät laden. Das Anklicken von Links in gefälschten oder unsicheren Shops birgt ähnliche Risiken. Zahlungsinformationen sollten niemals per E-Mail, Telefon oder Nachricht weitergegeben werden, da Angreifer sie für Betrug oder Identitätsdiebstahl nutzen könnten. Plattformen für Online-Handel bieten oft Schutzmechanismen wie Käuferschutz oder sichere Zahlungsmethoden. Zahlungen außerhalb dieser Systeme setzen Käufer und Verkäufer jedoch einem hohen Risiko aus. Gefälschte Online-Shops oder unsichere Webseiten versuchen, Nutzer zu täuschen, indem sie attraktive Angebote präsentieren, die persönliche Daten oder Zahlungsinformationen abgreifen sollen. Zudem sind Phishing-Links in Nachrichten oder E-Mails eine häufig genutzte Methode, um Malware zu verbreiten oder Daten zu stehlen. Im Jahr 2024 berichteten 45 % der Online-Käufer, dass sie mindestens einmal auf einen gefälschten Online-Shop hereingefallen sind oder Opfer von Zahlungsbetrug wurden. ",
                    "beispiel": "Eine gefälschte Shop-Seite lockt Sie mit unschlagbaren Angeboten und stiehlt Ihre Zahlungsinformationen beim Checkout.",
                    "risiken": [
                        "Zahlungen außerhalb der Plattform setzen Nutzer einem erhöhten Betrugsrisiko aus, da kein Käuferschutz greift.",
                        "Gefälschte Shops können persönliche Daten und Zahlungsinformationen abgreifen oder Schadsoftware verbreiten.",
                        "Die Weitergabe von Zahlungsinformationen über unsichere Kanäle wie E-Mail oder Telefon kann zum Datenmissbrauch führen.",
                        "Phishing-Links in Nachrichten können Schadsoftware installieren oder Daten abgreifen."
                    ],
                    "barrieren": "Attraktive Angebote und direkte Zahlungsaufforderungen schaffen Vertrauen, das Betrüger gezielt ausnutzen. Viele Nutzer sind sich der Gefahren durch unsichere Shops oder Links nicht bewusst. Mit den folgenden Empfehlungen können Sie sich vor diesen Bedrohungen schützen.",
                    "empfehlungen": {
                        "Nutzen Sie die Plattform-Zahlungsmethoden": "Nutzen Sie die Plattform-Zahlungsmethoden: Führen Sie Zahlungen ausschließlich über die offiziellen Zahlungsmethoden der Plattform durch, um von Käuferschutz und Sicherheit zu profitieren.",
                        "Überprüfen Sie Online-Shops sorgfältig": "Überprüfen Sie Online-Shops sorgfältig: Prüfen Sie die URL des Shops auf Rechtschreibfehler oder ungewöhnliche Domain-Endungen. Achten Sie darauf, dass die Seite mit „https“ beginnt und ein Schlosssymbol in der Adressleiste angezeigt wird.",
                        "Klicken Sie keine verdächtigen Links an": "Klicken Sie keine verdächtigen Links an: Öffnen Sie Links zu Shops nur, wenn Sie sicher sind, dass sie aus einer vertrauenswürdigen Quelle stammen.",
                        "Geben Sie keine Zahlungsinformationen über unsichere Kanäle weiter": "Geben Sie keine Zahlungsinformationen über unsichere Kanäle weiter: Vermeiden Sie die Weitergabe von Kreditkartendaten, Bankverbindungen oder anderen Zahlungsinformationen per E-Mail, Telefon oder Nachricht.",
                        "Nutzen Sie sichere Zahlungsmethoden": "Nutzen Sie sichere Zahlungsmethoden: Verwenden Sie Dienste wie PayPal oder Kreditkarten mit Käuferschutz, um Ihre Zahlungen abzusichern.",
                        "Seien Sie skeptisch bei außergewöhnlich günstigen Angeboten":"Seien Sie skeptisch bei außergewöhnlich günstigen Angeboten: Wenn ein Angebot zu gut klingt, um wahr zu sein, ist es wahrscheinlich betrügerisch.",
                        "Speichern Sie keine Zahlungsdaten":"Speichern Sie keine Zahlungsdaten: Verzichten Sie darauf, Ihre Zahlungsinformationen auf Online-Shop-Seiten zu speichern, um deren Missbrauch zu verhindern.",
                        "Überprüfen Sie Bewertungen":"Überprüfen Sie Bewertungen: Recherchieren Sie die Reputation eines Online-Shops oder Verkäufers, bevor Sie dort einkaufen."
                    },
                    "umsetzung": {
                        "Käufe in Onlineshops": [
                            "Wenn Sie sich bei einem Onlineshop nicht sicher sind, ob dieser seriös ist, prüfen Sie die Zahlungsmöglichkeiten des Shops. Wenn Ihnen nur die Möglichkeit der Vorauszahlung angeboten wird, könnte dies darauf hinweisen, dass der Shop nicht vertrauenswürdig ist. Prüfen Sie zudem immer das Impressum der Seite und betrachten Sie Bewertungen des Shops kritisch, auch wenn diese positiv sind.",
                            "Wenn Sie online etwas Einkaufen, dann speicher Sie nach der Eingabe Ihrerzahlungsinformationen diese nicht dauerhaft in dem Onlineshop ab. Geben Sie diese jedesmal händisch ein."
                        ]
                }
            },
            "Netzwerk und Verschlüsselung": {
                    "kontext": "Die Nutzung öffentlicher WLAN-Hotspots ohne Schutzmaßnahmen birgt das Risiko, dass Angreifer Aktivitäten wie den Kauf- und Verkaufsprozess überwachen und Zugangsdaten abgreifen oder manipulieren. Unsichere Verbindungen erhöhen die Gefahr, dass Aktivitäten, persönliche Informationen und Zugangsdaten eingesehen und missbraucht werden. Öffentliche WLAN-Hotspots sind oft ungesichert und erlauben es Angreifern, sich unbemerkt in die Kommunikation zwischen Nutzern und Online-Plattformen einzuschalten. Dabei können sie nicht nur Zugangsdaten und persönliche Informationen abgreifen, sondern auch Transaktionen manipulieren. Unsichere Verbindungen, die keine ausreichende Verschlüsselung nutzen, bieten ähnliche Angriffsmöglichkeiten, wodurch sensible Daten kompromittiert werden können. Laut einer Studie aus dem Jahr 2024 wurden etwa 50 % der Angriffe auf Online-Shopper durch die Nutzung öffentlicher Netzwerke oder ungesicherter Verbindungen ermöglicht. ",
                    "beispiel": "Eine unsichere Verbindung erlaubt es einem Angreifer, Ihre Zahlungsdaten während einer Transaktion mitzulesen und zu manipulieren.",
                    "risiken": [
                        "Aktivitäten wie das Einloggen oder Bezahlen können über öffentliche WLAN-Hotspots abgegriffen werden.",
                        "Unsichere Verbindungen ermöglichen es Angreifern, persönliche Informationen und Zugangsdaten zu stehlen oder Transaktionen zu manipulieren.",
                        "Gestohlene Daten können für unbefugte Zugriffe oder Betrug genutzt werden."
                    ],
                    "barrieren": "Die Nutzung öffentlicher WLAN-Hotspots oder unsicherer Verbindungen scheint bequem, birgt jedoch erhebliche Risiken. Viele Nutzer unterschätzen das Risiko, dass ihre Aktivitäten und Daten in solchen Netzwerken überwacht werden können. Die folgenden Empfehlungen helfen Ihnen, diese Risiken zu minimieren.",
                    "empfehlungen": {
                        "Vermeiden Sie öffentliche WLAN-Hotspots": "Vermeiden Sie öffentliche WLAN-Hotspots: Nutzen Sie öffentliche Netzwerke nur, wenn es unbedingt erforderlich ist und führen Sie keine sensiblen Aktivitäten wie Online-Käufe oder -Verkäufe durch.",
                        "Prüfen Sie die Sicherheit der Verbindung": "Prüfen Sie die Sicherheit der Verbindung: Überprüfen Sie, ob die URL des Online-Shops mit „https“ beginnt und ein Schlosssymbol in der Adressleiste vorhanden ist.",
                        "Vermeiden Sie unsichere Verbindungen": "Vermeiden Sie unsichere Verbindungen: Nutzen Sie nur bekannte und sichere Netzwerke, insbesondere bei sensiblen Transaktionen.",
                        "Melden Sie sich ab": "Melden Sie sich ab: Loggen Sie sich nach jeder Transaktion aus Ihrem Online-Shop-Konto aus, um unbefugten Zugriff zu verhindern.",
                        "Löschen Sie Cookies regelmäßig": "Löschen Sie Cookies regelmäßig: Vermeiden Sie das Speichern von Sitzungsdaten, indem Sie Cookies nach jeder Sitzung löschen oder Browser-Erweiterungen verwenden, die Tracking minimieren.",
                        "Nutzen Sie sichere Zahlungsmethoden:": "Nutzen Sie sichere Zahlungsmethoden: Bevorzugen Sie Zahlungsmethoden mit integriertem Schutz, wie PayPal oder Kreditkarten mit Zwei-Faktor-Authentifizierung.",
                        "Seien Sie vorsichtig bei ungewöhnlichen Aktivitäten":"Seien Sie vorsichtig bei ungewöhnlichen Aktivitäten: Wenn Sie verdächtige Änderungen an Ihrem Konto bemerken, informieren Sie sofort die Plattform und Ihre Bank."
                    },
                    "umsetzung": {
                        "Käufe in Onlineshops über den Browser": [
                            "Überprüfen Sie das Schlosssymbol in der URL-Leiste, um sicherzustellen, dass die Verbindung verschlüsselt ist. Überprüfen Sie zusätzlich, ob die URL der Webseite mit 'https' beginnt. Somit ist es Angreifern nicht ohne Weiteres möglich, Ihre Zugangs- oder Bezahldaten einzusehen.",
                            "Vermeiden Sie Online-Käufe, wenn Sie mit einem öffentlichen WLAN-Hotspot verbunden sind. Diese sind oft unverschlüsselt oder nur schwach verschlüsselt. Dies kann dazu führen, dass Angreifer Ihre Zugangs- und Zahlungsdaten abgreifen könnten. Wenn Sie öffentliche WLAN-Hotspots nutzen müssen, verwenden Sie ein Virtual Private Network (VPN), um Ihre Daten zu schützen."
                        ],
                        "Käufe in Onlineshops über Apps": [
                            "Laden Sie Apps von Onlineshops ausschließlich über den offiziellen Appstore Ihres Gerätes herunter. Vermeiden Sie das Herunterladen von Apps außerhalb des offiziellen Appstores, da diese nicht überprüft werden und möglicherweise Schadsoftware enthalten.",
                            "Vermeiden Sie Online-Käufe, wenn Sie mit einem öffentlichen WLAN-Hotspot verbunden sind. Diese sind oft unverschlüsselt oder nur schwach verschlüsselt. Dies kann dazu führen, dass Angreifer Ihre Zugangs- und Zahlungsdaten abgreifen könnten. Wenn Sie öffentliche WLAN-Hotspots nutzen müssen, verwenden Sie ein Virtual Private Network (VPN), um Ihre Daten zu schützen."
                        ]
                    }
                }
        }
    }
}







}

    


    


        


# Logik für dynamische Empfehlungen
def generate_recommendations(activity, device, implemented_measures):
    # Hole die Daten für die gewählte Aktivität und das Gerät
    data = recommendation_data.get(activity, {}).get(device, {})
    bedrohungen = data.get("bedrohung", {})

    # Dynamisches Mapping von Maßnahmen zu Empfehlungen
    dynamic_mapping = {}
    for bedrohung in bedrohungen.values():
        for measure, recommendation in bedrohung.get("empfehlungen", {}).items():
            dynamic_mapping[measure] = recommendation

    # Filtere `implemented_measures` für die aktuelle Aktivität und das Gerät
    relevant_measures = set(dynamic_mapping.keys())
    filtered_measures = [measure for measure in implemented_measures if measure in relevant_measures]

    # Bereite die Bedrohungen und deren Inhalte auf
    formatted_bedrohungen = {}
    for bedrohung_name, details in bedrohungen.items():
        fehlende_empfehlungen = [
            recommendation for measure, recommendation in details.get("empfehlungen", {}).items()
            if measure not in filtered_measures
        ]

        formatted_bedrohungen[bedrohung_name] = {
            "kontext": details.get("kontext", ""),
            "beispiel": details.get("beispiel", ""),
            "risiken": details.get("risiken", []),
            "barrieren": details.get("barrieren", ""),
            "empfehlungen": fehlende_empfehlungen,
            "umsetzung": details.get("umsetzung", {})
        }

    return {
        "bedrohungen": formatted_bedrohungen,
        "message": (
            "Herzlichen Glückwunsch! Sie haben bereits alle empfohlenen Maßnahmen umgesetzt."
            if not any(b["empfehlungen"] for b in formatted_bedrohungen.values())
            else ""
        )
    }






@app.route("/")
def index():
    return render_template("index.html")


@app.route("/questions", methods=["GET", "POST"])
def questions():
    activity = request.args.get("activity", "")
    device = request.args.get("device", "")
    return render_template("questions.html", activity=activity, device=device)



@app.route("/recommendations", methods=["POST"])
def recommendations():
    activity = request.form.get("activity")
    device = request.form.get("device")
    implemented_measures = request.form.getlist("measures")

    result = generate_recommendations(activity, device, implemented_measures)

    return render_template(
        "recommendations.html",
        bedrohungen=result["bedrohungen"],
        message=result["message"]
    )




if __name__ == "__main__":
    app.run(debug=True)
