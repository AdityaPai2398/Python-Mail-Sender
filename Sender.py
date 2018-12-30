import smtplib
from email.mime.text import MIMEText
import config
server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

EMAIL=config.EMAIL
PASSWORD=config.PASSWORD
server.login(EMAIL,PASSWORD)

message=MIMEText("Sent from py")
message["From"]=EMAIL
message["To"]=EMAIL
message["Subject"]="Hellow WOrld"


server.sendmail(EMAIL,EMAIL,message.as_string())

print("Mail is successfully sent")
