i mport smtplib

sender = 'designinfo@dcemail.com'
receivers = ['kovalewskiy@gmail.com']

message = "This is a test e-mail message."

smtpObj = smtplib.SMTP('localhost', 25	)
smtpObj.ehlo()
# smtpObj.starttls()
smtpObj.login("kiko", "123")
smtpObj.sendmail(sender, receivers, message)
# smtpObj.close()
print "Successfully sent email"



# smtpObj = smtplib.SMTP('smtp.dcemail.com', 587)
# smtpObj.ehlo()
# smtpObj.starttls()
# smtpObj.login("designinfo@dcemail.com", "DesignInfo(4)")
# smtpObj.sendmail(sender, receivers, message)
# smtpObj.close()
# print "Successfully sent email"

# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# smtpObj.ehlo()
# smtpObj.starttls()
# smtpObj.login("kovalewskiy@gmail.com", "")
# smtpObj.sendmail(sender, receivers, message)
# smtpObj.close()
# print "Successfully sent email"
