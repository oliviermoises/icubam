from decouple import config
from imaplib import IMAP4_SSL as IMAP
from socket import gaierror

server = config("server")
user = config("user")
password = config("password")



try:
    conn = IMAP(server)
    conn.login(user, password)
    conn.select()


    ret, data = conn.uid('search', None, '(UNSEEN)')
    if ret == 'OK':
        uids = data[0].split()
    for uid in uids:
        print (uid)
    # for uid in uids:
    #     ret, data = conn.uid('fetch', uid, '(BODY[TEXT])')
    #     if ret == 'OK':
    #         body = data[0][1]
    #         print (body)

except gaierror as e:
    # Le serveur IMAP est erroné ou injoignable
    print ('gaierror')
    print (e)
except IMAP.error as e:
    # Problème d'identification !
    # L'utilisateur et mot de passe sont-ils corrects ?
    print ('IMAP ERROR')
    print (e)
