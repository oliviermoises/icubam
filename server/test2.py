import email

from imapclient import IMAPClient
from decouple import config

server = config("server")
user = config("user")
password = config("password")

with IMAPClient(server) as server:
    server.login(user, password)
    server.select_folder("INBOX", readonly=True)

    messages = server.search("UNSEEN")
    for uid, message_data in server.fetch(messages, "RFC822").items():
        email_message = email.message_from_bytes(message_data[b"RFC822"])
        print(uid, email_message.get("From"), email_message.get("Subject"))
        if email_message.is_multipart:
            for payload in email_message.get_payload():
                print(payload.get_payload())
        else:
            print(email_message.get_payload())
        print("--------------------")
    server.logout()
