import poplib
mailServer = 'pop.gmail.com'
emailID = ''    #Enter your Email Id here
emailPass = ''  #Enter Your Password here

lines=[]

myEmailConnection = poplib.POP3_SSL(mailServer)
print(myEmailConnection.getwelcome())
myEmailConnection.user(emailID)
myEmailConnection.pass_(emailPass)
EmailInformation = myEmailConnection.stat()
print("Number of new emails: %s (%s bytes)" % EmailInformation)

print("\n=====================\nReading All Emails\n=====================\n")

## Read all emails
for i in range(EmailInformation[0]):
    for email in myEmailConnection.retr(i+1)[1]:
        lines.append(str(email))
    print('\nEmail Number '+str(i+1))
    print(lines[1][2:-1])
    print(lines[4][2:-1])
    print(lines[3][2:-1])
    print('Message:')
    for i in lines[11:-7]:
        print(i[2:-1])
    lines.clear()
