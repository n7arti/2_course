from imaplib import IMAP4_SSL

HOST = '127.0.0.1'
PORT = 50007
admin_mail = 'admin@amail.adm'
admin_pass = 'admin_password'
PERIOD_CHECK = 60
with IMAP4_SSL(HOST, PORT) as M:
    rc, resp = M.login(admin_mail, admin_pass)
    while True:
        M.select()
        typ, data = M.search(None, 'ALL')
        for num in data[0].split():
            typ, data = M.fetch(num, '(RFC822)')
            ID = data[0][1]
            text = data[0][2]
            with open("ID.txt", "r") as file:
                INFO = [int(line) for line in file]
            if ID in INFO:
                log = open("success_request.log", "a")
            else:
                log = open("error_request.log", "a")
            log.write("%s: %s\n" % (ID, text))
            log.close()
    sleep(PERIOD_CHECK)
