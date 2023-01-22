import os
from twilio.rest import Client

TWILIO_SID = "AC6aca28f106772e6f4a909358a22a1a0f"
TWILIO_AT = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUM = "+17652689798"
print(TWILIO_SID,'---', TWILIO_AT)


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, message):
        self.message = f"Price: {message[0]}\nDeparture: {message[1]}\nArrival: {message[2]}"
        client = Client(TWILIO_SID, TWILIO_AT)
        message = client.messages.create(
            body=self.message,
            from_=TWILIO_NUM,
            to="+917970940623"
        )
        print(message.sid)
