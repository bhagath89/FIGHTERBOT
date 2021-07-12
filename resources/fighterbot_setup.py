from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details
For TeleBot"""
)
print("")

APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    tele = client.send_message("me", client.session.save())
    tele.reply(
        "The above is the `STRING_SESSION` for your current session."
    )
    print("")
    print(
        "Below is the STRING_SESSION. You can also find it in your Telegram Saved Messages."
    )
    print("")
    print("")
    print(client.session.save())
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
