import smtplib
from decouple import config


user = config("user")
password = config("password")


sent_from = user
to = ["olivier@moises.fr"]
subject = "OMG Super Important Message"
body = "Hey, what's up?\n\n- You"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (
    sent_from,
    ", ".join(to),
    subject,
    body,
)

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print("Email sent!")
except:
    print("Something went wrong...")
