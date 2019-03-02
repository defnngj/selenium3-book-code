import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 邮件主题
subject = 'Python send email test'
# 发送的附件
with open('log.txt', 'rb') as f:
    send_att = f.read()

att = MIMEText(send_att, 'text', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="log.txt"'

msg = MIMEMultipart()
msg['Subject'] = subject
msg.attach(att)

smtp = smtplib.SMTP()
smtp.connect("smtp.126.com")
smtp.login("sender@126.com", "a123456")
smtp.sendmail("sender@126.com", "receiver@126.com", msg.as_string())
smtp.quit()
