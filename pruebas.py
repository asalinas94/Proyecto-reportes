from O365 import Message
import smtplib

sendto = 'allan.salinas.ramirez@gmail.com'
user = 'allan.salinas.ramirez@gmail.com'

password = 'Reflektor94'
smtpsrv = 'smtp.gmail.com'
smtpserver = smtplib.SMTP(smtpsrv,587)


smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(user,password)
header = 'Correo de prueba'
print header
msgbody = header + 'n This is a test Email send using Python nn'

smtpserver.sendmail(user, sendto, msgbody)

print 'done!'
smtpserver.close()

#o365_auth = ('asalinas@realnet.com.mx','')
#m = Message(auth=o365_auth)
#m.setRecipients('asalinas@realnet.com.mx')
#m.setSubject('Prueba de Python')
#m.setBody('Hola amigo.')
#m.sendMessage()
