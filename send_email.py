import smtplib, ssl  # standard email library

host = 'smtp.gmail.com'   #default gmail host
port = 465       #default gmail port
subject= "Email subject"
username = 'fyznitch@gmail.com'
password = 'xxhndnakhwcmkzrs'
recipient = "fyznitch@gmail.com"
message = f"""\
Subject: {subject}
df sdkhjdlgf sdgfksdgj sdgkldgjf dfgdfgkljdf gdfgkjdf g
dsjfkds gdfkgjd fgjdklgfj dlfgjdfkg dfgkjdf gdfjgdlgf jdfg
jdsfgkl dsgjfkldjgflkdgjf dlkgjkdlg jdlkgj dlgfj dlkgjdfgj 
dfjg dfkgjdlfgjdklgj dlkgjf ldkgjflkdgjfldkgjf dfjgdlfg j
dfgj ldkgjf kdlgjfkl djgfkldjfglkdgjf lkdjfgkldjfgkljdkg d
"""
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, recipient, message)
