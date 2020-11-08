from decouple import config
from imaplib import IMAP4_SSL as IMAP
from socket import gaierror
import codecs


server = config("server")
user = config("user")
password = config("password")


try:
    imap_client = IMAP(server)
    imap_client.login(user, password)
    imap_client.select()
    typ, data = imap_client.list()

    for m in data:
        print (m)
        mailbox = (
            codecs.decode(m.replace(b"&", b"+"), "utf-7")
            .split("\"/\"")[-1]
            .replace('"', "")
        )
        print(mailbox)

    # ret, data = imap_client.uid("search", None, "(UNSEEN)")
    # if ret == "OK":
    #     uids = data[0].split()
    # for uid in uids:
    #     print(uid)
    # for uid in uids:
    #     ret, data = imap_client.uid('fetch', uid, '(BODY[TEXT])')
    #     if ret == 'OK':
    #         body = data[0][1]
    #         print (body)
    imap_client.close()

except gaierror as e:
    # Le serveur IMAP est erroné ou injoignable
    print("gaierror")
    print(e)
except IMAP.error as e:
    # Problème d'identification !
    # L'utilisateur et mot de passe sont-ils corrects ?
    print("IMAP ERROR")
    print(e)
finally:
    imap_client.logout()
