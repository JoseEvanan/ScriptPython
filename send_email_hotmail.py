import email
import smtplib

msg = email.message_from_string('warning')
msg['From'] = "noreply@kiwilex.biz"
msg['To'] = "jose.evanan@gmail.com"
msg['Subject'] = "Holiii"

s = smtplib.SMTP("smtp.office365.com",587)
s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
s.starttls() #Puts connection to SMTP server in TLS mode
s.ehlo()
s.login('noreply@kiwilex.biz', 'K1w1R0b0t_')

s.sendmail("noreply@kiwilex.biz", "jose.evanan@gmail.com", msg.as_string())

s.quit()